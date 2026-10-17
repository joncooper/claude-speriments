# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import html
import os
import tempfile
from binascii import b2a_hex
from os.path import expanduser as _expanduser
from typing import Any, Dict, IO, List, NamedTuple, Optional, Set, Tuple
from urllib import parse as urlparse
from uuid import uuid4
from build_number.features import feature_enabled
from dropbox.async_timers import async_timers
from dropbox.build_common import get_build_number
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.desktop_login.constants import LINK_LIFETIME_SECONDS, PAGE_TIMEOUT_MS
from dropbox.client.desktop_login.prefetch import DesktopLoginPrefetch
from dropbox.client.desktop_login.resources import SPINNER_GIF_DATA
from dropbox.client.server_time_controller import ServerTimeController
from dropbox.client.ui.common.misc import MiscStrings
from dropbox.client.ui.common.pap_logging_helpers import log_desktop_to_web_redirect
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.dispatch import Worker
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import make_bytes, make_str, strxor
from dropbox.platform import IS_LINUX
from dropbox.trace import TRACE
from dropbox.url_info import url_from_path
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
LOGIN_CSS = '\n    <style type="text/css">\n        body {\n            text-align: center;\n        }\n        html,body {\n            height: 100%;\n        }\n        body:before {\n            content: \'\';\n            display: inline-block;\n            height: 100%;\n            vertical-align: middle;\n            margin-right: -0.25em; /* Adjusts for spacing */\n        }\n        .container {\n            display: inline-block;\n        }\n    </style>\n'
LOGIN_PAGE_TEMPLATE = '\n<!DOCTYPE html>\n<!-- saved from url=(0023)https://www.dropbox.com -->\r\n\n<html>\n<head>\n    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n    <script type="text/javascript">\n        (function () {\n            "use strict";\n            function join_nonce(b, c) {\n                if (b == undefined || c == undefined || c.length !== b.length || (c.length %% 2) !== 0) {\n                    // Invalid inputs; Return empty string.\n                    return null;\n                }\n\n                // hex-decode and xor\n                var a = \'\';\n                for (var i = 0; i !== c.length; i += 2) {\n                    a += String.fromCharCode(parseInt(c.slice(i, i + 2), 16) ^ parseInt(b.slice(i, i + 2), 16));\n                }\n                return a;\n            }\n            function go() {\n                var b_parts = window.location.hash.substr(1).split(\'-\');\n                // Clear the URI fragment, so that we don\'t try to re-use the\n                // nonce if the user presses \'Back\'.\n                window.location.hash = \'\';\n                var inputs = document.getElementsByName(\'n\');\n                var broken = false;\n                for (var i = 0; i < inputs.length; i++) {\n                    var input = inputs.item(i);\n                    var b = b_parts[i];\n                    var c = input.getAttribute(\'data-nonce-c\');\n                    var n = join_nonce(b, c);\n                    if (n === null) {\n                        broken = true;\n                        n = \'\';\n                    }\n                    input.setAttribute(\'value\', n);\n                }\n                if (broken) {\n                    // If any of the nonces are broken, don\'t send any.\n                    for (var i = 0; i < inputs.length; i++) {\n                        inputs.item(i).setAttribute(\'value\', \'\');\n                    }\n                }\n                setTimeout(function() { document.desktop_login.submit(); }, 100);\n                setTimeout(function() { window.location = %(default_web_url$j)s; }, %(page_timeout)d);\n            }\n            window.onload = go;\n        })();\n    </script>\n    %(login_css)s\n    <title>Dropbox</title>\n</head>\n<body>\n<div class="container">\n  <img width="40" height="40" src="data:image/gif;base64,%(loader_gif$h)s">\n</div>\n<form name="desktop_login" action="%(desktop_login_url$h)s" method="post">\n    %(form_elements)s\n    <noscript>\n        <div class="center">\n            <meta id="meta-refresh" http-equiv="refresh" content="2;URL=%(fallback_login_url$h)s">\n            <p>%(noscript_text$h)s</p>\n            <a href="%(fallback_login_url$h)s">%(signin_text$h)s</a>\n        </div>\n    </noscript>\n</form>\n</body>\n</html>\n'

class HostAuthParams(NamedTuple):
    client_locale: 'str' = 'HostAuthParams'

_OAUTH2_AUTHORIZE_PATH_PREFIX = '/oauth2/authorize'
_SCL_SHARING_PATH_PREFIXES = ('/scl/fi', '/scl/fo')
_SCL_NATIVE_NAVIGATION_GROWTHBOOK = 'desktop-experience-2026-09-17-app-shell-scl-native-navigation-enabled'
_GROWTHBOOK_ENABLED_VARIANTS = ('ON', 'FORCED_ON')

def _is_oauth2_authorize_url(url = None):
