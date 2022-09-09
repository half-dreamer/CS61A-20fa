import sys
import os

VERSION_MESSAGE = """
ERROR: You are using Python {}.{}, but OK requires Python 3.4 or higher.
Make sure you are using the right command (e.g. `python3 ok` instead of
`python ok`) and that you have Python 3 installed.
""".strip()

if sys.version_info[:2] < (3, 4):
    print(VERSION_MESSAGE.format(*sys.version_info[:2]))
    sys.exit(1)

from client.cli import ok
from client.utils import config
import certifi

def patch_requests():
    """ Customize the cacerts.pem file that requests uses.
    Automatically updates the cert file if the contents are different.
    """
    config.create_config_directory()
    ca_certs_file = config.CERT_FILE
    ca_certs_contents = certifi.__loader__.get_data('certifi/cacert.pem')

    should_write_certs = True

    if os.path.isfile(ca_certs_file):
        with open(ca_certs_file, 'rb') as f:
            existing_certs = f.read()
            if existing_certs != ca_certs_contents:
                should_write_certs = True
                print("Updating local SSL certificates")
            else:
                should_write_certs = False

    if should_write_certs:
        with open(ca_certs_file, 'wb') as f:
            f.write(ca_certs_contents)

    os.environ['REQUESTS_CA_BUNDLE'] = ca_certs_file

patch_requests()

if __name__ == '__main__':
    ok.main()
