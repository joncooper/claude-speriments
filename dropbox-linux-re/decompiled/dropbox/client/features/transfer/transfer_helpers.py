# Source Generated with Decompyle++
# File: transfer_helpers.pyc (Python 3.11)

from datetime import datetime, timedelta
from typing import List, Optional, Text
from dropbox.client.authentication.account import Account
from dropbox.client.features.transfer.constants import EXPIRATION_OPTION_METADATA_NAME, SHOULD_NOTIFY_CREATOR_ON_DOWNLOAD_METADATA_NAME
from dropbox.client.features.transfer.network_utils import FileTransfersApiResponse, make_api_request
from dropbox.client.features.transfer.types import ProductConfig, ProductConfigConstants, TransferSettings, UpsellVariables, UserMetadata
from dropbox.client_api.dropbox_connection import DROPBOX_TIMESTAMP_FORMAT
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
MYPY = False
if MYPY:
    from dropbox.client_api.dropbox_connection import DropboxConnection

def create_transfer(account = None, connection = None, transfer_tracking_id = None):
    pass
# WARNING: Decompyle incomplete


def _get_upsell_variables(upsell_variables_res = None):
    pass
# WARNING: Decompyle incomplete


def get_product_config(account = None, connection = None):
    pass
# WARNING: Decompyle incomplete


def get_user_metadata(account = None, connection = None):
    pass
# WARNING: Decompyle incomplete


def persist_user_default_settings(account = None, connection = None, settings = None):
    pass
# WARNING: Decompyle incomplete


def send_email_to_recipients(account, connection = None, transfer_id = None, email_addresses = None, message = ('account', 'Account', 'connection', 'DropboxConnection', 'transfer_id', 'Text', 'email_addresses', 'List[Text]', 'message', 'Optional[Text]', 'return', 'Future[None]')):
    pass
# WARNING: Decompyle incomplete


def share_transfer(account = None, connection = None, transfer_id = None):
    pass
# WARNING: Decompyle incomplete


def update_metadata(account, connection = None, transfer_id = None, now_time = None, settings = ('account', 'Account', 'connection', 'DropboxConnection', 'transfer_id', 'Text', 'now_time', 'datetime', 'settings', 'TransferSettings', 'return', 'Future[None]')):
    pass
# WARNING: Decompyle incomplete


def share_transfer_with_settings_blocking(account, connection = None, transfer_id = None, now_time = None, settings = ('account', 'Account', 'connection', 'DropboxConnection', 'transfer_id', 'Text', 'now_time', 'datetime', 'settings', 'TransferSettings', 'return', 'Text')):
    update_metadata(account, connection, transfer_id, now_time, settings).block()
    share_future = share_transfer(account, connection, transfer_id)
    share_future.block()
    return share_future.result()

