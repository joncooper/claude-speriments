# Source Generated with Decompyle++
# File: photodownloader_image_capture_core.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import datetime
from contextlib import contextmanager
from threading import Event, Timer
from typing import Any, Callable, Iterator, List, MutableSequence, Optional, Set, Text
from pymac.constants import kUTTypeImage, kUTTypeMovie
from dropbox.camera import Device, File, PhotoImportCanceled, PhotoImportNotReady, PhotoImportPhotoFailedToImport
from dropbox.client.camera_upload.camera_uploads import CameraHandler
from dropbox.client.camera_upload.types import CUDeviceUID
from dropbox.client.photodownloader.mac.db_image_capture_core import DBICCameraDevice, DBICCameraDeviceDelegate, DBICCameraFile, DBICDeviceBrowser, DBICDeviceBrowserDelegate, DBNSError
from dropbox.client.photodownloader.mac.db_image_capture_core_factory import DBICDeviceLocationTypeMaskLocal, DBICDeviceTypeMaskCamera, DBImageCaptureCoreFactory
from dropbox.client.photodownloader.mac.photodownloader_mac import is_hidden, PhotoDownloaderMac, UnsupportedDevice
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.fileutils import safe_remove
from dropbox.mac.version import CATALINA, MAC_VERSION, MOJAVE, VENTURA
from dropbox.shared.local_path import LocalPath
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.camera_upload.configuration_manager import CameraConfigurationManager

class PhotoDownloader(PhotoDownloaderMac):
    pass
# WARNING: Decompyle incomplete


class EFPhotoUploader(object):
    __init__ = (lambda self = None: self.db_ic_browser_delegate = DBICDeviceBrowserDelegate(self.device_browser_enumerated_local_devices, self.device_browser_did_add_device_more_coming, self.device_browser_did_remove_device_more_going)self.db_ic_device_delegate = DBICCameraDeviceDelegate(self.device_did_become_ready_with_complete_content_catalog, self.device_did_become_ready, self.device_did_encounter_error, self.device_did_open_session_with_error, self.device_did_close_session_with_error, self.did_remove_device)self.browser = DBImageCaptureCoreFactory.build_device_browser()self.browser.set_delegate(self.db_ic_browser_delegate)self.handler = Noneself.screen_busy = Falseself.cameras_fetched = False)()
    
    def device_browser_did_add_device_more_coming(self = None, browser = None, device = None, more_coming = ('browser', 'DBICDeviceBrowser', 'device', 'DBICCameraDevice', 'more_coming', 'bool', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def device_browser_did_remove_device_more_going(self = None, browser = None, device = None, more_going = ('browser', 'DBICDeviceBrowser', 'device', 'DBICCameraDevice', 'more_going', 'bool', 'return', 'None')):
        device.set_delegate(None)
    # WARNING: Decompyle incomplete

    
    def device_browser_enumerated_local_devices(self = None, browser = None):
        TRACE('DBICC: Devices fetched')
        self.cameras_fetched = True

    
    def did_remove_device(self = None, device = None):
        TRACE('ICC: Device removed')
    # WARNING: Decompyle incomplete

    
    def device_did_open_session_with_error(self = None, device = None, error = None):
        TRACE('ICC: Session opened')
    # WARNING: Decompyle incomplete

    
    def device_did_become_ready(self = None, device = None):
        TRACE('ICC: Device ready (connecting...)')
    # WARNING: Decompyle incomplete

    
    def device_did_close_session_with_error(self = None, device = None, error = None):
        TRACE('ICC: Session closed')
    # WARNING: Decompyle incomplete

    
    def device_did_encounter_error(self = None, device = None, error = None):
        TRACE('ICC: Device encountered error')
    # WARNING: Decompyle incomplete

    
    def device_did_become_ready_with_complete_content_catalog(self = None, camera = None):
        TRACE('ICC: Device reports ready with complete content catalog')
        self.handle_camera_ready(camera)

    
    def handle_camera_ready(self = None, camera = None, prev_media_count = None, lapse_time = (0, 0)):
        if not self.handler:
            report_bad_assumption('EFPhotoUploader has no CameraHandler', component = DesktopComponent.SYNC_EVERYTHING)
            return None
        if not None.has_open_session():
            TRACE('PhotoDownloader stopping camera poll because the session was closed.')
            return None
        timeout = None.handler.get_file_list_timeout()
        interval = 0.5
        media_count = len(camera.media_files())
        if media_count or media_count == prev_media_count or lapse_time >= timeout:
            TRACE('ICC: Device connected with %r files after %r seconds', media_count, lapse_time)
            self.handler.report_camera_ready_time_lapsed(ImageCaptureDevice(camera, self.handler.should_allow_iphone(), None), media_count, lapse_time, self.is_screen_busy())
            if not self.is_screen_busy():
                self.handler.connected(ImageCaptureConnectedDevice(camera, self.handler.should_allow_iphone(), None))
            return None
        timer = Timer(interval, self.handle_camera_ready, [
            camera,
            media_count,
            lapse_time + interval])
        timer.start()

    
    def handle_error(self = None, device = None, error = None):
        if not self.handler:
            report_bad_assumption('EFPhotoUploader has no CameraHandler', component = DesktopComponent.SYNC_EVERYTHING)
            return None
        TRACE('ICC: Error %r %r: %r', error.domain(), error.code(), error.localized_description())
    # WARNING: Decompyle incomplete

    
    def set_controller(self = None, controller = None):
        self.handler = controller

    
    def set_screen_busy(self = None, screen_busy = None):
        self.screen_busy = screen_busy

    
    def is_screen_busy(self = None):
        if self.screen_busy:
            TRACE('ICC: Skipping ImageCapture event because the screen is not available.')
        return self.screen_busy

    
    def start(self = None):
        self.browser.start()

    
    def stop(self = None):
        self.browser.stop()

    
    def get_connected_devices(self = None):
        return self.browser.devices()

    
    def ready(self):
        if not self.cameras_fetched:
            return False
        for device in None.browser.devices():
            if device.content_catalog_percent_completed() < 100:
                return False
            return True

    
    def is_enabled(self = None):
        if self.handler:
            return self.handler.is_enabled()



class ImageCaptureDevice(Device):
    pass
# WARNING: Decompyle incomplete


class ImageCaptureConnectedDevice(ImageCaptureDevice):
    pass
# WARNING: Decompyle incomplete

MAX_BUFFER = 134217728

class ImageCaptureConnectedDeviceFile(File):
    __slots__ = ('_image_capture_device', '_camera_item', 'cur_pos', '_failed', '_file', '_data', '_cache', '_done')
    
    def __init__(self = None, image_capture_device = None, camera_item = None):
        self._image_capture_device = image_capture_device
        self._camera_item = camera_item
        self.cur_pos = 0
        self._failed = False
        self._data = b''
        self._file = None
        self._cache = None
        self._done = Event()

    id = (lambda self = None: self._camera_item.name())()
    
    def time(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def name(self = None):
        return self._camera_item.name()

    
    def size(self = None):
        return self._camera_item.file_size()

    open = (lambda self = None, fs = None, cache = contextmanager: pass# WARNING: Decompyle incomplete
)()
    
    def _handle_data(self, data = None, camera_item = None, error = None, _context = ('data', 'bytes', 'camera_item', 'DBICCameraFile', 'error', 'Optional[DBNSError]', '_context', 'Any', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _handle_download(self, camera_item = None, path = None, error = None, _context = ('camera_item', 'DBICCameraFile', 'path', 'Optional[Text]', 'error', 'Optional[DBNSError]', '_context', 'Any', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def read(self = None, size = None):
        self._done.wait(600)
        if self._done.is_set() or self._failed:
            TRACE('Async read file is_done: %r, is_failed: %r', self._done.is_set(), self._failed)
            raise PhotoImportPhotoFailedToImport(self.name())
        left = self.size() - self.cur_pos
        if size < 0 or size > left:
            size = left
        if size <= 0:
            return b''
        offset = None.cur_pos
        if self._data:
            return self._data[offset:offset + size]
        if None._file:
            open(self._file, 'rb') = None
            f.seek(offset)
            buf = f.read(size)
            if len(buf) == size:
                None(None, None)
                return 
            TRACE('Download expected %r got %r', size, buf)
            None(None, None)
        else:
            with None:
                if not None:
                    pass
        raise PhotoImportPhotoFailedToImport(self.name())



class ImageCaptureConnectingDevice(ImageCaptureDevice):
    PROPS = Device.PROPS + ('percent',)
    percent = (lambda self = None: try:
self.device.content_catalog_percent_completed()except Exception:
100)()

