# Source Generated with Decompyle++
# File: pager.pyc (Python 3.11)

from __future__ import annotations
from abc import ABCMeta, abstractmethod, abstractproperty
from enum import IntEnum
from typing import Any, Optional, Text
from six import add_metaclass
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.infinite import infinite_platform_supported
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
MYPY = False
if MYPY:
    from dropbox.infinite.blacklist import InfiniteRecallBlacklist

class PagerNotLoadedError(Exception):
    pass


class PagerMissingElevationError(PagerNotLoadedError):
    pass


class KextNotApprovedError(PagerNotLoadedError):
    pass


class PagerCommunicationError(Exception):
    
    def __str__(self = None):
        return 'Failed to communicate with pager'


Pager = <NODE:12>()

class PagerRequestType(IntEnum):
    PAGE_FILE = 1
    MOVE_FILE = 2
    PAGE_FOLDER = 3
    CANCEL_PAGE = 4
    CANCEL_MOVE = 5

InfiniteRequest = <NODE:12>()
PageRequest = <NODE:12>()

class PageFileRequest(PageRequest):
    type = (lambda self = None: PagerRequestType.PAGE_FILE)()


class PageFolderRequest(PageRequest):
    type = (lambda self = None: PagerRequestType.PAGE_FOLDER)()


class CancelPageRequest(InfiniteRequest):
    type = (lambda self = None: PagerRequestType.CANCEL_PAGE)()


class CancelMoveRequest(InfiniteRequest):
    type = (lambda self = None: PagerRequestType.CANCEL_MOVE)()


class MoveFileRequest(InfiniteRequest):
    pass
# WARNING: Decompyle incomplete


class PageResponse(IntEnum):
    CANCEL = 0
    CONTINUE = 1
    CONTINUE_STILL_PLACEHOLDER = 2

