# Source Generated with Decompyle++
# File: user.pyc (Python 3.11)

from typing import cast, Optional, Text
from apex.metrics import MetricsReporter
from bridge_gen.bridge_interface_user_context import UserContextBridgeInterface, UserContextObservableMixin
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.types import AccountId
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.configuration.wrapper import LocalConfigurationWrapper, MachineConfigurationWrapper
from dropbox.client.gandalf import Gandalf
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.account_flags.account_flags_creator import create_account_flags
from dropbox.foundation.context import Context, ContextInterface
from dropbox.foundation.session_metadata import SessionMetadata
from dropbox.foundation.stormcrow.user import UserStormcrow
MYPY = False
if MYPY:
    from dropbox.client.session_metadata.interface import LegacySessionMetadata

class UserContext(UserContextBridgeInterface, UserContextObservableMixin, Context):
    pass
# WARNING: Decompyle incomplete

