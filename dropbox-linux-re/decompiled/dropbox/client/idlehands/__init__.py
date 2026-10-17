# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, print_function
import time
from pprint import pprint
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.native_threading import NativeCondition
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.threadutils import StoppableThread
DEFAULT_POLL_SECONDS = 60
TS_DELTA_SECONDS = 3
DEBUG = False

class IdleHandler(StoppableThread):
    pass
# WARNING: Decompyle incomplete

