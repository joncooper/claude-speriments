# Source Generated with Decompyle++
# File: paging_thread.pyc (Python 3.11)

import contextlib
import itertools
import os
import random as insecure_random
import threading
from typing import Callable, cast, Generator
from build_number import is_run_box
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.gandalf import Gandalf
from dropbox.client.ui.common.tray_popup_constants import TrayUpdateOptionsReason
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.infinite.blacklist import InfiniteRecallBlacklist
from dropbox.infinite.constants import InfiniteEventType
from dropbox.infinite.honeypot import create_honeypot_placeholder_files, is_path_in_honeypot, remove_honeypot_placeholder_files
from dropbox.infinite.pager import CancelPageRequest, InfiniteRequest, Pager, PagerCommunicationError, PageRequest, PageResponse, PagerMissingElevationError, PagerNotLoadedError, PagerRequestType
from dropbox.infinite.paging_worker_thread import on_paging_worker_thread
from dropbox.infinite.util import report_infinite_event
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.ui.common.tray_menu_controller import TrayMenuController

class PagingThread(StoppableThread):
    pass
# WARNING: Decompyle incomplete

