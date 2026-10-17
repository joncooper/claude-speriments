# Source Generated with Decompyle++
# File: linux.pyc (Python 3.11)

from __future__ import absolute_import
from typing import List, Text
from dropbox.functions import EitherStr
from dropbox.i18n import trans
from dropbox.linux.internal import run_as_root
from dropbox.trace import TRACE

def request_authorization_from_user_and_run(cmd = None, argv = None, auth_text = None):
    if auth_text:
        auth_text += '\n'
    auth_text += trans('Type your Linux password to let Dropbox make changes.')
    TRACE('Running %s as root', cmd)
    retcode = run_as_root([
        cmd] + argv, auth_text)
    TRACE('%s returned %s', cmd, retcode)
    if retcode != 0:
        raise Exception(f'''command {cmd!r} {argv!r} returned nonzero retcode {retcode!r}''')

