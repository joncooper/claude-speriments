# Source Generated with Decompyle++
# File: content_metadata.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, Callable, Dict, NamedTuple, Optional, Text, Type
from build_number.platform import IS_MAC, IS_WINDOWS
from interface import HtmlViewAffinityGroup, StandaloneHtmlViewLocation, ViewAnchorInterface
from dropbox.foundation.html_views.common.constants import MAC_DEFAULT_TITLE_BAR_HEIGHT
from dropbox.foundation.types.rect import Size
from dropbox.repr_utils import easy_repr
ResizeConfig = NamedTuple('ResizeConfig', [
    ('is_resizable', bool),
    ('min', Optional[Size]),
    ('max', Optional[Size])])

class MacInvisibleConfig(NamedTuple):
    title_bar_height: 'float' = MAC_DEFAULT_TITLE_BAR_HEIGHT
    traffic_light_buttons_hoffset: 'float' = 6


class WindowsInvisibleConfig(NamedTuple):
    title_bar_height: 'float' = 22
    title_bar_left_margin: 'int' = 50
    title_bar_right_margin: 'int' = 154


class TitleBarConfig(NamedTuple):
    windows_invisible_config: 'Optional[WindowsInvisibleConfig]' = None
    mac_invisible_config: 'Optional[MacInvisibleConfig]' = None


class FrameConfig(NamedTuple):
    title_bar: 'Optional[TitleBarConfig]' = None
    frameless: 'bool' = False


class StandaloneHtmlContentMetadata(object):
    __slots__ = ('_accessibility_identifier', '_default_title', '_view_anchor_class', '_default_location', '_default_width', '_default_height', '_default_is_visible', '_default_resize_config', '_default_always_on_top', '_is_minimizable', '_hide_on_close', '_frame', '_affinity_group', '_parent_id')
    create_with_defaults = (lambda accessibility_identifier, default_title, view_anchor_class, default_location, default_width, default_height, default_is_visible, default_resize_config, default_always_on_top, is_minimizable = None, hide_on_close = None, frame = staticmethod, affinity_group = (StandaloneHtmlViewLocation.CENTER_MAIN, 800, 600, True, ResizeConfig(is_resizable = False, min = None, max = None), False, True, False, FrameConfig(title_bar = TitleBarConfig(), frameless = False), HtmlViewAffinityGroup.DEFAULT, None), parent_id = ('accessibility_identifier', 'Callable[[], Text]', 'default_title', 'Callable[[], Text]', 'view_anchor_class', 'Type[ViewAnchorInterface]', 'default_location', 'StandaloneHtmlViewLocation', 'default_width', 'int', 'default_height', 'int', 'default_is_visible', 'bool', 'default_resize_config', 'ResizeConfig', 'default_always_on_top', 'bool', 'is_minimizable', 'bool', 'hide_on_close', 'bool', 'frame', 'FrameConfig', 'affinity_group', 'HtmlViewAffinityGroup', 'parent_id', 'Optional[int]', 'return', "'StandaloneHtmlContentMetadata'"): StandaloneHtmlContentMetadata(accessibility_identifier, default_title, view_anchor_class, default_location, default_width, default_height, default_is_visible, default_resize_config, default_always_on_top, is_minimizable, hide_on_close, frame, affinity_group, parent_id))()
    copy_with_changes = (lambda original, accessibility_identifier, default_title, view_anchor_class, default_location, default_width, default_height, default_is_visible, default_resize_config, default_always_on_top, is_minimizable = None, hide_on_close = None, frame = staticmethod, affinity_group = (None, None, None, None, None, None, None, None, None, None, None, None, None, None), parent_id = ('original', 'StandaloneHtmlContentMetadata', 'accessibility_identifier', 'Optional[Callable[[], Text]]', 'default_title', 'Optional[Callable[[], Text]]', 'view_anchor_class', 'Optional[Type[ViewAnchorInterface]]', 'default_location', 'Optional[StandaloneHtmlViewLocation]', 'default_width', 'Optional[int]', 'default_height', 'Optional[int]', 'default_is_visible', 'Optional[bool]', 'default_resize_config', 'Optional[ResizeConfig]', 'default_always_on_top', 'Optional[bool]', 'is_minimizable', 'Optional[bool]', 'hide_on_close', 'Optional[bool]', 'frame', 'Optional[FrameConfig]', 'affinity_group', 'Optional[HtmlViewAffinityGroup]', 'parent_id', 'Optional[int]', 'return', 'StandaloneHtmlContentMetadata'): pass# WARNING: Decompyle incomplete
)()
    
    def __init__(self, accessibility_identifier, default_title, view_anchor_class, default_location, default_width, default_height, default_is_visible, default_resize_config, default_always_on_top, is_minimizable, hide_on_close = None, frame = None, affinity_group = None, parent_id = ('accessibility_identifier', 'Callable[[], Text]', 'default_title', 'Callable[[], Text]', 'view_anchor_class', 'Type[ViewAnchorInterface]', 'default_location', 'StandaloneHtmlViewLocation', 'default_width', 'int', 'default_height', 'int', 'default_is_visible', 'bool', 'default_resize_config', 'ResizeConfig', 'default_always_on_top', 'bool', 'is_minimizable', 'bool', 'hide_on_close', 'bool', 'frame', 'FrameConfig', 'affinity_group', 'HtmlViewAffinityGroup', 'parent_id', 'Optional[int]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return self.__str__()

    accessibility_identifier = (lambda self = None: self._accessibility_identifier())()
    default_title = (lambda self = None: self._default_title())()
    view_anchor_class = (lambda self = None: self._view_anchor_class)()
    default_location = (lambda self = None: self._default_location)()
    default_width = (lambda self = None: self._default_width)()
    default_height = (lambda self = None: self._default_height)()
    default_is_visible = (lambda self = None: self._default_is_visible)()
    default_resize_config = (lambda self = None: self._default_resize_config)()
    default_always_on_top = (lambda self = None: self._default_always_on_top)()
    is_minimizable = (lambda self = None: self._is_minimizable)()
    hide_on_close = (lambda self = None: self._hide_on_close)()
    title_bar = (lambda self = None: self._frame.title_bar)()
    frame = (lambda self = None: self._frame)()
    has_frame = (lambda self = None: 