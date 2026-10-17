# Source Generated with Decompyle++
# File: meta_engine_utils.pyc (Python 3.11)

import json
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.fenix.generated_types.shared_pb2 import AccountRole, AuthenticatedAccount as ProtoAuthenticatedAccount
from dropbox.client.fenix.types.account import AuthenticatedAccount
from dropbox.client.multiaccount.role import Roles

def proto_to_authenticated_account_dict(proto = None):
    role_str = 'personal' if proto.role == AccountRole.PERSONAL else 'business'
# WARNING: Decompyle incomplete


def account_to_proto(account = None):
    pass
# WARNING: Decompyle incomplete

