# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import contextlib
import random as insecure_random
from typing import cast, Iterator, Optional, Text
from apex.metrics import MetricsReporter
from build_number.features import feature_enabled
from dropbox.client.authentication.account import Account
from dropbox.client.cloud_docs.constants import CLOUD_DOC_ID_CHARS, CLOUD_DOC_ID_LENGTH, HOST_ID_HASH_LENGTH
from dropbox.foundation.account_manager import AccountManager
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.platform_version import PLATFORM_VERSION
from dropbox.foundation.raii2 import destroying
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
nucleus_wrapper_for_path = (lambda account_manager = None, sync_engine_adapter = None, path = contextlib.contextmanager: pass# WARNING: Decompyle incomplete
)()

def user_context_for_path(account_manager = None, sync_engine_adapter = None, path = None):
    local_path = sync_engine_adapter.file_system.make_path(path)
    (account, _) = sync_engine_adapter.get_account_for_path(local_path)
    account_models = account_manager.account_models_all if feature_enabled('multi-team-accounts-prod') else account_manager.account_models
    account = cast(Account, account)
# WARNING: Decompyle incomplete


def generate_cloud_doc_id(account = None):
    host_id = str(account.host_int)
    hashed_host_id = str(hash(host_id))[-HOST_ID_HASH_LENGTH:]
    rand_id = ''.join(insecure_random.choices(CLOUD_DOC_ID_CHARS, k = CLOUD_DOC_ID_LENGTH))
    return hashed_host_id + ':' + rand_id


def create_cloud_docs_metrics_reporter(metrics_reporter = None):
    return metrics_reporter.child({
        'platform_version': PLATFORM_VERSION })

