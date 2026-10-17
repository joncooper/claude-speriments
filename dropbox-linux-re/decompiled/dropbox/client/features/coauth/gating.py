# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.coauth.constants import COAUTH_EXTENSIONS, COAUTH_FEATURE
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.functions import file_extension

class CoauthFeature:
    is_coauth_enabled_for_any_user = (lambda machine_context = None, account_being_unlinked = None: for account_model in machine_context.account_manager.account_models.values():
if account_being_unlinked and account_model.user_context.account_id == account_being_unlinked.account_id:
continueif CoauthFeature.is_coauth_enabled_for_user(account_model.user_context):
TrueFalse)()
    is_coauth_enabled_for_user = (lambda user_context = None: user_context.stormcrow.allows(COAUTH_FEATURE))()
    path_has_coauth_extension = (lambda path = None: file_extension(path).lower() in COAUTH_EXTENSIONS)()

