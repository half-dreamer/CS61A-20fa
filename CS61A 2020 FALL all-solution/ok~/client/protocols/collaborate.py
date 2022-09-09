from client.protocols.common import models
from client.protocols.grading import grade
from client.utils import network, output
from client.utils.firebase import pyrebase

import client
import requests

import os
import sys
import shutil

import logging
import platform
import time

import webbrowser

log = logging.getLogger(__name__)

from client.utils.printer import print_error, print_warning, print_success

class CollaborateProtocol(models.Protocol):

    # Timeouts are specified in seconds.
    LONG_TIMEOUT = 30
    FIREBASE_CONFIG = {
        'apiKey': "AIzaSyAFJn-q5SbxJnJcPVFhjxd25DA5Jusmd74",
        'authDomain': "ok-server.firebaseapp.com",
        'databaseURL': "https://ok-server.firebaseio.com",
        'storageBucket': "ok-server.appspot.com"
    }

    FILE_TIME_FORMAT = '%m_%d_%H_%M_%S'
    TIME_FORMAT = '%m/%d %H:%M:%S'
    BACKUP_DIRECTORY = 'ok-collab'
    COLLAB_SERVER = 'collab.cs61a.org'
    # COLLAB_SERVER = '127.0.0.1:8000'  # Dev Server

    def run(self, messages):
        if not self.args.collab:
            return
        elif self.args.local:
            log.info("Collaborate requires network access.")
            return

        if not messages.get('file_contents'):
            log.warning("Collaborate needs to be after file contents")
            return
        if not messages.get('analytics'):
            log.warning("Collaborate needs to be after analytics")
            return

        self.file_contents = messages.get('file_contents', {})
        self.collab_analytics = {'save': [], 'grade': []}
        messages['collaborate'] = self.collab_analytics

        self.collab_analytics['launch'] = time.strftime(self.TIME_FORMAT)

        try:
            print("Starting collaboration mode.")
            exit_val = self.start_firebase(messages)
            if exit_val is None:
                return
        except (Exception, KeyboardInterrupt, AttributeError, RuntimeError, OSError) as e:
            print("Exiting collaboration mode (Run with --debug if this was unexpected)")
            self.log_event('exit',  {'method': str(e)})

            if hasattr(self, 'stream') and self.stream:
                self.stream.close()
            if hasattr(self, 'presence'):
                (self.get_firebase()
                     .child('clients').child(self.presence['name'])
                    .remove(self.fire_user['idToken']))
            log.warning("Exception while waiting", exc_info=True)

    def start_firebase(self, messages):
        access_token = self.assignment.authenticate()
        email = self.assignment.get_student_email()
        identifier = self.assignment.get_identifier()

        firebase = pyrebase.initialize_app(self.FIREBASE_CONFIG)
        self.fire_auth = firebase.auth()
        self.fire_db = firebase.database()

        self.user_email = email
        self.hostname = platform.node()

        data = {
            'access_token': access_token,
            'email': email,
            'identifier': identifier,
            'assignment': self.assignment.endpoint,
            'file_contents': messages.get('file_contents'),
            'analytics': messages.get('analytics'),
        }

        # Check for existing sessions first - TBD Future
        # existing_sessions = self.send_messages(data, endpoint='/collab/list')
        # response = self.prompt_for_existing_session(existing_sessions.get('sessions'))
        # if response:
        #     data['desired_session'] = response

        # Send data to collaborate server
        response_data = self.send_messages(data, self.LONG_TIMEOUT)
        if 'error' in response_data or 'session' not in response_data:
            print_error("There was an error while starting the session: {} Try again later"
                  .format(response_data.get('error')))
            log.warning("Error: {}".format(response_data.get('error')))
            return

        self.session_id = response_data['session']
        self.short_url = response_data['short_url']
        self.login_user = response_data.get('login_user')

        # Login as the firebase user
        email, password = response_data.get('login_user'), response_data.get('password')

        try:
            self.fire_user = self.fire_auth.sign_in_with_email_and_password(email,
                                                                            password)
            self.fire_uid = self.fire_user['localId']
        except (ValueError, KeyError) as e:
            log.warning("Could not login", exc_info=True)
            print_error("Could not login to the collaboration server.")
            return

        self.stream = (self.get_firebase()
                           .child('actions').stream(self.stream_listener,
                                                    self.fire_user['idToken']))

        self.presence = (self.get_firebase()
                             .child('clients').push({'computer': platform.node(),
                                                     'uid': self.fire_uid,
                                                     'owner': self.user_email,
                                                     'email': self.user_email},
                                                    self.fire_user['idToken']))

        # Parse response_url
        if response_data:
            open_url = response_data['url']
            if 'access_token' not in open_url:
                open_url = open_url + "?access_token={}".format(access_token)
            could_open = webbrowser.open_new(open_url)
            if not could_open:
                print("Could not open browser. Go to {}".format(open_url))
        else:
            log.error("There was an error with the server. Please try again later!")
            return

        print_success("Tell your group members or course staff to go to {}"
              .format(self.short_url))

        while True:
            data = input("[{}] Type exit to disconnect: ".format(self.short_url))
            if data.strip().lower() == 'exit':
                raise ValueError('Done with session')

    def prompt_for_existing_session(self, sessions):
        """ Prompt user if they want to resume an old session
        (or their partners session) or create a new session.
        """
        if not sessions:
            return None
        print("Would you like to join a previous session or create a new session?")
        for index, session in enumerate(sessions):
            print(("{id} : {creator} started at {timestamp} ({hashid})"
                   .format(id=index+1, creator=session.get('creator'),
                           timestamp=session.get('created'), hashid=session.get('id'))))
        print("{new_id} : Create a new session with the current files?"
              .format(new_id=len(sessions)+1))
        desired = input("Type the number of the session you'd like to join: ")
        try:
            outcome = int(desired.strip())
        except:
            outcome = len(sessions)+1
            log.warning("Could not parse int for choice")

        if outcome >= len(sessions):
            log.info("Chose to start new session")
            return None
        else:
            log.info("Resuming session {}".format(outcome - 1))
            desired = sessions[outcome - 1]
            return session

    def send_messages(self, data, timeout=30, endpoint='/collab/start/'):
        """Send messages to server, along with user authentication."""
        address = 'https://{}{}'.format(self.COLLAB_SERVER, endpoint)
        params = {
            'client_name': 'ok-client',
            'client_version': client.__version__,
        }

        log.info('Sending messages to %s', address)
        try:
            r = requests.post(address, params=params, json=data, timeout=timeout)
            r.raise_for_status()
            return r.json()
        except (requests.exceptions.RequestException, requests.exceptions.BaseHTTPError, Exception) as ex:
            message = '{}: {}'.format(ex.__class__.__name__, str(ex))
            log.warning(message)
            print_error("There was an error connecting to the server."
                  "Run with --debug for more details")
        return

    def log_event(self, name, data):
        if not self.collab_analytics.get(name):
            self.collab_analytics[name] = []
        log_data = {
            'time': time.strftime(self.TIME_FORMAT),
            'data': data
        }
        self.collab_analytics[name].append(log_data)

    ############
    # Firebase #
    ############

    def get_firebase(self):
        return (self.fire_db.child('ok-sessions')
                            .child(self.fire_uid)
                            .child(self.session_id))

    def send_firebase(self, channel, data):
        return (self.get_firebase().child(channel)
                    .push(data, self.fire_user['idToken']))

    def stream_listener(self, message):
        data = message.get('data')
        if not data:
            logging.info("Irrelevant message logged while listening")
            return
        action = data.get('action')
        sender = data.get('user')
        log.debug('Received new {} message from {}'.format(action, sender))

        file_name = data.get('fileName')

        if action == "save":
            print("Saving {} locally (initiated by {})"
                  .format(file_name, data.get('user')))
            self.log_event('save', data)
            return self.save(data)
        elif action == "grade":
            print("Running tests locally (initiated by {})".format(data.get('user')))
            self.log_event('grade', data)
            return self.run_tests(data)
        else:
            print_warning("Unknown action {}".format(action))

    def run_tests(self, data):
        backup = self.save(data)

        # Perform reload of some modules for file change
        if self.assignment.src:
            for module in self.assignment.src:
                module_name = module.replace('.py', '')
                if '/' not in module_name:
                    # Ignore subdirectories for now.
                    if module_name in sys.modules:
                        del sys.modules[module_name]

        if not backup:
            (self.get_firebase().child('term')
                 .push({"status": 'Failed',
                        "computer": self.hostname,
                        "time": time.strftime(self.TIME_FORMAT),
                        "email": self.user_email,
                        'text': "Unknown files. Could not run autograding\n"},
                       self.fire_user['idToken']))
            return

        test_names = [t.name for t in list(self.assignment.test_map.values())]

        desired_test = data.get('run_test')
        if desired_test:
            test_names = [t for t in test_names if t.lower() == desired_test.lower()]

        (self.get_firebase().child('term')
             .push({"status": 'Running',
                    "computer": self.hostname,
                    "time": time.strftime(self.TIME_FORMAT),
                    "email": self.user_email,
                    'text': "Running tests for: {}\n".format(test_names)},
                   self.fire_user['idToken']))

        grading_results = self.grade(list(self.assignment.test_map.values()))
        (self.get_firebase().child('term')
             .push({"status": 'Done',
                    "computer": self.hostname,
                    "email": self.user_email,
                    "time": time.strftime(self.TIME_FORMAT),
                    'text': str(grading_results['output'])[:50000],
                    'grading': grading_results['grading']},
                   self.fire_user['idToken']))

        # Treat autograde attempts like a backup if the source wasn't from the same user
        if data['user'] != self.user_email:
            if backup and backup != data.get('fileName'):
                shutil.move(backup, data.get('fileName'))

    def save(self, data):
        file_name = data['fileName']
        file_name = file_name.strip()

        if file_name not in self.assignment.src or file_name.endswith('.ok'):
            if file_name != 'submit':
                logging.warning("Unknown filename {}".format(file_name))
                print_error("Unknown file - Not saving {}".format(file_name))
                return

        if not os.path.isfile(file_name):
            log.warning('File {} does not exist. Not backing up'.format(file_name))
            backup_dst = file_name
        else:
            # Backup the file
            log.debug("Backing up file")
            backup_dst = self.backup_file(file_name)
            print_success("Backed up file to {}".format(backup_dst))

        log.debug("Beginning overwriting file")
        contents = data['file']
        with open(file_name, 'w') as f:
            f.write(contents)
        log.debug("Done replacing file")

        # Update file contents for backup
        self.file_contents[file_name] = contents

        return backup_dst

    def backup_file(self, file_name):
        if not os.path.exists(self.BACKUP_DIRECTORY):
            os.makedirs(self.BACKUP_DIRECTORY)

        safe_file_name = file_name.replace('/', '').replace('.py', '')
        backup_name = '{}/{}-{}.txt'.format(self.BACKUP_DIRECTORY, safe_file_name,
                                            time.strftime(self.FILE_TIME_FORMAT))
        log.info("Backing up {} to {}".format(file_name, backup_name))
        shutil.copyfile(file_name, backup_name)
        return backup_name

    def grade(self, tests):
        data = {}
        print("Starting grading from external request")
        log_id = output.new_log()
        grade(tests, data, verbose=self.args.verbose)
        printed_output = ''.join(output.get_log(log_id))
        output.remove_log(log_id)
        data['output'] = printed_output
        return data

protocol = CollaborateProtocol
