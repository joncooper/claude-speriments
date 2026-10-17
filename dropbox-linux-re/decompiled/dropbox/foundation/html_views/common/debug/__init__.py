# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
from typing import Text
from build_number import is_frozen
from build_number.environment import magic_trace_key_is_set
from build_number.features import feature_enabled
from dropbox.functions import make_str
from dropbox.platform import IS_MAC
HTML_VIEWS_DEFAULT_DEBUG_PORT_RUN_BOX = '7138'
HTML_VIEWS_DEFAULT_DEBUG_PORT_FROZEN = '7139'

def default_html_view_port():
    if is_frozen():
        return HTML_VIEWS_DEFAULT_DEBUG_PORT_FROZEN


def html_view_port_env_name():
    return 'ELECTRON_REMOTE_DEBUGGING'


def html_view_debugging_features_enabled():
