# Source Generated with Decompyle++
# File: file_icon_windows.pyc (Python 3.11)

from __future__ import absolute_import
import os
import subprocess
from typing import Optional, Text
from apex.metrics import Metric
from build_number import dropbox_version
from pynt.constants import ERROR_FILE_NOT_FOUND, REGDB_E_CLASSNOTREG, WTS_E_FAILEDEXTRACTION
from pynt.dlls.shell32 import shell32
from pynt.headers.windows import FILE_ATTRIBUTE_DIRECTORY, FILE_ATTRIBUTE_NORMAL
from pynt.helpers.general import windows_error
from winffi.gdi32.api import DeleteObject
from winffi.gdiplus.api import get_icon_as_bytes
from winffi.shell32.api import extract_icon_of_size, shell_get_file_info, SHGFI_SYSICONINDEX, SHGFI_USEFILEATTRIBUTES
from winffi.user32.api import DestroyIcon
from winshell.api import get_file_image, get_icon_by_index, get_icon_from_hbitmap, ShellFileImageType, SHIL_EXTRALARGE, SHIL_JUMBO, SHIL_LARGE, SHIL_SMALL
from dropbox.client.folder_tagger.folder_icon_windows import FolderTagIcon
from dropbox.client.util.win import get_contents_root
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context import Context
from dropbox.foundation.native_icon.interface import ImageFormat, NativeIconLoaderInterface
from dropbox.foundation.native_icon.util import create_metrics_reporter
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.reporting import report_app_framework_event, report_app_framework_event_restricted
from dropbox.foundation.scheme_handler.interface import CUSTOM_SCHEME_HANDLER_AMP_NAMESPACE
from dropbox.trace import TRACE
METRIC_THUMBNAIL_GENERATE_THUMBNAIL = 'native_file_icon/native_thumbnail_generate'
TAG_NAME_THUMBNAIL_RESULT = 'result'
TAG_VALUE_RESULT_UNABLE_TO_LOCATE_EXE = 'missing_exe'
TAG_VALUE_RESULT_TIMEOUT = 'timeout'
TAG_VALUE_RESULT_SUCCESSFULL_EXECUTION = 'success'
TAG_VALUE_RESULT_FAILED_EXECUTION = 'failed_execution'
TAG_VALUE_RESULT_FILE_NOT_FOUND = 'file_not_found'
TAG_NAME_DROPBOX_FEATURE_ATTRIBUTION = 'feature_attribution'
CREATE_NO_WINDOW = 134217728
_ICON_LOADER_WIN_PERF_LOGGING_RATE = 0.05 if dropbox_version.is_internal_alpha() else 0.01

def _get_general_file_icon(fake_filename, file_attrs = None, size = None, perf_session = None, image_format = ('fake_filename', 'Text', 'file_attrs', 'int', 'size', 'int', 'perf_session', 'PerfSession', 'image_format', 'ImageFormat', 'return', 'Optional[bytes]')):
    flags = SHGFI_SYSICONINDEX | SHGFI_USEFILEATTRIBUTES
    icon_type = SHIL_JUMBO
    if size <= 16:
        icon_type = SHIL_SMALL
    if size <= 32:
        icon_type = SHIL_LARGE
    elif size <= 48:
        icon_type = SHIL_EXTRALARGE
    
    try:
        info = shell_get_file_info(fake_filename, flags, file_attrs = file_attrs)
        perf_session.checkpoint('Get info finished')
        hicon = get_icon_by_index(info.iIcon, icon_type)
        perf_session.checkpoint('Get icon by index finished')
    except (WindowsError, AttributeError):
        report_exception(severity = Severity.WARN, component = DesktopComponent.LOCAL_VIEWS_NATIVE_ICON)
        return None

    icon_bytes = None
    
    try:
        icon_bytes = get_icon_as_bytes(image_format.value, hicon)
        
        try:
            pass
        except WindowsError:
            report_exception(severity = Severity.WARN, component = DesktopComponent.LOCAL_VIEWS_NATIVE_ICON)
            
            try:
                pass
            try:
                if not DestroyIcon(hicon):
                    report_bad_assumption(f'''DestroyIcon() failed: {windows_error}''')
                elif not DestroyIcon(hicon):
                    report_bad_assumption(f'''DestroyIcon() failed: {windows_error}''')



    return icon_bytes


class NativeIconLoaderWin(NativeIconLoaderInterface):
    _get_file_icon_by_type = (lambda cls = None, extension = None, size = classmethod, image_format = ('extension', 'Text', 'size', 'int', 'image_format', 'ImageFormat', 'return', 'Optional[bytes]'): fake_filename = 'foobar.' + extensionperf_session = PerfSession('NativeIconLoaderWin-get-file-icon-by-type', sampling_rate = _ICON_LOADER_WIN_PERF_LOGGING_RATE)icon_bytes = _get_general_file_icon(fake_filename, FILE_ATTRIBUTE_NORMAL, size, perf_session, image_format)perf_session.end()# WARNING: Decompyle incomplete
)()
    _get_default_folder_icon = (lambda cls = None, size = None, image_format = classmethod: fake_filename = 'folder'perf_session = PerfSession('NativeIconLoaderWin-get-default-folder-icon', sampling_rate = _ICON_LOADER_WIN_PERF_LOGGING_RATE)icon_bytes = _get_general_file_icon(fake_filename, FILE_ATTRIBUTE_DIRECTORY, size, perf_session, image_format)perf_session.end()# WARNING: Decompyle incomplete
)()
    _get_folder_tag_icon = (lambda cls = None, tag = None, size = classmethod, image_format = ('tag', 'Text', 'size', 'int', 'image_format', 'ImageFormat', 'return', 'Optional[bytes]'): try:
(icon_path, icon_index) = FolderTagIcon.icon_tags[tag]except KeyError:
report_exception(severity = Severity.CRITICAL, component = DesktopComponent.LOCAL_VIEWS_NATIVE_ICON)Nonetry:
hicon = extract_icon_of_size(icon_path, icon_index, size)except WindowsError:
report_exception(severity = Severity.CRITICAL, component = DesktopComponent.LOCAL_VIEWS_NATIVE_ICON)Noneicon_bytes = Nonetry:
icon_bytes = get_icon_as_bytes(image_format.value, hicon)try:
passexcept WindowsError:
report_exception(severity = Severity.WARN, component = DesktopComponent.LOCAL_VIEWS_NATIVE_ICON)try:
passtry:
if not DestroyIcon(hicon):
report_bad_assumption(f'''DestroyIcon() failed: {windows_error}''')elif not DestroyIcon(hicon):
report_bad_assumption(f'''DestroyIcon() failed: {windows_error}''')icon_bytes)()
    _get_file_image_by_path = (lambda cls = None, local_path = None, size = classmethod, image_format = (ShellFileImageType.DEFAULT,), option = ('local_path', 'Text', 'size', 'int', 'image_format', 'ImageFormat', 'option', 'ShellFileImageType', 'return', 'Optional[bytes]'): perf_session = PerfSession('NativeIconLoaderWin-get-file-image', option.name, sampling_rate = _ICON_LOADER_WIN_PERF_LOGGING_RATE)try:
hbitmap = get_file_image(local_path, size = size, option = option)perf_session.checkpoint('Get file image as hbitmap finished')except WindowsError:
e = Noneerror = e.winerror & 0xFFFFFFFFif error == WTS_E_FAILEDEXTRACTION:
passelif error == REGDB_E_CLASSNOTREG:
report_exception(severity = Severity.TRACE, component = DesktopComponent.LOCAL_VIEWS_NATIVE_ICON)elif error == ERROR_FILE_NOT_FOUND:
report_exception(severity = Severity.TRACE, component = DesktopComponent.LOCAL_VIEWS_NATIVE_ICON)else:
report_exception(severity = Severity.WARN, component = DesktopComponent.LOCAL_VIEWS_NATIVE_ICON)e = Nonedel eNonee = Nonedel etry:
hicon = get_icon_from_hbitmap(hbitmap)perf_session.checkpoint('Get icon from hbitmap finished')try:
passexcept WindowsError:
report_exception(severity = Severity.WARN, component = DesktopComponent.LOCAL_VIEWS_NATIVE_ICON)try:
if not DeleteObject(hbitmap):
report_bad_assumption(f'''DeleteObject failed: {windows_error}''')NoneNonetry:
if not DeleteObject(hbitmap):
report_bad_assumption(f'''DeleteObject failed: {windows_error}''')elif not DeleteObject(hbitmap):
report_bad_assumption(f'''DeleteObject failed: {windows_error}''')icon_bytes = Nonetry:
icon_bytes = get_icon_as_bytes(image_format.value, hicon)perf_session.checkpoint('Get icon bytes from hicon finished')try:
passexcept WindowsError:
report_exception(severity = Severity.WARN, component = DesktopComponent.LOCAL_VIEWS_NATIVE_ICON)try:
passtry:
if not DestroyIcon(hicon):
report_bad_assumption(f'''DestroyIcon() failed: {windows_error}''')elif not DestroyIcon(hicon):
report_bad_assumption(f'''DestroyIcon() failed: {windows_error}''')perf_session.end()# WARNING: Decompyle incomplete
)()
    
    def __init__(self = None, context = None):
        success = shell32.FileIconInit(False)
        if not success:
            err = windows_error()
            report_exception(severity = Severity.TRACE, exc_type = type(err), exc_val = err, component = DesktopComponent.LOCAL_VIEWS_NATIVE_ICON)
        self._context = context

    
    def get_file_icon_by_path(self = None, local_path = None, size = None, scale_factor = (ImageFormat.PNG,), format = ('local_path', 'Text', 'size', 'int', 'scale_factor', 'float', 'format', 'ImageFormat', 'return', 'Optional[bytes]')):
        size = int(size * scale_factor)
        icon_bytes = self._get_file_image_by_path(local_path, size = size, image_format = format, option = ShellFileImageType.ICON_ONLY)
        return icon_bytes

    
    def get_file_icon_by_type(self = None, extension = None, size = None, scale_factor = (ImageFormat.PNG,), format = ('extension', 'Text', 'size', 'int', 'scale_factor', 'float', 'format', 'ImageFormat', 'return', 'Optional[bytes]')):
        return self._get_file_icon_by_type(extension, size = size, image_format = format)

    
    def get_default_folder_icon(self = None, size = None, scale_factor = None, format = (ImageFormat.PNG,)):
        return self._get_default_folder_icon(size, format)

    
    def get_folder_icon_by_tag(self = None, tag = None, size = None, scale_factor = (ImageFormat.PNG,), format = ('tag', 'Text', 'size', 'int', 'scale_factor', 'float', 'format', 'ImageFormat', 'return', 'Optional[bytes]')):
        size = int(size * scale_factor)
        icon_bytes = self._get_folder_tag_icon(tag, size, format)
        return icon_bytes

    
    def get_file_thumbnail_by_path(self = None, local_path = None, size = None, dropbox_feature_attribution = (ImageFormat.PNG,), format = ('local_path', 'Text', 'size', 'int', 'dropbox_feature_attribution', 'Text', 'format', 'ImageFormat', 'return', 'Optional[bytes]')):
        if 'qebcobkqbgpbzfynfuwbof' in local_path:
            report_app_framework_event('honeypot_thumbnail_request_rejected', feature = dropbox_feature_attribution)
            return None
        app_dir = get_contents_root()
        app_path = os.path.join(app_dir, 'DropboxThumbnailGenerator.exe')
        args = [
            app_path,
            local_path]
        amp_tags = {
            TAG_NAME_DROPBOX_FEATURE_ATTRIBUTION: dropbox_feature_attribution }
        metric = create_metrics_reporter(self._context, amp_tags)
        
        try:
            process = subprocess.Popen(args, stdout = subprocess.PIPE, stderr = subprocess.PIPE, creationflags = CREATE_NO_WINDOW)
        except OSError:
            amp_tags = {
                TAG_NAME_THUMBNAIL_RESULT: TAG_VALUE_RESULT_UNABLE_TO_LOCATE_EXE }
            metric.create_stats(Metric(CUSTOM_SCHEME_HANDLER_AMP_NAMESPACE, METRIC_THUMBNAIL_GENERATE_THUMBNAIL), amp_tags).record(0)
            report_exception(severity = Severity.WARN, component = DesktopComponent.LOCAL_VIEWS_NATIVE_ICON)
            return None

    # WARNING: Decompyle incomplete


