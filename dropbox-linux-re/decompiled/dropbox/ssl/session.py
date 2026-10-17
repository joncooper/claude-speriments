# Source Generated with Decompyle++
# File: session.pyc (Python 3.11)

from ssl import SSLContext, SSLSession
from typing import Dict
from dropbox.threading import Lock

class SSLSessionInfo(object):
    
    def __init__(self = None, session = None, context = None):
        self.session = session
        self.context = context

    
    def __repr__(self):
        return 'session: {} context: {}'.format(self.session, self.context)


DROPBOX_SSL_SESSION_DICT: 'Dict[str, SSLSessionInfo]' = { }
DROPBOX_SSL_SESSION_LOCK = Lock()
