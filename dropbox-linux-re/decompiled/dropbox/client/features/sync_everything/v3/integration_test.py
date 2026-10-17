# Source Generated with Decompyle++
# File: integration_test.pyc (Python 3.11)

import os
import traceback
from functools import partial
from typing import Any, Callable, Dict, IO, List, Mapping, Optional, Text, TypeVar
from build_number.platform import IS_MAC, IS_WINDOWS
from dropbox import fsutil
from dropbox.client.authentication.account import Account
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.backup_common.errors import report_exception_and_ignore
from dropbox.client.features.computer_backup.constants import CBFolderId
from dropbox.client.features.debug_menu_override_stormcrow.override_stormcrow import StormcrowOverride
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.sync_everything.constants import DeviceStatus, InvariantCheckMode, KnownFolderRequest, SYNC_EVERYTHING_DEVICE_CONFLICT_NAME_OVERRIDE, SYNC_EVERYTHING_INVARIANT_ADD_IMMUTABLE, SYNC_EVERYTHING_INVARIANT_CLEAR_IMMUTABLE
from dropbox.client.features.sync_everything.gating import get_known_folders
from dropbox.client.features.sync_everything.v3.async_tools import future_function, future_sequence
from dropbox.client.features.sync_everything.v3.device_state import DeviceState, KnownFolder
from dropbox.client.features.sync_everything.v3.event_reporter import PerformanceEventReporter
from dropbox.client.features.sync_everything.v3.fs_utils import fast_over_quota_check, is_directory_overquota, OverquotaTimer
from dropbox.client.features.sync_everything.v3.nodep_utils import SE_WARN
from dropbox.client.features.sync_everything.v3.server_interface import DeviceNotFoundError, DeviceStatusError, parse_apiv2_error, ServerInterface
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingEvent
from dropbox.client.features.sync_everything.v3.sync_everything_manager import SyncEverythingManager
from dropbox.client.features.sync_everything.v3.utils import clear_immutable, fixup_dock, paths_have_immutable_flag, wait_for_predicate, wrap_with_retries, wrap_with_retries_op
from dropbox.client.features.sync_everything.view_model.bridge_gen.bridge_interface_folder_status import FolderStatusBridgeInterface
from dropbox.client.features.sync_everything.view_model.bridge_gen.bridge_interface_sync_everything_manager_view_model import Source
from dropbox.client.features.sync_everything.view_model.bridge_gen.merge_failure import MergeFailure
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_error import RedirectError
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.client.features.sync_everything.view_model.operation_result import OperationResult
from dropbox.client.features.sync_everything.view_model.sync_everything_manager_view_model import SyncEverythingManagerViewModel
from dropbox.client.notifications.legacy_notifications import SyncEverythingErrorStickyNotification
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.client_api.exceptions import HTTP409Error
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import FailedFuture, Future, FutureHelpers, ResolvedFuture, sleep_async
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.fsutil import FileSystem
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import OSFolderID
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
_RANDOM_SUFFIX = '_PZOfIa3wEg'
_DEVICE_NAME = 'IntegrationTest' + _RANDOM_SUFFIX
if IS_MAC:
    _BREADCRUMB_NAME = 'My files in Dropbox'
else:
    _BREADCRUMB_NAME = 'My files in Dropbox.lnk'
if IS_MAC:
    from dropbox.mac.version import CATALINA, MAC_VERSION
_TEST_FILE = 'TestFileContext.txt'
_TEST_OPEN_FILE = 'TestOpenFile.txt'
_MenuFunction = Callable[([], None)]
_T = TypeVar('_T')
assert_result = (lambda result = None, expected_result = None, expected_errors = future_function, skip_destroy = (None, None, False): pass# WARNING: Decompyle incomplete
)()

def default_path(folder = None, file_system = None):
    home_folder_path = file_system.make_path(os.path.expanduser('~'))
    return home_folder_path.join(folder.value)


def breadcrumb_path(folder = None, file_system = None):
    base_path = default_path(folder, file_system)
    return base_path.join(_BREADCRUMB_NAME)


def _file_path(folder = None, file_system = None):
    base_path = default_path(folder, file_system)
    return base_path.join(_TEST_FILE)


def _open_file_path(folder = None, file_system = None):
    base_path = default_path(folder, file_system)
    return base_path.join(_TEST_OPEN_FILE)


class TestContext(Destroyable):
    pass
# WARNING: Decompyle incomplete

with_stormcrow_set = (lambda context = None, name = None, enabled = future_function, test = ('context', 'TestContext', 'name', 'Text', 'enabled', 'bool', 'test', 'Callable[[], Future[_T]]', 'return', 'Future[_T]'): pass# WARNING: Decompyle incomplete
)()
_TestFunction = Callable[([
    TestContext], Future[None])]

def as_menu_action(app = None, name = None, func = None):
    pass
# WARNING: Decompyle incomplete

_WebdebuggerFunction = Callable[([], Future[bool])]

def as_webdebugger_test(app = None, name = None, func = None):
    pass
# WARNING: Decompyle incomplete


class SyncEverythingIntegrationTest:
    base_tests = (lambda cls = None: {
'Bind/Unbind Twice': cls.test_bind_unbind_twice,
'Bind/Unbind/Rename': cls.test_bind_unbind_rename,
'Force Quota Check': cls.test_force_over_quota,
'Fake Quota Check on Root': cls.test_quota_check_on_root,
'Quota Check with Broken Link': cls.test_quota_check_with_bad_symlink,
'Pause/Unpause/Bind': cls.test_pause_unpause_bind,
'VM Redirect/Update': cls.test_vm_redirect_update,
'IC Server Mismatch': cls.test_ic_server_mismatch,
'IC Local Mismatch': cls.test_ic_local_mismatch,
'Test Immutable Update': cls.test_immutable,
'Test Bind Anyways': cls.test_bind_anyways,
'Test Dock': cls.test_dock,
'Test Device Name Conflict Override': cls.test_device_name_conflict_override,
'Simple rebind': cls.test_rebind_simple,
'Rebind mismatch': cls.test_rebind_mismatched })()
    get_test_list = (lambda cls = None, app = None: pass# WARNING: Decompyle incomplete
)()
    get_webdebugger_tests = (lambda cls = None, app = None: pass# WARNING: Decompyle incomplete
)()
    cleanup = (lambda cls = None, context = None: context.clean_up())()
    test_bind_unbind_twice = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()
    test_bind_unbind_rename = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()
    test_force_over_quota = (lambda cls = None, context = None: session_id = random_session_id()user_context = context.user_contextreporter = PerformanceEventReporter(SyncEverythingEvent.overquota_check, session_id = session_id, account = user_context.account, metrics_reporter = user_context.metrics_reporter)reporter.wrap(fast_over_quota_check(user_context, get_known_folders(), reporter)).discard_value())()
    test_quota_check_on_root = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()
    test_quota_check_with_bad_symlink = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()
    test_pause_unpause_bind = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()
    test_vm_redirect_update = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()
    test_ic_server_mismatch = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()
    test_ic_local_mismatch = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()
    test_immutable = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()
    test_bind_anyways = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()
    test_dock = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()
    test_device_name_conflict_override = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()
    test_rebind_simple = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()
    test_rebind_mismatched = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()

