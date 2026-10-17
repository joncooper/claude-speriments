# Source Generated with Decompyle++
# File: launcher.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import json
import socket
from typing import Any, Dict, Optional, Text
from six import iteritems
from dropbox.client.features.cesna.tests import construct_test
from dropbox.client.features.cesna.tests.base import CesnaTestInterface, UnsupportedCesnaTestError
from dropbox.client.features.cesna.updater import CesnaTestUpdater
from dropbox.client_api.exceptions import TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor, AutocancellerMixin
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture, sleep_async
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.transitional.connection_pool import make_delayed_network_call
from dropbox.trace import TRACE
CESNA_DNS_KILLSWITCH_DOMAIN = 'netmon-control.dropbox.com'
CESNA_SC_RULE = 'desktop-cesna-tests'

class CesnaTestState(AutocancellerMixin, Destroyable):
    pass
# WARNING: Decompyle incomplete


class CesnaTestLauncher(Actor):
    pass
# WARNING: Decompyle incomplete

