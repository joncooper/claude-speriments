# Source Generated with Decompyle++
# File: _mac.pyc (Python 3.11)

from __future__ import absolute_import
import os
import re
import time
from typing import Iterable, Optional, Text, Tuple, Union
from Foundation import NSUserDefaults
from _base import ScreenshotsProviderBase
from constants import MAC_SCREENCAPTURE_XATTR, MOVED_SCREENRECORDING_XATTR_KEY, MOVED_SCREENSHOT_XATTR_KEY
from dropbox import fsutil
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.screenshots import Screenshot
from dropbox.client.transient_simple_metric.transient_simple_metric import report_transient_simple_metric, SimpleMetricCategoryWhitelist
from dropbox.client.ui.common.screenshots import ScreenshotsStrings
from dropbox.components.desktop_components import DesktopComponent
from dropbox.directoryevent import DirectoryEvent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.fileevents import FileEvents
from dropbox.functions import file_extension
from dropbox.mac.internal import autoreleasepool, get_desktop_directory
from dropbox.mac.version import CATALINA, MAC_VERSION
from dropbox.preferences import OPT_SCREENSHOTS
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary import file_system_exceptions
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from controller import ScreenshotsController
    from dropbox.client.main import DropboxApplication

class ScreenshotsProvider(ScreenshotsProviderBase):
    pass
# WARNING: Decompyle incomplete

