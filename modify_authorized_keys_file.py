import sys

from decouple import config as decouple_config

from database_manager import DatabaseManager
from ssh_client import SSHClient


def modify_file(operate):
    servers = DatabaseManager().get_server_info()
    local_script_file = 'add_remove_public_key_in_authorized_keys.sh'
    remote_script_file = f'/tmp/{local_script_file}'
    with open(decouple_config('SSH_VENDOR_KEY_PAIR_PUBLIC'), 'r', encoding='utf-8') as file:
        public_key_content = file.read()
    authorized_keys_file = decouple_config('SSH_VENDOR_AUTHORIZED_KEYS_FILE')
    command = f'sudo bash {remote_script_file} {operate} "{public_key_content}" "{authorized_keys_file}"'
    for server in servers:
        ssh = SSHClient(server, decouple_config('SSH_USER'), decouple_config('SSH_PRIVATE_KEY'))
        try:
            ssh.connect()
            ssh.upload_file(local_script_file, remote_script_file)
            output, error = ssh.execute_command(command)
            print('Output:', output)
            print('Error:', error)
        finally:
            ssh.remove_file(remote_script_file)
            ssh.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please specify how to modify the authorized_keys file.')
        sys.exit(1)
    modify_operate = sys.argv[1]
    modify_file(modify_operate)
