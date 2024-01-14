import subprocess


def execute(command: str) -> str:
    """Execute a command and return the output."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        raise Exception(error.decode('utf-8'))
    return output.decode('utf-8')
