# Source Generated with Decompyle++
# File: dynamic_contents_manager.pyc (Python 3.11)

from dropbox.client.authentication.account import Account
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.background_worker import on_background_thread
from dropbox.client.dynamic_contents.model.dynamic_texts import DynamicTexts
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.i18n import get_current_code
from dropbox.threading import RWLock
MYPY = False
if MYPY:
    from typing import Any, Dict, Optional, Text
    from dropbox.client.authentication.interface import AccountManagerInterface
    from dropbox.client.gandalf import Gandalf
    from dropbox.client.hourly_refresh import HourlyRefreshController
    from dropbox.client_api.dropbox_connection import DropboxConnection

class DynamicContentsManager(object):
    
    def __init__(self, account_manager = None, hourly_refresh_controller = None, gandalf = None, conn = ('account_manager', 'AccountManagerInterface', 'hourly_refresh_controller', 'HourlyRefreshController', 'gandalf', 'Gandalf', 'conn', 'DropboxConnection', 'return', 'None')):
        self._dynamic_texts_mapping = { }
        self._account_manager = account_manager
        self._hourly_refresh_controller = hourly_refresh_controller
        self._gandalf = gandalf
        self._conn = conn
        self._hourly_refresh_controller.add_refresh_callback(self._hourly_refresh_callback)
        self._account_manager.add_accounts_changed_callback(self._dynamic_contents_account_callback)
        self._lock = RWLock()

    
    def update_dynamic_texts(self = None, account = None, texts = None):
        self._lock.acquire_write()
        
        try:
            if account not in self._dynamic_texts_mapping:
                self._dynamic_texts_mapping[account] = DynamicTexts()
            self._lock.release_write()
        except:
            self._lock.release_write()

        self._dynamic_texts_mapping[account].update_texts_batch(texts)

    
    def get_dynamic_texts(self = None, account = None):
        if self._gandalf.get_variant('desktop-dynamic-texts', account = account) == 'ON':
            self._lock.acquire_read()
            
            try:
                self._lock.release_read()
                return self._dynamic_texts_mapping.get(account, None)
            except:
                self._lock.release_read()
                return None


    
    def remove_dynamic_texts(self = None, account = None):
        self._lock.acquire_write()
        
        try:
            if account not in self._dynamic_texts_mapping:
                report_bad_assumption(f'''[{account!r}] is not in dynamic texts dict [{self._dynamic_texts_mapping!r}]''')
            self._dynamic_texts_mapping.pop(account, None)
            self._lock.release_write()
            return None
        except:
            self._lock.release_write()


    sync_dynamic_texts = (lambda self = None, account = None, conn = on_background_thread(): try:
texts = conn.api_v2_get_dynamic_texts(account, get_current_code())self.update_dynamic_texts(account, texts)Noneexcept Exception:
report_exception(severity = Severity.WARN, account = account, component = DesktopComponent.UNKNOWN)None)()
    
    def _dynamic_contents_account_callback(self, account, account_type):
        if account_type == AccountChangeType.REMOVE:
            self.remove_dynamic_texts(account)
            return None

    
    def _hourly_refresh_callback(self = None, *n, **kw):
        for account in self._account_manager.linked_accounts:
            if self._gandalf.get_variant('desktop-dynamic-texts', account = account) == 'ON':
                self.sync_dynamic_texts(account, self._conn)
                continue
            self._dynamic_texts_mapping.pop(account, None)
            return None


