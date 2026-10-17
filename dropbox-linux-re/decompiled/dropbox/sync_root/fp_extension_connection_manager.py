# Source Generated with Decompyle++
# File: fp_extension_connection_manager.pyc (Python 3.11)

from typing import Optional
import tprt
from Foundation import NSError, NSXPCConnection
from google.protobuf.empty_pb2 import Empty
from google.protobuf.service import RpcController
from dropbox.backoff import TruncatedExponentialBackoff
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.futures import Future, ResolvedFuture, sleep_async
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.proto.nucleus.app_service_pb2 import EchoMessage
from dropbox.proto.nucleus.app_service_tprt_client import NucleusPhaseAgnosticAPIClient
from dropbox.sync_root.fp_helpers import fp_retrieve_boundary_connection
from dropbox.sync_root.fp_shadow_migration_constants import FP_EXTENSION_CONNECTION_RETRIEVAL_BACKOFF_MULTIPLIER, FP_EXTENSION_INITIAL_CONNECTION_RETRIEVAL_SLEEP, FP_EXTENSION_MAX_CONNECTION_RETRIEVAL_SLEEP, FP_EXTENSION_PING_PERIOD_SECONDS
from dropbox.trace import TRACE

class FPExtensionConnectionManager:
    
    def __init__(self = None, domain_id = None):
        self._domain_id = domain_id
        self._connection = None
        self._shutting_down = False
        self._backoff = TruncatedExponentialBackoff(FP_EXTENSION_INITIAL_CONNECTION_RETRIEVAL_SLEEP, FP_EXTENSION_MAX_CONNECTION_RETRIEVAL_SLEEP, FP_EXTENSION_CONNECTION_RETRIEVAL_BACKOFF_MULTIPLIER)
        self._ping_period_seconds = FP_EXTENSION_PING_PERIOD_SECONDS
        self._ping_generation = 0

    
    def establish_connection(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _retry_connection(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _start_ping_loop(self = None, phase_agnostic_client = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _on_connection_invalidated(self = None):
        TRACE('[FPExtensionConnectionManager] Connection invalidated for domain %r', self._domain_id)
        if self._shutting_down:
            TRACE('[FPExtensionConnectionManager] Shutting down, not re-establishing connection for domain %r', self._domain_id)
            return None
        self._connection = None
        TRACE('[FPExtensionConnectionManager] Re-establishing connection for domain %r', self._domain_id)
        self.establish_connection()

    
    def destroy(self = None):
        self._shutting_down = True
        if not self._connection:
            return None
        TRACE('[FPExtensionConnectionManager] Invalidating XPC connection for domain %r', self._domain_id)
        self._connection.invalidate()
        self._connection = None


