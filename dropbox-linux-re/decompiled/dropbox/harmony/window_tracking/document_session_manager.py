# Source Generated with Decompyle++
# File: document_session_manager.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from collections import defaultdict
from typing import Callable, DefaultDict, Dict, Iterable, List, Optional, Set, Tuple
from six import iteritems, itervalues
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method_0, async_queued_method_1, async_queued_method_3
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.signals import SignalConnection, StandardSignal
from dropbox.harmony.models.types import ApplicationID, DocumentSession, DocumentSessionID, WindowFile, WindowID
from dropbox.harmony.window_tracking.deleted_file_cache import DeletedFileCache
from dropbox.harmony.window_tracking.window_file_map import WindowDetails, WindowFileMap
from dropbox.model.types import FileId
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRLowerServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.exceptions import UnmountedPathError
from dropbox.sync_engine_boundary.types.local_path import OutsideDropboxException
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.trace import TRACE

class DocumentSessionManager(SingletonActor):
    pass
# WARNING: Decompyle incomplete

