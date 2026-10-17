# Source Generated with Decompyle++
# File: trace.pyc (Python 3.11)

from typing import Any, Optional
from dropbox.trace import TRACE, WARNING

def CB_TRACE(fmt = None, session_id = None, *args):
    formatted_session_id = session_id if session_id else 'ComputerBackup'
    real_fmt = f'''[{formatted_session_id}] {fmt}'''
# WARNING: Decompyle incomplete


def CB_WARN(fmt = None, session_id = None, *args):
    formatted_session_id = session_id if session_id else 'ComputerBackup'
    real_fmt = f'''[{formatted_session_id}] {fmt}'''
# WARNING: Decompyle incomplete

