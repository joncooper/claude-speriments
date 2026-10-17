# Source Generated with Decompyle++
# File: formatted_traces.pyc (Python 3.11)

import errno
import getpass
import os
import uuid
from typing import Dict, Iterable, List, Mapping, Optional, Text, Tuple, Union
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.configuration.interface import ConfigurationManagerInterface, LocalConfigurationInterface
from dropbox.client.features.app_model_watcher.app_model_watcher import ApplicationModelWatcher
from dropbox.client.features.backup_instance.utils import best_effort_user_has_backup_root
from dropbox.client.features.external_drive_backup.edb_instance_wrapper import EDBInstanceWrapper
from dropbox.client.features.smarter_smart_sync.constants import SS_AUTOEVICT_ADMIN_POLICY_NAME, SS_AUTOEVICT_POLICY_NAME, SSAutoevictPolicy
from dropbox.client.features.smarter_smart_sync.feature import SmarterSmartSyncFeature
from dropbox.client.features.smarter_smart_sync.smarter_smart_sync_policy import SmarterSmartSyncPolicyController
from dropbox.client.gandalf import Gandalf
from dropbox.client.ui.common.preferences import get_harmony_level_from_local_config
from dropbox.client.util import get_drives, get_free_space
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.exceptions import DropboxServerError, TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.app_model.app_model import ApplicationModel
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, IncompleteFutureException, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.functions import make_str, make_unicode
from dropbox.infinite.preferences import InfinitePolicy, InfinitePolicyController
from dropbox.model.types import FileId, NsId
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.preferences import OPT_PHOTO
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.types.local_props import LocalLocationProperties
from dropbox.trace import TRACE
if IS_WINDOWS:
    from dropbox.client.util.win import formatted_trace
    from dropbox.win32.internal import is_admin
if IS_LINUX:
    from lib.linuxffi.sys.api import statfs as linux_statfs
Header = List[Optional[str]]
Row = Iterable[Union[(str, NsId, None)]]
Content = Iterable[Row]
Stat = Tuple[(Header, Content)]

def report_statfs(path = None):
    if not IS_LINUX:
        return None
    
    try:
        TRACE('reporting statfs on %s', path)
        st = linux_statfs(path)
        report('statfs', fs_type_raw = st.f_type)
        return None
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.TRACES)
        return None



def get_free_space_formatted(folder = None):
    
    try:
        free_bytes = get_free_space(folder)
    except OSError:
        e = None
        if e.errno not in (errno.EACCES, errno.ENOENT):
            report_exception(component = DesktopComponent.TRACES)
        del e
        return None
        None = 
        del e
        except Exception:
            e = None
            del e
            return None
            None = 
            del e

    kb = free_bytes / 1024
    mb = kb / 1024
    gb = mb / 1024
    if gb > 1:
        return '%.1f G' % gb
    if None > 1:
        return '%s M' % mb
    if None > 1:
        return '%s K' % kb
    return None % free_bytes


def get_drive_info():
    drive_info = []
    for d, i, a, _ in get_drives():
        row = [
            ' OR '.join,
            (lambda .0: [ make_str(element) for element in .0 ])(a())]
        row.append(get_free_space_formatted(drive_dir))
        drive_info.append(row)
        return drive_info


class FormattedTraceReporter(object):
    
    def __init__(self, buildno, conn, local_config, account_manager = None, config_manager = None, app_model_watcher = None, require_sync_engine = (True, None), dummy_account = ('buildno', 'str', 'conn', 'DropboxConnection', 'local_config', 'LocalConfigurationInterface', 'account_manager', 'Optional[AccountManagerInterface]', 'config_manager', 'Optional[ConfigurationManagerInterface]', 'app_model_watcher', 'Optional[ApplicationModelWatcher]', 'dummy_account', 'Optional[Account]')):
        self.buildno = buildno
        self.conn = conn
        self.sync_engine_adapter = None
        self.local_config = local_config
        self.drive_info = None
        self.account_manager = account_manager
        self.config_manager = config_manager
        self.dummy_account = dummy_account
        self.require_sync_engine = require_sync_engine
        self._gandalf = None
        self._app_model_watcher = app_model_watcher

    
    def _get_app_model(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _context_for_account(self = None, account = None):
        app_model = self._get_app_model()
        if not app_model:
            return None
        model = None.account_manager.account_models.get(account)
        if not model:
            return None
        return None.user_context

    
    def set_gandalf(self = None, gandalf = None):
        self._gandalf = gandalf

    
    def on_sync_engine_ready(self = None, sync_engine_adapter = None, account = None):
        self.sync_engine_adapter = sync_engine_adapter

    
    def run(self = None):
        pass
    # WARNING: Decompyle incomplete


