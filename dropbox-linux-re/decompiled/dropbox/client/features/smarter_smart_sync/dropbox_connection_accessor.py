# Source Generated with Decompyle++
# File: dropbox_connection_accessor.pyc (Python 3.11)

from typing import Optional
from dropbox.client_api.dropbox_connection import DropboxConnection

class DropboxConnectionAccessor:
    _connection = None
    
    def __init__(self):
        pass
    # WARNING: Decompyle incomplete

    add_connection = (lambda cls, connection: cls._connection = connection)()
    is_offline = (lambda cls: if cls._connection:
cls._connection.offline_status)()

