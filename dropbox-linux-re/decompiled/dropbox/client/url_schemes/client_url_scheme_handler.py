# Source Generated with Decompyle++
# File: client_url_scheme_handler.pyc (Python 3.11)

from typing import Optional, List, Mapping
from urllib.parse import parse_qs, ParseResult
from build_number import BUILD_KEY
from dropbox.client.features.foundation.custom_url_scheme_handler import CustomURLSchemeHandler
from dropbox.client.url_schemes.link_registry import LINK_REGISTRY
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.navigation_service.navigation_service import NavigationServiceInterface
from dropbox.threading import Lock
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.app.machine_ui_dispatcher import AttemptLinkFunc
    from dropbox.client.url_schemes.link_registry import LinkHandler

class DesktopClientURLSchemeHandler(CustomURLSchemeHandler):
    pass
# WARNING: Decompyle incomplete

