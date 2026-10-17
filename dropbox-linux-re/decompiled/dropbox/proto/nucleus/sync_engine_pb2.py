# Source Generated with Decompyle++
# File: sync_engine_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/nucleus/sync_engine.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.database import icons_pb2 as dropbox_dot_proto_dot_database_dot_icons__pb2
from dropbox.proto.nucleus import cdm_relocation_pb2 as dropbox_dot_proto_dot_nucleus_dot_cdm__relocation__pb2
from dropbox.proto.nucleus import feature_configs_pb2 as dropbox_dot_proto_dot_nucleus_dot_feature__configs__pb2
from dropbox.proto.nucleus import integration_test_pb2 as dropbox_dot_proto_dot_nucleus_dot_integration__test__pb2
from dropbox.proto.nucleus import migration_pb2 as dropbox_dot_proto_dot_nucleus_dot_migration__pb2
from dropbox.proto.nucleus import types_pb2 as dropbox_dot_proto_dot_nucleus_dot_types__pb2
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from dropbox.proto.sync_frontend import context_pb2 as dropbox_dot_proto_dot_sync__frontend_dot_context__pb2
from dropbox.proto.sync import remote_ops_pb2 as dropbox_dot_proto_dot_sync_dot_remote__ops__pb2
from dropbox.proto.sync import root_pb2 as dropbox_dot_proto_dot_sync_dot_root__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'dropbox/proto/nucleus/sync_engine.proto\x12\x07nucleus\x1a"dropbox/proto/database/icons.proto\x1a*dropbox/proto/nucleus/cdm_relocation.proto\x1a+dropbox/proto/nucleus/feature_configs.proto\x1a,dropbox/proto/nucleus/integration_test.proto\x1a%dropbox/proto/nucleus/migration.proto\x1a!dropbox/proto/nucleus/types.proto\x1a#dropbox/proto/rust/extensions.proto\x1a)dropbox/proto/sync_frontend/context.proto\x1a#dropbox/proto/sync/remote_ops.proto\x1a\x1ddropbox/proto/sync/root.proto\x1a\x1bgoogle/protobuf/empty.proto"\xf2\x04\n\x07Account\x12\x0f\n\x07host_id\x18\x01 \x01(\x04\x12\x10\n\x08host_key\x18\x02 \x01(\t\x12\x17\n\x0fpaired_host_key\x18\r \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\x03\x12\x16\n\x0epaired_user_id\x18\x0f \x01(\x03\x12\x12\n\naccount_id\x18\x11 \x01(\t\x12\x11\n\tdevice_id\x18\x0e \x01(\t\x12\x12\n\nroot_ns_id\x18\x06 \x01(\x04\x12\x12\n\nhome_ns_id\x18\x07 \x01(\x04\x12-\n\x0eroot_ns_fileid\x18\t \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00\x12-\n\x0ehome_ns_fileid\x18\n \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00\x12%\n\x0broot_layout\x18\x10 \x01(\x0e2\x10.sync.RootLayout\x12-\n\x08personal\x18\x0b \x01(\x0b2\x19.nucleus.Account.PersonalH\x00\x12)\n\x08business\x18\x0c \x01(\x0b2\x15.nucleus.Account.TeamH\x00\x1a\n\n\x08Personal\x1a\xb3\x01\n\x04Team\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08is_admin\x18\x03 \x01(\x08\x12$\n\x1cis_non_team_sharing_disabled\x18\x04 \x01(\x08\x12\x0f\n\x07team_id\x18\x05 \x01(\x03\x12\'\n\x1fis_team_file_transfers_disabled\x18\x06 \x01(\x08\x12+\n#is_team_send_for_signature_disabled\x18\x07 \x01(\x08B\x0c\n\x04role\x12\x04\x88\xb5\x18\x00J\x04\x08\x08\x10\t"9\n\x14LinkedAccountHostKey\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x10\n\x08host_key\x18\x02 \x01(\t"i\n\rNetworkConfig\x12\x17\n\x0fpaired_host_key\x18\x01 \x01(\t\x12?\n\x18linked_account_host_keys\x18\x02 \x03(\x0b2\x1d.nucleus.LinkedAccountHostKey"\x84\x01\n\x17FlexibleFilenamesConfig\x125\n\x05rules\x18\x01 \x01(\x0e2&.nucleus.FlexibleFilenamesConfig.Rules"2\n\x05Rules\x12\x11\n\rUNKNOWN_RULES\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\r\n\tVERSION_0\x10\x02"\xdc\x02\n\nUserConfig\x12<\n\x12flexible_filenames\x18\x01 \x01(\x0b2 .nucleus.FlexibleFilenamesConfig\x12\x18\n\x0bp2p_enabled\x18\x02 \x01(\x08H\x00\x88\x01\x01\x121\n$show_open_in_dropbox_foreground_menu\x18\x03 \x01(\x08H\x01\x88\x01\x01\x12&\n\x19local_block_cache_enabled\x18\x04 \x01(\x08H\x02\x88\x01\x01\x12&\n\x19local_block_cache_size_gb\x18\x05 \x01(\x04H\x03\x88\x01\x01B\x0e\n\x0c_p2p_enabledB\'\n%_show_open_in_dropbox_foreground_menuB\x1c\n\x1a_local_block_cache_enabledB\x1c\n\x1a_local_block_cache_size_gb"\x8e\x01\n\x12UpdatableAppConfig\x12\x1e\n\x16bolt_stormcrow_variant\x18\x02 \x01(\t\x12.\n\x0enetwork_config\x18\x04 \x01(\x0b2\x16.nucleus.NetworkConfig\x12(\n\x0buser_config\x18\x05 \x01(\x0b2\x13.nucleus.UserConfig"\xb7\x07\n\x10LocalizedStrings\x12\x1c\n\x14conflicted_copy_host\x18\x01 \x01(\t\x12\x1c\n\x14conflicted_copy_user\x18\x02 \x01(\t\x12\x1c\n\x14permissions_conflict\x18\x03 \x01(\t\x12\x15\n\rcase_conflict\x18\x04 \x01(\t\x12\x1b\n\x13whitespace_conflict\x18\x05 \x01(\t\x12!\n\x19unicode_encoding_conflict\x18\x06 \x01(\t\x12\x1f\n\x17selective_sync_conflict\x18\x07 \x01(\t\x12\x1a\n\x12camera_uploads_old\x18\x08 \x01(\t\x12\x15\n\rcycle_renamed\x18\t \x01(\t\x12\x1d\n\x15ignored_path_conflict\x18\n \x01(\t\x12\x1e\n\x16shared_folder_conflict\x18\x0b \x01(\t\x12\x1d\n\x15file_locking_conflict\x18\x0c \x01(\t\x12\x1e\n\x16invalid_files_conflict\x18\x0f \x01(\t\x12#\n\x1bmerge_into_dropbox_conflict\x18\x10 \x01(\t\x12"\n\x1aext_to_dbx_breadcrumb_name\x18\x11 \x01(\t\x12"\n\x1adbx_to_ext_breadcrumb_name\x18\x12 \x01(\t\x12\x1d\n\x15one_way_sync_conflict\x18\x13 \x01(\t\x12\x0f\n\x07ignored\x18\x16 \x01(\t\x12\x11\n\tcloud_doc\x18\x17 \x01(\t\x12\x19\n\x11error_sync_paused\x18\x14 \x01(\t\x12\x1b\n\x13error_invalid_phase\x18\x15 \x01(\t\x12\x1e\n\x16error_invalid_filename\x18\x18 \x01(\t\x12\x1b\n\x13error_trash_in_root\x18\x19 \x01(\t\x12\x1f\n\x17error_unsynced_filename\x18\x1a \x01(\t\x12\x1b\n\x13error_dropbox_cache\x18\x1b \x01(\t\x12\x1e\n\x16error_injected_failure\x18\x1c \x01(\t\x12\'\n\x1ferror_conflicted_copy_exhausted\x18\x1d \x01(\t\x12\x1e\n\x16fp_cannot_find_account\x18\x1e \x01(\t\x12$\n\x1cerror_invalid_symlink_target\x18\x1f \x01(\t\x12"\n\x1aerror_while_syncing_parent\x18  \x01(\tJ\x04\x08\r\x10\x0eJ\x04\x08\x0e\x10\x0f"\xad\x01\n\x11CdmRelocationMode\x12(\n cdm_relocation_target_root_ns_id\x18\x01 \x01(\x04\x12%\n\tteam_join\x18\x02 \x01(\x0b2\x10.nucleus.CdmJoinH\x00\x12,\n\nteam_leave\x18\x03 \x01(\x0b2\x16.google.protobuf.EmptyH\x00B\x19\n\x11relocate_scenario\x12\x04\x88\xb5\x18\x00"5\n\x0eBackupModeArgs\x12#\n\x1bpause_cboa_anchors_on_start\x18\x01 \x01(\x08"\xd6\x04\n\x18FPContextMenuPreferences\x12\x1b\n\x13show_get_signatures\x18\x01 \x01(\x08\x122\n*show_lock_unlock_editing_request_to_unlock\x18\x02 \x01(\x08\x12!\n\x19show_preview_with_dropbox\x18\x03 \x01(\x08\x12\x1f\n\x17show_rename_team_folder\x18\x04 \x01(\x08\x12\x1a\n\x12show_sign_yourself\x18\x05 \x01(\x08\x12\x1c\n\x14show_view_on_dropbox\x18\x07 \x01(\x08\x12\x16\n\x0eshow_copy_link\x18\x08 \x01(\x08\x12\'\n\x1fshow_team_folder_settings_share\x18\t \x01(\x08\x12\x1c\n\x14show_transfer_a_copy\x18\n \x01(\x08\x12\x1b\n\x13show_send_and_track\x18\x0b \x01(\x08\x12/\n\'show_make_online_only_make_offline_only\x18\x0c \x01(\x08\x12\x1c\n\x14show_version_history\x18\r \x01(\x08\x12,\n$show_ignore_dont_sync_to_dropbox_com\x18\x0e \x01(\x08\x12\x1b\n\x0eshow_file_info\x18\x0f \x01(\x08H\x00\x88\x01\x01\x12"\n\x15show_review_in_replay\x18\x10 \x01(\x08H\x01\x88\x01\x01B\x11\n\x0f_show_file_infoB\x18\n\x16_show_review_in_replayJ\x04\x08\x06\x10\x07"\x82\x11\n\x14SyncEngineCreateArgs\x12\x18\n\x10config_directory\x18\x01 \x01(\t\x12\'\n\x07account\x18\x02 \x01(\x0b2\x10.nucleus.AccountB\x04\xc0\xb5\x18\x00\x129\n\x0einitial_config\x18\x03 \x01(\x0b2\x1b.nucleus.UpdatableAppConfigB\x04\xc0\xb5\x18\x00\x12+\n\x0emigration_mode\x18\x05 \x01(\x0b2\r.nucleus.ModeB\x04\xc0\xb5\x18\x00\x12 \n\x05icons\x18\x07 \x03(\x0b2\x11.database.DBXIcon\x12\x10\n\x08build_no\x18\t \x01(\t\x12\x19\n\x11client_session_id\x18\n \x01(\t\x12A\n\nroot_moved\x18\x0b \x01(\x0e2-.nucleus.SyncEngineCreateArgs.RootMovedStatus\x12:\n\x11localized_strings\x18\x0c \x01(\x0b2\x19.nucleus.LocalizedStringsB\x04\xc0\xb5\x18\x00\x12?\n\x0cnetwork_type\x18\r \x01(\x0e2).nucleus.SyncEngineCreateArgs.NetworkType\x12\'\n\x0ehidden_fileids\x18\x0f \x03(\x0b2\x0f.nucleus.FileId\x12C\n\x16server_feature_configs\x18\x10 \x01(\x0b2\x1d.nucleus.ServerFeatureConfigsB\x04\xc0\xb5\x18\x00\x12\x1c\n\x14sync_engine_build_no\x18\x11 \x01(\t\x127\n\x13cdm_relocation_mode\x18\x13 \x01(\x0b2\x1a.nucleus.CdmRelocationMode\x12F\n\x1bfp_context_menu_preferences\x18\x17 \x01(\x0b2!.nucleus.FPContextMenuPreferences\x12R\n\x16resource_throttle_mode\x18\x18 \x01(\x0e22.nucleus.SyncEngineCreateArgs.ResourceThrottleMode\x12\x1c\n\x14use_hql_event_logger\x18\x19 \x01(\x08\x12>\n\x0fforced_run_type\x18\x1a \x01(\x0e2%.sync_frontend.RequestContext.RunType\x12,\n\x0bbackup_mode\x18\x1b \x01(\x0b2\x17.nucleus.BackupModeArgs\x12@\n\x17fake_network_extra_data\x18\x1c \x01(\x0b2\x1d.nucleus.FakeNetworkExtraDataH\x00\x12<\n\x0edevbox_network\x18" \x01(\x0b2".nucleus.DevboxIntegrationTestArgsH\x00\x126\n\x12hydration_settings\x18\x1d \x01(\x0b2\x1a.nucleus.HydrationSettings\x12D\n\x0fclient_key_pair\x18\x1e \x01(\x0b2+.nucleus.SyncEngineCreateArgs.ClientKeyPair\x12N\n\x14team_key_fingerprint\x18\x1f \x01(\x0b20.nucleus.SyncEngineCreateArgs.TeamKeyFingerprint\x12C\n\rmounted_paths\x18  \x01(\x0b2*.nucleus.SyncEngineCreateArgs.MountedPathsH\x01\x129\n\x08fp_paths\x18! \x01(\x0b2%.nucleus.SyncEngineCreateArgs.FpPathsH\x01\x12-\n\x0esync_root_type\x18# \x01(\x0e2\x15.nucleus.SyncRootType\x126\n\x10fp_shadow_config\x18% \x01(\x0b2\x17.nucleus.FPShadowConfigH\x02\x88\x01\x01\x12L\n\x1cfake_peer_network_extra_data\x18& \x01(\x0b2!.nucleus.FakePeerNetworkExtraDataH\x03\x88\x01\x01\x1aK\n\rClientKeyPair\x12\x11\n\talgorithm\x18\x01 \x01(\t\x12\x12\n\npublic_key\x18\x02 \x01(\x0c\x12\x13\n\x0bprivate_key\x18\x03 \x01(\x0c\x1a)\n\x12TeamKeyFingerprint\x12\x13\n\x0bfingerprint\x18\x01 \x01(\x0c\x1a\'\n\x0cMountedPaths\x12\x17\n\x0froot_mount_path\x18\x01 \x01(\t\x1aV\n\x07FpPaths\x12\x14\n\x0cscratch_path\x18\x01 \x01(\t\x12\x17\n\x0ffile_clone_path\x18\x02 \x01(\t\x12\x1c\n\x14old_config_directory\x18\x03 \x01(\t"Z\n\x0fRootMovedStatus\x12\x1a\n\x16UnknownRootMovedStatus\x10\x00\x12\x0c\n\x08NotMoved\x10\x01\x12\n\n\x06Copied\x10\x02\x12\x0b\n\x07Renamed\x10\x03\x1a\x04\x90\xb5\x18\x01"D\n\x0bNetworkType\x12\x0b\n\x07Unknown\x10\x00\x12\n\n\x06Normal\x10\x01\x12\x08\n\x04Fake\x10\x02\x12\x0c\n\x08ReadOnly\x10\x03\x1a\x04\x90\xb5\x18\x01"1\n\x14ResourceThrottleMode\x12\n\n\x06NORMAL\x10\x00\x12\r\n\tUNLIMITED\x10\x01B\x1b\n\x19test_only_network_backendB\x07\n\x05pathsB\x13\n\x11_fp_shadow_configB\x1f\n\x1d_fake_peer_network_extra_dataJ\x04\x08\x06\x10\x07J\x04\x08\x0e\x10\x0fJ\x04\x08\x12\x10\x13J\x04\x08\x16\x10\x17"x\n\x0eFPShadowConfig\x12%\n\x1dshadow_to_mounted_socket_path\x18\x01 \x01(\t\x12%\n\x1dmounted_to_shadow_socket_path\x18\x02 \x01(\t\x12\x18\n\x10shadow_domain_id\x18\x03 \x01(\t"z\n\x14FakeNetworkExtraData\x12\x12\n\ncreate_tmf\x18\x01 \x01(\x08\x124\n\x12root_ns_properties\x18\x02 \x01(\x0b2\x18.sync.TargetNSProperties\x12\x18\n\x10is_root_readonly\x18\x03 \x01(\x08"\x1a\n\x18FakePeerNetworkExtraData"B\n\x11HydrationSettings\x12-\n\x0broot_policy\x18\x01 \x01(\x0e2\x18.nucleus.HydrationPolicy*c\n\x0cSyncRootType\x12\x0b\n\x07MOUNTED\x10\x00\x12\x11\n\rFILE_PROVIDER\x10\x01\x12\x0f\n\x0bCLOUD_FILES\x10\x02\x12\t\n\x05DEBUG\x10\x03\x12\x17\n\x13FP_SHADOW_MIGRATION\x10\x04B\x0c\xa2\x02\tNucleusSEb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.nucleus.sync_engine_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\tNucleusSE'
    _globals['_ACCOUNT'].oneofs_by_name['role']._loaded_options = None
    _globals['_ACCOUNT'].oneofs_by_name['role']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_ACCOUNT'].fields_by_name['root_ns_fileid']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['root_ns_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_ACCOUNT'].fields_by_name['home_ns_fileid']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['home_ns_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_CDMRELOCATIONMODE'].oneofs_by_name['relocate_scenario']._loaded_options = None
    _globals['_CDMRELOCATIONMODE'].oneofs_by_name['relocate_scenario']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_SYNCENGINECREATEARGS_ROOTMOVEDSTATUS']._loaded_options = None
    _globals['_SYNCENGINECREATEARGS_ROOTMOVEDSTATUS']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_SYNCENGINECREATEARGS_NETWORKTYPE']._loaded_options = None
    _globals['_SYNCENGINECREATEARGS_NETWORKTYPE']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_SYNCENGINECREATEARGS'].fields_by_name['account']._loaded_options = None
    _globals['_SYNCENGINECREATEARGS'].fields_by_name['account']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCENGINECREATEARGS'].fields_by_name['initial_config']._loaded_options = None
    _globals['_SYNCENGINECREATEARGS'].fields_by_name['initial_config']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCENGINECREATEARGS'].fields_by_name['migration_mode']._loaded_options = None
    _globals['_SYNCENGINECREATEARGS'].fields_by_name['migration_mode']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCENGINECREATEARGS'].fields_by_name['localized_strings']._loaded_options = None
    _globals['_SYNCENGINECREATEARGS'].fields_by_name['localized_strings']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCENGINECREATEARGS'].fields_by_name['server_feature_configs']._loaded_options = None
    _globals['_SYNCENGINECREATEARGS'].fields_by_name['server_feature_configs']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCROOTTYPE']._serialized_start = 6209
    _globals['_SYNCROOTTYPE']._serialized_end = 6308
    _globals['_ACCOUNT']._serialized_start = 475
    _globals['_ACCOUNT']._serialized_end = 1101
    _globals['_ACCOUNT_PERSONAL']._serialized_start = 889
    _globals['_ACCOUNT_PERSONAL']._serialized_end = 899
    _globals['_ACCOUNT_TEAM']._serialized_start = 902
    _globals['_ACCOUNT_TEAM']._serialized_end = 1081
    _globals['_LINKEDACCOUNTHOSTKEY']._serialized_start = 1103
    _globals['_LINKEDACCOUNTHOSTKEY']._serialized_end = 1160
    _globals['_NETWORKCONFIG']._serialized_start = 1162
    _globals['_NETWORKCONFIG']._serialized_end = 1267
    _globals['_FLEXIBLEFILENAMESCONFIG']._serialized_start = 1270
    _globals['_FLEXIBLEFILENAMESCONFIG']._serialized_end = 1402
    _globals['_FLEXIBLEFILENAMESCONFIG_RULES']._serialized_start = 1352
    _globals['_FLEXIBLEFILENAMESCONFIG_RULES']._serialized_end = 1402
    _globals['_USERCONFIG']._serialized_start = 1405
    _globals['_USERCONFIG']._serialized_end = 1753
    _globals['_UPDATABLEAPPCONFIG']._serialized_start = 1756
    _globals['_UPDATABLEAPPCONFIG']._serialized_end = 1898
    _globals['_LOCALIZEDSTRINGS']._serialized_start = 1901
    _globals['_LOCALIZEDSTRINGS']._serialized_end = 2852
    _globals['_CDMRELOCATIONMODE']._serialized_start = 2855
    _globals['_CDMRELOCATIONMODE']._serialized_end = 3028
    _globals['_BACKUPMODEARGS']._serialized_start = 3030
    _globals['_BACKUPMODEARGS']._serialized_end = 3083
    _globals['_FPCONTEXTMENUPREFERENCES']._serialized_start = 3086
    _globals['_FPCONTEXTMENUPREFERENCES']._serialized_end = 3684
    _globals['_SYNCENGINECREATEARGS']._serialized_start = 3687
    _globals['_SYNCENGINECREATEARGS']._serialized_end = 5865
    _globals['_SYNCENGINECREATEARGS_CLIENTKEYPAIR']._serialized_start = 5289
    _globals['_SYNCENGINECREATEARGS_CLIENTKEYPAIR']._serialized_end = 5364
    _globals['_SYNCENGINECREATEARGS_TEAMKEYFINGERPRINT']._serialized_start = 5366
    _globals['_SYNCENGINECREATEARGS_TEAMKEYFINGERPRINT']._serialized_end = 5407
    _globals['_SYNCENGINECREATEARGS_MOUNTEDPATHS']._serialized_start = 5409
    _globals['_SYNCENGINECREATEARGS_MOUNTEDPATHS']._serialized_end = 5448
    _globals['_SYNCENGINECREATEARGS_FPPATHS']._serialized_start = 5450
    _globals['_SYNCENGINECREATEARGS_FPPATHS']._serialized_end = 5536
    _globals['_SYNCENGINECREATEARGS_ROOTMOVEDSTATUS']._serialized_start = 5538
    _globals['_SYNCENGINECREATEARGS_ROOTMOVEDSTATUS']._serialized_end = 5628
    _globals['_SYNCENGINECREATEARGS_NETWORKTYPE']._serialized_start = 5630
    _globals['_SYNCENGINECREATEARGS_NETWORKTYPE']._serialized_end = 5698
    _globals['_SYNCENGINECREATEARGS_RESOURCETHROTTLEMODE']._serialized_start = 5700
    _globals['_SYNCENGINECREATEARGS_RESOURCETHROTTLEMODE']._serialized_end = 5749
    _globals['_FPSHADOWCONFIG']._serialized_start = 5867
    _globals['_FPSHADOWCONFIG']._serialized_end = 5987
    _globals['_FAKENETWORKEXTRADATA']._serialized_start = 5989
    _globals['_FAKENETWORKEXTRADATA']._serialized_end = 6111
    _globals['_FAKEPEERNETWORKEXTRADATA']._serialized_start = 6113
    _globals['_FAKEPEERNETWORKEXTRADATA']._serialized_end = 6139
    _globals['_HYDRATIONSETTINGS']._serialized_start = 6141
    _globals['_HYDRATIONSETTINGS']._serialized_end = 6207
    return None
