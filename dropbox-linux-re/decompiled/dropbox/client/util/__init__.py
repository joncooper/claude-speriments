# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import functools
import os
import sys
import time
import traceback
from pathlib import Path
from typing import Any, Callable, cast, Iterable, List, Optional, Text, Tuple, TypeVar, Union
from build_number import dropbox_version, is_frozen, is_test
from build_number.features import feature_enabled
from lib.crashpad.api import add_simple_annotation
from dropbox.callbacks import Handler
from dropbox.client.constants import AppDataPaths
from dropbox.client.ui.common.dialog_constants import DialogEventTypes, DialogFrameworkTypes, DialogSourceTypes
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception, stop_reporting_connection_closed
from dropbox.exception.severity import Severity
from dropbox.foundation.environment import debugging_features_are_enabled
from dropbox.foundation.exception_info import ExcInfo, typed_exc_info
from dropbox.foundation.reporting import report_app_framework_event_restricted
from dropbox.foundation.runtime import panic_with_report
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.functions import synchronized
from dropbox.gui import spawn_thread_with_name
from dropbox.i18n import trans
from dropbox.observable import watchable
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.threading import Lock
from dropbox.trace import dump_python_stacks, TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.ui.common.dialogs import BaseDialogController, DialogController
if IS_LINUX:
    from dropbox.client.util.linux import app_display_name_for_file, app_for_file, check_move_blocked, clean_tray, create_hidden_symlink, enable_p2p_default, executable, fs_supports_attrs, get_contents_root, get_drives, get_free_space, get_fs_type, get_platform_info, get_repo_root_unfrozen, get_sanitized_executable_path, get_update_manager_id, get_update_manager_logs, get_user_agent_dict, get_volume_info, hard_exit_unwatched, highlight_file, highlight_files, is_dir, kill_other_instances, launch_app, launch_folder, launch_new_dropbox, natural_basename_sort_cmp, restart_unwatched, show_folder, switch_sidebar_link
elif IS_MAC:
    from dropbox.client.util.mac import app_display_name_for_file, app_for_file, check_move_blocked, clean_tray, create_hidden_symlink, enable_p2p_default, executable, fs_supports_attrs, get_contents_root, get_drives, get_free_space, get_fs_type, get_platform_info, get_repo_root_unfrozen, get_sanitized_executable_path, get_update_manager_id, get_update_manager_logs, get_user_agent_dict, get_volume_info, hard_exit_unwatched, highlight_file, highlight_files, is_dir, kill_other_instances, launch_app, launch_folder, launch_new_dropbox, natural_basename_sort_cmp, restart_unwatched, show_folder, switch_sidebar_link
elif IS_WINDOWS:
    from dropbox.client.util.win import app_display_name_for_file, app_for_file, check_move_blocked, clean_tray, create_hidden_symlink, enable_p2p_default, executable, fs_supports_attrs, get_contents_root, get_drives, get_free_space, get_fs_type, get_platform_info, get_repo_root_unfrozen, get_sanitized_executable_path, get_update_manager_id, get_update_manager_logs, get_user_agent_dict, get_volume_info, hard_exit_unwatched, highlight_file, highlight_files, is_dir, kill_other_instances, launch_app, launch_folder, launch_new_dropbox, natural_basename_sort_cmp, restart_unwatched, show_folder, switch_sidebar_link
IS_HARD_EXITING = False
_MAX_WAIT_ON_QUIT_SEC = 60
_KILLER_THREAD_STARTED_LOCK = Lock()
_KILLER_THREAD_STARTED = False

def _try_trace_exception():
    
    try:
        report_exception(severity = Severity.TRACE, component = DesktopComponent.UNKNOWN)
        return None
    except Exception:
        return None


hard_exit = (lambda exit_code = None, reason = None: IS_HARD_EXITING = Trueadd_simple_annotation('during_shutdown', 'True')report_app_framework_event_restricted('hard_exit_started', exit_code = str(exit_code.value), reason = str(reason))try:
TRACE('############################## HARD EXIT ##################################')TRACE('Hard exiting with code %d and reason %r', exit_code.value, reason)_print_exit_traceback()except Exception:
_try_trace_exception()start_killer_thread(exit_code, reason)try:
TRACE('Running pre exit handlers...')except Exception:
_try_trace_exception()stop_reporting_connection_closed()on_exit(exit_code)hard_exit_unwatched(exit_code))()

def is_app_hard_exiting():
    return IS_HARD_EXITING


def start_unlink_and_quit(arg = None, dialog_controller = None):
    launch_new_dropbox([
        arg], wait = True)
    failure_caption = trans('Sign out failed')
    failure_message = trans('Please try again or contact support if this error persists')
    ok_button = trans('Ok')
    dialog_controller.report_dialog_metrics(event = DialogEventTypes.TRIGGERED, framework = DialogFrameworkTypes.NATIVE, source = DialogSourceTypes.OTHER)
    dialog_controller.native_dialog_controller.show_non_blocking_alert_dialog(caption = failure_caption, message = failure_message, buttons = [
        ok_button])


def restart(opts = None):
    
    try:
        TRACE('############################## RESTART ##################################')
        TRACE('Restart called. Restarting with args %r', opts)
        _print_exit_traceback()
    except Exception:
        _try_trace_exception()

    _start_killer_thread_for_restart(opts)
    
    try:
        TRACE('Running pre exit handlers...')
    except Exception:
        _try_trace_exception()

    stop_reporting_connection_closed()
    on_exit(None)
    restart_unwatched(opts)

on_exit = (lambda exit_code = None: try:
TRACE('Handlers to prep app to exit have finished running')Noneexcept Exception:
_try_trace_exception()None)()()

def hard_exit_runbox(reason = None, component = None, exc_info = None):
    if not feature_enabled('runbox-hard-exits-exception') or is_frozen():
        panic_with_report(ExitCode.FATAL_EXCEPTION, reason = reason, component = component, exc_info = exc_info)
        return None
    return None

_C = TypeVar('_C', bound = Callable[(..., Any)])

def hard_exit_runbox_on_none_return(func = None, component = None):
    pass
# WARNING: Decompyle incomplete


def hard_exit_runbox_on_exception(func = None, component = None):
    pass
# WARNING: Decompyle incomplete


def _print_exit_traceback():
    tb_list = traceback.extract_stack()
    tb_list = tb_list[:-1]
    TRACE('Called with stack:\n%s', ''.join(traceback.format_list(tb_list)))


def _killer_thread_enabled():
    return not is_test()


def start_killer_thread(exit_code = None, reason = None):
    global _KILLER_THREAD_STARTED
    _KILLER_THREAD_STARTED_LOCK
    if not _killer_thread_enabled():
        None(None, None)
        return None
    if None:
        None(None, None)
        return None
    _KILLER_THREAD_STARTED = None
    None(None, None)


def _start_killer_thread_for_restart(opts = None):
    global _KILLER_THREAD_STARTED
    _KILLER_THREAD_STARTED_LOCK
    if not _killer_thread_enabled():
        None(None, None)
        return None
    if None:
        None(None, None)
        return None
    _KILLER_THREAD_STARTED = None
    None(None, None)


def _killer_thread_wait(action = None):
    total_quit_wait = _MAX_WAIT_ON_QUIT_SEC
    if debugging_features_are_enabled():
        total_quit_wait *= 2
    killer_warn_time = int(total_quit_wait / 2)
    time.sleep(killer_warn_time)
    
    try:
        TRACE('!! Quit callbacks taking a long time (%r sec)', killer_warn_time)
    except Exception:
        _try_trace_exception()

    time.sleep(killer_warn_time)
    
    try:
        TRACE('!! Quit handlers timed out (%r sec), %s Dropbox', total_quit_wait, action)
        python_stacks = dump_python_stacks()
        TRACE('!! Dumping Python stacks due to quit timeout:\n%s', python_stacks)
        return None
    except Exception:
        _try_trace_exception()
        return None



def _killer_thread_main_kill(exit_code = None, reason = None):
    _killer_thread_wait('exiting')
    
    try:
        TRACE('############################## KILLER THREAD EXIT ##################################')
        report_bad_assumption('Exiting due to killer thread (original_reason: %s)', reason)
    except Exception:
        _try_trace_exception()

    real_exit_code = ExitCode.KILLER_THREAD_EXIT
    if exit_code == ExitCode.FATAL_EXCEPTION:
        real_exit_code = exit_code
    
    try:
        force_flush = force_flush
        import dropbox.client.high_trace
        force_flush()
    except Exception:
        _try_trace_exception()

    hard_exit_unwatched(real_exit_code)


def _killer_thread_main_restart(opts = None):
    _killer_thread_wait('restarting')
    
    try:
        TRACE('############################## KILLER THREAD RESTART ##################################')
        report_bad_assumption('Restarting due to killer thread with opts: %s', opts)
        force_flush = force_flush
        import dropbox.client.high_trace
        force_flush()
    except Exception:
        _try_trace_exception()

    restart_unwatched(opts)


def safe_print(text, redacted_text, account = (None, None)):
    pass
# WARNING: Decompyle incomplete


def safe_to_str(obj = None):
    if isinstance(obj, str):
        return obj
    
    try:
        return str(obj, 'utf-8')
    except TypeError:
        if dropbox_version.is_internal_alpha():
            report_bad_assumption(f'''Received a non-str, non-bytes obj in safe_to_str(): {obj!r}''')
        return 


