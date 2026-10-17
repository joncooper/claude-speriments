# Source Generated with Decompyle++
# File: posix.pyc (Python 3.11)

import subprocess
from typing import Any, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class HardlinkFixFailed(Exception):
    pass


def _convert_hardlinks_to_copies_under_path(path):
    
    try:
        output = subprocess.check_output([
            'find',
            path,
            '-type',
            'f',
            '-links',
            '+1',
            '!',
            '(',
            '-name',
            'Icon\r',
            '-or',
            '-path',
            '*/.dropbox.cache/*',
            ')',
            '-exec',
            'cp',
            '-can',
            '{}',
            '{}.hardlink.bak',
            ';',
            '-exec',
            'mv',
            '{}.hardlink.bak',
            '{}',
            ';',
            '-print']).strip()

    
    try:
        output = subprocess.check_output([
            'find',
            path,
            '-type',
            'f',
            '-links',
            '+1',
            '!',
            '(',
            '-name',
            'Icon\r',
            '-or',
            '-path',
            '*/.dropbox.cache/*',
            ')',
            '-print']).strip()
        if output:
            TRACE('Hardlinks exist even after running the command to fix them. Output: %r', output)
            raise HardlinkFixFailed(output)
    except subprocess.CalledProcessError:
        exc = None
        TRACE('Hardlink check failed with exit code: %r and output: %r', exc.returncode, exc.output)
        raise HardlinkFixFailed(exc.output)
        exc = None
        del exc

    TRACE('Successfully fixed all hardlinks by converting them into copies.')


def convert_hardlinks_to_copies_in_dropbox(app, account = (None,)):
    local_config = app.config_manager.local_config(account)
    path = local_config.config_dict.get('dropbox_path')
    if not path:
        TRACE("!! User hasn't picked their Dropbox location, so we can't fix hardlinks yet.")
        return None
    _convert_hardlinks_to_copies_under_path(path)

