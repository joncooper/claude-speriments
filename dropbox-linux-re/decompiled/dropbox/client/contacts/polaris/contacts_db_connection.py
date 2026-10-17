# Source Generated with Decompyle++
# File: contacts_db_connection.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
from typing import Any, Callable, Dict, List, Optional, Text, Tuple
from dropbox.client.bolt.types import BoltToken, BoltUniqueID
from dropbox.client.contacts.contact_db import CONTACTS_READ_LIMIT, ContactsDB
from dropbox.client.contacts.polaris.types import ContactLocalMetadata
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.trace import TRACE

class ContactsDBConnection(SingletonActor):
    pass
# WARNING: Decompyle incomplete

