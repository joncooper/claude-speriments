# Source Generated with Decompyle++
# File: multiaccount_shell_adapter.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, Text, Union
from dropbox.exception.reporting import report_bad_assumption
from dropbox.shared.local_path import LocalPath
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class MultiaccountShellAdapter(object):
    
    def __init__(self = None, app = None):
        self._app = app

    
    def shell_touch(self = None, local_path = None, *args, **kwargs):
        if self._app.shell_controller:
            self._app.shell_controller.touch_files([
                Text(local_path)])
            return None
        report_bad_assumption('Cannot shell_touch without shell_controller')

    
    def clear_shell_state(self, dropbox_path):
        if self._app.shell_controller:
            self._app.shell_controller.reset_root_path(Text(dropbox_path))
            return None
        report_bad_assumption('Cannot clear_shell_state without shell_controller')


