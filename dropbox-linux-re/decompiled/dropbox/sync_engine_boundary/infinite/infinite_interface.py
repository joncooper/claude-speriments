# Source Generated with Decompyle++
# File: infinite_interface.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Callable, Iterable, List
from dropbox.foundation.futures import Future
from dropbox.model.types import FileId
from dropbox.sync_engine_boundary.infinite.constants import InfiniteOperatingMode
MYPY = False
if MYPY:
    from dropbox.infinite.pager import CancelPageRequest, PageFileRequest, PageResponse

class NucleusInfiniteInterface(ABC):
    infinite_evict_batch = (lambda self = None, fileids = None, recursive = abstractmethod: raise NotImplementedError())()
    infinite_recall_batch = (lambda self = None, fileids = None, recursive = abstractmethod: raise NotImplementedError())()
    update_infinite_operating_mode = (lambda self = None, operating_mode = None: raise NotImplementedError())()
    set_infinite_page_response_callback = (lambda self = None, callback = None: raise NotImplementedError())()
    infinite_cancel_batch = (lambda self = None, cancel_ids = None: pass)()
    infinite_cancel_page_request = (lambda self = None, request = None: raise NotImplementedError())()
    infinite_ensure_recalled = (lambda self = None, fileid = None: raise NotImplementedError())()

