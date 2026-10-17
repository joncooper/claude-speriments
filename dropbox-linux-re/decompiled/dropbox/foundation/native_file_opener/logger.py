# Source Generated with Decompyle++
# File: logger.pyc (Python 3.11)

import os
from typing import Any, Dict, Optional, Text, Union
from build_number.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.client.analytics import log_pap_event
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import PAPLoggingEvent
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import sanitize_event_extra_dict
from dropbox.foundation.native_file_opener.bridge_gen.file_open_origin import FileOpenOrigin
from dropbox.functions import file_extension
from dropbox.model.types import FileId
from dropbox.pap.events.enums.desktop_open_origin_pb2 import DesktopOpenOrigin
from dropbox.pap.events.filesystem_item_actions.open_file_pb2 import Open_File
from dropbox.pap_event_logging.utils import get_enum_value_for_string
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import ServerPath
OS_SHELL_EXTENSION_COMPONENT = DesktopComponent.UNKNOWN
if IS_WINDOWS:
    OS_SHELL_EXTENSION_COMPONENT = DesktopComponent.SHELL_INTEGRATION_FILE_EXPLORER
elif IS_MAC:
    OS_SHELL_EXTENSION_COMPONENT = DesktopComponent.SHELL_INTEGRATION_FINDER_SYNC
elif IS_LINUX:
    OS_SHELL_EXTENSION_COMPONENT = DesktopComponent.SHELL_INTEGRATION_NAUTILUS
FILE_OPEN_ORIGIN_TO_PAP = {
    FileOpenOrigin.DESKTOP_SHELL: 'DESKTOP_SHELL',
    FileOpenOrigin.DESKTOP_NOTIFICATION: 'DESKTOP_NOTIFICATION',
    FileOpenOrigin.DESKTOP_NATIVE: 'DESKTOP_NATIVE',
    FileOpenOrigin.UNITY: 'UNITY',
    FileOpenOrigin.TRAY_RECENTS: 'TRAY_RECENTS',
    FileOpenOrigin.TRAY_CREATION: 'TRAY_CREATION',
    FileOpenOrigin.TRAY: 'TRAY',
    FileOpenOrigin.DEBUG: 'UNKNOWN' }
FILE_OPEN_ORIGIN_TO_COMPONENT = {
    FileOpenOrigin.DESKTOP_SHELL: OS_SHELL_EXTENSION_COMPONENT,
    FileOpenOrigin.TRAY_RECENTS: DesktopComponent.TRAY,
    FileOpenOrigin.TRAY_CREATION: DesktopComponent.TRAY,
    FileOpenOrigin.TRAY: DesktopComponent.TRAY,
    FileOpenOrigin.DESKTOP_NOTIFICATION: DesktopComponent.NATIVE_NOTIFICATIONS,
    FileOpenOrigin.DESKTOP_NATIVE: OS_SHELL_EXTENSION_COMPONENT,
    FileOpenOrigin.UNITY: DesktopComponent.UNITY_FEATURES,
    FileOpenOrigin.DEBUG: DesktopComponent.UNKNOWN,
    FileOpenOrigin.UNKNOWN: DesktopComponent.UNKNOWN }

def log_to_pap_for_open_events(input_path = None, origin = None):
