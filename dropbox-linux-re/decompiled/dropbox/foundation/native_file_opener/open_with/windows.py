# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from os import path
from typing import List, Optional, Text, Union
from winffi.kernel32.api import CreateProcess
from winshell.api import assoc_enum_handlers, invoke_by_ui_name
from dropbox.client.util.win import app_display_name_for_file, executable_for_file, get_executable, get_shortened_long_path
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.native_file_opener.bridge_gen.app_info import AppInfo
from dropbox.foundation.native_file_opener.bridge_gen.app_info_list import AppInfoList
from dropbox.foundation.native_file_opener.bridge_gen.icon_info import IconInfo
from dropbox.shared.local_path import LocalPath
from dropbox.win32._icon_constants import IDI_DROPBOX, IDI_DROPBOX_M2_WEBSITE_MENU_OPEN_PAPER

def executable_or_friendly_name_for_file(full_path = None):
    executable_name = executable_for_file(full_path)
# WARNING: Decompyle incomplete


def get_associated_applications(local_path = None):
    (_, ext) = path.splitext(Text(local_path))
    
    try:
        handlers = assoc_enum_handlers(ext)
    except WindowsError:
        report_exception(severity = Severity.TRACE, component = DesktopComponent.NATIVE_FILE_OPENER)
        return 

    None = handlers()
    default_exe = executable_or_friendly_name_for_file(Text(local_path))
    if default_exe:
        for app in apps:
            if default_exe == app.app_id:
                default_app = app
                (lambda .0: [ AppInfo(handler.name, handler.path, icon_path = handler.icon_path, icon_index = handler.icon_index, app_id = handler.exe_name) for handler in .0 ])
            
            return AppInfoList(apps = apps, default = default_app)


def open_with_application(file_path = None, app = None):
    santized_path = get_shortened_long_path(Text(file_path))
    if app.path.lower().endswith('.exe') or app.path.lower().endswith('\\launchwinapp.exe'):
        (_, ext) = path.splitext(santized_path)
        return invoke_by_ui_name(ext, app.path, app.name, [
            santized_path])
    if None in santized_path:
        report_bad_assumption('Windows file names should not contain double quotes')
        return False
    cmd_line = None + app.path + '" "' + santized_path + '"'
    return CreateProcess(app.path, cmd_line)


def open_multiple_files_with_application(file_paths = None, app = None):
    pass
# WARNING: Decompyle incomplete


def get_dropbox_icon():
    return IconInfo(icon_path = get_executable(), icon_index = -IDI_DROPBOX)


def get_dropbox_paper_icon():
    return IconInfo(icon_path = get_executable(), icon_index = -IDI_DROPBOX_M2_WEBSITE_MENU_OPEN_PAPER)

