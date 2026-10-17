# Source Generated with Decompyle++
# File: contacts_db_updater.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import base64
import json
import zlib
from collections import OrderedDict
from datetime import datetime
from time import time as _time
from typing import Any, List, Optional, Text, Tuple
from dropbox.client.bolt.types import BoltToken, BoltUniqueID
from dropbox.client.contacts.polaris.contacts_bolt_update_manager import ContactsBoltUpdateManager
from dropbox.client.contacts.polaris.contacts_db_connection import ContactsDBConnection
from dropbox.client.contacts.polaris.contacts_query_interface import ContactsQueryInterface
from dropbox.client.contacts.polaris.types import Contact
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method, async_queued_method_2
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.functions import make_unicode
from dropbox.platform import platform as system_platform
from dropbox.sharing.constants.network_response import NetworkResponse
from dropbox.sharing.utils.network_util import make_api_request
from dropbox.trace import TRACE

class ContactsDBUpdater(SingletonActor):
    pass
# WARNING: Decompyle incomplete

