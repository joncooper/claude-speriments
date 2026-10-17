# Source Generated with Decompyle++
# File: open_program_name.pyc (Python 3.11)

import itertools
from typing import List, Optional, Text
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventClass
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.components.desktop_components import DesktopComponent
from dropbox.platform import IS_WINDOWS
if IS_WINDOWS:
    from winenumhandles.api import get_proc_description, get_proc_path, OpenHandleEnumerator
EXCEPTION_LIMIT = 10

def open_program_name(fs_path = None):
    programs = []
# WARNING: Decompyle incomplete


def _log_open_program_name_exception(exception = None):
