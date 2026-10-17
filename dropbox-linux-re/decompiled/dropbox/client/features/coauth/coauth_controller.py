# Source Generated with Decompyle++
# File: coauth_controller.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.coauth.gating import CoauthFeature
from dropbox.client.features.coauth.utils import create_coauth_registry_key_for_account_if_needed, create_coauth_registry_keys_global_if_needed, destroy_coauth_global_registry_key, destroy_coauth_registry_key_for_account, remove_dangling_account_keys_if_any, update_registry_key_root_path
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.shared.local_path import LocalPath
from dropbox.sync_root.accessor import RootManagerAccessor
from dropbox.trace import TRACE

class CoauthController(SingletonActor):
    pass
# WARNING: Decompyle incomplete

