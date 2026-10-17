# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional
from dropbox.client.cli.control_thread import ControlThread
from dropbox.db_thread import db_thread
from dropbox.threading import Lock
MYPY = False
if MYPY:
    from dropbox.client.cli.tprt_control_endpoint import TprtControlEndpoint
    from dropbox.client.main import DropboxApplication
_ct: 'Optional[ControlThread]' = None
_tprt_endpoint: "Optional['TprtControlEndpoint']" = None
_tprt_endpoint_lock = Lock()

def start_control_thread(app = None):
    global _ct
    _ct = db_thread(ControlThread)(app)
    _ct.start()
    return _ct


def start_tprt_control_endpoint(app = None, primary_account_id = None):
    TprtControlEndpoint = TprtControlEndpoint
    import dropbox.client.cli.tprt_control_endpoint
    _tprt_endpoint_lock
# WARNING: Decompyle incomplete


def get_existing_control_thread():
    pass
# WARNING: Decompyle incomplete

