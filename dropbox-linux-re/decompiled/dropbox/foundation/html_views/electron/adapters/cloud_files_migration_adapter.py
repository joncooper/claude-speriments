# Source Generated with Decompyle++
# File: cloud_files_migration_adapter.pyc (Python 3.11)

from build_number.features import feature_enabled
from dropbox.client.features.cloud_files_migration.helpers import get_local_config
from dropbox.client.features.cloud_files_migration.migration_manager import CloudFilesMigrationManager
from dropbox.client.features.cloud_files_migration.state_machine import MigrationStateMachine
from dropbox.client.features.cloud_files_migration.types import CloudFilesAccountMigrationState, CloudFilesMigrationUIStatus
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures.basic import Future, ResolvedFuture
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.trace import TRACE
IPC_TOPIC = 'cloud_files_migration'

class CloudFilesMigrationAdapter(Destroyable):
    pass
# WARNING: Decompyle incomplete

