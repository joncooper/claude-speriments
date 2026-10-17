# Source Generated with Decompyle++
# File: impl.pyc (Python 3.11)

from typing import cast, Dict, List, Optional, Set, Type
from build_number.features import feature_enabled
from  import AccountManager, AccountUpdateType
from account_model import AccountModel
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface as LegacyAccountManagerInterface, ACCOUNTS_CHANGED_PRIORITY_POLARIS_ACCOUNT_MANAGER
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.configuration.manager import ConfigurationManager
from dropbox.client.gandalf import Gandalf
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.foundation.account_manager import AccountUpdate
from dropbox.foundation.account_manager.user_anchor_interface import UserAnchorInterface
from dropbox.foundation.context import ContextInterface
from dropbox.foundation.context.bridge_gen.bridge_interface_user_context import UserContextBridgeInterface
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.signals import Signal, StandardSignal
from dropbox.foundation.signals.event import EventSignal
from dropbox.threading import Lock
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.session_metadata.interface import LegacySessionMetadata

class AccountManagerImpl(Destroyable, AccountManager):
    pass
# WARNING: Decompyle incomplete

