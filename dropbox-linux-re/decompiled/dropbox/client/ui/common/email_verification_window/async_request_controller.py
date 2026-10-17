# Source Generated with Decompyle++
# File: async_request_controller.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Text
from six import add_metaclass
from dropbox.client.background_worker import on_background_thread
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.client_api.exceptions import DropboxServerError, is_transient_error
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.sharing.sharing_logger import ShareDesktopTiburonEvent
from dropbox.tiburon_log import log_tiburon_event
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.threadutils import ThreadPool

class AsyncRequestControllerStrings(UIStrings):
    server_error_msg = UI('We are unable to process your request. Please try again later.')
    transient_network_error_msg = UI('Check your internet connection and try again.')

AsyncRequestController = <NODE:12>()
