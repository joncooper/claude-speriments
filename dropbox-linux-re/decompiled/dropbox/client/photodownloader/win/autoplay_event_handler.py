# Source Generated with Decompyle++
# File: autoplay_event_handler.pyc (Python 3.11)

from __future__ import absolute_import
from ctypes import c_ulong
import comtypes
import comtypes.server.localserver as comtypes
from bazel_generated.comtypes.PhotoUploaderLib import AutoplayEventHandler
from build_number import BUILD_KEY
from dropbox.client.photodownloader.win.sdcarddevice import WinSDCardDevice
from dropbox.client.photodownloader.win.wpddevice import WpdDevice
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.trace import TRACE
DROPEFFECT_COPY = c_ulong(1)

class AutoplayEventHandlerImpl(AutoplayEventHandler):
    _reg_threading_ = 'Apartment'
    _reg_desc_ = BUILD_KEY + ' autoplay COM server'
    _reg_clsctx_ = comtypes.CLSCTX_LOCAL_SERVER
    _regcls_ = comtypes.server.localserver.REGCLS_MULTIPLEUSE
    
    def __init__(self):
        self._buffer = None
        self._block_size = 0

    
    def Initialize(self, init_params):
        TRACE('PHOTOUPLOADER: IHWEventHandler::Initialize')
        TRACE('init_params: %s', init_params)
        return 0

    
    def HandleEvent(self, device_id, alt_device_id, event_type):
        
        try:
            TRACE('PHOTOUPLOADER: IHWEventHandler::HandleEvent')
            TRACE('device_id: %r, alt_device_id: %r, event_type: %r', device_id, alt_device_id, event_type)
            if event_type != 'DeviceArrival':
                TRACE('!! HandleEvent received an event that was not a device arrival!')
                return 0
            WpdDevice(device_id, self.handler)
        except Exception:
            report_exception(component = DesktopComponent.SYNC_EVERYTHING)

        return 0

    
    def HandleEventWithContent(self, device_id, alt_device_id, event_type, content_type_handler, obj_data):
        TRACE('!! PHOTOUPLOADER: IHWEventHandler::HandleEventWithContent')
        return 0

    
    def DragEnter(self, data_obj, grfKeyState, pt, pdw_effect):
        TRACE('PHOTOUPLOADER: IDropTarget::DragEnter')
        pdw_effect.contents = DROPEFFECT_COPY
        return 0

    
    def DragOver(self, this, grfKeyState, pt, pdw_effect):
        TRACE('PHOTOUPLOADER: IDropTarget::DragOver')
        pdw_effect.contents = DROPEFFECT_COPY
        return 0

    
    def DragLeave(self):
        TRACE('PHOTOUPLOADER: IDropTarget::DragLeave')
        return 0

    
    def Drop(self, data_obj, key_state, pt, pdw_effect):
        
        try:
            TRACE('PHOTOUPLOADER: IDropTarget::Drop')
            TRACE('data_obj: %r, key_state: %r, pt: %r, dw_effect: %r', data_obj, key_state, pt, pdw_effect.contents)
            WinSDCardDevice(data_obj, self.handler)
            pdw_effect.contents = DROPEFFECT_COPY
        except Exception:
            report_exception(component = DesktopComponent.SYNC_EVERYTHING)

        return 0


