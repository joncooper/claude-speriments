# Source Generated with Decompyle++
# File: event_types.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function

class HarmonyRegressionMetrics(object):
    GET_ACTIVE_FILE_ATTEMPT = 'get_active_file_attempt'
    GET_ACTIVE_FILE_SUCCESS = 'get_active_file_success'
    BAUBLE_ON_WINDOW_SWITCH_ATTEMPT = 'show_bauble_on_window_switch_attempt'
    BAUBLE_ON_WINDOW_SWITCH_SUCCESS = 'show_bauble_on_window_switch_success'
    CONSISTENCY_CHECK_ATTEMPT = 'consistency_check_attempt'
    CONSISTENCY_CHECK_SUCCESS = 'consistency_check_success'
    FLYOUT_ON_CLICK_ATTEMPT = 'show_flyout_on_click_attempt'
    FLYOUT_ON_CLICK_SUCCESS = 'show_flyout_on_click_success'


class CoordinationEvent(object):
    ERROR = 'coordination_error'
    RESOLUTION_START = 'conflict_resolution_start'
    RESOLUTION_FAIL = 'conflict_resolution_failed'
    RESOLUTION_SUCCESS = 'conflict_resolution_success'
    START = 'coordination_start'
    SUCCESS = 'coordination_success'


class OwnerManagerEvents(object):
    MAYBE_MIGRATE_VISIBILITY_PREF_SUCCESS = 'maybe_migrate_visibility_pref_success'
    MAYBE_MIGRATE_VISIBILITY_PREF_FAIL = 'maybe_migrate_visibility_pref_fail'


class MEVOwnerEvents(object):
    MEV_OWNER_DESTROYED = 'mev_owner_destroyed'
    VIEW_PRUNED_EVENT = 'session_view_pruned'


class FileMapEvent(object):
    SUCCESS = 'file_map'
    ERROR = 'file_map_error'
    CONVERT = 'convert'

