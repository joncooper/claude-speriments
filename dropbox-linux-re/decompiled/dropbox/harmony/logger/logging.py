# Source Generated with Decompyle++
# File: logging.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
from typing import Any, Dict, List, Optional, Text, Union
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventAction, EventClass, EventObject
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent, UserEventLoggingEvent
from dropbox.client.product_span import ProductSpan
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.event_names import HARMONY_EVENT
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.functions import md5_hash
from dropbox.harmony.logger.utils import get_application_type_from_aid, get_viewer_count_amis_bucket
from dropbox.harmony.models.types import ApplicationDetails, DocumentSession, DocumentSessionID, WindowDetails, WindowFile
from dropbox.trace import TRACE
Extra = Optional[Union[(List, bool, int, float, Text)]]

class Logger(Destroyable):
    pass
# WARNING: Decompyle incomplete

