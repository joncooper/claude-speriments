# Source Generated with Decompyle++
# File: fp_shadow_migration_interface.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Iterable
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.configuration.interface import ConfigurationManagerInterface
from dropbox.foundation.futures import Future
from dropbox.proto.nucleus.app_service_pb2 import FPCutoverDryRunExtraData, StartFPCutoverDryRunReply, StartFPCutoverReply

class FPShadowMigrationControllerInterface(ABC):
    create_shadow_domain = (lambda self = None, account = None, all_accounts = abstractmethod: pass)()
    cancel_migration = (lambda self = None, account = None: pass)()
    run_cutover_dryrun = (lambda self = None, account = None, extra_data = abstractmethod: pass)()
    run_cutover = (lambda self = None, account = None: pass)()
    _set_hidden = (lambda self = None, account = None, hidden = abstractmethod: pass)()
    
    def _set_last_dryrun_migration_generation(self = None, account = None, generation = None):
        pass



class FPShadowPostMigrationControllerInterface(ABC):
    run_post_migration_actions = (lambda self = None, account = None, change_type = abstractmethod: pass)()


class FPShadowMigrationDfcControllerInterface(ABC):
    should_run_dfc = (lambda account_manager = None, config_manager = staticmethod: pass)()()
    register_periodic_task = (lambda self: pass)()

