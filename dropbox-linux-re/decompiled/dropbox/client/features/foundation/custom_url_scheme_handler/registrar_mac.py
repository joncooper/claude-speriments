# Source Generated with Decompyle++
# File: registrar_mac.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import struct
from AppKit import NSAppleEventManager
from Cocoa import NSAppleEventDescriptor
from registrar import URLSchemeRegistrar
from dropbox.components.desktop_components import DesktopComponent

def unpack_four_char_code(code = None):
    pass
# WARNING: Decompyle incomplete

kInternetEventClass = unpack_four_char_code(b'GURL')
kAEGetURL = kInternetEventClass

class MacURLSchemeRegistrar(URLSchemeRegistrar):
    
    def _handleEvent_withReplyEvent_(self = None, event = None, reply = None):
        url_descriptor = event.descriptorForKeyword_(unpack_four_char_code(b'----'))
        self.forward_or_queue_url_string(url_descriptor.stringValue()).ground(component = DesktopComponent.HTML_VIEWS)

    
    def _register_scheme(self = None):
        manager = NSAppleEventManager.sharedAppleEventManager()
        manager.setEventHandler_andSelector_forEventClass_andEventID_(self, '_handleEvent:withReplyEvent:', kInternetEventClass, kAEGetURL)


