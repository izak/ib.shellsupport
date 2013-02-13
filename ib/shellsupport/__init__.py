import shlex
import subprocess

class CommandFailed(Exception):
    def __init__(self, code):
        super(CommandFailed, self).__init__(self, code)
        self.code = code

def sh(command, stdin=None, stdout=None, stderr=None):
    if hasattr(stdin, 'read'):
        stdin = stdin.read()

    closestdout = False
    if stdout is None:
        stdout = open('/dev/null', 'w')
        closestdout = True

    if stderr is None:
        stderr = subprocess.STDOUT

    try:
        p = subprocess.Popen(shlex.split(command),
            stdin=subprocess.PIPE, stdout=stdout, stderr=stderr)
        p.communicate(input=stdin)
    finally:
        if closestdout:
            stdout.close()
    if p.returncode != 0:
        raise CommandFailed(p.returncode)
