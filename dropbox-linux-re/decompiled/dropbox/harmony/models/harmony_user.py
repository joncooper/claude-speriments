# Source Generated with Decompyle++
# File: harmony_user.pyc (Python 3.11)

from __future__ import absolute_import, annotations
import time
from typing import Callable, Optional, Text
from six import itervalues
from dropbox.client.presence.model import PresenceInfo
from dropbox.client.ui.common.harmony_strings import HarmonyStrings
from dropbox.client.users import UserInfo
from dropbox.i18n import ago, format_time_interval
from dropbox.repr_utils import easy_repr

class HarmonyUser:
    
    def __init__(self = None, viewer = None, server_time_getter = None):
        pass
    # WARNING: Decompyle incomplete

    
    def copy(self = None):
        new_copy = object.__new__(self.__class__)
        new_copy._viewers = self._viewers.copy()
        new_copy._server_time = self._server_time
        new_copy._last_editor = self._last_editor
        new_copy._last_viewer = self._last_viewer
        new_copy._user_info = self._user_info
        return new_copy

    
    def _process_viewers(self = None):
        last_editor = None
        last_viewer = None
    # WARNING: Decompyle incomplete

    
    def set_viewer(self = None, viewer = None):
        pass
    # WARNING: Decompyle incomplete

    
    def remove_viewer(self = None, host_key = None):
        if self._viewers.pop(host_key, None):
            self._process_viewers()
        return len(self._viewers)

    
    def update_with_info(self = None, user_info = None):
        pass
    # WARNING: Decompyle incomplete

    is_editing = (lambda self = None: self._last_editor is not None)()
    last_edited = (lambda self = None: self._last_editor.last_edited if self._last_editor else None)()
    last_opened = (lambda self = None: self._last_viewer.last_opened if self._last_viewer else None)()
    status_text = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    dbid = (lambda self = None: self._user_info.dbid)()
    image_url = (lambda self = None: self._user_info.image_url)()
    first_name = (lambda self = None: self._user_info.first_name)()
    last_name = (lambda self = None: self._user_info.last_name)()
    short_name = (lambda self = None: self._user_info.short_name)()
    initials = (lambda self = None: self._user_info.initials)()
    display_name = (lambda self = None: self._user_info.display_name)()
    user_info = (lambda self = None: self._user_info)()
    
    def __repr__(self = None):
        return easy_repr(self, 'dbid', 'is_editing')



def get_viewer_status_text(user = None, server_time = None):
    if not server_time:
        pass
    now = time.time()
    if user.is_editing:
        interval = now - user.last_edited
        if interval < 60 or user.last_edited == 0:
            return HarmonyStrings.viewer_status_editing_now
        return None.viewer_status_editing % dict(ago = ago(user.last_edited, now))
    interval = None - user.last_opened
    if interval < 60 or user.last_opened == 0:
        return HarmonyStrings.viewer_status_viewing_now
    return None.viewer_status_viewing % dict(time = format_time_interval(interval))

