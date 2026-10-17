# Source Generated with Decompyle++
# File: system_preferences.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
import enum
import subprocess
from AppKit import NSWorkspace, NSWorkspaceLaunchAsync
from build_number import dropbox_version
from Foundation import NSAppleEventDescriptor, NSDictionary, NSPropertyListSerialization, NSPropertyListXMLFormat_v1_0, NSString, NSURL, NSUTF8StringEncoding
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.mac.internal import autoreleasepool, MacError
from dropbox.mac.version import CATALINA, HIGH_SIERRA, MAC_VERSION, MOJAVE
from dropbox.trace import TRACE

def open_security_pane_general():
    autoreleasepool()
    shared_workspace = NSWorkspace.sharedWorkspace()
    None(None, None)
    return None
    with None:
        if not None if MAC_VERSION <= HIGH_SIERRA else len:
            pass


class SecurityPaneServiceType(enum.Enum):
    DESKTOP_FOLDER = 'Privacy_DesktopFolder'
    DOCUMENTS_FOLDER = 'Privacy_DocumentsFolder'


def open_security_pane_privacy(service_type = None):
    autoreleasepool()
    shared_workspace = NSWorkspace.sharedWorkspace()
    pane_url = NSURL.fileURLWithPath_('/System/Library/PreferencePanes/Security.prefPane')
    pane_command_str = NSString.stringWithString_(service_type.value)
    pane_command = pane_command_str.dataUsingEncoding_(NSUTF8StringEncoding)
    desc = NSAppleEventDescriptor.alloc().initWithDescriptorType_data_(1886679669, pane_command)
    shared_workspace.openURLs_withAppBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifiers_([
        pane_url], None, NSWorkspaceLaunchAsync, desc, None)
    None(None, None)
    return None
    with None:
        if not None:
            pass


def open_accessibility_preferences():
    autoreleasepool()
    url = NSURL.URLWithString_('x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility')
    NSWorkspace.sharedWorkspace().openURL_(url)
    None(None, None)
    return None
    with None:
        if not None:
            pass


def open_automation_preferences():
    pass
# WARNING: Decompyle incomplete


def open_notifications_preferences():
    autoreleasepool()
    shared_workspace = NSWorkspace.sharedWorkspace()
# WARNING: Decompyle incomplete


def open_icloud_preferences():
    autoreleasepool()
    if MAC_VERSION >= CATALINA:
        url = NSURL.URLWithString_('x-apple.systempreferences:com.apple.preferences.AppleIDPrefPane?iCloud')
    else:
        url = NSURL.URLWithString_('x-apple.systempreferences:com.apple.preferences.icloud')
    NSWorkspace.sharedWorkspace().openURL_(url)
    None(None, None)
    return None
    with None:
        if not None:
            pass


def open_full_disk_access_preferences():
    autoreleasepool()
    url = NSURL.URLWithString_('x-apple.systempreferences:com.apple.preference.security?Privacy_AllFiles')
    NSWorkspace.sharedWorkspace().openURL_(url)
    None(None, None)
    return None
    with None:
        if not None:
            pass

