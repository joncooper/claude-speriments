# Source Generated with Decompyle++
# File: file_system_exceptions.pyc (Python 3.11)

from __future__ import annotations
import errno
import functools
import os
from typing import Any, Dict, Optional, Text
from dropbox.exception.severity import Severity

class AttrsModifiedError(IOError):
    pass


class FileSystemError(OSError):
    pass
# WARNING: Decompyle incomplete


class FileNotFoundError(FileSystemError):
    file_system_errno = errno.ENOENT


class FileExistsError(FileSystemError):
    file_system_errno = errno.EEXIST


class NotADirectoryError(FileSystemError):
    file_system_errno = errno.ENOTDIR


class DirectoryNotEmptyError(FileSystemError):
    file_system_errno = errno.ENOTEMPTY


class IsADirectoryError(FileSystemError):
    file_system_errno = errno.EISDIR


class PermissionDeniedError(FileSystemError):
    file_system_errno = errno.EACCES


class FSInvalidArgumentError(FileSystemError):
    file_system_errno = errno.EINVAL


class FilenameTooLongError(FileSystemError):
    file_system_errno = errno.ENAMETOOLONG


class InfiniteKextIOError(FileSystemError):
    file_system_errno = 219


class AttrNotFoundError(FileSystemError):
    file_system_errno = 93


class OperationNotPermittedError(FileSystemError):
    file_system_errno = errno.EPERM


class NoSpaceOnDriveError(FileSystemError):
    file_system_errno = errno.ENOSPC


class TooManyOpenFilesError(FileSystemError):
    file_system_errno = errno.ENFILE


class MacKnownInvalidArgumentError(FileSystemError):
    file_system_errno = 1234500022
    from_error = (lambda e = None: MacKnownInvalidArgumentError(MacKnownInvalidArgumentError.file_system_errno, e.strerror))()

FileSystemError.register_substitute_subclasses()

def create_file_system_error(errno = None, message = None, filename = None, original_errno = (None, None, None, None), original_os_errno = ('errno', 'int', 'message', 'Optional[str]', 'filename', 'Optional[Text]', 'original_errno', 'Optional[int]', 'original_os_errno', 'Optional[int]', 'return', 'FileSystemError')):
    pass
# WARNING: Decompyle incomplete


def create_io_error(errno = None, message = None, filename = None):
    return create_file_system_error(errno, message, filename)


def _make_create_error_function(cls):
    return functools.partial(create_file_system_error, cls.file_system_errno)

create_file_not_found_error = _make_create_error_function(FileNotFoundError)
create_file_exists_error = _make_create_error_function(FileExistsError)
create_not_a_directory_error = _make_create_error_function(NotADirectoryError)
create_directory_not_empty_error = _make_create_error_function(DirectoryNotEmptyError)
create_is_a_directory_error = _make_create_error_function(IsADirectoryError)
create_permission_denied_error = _make_create_error_function(PermissionDeniedError)
create_fs_invalid_argument_error = _make_create_error_function(FSInvalidArgumentError)
create_filename_too_long_error = _make_create_error_function(FilenameTooLongError)
create_infinite_kext_io_error = _make_create_error_function(InfiniteKextIOError)
create_no_such_attr_error = _make_create_error_function(AttrNotFoundError)
create_no_space_on_drive_error = _make_create_error_function(NoSpaceOnDriveError)
create_too_many_open_files_error = _make_create_error_function(TooManyOpenFilesError)

class CannotMoveJunctionPointError(Exception):
    pass
# WARNING: Decompyle incomplete


class CannotMoveSymlinkError(Exception):
    pass
# WARNING: Decompyle incomplete


class ExclusiveAccessException(Exception):
    pass
# WARNING: Decompyle incomplete

