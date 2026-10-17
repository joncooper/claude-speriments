# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.databases import reinitialize_databases
from dropbox.client.unlink_cookie import write_unlink_cookie_no_sync_engine
from dropbox.trace import TRACE

def clear_all_sync_state(local_config = None, account = None):
    TRACE('Clearing all sync / account state (root_ns, email, host_secret, filecache)')
# WARNING: Decompyle incomplete

