# Source Generated with Decompyle++
# File: bug_reporter_service.pyc (Python 3.11)

from collections import OrderedDict
from typing import Optional, OrderedDict as OrderedDictType
from dropbox.client.features.bug_reporter.actor import BugReporter
from dropbox.client.features.bug_reporter.types import BugTime, BugType, ErrorDetails
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures import Future
from dropbox.foundation.futures.helpers import FutureHelpers
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.html_views.electron.ipc._interface import JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class BugReporterService(Actor):
    pass
# WARNING: Decompyle incomplete

