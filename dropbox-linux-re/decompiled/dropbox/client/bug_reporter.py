# Source Generated with Decompyle++
# File: bug_reporter.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
import json
import pprint
from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Dict, List, Optional, Tuple
from build_number import dropbox_version
from six import add_metaclass
from dropbox.client.bug_report_providers import BugReportProvider
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.sync_root.gating import file_provider_supported
from dropbox.threading import Lock
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE

def build_allows_bug_reporter():
