# Source Generated with Decompyle++
# File: model.pyc (Python 3.11)

import hashlib
import json
import os
import re
from typing import Any, Callable, Dict, List, Optional, Text, Tuple, Union
from mypy_extensions import TypedDict
from six.moves.urllib import parse as urlparse
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.actions_factory_interface import UserNotificationActionContext, UserNotificationActionFactoryInterface
from dropbox.client.notifications.constants import BLUENOTE_NOTIFICATION_ID, BNNotificationType, CURRENT_NOTIFICATIONS_VERSION, GENERIC_TEMPLATE
from dropbox.client.notifications.exceptions import IncompletePayloadException, UnsupportedPayloadException
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotificationButton, LoudNotificationType
from dropbox.client.notifications.preference_settings import DEFAULT_PREFERENCE_BUCKET
from dropbox.client.notifications.typed_data import extract_typed_data
from dropbox.client.notifications.types import NotificationAction, NotificationActor, NotificationAvatarIcon, NotificationIcon, NotificationImageType, NotificationInfo, NotificationRawType, NotificationRemoteIcon, NotificationSourceObject, NotificationSystemIcon, NotificationTask, NotificationThumbnail, NotificationTok, NotificationType, UserNotificationSeenState, UserNotificationStatus
from dropbox.exception.reporting import report_bad_assumption
from dropbox.functions import make_bytes
from dropbox.repr_utils import easy_repr
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
BLUENOTE_TYPE_MAP = {
    BNNotificationType.REQUEST_UNLOCK: NotificationType.REQUEST_UNLOCK,
    BNNotificationType.COMMENTS2_COMMENT: NotificationType.COMMENT,
    BNNotificationType.PAPER_COMMENT: NotificationType.COMMENT,
    BNNotificationType.PAPER_MENTION: NotificationType.MENTION,
    BNNotificationType.PAPER_SHARE: NotificationType.SHARE,
    BNNotificationType.CLIENT_TYPE_DROPBOX_FOLDER_SHARE: NotificationType.SHARE,
    BNNotificationType.CLIENT_TYPE_DROPBOX_FILE_SHARE: NotificationType.SHARE,
    BNNotificationType.DROPBOX_FILE_COMMENT: NotificationType.COMMENT,
    BNNotificationType.NONE: NotificationType.OTHER }

def as_notification_image_type(name = None):
    if not name:
        return None
    
    try:
        return NotificationImageType[name.upper()]
    except KeyError:
        return None



def LoudNotificationParams():
    '''LoudNotificationParams'''
    bluenote_id: 'Optional[int]' = 'LoudNotificationParams'

LoudNotificationParams = <NODE:27>(LoudNotificationParams, 'LoudNotificationParams', TypedDict, total = False)

class UserNotificationInterface(object):
    
    def __init__(self, account, nid, type_id, target_object_key, payload = None, status = None, seen_state = None, feed_time = (None,), trigger_id = ('account', 'AccountInterface', 'nid', 'int', 'type_id', 'int', 'target_object_key', 'NotificationTok', 'payload', 'Dict[Text, Any]', 'status', 'UserNotificationStatus', 'seen_state', 'UserNotificationSeenState', 'feed_time', 'float', 'trigger_id', 'Optional[Text]', 'return', 'None')):
        self._nid = nid
        self._type_id = type_id
        self._target_object_key = target_object_key
        self._payload = payload
        self._status = status
        self._seen_state = seen_state
        self._trigger_id = trigger_id
        self.role = None
        self.account = account
        self.timestamp = feed_time
        _hash = hashlib.md5()
        _hash.update(make_bytes(f'''{type_id!s}_{target_object_key!s}_{account.role!s}'''))
        self.key = _hash.hexdigest()

    
    def __lt__(self = None, other = None):
        return self.timestamp < other.timestamp

    nid = (lambda self = None: self._nid)()
    type_id = (lambda self = None: self._type_id)()
    target_object_key = (lambda self = None: self._target_object_key)()
    payload = (lambda self = None: self._payload)()
    status = (lambda self = None: self._status)()
    
    def set_status(self = None, status = None):
        self._status = status

    seen_state = (lambda self = None: self._seen_state)()
    campaign_id = (lambda self = None: pass)()
    campaign_version = (lambda self = None: pass)()
    trigger_id = (lambda self = None: self._trigger_id)()
    has_structured_data = (lambda self = None: False)()
    non_pii_logging = (lambda self = None: { })()
    preference_bucket = (lambda self = None: DEFAULT_PREFERENCE_BUCKET)()
    
    def has_actions(self = None):
        return False

    
    def is_loud(self = None):
        return True

    
    def is_visible(self = None):
        return True

    
    def is_assistant_viewable(self = None):
        if not self.has_structured_data:
            
            try:
                message = self.get_message()
            except NotImplementedError:
                message = None

            if not message:
                return False
            return None

    
    def get_message(self = None):
        raise NotImplementedError()

    
    def get_loud_notification_params(self = None):
        raise NotImplementedError()

    
    def perform_action(self = None, key = None):
        raise NotImplementedError()

    
    def get_timestamp(self = None):
        return self.timestamp

    is_sticky = (lambda self = None: raise NotImplementedError())()
    
    def short_name(self = None):
        return f'''Notification[{self.__class__.__name__},{self._type_id}]'''



class UserNotification(UserNotificationInterface):
    pass
# WARNING: Decompyle incomplete


def is_bluenote(notif = None):
    return notif.type_id == BLUENOTE_NOTIFICATION_ID

