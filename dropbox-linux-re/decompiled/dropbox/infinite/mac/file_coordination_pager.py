# Source Generated with Decompyle++
# File: file_coordination_pager.pyc (Python 3.11)

import errno
import os
import stat
import sys
from queue import Queue
from typing import Callable, Dict, Optional, Tuple
import objc
from Foundation import NSError, NSFileCoordinator, NSFileCoordinatorReadingImmediatelyAvailableMetadataOnly, NSObject, NSOperationQueue, NSPOSIXErrorDomain, NSString, NSURL
from macinfinite.common import DROPBOX_PLACEHOLDER_ATTR, process_path
from macinfinite.xattr import hasxattr
from build_number import BUILD_KEY
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.infinite.blacklist import InfiniteRecallBlacklist
from dropbox.infinite.constants import InfiniteEventType
from dropbox.infinite.pager import InfiniteRequest, PageFileRequest, PageFolderRequest, Pager, PagerCommunicationError, PageRequest, PageResponse
from dropbox.infinite.util import report_infinite_event
from dropbox.mac.internal import autoreleasepool
from dropbox.sync_engine_boundary.infinite.mac.xattr_placeholder_context import XattrPlaceholderContext
from dropbox.sync_event.report import truncated_hash
from dropbox.trace import TRACE
MYPY = False

class EFFileCoordinationProvider(NSObject):
    
    def initWithAccount_andBlacklist_andQueue_(self = None, account = None, recall_blacklist = None, queue = ('account', 'AccountInterface', 'recall_blacklist', 'InfiniteRecallBlacklist', 'queue', 'Queue[Tuple[PageRequest, Callable[[Optional[NSError]], None]]]', 'return', "'EFFileCoordinationProvider'")):
        self = objc.super(EFFileCoordinationProvider, self).init()
    # WARNING: Decompyle incomplete

    
    def _providedItemsOperationQueue(self = None):
        return self._operation_queue

    
    def _providedItemsURL(self = None):
        return self._root_url

    
    def _fileReactorID(self = None):
        return self._reactor_id

    
    def _provideItemAtURL_toReaderWithID_completionHandler_(self = None, itemUrl = None, claimID = None, replyBlock = ('itemUrl', 'NSURL', 'claimID', 'Optional[NSString]', 'return', 'None')):
        queued = False
    # WARNING: Decompyle incomplete

    
    def _cancelProvidingItemAtURL_toReaderWithID_(self = None, itemUrl = None, claimID = None):
        TRACE('[FCPager] cancel request to provide %r to reader %r', itemUrl, claimID)



class FileCoordinationPager(Pager):
    pass
# WARNING: Decompyle incomplete

