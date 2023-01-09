import subprocess

def make_file_accessible(self, file_path: str, file_name: str, user: str) -> str:
    full_path = os.path.join(file_path, file_name)
    command = ['sudo', 'chown', f'{user}:', full_path]
    subprocess.run(command)
    return full_path