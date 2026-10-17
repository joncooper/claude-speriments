# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from cffi_transport.exceptions import ServiceNotAvailableException as _ServiceNotAvailableException
from dropbox.exception.severity import Severity

class BlockContentsError(Exception):
    pass


class BlockContentsNotFoundError(BlockContentsError):
    pass


class BlockContentsBadDataError(BlockContentsError):
    pass


class ConditionTimeoutError(Exception):
    pass


class NamespaceNotMountedError(Exception):
    pass


class SyncEngineStoppedError(Exception):
    _severity_class = Severity.TRACE


class UnmountedPathError(Exception):
    pass


class InvalidRRServerPathNotInRootNs(Exception):
    pass


class InvalidLocalPathError(UnmountedPathError):
    pass


class LocalPathNotInDropboxError(UnmountedPathError):
    pass


class UnsyncablePathError(InvalidLocalPathError):
    pass


class UnwatchedPathError(UnmountedPathError):
    pass


class FileIdRaceError(UnmountedPathError):
    pass


class UnknownServerPathError(Exception):
    pass


class DropboxNotMountedError(Exception):
    pass


class InvalidSyncEngineFeatureException(Exception):
    pass


class EDPRevocationError(Exception):
    pass


class IncompleteMigrationException(Exception):
    pass


class NucleusProtoException(Exception):
    pass


class NetworkPathException(Exception):
    pass


class UnknownPathException(Exception):
    pass


class NucleusNotAvailableDuringAppShutdown(_ServiceNotAvailableException):
    _severity_class = Severity.TRACE


class ServiceNotAvailableException(Exception):
    pass


class FileProviderNoConsentException(Exception):
    pass


class OSFolderNotFoundException(Exception):
    pass

