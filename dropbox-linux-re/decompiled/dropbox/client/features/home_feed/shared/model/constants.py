# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from enum import IntEnum
from dropbox.enum_utils import auto, AutoNameEnum

class AntennaEventType(IntEnum):
    UNKNOWN_ACTION = 0
    ADD = 1
    EDIT = 2
    RENAME = 3
    DELETE = 4
    RESTORE = 5
    SHARE = 8
    MOUNT = 11
    UNMOUNT = 12
    INVISIBLE = 13
    DELETED_CLOBBERED_BY_MOUNT = 14
    EXISTING_CLOBBERED_BY_MOUNT = 15
    MOVE = 16
    UNSHARE = 17
    VIEW = 6
    SHARED_LINK_VIEW = 18
    SHARED_LINK_CREATE = 24
    COMMENT = 7
    COMMENT_MENTION = 25
    COMMENT_NEW = 53
    COMMENT_REPLY = 54
    COMMENT_RESOLVE_THREAD = 55
    COMMENT_UNRESOLVE_THREAD = 56
    COMMENT_ENABLE_COMMENTING = 57
    COMMENT_DISABLE_COMMENTING = 58
    STAR = 49
    UNSTAR = 50
    PAPER_ADD = 19
    PAPER_EDIT = 20
    PAPER_VIEW = 23
    PAPER_OPEN = 39
    PAPER_COMMENT = 21
    PAPER_SHARE_PAD = 22
    PAPER_SHARE_FOLDER = 29
    PAPER_NEW_MENTION = 28
    PAPER_NEW_TASK = 30
    PAPER_COMPLETE_TASK = 31
    PAPER_INCOMPLETE_TASK = 32
    PAPER_PAD_DELETED = 33
    PAPER_CREATE_FOLDER = 37
    PAPER_MOVE = 38
    PAPER_STAR_PAD = 43
    PAPER_UNSTAR_PAD = 44
    PAPER_STAR_FOLDER = 45
    PAPER_UNSTAR_FOLDER = 46
    PAPER_FOLLOW_EDIT = 47
    PAPER_FOLLOW_VIEW = 48
    SHARED_CONTENT_INVITE_SEND = 26
    SHARED_CONTENT_INVITE_RECEIVE = 27
    SHARED_CONTENT_INVITE_CHANGE_ACCESS = 34
    SHARED_CONTENT_INVITE_REMOVE = 35
    SHARED_CONTENT_LINK_SETTINGS_CHANGE = 36
    FILE_SETTINGS_CHANGE = 42
    SEARCH_REQUEST = 40
    SEARCH_CLICK = 41
    EXTERNAL_SLACK_LINK_SHARE = 51
    EXTERNAL_ZOOM_SCREEN_SHARE = 52
    EXTERNAL_TRELLO_ADD_ATTACHMENT = 71
    EXTERNAL_TRELLO_MOVE_CARD = 72
    EXTERNAL_TRELLO_ARCHIVE_CARD = 73
    EXTERNAL_TRELLO_UNARCHIVE_CARD = 74

ASSISTANT_LOGGING_SURFACE = 'assistant'

class AssistantDataConsumer(AutoNameEnum):
    TRAY = auto()
    BROWSE = auto()


class AssistantFeature(AutoNameEnum):
    ACTIVITY = auto()
    RECENTS = auto()
    STARRED = auto()
    SUGGEST_FILES = auto()
    SUGGEST_FOLDER_STARS = auto()

ASSISTANT_FEATURES = [
    AssistantFeature.ACTIVITY,
    AssistantFeature.RECENTS,
    AssistantFeature.STARRED,
    AssistantFeature.SUGGEST_FILES]
BROWSE_FEATURES = [
    AssistantFeature.SUGGEST_FOLDER_STARS,
    AssistantFeature.STARRED]
_feature_trace_names = {
    AssistantFeature.SUGGEST_FOLDER_STARS: 'Suggest Folder Stars',
    AssistantFeature.SUGGEST_FILES: 'Suggest',
    AssistantFeature.STARRED: 'Starred',
    AssistantFeature.RECENTS: 'Recents',
    AssistantFeature.ACTIVITY: 'Activity' }

def trace_name_for_feature(feature = None):
    return _feature_trace_names[feature]

