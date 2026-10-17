# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from dropbox.sync_engine_boundary.exceptions import DropboxNotMountedError, UnmountedPathError

class ReconstructError(Exception):
    pass


class ReconstructCodeError(ReconstructError):
    
    def __init__(self, code):
        self.code = code



class ReconstructPossibleCorruptionError(ReconstructError):
    pass


class UnreconstructableError(ReconstructError):
    pass


class UnreconstructablePathError(UnreconstructableError):
    pass


class PredictableError(ReconstructError):
    pass


class CustomPermissionError(ReconstructError):
    pass


class NoParentFolderError(ReconstructError):
    pass


class BusyFileError(ReconstructError):
    pass


class MissingImportantAttrsError(ReconstructError):
    pass


class ReconstructErrorWithMessage(ReconstructError):
    
    def __str__(self):
        return self.str

    
    def __repr__(self):
        return self.str



class BadLocalDetailsError(ReconstructErrorWithMessage):
    
    def __init__(self, local_path, server_path, local_details, st):
        self.local_path = local_path
        self.str = f'''Expected different local file details, {local_path!r}:{server_path!r} {local_details!r} vs statted {st!r}'''



class ReconstructDirectoryNotEmptyError(ReconstructErrorWithMessage):
    
    def __init__(self, local_path):
        self.local_path = local_path
        self.str = 'Could not reconstruct over path %r due to directory not empty error' % local_path



class FileSystemStructureChangedError(Exception):
    pass


class FileProtectedError(Exception):
    pass


class FileMightBeTemporaryError(Exception):
    pass


class UnknownReparsePointError(Exception):
    pass


class UnmountTransitionError(Exception):
    pass


class FileCacheInconsistencyError(Exception):
    pass

