# Source Generated with Decompyle++
# File: implementation.pyc (Python 3.11)

from typing import Dict
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.configuration.manager import ConfigurationManager
from dropbox.client.features.download_on_demand.dod_logger import DownloadOnDemandLogger
from dropbox.client.features.download_on_demand.helpers import set_ss_autoevict_off
from dropbox.client.features.download_on_demand.logging_helpers import get_or_create_dod_session_id
from dropbox.client.gandalf import Gandalf
from dropbox.infinite import dod_for_non_fp_enabled

class DownloadOnDemandController:
    
    def __init__(self = None, account_manager = None, config_manager = None, gandalf = ('account_manager', 'AccountManagerInterface', 'config_manager', 'ConfigurationManager', 'gandalf', 'Gandalf', 'return', 'None')):
        self._account_manager = account_manager
        self._config_manager = config_manager
        self._gandalf = gandalf
        self._account_manager.add_accounts_changed_callback(self._on_accounts_changed)

    
    def _on_accounts_changed(self = None, account = None, change_type = None):
        if change_type == AccountChangeType.LINK:
            self._perform_dod_setup_if_eligible(account)
            self._gandalf.add_on_changed_callback(self.on_gandalf_changed, account)
            return None

    
    def on_gandalf_changed(self = None):
        for account in self._account_manager.linked_accounts:
            self._perform_dod_setup_if_eligible(account)
            return None

    
    def _perform_dod_setup_if_eligible(self = None, account = None):
        local_config = self._config_manager.local_config(account)
    # WARNING: Decompyle incomplete


