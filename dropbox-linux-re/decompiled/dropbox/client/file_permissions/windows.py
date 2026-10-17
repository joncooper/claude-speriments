# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import re
import subprocess
import traceback as error_traceback
import typing
from typing import Any, Optional, Text
from build_number.platform import IS_WINDOWS
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.sync_error.model.common import SyncErrorDetail
from dropbox.client.features.sync_error.model.sync_error_logger import PermissionEvent, SyncErrorLogger
from dropbox.client.ui.common.dialog_constants import IconType
from dropbox.client.ui.common.dialogs import BaseDialogController
from dropbox.client.ui.common.misc import MiscStrings
from dropbox.exception.reporting import report_bad_assumption, report_exception, Severity
from dropbox.i18n import trans
from dropbox.sync_event.report import report_sync_event, SyncEventName
from dropbox.trace import TRACE
if IS_WINDOWS:
    from subprocess import CREATE_NO_WINDOW
else:
    CREATE_NO_WINDOW = 0

def _parse_summary(raw = None):
    text = raw.decode('utf-8', errors = 'ignore')
    nums = re.findall('\\b\\d+\\b', text)
    if len(nums) >= 2:
        return (int(nums[-2]), int(nums[-1]))


def fix_permissions_under_path(account = None, path = None, location = None):
    (output_cmd1, ex_cmd1, retcode_cmd1, success_cnt_cmd1, failure_cnt_cmd1) = icacls_clear_permissions(path, account, location)
    (output_cmd2, ex_cmd2, retcode_cmd2, success_cnt_cmd2, failure_cnt_cmd2) = icacls_set_explicit_sync_root_permissions(path, account, location)
    output = f'''{output_cmd1}\n\n{output_cmd2}'''
    success_cnt = success_cnt_cmd1 + success_cnt_cmd2
    failure_cnt = failure_cnt_cmd1 + failure_cnt_cmd2
    TRACE('Output: {}', output)
# WARNING: Decompyle incomplete


def icacls_clear_permissions(path = None, account = None, location = None):
    command_clear_perms = [
        'icacls',
        path,
        '/T',
        '/Q',
        '/C',
        '/reset']
    return run_icacls_command(command_clear_perms, account, location)


def icacls_set_explicit_sync_root_permissions(path = None, account = None, location = None):
    username = os.environ.get('USERNAME')
    if not username:
        return ('', KeyError('USERNAME environment variable not found'), None, 0, 0)
    command_explicit_sync_root_perms = [
        None,
        path,
        '/grant',
        f'''{username}:(OI)(CI)F''',
        '/inheritance:e',
        '/Q',
        '/C']
    return run_icacls_command(command_explicit_sync_root_perms, account, location)


def run_icacls_command(command = None, account = None, location = None):
    full_output = 'Command: {}\n'.format(' '.join(command))
    retcode = 0
    
    try:
        output = subprocess.check_output(command, creationflags = CREATE_NO_WINDOW)
        (success_cnt, failure_cnt) = _parse_summary(output)
        full_output = full_output + output.decode('utf-8', errors = 'replace')
        if not success_cnt and failure_cnt:
            return (full_output, None, 0, 0, 0)
        except subprocess.CalledProcessError:
            exc = 0
            (success_cnt, failure_cnt) = _parse_summary(exc.output) if exc.output else (None, None)
            retcode = exc.returncode
            full_output = '{}\n{}'.format(full_output, exc.output.decode('utf-8', errors = 'replace') if exc.output else '')
            if not success_cnt and failure_cnt:
                del exc
                return None
            failure_cnt = 0
            del exc



def fix_permissions_for_entire_dropbox(account = None, location = None):
    pass
# WARNING: Decompyle incomplete


def show_dialog_to_fix_permissions_for_entire_dropbox(account, dialog_controller, location = None, detail = None, callback = None, extensions = ('startup', None, None, None, 1), attempt = ('account', 'AccountInterface', 'dialog_controller', 'BaseDialogController', 'location', 'Text', 'detail', 'Optional[SyncErrorDetail]', 'callback', 'Optional[Any]', 'extensions', 'Optional[Text]', 'attempt', 'int')):
    pass
# WARNING: Decompyle incomplete

