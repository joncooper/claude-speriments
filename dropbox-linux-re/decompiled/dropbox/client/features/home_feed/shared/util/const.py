# Source Generated with Decompyle++
# File: const.pyc (Python 3.11)

from typing import Dict, Tuple, Type
from dropbox.client_api.exceptions import ConnectFailedOnAllAddressesError, HTTP401Error, HTTP429Error, TransientNetworkError
from dropbox.enum_utils import auto, AutoNameEnum
from dropbox.foundation.futures import Future

class RateLimitExceeded(Exception):
    pass


class NoopResponse:
    pass

EXPECTED_ERRORS: 'Tuple[Type[Exception], ...]' = (HTTP401Error, HTTP429Error, TransientNetworkError, RateLimitExceeded, ConnectFailedOnAllAddressesError)

class SyncWorkerRequestState(AutoNameEnum):
    Success = auto()
    Error = auto()
    TransientError = auto()
    Cancelled = auto()
    Incomplete = auto()
    Unknown = auto()

SyncWorkerRequestStateMap: 'Dict[Future.State, SyncWorkerRequestState]' = {
    Future.State.Incomplete: SyncWorkerRequestState.Incomplete,
    Future.State.Exception: SyncWorkerRequestState.Error,
    Future.State.Result: SyncWorkerRequestState.Success,
    Future.State.Cancelled: SyncWorkerRequestState.Cancelled }
