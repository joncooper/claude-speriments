# Source Generated with Decompyle++
# File: nucleus_local_config.pyc (Python 3.11)

from typing import AbstractSet, Any, Callable, Dict, List, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.config import ConfigDict
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.mapreduce import DBKeyStore
from dropbox.model.types import FileId
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface

class _MemoryLocalConfig(LocalConfigurationInterface):
    
    def __init__(self = None, account = None, real_config = None):
        self._MemoryLocalConfig__real_local_config = real_config
        config_filename = 'file:memdb_{}?mode=memory&cache=shared'.format(account.account_id)
        self._MemoryLocalConfig__config_dict = ConfigDict(config_filename)

    appdata_path = (lambda self = None: self._MemoryLocalConfig__real_local_config.appdata_path)()
    appdata_path = (lambda self = None, str = None: pass)()
    unlink_cookie = (lambda self = None: pass)()
    unlink_cookie = (lambda self = None, _ = None: pass)()
    instance_id = (lambda self = None: self._MemoryLocalConfig__real_local_config.instance_id)()
    instance_id = (lambda self = None, _ = None: pass)()
    config_dict = (lambda self = None: self._MemoryLocalConfig__config_dict)()
    config_dict = (lambda self = None, _ = None: pass)()
    keystore = (lambda self = None: self._MemoryLocalConfig__real_local_config.keystore)()
    keystore = (lambda self = None, _ = None: pass)()
    has_secondary_creds = (lambda self = None: self._MemoryLocalConfig__real_local_config.has_secondary_creds)()
    
    def load_config(self = None, is_first_run = None, with_context_awareness = None):
        return self.config_dict

    
    def migrate_config(self = None):
        pass

    
    def create_keystore(self = None, is_primary = None):
        return self.keystore

    
    def load_unlink_cookie(self = None, is_primary = None):
        pass

    
    def get_host_secret(self = None):
        return self._MemoryLocalConfig__real_local_config.get_host_secret()

    
    def get_dropbox_path(self = None):
        return self._MemoryLocalConfig__real_local_config.get_dropbox_path()

    
    def save_app_hidden_fileids(self = None, nucleus_interface = None, account = None):
        pass

    
    def get_app_hidden_fileids(self = None):
        pass

    
    def migrate_app_hidden_fileids_from_login(self = None, hidden_set = None):
        pass

    
    def update_account_info(self = None, account = None):
        pass

    
    def get_config_dict(self = None):
        return { }

    
    def update_preferences(self = None, prefs = None, force_callbacks = None, skip_pwd_check = (False, False)):
        pass

    
    def add_pref_callback(self = None, key_re_template = None, callback = None):
        pass

    
    def remove_pref_callback(self = None, key_re_template = None, callback = None):
        pass


