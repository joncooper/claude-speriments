# Source Generated with Decompyle++
# File: watchdog.pyc (Python 3.11)

from typing import Optional
from uuid import UUID
from apex._apex import ffi, lib

def is_monitored():
    return lib.is_monitored()


def monitor_session_id():
    uuid = lib.monitor_session_id()
    return UUID(ffi.string(uuid).decode('utf-8')) if uuid != ffi.NULL else None


def notify_monitor_clean_termination():
    lib.notify_monitor_clean_termination()


def request_autorestart_enable():
    lib.request_autorestart_enable()


def request_autorestart_disable():
    lib.request_autorestart_disable()

