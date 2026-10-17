# Source Generated with Decompyle++
# File: contacts_typeahead.pyc (Python 3.11)

from functools import partial
from time import time as _time
from typing import Dict, List, Optional, Text
from dropbox.client.contacts.polaris.contacts_db_updater import ContactsDBUpdater
from dropbox.client.contacts.polaris.types import Contact, ContactType
from dropbox.client.features.avatar.model.avatar_fetcher import CachedAvatarFetcher
from dropbox.client.fenix.journeys.file_transfer.bridge_dicts import ContactToken, ContactTokenVariantWithReason
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.basic import flatten_future
from dropbox.i18n import ungettext
from dropbox.trace import TRACE
SUGGESTIONS_LIMIT = 3
AVATAR_EXPIRY_SECONDS = 10800

def get_description(contact = None):
    pass
# WARNING: Decompyle incomplete


def get_initials_from_name(name = None):
    first_letters = name.split(' ')()
    return ''.join(first_letters[:2]).upper()


class ContactsTypeahead(Actor):
    pass
# WARNING: Decompyle incomplete

