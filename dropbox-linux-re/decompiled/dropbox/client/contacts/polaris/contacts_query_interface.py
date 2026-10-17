# Source Generated with Decompyle++
# File: contacts_query_interface.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import re
from collections import defaultdict, OrderedDict
from functools import partial
from typing import Callable, DefaultDict, List, Optional, Text, Tuple
from dropbox.client.contacts.polaris.types import Contact
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method
from dropbox.foundation.futures import Future
from dropbox.foundation.signals import RepeatedEventSignal
FB_PREFIX = '@fb:'
GROUP_PREFIX = 'g:'
STONE_API_EMAIL_REGEX = re.compile("^['&A-Za-z0-9._%+-]+@[A-Za-z0-9-][A-Za-z0-9.-]*.[A-Za-z]{2,15}$")

def is_valid_email(email = None):
