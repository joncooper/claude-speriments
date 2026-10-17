# Source Generated with Decompyle++
# File: nucleus_types.pyc (Python 3.11)

from typing import Iterable, NamedTuple, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.multiaccount.role import Roles
from dropbox.proto.nucleus.sync_engine_pb2 import Account as NucleusAccount, NetworkConfig
from dropbox.sync_engine_boundary.hidden import HiddenSet
FileCacheDumpResult = NamedTuple('FileCacheDumpResult', [
    ('timed_out', bool),
    ('number_of_entries_processed', int),
    ('time_to_generate_ms', float),
    ('path', str),
    ('hidden_set', HiddenSet)])

class FileCacheDumpTimedOut(Exception):
    pass


def make_nucleus_account(account = None):
    proto = NucleusAccount()
# WARNING: Decompyle incomplete


def make_nucleus_network_config(account = None, linked_accounts = None):
    proto = NetworkConfig()
    if not account.paired_host_secret:
        proto.paired_host_key = ''
        if not linked_accounts:
            linked_accounts = sorted((), key = (lambda linked_account: 