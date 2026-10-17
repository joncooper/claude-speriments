# Source Generated with Decompyle++
# File: notifications_retrieval.pyc (Python 3.11)

import abc
from itertools import chain
from typing import Any, Callable, Dict, Iterator, List, Optional, Set, Text
from six import add_metaclass, iteritems
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.bolt.signalling import BoltClient, BoltLongPoller, BoltLongPollHandlerBase
from dropbox.client.bolt.types import BoltAppID, BoltChannelId, BoltChannelState, BoltRevisionInfo, BoltToken, BoltUniqueID
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.constants import CURRENT_NOTIFICATIONS_VERSION, RESYNC_KEY, TIMELINE_CACHE_SIZE
from dropbox.client.notifications.threading import on_user_notification_thread
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.exceptions import HTTP429Error, HTTP500Error, TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.connection_backoff import ConnectionBackoff
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.trace import TRACE
NOTIFICATION_NOTIFY_SERVICE_NAME = 'user_notification'
NOTIFICATION_BOLT_APP_ID = BoltAppID(NOTIFICATION_NOTIFY_SERVICE_NAME)
NotificationRetrievalResultHandlerBase = <NODE:12>()

class NotificationRetrievalState(object):
    MAX_INITIAL_CONNECT_DELAY = 3600
    MAX_SERVER_ERROR_DELAY = 86400
    
    def __init__(self = None, local_config = None, result_handlers = None, last_resync_ts = ('local_config', 'LocalConfigurationInterface', 'result_handlers', 'List[NotificationRetrievalResultHandlerBase]', 'last_resync_ts', 'int', 'return', 'None')):
        self.local_config = local_config
        self.result_handlers = result_handlers
        self.last_resync_ts = last_resync_ts
        self.nid = 0
        self.bolt_token = None
        self.latest_nid = None
        self._established_initial_connection = False
        self.backoff = None

    established_initial_connection = (lambda self = None: self._established_initial_connection)()
    established_initial_connection = (lambda self = None, value = None: pass# WARNING: Decompyle incomplete
)()


class NotificationRetriever(BoltLongPollHandlerBase):
    
    def __init__(self, gandalf, bolt_client = None, conn = None, add_quit_handler_callback = None, check_for_reboot_callback = ('gandalf', 'Gandalf', 'bolt_client', 'BoltClient', 'conn', 'DropboxConnection', 'add_quit_handler_callback', 'Callable[[Callable[..., Any], int], None]', 'check_for_reboot_callback', 'Callable[[AccountInterface, Dict[Text, Any]], None]', 'return', 'None')):
        self._gandalf = gandalf
        self._conn = conn
        self._check_for_reboot_callback = check_for_reboot_callback
        self._pending = { }
        self._account_states = { }
        self._channel_id_to_account = { }
        self._long_poller = db_thread(BoltLongPoller)(self, bolt_client, NOTIFICATION_BOLT_APP_ID, 'NOTIFICATION_RETRIEVAL')
        self._long_poller.start()
        add_quit_handler_callback(self._on_quit, 0)

    add_account = (lambda self = None, account = None, local_config = on_user_notification_thread, result_handlers = (False,), is_retry = ('account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'result_handlers', 'List[NotificationRetrievalResultHandlerBase]', 'is_retry', 'bool', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()
    
    def _handle_add_account_long_poll(self = None, account = None):
        channels = self._retrieve_notifications(account)
        for channel in channels:
            self._channel_id_to_account[channel.channel_id] = account
            self._long_poller.add_subscription(channels)
            return None

    remove_account = (lambda self = None, account = None: TRACE('Stopped retrieving notifications for user %d', account.uid)self._account_states.pop(account, None)self._handle_remove_account_long_poll(account))()
    
    def _handle_remove_account_long_poll(self = None, account_to_remove = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _on_quit(self = None, exit_code = None):
        TRACE('Disabling notification retrieval')
        self._long_poller.signal_stop()

    
    def initialize(self = None):
        return []

    on_bolt_update = (lambda self = None, channels_to_update = None, invalid_channels = on_user_notification_thread(debounce = True): new_channels_to_subscribe_to = []updated_channel_ids = channels_to_update()accounts_to_check = set()for channel_id in chain(updated_channel_ids, invalid_channels):
account = self._channel_id_to_account.get(channel_id, None)if account:
accounts_to_check.add(account)for account in accounts_to_check:
new_channels_to_subscribe_to.extend(self._retrieve_notifications(account))self._long_poller.add_subscription(new_channels_to_subscribe_to)None)()
    
    def _retrieve_notifications(self = None, account = None, resyncing = None):
        account_state = self._account_states[account]
        result = self._conn.list_user_notifications(account, start_nid = account_state.nid + 1 if account_state.nid else None, limit = TIMELINE_CACHE_SIZE, template_version = str(CURRENT_NOTIFICATIONS_VERSION))
        self._check_for_reboot_callback(account, result)
        resync_ts = result.get('resync_ts')
    # WARNING: Decompyle incomplete

    
    def _reset_state(self = None, account_state = None):
        account_state.nid = 0
        account_state.latest_nid = None
        account_state.bolt_token = None

    
    def _update_resync_ts(self = None, account_state = None, resync_ts = None):
        account_state.last_resync_ts = resync_ts
        account_state.local_config.config_dict[RESYNC_KEY] = resync_ts


