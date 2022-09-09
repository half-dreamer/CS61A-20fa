from client.protocols.common import models
import client

import logging
import requests
import webbrowser

from client.utils.printer import print_error

log = logging.getLogger(__name__)


class AutoStyleProtocol(models.Protocol):

    # Timeouts are specified in seconds.
    SHORT_TIMEOUT = 10
    API_ENDPOINT = 'https://codestyle.herokuapp.com/ok_launch/'
    ALLOW_QUESTIONS = ['flatten', 'add_up', 'permutations', 'deep_len']

    def run(self, messages):
        if not self.args.style:
            log.info("Autostyle not enabled.")
            return
        elif self.args.local:
            log.info("Autostyle requires network access.")
            return

        if not messages.get('analytics'):
            log.warning("Autostyle needs to be after analytics")
            return
        if not messages.get('grading'):
            log.warning("Autostyle needs to be after grading")
            return
        if not self.args.question:
            log.warning("Autostyle requires a specific question")
            return
        messages['autostyle'] = {}

        grading = messages['grading']

        for question in self.args.question:
            if question in AutoStyleProtocol.ALLOW_QUESTIONS:
                # Ensure that all tests have passed
                results = grading.get(question)
                if not results:
                    log.warning("No grading info")
                    return
                elif results['failed'] or results['locked']:
                    log.warning("Has not passed all tests")
                    print_error(
                        "To use AutoStyle you must have a correct solution for {0}!".format(question))
                    return
            else:
                log.info("Not an autostyle question")
                print_error("Make sure the question you are using is an AutoStyle question!")
                return

        print("Once you begin you must finish the experiment in one sitting. This will take at most 2 hours.")
        confirm = input("Do you wish to continue to AutoStyle? (y/n): ")
        if confirm.lower().strip() != 'y':
            return

        messages['analytics']['identifier'] = self.assignment.get_identifier()
        # Send data to autostyle
        response_url = self.send_messages(messages, self.SHORT_TIMEOUT)
        # Parse response_url
        if response_url:
            webbrowser.open_new(response_url)
        else:
            log.error("There was an error with AutoStyle. Please try again later!")

    def send_messages(self, messages, timeout):
        """Send messages to server, along with user authentication."""
        data = {
            'assignment': self.assignment.endpoint,
            'messages': messages,
            'submit': self.args.submit
        }
        address = self.API_ENDPOINT
        address_params = {
            'client_name': 'ok-client',
            'client_version': client.__version__,
        }
        log.info('Sending messages to %s', address)
        try:
            response = requests.post(address,
                params=address_params, json=data, timeout=timeout)
            response.raise_for_status()
            return response.json()['url']
        except (requests.exceptions.RequestException, requests.exceptions.BaseHTTPError, ValueError) as ex:
            log.warning('%s: %s', ex.__class__.__name__, str(ex))
        return

protocol = AutoStyleProtocol
