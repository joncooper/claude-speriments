# Source Generated with Decompyle++
# File: bridge_interface_view_context.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import List, Optional
from dropbox.foundation.futures import Future
from dropbox.foundation.html_views.common.bridge_gen.display import Display
from dropbox.foundation.html_views.common.bridge_gen.drag_record import DragRecord
from dropbox.foundation.html_views.common.bridge_gen.drop_operation import DropOperation
from dropbox.foundation.html_views.common.bridge_gen.file_folder_selector_options import FileFolderSelectorOptions
from dropbox.foundation.html_views.common.bridge_gen.point import Point
from dropbox.foundation.html_views.common.bridge_gen.rect import Rect
from dropbox.foundation.html_views.common.bridge_gen.size import Size
from dropbox.foundation.html_views.common.bridge_gen.types import NativeViewHandle
from dropbox.foundation.html_views.common.bridge_gen.view_close_reason import ViewCloseReason

class ViewContextBridgeInterface(ABC):
    resize = (lambda self = None, size = None: pass)()
    set_title = (lambda self = None, title = None: pass)()
    get_title = (lambda self = None: pass)()
    close = (lambda self = None, reason = None: pass)()
    close_with_result = (lambda self = None, reason = None, result = abstractmethod: pass)()
    hide = (lambda self = None: pass)()
    hide_with_result = (lambda self = None, result = None: pass)()
    show = (lambda self = None: pass)()
    foreground = (lambda self = None: pass)()
    get_origin = (lambda self = None: pass)()
    set_position = (lambda self = None, rect = None: pass)()
    move = (lambda self = None, origin = None: pass)()
    get_current_display = (lambda self = None: pass)()
    enter_fullscreen = (lambda self = None: pass)()
    exit_fullscreen = (lambda self = None: pass)()
    toggle_fullscreen = (lambda self = None: pass)()
    is_fullscreen = (lambda self = None: pass)()
    toggle_maximize = (lambda self = None: pass)()
    maximize = (lambda self = None: pass)()
    normalize = (lambda self = None: pass)()
    is_maximized = (lambda self = None: pass)()
    minimize = (lambda self = None: pass)()
    disable_traffic_lights = (lambda self = None: pass)()
    enable_traffic_lights = (lambda self = None: pass)()
    mark_update = (lambda self = None, render_tag_string = None: pass)()
    popup_view_menu = (lambda self = None, x = None, y = abstractmethod: pass)()
    start_native_drag = (lambda self = None, items = None, drag_image_size = abstractmethod: pass)()
    show_file_folder_selector = (lambda self = None, options = None: pass)()
    get_view_key = (lambda self = None: pass)()
    focus_parent = (lambda self = None: pass)()
    get_native_view_handle = (lambda self = None: pass)()

