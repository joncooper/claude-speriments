# Source Generated with Decompyle++
# File: dropbox_menu.pyc (Python 3.11)

from __future__ import absolute_import
from enum import Enum
from typing import Any, Callable, NamedTuple, Optional, Sequence, Text, Union
MenuComponent = Union[('SubMenu', 'MenuItem', 'MenuRadioItems')]

class SubMenu:
    
    def __init__(self = None, label = None, subitems = None, image_path = (None, None), image_index = ('label', 'Text', 'subitems', 'Sequence[MenuComponent]', 'image_path', 'Optional[Text]', 'image_index', 'Optional[int]', 'return', 'None')):
        self.label = label
        self.subitems = subitems
        self.image_path = image_path
        self.image_index = image_index



class AfterTrayMenuAction(Enum):
    CLOSE_TRAY = 0
    KEEP_TRAY_OPEN = 1


class MenuItem:
    
    def __init__(self = None, label = None, action = None, *, checked, after_tray_menu_action, patched_action, image_path, image_index, enabled):
        self.label = label
        self.action = action
        self.checked = checked
        self.after_tray_menu_action = after_tray_menu_action
        self.patched_action = patched_action
        self.image_path = image_path
        self.image_index = image_index
        self.enabled = enabled

    
    def replace(self = None, **kwargs):
        replacement = MenuItem(label = self.label, action = self.action, checked = self.checked, after_tray_menu_action = self.after_tray_menu_action, patched_action = self.patched_action, image_path = self.image_path, image_index = self.image_index, enabled = self.enabled)
        for key, value in kwargs.items():
            setattr(replacement, key, value)
            return replacement


MenuRadioItems = NamedTuple('MenuRadioItems', [
    ('labels', Sequence[Text]),
    ('action', Callable[([
        int], None)]),
    ('default_checked', int)])
Separator = MenuItem('')
