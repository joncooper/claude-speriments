# Source Generated with Decompyle++
# File: avatar_cache.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
import hashlib
import os
import time
from os.path import getmtime as _getmtime, join as _join
from typing import Callable, Optional, Text
from winffi.gdiplus.api import create_avatar_from_initials, is_valid_image
from dropbox.client.background_worker import on_background_thread
from dropbox.client.constants import AppDataPaths
from dropbox.client.ui.common.colors import color_value_for_avatar
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.exceptions import ClientInitiatedDisconnect, DropboxResponseClientError, DropboxResponseServerError, TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception, Severity
from dropbox.functions import make_bytes
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.threadutils import ThreadPool
DEFAULT_AVATAR_SIZE = 64
DEFAULT_AVATAR_FONT = 'Segoe UI Semibold'
DEFAULT_AVATAR_FONT_SIZE = 28

class AvatarCache(object):
    MAX_NUM_IMAGES = 100
    AVATAR_VERSION = '-2'
    AVATAR_CACHE_PATH = _join(AppDataPaths.dropbox_appdata_path, 'avatar_cache')
    
    def __init__(self = None, conn = None):
        self._conn = conn
        self.threadpool = None
        if not os.path.exists(self.AVATAR_CACHE_PATH):
            
            try:
                os.makedirs(self.AVATAR_CACHE_PATH)
                return None
            except WindowsError:
                report_exception(component = DesktopComponent.NATIVE_NOTIFICATIONS)
                return None
                return None


    
    def register_thread_pool(self = None, threadpool = None):
        self.threadpool = threadpool

    
    def unregister_thread_pool(self = None):
        self.threadpool = None

    
    def get_avatar_async(self, account_id = None, initials = None, callback = None, dropbox_feature_attribution = (True,), fallback = ('account_id', 'Text', 'initials', 'Text', 'callback', 'Callable[[Optional[Text]], None]', 'dropbox_feature_attribution', 'str', 'fallback', 'bool', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _download_avatar_async(self, account_id, initials = None, image_path = None, dropbox_feature_attribution = None, callback = (None, True), fallback = ('account_id', 'Text', 'initials', 'Text', 'image_path', 'Text', 'dropbox_feature_attribution', 'str', 'callback', 'Optional[Callable[[Optional[Text]], None]]', 'fallback', 'bool', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _download_avatar_fn(self, account_id = None, success_callback = None, fail_callback = None, dropbox_feature_attribution = ('account_id', 'Text', 'success_callback', 'Callable[[bytes], None]', 'fail_callback', 'Callable[[], None]', 'dropbox_feature_attribution', 'str', 'return', 'None')):
        
        try:
            image_contents = self._conn.get_account_photo(account_id, dropbox_feature_attribution = dropbox_feature_attribution, expect_account_photo = False)
            if is_valid_image(image_contents):
                success_callback(image_contents)
                return None
            fail_callback()
            return None
        except (DropboxResponseClientError, DropboxResponseServerError, ClientInitiatedDisconnect, TransientNetworkError):
            fail_callback()
            return None
            except Exception:
                report_exception(severity = Severity.WARN, component = DesktopComponent.NATIVE_NOTIFICATIONS)
                fail_callback()
                return None


    
    def _create_avatar_initials(self = None, account_id = None, initials = None, image_path = ('account_id', 'Text', 'initials', 'Text', 'image_path', 'Text', 'return', 'None')):
        avatar_path = _join(self.AVATAR_CACHE_PATH, image_path)
        rgb_color = color_value_for_avatar(account_id)
        create_avatar_from_initials(avatar_path, initials, DEFAULT_AVATAR_FONT, DEFAULT_AVATAR_FONT_SIZE, DEFAULT_AVATAR_SIZE, rgb_color)


