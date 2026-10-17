# Source Generated with Decompyle++
# File: hostname.pyc (Python 3.11)

from __future__ import absolute_import
import socket
from typing import Text
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_MAC

def _get_short_unicode_hostname():
    hostname = _get_unicode_hostname()
    dot_index = hostname.find('.')
    if dot_index != -1:
        hostname = hostname[:dot_index]
    return hostname if hostname else 'localhost'


def _get_unicode_hostname():
    return socket.gethostname()


def get_local_host_display_name():
    pass
# WARNING: Decompyle incomplete

