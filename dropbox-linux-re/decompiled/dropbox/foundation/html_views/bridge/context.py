# Source Generated with Decompyle++
# File: context.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Callable, List, Optional, Text
from dropbox.foundation.futures import Future
from dropbox.foundation.html_views.common.bridge_gen.drag_record import DragRecord
from dropbox.foundation.html_views.common.bridge_gen.file_folder_selector_options import FileFolderSelectorOptions
from dropbox.foundation.html_views.common.bridge_gen.view_close_reason import ViewCloseReason
from dropbox.foundation.native_drag.model.types import DropOperation
from dropbox.foundation.system.display import Display
from dropbox.foundation.types.rect import Point, Rect
CloseWithResultType = Callable[([
    ViewCloseReason,
    Optional[Text]], None)]

class JavaScriptBridgeViewContext:
    
    def __init__(self, viewmgmt_close_func, foreground_window_func, set_is_topmost_view_level_func, viewmgmt_close_with_result_func, viewmgmt_hide_func, viewmgmt_hide_with_result_func, viewmgmt_show_func, viewmgmt_get_origin_func, viewmgmt_set_position_func, viewmgmt_move_func, viewmgmt_resize_func, viewmgmt_get_title_func, viewmgmt_set_title_func, viewmgmt_get_current_display_func, viewmgmt_enter_fullscreen_func, viewmgmt_exit_fullscreen_func, viewmgmt_is_fullscreen_func, viewmgmt_maximize_func, viewmgmt_normalize_func, viewmgmt_is_maximized_func, viewmgmt_minimize_func, viewmgmt_mark_update_func, viewmgmt_start_native_drag, viewmgmt_show_file_folder_selector, viewmgmt_get_view_key_func = None, popup_view_menu_func = None, viewmgmt_focus_parent_func = None, viewmgmt_disable_traffic_lights_func = (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None), viewmgmt_enable_traffic_lights_func = ('viewmgmt_close_func', 'Callable[[ViewCloseReason], None]', 'foreground_window_func', 'Optional[Callable[[], None]]', 'set_is_topmost_view_level_func', 'Optional[Callable[[bool], None]]', 'viewmgmt_close_with_result_func', 'Optional[CloseWithResultType]', 'viewmgmt_hide_func', 'Optional[Callable[[], None]]', 'viewmgmt_hide_with_result_func', 'Optional[Callable[[Optional[Text]], None]]', 'viewmgmt_show_func', 'Optional[Callable[[], None]]', 'viewmgmt_get_origin_func', 'Optional[Callable[[], Point]]', 'viewmgmt_set_position_func', 'Optional[Callable[[Rect], None]]', 'viewmgmt_move_func', 'Optional[Callable[[int, int], None]]', 'viewmgmt_resize_func', 'Optional[Callable[[int, int], None]]', 'viewmgmt_get_title_func', 'Optional[Callable[[], Text]]', 'viewmgmt_set_title_func', 'Optional[Callable[[Text], None]]', 'viewmgmt_get_current_display_func', 'Optional[Callable[[], Display]]', 'viewmgmt_enter_fullscreen_func', 'Optional[Callable[[], None]]', 'viewmgmt_exit_fullscreen_func', 'Optional[Callable[[], None]]', 'viewmgmt_is_fullscreen_func', 'Optional[Callable[[], bool]]', 'viewmgmt_maximize_func', 'Optional[Callable[[], None]]', 'viewmgmt_normalize_func', 'Optional[Callable[[], None]]', 'viewmgmt_is_maximized_func', 'Optional[Callable[[], bool]]', 'viewmgmt_minimize_func', 'Optional[Callable[[], None]]', 'viewmgmt_mark_update_func', 'Optional[Callable[[Text], None]]', 'viewmgmt_start_native_drag', 'Optional[Callable[[List[DragRecord], Optional[int]], Future[DropOperation]]]', 'viewmgmt_show_file_folder_selector', 'Optional[Callable[[FileFolderSelectorOptions], Future[Optional[Text]]]]', 'viewmgmt_get_view_key_func', 'Optional[Callable[[], Optional[Text]]]', 'popup_view_menu_func', 'Optional[Callable[[int, int], None]]', 'viewmgmt_focus_parent_func', 'Optional[Callable[[], None]]', 'viewmgmt_disable_traffic_lights_func', 'Optional[Callable[[], None]]', 'viewmgmt_enable_traffic_lights_func', 'Optional[Callable[[], None]]', 'return', 'None')):
        self._foreground_window_func = foreground_window_func
        self._set_is_topmost_view_level = set_is_topmost_view_level_func
        self._popup_view_menu_func = popup_view_menu_func
        self._view_management_close_func = viewmgmt_close_func
        self._view_management_close_with_result_func = viewmgmt_close_with_result_func
        self._view_management_hide_func = viewmgmt_hide_func
        self._view_management_hide_with_result_func = viewmgmt_hide_with_result_func
        self._view_management_show_func = viewmgmt_show_func
        self._view_management_get_origin_func = viewmgmt_get_origin_func
        self._view_management_set_position_func = viewmgmt_set_position_func
        self._view_management_move_func = viewmgmt_move_func
        self._view_management_resize_func = viewmgmt_resize_func
        self._view_management_get_title_func = viewmgmt_get_title_func
        self._view_management_set_title_func = viewmgmt_set_title_func
        self._view_management_get_current_display_func = viewmgmt_get_current_display_func
        self._view_management_enter_fullscreen_func = viewmgmt_enter_fullscreen_func
        self._view_management_exit_fullscreen_func = viewmgmt_exit_fullscreen_func
        self._view_management_is_fullscreen_func = viewmgmt_is_fullscreen_func
        self._view_management_maximize_func = viewmgmt_maximize_func
        self._view_management_normalize_func = viewmgmt_normalize_func
        self._view_management_is_maximized_func = viewmgmt_is_maximized_func
        self._view_management_minimize_func = viewmgmt_minimize_func
        self._view_management_mark_update_func = viewmgmt_mark_update_func
        self._view_management_start_native_drag = viewmgmt_start_native_drag
        self._view_management_show_file_folder_selector = viewmgmt_show_file_folder_selector
        self._view_management_get_view_key_func = viewmgmt_get_view_key_func
        self._view_management_focus_parent = viewmgmt_focus_parent_func
        self._view_management_disable_traffic_lights_func = viewmgmt_disable_traffic_lights_func
        self._view_management_enable_traffic_lights_func = viewmgmt_enable_traffic_lights_func

    
    def clear_actions(self = None):
        self._foreground_window_func = None
        self._set_is_topmost_view_level = None
        self._popup_view_menu_func = None
        self._view_management_close_with_result_func = None
        self._view_management_hide_func = None
        self._view_management_hide_with_result_func = None
        self._view_management_show_func = None
        self._view_management_get_origin_func = None
        self._view_management_set_position_func = None
        self._view_management_move_func = None
        self._view_management_resize_func = None
        self._view_management_get_title_func = None
        self._view_management_set_title_func = None
        self._view_management_get_current_display_func = None
        self._view_management_enter_fullscreen_func = None
        self._view_management_exit_fullscreen_func = None
        self._view_management_is_fullscreen_func = None
        self._view_management_maximize_func = None
        self._view_management_normalize_func = None
        self._view_management_is_maximized_func = None
        self._view_management_minimize_func = None
        self._view_management_mark_update_func = None
        self._view_management_start_native_drag = None
        self._view_management_show_file_folder_selector = None
        self._view_management_get_view_key_func = None
        self._view_management_focus_parent = None
        self._view_management_disable_traffic_lights_func = None
        self._view_management_enable_traffic_lights_func = None

    
    def copy_actions(self = None, other = None):
        self._foreground_window_func = other._foreground_window_func
        self._set_is_topmost_view_level = other._set_is_topmost_view_level
        self._popup_view_menu_func = other._popup_view_menu_func
        self._view_management_close_func = other._view_management_close_func
        self._view_management_close_with_result_func = other._view_management_close_with_result_func
        self._view_management_hide_func = other._view_management_hide_func
        self._view_management_hide_with_result_func = other._view_management_hide_with_result_func
        self._view_management_show_func = other._view_management_show_func
        self._view_management_get_origin_func = other._view_management_get_origin_func
        self._view_management_set_position_func = other._view_management_set_position_func
        self._view_management_move_func = other._view_management_move_func
        self._view_management_resize_func = other._view_management_resize_func
        self._view_management_get_title_func = other._view_management_get_title_func
        self._view_management_set_title_func = other._view_management_set_title_func
        self._view_management_get_current_display_func = other._view_management_get_current_display_func
        self._view_management_enter_fullscreen_func = other._view_management_enter_fullscreen_func
        self._view_management_exit_fullscreen_func = other._view_management_exit_fullscreen_func
        self._view_management_is_fullscreen_func = other._view_management_is_fullscreen_func
        self._view_management_maximize_func = other._view_management_maximize_func
        self._view_management_normalize_func = other._view_management_normalize_func
        self._view_management_is_maximized_func = other._view_management_is_maximized_func
        self._view_management_minimize_func = other._view_management_minimize_func
        self._view_management_mark_update_func = other._view_management_mark_update_func
        self._view_management_start_native_drag = other._view_management_start_native_drag
        self._view_management_show_file_folder_selector = other._view_management_show_file_folder_selector
        self._view_management_get_view_key_func = other._view_management_get_view_key_func
        self._view_management_focus_parent = other._view_management_focus_parent
        self._view_management_disable_traffic_lights_func = other._view_management_disable_traffic_lights_func
        self._view_management_enable_traffic_lights_func = other._view_management_enable_traffic_lights_func

    
    def is_foreground_window_supported(self = None):
        return self._foreground_window_func is not None

    
    def foreground_window(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_set_is_topmost_view_level_supported(self = None):
        return self._set_is_topmost_view_level is not None

    
    def set_is_topmost_view_level(self = None, is_topmost = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_view_management_get_current_display_supported(self = None):
        return self._view_management_get_current_display_func is not None

    
    def view_management_get_current_display(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def view_management_close(self = None, close_reason = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_view_management_close_with_result_supported(self = None):
        return self._view_management_close_with_result_func is not None

    
    def view_management_close_with_result(self = None, close_reason = None, result = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_view_management_hide_supported(self = None):
        return self._view_management_hide_func is not None

    
    def view_management_hide(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_view_management_hide_with_result_supported(self = None):
        return self._view_management_hide_with_result_func is not None

    
    def view_management_focus_parent(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def view_management_hide_with_result(self = None, result = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_view_management_show_supported(self = None):
        return self._view_management_show_func is not None

    
    def view_management_show(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_view_management_get_origin_supported(self = None):
        return self._view_management_get_origin_func is not None

    
    def view_management_get_origin(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_view_management_set_position_supported(self = None):
        return self._view_management_set_position_func is not None

    
    def view_management_set_position(self = None, rect = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_view_management_move_supported(self = None):
        return self._view_management_move_func is not None

    
    def view_management_move(self = None, x = None, y = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_view_management_resize_supported(self = None):
        return self._view_management_resize_func is not None

    
    def view_management_resize(self = None, width = None, height = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_view_management_get_title_supported(self = None):
        return self._view_management_get_title_func is not None

    
    def view_management_get_title(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_view_management_set_title_supported(self = None):
        return self._view_management_set_title_func is not None

    
    def view_management_set_title(self = None, title = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_view_management_fullscreen_supported(self = None):
