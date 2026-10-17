# Source Generated with Decompyle++
# File: migration_session.pyc (Python 3.11)

import uuid
from typing import Any, Dict, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.file_provider_migration.constants import FILE_PROVIDER_SESSION_ID_CONFIG_KEY, FILE_PROVIDER_SESSION_KEY
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase
from dropbox.threading import Lock
from dropbox.trace import TRACE

class FPMigrationSessionData:
    __SESSION_DATA_LOCK = Lock()
    
    def __init__(self = None, session_id = None):
        self.session_id = session_id
        self.syncing_time = { }
        self.notifications_dismissed = False
        self.migration_requested_event_fallback_extra = None

    set_migration_requested_event_fallback = (lambda cls = None, local_config = None, extra = classmethod: FPMigrationSessionData.__SESSION_DATA_LOCKsession_data = cls._get_or_create_fp_session(local_config)session_data.migration_requested_event_fallback_extra = extralocal_config.config_dict[FILE_PROVIDER_SESSION_KEY] = session_dataTRACE('Set migration requested event fallback for session_id[%r]', session_data.session_id)None(None, None)Nonewith None:
if not None:
pass)()
    flush_migration_requested_event = (lambda cls = None, local_config = None: FPMigrationSessionData.__SESSION_DATA_LOCKsession_data = cls._get_or_create_fp_session(local_config)session_data.migration_requested_event_fallback_extra = Nonelocal_config.config_dict[FILE_PROVIDER_SESSION_KEY] = session_dataTRACE('Flushed migration requested event fallback for session_id[%r]', session_data.session_id)None(None, None)Nonewith None:
if not None:
pass)()
    update_syncing_time = (lambda cls = None, local_config = None, minutes = classmethod, account = ('local_config', 'LocalConfigurationInterface', 'minutes', 'int', 'account', 'AccountInterface', 'return', 'None'): FPMigrationSessionData.__SESSION_DATA_LOCKsession_data = cls._get_or_create_fp_session(local_config)key = cls._get_syncing_time_key(account)# WARNING: Decompyle incomplete
)()
    get_syncing_time = (lambda cls = None, primary_config = None, account = classmethod: FPMigrationSessionData.__SESSION_DATA_LOCKkey = cls._get_syncing_time_key(account)session_data = cls._get_or_create_fp_session(primary_config)None(None, None)with None:
if not None, session_data.syncing_time.get(key, 0):
pass)()
    mark_syncing_time_done = (lambda cls = None, primary_config = None, account = classmethod: FPMigrationSessionData.__SESSION_DATA_LOCKkey = cls._get_syncing_time_key(account)session_data = cls._get_or_create_fp_session(primary_config)session_data.syncing_time[key] = SyncPhase.SYNCEDNone(None, None))()
    _get_syncing_time_key = (lambda cls = None, account = None: 'primary' if account.is_primary else 'secondary')()
    set_notifications_dismissed = (lambda cls = None, local_config = None, is_dismissed = classmethod: FPMigrationSessionData.__SESSION_DATA_LOCKsession_data = cls._get_or_create_fp_session(local_config)session_data.notifications_dismissed = is_dismissedlocal_config.config_dict[FILE_PROVIDER_SESSION_KEY] = session_dataNone(None, None)Nonewith None:
if not None:
pass)()
    _get_session_id_from_old_format = (lambda cls = None, local_config = None: pass# WARNING: Decompyle incomplete
)()
    _get_or_create_fp_session = (lambda cls = None, local_config = None: pass# WARNING: Decompyle incomplete
)()
    get_or_create_fp_session = (lambda cls = None, local_config = None: cls.__SESSION_DATA_LOCKNone(None, None)with None:
if not None, cls._get_or_create_fp_session(local_config):
pass)()

