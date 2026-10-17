# Source Generated with Decompyle++
# File: interface.pyc (Python 3.11)

from __future__ import annotations
from abc import ABCMeta, abstractmethod, abstractproperty
from typing import AbstractSet, Any, Callable, Dict, List, Optional
from dropbox.client.authentication.account_interface import AccountInterface
MYPY = False
if MYPY:
    from dropbox.client.config import ConfigDict
    from dropbox.client.mapreduce import DBKeyStore
    from dropbox.client.multiaccount.instance_database import InstanceConfig
    from dropbox.model.types import FileId
    from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface

class ConcurrentConfigurationEditError(Exception):
    pass


def LocalConfigurationInterface():
    '''LocalConfigurationInterface'''
    appdata_path = (lambda self = None: pass)()
    appdata_path = (lambda self = None, appdata_path = None: pass)()
    unlink_cookie = (lambda self = None: pass)()
    unlink_cookie = (lambda self = None, unlink_cookie = None: pass)()
    instance_id = (lambda self = None: pass)()
    instance_id = (lambda self = None, instance_id = None: pass)()
    config_dict = (lambda self = None: pass)()
    config_dict = (lambda self = None, config_dict = None: pass)()
    keystore = (lambda self = None: pass)()
    keystore = (lambda self = None, keystore = None: pass)()
    has_secondary_creds = (lambda self = None: pass)()
    load_config = (lambda self = None, is_first_run = None, with_context_awareness = abstractmethod: pass)()
    migrate_config = (lambda self = None: pass)()
    create_keystore = (lambda self = None, is_primary = None: pass)()
    load_unlink_cookie = (lambda self = None, is_primary = None: pass)()
    get_host_secret = (lambda self = None: pass)()
    get_dropbox_path = (lambda self = None: pass)()
    save_app_hidden_fileids = (lambda self = None, nucleus_interface = None, account = abstractmethod: pass)()
    get_app_hidden_fileids = (lambda self = None: pass)()
    migrate_app_hidden_fileids_from_login = (lambda self = None, hidden_set = None: pass)()
    update_account_info = (lambda self = None, account = None: pass)()
    get_config_dict = (lambda self = None: pass)()
    update_preferences = (lambda self = None, prefs = None, force_callbacks = abstractmethod, skip_pwd_check = (False, False): pass)()
    add_pref_callback = (lambda self = None, key_re_template = None, callback = abstractmethod: pass)()
    remove_pref_callback = (lambda self = None, key_re_template = None, callback = abstractmethod: pass)()
    
    def __getitem__(self = None, k = None):
        pass


LocalConfigurationInterface = <NODE:27>(LocalConfigurationInterface, 'LocalConfigurationInterface', metaclass = ABCMeta)

def ConfigurationManagerInterface():
    '''ConfigurationManagerInterface'''
    instance_config = (lambda self = None: pass)()
    corruptdb = (lambda self = None: pass)()
    corruptdb_secondary = (lambda self = None: pass)()
    corruptdb_name = (lambda self = None: pass)()
    
    def check_for_corruptdb(self = None, account = None):
        pass

    load_instance_data = (lambda self = None, account = None, instance_id = abstractmethod: pass)()
    local_config = (lambda self = None, account = None: pass)()
    load_secondary_config = (lambda self = None, secondary_account = None: pass)()
    clear_state_for_account = (lambda self = None, account = None: pass)()
    write_host_secret_to_instance_db = (lambda self = None, local_config = None, host_secret = abstractmethod: pass)()
    get_host_secret_from_instance_db = (lambda self = None, account = None: pass)()
    update_preferences = (lambda self = None, prefs = None: pass)()
    update_config_for_account = (lambda self = None, account = None, key = abstractmethod, value = ('account', 'Optional[AccountInterface]', 'key', 'str', 'value', 'Any', 'return', 'None'): pass)()
    get_config_value_for_account = (lambda self = None, account = None, key = abstractmethod, default_value = (None,): pass)()

ConfigurationManagerInterface = <NODE:27>(ConfigurationManagerInterface, 'ConfigurationManagerInterface', metaclass = ABCMeta)
