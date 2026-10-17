# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from os import path
from typing import List, Optional, Text, Union
from AppKit import NSBundle, NSURL, NSWorkspace, NSWorkspaceLaunchDefault
from build_number import is_frozen
from CoreFoundation import CFURLCopyFileSystemPath, kCFURLPOSIXPathStyle
from CoreServices.LaunchServices import kLSRolesEditor, kLSRolesShell, kLSRolesViewer, LSCopyApplicationURLsForURL
from dropbox.client.util import app_display_name_for_file, app_for_file, get_repo_root_unfrozen
from dropbox.foundation.file_location_helpers import get_resources_dir
from dropbox.foundation.native_file_opener.bridge_gen.app_info import AppInfo
from dropbox.foundation.native_file_opener.bridge_gen.app_info_list import AppInfoList
from dropbox.foundation.native_file_opener.bridge_gen.icon_info import IconInfo
from dropbox.foundation.reporting import report_app_framework_event_restricted
from dropbox.mac.internal import autoreleasepool
from dropbox.shared.local_path import LocalPath
from dropbox.trace import TRACE

def get_associated_applications(local_path = None):
