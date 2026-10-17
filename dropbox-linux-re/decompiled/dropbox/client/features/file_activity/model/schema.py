# Source Generated with Decompyle++
# File: schema.pyc (Python 3.11)

import datetime
from typing import Any, Dict, Iterable, Optional
from dropbox.client.features.file_activity.model.bridge_gen.fetch_file_activities_response import FetchFileActivitiesResponse
from dropbox.client.features.file_activity.model.bridge_gen.file_activity_data import FileActivityData
from dropbox.client.features.file_activity.model.bridge_gen.file_activity_event_type import FileActivityEventType
from dropbox.client.features.file_activity.model.bridge_gen.file_activity_group import FileActivityGroup
from dropbox.client.features.file_activity.model.bridge_gen.slack_conversation_type import SlackConversationType
from dropbox.client.features.file_activity.model.bridge_gen.trello_event_type import TrelloEventType
from dropbox.client.features.file_activity.model.bridge_gen.zoom_screen_share_type import ZoomScreenShareType
from dropbox.client_api.dropbox_connection import DROPBOX_TIMESTAMP_FORMAT
from dropbox.client_api.exceptions import TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future
from dropbox.foundation.transitional import make_delayed_network_call
from dropbox.foundation.types.ids import FileID
from dropbox.i18n import ago
from dropbox.overrides import report_exception
JSON = Dict[(str, Any)]

def fetch_file_activity_batch(context = None, file_ids = None):
    pass
# WARNING: Decompyle incomplete


def parse_file_activity_response(account_id = None, response = None):
    pass
# WARNING: Decompyle incomplete

_TAG_TO_EVENT_TYPE = {
    'add': FileActivityEventType.ADD,
    'edit': FileActivityEventType.EDIT,
    'move': FileActivityEventType.MOVE,
    'rename': FileActivityEventType.RENAME,
    'shared_content_invite': FileActivityEventType.SHARED_CONTENT_INVITE,
    'slack_link_share': FileActivityEventType.SLACK_LINK_SHARE,
    'view': FileActivityEventType.VIEW,
    'zoom_screen_share': FileActivityEventType.ZOOM_SCREEN_SHARE,
    'file_lock_change': FileActivityEventType.LOCK_CHANGED,
    'trello_file_activity': FileActivityEventType.TRELLO_FILE_ACTIVITY }
_SLACK_CONVERSATION_TYPE_MAP = {
    'redacted_viewer_not_slack_connected': SlackConversationType.REDACTED_VIEWER_NOT_SLACK_CONNECTED,
    'redacted_viewer_not_in_conversation': SlackConversationType.REDACTED_VIEWER_NOT_IN_CONVERSATION,
    'channel': SlackConversationType.CHANNEL,
    'dm_multiperson': SlackConversationType.DM_MULTIPERSON,
    'dm_to_someone_other_than_viewer': SlackConversationType.DM_TO_SOMEONE_OTHER_THAN_VIEWER,
    'dm_to_viewer': SlackConversationType.DM_TO_VIEWER }
_ZOOM_SCREEN_SHARE_TYPE_MAP = {
    'redacted_viewer_not_zoom_connected': ZoomScreenShareType.REDACTED_VIEWER_NOT_ZOOM_CONNECTED,
    'redacted_viewer_not_in_meeting': ZoomScreenShareType.REDACTED_VIEWER_NOT_IN_MEETING,
    'in_anonymous_meeting': ZoomScreenShareType.IN_ANONYMOUS_MEETING,
    'in_meeting_with_name': ZoomScreenShareType.IN_MEETING_WITH_NAME }
_TRELLO_EVENT_TYPE_MAP = {
    'attach_file_to_card': TrelloEventType.ATTACH_FILE_TO_CARD,
    'move_card_between_lists': TrelloEventType.MOVE_CARD_BETWEEN_LISTS,
    'move_card_between_boards': TrelloEventType.MOVE_CARD_BETWEEN_BOARDS,
    'archive_card': TrelloEventType.ARCHIVE_CARD,
    'unarchive_card': TrelloEventType.UNARCHIVE_CARD }

def _parse_group(account_id = None, utc_now = None, group = None):
    pass
# WARNING: Decompyle incomplete


def _parse_activity(account_id = None, utc_now = None, activity = None):
    pass
# WARNING: Decompyle incomplete


def _parse_slack_conversation_type(conv_type = None):
    if conv_type:
        return _SLACK_CONVERSATION_TYPE_MAP.get(conv_type['.tag'])


def _parse_zoom_screen_share_type(share_type = None):
    if share_type:
        return _ZOOM_SCREEN_SHARE_TYPE_MAP.get(share_type['.tag'])


def _parse_trello_event_type(event_type = None):
    if event_type:
        return _TRELLO_EVENT_TYPE_MAP.get(event_type['.tag'])


def _ago_text(timestamp = None, utc_now = None):
    date = datetime.datetime.strptime(timestamp, DROPBOX_TIMESTAMP_FORMAT)
    return ago(date.timestamp(), utc_now)


def _initials(display_name = None):
    inits = display_name.split(' ')()
    two_initials = inits[0] if len(inits) > 0 else '' + inits[-1] if len(inits) > 1 else ''
    return two_initials.upper()

