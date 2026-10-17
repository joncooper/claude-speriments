# Source Generated with Decompyle++
# File: bug_report_providers.pyc (Python 3.11)

import io
import textwrap
from abc import ABCMeta, abstractmethod
from pprint import pformat
from typing import Any, Dict, List, Optional, Text, Tuple, Union
from six import add_metaclass
from build_number import BUILDID, is_full_msix, is_store_managed, VERSION
from build_number.constants import MAIN_BUILDID
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.configuration.manager import ConfigurationManager
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.preference_settings import NotificationPreferencesStringMapping
from dropbox.client.shell.base import ShellControllerBase
from dropbox.client.status.interface import StatusControllerInterface
from dropbox.client.util import get_user_agent_dict
from dropbox.functions import python_version_string
from dropbox.nucleus.migration_state import SyncEngineStateManager
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_root.interface import SyncRootManagerInterface, SyncRootType
from dropbox.trace import debugging_features_are_enabled
BugReportProvider = <NODE:12>()

class BasicInformationProvider(BugReportProvider):
    
    def __init__(self = None):
        pass

    
    def key(self = None):
        return 'Basic information'

    
    def produce_info(self = None):
        if IS_MAC:
            pass
        elif IS_LINUX:
            pass
        
        pretty_platform = 'Windows'
        extra_platform_info = ''
        if IS_WINDOWS:
            WINDOWS_VERSION = WINDOWS_VERSION
            import dropbox.win32.version
            extra_platform_info = ' (build %s)' % WINDOWS_VERSION.build()
            if is_full_msix():
                extra_platform_info += ' (full-msix)'
            if is_store_managed():
                extra_platform_info += ' (store-managed)'
    # WARNING: Decompyle incomplete

    
    def report_externally(self = None):
        return True



class SyncInformationProvider(BugReportProvider):
    
    def __init__(self = None, root_manager = None):
        self._root_manager = root_manager
        self._sync_engine_version = { }

    
    def key(self = None):
        return 'Sync Information'

    
    def set_sync_engine_version(self = None, account = None, sync_engine_version = None):
        self._sync_engine_version[account] = sync_engine_version

    
    def produce_info(self = None):
        registered_versions = dict(self._sync_engine_version)
        if not registered_versions:
            return '<none>'
        ret = io.StringIO()
    # WARNING: Decompyle incomplete

    
    def report_externally(self = None):
        return True



class AccountsProvider(BugReportProvider):
    
    def __init__(self = None, account_manager = None):
        self._account_manager = account_manager

    
    def key(self = None):
        return 'accounts'

    
    def produce_info(self = None):
        accounts = []
        
        def dict_for_account(account = None):
            return {
                'host_int': account.host_int,
                'is_primary': account.is_primary }

        if len(self._account_manager.linked_accounts) > 0:
            for account in self._account_manager.linked_accounts:
                accounts.append(dict_for_account(account))
    # WARNING: Decompyle incomplete

    
    def report_externally(self = None):
        return True



class ShellExtensionProvider(BugReportProvider):
    
    def __init__(self = None, shell_controller = None):
        self._shell_controller = shell_controller

    
    def key(self = None):
        return 'Shell Extension Debug Information'

    
    def produce_info(self = None):
        return textwrap.indent(pformat(self._shell_controller.extension_debug_state()), '  ')



class NotificationSettingsProvider(BugReportProvider):
    
    def __init__(self = None, gandalf = None, config_manager = None):
        self._gandalf = gandalf
        self._config_manager = config_manager

    
    def set_gandalf(self = None, gandalf = None):
        self._gandalf = gandalf

    
    def produce_info(self = None):
        alternate_notification_string = f'''  Gandalf:\n    Service: {self._gandalf.allows_any_account('desktop-alternate-notification-service') if self._gandalf else False!s}\n'''
        preferences_string = '  Preferences:\n'
        local_config = self._config_manager.local_config(None)
        for pref, pref_string in NotificationPreferencesStringMapping.mapping():
            preferences_string = preferences_string + f'''    {pref_string!s}: {bool(local_config[pref])!s}\n'''
            return f'''{alternate_notification_string!s}\n{preferences_string!s}'''

    
    def key(self = None):
        return 'Notification Settings'

    
    def report_externally(self = None):
        return True



class StatusLabelsProvider(BugReportProvider):
    
    def __init__(self = None, status_controller = None):
        self._status_controller = status_controller

    
    def key(self = None):
        return 'Status labels'

    
    def produce_info(self = None):
        return ','.join(self._status_controller.get_status().labels.values())

    
    def report_externally(self = None):
        return True



class SyncEngineStatsProvider(BugReportProvider):
    KEY = 'Sync Engine Stats'
    
    def __init__(self = None, account_manager = None, sync_engine_adapter = None, config_manager = ('account_manager', 'AccountManagerInterface', 'sync_engine_adapter', 'SyncEngineAdapter', 'config_manager', 'ConfigurationManager', 'return', 'None')):
        self._account_manager = account_manager
        self._sync_engine_adapter = sync_engine_adapter
        self._config_manager = config_manager

    
    def key(self = None):
        return 'Sync engine stats'

    
    def produce_info(self = None):
        sync_engine_adapter = self._sync_engine_adapter
        account_manager = self._account_manager
        config_manager = self._config_manager
        lines = []
        account_infos = []
        for linked_account in account_manager.linked_accounts:
            nucleus_api = self._sync_engine_adapter.nucleus_api(linked_account)
            if not nucleus_api:
                continue
            stats = []
            account = nucleus_api.account
            upload_status = nucleus_api.get_upload_status_snapshot()
            download_status = nucleus_api.get_download_status_snapshot()
            speed_summary = '(upload %d kB/s, download %d kB/s)' % (upload_status.speed_kb_per_sec, download_status.speed_kb_per_sec)
            stats.append(('Current speed', speed_summary))
            se_state = SyncEngineStateManager.get_sync_engine_state(config_manager.local_config(account))
            if se_state:
                stats.append(('Migration state', se_state.name))
            bugreporter_stats = nucleus_api.get_bugreporter_stats().block(timeout = 5).result()
            for key, value in bugreporter_stats:
                stats.append((key, value))
            except Exception:
                e = None
                stats.append(('Error Gathering stats', str(e)))
                e = None
                del e
            except:
                e = None
                del e
            stats_str = '\n  '.join + (lambda .0: pass# WARNING: Decompyle incomplete
)(stats())
            account_infos.append((stats_str, account.email))
            if not account_infos:
                pass
            elif len(account_infos) == 1:
                lines.append(account_infos[0][0])
            else:
                for ent, email in account_infos:
                    lines.append(f'''{email!s}:\n{ent!s}''')
                    return '\n'.join(lines)

    
    def report_externally(self = None):
        return True


