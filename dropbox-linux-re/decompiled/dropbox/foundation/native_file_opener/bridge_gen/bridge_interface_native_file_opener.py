# Source Generated with Decompyle++
# File: bridge_interface_native_file_opener.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Optional
from dropbox.foundation.futures import Future
from dropbox.foundation.native_file_opener.bridge_gen.app_info import AppInfo
from dropbox.foundation.native_file_opener.bridge_gen.app_info_list import AppInfoList
from dropbox.foundation.native_file_opener.bridge_gen.dangerously_bypass_whitelist import DangerouslyBypassWhitelist
from dropbox.foundation.native_file_opener.bridge_gen.file_open_bridge_result import FileOpenBridgeResult
from dropbox.foundation.native_file_opener.bridge_gen.file_open_origin import FileOpenOrigin
from dropbox.foundation.native_file_opener.bridge_gen.file_open_path import FileOpenPath
from dropbox.foundation.native_file_opener.bridge_gen.icon_info import IconInfo
from dropbox.foundation.native_file_opener.bridge_gen.path_open_properties import PathOpenProperties

class NativeFileOpenerBridgeInterface(ABC):
    open_file = (lambda self, path, origin, in_file_browser = None, with_app = None, dangerously_bypass_whitelist = abstractmethod, from_background = ('path', 'FileOpenPath', 'origin', 'FileOpenOrigin', 'in_file_browser', 'bool', 'with_app', 'Optional[AppInfo]', 'dangerously_bypass_whitelist', 'Optional[DangerouslyBypassWhitelist]', 'from_background', 'Optional[bool]', 'return', 'Future[FileOpenBridgeResult]'): pass)()
    get_applications_for_file = (lambda self = None, path = None: pass)()
    get_path_open_properties = (lambda self = None, path = None, with_app = abstractmethod, dangerously_bypass_whitelist = ('path', 'FileOpenPath', 'with_app', 'Optional[AppInfo]', 'dangerously_bypass_whitelist', 'Optional[DangerouslyBypassWhitelist]', 'return', 'Future[PathOpenProperties]'): pass)()
    get_dropbox_icon = (lambda self = None: pass)()
    get_dropbox_paper_icon = (lambda self = None: pass)()

