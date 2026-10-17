# Source Generated with Decompyle++
# File: stub_image_capture_core.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import datetime
import os
import re
import shutil
from typing import Any, Callable, Dict, List, Optional, Text, Union
from dropbox.client.background_worker import on_background_thread_returns_none
from dropbox.client.photodownloader.mac.db_image_capture_core import DBICCameraDevice, DBICCameraDeviceDelegate, DBICCameraFile, DBICCameraFolder, DBICDeviceBrowser, DBICDeviceBrowserDelegate, DBNSError, DidDownloadCallbackType, DidReadCallbackType
from dropbox.client_api.hashing import DROPBOX_MAX_BLOCK_SIZE
from dropbox.db_thread import db_thread
from dropbox.directoryevent import DirectoryEvent
from dropbox.fileevents import FileEvents
from dropbox.functions import make_str
from dropbox.mac.version import CATALINA, MAC_VERSION
from dropbox.trace import TRACE
EXCLUDED_FILES = [
    re.compile('/\\.dropbox($|/)'),
    re.compile('/\\.dropbox\\.cache($|/)'),
    re.compile('/Icon\\r$'),
    re.compile('/desktop\\.ini$'),
    re.compile('/\\.~[0-9]+HI$'),
    re.compile('/~[0-9]+HI\\.tmp$'),
    re.compile('/\\.dropbox\\.attr($|/)'),
    re.compile('/\\.DS_Store$'),
    re.compile('/~\\$.*\\.(docx|xlsx|pptx)$'),
    re.compile('/\\.mount_id$')]

def is_excluded(curpath = None):
    for exc_re in EXCLUDED_FILES:
        if exc_re.search(make_str(curpath)):
            return True
        return False


class StubNSError(DBNSError):
    
    def localized_description(self = None):
        return 'ImageCaptureCore experienced brittleness'

    
    def domain(self = None):
        return 'com.apple.ImageCaptureCore'

    
    def code(self):
        return 195948557



class StubICCameraFolder(DBICCameraFolder):
    
    def __init__(self = None, path = None):
        self._path = path

    
    def name(self = None):
        split = os.path.split(self._path)
        return split[len(os.path.split(self._path)) - 1]

    
    def parent_folder(self = None):
        parent_path = os.path.dirname(self._path)
        if len(parent_path) <= 1:
            return None
        return StubICCameraFolder(parent_path)



class StubICCameraFile(DBICCameraFile):
    
    def __init__(self = None, name = None, file_path = None):
        self._name = name
        self._file_path = file_path
        self.stat_result = os.stat(self._file_path)
        self._bytes = b''
        date = self.creation_date()
        TRACE('StubICCameraFile %s (%s)', name, date.strftime('%Y-%m-%d %H.%M.%S') if date else 'unknown date')

    
    def creation_date(self = None):
        return datetime.datetime.fromtimestamp(self.stat_result.st_birthtime)

    
    def modification_date(self = None):
        return datetime.datetime.fromtimestamp(self.stat_result.st_mtime)

    
    def name(self = None):
        return self._name

    
    def file_size(self = None):
        return self.stat_result.st_size

    
    def uti(self = None):
        return 'public.image'

    
    def parent_folder(self = None):
        return StubICCameraFolder(make_str(self._file_path))

    
    def get_bytes(self = None, offset = None, length = None):
        if not self._bytes:
            f = open(self._file_path, 'rb')
            buf = f.read(DROPBOX_MAX_BLOCK_SIZE)
            if buf:
                pass
            
        
        None(None, None)

    
    def copy_to_path(self = None, local_path = None):
        shutil.copyfile(self._file_path, local_path)



class StubICCameraDevice(DBICCameraDevice):
    
    def __init__(self = None, observable_path = None, mount_id = None, on_disconnect = ('observable_path', 'Text', 'mount_id', 'Text', 'on_disconnect', 'Callable[[], None]', 'return', 'None')):
        self.observable_path = observable_path
        self.mount_id = mount_id
        self.open_session = False
        self._on_disconnect = on_disconnect

    
    def set_delegate(self = None, db_ic_device_delegate = None):
        self.db_ic_device_delegate = db_ic_device_delegate

    
    def uuid_string(self):
        if self.name().startswith('no_uid'):
            TRACE('StubICCameraDevice with no_uid')
            return None
        return None.name() + '-66383736-6630-6363-6463-663733653263'

    
    def usb_product_id(self = None):
        return 4776

    
    def is_locked(self = None):
        return False

    
    def type(self = None):
        return 257

    
    def is_device_local(self = None):
        return True

    
    def product_type(self = None):
        pass

    
    def capabilities(self = None):
        return [
            'ICCameraDeviceCanAcceptPTPCommands',
            'ICCameraDeviceSupportsApplePTP']

    
    def name(self = None):
        return os.path.basename(self.observable_path)

    
    def persistent_id_string(self = None):
        return self.name() + '-66383736-6630-6363-6463-663733653263'

    
    def serial_number_string(self = None):
        return self.name() + '-f876f0ccdcf73e2cc9f17f085a046a20c41f905d'

    
    def has_open_session(self = None):
        return self.open_session

    
    def request_open_session(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def content_catalog_percent_completed(self = None):
        return 100

    
    def media_files(self = None):
        TRACE('StubICCameraDevice %r fetching media files', self.mount_id)
        media_files = []
        for filename in os.listdir(self.observable_path):
            file_path = os.path.join(self.observable_path, filename)
            if not is_excluded(str(file_path)):
                db_file = StubICCameraFile(filename, file_path)
                media_files.append(db_file)
            return media_files

    
    def request_download_file(self, camera_file = None, download_dir = None, did_download_callback = None, context_info = ('camera_file', 'DBICCameraFile', 'download_dir', 'Text', 'did_download_callback', 'DidDownloadCallbackType', 'context_info', 'Any', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def request_read_data_from_file(self, camera_file, offset = None, length = None, did_read_callback = None, context_info = ('camera_file', 'DBICCameraFile', 'offset', 'int', 'length', 'int', 'did_read_callback', 'DidReadCallbackType', 'context_info', 'Any', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete



def get_filename_for_path(path = None):
    return os.path.basename(path)


class StubICDeviceBrowser(DBICDeviceBrowser):
    
    def __init__(self = None, observable_path = None):
        TRACE('StubICDeviceBrowser initialized for path %r', observable_path)
        self.file_events = db_thread(FileEvents)()
        self._watch_id = None
        self._observable_path = observable_path
        self.camera_devices = { }

    
    def _get_mount_id(self = None, path = None):
        
        try:
            id_file = open(os.path.join(path, '.mount_id'))
            
            try:
                None(None, None)
                return 
                with None:
                    if not None, id_file.read():
                        
                        try:
                            
                            try:
                                return None
                            except FileNotFoundError:
                                return None





    
    def _mount_device(self = None, file_path = None, timeout = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _unmount_device(self = None, file_path = None):
        filename = get_filename_for_path(file_path)
        if filename not in self.camera_devices:
            TRACE('Already unmounted stub device, skipping.')
            return None
        device = None.camera_devices[filename]
    # WARNING: Decompyle incomplete

    
    def _handle_fs_event(self = None, local_path_iter = None):
        if isinstance(local_path_iter, List):
            events = local_path_iter
        else:
            events = [
                local_path_iter]
        for event in events:
            TRACE('stub_image_capture_core: file event: %r', event)
            path = Text(event.path)
            if is_excluded(path):
                continue
            if os.path.isdir(path):
                self._mount_device(path)
                continue
            self._unmount_device(path)
            return None

    
    def set_delegate(self = None, db_ic_browser_delegate = None):
        self.delegate = db_ic_browser_delegate

    
    def devices(self = None):
        return list(self.camera_devices.values())

    
    def start(self = None):
        (self._watch_id, _) = self.file_events.add_watch_async(os.path.realpath(self._observable_path), self._handle_fs_event, watch_root = True, recurse = FileEvents.RECURSE_ONE)
        self.file_events.start()
        TRACE('stub_image_capture_core: Started listening at %s  ', self._observable_path)
        if os.path.isdir(self._observable_path):
            TRACE('observable path exists, handling existing contents')
            for path in os.listdir(self._observable_path):
                TRACE('handling %r', path)
                self._handle_fs_event(DirectoryEvent(os.path.join(self._observable_path, path)))
                return None
                return None

    
    def stop(self = None):
        pass
    # WARNING: Decompyle incomplete


