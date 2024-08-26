import os
import webbrowser

env = 'CFFIXED_USER_HOME'
env = 'HOME'
env = 'TMPDIR'


home = os.getenv(env)
_root = '/..' * 9

url = _root + home

webbrowser.open(f'pythonista3://{url}')

