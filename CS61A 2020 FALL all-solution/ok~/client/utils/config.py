import os

CONFIG_DIRECTORY = os.path.join(os.path.expanduser('~'), '.config', 'ok')
REFRESH_FILE = os.path.join(CONFIG_DIRECTORY, "auth_refresh")
CERT_FILE = os.path.join(CONFIG_DIRECTORY, "cacert.pem")

def create_config_directory():
    if not os.path.exists(CONFIG_DIRECTORY):
        os.makedirs(CONFIG_DIRECTORY)
    return CONFIG_DIRECTORY
