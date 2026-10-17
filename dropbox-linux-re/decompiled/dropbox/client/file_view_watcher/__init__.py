# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Dict, Optional, Text
from six import add_metaclass
from dropbox.client.authentication.manager import Account
from dropbox.client.gandalf import Gandalf
from dropbox.exception.exceptions import BadAssumptionError
from dropbox.exception.reporting import assert_not_none
from dropbox.fileevents import FileEvents
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
FileViewWatcher = <NODE:12>()
