# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

from __future__ import absolute_import
import binascii
import os
import random as insecure_random
import struct
import threading
import time
from os.path import isdir as _isdir
from typing import Any, Dict, FrozenSet, List, MutableMapping, NamedTuple, Optional, Set, Text, Tuple
import objc
from AppKit import NSNumber, NSRunningApplication
from CoreFoundation import CFRunLoopPerformBlock, CFRunLoopWakeUp, kCFRunLoopCommonModes
from FinderSync import FIFinderSyncController
from Foundation import NSBundle, NSCocoaErrorDomain, NSData, NSDate, NSDefaultRunLoopMode, NSDistributedNotificationCenter, NSExtension, NSFileReadNoSuchFileError, NSFileWriteOutOfSpaceError, NSKeyedArchiver, NSKeyedUnarchiver, NSMachBootstrapServer, NSMachPort, NSMutableArray, NSMutableData, NSNotification, NSNotificationCenter, NSObject, NSPortDidBecomeInvalidNotification, NSPortMessage, NSRunLoop, NSSet, NSURL
from build_number import dropbox_version
from build_number.features import feature_enabled
from dropbox.client.background_worker import on_background_thread
from dropbox.client.context_menu.wrapper import ContextMenuConfigWrapper
from dropbox.client.gandalf import Gandalf
from dropbox.client.high_trace import send_finder_crashes
from dropbox.client.shell.base import ShellControllerBase
from dropbox.client.ui.cocoa.extensions import NSTimer
from dropbox.client.ui.icon_overlay import do_context_action, encode_menu, get_option_group, get_toolbar_option_group
from dropbox.client.util.mac import get_dock_persistent_others_map, user_has_icloud_drive, user_has_icloud_drive_desktop_sync, user_has_icloud_drive_documents_sync
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.event import report, report_aggregate_event
from dropbox.event_names import FINDER_SERVER_STATUS_EVENT
from dropbox.exception.exception_decorators import handle_exceptions, handle_exceptions_ex_2
from dropbox.exception.reporting import report_bad_assumption, report_exception, report_rare_event
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.gui import assert_not_on_main_thread, event_handler
from dropbox.mac.internal import autoreleasepool, MacError
from dropbox.mac.version import MAC_BUILD, MAC_VERSION, MOJAVE, VENTURA
from dropbox.preferences import DESKTOP_CUSTOMIZABLE_CONTEXT_MENU_STORMCROW_ENABLED
from dropbox.proto.nucleus.common_api_types_pb2 import LookupSyncIconReply
from dropbox.sync_engine_boundary.file_locking.file_locking_types import FileLockState
from dropbox.sync_engine_boundary.types.local_props import FileSyncStatus
from dropbox.sync_root.events.reporter import report_sync_root_event
from dropbox.sync_root.events.types import ExtraInfo, SyncRootEvent, SyncRootEventType
from dropbox.sync_root.interface import SyncRootType
from dropbox.sync_root.types import SyncRootInfo
from dropbox.threading import RLock
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter

class PortRegistrationError(Exception):
    pass


class RemotePortTimeoutError(Exception):
    pass


class UnrecognizedMessageError(Exception):
    pass


class ExtensionNotRegisteredError(Exception):
    pass

CRASH_LOGS_DIRECTORY = os.path.expanduser('~/Library/Logs/DiagnosticReports')
CRASH_LOG_MAX_AGE = 60
ICLOUD_FOLDER_PATH = '~/Library/Mobile Documents'
ICLOUD_DESKTOP_XATTR_NAME = 'com.apple.icloud.desktop'
EXTERNAL_FINDER_SYNC_BUILD_FEATURE = 'finder-sync-external-context-menus'
EXAMPLE_MANAGED_MOUNT_ROOTS = ('/Users',)
FINDER_SYNC_HOST_BUNDLE_IDENTIFIER = 'com.getdropbox.%s.findersyncintegration' % dropbox_version.key.lower()
LEGACY_FINDER_SYNC_EXTENSION_BUNDLE_IDENTIFIER = 'com.getdropbox.%s.garcon' % dropbox_version.key.lower()
HOSTED_FINDER_SYNC_EXTENSION_BUNDLE_IDENTIFIER = 'com.getdropbox.%s.findersyncintegration.garcon' % dropbox_version.key.lower()

def external_finder_sync_enabled():
    return feature_enabled(EXTERNAL_FINDER_SYNC_BUILD_FEATURE)


class FinderSyncExtensionLocation(NamedTuple):
    path: 'Text' = 'FinderSyncExtensionLocation'


def _bundled_hosted_finder_sync_extension():
    if not external_finder_sync_enabled():
        return None
    main_bundle_path = NSBundle.mainBundle().bundlePath()
# WARNING: Decompyle incomplete


def ensure_finder_sync_host_registered(local_config = None):
    if not external_finder_sync_enabled():
        return False
    extension = _bundled_hosted_finder_sync_extension()
# WARNING: Decompyle incomplete


def _runningGarconApplications(hosted = None):
    autoreleasepool()
    bundle_identifier = HOSTED_FINDER_SYNC_EXTENSION_BUNDLE_IDENTIFIER if hosted else LEGACY_FINDER_SYNC_EXTENSION_BUNDLE_IDENTIFIER
    applications = NSRunningApplication.runningApplicationsWithBundleIdentifier_(bundle_identifier)
    None(None, None)
    return 
    with None:
        if not (lambda .0: pass# WARNING: Decompyle incomplete
), applications():
            pass

EFFinderServerDidBecomeAvailableNotification = 'EFFinderServerDidBecomeAvailableNotification'

def _destroy_mounted_sync_root_registration(mount_path = None):
    pass
# WARNING: Decompyle incomplete


def _update_mounted_sync_root_registration(mount_paths = None):
    TRACE('[findersync] Updating mounts paths in FinderSync cache')
    autoreleasepool()
# WARNING: Decompyle incomplete


def finder_extensions_log_path():
    autoreleasepool()
    container_path = NSBundle.ef_syncGroupContainerURL().path()
    None(None, None)
    return 
    with None:
        if not None, os.path.join(container_path, 'logs', '0'):
            pass


class EFFinderServer(NSObject):
    _SUPPORTED_EXTENSION_POINT_VERSIONS = ('1.0',)
    EXTENSION_BUNDLE_IDENTIFIER = LEGACY_FINDER_SYNC_EXTENSION_BUNDLE_IDENTIFIER
    GOOGLE_DRIVE_EXTENSION_BUNDLE_IDENTIFIER = 'com.google.GoogleDrive.FinderSyncAPIExtension'
    TRANSFER_SHARE_EXTENSION_BUNDLE_IDENTIFIER = f'''com.getdropbox.{dropbox_version.key.lower()}.TransferExtension'''
    VERIFY_TIMER_PERIOD = 300
    VERIFY_TIMER_MAX_COUNT = 5
    PORT_SEND_TIMEOUT = 5
    SESSION_ID_LEN = 32
    HEARTBEAT_DELAY = 2.8
    HEARTBEAT_VALIDATION_DELAY = 20
    HEARTBEAT_TOKEN_RANGE = (-999999, -1)
    MESSAGE_CONNECT = 0
    MESSAGE_RESPONSE = 1
    MESSAGE_HEALTH_WATCHDOG = 10
    MESSAGE_HEALTH_HEARTBEAT = 11
    MESSAGE_REQUEST_WATCH_SET = 100
    MESSAGE_REQUEST_FILE_STATUS = 101
    MESSAGE_REQUEST_CONTEXT_MENU_OPTIONS = 102
    MESSAGE_REQUEST_TOOLBAR_CONTEXT_MENU_OPTIONS = 103
    MESSAGE_PERFORM_ACTION = 104
    MESSAGE_OBSERVING_URL = 105
    MESSAGE_INVALIDATE_WATCH_SET = 200
    MESSAGE_INVALIDATE_BADGE = 201
    MESSAGE_INVALIDATE_ALL_BADGES = 202
    _LOCKED_FILE_STATUS = 99
    
    def __new__(cls = None, app = None, sync_engine_adapter = None):
        return EFFinderServer.alloc().initWithApp_syncEngine_(app, sync_engine_adapter)

    
    def initWithApp_syncEngine_(self = None, app = None, sync_engine_adapter = None):
        self = objc.super(EFFinderServer, self).init()
        if not self:
            return None
        self._app = None
        self._sync_engine_adapter = sync_engine_adapter
        self._local_config = self._app.config_manager.local_config(None).config_dict
        self._root_manager = self._app.root_manager
        self._context_menu_config = ContextMenuConfigWrapper(self._app.config_manager.local_config(None), self._app.gandalf.allows(DESKTOP_CUSTOMIZABLE_CONTEXT_MENU_STORMCROW_ENABLED, treat_control_as_off = True))
        self._lock = RLock()
        self._listening = False
        self._run_loop = None
        self._local_port = None
        self._remote_ports = set()
        self._hosted_finder_sync_active = False
        self._managed_mount_roots = frozenset()
        self._file_provider_roots = None
        self._file_provider_roots_generation = 0
        self._verify_count = 0
        self._verify_timer = None
        self._session_id = binascii.hexlify(os.urandom(self.SESSION_ID_LEN))
        self._expected_tokens = []
       