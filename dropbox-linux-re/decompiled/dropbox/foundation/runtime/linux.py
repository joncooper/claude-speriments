# Source Generated with Decompyle++
# File: linux.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import subprocess
import sys
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.linux.internal import executable
from dropbox.trace import TRACE, WARNING
MYPY = False

def notify_monitor_clean_termination():
    pass


def notify_request_restart():
    TRACE('Launching autorestart process')
    if MYPY and sys.platform.startswith('win'):
        read = 0
    else:
        (read, _) = os.pipe2(os.O_CLOEXEC)
    
    try:
        env = os.environ.copy()
        env['_dbx_autorestart_fd'] = str(read)
        argv = executable(('--autorestarted',))
        subprocess.Popen(argv, pass_fds = (read,), env = env)
        
        try:
            pass
        except Exception:
            WARNING('failed to launch; autorestart will not work')
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.POLARIS_PRIMITIVES)
            
            try:
                pass
            try:
                os.close(read)
                return None
            except:
                os.close(read)





def set_restart_state(enable = None):
    pass

halt_process = os._exit
__all__ = [
    'notify_monitor_clean_termination',
    'notify_request_restart',
    'set_restart_state',
    'halt_process']
