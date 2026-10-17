# Source Generated with Decompyle++
# File: menu.pyc (Python 3.11)

from __future__ import absolute_import
import uuid
from functools import partial
from typing import Any, Callable, Dict, FrozenSet, List, Optional, Sequence, Text, Tuple, Union
import objc
from AppKit import NSImage, NSMenu, NSMenuItem, NSOffState, NSOnState
from six.moves import range
from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem, MenuRadioItems, Separator, SubMenu
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.gui import event_handler
from dropbox.mac.typed_objc import typed_python_method
from dropbox.trace import TRACE

class EFMenuItem(NSMenuItem):
    
    def initWithTitle_target_action_state_(self, title, target, action, state = (None,)):
        self = objc.super(EFMenuItem, self).initWithTitle_action_keyEquivalent_(title, None, '')
        self.setTarget_(target)
        self.setAction_(action)
        self.state = state
        return self



class EFMenu(NSMenu):
    
    def initWithDescriptor_(self = None, descriptor = None):
        self = objc.super(EFMenu, self).init()
    # WARNING: Decompyle incomplete

    refreshDescriptor_ = (lambda self = None, descriptor = None: for i in reversed(range(self.numberOfItems())):
self.removeItemAtIndex_(i)for item in descriptor:
menuitem = self._create_and_add_menu_item(item)if menuitem:
self.addItem_(menuitem)self)()
    _create_and_add_menu_item = (lambda self = None, item = None: menuitem = Noneif item is Separator:
menuitem = EFMenuItem.separatorItem()elif isinstance(item, SubMenu):
text = Text(item.label)menuitem = EFMenuItem.alloc().initWithTitle_action_keyEquivalent_(text, None, '')if item.image_path:
menuitem.setImage_(NSImage.alloc().initWithContentsOfFile_(item.image_path))submenu = EFMenu.alloc().initWithDescriptor_(item.subitems)menuitem.setSubmenu_(submenu)elif isinstance(item, MenuItem):
menuitem = self._create_menu_item(label = item.label, action = item.action, checked = item.checked, image_path = item.image_path, enabled = item.enabled)elif isinstance(item, MenuRadioItems):
radioItems = []radioItemsId = uuid.uuid4()for index, label in enumerate(item.labels):
menuitem = self._create_menu_item(label = label, action = partial(self._radio_action_wrapper, item.action, index, radioItemsId), checked = index == item.default_checked)radioItems.append(menuitem)self.addItem_(menuitem)self._radioItems[radioItemsId] = radioItemsreport_bad_assumption('Invalid menu item: %s', item)menuitem)()
    refreshDescriptorConditional_ = (lambda self = None, descriptor = None: new_menu_components = frozenset(descriptor)deleted = self._menu_components - new_menu_componentsadded = new_menu_components - self._menu_componentsif len(deleted) == 0 and len(added) == 0:
False# WARNING: Decompyle incomplete
)()
    refreshDescriptorInPlaceIfKeysMatch_ = (lambda self = None, descriptor = None, keys = typed_python_method: previous_keys = self._last_menu_keys# WARNING: Decompyle incomplete
)()
    _create_menu_item = (lambda self = None, *, label: text = Text(label)menuitem = EFMenuItem.alloc().initWithTitle_action_keyEquivalent_(text, None, '')if callable(action):
enabled = enabledif enabled:
menuitem.dropboxFunc = actionmenuitem.setTarget_(self)menuitem.setAction_('menuAction:')else:
menuitem.setEnabled_(False)if checked and image_path:
report_bad_assumption('Do not allow to have both an icon and a check image until T288774 is fixed ')if checked:
menuitem.setState_(NSOnState)elif image_path:
menuitem.setImage_(NSImage.alloc().initWithContentsOfFile_(image_path))menuitem)()
    _radio_action_wrapper = (lambda self = None, action = None, click_index = objc.python_method, radioItemsId = ('action', 'Callable[[int], None]', 'click_index', 'int', 'radioItemsId', 'uuid.UUID', 'return', 'None'): for index, radioitem in enumerate(self._radioItems[radioItemsId]):
if click_index == index:
radioitem.setState_(NSOnState)continueradioitem.setState_(NSOffState)action(click_index)None)()
    menuAction_ = (lambda self = None, menu_item = objc.typedSelector(b'v@:@'): TRACE('menuAction: %s', menu_item.title())try:
menu_item.dropboxFunc()Noneexcept Exception:
report_exception(component = DesktopComponent.UI_KIT)None)()()

