# Source Generated with Decompyle++
# File: objc_image_capture_core.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import datetime
from typing import Any, Callable, Dict, List, Optional, Text, TypeVar
import objc
from AppKit import NSObject
from Foundation import NSArray, NSData, NSDictionary, NSError, NSString, NSURL
from ImageCaptureCore import ICCameraDevice, ICCameraFile, ICCameraFolder, ICCameraItem, ICDevice, ICDeviceBrowser, ICDeviceLocationDescriptionUSB, ICDeviceLocationTypeMaskLocal, ICDeviceTypeMaskCamera, ICDownloadsDirectoryURL, ICOverwrite, ICSavedFilename
from dropbox.client.photodownloader.mac.db_image_capture_core import DBICCameraDevice, DBICCameraDeviceDelegate, DBICCameraFile, DBICCameraFolder, DBICDeviceBrowser, DBICDeviceBrowserDelegate, DBNSError, DidDownloadCallbackType, DidReadCallbackType
from dropbox.client.ui.common.uikit import on_ui_thread_returns_none
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception, Severity
from dropbox.gui import event_handler as event_handler_unsafe
from dropbox.mac.internal import autoreleasepool
from dropbox.trace import TRACE
_C = TypeVar('_C', bound = Callable[(..., Any)])

def event_handler(func = None):
    return event_handler_unsafe(func, do_trace_locals = False)


def event_handler_unknown_thread(func = None):
    return event_handler_unsafe(func, thread_name = None, do_trace_locals = False)

_CNone = TypeVar('_CNone', bound = Callable[(..., None)])

def event_requester(func = None):
    return on_ui_thread_returns_none()(event_handler_unsafe(func, do_trace_locals = False))


class ObjCNSError(DBNSError):
    
    def __init__(self = None, error = None):
        self.error = error

    
    def __eq__(self = None, other = None):
        if not isinstance(other, ObjCNSError):
            return False
        return None.error is other.error

    
    def __ne__(self = None, other = None):
        return not self.__eq__(other)

    
    def __hash__(self = None):
        return hash(self.error)

    localized_description = (lambda self = None: if isinstance(self.error, NSError):
self.error.localizedDescription())()
    domain = (lambda self = None: if isinstance(self.error, NSError):
self.error.domain())()
    code = (lambda self = None: if isinstance(self.error, NSError):
self.error.code())()


class ObjCICCameraFolder(DBICCameraFolder):
    
    def __init__(self = None, camera_folder = None):
        self.camera_folder = camera_folder

    
    def __eq__(self = None, other = None):
        if not isinstance(other, ObjCICCameraFolder):
            return False
        return None.camera_folder is other.camera_folder

    
    def __ne__(self = None, other = None):
        return not self.__eq__(other)

    
    def __hash__(self = None):
        return hash(self.camera_folder)

    
    def name(self = None):
        return self.camera_folder.name()

    
    def parent_folder(self = None):
        autoreleasepool()
        parent_folder = self.camera_folder.parentFolder()
    # WARNING: Decompyle incomplete



class ObjCICCameraFile(DBICCameraFile):
    
    def __init__(self = None, ic_camera = None):
        self.ic_file = ic_camera

    
    def __eq__(self = None, other = None):
        if not isinstance(other, ObjCICCameraFile):
            return False
        return None.ic_file is other.ic_file

    
    def __ne__(self = None, other = None):
        return not self.__eq__(other)

    
    def __hash__(self = None):
        return hash(self.ic_file)

    
    def creation_date(self = None):
        autoreleasepool()
    # WARNING: Decompyle incomplete

    
    def modification_date(self = None):
        autoreleasepool()
    # WARNING: Decompyle incomplete

    
    def name(self = None):
        autoreleasepool()
        None(None, None)
        return 
        with None:
            if not None, self.ic_file.name():
                pass

    
    def file_size(self = None):
        autoreleasepool()
        None(None, None)
        return 
        with None:
            if not None, int(self.ic_file.fileSize()):
                pass

    
    def uti(self = None):
        autoreleasepool()
        None(None, None)
        return 
        with None:
            if not None, self.ic_file.UTI():
                pass

    
    def parent_folder(self = None):
        autoreleasepool()
        None(None, None)
        return 
        with None:
            if not None, ObjCICCameraFolder(self.ic_file.parentFolder()):
                pass



class ObjCICCameraDevice(DBICCameraDevice):
    
    def __init__(self = None, ic_device = None):
        pass
    # WARNING: Decompyle incomplete

    
    def set_delegate(self = None, db_ic_device_delegate = None):
        self.delegate.setDelegateCallbacks_(db_ic_device_delegate)

    
    def __eq__(self = None, other = None):
        if not isinstance(other, ObjCICCameraDevice):
            return False
        return None.ic_device is other.ic_device

    
    def __ne__(self = None, other = None):
        return not self.__eq__(other)

    
    def __hash__(self = None):
        return hash(self.ic_device)

    
    def _device_has_function(self = None, name = None):
        return callable(getattr(self.ic_device, name, None))

    
    def type(self = None):
        return self.ic_device.type()

    
    def is_device_local(self = None):
        return self.ic_device.locationDescription() == ICDeviceLocationDescriptionUSB

    
    def name(self = None):
        
        try:
            return self.ic_device.name()
        except Exception:
            return None


    
    def usb_product_id(self = None):
        return self.ic_device.usbProductID()

    
    def serial_number_string(self = None):
        
        try:
            return self.ic_device.serialNumberString()
        except Exception:
            return None


    
    def has_open_session(self = None):
        return self.ic_device.hasOpenSession()

    
    def uuid_string(self = None):
        return self.ic_device.UUIDString()

    
    def persistent_id_string(self = None):
        
        try:
            return self.ic_device.persistentIDString()
        except Exception:
            return None


    
    def request_open_session(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def content_catalog_percent_completed(self = None):
        return self.ic_device.contentCatalogPercentCompleted()

    
    def media_files(self = None):
        autoreleasepool()
        wrapped_media_files = []
        if not self.ic_device.mediaFiles():
            apple_media_files = []
            for apple_file in apple_media_files:
                wrapped_file = ObjCICCameraFile(apple_file)
                wrapped_media_files.append(wrapped_file)
                None(None, None)
                return 
                with None:
                    if not None, wrapped_media_files:
                        pass

    
    def is_locked(self = None):
        
        try:
            if self._device_has_function('isAccessRestrictedAppleDevice'):
                return self.ic_device.isAccessRestrictedAppleDevice()
            report_bad_assumption('ICCameraDevice::is_locked -- isAccessRestrictedAppleDevice has been deprecated. Update this function to permanently call new version.')
            if self._device_has_function('locked'):
                return self.ic_device.locked()
        except Exception:
            TRACE('ICCameraDevice::is_locked -- cannot determine locked state. Defaulting to false.')
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.SYNC_EVERYTHING)

        return False

    request_download_file = (lambda self, camera_file = None, download_dir = None, did_download_callback = event_requester, context_info = ('camera_file', 'DBICCameraFile', 'download_dir', 'Text', 'did_download_callback', 'DidDownloadCallbackType', 'context_info', 'Optional[Any]', 'return', 'None'): TRACE('ICCameraDevice::requestDownloadFile:options:downloadDelegate:didDownloadSelector:contextInfo:')# WARNING: Decompyle incomplete
)()
    request_read_data_from_file = (lambda self, camera_item, offset = None, length = None, did_read_callback = event_requester, context_info = ('camera_item', 'DBICCameraFile', 'offset', 'int', 'length', 'int', 'did_read_callback', 'DidReadCallbackType', 'context_info', 'Any', 'return', 'None'): TRACE('ICCameraDevice::requestReadDataFromFile:atOffset:length:readDelegate:didReadDataSelector:contextInfo:')TRACE('%r (%r b) offset %r length %r', camera_item.name(), camera_item.file_size(), offset, length)# WARNING: Decompyle incomplete
)()
    
    def product_type(self = None):
        
        try:
            return self.ic_device.productType()
        except Exception:
            return None


    
    def capabilities(self = None):
        
        try:
            return self.ic_device.capabilities()
        except Exception:
            ex = None
            TRACE('Failed to read capabilities %r', ex)
            del ex
            return None
            None = 
            del ex




class ObjCICCameraDeviceDelegate(NSObject):
    
    def __new__(cls = None, apple_device = None):
        return ObjCICCameraDeviceDelegate.alloc().init_(apple_device)

    
    def init_(self = None, apple_device = None):
        self = objc.super(ObjCICCameraDeviceDelegate, self).init()
    # WARNING: Decompyle incomplete

    
    def setDelegateCallbacks_(self = None, db_ic_device_delegate = None):
        self.db_ic_device_delegate = db_ic_device_delegate
    # WARNING: Decompyle incomplete

    
    def dealloc(self = None):
        pass
    # WARNING: Decompyle incomplete

    didRemoveDevice_ = (lambda self = None, device = None: TRACE('ICDeviceDelegate::didRemoveDevice:')# WARNING: Decompyle incomplete
)()
    device_didOpenSessionWithError_ = (lambda self = None, device = objc.typedSelector(b'v@:@@'), error = event_handler_unknown_thread: TRACE('ICDeviceDelegate::device:didOpenSessionWithError:')# WARNING: Decompyle incomplete
)()()
    deviceDidBecomeReady_ = (lambda self = None, device = objc.typedSelector(b'v@:@'): TRACE('ICDeviceDelegate::deviceDidBecomeReady:')# WARNING: Decompyle incomplete
)()()
    device_didCloseSessionWithError_ = (lambda self = None, device = objc.typedSelector(b'v@:@@'), error = event_handler: TRACE('ICDeviceDelegate::device:didCloseSessionWithError:')# WARNING: Decompyle incomplete
)()()
    deviceDidChangeName_ = (lambda self = None, device = objc.typedSelector(b'v@:@'): TRACE('ICDeviceDelegate::deviceDidChangeName:'))()()
    deviceDidChangeSharingState_ = (lambda self = None, device = objc.typedSelector(b'v@:@'): TRACE('ICDeviceDelegate::deviceDidChangeSharingState:'))()()
    device_didReceiveStatusInformation_ = (lambda self = None, device = objc.typedSelector(b'v@:@@'), status = event_handler_unknown_thread: TRACE('ICDeviceDelegate::device:didReceiveStatusInformation:'))()()
    device_didEncounterError_ = (lambda self = None, device = objc.typedSelector(b'v@:@@'), error = event_handler: pass# WARNING: Decompyle incomplete
)()()
    device_didReceiveButtonPress_ = (lambda self = None, device = objc.typedSelector(b'v@:@@'), buttonType = event_handler_unknown_thread: TRACE('ICDeviceDelegate::device:didReceiveButtonPress:'))()()
    device_didReceiveCustomNotification_data_ = (lambda self = None, device = objc.typedSelector(b'v@:@@@'), notification = event_handler_unknown_thread, data = ('device', 'ICDevice', 'notification', 'NSDictionary', 'data', 'NSData', 'return', 'None'): TRACE('ICDeviceDelegate::device:didReceiveCustomNotification:data:'))()()
    cameraDevice_didAddItem_ = (lambda self = None, camera = objc.typedSelector(b'v@:@@'), item = event_handler_unknown_thread: TRACE('ICCameraDeviceDelegate::cameraDevice:didAddItem:'))()()
    cameraDevice_didAddItems_ = (lambda self = None, camera = objc.typedSelector(b'v@:@@'), items = event_handler_unknown_thread: TRACE('ICCameraDeviceDelegate::cameraDevice:didAddItems:'))()()
    cameraDevice_didRemoveItem_ = (lambda self, camera, item: TRACE('ICCameraDeviceDelegate::cameraDevice:didRemoveItem:'))()()
    cameraDevice_didRemoveItems_ = (lambda self, camera, items: TRACE('ICCameraDeviceDelegate::cameraDevice:didRemoveItems:'))()()
    cameraDevice_didRenameItems_ = (lambda self, camera, items: TRACE('ICCameraDeviceDelegate::cameraDevice:didRenameItems:'))()()
    cameraDevice_didCompleteDeleteFilesWithError_ = (lambda self = event_handler_unknown_thread, camera = objc.typedSelector(b'v@:@@'), error = event_handler_unknown_thread: TRACE('ICCameraDeviceDelegate::cameraDevice:didCompleteDeleteFilesWithError:'))()()
    cameraDeviceDidChangeCapability_ = (lambda self = objc.typedSelector(b'v@:@@'), camera = objc.typedSelector(b'v@:@'): TRACE('ICCameraDeviceDelegate::cameraDeviceDidChangeCapability:'))()()
    cameraDevice_didReceiveThumbnailForItem_ = (lambda self = event_handler_unknown_thread, camera = objc.typedSelector(b'v@:@@'), item = event_handler_unknown_thread: TRACE('ICCameraDeviceDelegate::cameraDevice:didReceiveThumbnailForItem:'))()()
    cameraDevice_didReceiveMetadataForItem_ = (lambda self = objc.typedSelector(b'v@:@@'), camera = objc.typedSelector(b'v@:@@'), item = event_handler_unknown_thread: TRACE('ICCameraDeviceDelegate::cameraDevice:didReceiveMetadataForItem:'))()()
    cameraDevice_didReceivePTPEvent_ = (lambda self = event_handler_unknown_thread, camera = objc.typedSelector(b'v@:@@'), eventData = event_handler_unknown_thread: TRACE('ICCameraDeviceDelegate::cameraDevice:didReceivePTPEvent:'))()()
    deviceDidBecomeReadyWithCompleteContentCatalog_ = (lambda self = objc.typedSelector(b'v@:@@'), device = objc.typedSelector(b'v@:@'): TRACE('ICCameraDeviceDelegate::deviceDidBecomeReadyWithCompleteContentCatalog:')# WARNING: Decompyle incomplete
)()()
    cameraDevice_shouldGetThumbnailOfItem_ = (lambda self = None, camera = objc.typedSelector(b'v@:@@'), item = event_handler_unknown_thread: TRACE('ICCameraDeviceDelegate::cameraDevice:shouldGetThumbnailOfItem:')True)()()
    cameraDevice_shouldGetMetadataOfItem_ = (lambda self, camera, item: TRACE('ICCameraDeviceDelegate::cameraDevice:shouldGetMetadataOfItem:')True)()()
    didDownloadFile_error_options_contextInfo_ = (lambda self, camera_file = event_handler_unknown_thread, error = objc.typedSelector(b'v@:@@@^v'), options = event_handler, contextInfo = ('camera_file', 'ICCameraFile', 'error', 'NSError', 'options', 'NSDictionary', 'contextInfo', 'int', 'return', 'None'): TRACE('ICCameraDeviceDownloadDelegate::didDownloadFile:error:options:contextInfo:')autoreleasepool()context_handle = objc.context.get(contextInfo)# WARNING: Decompyle incomplete
)()()
    
    def didReceiveDownloadProgressForFile_downloadedBytes_maxBytes_(self = None, camera_file = None, downloadedBytes = objc.typedSelector(b'v@:@@'), maxBytes = ('camera_file', 'ICCameraFile', 'downloadedBytes', 'int', 'maxBytes', 'int', 'return', 'None')):
        TRACE('ICCameraDeviceDownloadDelegate::didReceiveDownloadProgressForFile:downloadedBytes:maxBytes:')

    didReadData_fromFile_error_contextInfo_ = (lambda self, data = None, camera_item = objc.typedSelector(b'v@:@@@^v'), error = event_handler, context_info = ('data', 'NSData', 'camera_item', 'ICCameraFile', 'error', 'Optional[NSError]', 'context_info', 'int', 'return', 'None'): TRACE('didReadData:fromFile:error:contextInfo:')autoreleasepool()data_bytes = b''# WARNING: Decompyle incomplete
)()()


class ObjCICDeviceBrowser(DBICDeviceBrowser):
    
    def __init__(self = None):
        self.ic_browser = ICDeviceBrowser.alloc().init()
        self.ic_browser.setBrowsedDeviceTypeMask_(ICDeviceTypeMaskCamera | ICDeviceLocationTypeMaskLocal)
        TRACE('ObjCICDeviceBrowser initialized')
        self.delegate = ObjCICDeviceBrowserDelegate(self)

    
    def devices(self = None):
        autoreleasepool()
        apple_devices = []
        for ic_device in self.ic_browser.devices():
            if self.delegate.containsObjcDevice_(ic_device):
                apple_device = self.delegate.getObjcDevice_(ic_device)
                apple_devices.append(apple_device)
                continue
            report_exception(severity = Severity.WARN, component = DesktopComponent.SYNC_EVERYTHING)
            None(None, None)
            return 
            with None:
                if not None, apple_devices:
                    pass

    
    def start(self = None):
        TRACE('ICDeviceBrowser::start')
        autoreleasepool()
        self.ic_browser.start()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def stop(self = None):
        autoreleasepool()
        self.ic_browser.stop()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def set_delegate(self = None, db_ic_device_browser_delegate = None):
        self.delegate.setDelegateCallbacks_(db_ic_device_browser_delegate)



class ObjCICDeviceBrowserDelegate(NSObject):
    
    def __new__(cls = None, apple_browser = None):
        return ObjCICDeviceBrowserDelegate.alloc().init_(apple_browser)

    
    def init_(self = None, apple_browser = None):
        self = objc.super(ObjCICDeviceBrowserDelegate, self).init()
    # WARNING: Decompyle incomplete

    
    def setDelegateCallbacks_(self = None, db_ic_device_browser_delegate = None):
        self.db_ic_device_browser_delegate = db_ic_device_browser_delegate

    
    def containsObjcDevice_(self = None, ic_device = None):
        return ic_device.UUIDString() in self.camera_devices

    
    def getObjcDevice_(self = None, ic_device = None):
        return self.camera_devices[ic_device.UUIDString()]

    
    def createObjcDevice_(self = None, ic_device = None):
        apple_device = ObjCICCameraDevice(ic_device)
        self.camera_devices[ic_device.UUIDString()] = apple_device
        apple_device = self.camera_devices[ic_device.UUIDString()]
    # WARNING: Decompyle incomplete

    
    def dealloc(self = None):
        pass
    # WARNING: Decompyle incomplete

    deviceBrowser_didAddDevice_moreComing_ = (lambda self = None, ic_browser = objc.typedSelector(b'v@:@@B'), ic_device = event_handler, more_coming = ('ic_browser', 'ICDeviceBrowser', 'ic_device', 'ICDevice', 'more_coming', 'bool', 'return', 'None'): TRACE('ICDeviceBrowserDelegate::deviceBrowser:didAddDevice:moreComing:')# WARNING: Decompyle incomplete
)()()
    deviceBrowser_didRemoveDevice_moreGoing_ = (lambda self = None, ic_browser = objc.typedSelector(b'v@:@@B'), ic_device = event_handler, more_going = ('ic_browser', 'ICDeviceBrowser', 'ic_device', 'ICDevice', 'more_going', 'bool', 'return', 'None'): TRACE('ICDeviceBrowserDelegate::deviceBrowser:didRemoveDevice:moreGoing:')# WARNING: Decompyle incomplete
)()()
    deviceBrowser_deviceDidChangeName_ = (lambda self = None, browser = objc.typedSelector(b'v@:@@'), device = event_handler: TRACE('ICDeviceBrowserDelegate::deviceBrowser:deviceDidChangeName:'))()()
    deviceBrowser_deviceDidChangeSharingState_ = (lambda self = None, browser = objc.typedSelector(b'v@:@@'), device = event_handler: TRACE('ICDeviceBrowserDelegate::deviceBrowser:deviceDidChangeSharingState:'))()()
    deviceBrowser_requestsSelectDevice_ = (lambda self = None, browser = objc.typedSelector(b'v@:@@'), device = event_handler: TRACE('ICDeviceBrowserDelegate::deviceBrowser:requestsSelectDevice:'))()()
    deviceBrowserDidEnumerateLocalDevices_ = (lambda self = None, ic_browser = objc.typedSelector(b'v@:@'): TRACE('ICDeviceBrowserDelegate::deviceBrowserDidEnumerateLocalDevices:')# WARNING: Decompyle incomplete
)()()

