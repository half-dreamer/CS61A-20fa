import logging
import os
import requests

from client.utils.printer import print_error, print_success

log = logging.getLogger(__name__)

VERSION_ENDPOINT = 'https://{server}/api/v3/version/ok-client'

SHORT_TIMEOUT = 15  # seconds

def check_version(server, version, filename, timeout=SHORT_TIMEOUT):
    """Check for the latest version of OK and update accordingly."""

    address = VERSION_ENDPOINT.format(server=server)

    log.info('Checking for software updates...')
    log.info('Existing OK version: %s', version)
    log.info('Checking latest version from %s', address)

    try:
        response = requests.get(address, timeout=timeout)
        response.raise_for_status()
    except (requests.exceptions.RequestException, requests.exceptions.BaseHTTPError) as e:
        print_error('Network error when checking for updates.')
        log.warning('Network error when checking version from %s: %s', address,
                    str(e), stack_info=True)
        return False

    response_json = response.json()
    if not _validate_api_response(response_json):
        print_error('Error while checking updates: malformed server response')
        log.info('Malformed response from %s: %s', address, response.text)
        return False

    current_version = response_json['data']['results'][0]['current_version']
    if current_version == version:
        print_success('OK is up to date')
        return True

    download_link = response_json['data']['results'][0]['download_link']

    log.info('Downloading version %s from %s', current_version, download_link)

    try:
        response = requests.get(download_link, timeout=timeout)
        response.raise_for_status()
    except (requests.exceptions.RequestException, requests.exceptions.BaseHTTPError) as e:
        print_error('Error when downloading new version of OK')
        log.warning('Error when downloading new version of OK: %s', str(e),
                    stack_info=True)
        return False

    log.info('Writing new version to %s', filename)

    zip_binary = response.content
    try:
        _write_zip(filename, zip_binary)
    except IOError as e:
        print_error('Error when downloading new version of OK')
        log.warning('Error writing to %s: %s', filename, str(e))
        return False
    else:
        print_success('Updated to version: {}'.format(current_version))
        log.info('Successfully wrote to %s', filename)
        return True

def _validate_api_response(data):
    return isinstance(data, dict) and \
           'data' in data and \
           isinstance(data['data'], dict) and \
           'results' in data['data'] and \
           isinstance(data['data']['results'], list) and \
           len(data['data']['results']) > 0 and \
           isinstance(data['data']['results'][0], dict) and \
           'current_version' in data['data']['results'][0] and \
           'download_link' in data['data']['results'][0]



def _write_zip(zip_name, zip_contents):
    with open(zip_name, 'wb') as f:
        f.write(zip_contents)
        os.fsync(f)
