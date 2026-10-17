# Source Generated with Decompyle++
# File: preference_settings.pyc (Python 3.11)

from typing import List, NamedTuple, Optional, Sequence, Text, Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.multiaccount.role import Roles
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.event import report
from dropbox.preferences import NOTIFICATIONS_PREFERENCE_URL, OPT_NOTIFS_BLUENOTE_ASSIGNED_TASKS, OPT_NOTIFS_BLUENOTE_FOLLOWED_COMMENTS, OPT_NOTIFS_BLUENOTE_LEGACY, OPT_NOTIFS_BLUENOTE_MENTIONS, OPT_NOTIFS_BLUENOTE_SHARED_CONTENT, OPT_NOTIFS_BLUENOTE_VIEWS, OPT_NOTIFS_SYNC_ADD, OPT_NOTIFS_SYNC_EDIT_DELETE, OPT_NOTIFS_SYNC_LEGACY
from dropbox.url_info import DropboxURLInfo
BLUENOTE_PREFERENCE_BUCKETS = {
    'comment': OPT_NOTIFS_BLUENOTE_FOLLOWED_COMMENTS,
    'mention': OPT_NOTIFS_BLUENOTE_MENTIONS,
    'shared_content': OPT_NOTIFS_BLUENOTE_SHARED_CONTENT,
    'task': OPT_NOTIFS_BLUENOTE_ASSIGNED_TASKS,
    'view_read_receipt': OPT_NOTIFS_BLUENOTE_VIEWS }
DEFAULT_PREFERENCE_BUCKET = 'always_show'
MigrationInfo = NamedTuple('MigrationInfo', [
    ('old', Sequence[Text]),
    ('new', Sequence[Text])])
_PREFERENCE_MIGRATIONS = [
    MigrationInfo(old = (OPT_NOTIFS_BLUENOTE_LEGACY,), new = (OPT_NOTIFS_BLUENOTE_MENTIONS, OPT_NOTIFS_BLUENOTE_FOLLOWED_COMMENTS, OPT_NOTIFS_BLUENOTE_SHARED_CONTENT, OPT_NOTIFS_BLUENOTE_VIEWS)),
    MigrationInfo(old = (OPT_NOTIFS_SYNC_LEGACY,), new = (OPT_NOTIFS_SYNC_ADD,))]

class NotificationPrefStrings(UIStrings):
    mentions = UI('@mentions')
    comments = UI('Comments on files')
    tasks = UI('Tasks assigned to me')
    shared_content = UI('Files and folders shared with me')
    file_edits = UI('Edits to files')
    file_new = UI('New files synced')
    views = UI('Shared files and folders opened by others')


class NotificationPreferencesStringMapping(object):
    mapping = (lambda : [
(OPT_NOTIFS_BLUENOTE_MENTIONS, NotificationPrefStrings.mentions),
(OPT_NOTIFS_BLUENOTE_FOLLOWED_COMMENTS, NotificationPrefStrings.comments),
(OPT_NOTIFS_BLUENOTE_ASSIGNED_TASKS, NotificationPrefStrings.tasks),
(OPT_NOTIFS_BLUENOTE_SHARED_CONTENT, NotificationPrefStrings.shared_content),
(OPT_NOTIFS_BLUENOTE_VIEWS, NotificationPrefStrings.views),
(OPT_NOTIFS_SYNC_ADD, NotificationPrefStrings.file_new),
(OPT_NOTIFS_SYNC_EDIT_DELETE, NotificationPrefStrings.file_edits)])()


def report_notification_preference(pref = None, is_checked = None, account = None):
    pass
# WARNING: Decompyle incomplete


def get_notifications_settings_url(dropbox_url_info = None, account = None):
    role_info = []
# WARNING: Decompyle incomplete

