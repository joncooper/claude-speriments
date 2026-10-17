# Source Generated with Decompyle++
# File: proxies_sheet.pyc (Python 3.11)

from typing import Any, Dict
import objc
from AppKit import NSBackingStoreBuffered, NSClosableWindowMask, NSTitledWindowMask, NSWindow
from Foundation import NSZeroRect
from dropbox.client.ui.cocoa.preferences.inner.proxies_view import InnerProxiesView
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.foundation.context.machine import MachineContext

class ProxiesSheet(NSWindow):
    
    def __new__(cls = None, context = None, dropbox_app = None):
        return ProxiesSheet.alloc().initWithContext_DropboxApp_(context, dropbox_app)

    
    def initWithContext_DropboxApp_(self = None, context = None, dropbox_app = None):
        self = objc.super(ProxiesSheet, self).initWithContentRect_styleMask_backing_defer_(NSZeroRect, NSTitledWindowMask | NSClosableWindowMask, NSBackingStoreBuffered, True)
    # WARNING: Decompyle incomplete

    
    def readFromPreferences(self = None):
        self.innerView.setProxyMode_(self._local_config['proxy_mode'])
        self.innerView.setProxyType_(self._local_config['proxy_type'])
        self.innerView.setProxyServer_(self._local_config['proxy_server'])
        self.innerView.setProxyPort_(self._local_config['proxy_port'])
        self.innerView.setProxyRequiresAuth_(self._local_config['proxy_requires_auth'])
        self.innerView.setUsername_(self._local_config['proxy_username'])
        self.innerView.setPassword_(self._local_config['proxy_password'])

    
    def savePreferences(self = None):
        state = { }
        state['proxy_mode'] = self.innerView.proxyMode()
        state['proxy_type'] = self.innerView.proxyType()
        state['proxy_server'] = self.innerView.proxyServer()
        state['proxy_port'] = self.innerView.proxyPort()
        state['proxy_requires_auth'] = self.innerView.proxyRequiresAuth()
        state['proxy_username'] = self.innerView.username()
        state['proxy_password'] = self.innerView.password()
        self._dropbox_app.config_manager.update_preferences(state)


