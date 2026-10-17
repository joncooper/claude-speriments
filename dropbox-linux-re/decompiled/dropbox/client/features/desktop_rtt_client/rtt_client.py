# Source Generated with Decompyle++
# File: rtt_client.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.proto.growth_platform.rtt.triggers_pb2 import DesktopUserActionType
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.fenix.module import Fenix
    from dropbox.client.fenix.prompts_service import PromptsService
    from dropbox.foundation.context import Context
    from dropbox.foundation.futures.basic import Future

class DesktopRTTClient(SingletonActor):
    pass
# WARNING: Decompyle incomplete

