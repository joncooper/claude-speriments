# Source Generated with Decompyle++
# File: typed_data.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import cast, Dict, Optional, Text, Tuple, Union
from dropbox.client.notifications.constants import BNNotificationType
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption
_COMMENT_TYPES = {
    BNNotificationType.DROPBOX_FILE_COMMENT,
    BNNotificationType.PAPER_COMMENT}
_SHARE_TYPES = {
    BNNotificationType.DROPBOX_SHARED_CONTENT,
    BNNotificationType.PAPER_SHARE}
_MENTION_TYPES = {
    BNNotificationType.PAPER_MENTION}
_COMMENTS2_TYPES = {
    BNNotificationType.COMMENTS2_COMMENT}
_INTERNAL_SHARE_TYPES = {
    BNNotificationType.CLIENT_TYPE_DROPBOX_FILE_SHARE,
    BNNotificationType.CLIENT_TYPE_DROPBOX_FOLDER_SHARE}
_PROCESSABLE_NOTIFICATION_TYPES = _MENTION_TYPES | _COMMENT_TYPES | _SHARE_TYPES | {
    BNNotificationType.PAPER_TASK} | _COMMENTS2_TYPES
BADGEABLE_NOTIFICATION_TYPES = _PROCESSABLE_NOTIFICATION_TYPES | _INTERNAL_SHARE_TYPES

def _extract_quote(notification_type = None, typed_data_payload = None):
    quote_key = None
    
    try:
        if notification_type in _COMMENT_TYPES:
            quote_key = 'comment_text'
        elif notification_type in _SHARE_TYPES:
            quote_key = 'share_text'
        elif notification_type in _MENTION_TYPES:
            quote_key = 'mention_text'
        elif notification_type in _COMMENTS2_TYPES:
            quote_key = 'preview_quote'
        return cast(str, typed_data_payload[quote_key]) if quote_key else None
    except KeyError:
        report_bad_assumption(f'''Notification typed data does not match expected shape. Type: {notification_type!s}, keys: {typed_data_payload.keys()!s}''')
        return None



def extract_typed_data(nid = None, version_id = None, payload_notification_type = None, typed_data_payload = ('nid', 'Optional[int]', 'version_id', 'Optional[str]', 'payload_notification_type', 'Optional[str]', 'typed_data_payload', 'Optional[Dict[Text, Union[str, int]]]', 'return', 'Tuple[Optional[str], Optional[str]]')):
    if payload_notification_type or payload_notification_type not in _PROCESSABLE_NOTIFICATION_TYPES:
        return (None, None)
    if not None:
        report('notification-missing-typed-data', nid = str(nid), type_id = str(payload_notification_type), version = str(version_id))
        return (None, None)
    notification_quote = _extract_quote(payload_notification_type, typed_data_payload)
    notification_type_id = payload_notification_type
    if payload_notification_type == BNNotificationType.DROPBOX_SHARED_CONTENT:
        if typed_data_payload.get('file_obj_id'):
            notification_type_id = BNNotificationType.CLIENT_TYPE_DROPBOX_FILE_SHARE
        else:
            notification_type_id = BNNotificationType.CLIENT_TYPE_DROPBOX_FOLDER_SHARE
    return (notification_type_id, notification_quote)

