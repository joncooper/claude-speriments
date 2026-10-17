# Source Generated with Decompyle++
# File: preferences.pyc (Python 3.11)

from AppKit import NSApp
from dropbox.client.ui.cocoa.preferences.bandwidth_sheet import BandwidthSheet
from dropbox.client.ui.cocoa.preferences.proxies_sheet import ProxiesSheet
from dropbox.client.ui.common.uikit import on_ui_thread
show_bandwidth_settings_dialog = (lambda machine_context = None, app = None: sheet = BandwidthSheet(machine_context, app)sheet.center()sheet.readFromPreferences()sheet.makeKeyAndOrderFront_(None)NSApp.activateIgnoringOtherApps_(True))()
show_proxy_settings_dialog = (lambda machine_context = None, app = None: sheet = ProxiesSheet(machine_context, app)sheet.center()sheet.readFromPreferences()sheet.makeKeyAndOrderFront_(None)NSApp.activateIgnoringOtherApps_(True))()
