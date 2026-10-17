# Source Generated with Decompyle++
# File: registrar.pyc (Python 3.11)

import sys
from abc import abstractmethod
from collections import defaultdict
from typing import DefaultDict, Dict, List, Optional, Text
from urllib.parse import ParseResult, urlparse
from build_number import is_electron_application
from dropbox.client.features.foundation.custom_url_scheme_handler import CustomURLSchemeHandler
from dropbox.client.url_schemes.client_url_scheme_handler import DesktopClientURLSchemeHandler
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures.basic import Future, ResolvedFuture
from dropbox.foundation.html_views.electron.ipc import JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronIpc, ElectronRpc
from dropbox.foundation.reporting import report_app_framework_event
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.foundation.signals import StandardSignal
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.trace import TRACE

class URLSchemeRegistrar(Actor):
    pass
# WARNING: Decompyle incomplete

