# Source Generated with Decompyle++
# File: proxies_view.pyc (Python 3.11)

from typing import Any
import objc
from AppKit import NSBeginAlertSheet, NSButton, NSColor, NSMatrix, NSNumberFormatter, NSPopUpButton, NSSecureTextField, NSTextField, NSView, NSWindow
from Foundation import NSHeight, NSMaxX, NSObject, NSRect, NSSize, NSWidth, NSZeroRect
from dropbox.client.ui.cocoa.constants import ENTER_KEY, ESCAPE_KEY
from dropbox.client.ui.cocoa.dynamic_layouts import BUTTON_TO_HELP_BUTTON_ADJUSTMENT_FLIPPED, CONTENT_BORDER, help_button, HORIZ_BUTTON_SPACING, NEARBY_CONTROL_BORDER
from dropbox.client.ui.cocoa.preferences.util import helpForPane_DropboxApp_
from dropbox.client.ui.common.misc import MiscStrings
from dropbox.client.ui.common.pref_strings import PrefStrings
from dropbox.client.ui.common.selective_sync_v2 import selsync_strings
from dropbox.foundation.context.machine import MachineContext
from dropbox.gui import event_handler
from dropbox.preferences import HTTP, SOCKS4, SOCKS5
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class InnerProxiesView(NSView):
    
    def __new__(cls = None, context = None, dropbox_app = None):
        return cls.alloc().initWithFrame_DropboxApp_(context, dropbox_app)

    
    def initWithFrame_DropboxApp_(self = None, context = None, dropbox_app = None):
        self = objc.super(InnerProxiesView, self).initWithFrame_(NSZeroRect)
    # WARNING: Decompyle incomplete

    
    def isFlipped(self = None):
        return True

    windowOk_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): if not self.proxyMode() == 2 and self.portIsValid():
self.tickleAlertSheetForPort()Noneif not None.proxyMode() == 2 and self.proxyServer().strip():
None(NSBeginAlertSheet, PrefStrings.proxy_server_not_set, MiscStrings.ok_button, None, self.window(), self, None, None, 0, '%@', PrefStrings.proxy_server_not_set_explanation)NoneNone.relevantSheet.savePreferences()self.relevantSheet.close())()()
    windowCancel_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): self.relevantSheet.close())()()
    sheetDidEnd_returnCode_contextInfo_ = (lambda self = None, sheet = objc.typedSelector(b'v@:@i@'), returnCode = event_handler, contextInfo = ('sheet', 'NSWindow', 'returnCode', 'int', 'contextInfo', 'Any', 'return', 'None'): sheet.orderOut_(self))()()
    
    def sizeToFit(self = None):
        height_needed = CONTENT_BORDER
        width_needed = 0
        max_label_x = max(NSWidth(self.proxySettingsLabel.frame()), NSWidth(self.proxyTypeLabel.frame()), NSWidth(self.proxyServerLabel.frame()))
        max_label_x += CONTENT_BORDER
        self.proxySettingsLabel.setFrameOrigin_((max_label_x - NSWidth(self.proxySettingsLabel.frame()), height_needed))
        self.proxySettingsMatrix.placeRelativeToLabel_(self.proxySettingsLabel)
        width_needed = max(width_needed, NSMaxX(self.proxySettingsMatrix.frame()))
        height_needed = self.proxySettingsMatrix.nextControlY()
        self.proxyTypeLabel.setFrameOrigin_((max_label_x - NSWidth(self.proxyTypeLabel.frame()), height_needed))
        self.proxyTypePopup.placeRelativeToLabel_(self.proxyTypeLabel)
        width_needed = max(width_needed, NSMaxX(self.proxyTypePopup.frame()))
        height_needed = self.proxyTypePopup.nextControlY()
        self.proxyServerLabel.setFrameOrigin_((max_label_x - NSWidth(self.proxyServerLabel.frame()), height_needed))
        self.proxyServerTextField.placeRelativeToLabel_(self.proxyServerLabel)
        self.proxyServerTextField.setDelegate_(self)
        self.colonLabel.setFrameOrigin_((NSMaxX(self.proxyServerTextField.frame()), self.proxyServerLabel.frame().origin.y))
        self.proxyPortTextField.placeRelativeToLabel_(self.colonLabel)
        self.proxyPortTextField.setFrameOrigin_((self.proxyPortTextField.frame().origin.x - self.colonLabel.horizontalPadding(), self.proxyPortTextField.frame().origin.y))
        width_needed = max(width_needed, NSMaxX(self.proxyPortTextField.frame()))
        height_needed = self.proxyServerTextField.nextControlY()
        self.proxyRequiresPassword.setFrameOrigin_((self.proxyServerTextField.frame().origin.x, height_needed))
        width_needed = max(width_needed, NSMaxX(self.proxyRequiresPassword.frame()))
        height_needed = self.proxyRequiresPassword.nextControlY()
        self.usernameLabel.setFrameOrigin_((max_label_x - NSWidth(self.usernameLabel.frame()), height_needed))
        self.usernameTextField.placeRelativeToLabel_(self.usernameLabel)
        self.usernameTextField.setDelegate_(self)
        width_needed = max(width_needed, NSMaxX(self.usernameTextField.frame()))
        height_needed = self.usernameTextField.nextControlY()
        self.passwordLabel.setFrameOrigin_((max_label_x - NSWidth(self.passwordLabel.frame()), height_needed))
        self.passwordTextField.placeRelativeToLabel_(self.passwordLabel)
        self.passwordTextField.setDelegate_(self)
        width_needed = max(width_needed, NSMaxX(self.passwordTextField.frame()))
        height_needed = self.passwordTextField.nextControlY()
        height_needed += NEARBY_CONTROL_BORDER
        button_size = self._okButton.frame().size
        height_needed += button_size.height + 10
        width_needed += CONTENT_BORDER
        self.setFrameSize_(NSSize(width_needed, height_needed))
        self.helpButton.alignLeftInSuperview()
        self.helpButton.alignBottomInSuperview()
        y = self.helpButton.frame().origin.y - BUTTON_TO_HELP_BUTTON_ADJUSTMENT_FLIPPED
        self._okButton.alignRightInSuperview()
        x = self._okButton.frame().origin.x
        self._okButton.setFrameOrigin_((x, y))
        x -= self._cancelButton.frame().size.width + HORIZ_BUTTON_SPACING
        self._cancelButton.setFrameOrigin_((x, y))

    
    def portIsValid(self = None):
        text = self.proxyPortTextField.stringValue()
        (valid, number, error) = self.proxyPortTextField.formatter().getObjectValue_forString_errorDescription_(None, text, None)
        return valid

    
    def safePortValue_(self, value):
        (valid, number, error) = self.proxyPortTextField.formatter().getObjectValue_forString_errorDescription_(None, value, None)
        return number if valid else 8080

    checkboxAction_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): for c in self.login_controls:
c.setEnabled_(sender.state())for c in self.login_labels:
c.setTextColor_(NSColor.controlTextColor() if sender.state() else NSColor.disabledControlTextColor())None)()()
    radioGroupAction_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): t = sender.selectedCell().tag()if t == 0 or t == 1:
for c in self.non_login_controls + self.login_controls:
c.setEnabled_(False)for c in self.non_login_labels + self.login_labels:
c.setTextColor_(NSColor.disabledControlTextColor())Nonefor c in self.non_login_controls:
c.setEnabled_(True)for c in self.non_login_labels:
c.setTextColor_(NSColor.controlTextColor())self.checkboxAction_(self.proxyRequiresPassword)None)()()
    
    def proxyMode(self = None):
        return self.proxySettingsMatrix.selectedCell().tag()

    
    def setProxyMode_(self = None, proxy_mode = None):
        pass
    # WARNING: Decompyle incomplete

    
    def proxyType(self = None):
        return self.proxyTypePopup.selectedItem().title()

    
    def setProxyType_(self = None, proxy_type = None):
        self.proxyTypePopup.selectItemWithTitle_(proxy_type)

    
    def proxyServer(self = None):
        return self.proxyServerTextField.stringValue()

    
    def setProxyServer_(self = None, proxy_server = None):
        self.proxyServerTextField.setStringValue_(proxy_server)

    
    def proxyPort(self):
        return self.safePortValue_(self.proxyPortTextField.stringValue())

    
    def setProxyPort_(self = None, proxy_port = None):
        self.proxyPortTextField.setIntValue_(proxy_port)

    
    def proxyRequiresAuth(self = None):
        return self.proxyRequiresPassword.state()

    
    def setProxyRequiresAuth_(self = None, auth = None):
        self.proxyRequiresPassword.setState_(auth)
        self.proxyRequiresPassword.sendAction_to_(self.proxyRequiresPassword.action(), self)

    
    def username(self = None):
        return self.usernameTextField.stringValue()

    
    def setUsername_(self = None, username = None):
        self.usernameTextField.setStringValue_(username)

    
    def password(self = None):
        return self.passwordTextField.stringValue()

    
    def setPassword_(self = None, password = None):
        self.passwordTextField.setStringValue_(password)

    
    def tickleAlertSheetForPort(self = None):
        text = self.proxyPortTextField.stringValue()
        (valid, number, error) = self.proxyPortTextField.formatter().getObjectValue_forString_errorDescription_(None, text, None)
        if not valid:
            self.control_didFailToFormatString_errorDescription_(None, None, error)
            return None

    
    def control_didFailToFormatString_errorDescription_(self, control, string, error):
        None(NSBeginAlertSheet, PrefStrings.invalid_port, MiscStrings.ok_button, None, self.window(), self, None, None, 0, '%@', error)
        return False

    userNeedsHelp_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): helpForPane_DropboxApp_('proxies', self._dropbox_app))()()

