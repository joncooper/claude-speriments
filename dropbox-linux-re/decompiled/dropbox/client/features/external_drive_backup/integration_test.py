# Source Generated with Decompyle++
# File: integration_test.pyc (Python 3.11)

import traceback
from typing import Any, Callable, Dict, Mapping, Optional, Text, Tuple
from build_number.platform import IS_MAC
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.backup_common.constants import EDB_ANCHOR_EXTENSION
from dropbox.client.features.backup_common.errors import report_exception_and_ignore
from dropbox.client.features.backup_instance.constants import TEST_ONLY_BI_FEATURE_GATE_NAME, TEST_ONLY_DISABLED_VARIANT
from dropbox.client.features.backup_instance.gating import BackupInstanceFeature
from dropbox.client.features.backup_instance.manager import BackupInstanceManager
from dropbox.client.features.debug_menu_override_stormcrow.override_stormcrow import StormcrowOverride
from dropbox.client.features.external_drive_backup.edb_instance_wrapper import EDBInstanceWrapper
from dropbox.client.features.external_drive_backup.manager import ExternalBackupManager
from dropbox.client.features.external_drive_backup.trace import EDB_WARN
from dropbox.client.features.external_drive_backup.utils import list_anchors_by_uuid_active_engine
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_result import BackupResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.sync_everything.v3.async_tools import future_function, future_sequence
from dropbox.client.features.sync_everything.v3.utils import wait_for_predicate
from dropbox.client.multiaccount.role import Roles
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import assert_not_none, report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types import DeviceAnchorInfo, Filesystem, TempVolumeInfo
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
_MenuFunction = Callable[([], None)]

class TestContext(Destroyable):
    pass
# WARNING: Decompyle incomplete

_TestFunction = Callable[([
    TestContext], Future[None])]

def as_menu_action(app = None, name = None, func = None):
    pass
# WARNING: Decompyle incomplete

_WebdebuggerFunction = Callable[([
    bool], Future[bool])]

def as_webdebugger_test(app = None, name = None, func = None):
    pass
# WARNING: Decompyle incomplete


class ExternalDriveBackupIntegrationTest:
    base_tests = (lambda cls = None: {
'Basic Drive Backup': cls.test_basic_edb_backup,
'Basic Paired Scenario': cls.test_basic_paired_scenario })()
    get_test_list = (lambda cls = None, app = None: pass# WARNING: Decompyle incomplete
)()
    get_webdebugger_tests = (lambda cls = None, app = None: pass# WARNING: Decompyle incomplete
)()
    cleanup = (lambda cls = None, context = None: context.try_clean_up())()
    test_basic_edb_backup = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()
    test_basic_paired_scenario = (lambda cls = None, context = None: pass# WARNING: Decompyle incomplete
)()

