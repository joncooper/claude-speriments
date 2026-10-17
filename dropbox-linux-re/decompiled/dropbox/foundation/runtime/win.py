# Source Generated with Decompyle++
# File: win.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import win32api
import win32process
from apex.watchdog import notify_monitor_clean_termination as _notify_monitor_clean_termination, request_autorestart_disable as _request_autorestart_disable, request_autorestart_enable as _request_autorestart_enable
from mypy_extensions import NoReturn

def notify_monitor_clean_termination():
    _notify_monitor_clean_termination()


def set_restart_state(enable = None):
    if enable:
        _request_autorestart_enable()
        return None
    _request_autorestart_disable()


def notify_request_restart():
    _request_autorestart_enable()


def halt_process(n = None):
    
    try:
        process_handle = win32api.GetCurrentProcess()
        win32process.TerminateProcess(process_handle, n)
        os._exit(n)
        return None
    except:
        os._exit(n)


__all__ = [
    'notify_monitor_clean_termination',
    'set_restart_state',
    'notify_request_restart',
    'halt_process']
