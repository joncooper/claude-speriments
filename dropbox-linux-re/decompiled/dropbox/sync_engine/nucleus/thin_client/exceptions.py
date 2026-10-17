# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from cffi_transport.exceptions import ServiceNotAvailableException as CFFIServiceNotAvailableException
from dropbox.exception.severity import Severity
from dropbox.sync_engine_boundary.exceptions import SyncEngineStoppedError

class NucleusClientError(Exception):
    _severity_class = Severity.CRITICAL


class UnhandledUnknownFileEventError(NucleusClientError):
    pass


class NucleusUnavailableError(CFFIServiceNotAvailableException, NucleusClientError):
    _severity_class = Severity.WARN


class NucleusNotAvailableDuringMoveDropbox(NucleusUnavailableError):
    _severity_class = Severity.TRACE


class NucleusNotAvailableDuringNucleusRestart(NucleusUnavailableError):
    _severity_class = Severity.TRACE


class NucleusConnectionInvalidatedError(NucleusUnavailableError):
    _severity_class = Severity.TRACE


class NucleusConnectionTimeoutError(NucleusUnavailableError):
    _severity_class = Severity.TRACE

SERVICE_UNAVAILABLE_EXCEPTIONS = tuple([
    CFFIServiceNotAvailableException,
    NucleusUnavailableError,
    SyncEngineStoppedError])
