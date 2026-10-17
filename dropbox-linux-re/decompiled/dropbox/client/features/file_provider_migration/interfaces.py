# Source Generated with Decompyle++
# File: interfaces.pyc (Python 3.11)

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional
from dropbox.client.features.file_provider_migration.types import FileProviderMigrationState

class FPMigrationStateStoreInterface(ABC):
    set_fp_migration_state = (lambda self = None, state = None: pass)()
    get_fp_migration_state = (lambda self = None, default = None: pass)()
    set_auto_migration_deadline_if_unset = (lambda self = None, deadline = None, override = abstractmethod: pass)()
    get_auto_migration_deadline = (lambda self = None: pass)()
    set_auto_migration_scheduled_date = (lambda self = None, date = None: pass)()
    get_auto_migration_scheduled_date = (lambda self = None: pass)()
    get_auto_migration_opt_out = (lambda self = None: pass)()
    get_file_provider_opt_out_during_sign_in = (lambda self = None: pass)()

