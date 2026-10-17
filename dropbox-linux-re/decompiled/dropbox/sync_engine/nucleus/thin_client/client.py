# Source Generated with Decompyle++
# File: client.pyc (Python 3.11)

from concurrent.futures import Future
from typing import Callable, cast, Dict, FrozenSet, Optional, Text
import tprt
from apex.context import ApexContext
from cffi_transport.cffi_interface import CFFIInterface
from cffi_transport.exceptions import ServiceNotAvailableException
from nucleus_python import NucleusSyncEngine
from classic_client.thin_adapter.event_publisher import PublishedEventWrapper
from  import logging
from base import NucleusThinClient as NucleusThinClientBase
from helpers import nucleus_migration_args_to_migration_mode
from reverse_app_service import NucleusReverseAppService
from transport_adapter import NucleusTprtTransportAdapter, NucleusTransportAdapter
from dropbox.build_common import get_build_number
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.encrypted_folder.client_key_pair import ClientKeyPair
from dropbox.client.features.encrypted_folder.fingerprint import TeamKeyFingerprint
from dropbox.client.features.sync_everything.v3.sync_everything_controller import debug_uuid
from dropbox.localized_strings.common import localized_strings
from dropbox.model.types import FileId, NsId
from dropbox.nucleus.icon_generation import generate_icon_paths
from dropbox.nucleus.migration_constants import NucleusMigrationArgs
from dropbox.proto.nucleus import feature_configs_pb2
from dropbox.proto.nucleus.app_service_pb2 import NucleusAPI_Stub, NucleusPhaseAgnosticAPI_Stub
from dropbox.proto.nucleus.sync_engine_pb2 import Account as NucleusAccount, BackupModeArgs, CdmRelocationMode, FPShadowConfig, NetworkConfig, SyncEngineCreateArgs, UserConfig
from dropbox.proto.nucleus.types_pb2 import FileId as FileIdProto
from dropbox.proto.sync_frontend.context_pb2 import RequestContext
from dropbox.sync_root.types import SyncRootType
from dropbox.trace import TRACE

def get_sync_engine_create_args(account, nucleus_account, sync_engine_build_no, metadata_directory, migration_args, client_session_id, root_moved, use_fake_network, initial_hidden_fileid_set, server_feature_configs, sync_root_type, cdm_relocation_mode, resource_throttle_mode, use_hql_event_logger, forced_run_type, backup_mode, client_key_pair, team_key_fingerprint = None, root_mount_path = None, user_config = None, network_config = (None, SyncEngineCreateArgs.ResourceThrottleMode.NORMAL, False, RequestContext.RunType.UNKNOWN, None, None, None, '', None, None, None), fp_shadow_config = ('account', 'AccountInterface', 'nucleus_account', 'NucleusAccount', 'sync_engine_build_no', 'str', 'metadata_directory', 'Text', 'migration_args', 'NucleusMigrationArgs', 'client_session_id', 'Optional[Text]', 'root_moved', 'SyncEngineCreateArgs.RootMovedStatus.V', 'use_fake_network', 'bool', 'initial_hidden_fileid_set', 'FrozenSet[FileId]', 'server_feature_configs', 'feature_configs_pb2.ServerFeatureConfigs', 'sync_root_type', 'SyncRootType', 'cdm_relocation_mode', 'Optional[CdmRelocationMode]', 'use_hql_event_logger', 'bool', 'backup_mode', 'Optional[BackupModeArgs]', 'client_key_pair', 'Optional[ClientKeyPair]', 'team_key_fingerprint', 'Optional[TeamKeyFingerprint]', 'root_mount_path', 'str', 'user_config', 'Optional[UserConfig]', 'network_config', 'Optional[NetworkConfig]', 'fp_shadow_config', 'Optional[FPShadowConfig]', 'return', 'SyncEngineCreateArgs')):
    pass
# WARNING: Decompyle incomplete


class NucleusThinTprtClient(NucleusThinClientBase, NucleusPhaseAgnosticAPI_Stub, NucleusAPI_Stub):
    pass
# WARNING: Decompyle incomplete


class NucleusThinClient(NucleusThinClientBase, NucleusPhaseAgnosticAPI_Stub, NucleusAPI_Stub):
    pass
# WARNING: Decompyle incomplete

