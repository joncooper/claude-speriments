# Source Generated with Decompyle++
# File: bandwidth_sheet.pyc (Python 3.11)

import objc
from AppKit import NSBackingStoreBuffered, NSClosableWindowMask, NSTitledWindowMask, NSWindow
from Foundation import NSZeroRect
from dropbox.client.ui.cocoa.preferences.inner.bandwidth_view import InnerBandwidthView
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.foundation.context.machine import MachineContext
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class BandwidthSheet(NSWindow):
    
    def __new__(cls = None, context = None, dropbox_app = None):
        return BandwidthSheet.alloc().initWithContext_DropboxApp_(context, dropbox_app)

    
    def initWithContext_DropboxApp_(self = None, context = None, dropbox_app = None):
        self = objc.super(BandwidthSheet, self).initWithContentRect_styleMask_backing_defer_(NSZeroRect, NSTitledWindowMask | NSClosableWindowMask, NSBackingStoreBuffered, True)
    # WARNING: Decompyle incomplete

    
    def readFromPreferences(self = None):
        self.innerView.setDownloadSpeed_(self._local_config['throttle_download_speed'])
        self.innerView.setUploadSpeed_(self._local_config['throttle_upload_speed'])
        self.innerView.setDownloadStyle_(self._local_config['throttle_download_style'])
        self.innerView.setUploadStyle_(self._local_config['throttle_upload_style'])

    
    def beginSheetForWindow_(self = None, window = None):
        
        try:
            self.innerView.beginSheet_forWindow_(self, window)
            return None
        except Exception:
            report_exception(component = DesktopComponent.PREFERENCES_UI)
            return None


    
    def savePreferences(self = None):
        state = dict(throttle_download_style = self.innerView.downloadStyle(), throttle_download_speed = self.innerView.downloadSpeed(), throttle_upload_style = self.innerView.uploadStyle(), throttle_upload_speed = self.innerView.uploadSpeed())
        self._dropbox_app.config_manager.update_preferences(state)


