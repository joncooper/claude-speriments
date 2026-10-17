# Source Generated with Decompyle++
# File: contact_worker.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from dropbox.client.message_queue import MessageQueueThread
from dropbox.db_thread import db_thread

class _ContactsWorkerThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

ContactsWorkerThread = db_thread(_ContactsWorkerThreadImpl)
on_contacts_thread = ContactsWorkerThread.on_queue

class ContactsBoltUpdateThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

ContactsBoltUpdateThread = db_thread(ContactsBoltUpdateThreadImpl)
on_contacts_bolt_thread = ContactsBoltUpdateThread.on_queue
