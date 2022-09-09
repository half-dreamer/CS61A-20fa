import logging
import json
import os
import time

from client.api.assignment import load_assignment
from client.utils import auth as ok_auth

log = logging.getLogger(__name__)

class Notebook:
    def __init__(self, filepath=None, cmd_args=None, debug=False, mode='jupyter'):
        ok_logger = logging.getLogger('client')   # Get top-level ok logger
        ok_logger.setLevel(logging.DEBUG if debug else logging.ERROR)
        self.assignment = load_assignment(filepath, cmd_args)
        # Attempt a login with enviornment based tokens
        login_with_env(self.assignment)

        if mode not in ["jupyter", "jupyterlab"]:
            raise ValueError("Bad mode argument: should be either \'jupyter\' or \'jupyterlab\'")
        self.mode = mode

        

    def run(self, protocol, messages, **kwargs):
        if protocol not in self.assignment.protocol_map:
            print("{} has not been included in the .ok config".format(protocol))
            return
        return self.assignment.protocol_map[protocol].run(messages, **kwargs)

    def auth(self, force=False, inline=True):
        if not force and login_with_env(self.assignment):
            return
        self.assignment.authenticate(force=force, inline=inline)

    def grade(self, *args, **kwargs):
        return self.assignment.grade(*args, **kwargs)

    def grade_all(self, *args, **kwargs):
        for test_key in self.assignment.test_map:
            self.assignment.grade(test_key, *args, **kwargs)

    def score(self, env=None, score_out=None):
        """ Run the scoring protocol.

        score_out -- str; a file name to write the point breakdown
                     into.

        Returns: dict; maps score tag (str) -> points (float)
        """
        messages = {}
        self.assignment.set_args(
            score=True,
            score_out=score_out,
        )
        if env is None:
            import __main__
            env = __main__.__dict__
        self.run('scoring', messages, env=env)
        return messages['scoring']

    def backup(self):
        messages = {}
        self.assignment.set_args(backup=True)
        self.save(messages)
        return self.run('backup', messages)

    def submit(self):
        messages = {}
        self.assignment.set_args(submit=True)
        if self.save(messages):
            return self.run('backup', messages)
        else:
            filename = self.assignment.src[0]
            print("Making a best attempt to submit latest \'{}\',"
                " last modified at {}".format(filename, time.ctime(os.path.getmtime(filename))))
            return self.run('backup', messages)
        
    def save(self, messages, delay=0.5, attempts=3):
        saved = self.save_notebook()
        if not saved:
            return None

        for _ in range(attempts):
            self.run('file_contents', messages)
            if validate_contents(messages['file_contents']):
                return messages
            else:
                log.info("Notebook file is invalid, Retrying File Read")
                time.sleep(delay)
        log.warning("OK could not autosave the notebook. "
                    " Please ensure that the submission URL on OK appears complete")

    def save_notebook(self):
        """ Saves the current notebook by
        injecting JavaScript to save to .ipynb file.
        """
        try:
            from IPython.display import display, Javascript
        except ImportError:
            log.warning("Could not import IPython Display Function")
            print("Make sure to save your notebook before sending it to OK!")
            return

        if self.mode == "jupyter":
            display(Javascript('IPython.notebook.save_checkpoint();'))
            display(Javascript('IPython.notebook.save_notebook();'))
        elif self.mode == "jupyterlab":
            display(Javascript('document.querySelector(\'[data-command="docmanager:save"]\').click();'))   
                       
        print('Saving notebook...', end=' ')

        ipynbs = [path for path in self.assignment.src
                  if os.path.splitext(path)[1] == '.ipynb']
        # Wait for first .ipynb to save
        if ipynbs:
            if wait_for_save(ipynbs[0]):
                print("Saved '{}'.".format(ipynbs[0]))
            else:
                log.warning("Timed out waiting for IPython save")
                print("Could not automatically save \'{}\'".format(ipynbs[0]))
                print("Make sure your notebook"
                      " is correctly named and saved before submitting to OK!".format(ipynbs[0]))
                return False                
        else:
            print("No valid file sources found")
        return True

def login_with_env(assignment):
    access_token = os.environ.get('OKPY_ACCESS_TOKEN')
    if not access_token:
        log.info("ACCESS_TOKEN did not exist in the environment")
        return
    student_email = ok_auth.display_student_email(assignment.cmd_args, access_token)
    if student_email:
        # Token is valid,
        expires_in = int(os.environ.get('OKPY_EXPIRES_IN', 60))
        refresh_token = os.environ.get('OKPY_REFRESH_TOKEN')

        expires_at = int(time.time()) + expires_in
        ok_auth.update_storage(access_token, expires_at, refresh_token)
        return True

def validate_contents(file_contents):
    """Ensures that all ipynb files in FILE_CONTENTS
    are valid JSON files."""
    for name, contents in file_contents.items():
        if os.path.splitext(name)[1] != '.ipynb':
            continue
        if not contents:
            return False
        try:
            json_object = json.loads(contents)
        except ValueError:
            return False
    return True

def wait_for_save(filename, timeout=5):
    """Waits for FILENAME to update, waiting up to TIMEOUT seconds.
    Returns True if a save was detected, and False otherwise.
    """
    modification_time = os.path.getmtime(filename)
    start_time = time.time()
    while time.time() < start_time + timeout:
        if (os.path.getmtime(filename) > modification_time and
            os.path.getsize(filename) > 0):
            return True
        time.sleep(0.2)
    return False
