# Source Generated with Decompyle++
# File: tray_controller_native_helpers.pyc (Python 3.11)

from typing import List, Optional, Sequence
from dropbox.foundation.html_views.common.bridge_gen.types import NativeViewHandle
from dropbox.platform import IS_MAC
if IS_MAC:
    import objc
    from AppKit import NSMakePoint, NSMenu, NSObject
    from Foundation import NSObject
    from dropbox.client.ui.cocoa.menu import EFMenu
    from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem
    from dropbox.exception.reporting import report_bad_assumption
    from dropbox.foundation.html_views.cocoa.helpers import get_nsview_from_bridged_native_handle
    from dropbox.foundation.performance import PerfSession
    from dropbox.foundation.performance.bridge_gen.perf_session_amp_logging_namespace import PerfSessionAmpLoggingNamespace
    from dropbox.gui import event_handler
    from dropbox.mac.typed_objc import typed_python_method
    from dropbox.trace import TRACE
    
    class EFTrayTopBarPopupMenu(EFMenu):
        
        def initWithDescriptor_(self = None, descriptor = None):
            self = objc.super(EFTrayTopBarPopupMenu, self).initWithDescriptor_(descriptor)
            if not self:
                return None
            None.setAutoenablesItems_(False)
            return self

        popup_tray_settings_menu = (lambda self = None, x = None, y = typed_python_method, native_view = ('x', 'int', 'y', 'int', 'native_view', 'NativeViewHandle'): menu_parent_view = get_nsview_from_bridged_native_handle(native_view)y = menu_parent_view.frame().size.height - yself.popUpMenuPositioningItem_atLocation_inView_(None, NSMakePoint(x, y), menu_parent_view))()

    
    class EFTrayPopupMenuController(NSObject):
        
        def initWithPerfSessionSubGroupName_(self = None, sub_group_name = None):
            self = self.init()
            if not self:
                return None
            self._menu_open = None
            self._perf_session = None
            self._menu_updates_queued = False
            self._menu_items = []
            self._sub_group_name = sub_group_name
            return self

        set_perf_session = (lambda self = None, perf_session = None: self._perf_session = perf_session)()
        update_menu = (lambda self = None, menu_items = None: self._menu_items = list(menu_items)if self._menu_open:
TRACE('Skipping menu updates since the menu is already open.')self._menu_updates_queued = TrueNone)()
        menuNeedsUpdate_ = (lambda self = None, menu = objc.typedSelector(b'v@:@'): pass# WARNING: Decompyle incomplete
)()()
        menuWillOpen_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): self._menu_open = True# WARNING: Decompyle incomplete
)()()
        menuDidClose_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): self._menu_open = Falseif self._menu_updates_queued:
TRACE('Updating menu for updates that were skipped while menu was open.')self.update_menu(self._menu_items)self._menu_updates_queued = FalseNone)()()

    return None
