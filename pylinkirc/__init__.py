# XXX This file is overwritten by setup.py when building the module. XXX

try:
    import os
    versionpath = os.path.join(os.path.dirname(), '..', 'VERSION')
    with open(versionpath, encoding='utf-8') as f:
        __version__ = f.read().strip()
except:
    __version__ = 'unknown'


try:
    import subprocess
    real_version = subprocess.check_output(['git', 'describe', '--tags']).decode('utf-8').strip()
except:
    real_version = __version__ + '-sourcetree'
