# Source Generated with Decompyle++
# File: presence_tracker_interface.pyc (Python 3.11)

from abc import abstractmethod
from dropbox.foundation.futures import Future
from dropbox.shared.server_path import MRLowerServerPath

class PresenceTrackerInterface:
    async_report_file_viewing = (lambda self = None, server_path = None: pass)()
    async_report_file_offline = (lambda self = None, server_path = None: pass)()

