# Source Generated with Decompyle++
# File: rosetta_warning.pyc (Python 3.11)

from typing import Optional
from apex.util import process_architecture, system_architecture
from build_number import BUILDID
from build_number.constants import ENGINE_ONLY_BUILDID
from build_number.platform import IS_MAC
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes, IconType
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.i18n import trans
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
_APPLE_SILICON_HELP_URL = 'https://help.dropbox.com/installs/apple-silicon-support'
_LEARN_MORE_BUTTON_ID = 1

def maybe_show_rosetta_warning(ui_kit = None):
    if not IS_MAC:
        return None
    if None == ENGINE_ONLY_BUILDID:
        return None
    proc_arch = process_architecture()
    sys_arch = system_architecture()
    if not proc_arch == 'x86_64' or sys_arch == 'arm64':
        return None
    TRACE('ROSETTA WARNING: Intel build detected running on Apple Silicon.process_arch=%s, system_arch=%s', proc_arch, sys_arch)
    caption = trans('Dropbox Performance Warning')
    message = trans('You are running the Intel version of Dropbox on an Apple Silicon Mac using Rosetta 2. This will cause reduced performance.<br><br>For the best experience, please download the version of Dropbox built for Apple Silicon.')
    
    def _on_dialog_dismissed(button_id = None, _checkbox_checked = None):
        TRACE('ROSETTA WARNING: Alert dismissed by user: button_id=%r', button_id)
        if button_id == _LEARN_MORE_BUTTON_ID:
            dropbox_url_info.launch_full_url(_APPLE_SILICON_HELP_URL)
            return None

    ui_kit.show_native_non_blocking_dialog(caption = caption, message = message, buttons = [
        trans('OK')], left_buttons = [
        trans('Learn More')], icon = IconType.WARN, callback = _on_dialog_dismissed, dialog_source_type = DialogSourceTypes.OTHER)

