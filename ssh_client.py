import paramiko


class SSHClient(object):
    def __init__(self, server, username, private_key_path, port=22):
        self.hostname = server['hostname']
        self.dns = server['dns']
        self.username = username
        self.private_key_path = private_key_path
        self.port = port
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        private_key = paramiko.Ed25519Key.from_private_key_file(self.private_key_path)
        self.ssh.connect(self.dns, port=self.port, username=self.username, pkey=private_key)
        print(f'Connected to {self.hostname}.')

    def execute_command(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()
        return output, error

    def upload_file(self, local_path, remote_path):
        sftp = self.ssh.open_sftp()
        sftp.put(local_path, remote_path)
        sftp.close()

    def remove_file(self, remote_path):
        sftp = self.ssh.open_sftp()
        try:
            sftp.remove(remote_path)
        except FileNotFoundError:
            print(f'File {remote_path} not found')
        sftp.close()

    def close(self):
        self.ssh.close()
