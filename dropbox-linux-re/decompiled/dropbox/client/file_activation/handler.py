# Source Generated with Decompyle++
# File: handler.pyc (Python 3.11)

import os
from collections import defaultdict
from functools import partial
from typing import Any, cast, DefaultDict, List, Optional, Sequence, Text, Tuple, Type
from dropbox.client.authentication.account import Account
from dropbox.client.background_worker import on_background_thread_returns_none
from dropbox.client.cloud_docs.file_opener import CloudDocsFileOpener
from dropbox.client.device_info import get_process_start_time
from dropbox.client.features.external_drive_backup.device_anchor_opener import DeviceAnchorOpener
from dropbox.client.features.ignore_files.file_opener import IgnoreRulesFileOpener
from dropbox.client.file_activation.constants import FileActivationError
from dropbox.client.file_activation.events import FileOpenInfo
from dropbox.client.file_activation.interface import ExtensionHandler
from dropbox.client.gandalf import Gandalf
from dropbox.client.per_node_metadata.link_node import LinkNodeOpener
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.client.util import launch_app
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.account_manager import AccountManager
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.reporting import report_app_framework_event_restricted
from dropbox.functions import frozendict
from dropbox.infinite.constants import InfiniteEventType
from dropbox.infinite.util import report_infinite_event
from dropbox.platform import IS_MAC
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.infinite.recall_events import InfiniteRecallEvent, InfiniteRecallStatus, InfiniteRecallType
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUIEvent, InfiniteUIEventType, InfiniteUIRequest
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties
from dropbox.sync_event.report import truncated_hash
from dropbox.threading import Lock
from dropbox.trace import TRACE
if IS_MAC:
    from macinfinite.xattr import ENOATTR, getxattr, removexattr

def extension(filename = None):
    return os.path.splitext(filename)[1]

OPENWITH_XATTR_NAME = 'com.apple.LaunchServices.OpenWith'
NUCLEUS_PLACEHOLDER_XATTR = 'com.dropbox.placeholder'
FP_PACKAGE_OPENER_XATTR = 'com.dropbox.package'
FP_PACKAGE_OPENER_CONFLICTABLE_XATTR = 'com.dropbox.package.conflictable'
MAX_RECALL_ID = 0x7FFFFFFFFFFFFFFF

def has_placeholder_xattr(filename = None):
    pass
# WARNING: Decompyle incomplete


def has_openwith_xattr(filename = None):
    pass
# WARNING: Decompyle incomplete


def remove_openwith_xattr(filename = None):
    pass
# WARNING: Decompyle incomplete


def has_fp_package_opener_xattr(filename = None):
