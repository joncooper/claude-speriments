# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

import os
import stat
from typing import Any, cast, Iterable, List, Optional, Text
from dropbox.assertions import assert_
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.event_names import INFINITE_EVENT
from dropbox.foundation.platform_version import PLATFORM_VERSION
from dropbox.infinite.constants import InfiniteEventType
from dropbox.trace import TRACE

def report_infinite_event(event_name = None, account = None, **extra_dict):
    pass
# WARNING: Decompyle incomplete


def report_user_action_infinite_event(event_name = None, pathlist = None, account = None, **extra):
    extra_dict = extra.items()()
# WARNING: Decompyle incomplete

