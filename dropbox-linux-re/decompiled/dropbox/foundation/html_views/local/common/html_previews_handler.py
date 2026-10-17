# Source Generated with Decompyle++
# File: html_previews_handler.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Dict, List, Text
from dropbox.client.features.previews.model.html_previews import fetch_html_preview
from dropbox.client_api.connection_util import ConnectionResponse
from dropbox.client_api.exceptions import DropboxServerError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.account_manager import AccountManager, AccountUpdate, AccountUpdateType
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.html_views.common.navigation_rules import LOCAL_VIEW_HTML_PREVIEWS_PATH_PREFIX
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.scheme_handler.interface import CustomSchemeHandlerInterface
from dropbox.foundation.scheme_handler.types import CustomSchemeHandlerResult, CustomSchemeUrlRequest, scheme_handler_perf_logging_percentage
from dropbox.trace import TRACE, WARNING

class LocalViewHtmlPreviewsHandler(CustomSchemeHandlerInterface):
    pass
# WARNING: Decompyle incomplete

