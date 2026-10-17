# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

from typing import Any, Dict
from google.protobuf.empty_pb2 import Empty as EmptyPb
from dropbox.nucleus.migration_constants import NucleusMigrationArgs, SyncEngineState
from dropbox.proto.nucleus.migration_pb2 import Mode as MigrationMode, NucleusArgs, UpgradeFromClassicArgs

def nucleus_migration_args_to_migration_mode(args = None):
    state = args.migration_state
    if state == SyncEngineState.NUCLEUS:
        return MigrationMode(nucleus = NucleusArgs())
# WARNING: Decompyle incomplete

