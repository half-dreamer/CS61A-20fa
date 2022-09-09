import hashlib
import http.server
import os
import pickle
import requests
import time
from urllib.parse import urlencode, urlparse, parse_qsl
import webbrowser

from client.exceptions import AuthenticationException, OAuthException
from client.utils.config import (CONFIG_DIRECTORY, REFRESH_FILE,
                                 create_config_directory)
from client.utils import format, network

import logging
import traceback

log = logging.getLogger(__name__)

# The CLIENT_SECRET below is the secret for the ok-client app registered
# on the ok-server; the secret value can be found at:
# https://{root-url-for-your-ok-deployment}/admin/clients/ok-client
#
# In the case of the Google authentication provider, the client secret in an
# installed application isn't a secret so it can be checked in
# (see: https://developers.google.com/accounts/docs/OAuth2InstalledApp).
# However, for other authentication providers such as Azure Active Directory
# this might not be the case so it's also possible to configure the secret
# via an environment variable set in the Jupyter Notebook.
CLIENT_SECRET = os.getenv('OK_CLIENT_SECRET',
                          'EWKtcCp5nICeYgVyCPypjs3aLORqQ3H')

CLIENT_ID = 'ok-client'

OAUTH_SCOPE = 'all'

REFRESH_FILE = os.path.join(CONFIG_DIRECTORY, "auth_refresh")

REDIRECT_HOST = "127.0.0.1"
REDIRECT_PORT = 6165

TIMEOUT = 10

INFO_ENDPOINT = '/api/v3/user/'
AUTH_ENDPOINT =  '/oauth/authorize'
TOKEN_ENDPOINT = '/oauth/token'
ERROR_ENDPOINT = '/oauth/errors'

COPY_MESSAGE = """
Copy the following URL and open it in a web browser. To copy,
highlight the URL, right-click, and select "Copy".
""".strip()

NOTEBOOK_COPY_MESSAGE = "Open the following URL:"

NOTEBOOK_PASTE_MESSAGE = """After logging in, copy the code from the web page and paste it into the box.
Then press the "Enter" key on your keyboard."""

PASTE_MESSAGE = """
After logging in, copy the code from the web page, paste it below,
and press Enter. To paste, right-click and select "Paste".
""".strip()

HOSTNAME_ERROR_MESSAGE = """
Python couldn't recognize your computer's hostname because it contains
non-ASCII characters (e.g. Non-English characters or accent marks).

To fix, either upgrade Python to version 3.5.2+, or change your hostname.
""".strip()


def pick_free_port(hostname=REDIRECT_HOST, port=0):
    """ Try to bind a port. Default=0 selects a free port. """
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((hostname, port))  # port=0 finds an open port
    except OSError as e:
        log.warning("Could not bind to %s:%s %s", hostname, port, e)
        if port == 0:
            print('Unable to find an open port for authentication.')
            raise AuthenticationException(e)
        else:
            return pick_free_port(hostname, 0)
    addr, port = s.getsockname()
    s.close()
    return port

def make_token_post(server, data):
    """Try getting an access token from the server. If successful, returns the
    JSON response. If unsuccessful, raises an OAuthException.
    """
    try:
        response = requests.post(server + TOKEN_ENDPOINT, data=data, timeout=TIMEOUT)
        body = response.json()
    except Exception as e:
        log.warning('Other error when exchanging code', exc_info=True)
        raise OAuthException(
            error='Authentication Failed',
            error_description=str(e))
    if 'error' in body:
        log.error(body)
        raise OAuthException(
            error=body.get('error', 'Unknown Error'),
            error_description = body.get('error_description', ''))
    return body

def make_code_post(server, code, redirect_uri):
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri,
    }
    info = make_token_post(server, data)
    return info['access_token'], int(info['expires_in']), info['refresh_token']

def make_refresh_post(server, refresh_token):
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
    }
    info = make_token_post(server, data)
    return info['access_token'], int(info['expires_in'])

def get_storage():
    create_config_directory()
    with open(REFRESH_FILE, 'rb') as fp:
        storage = pickle.load(fp)

    access_token = storage['access_token']
    expires_at = storage['expires_at']
    refresh_token = storage['refresh_token']

    return access_token, expires_at, refresh_token


def update_storage(access_token, expires_in, refresh_token):
    if not (access_token and expires_in and refresh_token):
        raise AuthenticationException(
            "Authentication failed and returned an empty token.")

    cur_time = int(time.time())
    create_config_directory()
    with open(REFRESH_FILE, 'wb') as fp:
        pickle.dump({
            'access_token': access_token,
            'expires_at': cur_time + expires_in,
            'refresh_token': refresh_token
        }, fp)

def refresh_local_token(server):
    cur_time = int(time.time())
    access_token, expires_at, refresh_token = get_storage()
    if cur_time < expires_at - 10:
        return access_token
    access_token, expires_in = make_refresh_post(server, refresh_token)
    if not (access_token and expires_in):
        raise AuthenticationException(
            "Authentication failed and returned an empty token.")

    update_storage(access_token, expires_in, refresh_token)
    return access_token

def perform_oauth(code_fn, *args, **kwargs):
    try:
        access_token, expires_in, refresh_token = code_fn(*args, **kwargs)
    except UnicodeDecodeError as e:
        with format.block('-'):
            print("Authentication error\n:{}".format(HOSTNAME_ERROR_MESSAGE))
    except OAuthException as e:
        with format.block('-'):
            print("Authentication error: {}".format(e.error.replace('_', ' ')))
            if e.error_description:
                print(e.error_description)
    else:
        update_storage(access_token, expires_in, refresh_token)
        return access_token

def server_url(cmd_args):
    scheme = 'http' if cmd_args.insecure else 'https'
    return '{}://{}'.format(scheme, cmd_args.server)

def authenticate(cmd_args, endpoint='', force=False, nointeract=False):
    """Returns an OAuth token that can be passed to the server for
    identification. If FORCE is False, it will attempt to use a cached token
    or refresh the OAuth token. If NOINTERACT is true, it will return None
    rather than prompting the user.
    """
    server = server_url(cmd_args)
    network.check_ssl()
    access_token = None

    try:
        assert not force
        access_token = refresh_local_token(server)
    except Exception:
        if nointeract:
            return access_token
        print('Performing authentication')
        access_token = perform_oauth(get_code, cmd_args, endpoint)
        email = display_student_email(cmd_args, access_token)
        if not email:
            log.warning('Could not get login email. Try logging in again.')

    log.debug('Authenticated with access token={}'.format(access_token))

    return access_token

def notebook_authenticate(cmd_args, force=False, silent=True, nointeract=False):
    """ Similiar to authenticate but prints student emails after
    all calls and uses a different way to get codes. If SILENT is True,
    it will suppress the error message and redirect to FORCE=True
    """
    server = server_url(cmd_args)
    network.check_ssl()
    access_token = None
    if not force:
        try:
            access_token = refresh_local_token(server)
        except OAuthException as e:
            # Account for Invalid Grant Error During make_token_post
            if not silent:
                raise e
            return notebook_authenticate(cmd_args, force=True, silent=False)

    if nointeract:
        return None

    if not access_token:
        access_token = perform_oauth(
            get_code_via_terminal,
            cmd_args,
            copy_msg=NOTEBOOK_COPY_MESSAGE,
            paste_msg=NOTEBOOK_PASTE_MESSAGE)

    # Always display email
    email = display_student_email(cmd_args, access_token)
    if email is None and not force:
        return notebook_authenticate(cmd_args, force=True)  # Token has expired
    elif email is None:
        # Did not get a valid token even after a fresh login
        log.warning('Could not get login email. You may have been logged out. '
                    ' Try logging in again.')
    return access_token

def get_code(cmd_args, endpoint=''):
    if cmd_args.no_browser:
        return get_code_via_terminal(cmd_args)

    email = input("Please enter your school email (.edu): ")

    host_name = REDIRECT_HOST
    try:
        port_number = pick_free_port(port=REDIRECT_PORT)
    except AuthenticationException:
        # Could not bind to REDIRECT_HOST:0, try localhost instead
        host_name = 'localhost'
        port_number = pick_free_port(host_name, 0)

    redirect_uri = "http://{0}:{1}/".format(host_name, port_number)

    params = {
        'client_id': CLIENT_ID,
        'login_hint': email,
        'redirect_uri': redirect_uri,
        'response_type': 'code',
        'scope': OAUTH_SCOPE,
    }
    url = '{}{}?{}'.format(server_url(cmd_args), AUTH_ENDPOINT, urlencode(params))
    try:
        assert webbrowser.open_new(url)
        return get_code_via_browser(cmd_args, redirect_uri,
            host_name, port_number, endpoint)
    except Exception as e:
        log.debug('Error with Browser Auth:\n{}'.format(traceback.format_exc()))
        log.warning('Browser auth failed, falling back to browserless auth')
        return get_code_via_terminal(cmd_args, email)

def get_code_via_browser(cmd_args, redirect_uri, host_name, port_number, endpoint):
    server = server_url(cmd_args)
    code_response = None
    oauth_exception = None

    class CodeHandler(http.server.BaseHTTPRequestHandler):
        def send_redirect(self, location):
            self.send_response(302)
            self.send_header("Location", location)
            self.end_headers()

        def send_failure(self, oauth_exception):
            params = {
                'error': oauth_exception.error,
                'error_description': oauth_exception.error_description,
            }
            url = '{}{}?{}'.format(server, ERROR_ENDPOINT, urlencode(params))
            self.send_redirect(url)

        def do_GET(self):
            """Respond to the GET request made by the OAuth"""
            nonlocal code_response, oauth_exception
            log.debug('Received GET request for %s', self.path)
            path = urlparse(self.path)
            qs = {k: v for k, v in parse_qsl(path.query)}
            code = qs.get('code')
            if code:
                try:
                    code_response = make_code_post(server, code, redirect_uri)
                except OAuthException as e:
                    oauth_exception = e
            else:
                oauth_exception = OAuthException(
                    error=qs.get('error', 'Unknown Error'),
                    error_description = qs.get('error_description', ''))

            if oauth_exception:
                self.send_failure(oauth_exception)
            else:
                self.send_redirect('{}/{}'.format(server, endpoint))

        def log_message(self, format, *args):
            return

    server_address = (host_name, port_number)
    log.info("Authentication server running on {}:{}".format(host_name, port_number))

    try:
        httpd = http.server.HTTPServer(server_address, CodeHandler)
        httpd.handle_request()
    except OSError as e:
        log.warning("HTTP Server Err {}".format(server_address), exc_info=True)
        raise

    if oauth_exception:
        raise oauth_exception
    return code_response

def get_code_via_terminal(cmd_args, email=None,
                          copy_msg=COPY_MESSAGE, paste_msg=PASTE_MESSAGE):
    redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
    print()
    print(copy_msg)
    print()
    print('{}/client/login/'.format(server_url(cmd_args)))
    print()
    print(paste_msg)
    print()
    code = input('Paste your code here: ')
    return make_code_post(server_url(cmd_args), code, redirect_uri)

def get_info(cmd_args, access_token):
    response = requests.get(
        server_url(cmd_args) + INFO_ENDPOINT,
        headers={'Authorization': 'Bearer {}'.format(access_token)},
        timeout=5)
    response.raise_for_status()
    return response.json()['data']

def display_student_email(cmd_args, access_token):
    try:
        email = get_info(cmd_args, access_token)['email']
        print('Successfully logged in as', email)
        return email
    except Exception:  # Do not catch KeyboardInterrupts
        log.debug("Did not obtain email", exc_info=True)
        return None

def get_student_email(cmd_args, endpoint=''):
    """Attempts to get the student's email. Returns the email, or None."""
    log.info("Attempting to get student email")
    if cmd_args.local:
        return None
    access_token = authenticate(cmd_args, endpoint=endpoint, force=False)
    if not access_token:
        return None
    try:
        return get_info(cmd_args, access_token)['email']
    except IOError as e:
        return None

def get_identifier(cmd_args, endpoint=''):
    """ Obtain anonmyzied identifier."""
    student_email = get_student_email(cmd_args, endpoint)
    if not student_email:
        return "Unknown"
    return hashlib.md5(student_email.encode()).hexdigest()
