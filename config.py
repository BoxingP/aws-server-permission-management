import os

from dotenv import load_dotenv


class Config(object):

    def __init__(self):
        load_dotenv()
        self.ssh_admin_user = os.environ.get('SSH_ADMIN_USER')
        self.ssh_admin_user_private_key = os.environ.get('SSH_ADMIN_USER_PRIVATE_KEY')
        self.ssh_user_key_pair_public_file = os.environ.get('SSH_USER_KEY_PAIR_PUBLIC_FILE')
        self.ssh_user_authorized_keys_file_path = os.environ.get('SSH_USER_AUTHORIZED_KEYS_FILE_PATH')
        self.server_database_adapter = os.environ.get('SERVER_DATABASE_ADAPTER')
        self.server_database_host = os.environ.get('SERVER_DATABASE_HOST')
        self.server_database_port = os.environ.get('SERVER_DATABASE_PORT')
        self.server_database_database = os.environ.get('SERVER_DATABASE_DATABASE')
        self.server_database_user = os.environ.get('SERVER_DATABASE_USER')
        self.server_database_password = os.environ.get('SERVER_DATABASE_PASSWORD')
        self.server_aws_account = os.environ.get('SERVER_AWS_ACCOUNT')
        self.server_environment = os.environ.get('SERVER_ENVIRONMENT')
        self.server_state = os.environ.get('SERVER_STATE')


config = Config()
