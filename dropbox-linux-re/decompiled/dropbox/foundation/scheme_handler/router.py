# Source Generated with Decompyle++
# File: router.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Dict, Text, Tuple
from six.moves.urllib.parse import parse_qs, ParseResult, urlparse
from interface import CustomSchemeHandlerInterface, CustomSchemeRouterInterface
from types import CustomSchemeHandlerResult, CustomSchemeUrlRequest
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.wrappers import Transferable
from dropbox.foundation.reporting import report_app_framework_event_restricted
from dropbox.foundation.runtime import ExitCode, panic_with_report
from dropbox.functions import desanitize
from dropbox.threading import Condition, Lock
from dropbox.trace import TRACE, WARNING

class CustomSchemeRouter(CustomSchemeRouterInterface):
    pass
# WARNING: Decompyle incomplete

