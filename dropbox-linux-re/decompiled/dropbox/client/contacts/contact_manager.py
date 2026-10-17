# Source Generated with Decompyle++
# File: contact_manager.pyc (Python 3.11)

import base64
import json
import os
import time
import zlib
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional, Text
from dropbox.client.authentication.account import Account
from dropbox.client.bolt.signalling import BoltClient
from dropbox.client.bolt.types import BoltAppID, BoltChannelId, BoltChannelState, BoltRevisionInfo, BoltToken, BoltUniqueID
from dropbox.client.contacts.base_contact_controller import BaseContactsController
from dropbox.client.contacts.contact_db import ContactsDB
from dropbox.client.contacts.contact_worker import ContactsBoltUpdateThread, ContactsBoltUpdateThreadImpl, ContactsWorkerThread, on_contacts_bolt_thread, on_contacts_thread
from dropbox.client.contacts.polaris.types import ContactType
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import make_unicode
from dropbox.platform import platform as system_platform
from dropbox.threading import Lock
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class ContactsManager(BaseContactsController):
    pass
# WARNING: Decompyle incomplete


class ContactsBoltUpdateManager(object):
    BOLT_APP_ID = BoltAppID('contacts_cache_notify')
    
    def __init__(self = None, dropbox_app = None, bolt_client = None):
        self._setup_thread()
        self._bolt_client = bolt_client
        self.bolt_contacts_lock = Lock()
        self.bolt_contacts_need_update = False
        self._bolt_is_subscribed = False
        self._revision = 0
        self._notified_revision = 0
        self._unique_id = BoltUniqueID('')
        self._thread = None
        self.bolt_contacts_lock
        self._bolt_client.add_handler(key = self.BOLT_APP_ID, callback = self._bolt_update_callback)
        None(None, None)

    
    def _setup_thread(self = None):
        self._thread = ContactsBoltUpdateThread()
        self._thread.start()

    
    def _make_channel_state(self = None, new_revision = None, new_token = None, unique_id = ('new_revision', 'int', 'new_token', 'BoltToken', 'unique_id', 'BoltUniqueID', 'return', 'BoltChannelState')):
        return BoltChannelState(channel_id = BoltChannelId(unique_id = unique_id, app_id = self.BOLT_APP_ID), revision_info = BoltRevisionInfo(revision = new_revision, token = new_token))

    
    def _is_channel_invalid(self = None, invalid_channels = None):
        for channel_id in invalid_channels:
            if channel_id.unique_id == self._unique_id and channel_id.app_id == self.BOLT_APP_ID:
                return True
            return False

    
    def _get_our_channel(self = None, channel_states = None):
        for chan_state in channel_states:
            if chan_state.channel_id.unique_id == self._unique_id and chan_state.channel_id.app_id == self.BOLT_APP_ID:
                
                return None, chan_state
            return None

    _on_quit = (lambda self = None: if self._thread:
self._thread.signal_stop()self._thread = NoneNone)()
    
    def contacts_need_update(self = None):
        self.bolt_contacts_lock
        need_update = self.bolt_contacts_need_update
        self.bolt_contacts_need_update = False
        None(None, None)
        return 
        with None:
            if not None, need_update:
                pass

    
    def update_state(self = None, new_revision = None, new_token = None, unique_id = ('new_revision', 'int', 'new_token', 'BoltToken', 'unique_id', 'BoltUniqueID', 'return', 'None')):
        self.bolt_contacts_lock
        if self._unique_id and unique_id != self._unique_id:
            self._bolt_client.unsubscribe([
                BoltChannelId(unique_id = self._unique_id, app_id = self.BOLT_APP_ID)])
            self._bolt_is_subscribed = False
        self._unique_id = unique_id
        self._revision = new_revision
        if self._revision > self._notified_revision:
            self._notified_revision = self._revision
        if not self._bolt_is_subscribed:
            TRACE('Subcribing to Bolt for contacts cache notifications')
            self._bolt_client.subscribe([
                self._make_channel_state(new_revision, new_token, unique_id)])
            self._bolt_is_subscribed = True
        None(None, None)
        return None
        with None:
            if not None:
                pass

    _bolt_update_callback = (lambda self = None, channel_states = None, invalid_channels = on_contacts_bolt_thread: if self._is_channel_invalid(invalid_channels):
TRACE('Bolt callback received invalid channel')self.bolt_contacts_lockself._bolt_is_subscribed = Falseself.bolt_contacts_need_update = TrueNone(None, None)Nonewith None:
if not None:
passNoneour_channel_state = self._get_our_channel(channel_states)self.bolt_contacts_lockif our_channel_state and self._notified_revision < our_channel_state.revision_info.revision:
TRACE('Bolt callback received updated channels')self._notified_revision = our_channel_state.revision_info.revisionself.bolt_contacts_need_update = TrueNone(None, None)Nonewith None:
if not None:
pass)()

