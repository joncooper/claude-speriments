# Source Generated with Decompyle++
# File: out_of_band_response.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum
from typing import Any, Dict, Optional, Text
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.url_info import DropboxURLInfo

class OutOfBandResponseSource(Enum):
    REGISTER_HOST = 'register_host'
    LIST_LEGACY = 'list_legacy'
    HOURLY_REFRESH = 'hourly_refresh'


class OutOfBandResponse:
    __slots__ = [
        'host_int',
        'server_time',
        'role',
        'ui_flags',
        'in_use',
        'quota',
        'quota_info',
        'is_msl_team',
        'is_user_msl_on',
        'server_map',
        'update_to_dict',
        'trace_request',
        'should_reboot',
        'delete_data_cmd',
        'unlink_message',
        'restart_message',
        'ns_p2p_key_map',
        'more_results']
    SECRET_KEYS = [
        'ns_p2p_key_map']
    
    def __init__(self = None, list_response = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __eq__(self = None, other = None):
        if not isinstance(other, OutOfBandResponse):
            return False
        for k in None.__slots__:
            if getattr(self, k) != getattr(other, k):
                return False
            return True


