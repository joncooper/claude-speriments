# Source Generated with Decompyle++
# File: fsutil.pyc (Python 3.11)

import binascii
import contextlib
import errno
import os
import posixpath
import stat
import sys
import tempfile
from typing import Any, BinaryIO, Callable, ContextManager, Dict, Iterator, List, Optional, Text, Tuple, Union
from six import string_types
from six.moves import range
from dropbox.assertions import assert_
from dropbox.components.desktop_components import DesktopComponent
from dropbox.dirtraverse.common import DirectoryModifiedError
from dropbox.exception.reporting import report_exception, report_rare_event
from dropbox.exception.severity import Severity
from dropbox.fastwalk import fastwalk as fastwalk_fs, fastwalk_strict as _fastwalk_strict, fastwalk_with_exception_handling as fastwalk_with_exception_handling_fs, is_file_not_found_exception as _is_file_not_found_exception
from dropbox.fileutils import loop_delete
from dropbox.functions import EitherStr, make_bytes, split_extension
from dropbox.infinite import infinite_platform_supported
from dropbox.infinite.exceptions import NucleusPlaceholderError
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.shared.local_path import LocalPath
from dropbox.shared.util import db_lower
from dropbox.sync_engine_boundary.file_system_constants import DEFAULT_PRESERVED_ATTRS_NAME, FILE_TYPE_DIRECTORY, FILE_TYPE_POSIX_SYMLINK, FILE_TYPE_REGULAR, FILE_TYPE_WIN32_REPARSE_POINT, INTERNAL_PRESERVED_NAME, PERSISTED_FILEID_PRESERVED_NAME
from dropbox.sync_engine_boundary.file_system_exceptions import AttrsModifiedError, CannotMoveJunctionPointError, CannotMoveSymlinkError, FileExistsError, FilenameTooLongError, FileNotFoundError, FileSystemError, FSInvalidArgumentError, InfiniteKextIOError, NotADirectoryError, PermissionDeniedError
from dropbox.threading import RWLock
from dropbox.trace import TRACE, trace_stack
FileSystem = Any
MYPY = False
if MYPY:
    DropboxApplication = Any
    WindowsError = Any
    Gandalf = Any
# WARNING: Decompyle incomplete
