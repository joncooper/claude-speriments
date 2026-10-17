# Source Generated with Decompyle++
# File: camera.pyc (Python 3.11)

import functools
import os.path as os
import time
import weakref
from enum import Enum
from typing import Any, Callable, List, Optional, Text, Tuple
from build_number import is_full_msix
from dropbox.event_names import event_names
from dropbox.callbacks import Handler
from dropbox.camera import CameraSessionLogger, Device, IMPORT_LOW_DISK_SPACE, IMPORT_LOW_DROPBOX_SPACE, IMPORT_SUCCESS, IMPORT_UNKNOWN_ERROR, PhotoDetails, PhotoImportCanceled, PhotoImportDeviceLocked, PhotoImportDisconnected, PhotoImportLowDropboxSpace, PhotoImportNoConnectionError, PhotoImportSelectiveSync
from dropbox.camera.filetypes import IMAGE_EXTENSIONS, PHOTO_EXTENSIONS, VIDEO_EXTENSIONS
from dropbox.client.authentication.account import Account
from dropbox.client.camera_upload.camera_upload_metric_logger import CameraEvent, MetricsLogger
from dropbox.client.camera_upload.types import CameraSplashResponse
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.multiaccount.selector import MultiAccountSelector
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.tray.events import TrayEventName, TrayEventTrigger
from dropbox.client.ui.common.camera_strings import CameraStrings
from dropbox.client.ui.common.constants import SECONDS_PER_DAY, SECONDS_PER_HOUR
from dropbox.client.ui.common.dialogs import DialogController, IconType
from dropbox.client.ui.common.dropbox_menu import MenuItem
from dropbox.client.ui.common.tray_menu_controller import track_click, TrayMenuController, TrayOptionStrings
from dropbox.client.ui.common.uikit import on_ui_thread, on_ui_thread_blocking, on_ui_thread_returns_none
from dropbox.client.ui.common.utils import is_low_ui_mode
from dropbox.client.ui.electron.camera import PTPWarningSplashScreen, QuotaSplashScreen
from dropbox.client.util import highlight_files
from dropbox.components.desktop_components import DesktopComponent
from dropbox.dbexceptions import LowDiskSpaceError
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.foundation.throttling import timed_throttle
from dropbox.i18n import format_bytes, format_number, trans, ungettext
from dropbox.observable import Observable
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import RRLowerServerPath
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
MYPY = False
if MYPY:
    from dropbox.client.camera_upload.session_context import SessionContext
    from dropbox.client.main import DropboxApplication
PHOTO_EXTENSIONS = PHOTO_EXTENSIONS.union(IMAGE_EXTENSIONS)

class PhotoState(Enum):
    SHOW_NOTHING = 0
    SHOW_LAST_IMPORT = 1
    SHOW_UPLOADS_FOLDER = 2
    SHOW_PROGRESS = 3


def imported_message(transferred = None, device_name = None):
    num = len(transferred)
    (has_photos, has_videos) = has_photos_and_videos(transferred)
    if device_name:
        if has_photos and has_videos:
            msg = ungettext('Imported %(num)s new photo from %(device_name)s.', 'Imported all %(num)s new photos and videos from %(device_name)s.', num)
        elif has_videos:
            msg = ungettext('Imported %(num)s new video from %(device_name)s.', 'Imported all %(num)s new videos from %(device_name)s.', num)
        else:
            msg = ungettext('Imported %(num)s new photo from %(device_name)s.', 'Imported all %(num)s new photos from %(device_name)s.', num)
    elif has_photos and has_videos:
        msg = ungettext('Imported %(num)s new photo.', 'Imported all %(num)s new photos and videos.', num)
    elif has_videos:
        msg = ungettext('Imported %(num)s new video.', 'Imported all %(num)s new videos.', num)
    else:
        msg = ungettext('Imported %(num)s new photo.', 'Imported all %(num)s new photos.', num)
    return msg % {
        'device_name': device_name,
        'num': format_number(num, frac_precision = 0) }


def nothing_new_message(skipped = None, device_name = None):
    num = len(skipped)
    (has_photos, has_videos) = has_photos_and_videos(skipped)
    if device_name:
        if not num:
            msg = trans("Dropbox couldn't find any photos or videos on %(device_name)s.")
        elif has_photos and has_videos:
            msg = ungettext('The photo from %(device_name)s has already been imported.', 'All %(num)s photos and videos from %(device_name)s have already been imported.', num)
        elif has_videos:
            msg = ungettext('The video from %(device_name)s has already been imported.', 'All %(num)s videos from %(device_name)s have already been imported.', num)
        else:
            msg = ungettext('The photo from %(device_name)s has already been imported.', 'All %(num)s photos from %(device_name)s have already been imported.', num)
    elif not num:
        msg = trans("Dropbox couldn't find any photos or videos on this device.")
    elif has_photos and has_videos:
        msg = ungettext('The photo from this device has already been imported.', 'All %(num)s photos and videos from this device have already been imported.', num)
    elif has_videos:
        msg = ungettext('The video from this device has already been imported.', 'All %(num)s videos from this device have already been imported.', num)
    else:
        msg = ungettext('The photo from this device has already been imported.', 'All %(num)s photos from this device have already been imported.', num)
    return msg % {
        'device_name': device_name,
        'num': format_number(num, frac_precision = 0) }


def partial_import_message(transferred = None, failed = None):
    num = len(transferred)
    total = len(transferred) + len(failed)
    (photos, videos) = has_photos_and_videos(transferred + failed)
    if photos and videos:
        msg = ungettext('Imported %(num)s of %(total)s photo.', 'Imported %(num)s of %(total)s photos and videos.', total)
    elif videos:
        msg = ungettext('Imported %(num)s of %(total)s video.', 'Imported %(num)s of %(total)s videos.', total)
    else:
        msg = ungettext('Imported %(num)s of %(total)s photo.', 'Imported %(num)s of %(total)s photos.', total)
    return msg % dict(num = format_number(num, frac_precision = 0), total = format_number(total, frac_precision = 0))


def remaining_message(remaining = None):
    pass
# WARNING: Decompyle incomplete


def stunning_buffalo_message(device_count = None):
    return ungettext('We recently had some trouble importing videos from iOS devices. Please reconnect your device so that we can re-import the affected files.', 'We recently had some trouble importing videos from iOS devices. Please reconnect your %s devices so that we can re-import the affected files.', device_count)


class Dummy(object):
    pass


def has_photos_and_videos(paths = None):
    imported_exts = (lambda .0: pass# WARNING: Decompyle incomplete
)(paths())
    has_photos = bool(imported_exts.intersection(PHOTO_EXTENSIONS))
    has_videos = bool(imported_exts.intersection(VIDEO_EXTENSIONS))
    return (has_photos, has_videos)


def rect_to_centered_square(width = None, height = None):
    side = min(width, height)
    return ((width - side) / 2, (height - side) / 2, (width + side) / 2, (height + side) / 2)


def quota_splash_screen_show(dialog_controller, upgrade_cb, cancel_cb, cancel_text = None, never_cb = None, never_text = None, quota_message = ('dialog_controller', 'DialogController', 'upgrade_cb', 'Callable[[], None]', 'cancel_cb', 'Callable[[], None]', 'cancel_text', 'Text', 'never_cb', 'Optional[Callable[[], None]]', 'never_text', 'Optional[str]', 'quota_message', 'Text', 'return', 'None')):
    if not IS_LINUX:
        QuotaSplashScreen(dialog_controller, upgrade_cb, cancel_cb, cancel_text, never_cb, never_text, quota_message)
        return None


def show_ptp_warning_splash_screen(dialog_controller = None, device = None, cancel_cb = None):
    if IS_MAC:
        splash = _PTPWarningSplashScreen(dialog_controller, device, cancel_cb)
        return splash.close_window
    cancel_cb()


class _PTPWarningSplashScreen:
    
    def __init__(self = None, dialog_controller = None, device = None, close_cb = ('dialog_controller', 'DialogController', 'device', 'Device', 'close_cb', 'Callable[[], None]')):
