import sys

from config import config
from database_manager import DatabaseManager
from ssh_client import SSHClient


def modify_file(operate):
    servers = DatabaseManager().get_server_info()
    local_script_file = 'add_remove_public_key_in_authorized_keys.sh'
    remote_script_file = f'/tmp/{local_script_file}'
    with open(config.ssh_user_key_pair_public_file, 'r', encoding='utf-8') as file:
        public_key_content = file.read()
    authorized_keys_file = config.ssh_user_authorized_keys_file_path
    command = f'sudo bash {remote_script_file} {operate} "{public_key_content}" "{authorized_keys_file}"'
    for server in servers:
        ssh = SSHClient(server, config.ssh_admin_user, config.ssh_admin_user_private_key)
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
