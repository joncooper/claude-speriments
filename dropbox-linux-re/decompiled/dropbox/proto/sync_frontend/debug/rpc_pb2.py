# Source Generated with Decompyle++
# File: rpc_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/sync_frontend/debug/rpc.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.mypy import mypy_pb2 as dropbox_dot_proto_dot_mypy_dot_mypy__pb2
from dropbox.proto.rpc_core import service_extensions_pb2 as dropbox_dot_proto_dot_rpc__core_dot_service__extensions__pb2
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from dropbox.proto.sync import cursor_pb2 as dropbox_dot_proto_dot_sync_dot_cursor__pb2
from dropbox.proto.sync import list_pb2 as dropbox_dot_proto_dot_sync_dot_list__pb2
from dropbox.proto.sync import remote_ops_pb2 as dropbox_dot_proto_dot_sync_dot_remote__ops__pb2
from dropbox.proto.sync import root_pb2 as dropbox_dot_proto_dot_sync_dot_root__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from dropbox.proto.test_services import service_extensions_pb2 as dropbox_dot_proto_dot_test__services_dot_service__extensions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+dropbox/proto/sync_frontend/debug/rpc.proto\x12\x11sync_frontend_dbg\x1a\x1ddropbox/proto/mypy/mypy.proto\x1a/dropbox/proto/rpc_core/service_extensions.proto\x1a#dropbox/proto/rust/extensions.proto\x1a\x1fdropbox/proto/sync/cursor.proto\x1a\x1ddropbox/proto/sync/list.proto\x1a#dropbox/proto/sync/remote_ops.proto\x1a\x1ddropbox/proto/sync/root.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a4dropbox/proto/test_services/service_extensions.proto"\xa5\x02\n\x13RegisterHostRequest\x125\n\x0fcreate_new_user\x18\x01 \x01(\x0b2\x1a.sync_frontend_dbg.NewUserH\x00\x129\n\x0flink_to_user_id\x18\x02 \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.UserIdH\x00\x12\x14\n\nseed_value\x18\x03 \x01(\x0cH\x01\x12!\n\x17run_synchronously_value\x18\x04 \x01(\x08H\x02\x12"\n\x18create_backup_root_value\x18\x05 \x01(\x08H\x03B\x0c\n\x04user\x12\x04\x88\xb5\x18\x00B\x06\n\x04seedB\x13\n\x11run_synchronouslyB\x14\n\x12create_backup_root"\xda\x01\n\x07NewUser\x12)\n\x07no_team\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x127\n\x08new_team\x18\x02 \x01(\x0e2#.sync_frontend_dbg.NewUser.TeamTypeH\x00\x127\n\rexisting_team\x18\x03 \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.TeamIdH\x00"$\n\x08TeamType\x12\x07\n\x03CDM\x10\x00\x12\x06\n\x02GG\x10\x01\x12\x07\n\x03TMR\x10\x02B\x0c\n\x04team\x12\x04\x88\xb5\x18\x00"\xb0\x04\n\x14RegisterHostResponse\x12/\n\x07host_id\x18\x01 \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.HostId\x120\n\nroot_ns_id\x18\x02 \x01(\x04B\x1c\x82\xa6\x1d\x18dropbox/model/types.NsId\x12\x10\n\x08host_key\x18\x03 \x01(\t\x12\x17\n\x0fpaired_host_key\x18\x0b \x01(\t\x12/\n\x07user_id\x18\x04 \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.UserId\x126\n\x0eroot_ns_fileid\x18\x05 \x01(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileId\x120\n\nhome_ns_id\x18\x06 \x01(\x04B\x1c\x82\xa6\x1d\x18dropbox/model/types.NsId\x12\x14\n\x0chome_ns_path\x18\x07 \x01(\t\x12/\n\x07team_id\x18\x08 \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.TeamId\x125\n\radmin_user_id\x18\t \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.UserId\x126\n\x0ehome_ns_fileid\x18\n \x01(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileId\x12%\n\x0broot_layout\x18\x0c \x01(\x0e2\x10.sync.RootLayout\x12\x12\n\naccount_id\x18\r \x01(\t"\xbf\x01\n\x13TreeSnapshotRequest\x12/\n\x07user_id\x18\x01 \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.UserId\x12\x12\n\nreveal_all\x18\x02 \x01(\x08\x12+\n\x05ns_id\x18\x03 \x01(\x04B\x1c\x82\xa6\x1d\x18dropbox/model/types.NsId\x126\n\x12transplant_version\x18\x04 \x01(\x0e2\x1a.sync.NamespaceViewVersion"\xcf\x02\n\x14TreeSnapshotResponse\x12,\n\x06cursor\x18\x01 \x01(\x0b2\x16.sync.LinearizedCursorB\x04\xc0\xb5\x18\x00\x124\n\x13transplant_segments\x18\x02 \x03(\x0b2\x17.sync.TransplantSegment\x12U\n\x14mount_to_root_fileid\x18\x03 \x03(\x0b27.sync_frontend_dbg.TreeSnapshotResponse.MountRootFileId\x1a|\n\x0fMountRootFileId\x124\n\x0cmount_fileid\x18\x01 \x01(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileId\x123\n\x0broot_fileid\x18\x02 \x01(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileId"u\n\x12ApplyRemoteRequest\x12"\n\x03ops\x18\x01 \x03(\x0b2\x15.sync.CommitOperation\x12/\n\x07host_id\x18\x04 \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.HostIdJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04"2\n\x13ApplyRemoteResponse\x12\x0f\n\x07allowed\x18\x03 \x03(\x08J\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03"V\n\x16ReassignFileIdsRequest\x12<\n\x14fileid_reassignments\x18\x01 \x03(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileId"U\n\x17ReassignFileIdsResponse\x12:\n\x12reassigned_fileids\x18\x01 \x03(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileId"\xb8\x01\n\x12ShareFolderRequest\x12/\n\tparent_ns\x18\x01 \x01(\x04B\x1c\x82\xa6\x1d\x18dropbox/model/types.NsId\x12.\n\x06fileid\x18\x02 \x01(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileId\x12\x10\n\x08writable\x18\x03 \x01(\x08\x12/\n\x07host_id\x18\x04 \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.HostId"a\n\x13ShareFolderResponse\x12@\n\x07success\x18\x01 \x01(\x0b2-.sync_frontend_dbg.ShareFolderSuccessResponseH\x00B\x08\n\x06result"\x83\x01\n\x1aShareFolderSuccessResponse\x12/\n\ttarget_ns\x18\x01 \x01(\x04B\x1c\x82\xa6\x1d\x18dropbox/model/types.NsId\x124\n\x0cmount_fileid\x18\x02 \x01(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileId"\x9b\x02\n\x18ChangePermissionsRequest\x12+\n\x05ns_id\x18\x01 \x01(\x04B\x1c\x82\xa6\x1d\x18dropbox/model/types.NsId\x12B\n\x06access\x18\x02 \x01(\x0e22.sync_frontend_dbg.ChangePermissionsRequest.Access\x12\x14\n\x0cconfidential\x18\x03 \x01(\x08\x12/\n\x07host_id\x18\x04 \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.HostId"G\n\x06Access\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tNO_ACCESS\x10\x01\x12\x0f\n\x0bREAD_ACCESS\x10\x02\x12\x10\n\x0cWRITE_ACCESS\x10\x03"\x1b\n\x19ChangePermissionsResponse"y\n\x19PropagateTraversalRequest\x12+\n\x05ns_id\x18\x01 \x01(\x04B\x1c\x82\xa6\x1d\x18dropbox/model/types.NsId\x12/\n\x07host_id\x18\x02 \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.HostId"M\n\x1aPropagateTraversalResponse\x12/\n\x07host_id\x18\x01 \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.HostId"\x15\n\x13InjectMountsRequest"\x16\n\x14InjectMountsResponse"o\n\x0cPurgeRequest\x12/\n\x07host_id\x18\x01 \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.HostId\x12.\n\x06fileid\x18\x02 \x01(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileId"\x0f\n\rPurgeResponse"\x18\n\x16DriveXOpWorkersRequest"2\n\x17DriveXOpWorkersResponse\x12\x17\n\x0fmore_work_to_do\x18\x01 \x01(\x08"\x17\n\x15HasPendingXOpsRequest"1\n\x16HasPendingXOpsResponse\x12\x17\n\x0fmore_work_to_do\x18\x01 \x01(\x08"\x8e\x01\n\x15CreateCloudDocRequest\x12/\n\x07host_id\x18\x01 \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.HostId\x122\n\ndir_fileid\x18\x02 \x01(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileId\x12\x10\n\x08filename\x18\x03 \x01(\t"*\n\x16CreateCloudDocResponse\x12\x10\n\x08filename\x18\x01 \x01(\t"f\n!CreateNonNestableNamespaceRequest\x12/\n\x07host_id\x18\x01 \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.HostId\x12\x10\n\x08filename\x18\x02 \x01(\t"T\n"CreateNonNestableNamespaceResponse\x12.\n\x06fileid\x18\x01 \x01(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileId"\\\n\x17CreateTeamFolderRequest\x12/\n\x07host_id\x18\x01 \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.HostId\x12\x10\n\x08filename\x18\x02 \x01(\t"J\n\x18CreateTeamFolderResponse\x12.\n\x06fileid\x18\x01 \x01(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileId"\xb3\x01\n\x11TmrMigrateRequest\x12/\n\x07host_id\x18\x01 \x01(\x04B\x1e\x82\xa6\x1d\x1adropbox/model/types.HostId\x120\n\x0emigrate_to_tmr\x18\x02 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x121\n\x0frevert_from_tmr\x18\x03 \x01(\x0b2\x16.google.protobuf.EmptyH\x00B\x08\n\x06action"c\n\x12TmrMigrateResponse\x12M\n\x16register_host_response\x18\x01 \x01(\x0b2\'.sync_frontend_dbg.RegisterHostResponseB\x04\xc0\xb5\x18\x002\xc9\r\n\x0fSyncFrontendDbg\x12g\n\x0cRegisterHost\x12&.sync_frontend_dbg.RegisterHostRequest\x1a\'.sync_frontend_dbg.RegisterHostResponse"\x06\x98\xb5\x18\xe0\xd4\x03\x12f\n\x0cTreeSnapshot\x12&.sync_frontend_dbg.TreeSnapshotRequest\x1a\'.sync_frontend_dbg.TreeSnapshotResponse"\x05\x98\xb5\x18\x90N\x12c\n\x0bApplyRemote\x12%.sync_frontend_dbg.ApplyRemoteRequest\x1a&.sync_frontend_dbg.ApplyRemoteResponse"\x05\x98\xb5\x18\x90N\x12o\n\x0fReassignFileIds\x12).sync_frontend_dbg.ReassignFileIdsRequest\x1a*.sync_frontend_dbg.ReassignFileIdsResponse"\x05\x98\xb5\x18\x90N\x12d\n\x0bShareFolder\x12%.sync_frontend_dbg.ShareFolderRequest\x1a&.sync_frontend_dbg.ShareFolderResponse"\x06\x98\xb5\x18\xa0\x9c\x01\x12u\n\x11ChangePermissions\x12+.sync_frontend_dbg.ChangePermissionsRequest\x1a,.sync_frontend_dbg.ChangePermissionsResponse"\x05\x98\xb5\x18\x90N\x12x\n\x12PropagateTraversal\x12,.sync_frontend_dbg.PropagateTraversalRequest\x1a-.sync_frontend_dbg.PropagateTraversalResponse"\x05\x98\xb5\x18\x90N\x12f\n\x0cInjectMounts\x12&.sync_frontend_dbg.InjectMountsRequest\x1a\'.sync_frontend_dbg.InjectMountsResponse"\x05\x98\xb5\x18\x90N\x12Q\n\x05Purge\x12\x1f.sync_frontend_dbg.PurgeRequest\x1a .sync_frontend_dbg.PurgeResponse"\x05\x98\xb5\x18\x90N\x12o\n\x0fDriveXOpWorkers\x12).sync_frontend_dbg.DriveXOpWorkersRequest\x1a*.sync_frontend_dbg.DriveXOpWorkersResponse"\x05\x98\xb5\x18\x90N\x12l\n\x0eHasPendingXOps\x12(.sync_frontend_dbg.HasPendingXOpsRequest\x1a).sync_frontend_dbg.HasPendingXOpsResponse"\x05\x98\xb5\x18\x90N\x12l\n\x0eCreateCloudDoc\x12(.sync_frontend_dbg.CreateCloudDocRequest\x1a).sync_frontend_dbg.CreateCloudDocResponse"\x05\x98\xb5\x18\x90N\x12a\n\nTmrMigrate\x12$.sync_frontend_dbg.TmrMigrateRequest\x1a%.sync_frontend_dbg.TmrMigrateResponse"\x06\x98\xb5\x18\xb0\xea\x01\x12\x90\x01\n\x1aCreateNonNestableNamespace\x124.sync_frontend_dbg.CreateNonNestableNamespaceRequest\x1a5.sync_frontend_dbg.CreateNonNestableNamespaceResponse"\x05\x98\xb5\x18\x90N\x12r\n\x10CreateTeamFolder\x12*.sync_frontend_dbg.CreateTeamFolderRequest\x1a+.sync_frontend_dbg.CreateTeamFolderResponse"\x05\x98\xb5\x18\x90N\x1aF\x82\xb2\x19B//metaserver/sync_frontend/debug_service:sync_frontend_dbg_serviceB#Z!dropbox/proto/sync_frontend/debugb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.sync_frontend.debug.rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z!dropbox/proto/sync_frontend/debug'
    _globals['_REGISTERHOSTREQUEST'].oneofs_by_name['user']._loaded_options = None
    _globals['_REGISTERHOSTREQUEST'].oneofs_by_name['user']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_REGISTERHOSTREQUEST'].fields_by_name['link_to_user_id']._loaded_options = None
    _globals['_REGISTERHOSTREQUEST'].fields_by_name['link_to_user_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.UserId'
    _globals['_NEWUSER'].oneofs_by_name['team']._loaded_options = None
    _globals['_NEWUSER'].oneofs_by_name['team']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_NEWUSER'].fields_by_name['existing_team']._loaded_options = None
    _globals['_NEWUSER'].fields_by_name['existing_team']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.TeamId'
    _globals['_REGISTERHOSTRESPONSE'].fields_by_name['host_id']._loaded_options = None
    _globals['_REGISTERHOSTRESPONSE'].fields_by_name['host_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.HostId'
    _globals['_REGISTERHOSTRESPONSE'].fields_by_name['root_ns_id']._loaded_options = None
    _globals['_REGISTERHOSTRESPONSE'].fields_by_name['root_ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId'
    _globals['_REGISTERHOSTRESPONSE'].fields_by_name['user_id']._loaded_options = None
    _globals['_REGISTERHOSTRESPONSE'].fields_by_name['user_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.UserId'
    _globals['_REGISTERHOSTRESPONSE'].fields_by_name['root_ns_fileid']._loaded_options = None
    _globals['_REGISTERHOSTRESPONSE'].fields_by_name['root_ns_fileid']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_REGISTERHOSTRESPONSE'].fields_by_name['home_ns_id']._loaded_options = None
    _globals['_REGISTERHOSTRESPONSE'].fields_by_name['home_ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId'
    _globals['_REGISTERHOSTRESPONSE'].fields_by_name['team_id']._loaded_options = None
    _globals['_REGISTERHOSTRESPONSE'].fields_by_name['team_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.TeamId'
    _globals['_REGISTERHOSTRESPONSE'].fields_by_name['admin_user_id']._loaded_options = None
    _globals['_REGISTERHOSTRESPONSE'].fields_by_name['admin_user_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.UserId'
    _globals['_REGISTERHOSTRESPONSE'].fields_by_name['home_ns_fileid']._loaded_options = None
    _globals['_REGISTERHOSTRESPONSE'].fields_by_name['home_ns_fileid']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_TREESNAPSHOTREQUEST'].fields_by_name['user_id']._loaded_options = None
    _globals['_TREESNAPSHOTREQUEST'].fields_by_name['user_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.UserId'
    _globals['_TREESNAPSHOTREQUEST'].fields_by_name['ns_id']._loaded_options = None
    _globals['_TREESNAPSHOTREQUEST'].fields_by_name['ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId'
    _globals['_TREESNAPSHOTRESPONSE_MOUNTROOTFILEID'].fields_by_name['mount_fileid']._loaded_options = None
    _globals['_TREESNAPSHOTRESPONSE_MOUNTROOTFILEID'].fields_by_name['mount_fileid']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_TREESNAPSHOTRESPONSE_MOUNTROOTFILEID'].fields_by_name['root_fileid']._loaded_options = None
    _globals['_TREESNAPSHOTRESPONSE_MOUNTROOTFILEID'].fields_by_name['root_fileid']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_TREESNAPSHOTRESPONSE'].fields_by_name['cursor']._loaded_options = None
    _globals['_TREESNAPSHOTRESPONSE'].fields_by_name['cursor']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_APPLYREMOTEREQUEST'].fields_by_name['host_id']._loaded_options = None
    _globals['_APPLYREMOTEREQUEST'].fields_by_name['host_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.HostId'
    _globals['_REASSIGNFILEIDSREQUEST'].fields_by_name['fileid_reassignments']._loaded_options = None
    _globals['_REASSIGNFILEIDSREQUEST'].fields_by_name['fileid_reassignments']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_REASSIGNFILEIDSRESPONSE'].fields_by_name['reassigned_fileids']._loaded_options = None
    _globals['_REASSIGNFILEIDSRESPONSE'].fields_by_name['reassigned_fileids']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_SHAREFOLDERREQUEST'].fields_by_name['parent_ns']._loaded_options = None
    _globals['_SHAREFOLDERREQUEST'].fields_by_name['parent_ns']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId'
    _globals['_SHAREFOLDERREQUEST'].fields_by_name['fileid']._loaded_options = None
    _globals['_SHAREFOLDERREQUEST'].fields_by_name['fileid']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_SHAREFOLDERREQUEST'].fields_by_name['host_id']._loaded_options = None
    _globals['_SHAREFOLDERREQUEST'].fields_by_name['host_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.HostId'
    _globals['_SHAREFOLDERSUCCESSRESPONSE'].fields_by_name['target_ns']._loaded_options = None
    _globals['_SHAREFOLDERSUCCESSRESPONSE'].fields_by_name['target_ns']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId'
    _globals['_SHAREFOLDERSUCCESSRESPONSE'].fields_by_name['mount_fileid']._loaded_options = None
    _globals['_SHAREFOLDERSUCCESSRESPONSE'].fields_by_name['mount_fileid']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_CHANGEPERMISSIONSREQUEST'].fields_by_name['ns_id']._loaded_options = None
    _globals['_CHANGEPERMISSIONSREQUEST'].fields_by_name['ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId'
    _globals['_CHANGEPERMISSIONSREQUEST'].fields_by_name['host_id']._loaded_options = None
    _globals['_CHANGEPERMISSIONSREQUEST'].fields_by_name['host_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.HostId'
    _globals['_PROPAGATETRAVERSALREQUEST'].fields_by_name['ns_id']._loaded_options = None
    _globals['_PROPAGATETRAVERSALREQUEST'].fields_by_name['ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId'
    _globals['_PROPAGATETRAVERSALREQUEST'].fields_by_name['host_id']._loaded_options = None
    _globals['_PROPAGATETRAVERSALREQUEST'].fields_by_name['host_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.HostId'
    _globals['_PROPAGATETRAVERSALRESPONSE'].fields_by_name['host_id']._loaded_options = None
    _globals['_PROPAGATETRAVERSALRESPONSE'].fields_by_name['host_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.HostId'
    _globals['_PURGEREQUEST'].fields_by_name['host_id']._loaded_options = None
    _globals['_PURGEREQUEST'].fields_by_name['host_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.HostId'
    _globals['_PURGEREQUEST'].fields_by_name['fileid']._loaded_options = None
    _globals['_PURGEREQUEST'].fields_by_name['fileid']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_CREATECLOUDDOCREQUEST'].fields_by_name['host_id']._loaded_options = None
    _globals['_CREATECLOUDDOCREQUEST'].fields_by_name['host_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.HostId'
    _globals['_CREATECLOUDDOCREQUEST'].fields_by_name['dir_fileid']._loaded_options = None
    _globals['_CREATECLOUDDOCREQUEST'].fields_by_name['dir_fileid']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_CREATENONNESTABLENAMESPACEREQUEST'].fields_by_name['host_id']._loaded_options = None
    _globals['_CREATENONNESTABLENAMESPACEREQUEST'].fields_by_name['host_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.HostId'
    _globals['_CREATENONNESTABLENAMESPACERESPONSE'].fields_by_name['fileid']._loaded_options = None
    _globals['_CREATENONNESTABLENAMESPACERESPONSE'].fields_by_name['fileid']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_CREATETEAMFOLDERREQUEST'].fields_by_name['host_id']._loaded_options = None
    _globals['_CREATETEAMFOLDERREQUEST'].fields_by_name['host_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.HostId'
    _globals['_CREATETEAMFOLDERRESPONSE'].fields_by_name['fileid']._loaded_options = None
    _globals['_CREATETEAMFOLDERRESPONSE'].fields_by_name['fileid']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_TMRMIGRATEREQUEST'].fields_by_name['host_id']._loaded_options = None
    _globals['_TMRMIGRATEREQUEST'].fields_by_name['host_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.HostId'
    _globals['_TMRMIGRATERESPONSE'].fields_by_name['register_host_response']._loaded_options = None
    _globals['_TMRMIGRATERESPONSE'].fields_by_name['register_host_response']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCFRONTENDDBG']._loaded_options = None
    _globals['_SYNCFRONTENDDBG']._serialized_options = b'\x82\xb2\x19B//metaserver/sync_frontend/debug_service:sync_frontend_dbg_service'
    _globals['_SYNCFRONTENDDBG'].methods_by_name['RegisterHost']._loaded_options = None
    _globals['_SYNCFRONTENDDBG'].methods_by_name['RegisterHost']._serialized_options = b'\x98\xb5\x18\xe0\xd4\x03'
    _globals['_SYNCFRONTENDDBG'].methods_by_name['TreeSnapshot']._loaded_options = None
    _globals['_SYNCFRONTENDDBG'].methods_by_name['TreeSnapshot']._serialized_options = b'\x98\xb5\x18\x90N'
    _globals['_SYNCFRONTENDDBG'].methods_by_name['ApplyRemote']._loaded_options = None
    _globals['_SYNCFRONTENDDBG'].methods_by_name['ApplyRemote']._serialized_options = b'\x98\xb5\x18\x90N'
    _globals['_SYNCFRONTENDDBG'].methods_by_name['ReassignFileIds']._loaded_options = None
    _globals['_SYNCFRONTENDDBG'].methods_by_name['ReassignFileIds']._serialized_options = b'\x98\xb5\x18\x90N'
    _globals['_SYNCFRONTENDDBG'].methods_by_name['ShareFolder']._loaded_options = None
    _globals['_SYNCFRONTENDDBG'].methods_by_name['ShareFolder']._serialized_options = b'\x98\xb5\x18\xa0\x9c\x01'
    _globals['_SYNCFRONTENDDBG'].methods_by_name['ChangePermissions']._loaded_options = None
    _globals['_SYNCFRONTENDDBG'].methods_by_name['ChangePermissions']._serialized_options = b'\x98\xb5\x18\x90N'
    _globals['_SYNCFRONTENDDBG'].methods_by_name['PropagateTraversal']._loaded_options = None
    _globals['_SYNCFRONTENDDBG'].methods_by_name['PropagateTraversal']._serialized_options = b'\x98\xb5\x18\x90N'
    _globals['_SYNCFRONTENDDBG'].methods_by_name['InjectMounts']._loaded_options = None
    _globals['_SYNCFRONTENDDBG'].methods_by_name['InjectMounts']._serialized_options = b'\x98\xb5\x18\x90N'
    _globals['_SYNCFRONTENDDBG'].methods_by_name['Purge']._loaded_options = None
    _globals['_SYNCFRONTENDDBG'].methods_by_name['Purge']._serialized_options = b'\x98\xb5\x18\x90N'
    _globals['_SYNCFRONTENDDBG'].methods_by_name['DriveXOpWorkers']._loaded_options = None
    _globals['_SYNCFRONTENDDBG'].methods_by_name['DriveXOpWorkers']._serialized_options = b'\x98\xb5\x18\x90N'
    _globals['_SYNCFRONTENDDBG'].methods_by_name['HasPendingXOps']._loaded_options = None
    _globals['_SYNCFRONTENDDBG'].methods_by_name['HasPendingXOps']._serialized_options = b'\x98\xb5\x18\x90N'
    _globals['_SYNCFRONTENDDBG'].methods_by_name['CreateCloudDoc']._loaded_options = None
    _globals['_SYNCFRONTENDDBG'].methods_by_name['CreateCloudDoc']._serialized_options = b'\x98\xb5\x18\x90N'
    _globals['_SYNCFRONTENDDBG'].methods_by_name['TmrMigrate']._loaded_options = None
    _globals['_SYNCFRONTENDDBG'].methods_by_name['TmrMigrate']._serialized_options = b'\x98\xb5\x18\xb0\xea\x01'
    _globals['_SYNCFRONTENDDBG'].methods_by_name['CreateNonNestableNamespace']._loaded_options = None
    _globals['_SYNCFRONTENDDBG'].methods_by_name['CreateNonNestableNamespace']._serialized_options = b'\x98\xb5\x18\x90N'
    _globals['_SYNCFRONTENDDBG'].methods_by_name['CreateTeamFolder']._loaded_options = None
    _globals['_SYNCFRONTENDDBG'].methods_by_name['CreateTeamFolder']._serialized_options = b'\x98\xb5\x18\x90N'
    _globals['_REGISTERHOSTREQUEST']._serialized_start = 399
    _globals['_REGISTERHOSTREQUEST']._serialized_end = 692
    _globals['_NEWUSER']._serialized_start = 695
    _globals['_NEWUSER']._serialized_end = 913
    _globals['_NEWUSER_TEAMTYPE']._serialized_start = 863
    _globals['_NEWUSER_TEAMTYPE']._serialized_end = 899
    _globals['_REGISTERHOSTRESPONSE']._serialized_start = 916
    _globals['_REGISTERHOSTRESPONSE']._serialized_end = 1476
    _globals['_TREESNAPSHOTREQUEST']._serialized_start = 1479
    _globals['_TREESNAPSHOTREQUEST']._serialized_end = 1670
    _globals['_TREESNAPSHOTRESPONSE']._serialized_start = 1673
    _globals['_TREESNAPSHOTRESPONSE']._serialized_end = 2008
    _globals['_TREESNAPSHOTRESPONSE_MOUNTROOTFILEID']._serialized_start = 1884
    _globals['_TREESNAPSHOTRESPONSE_MOUNTROOTFILEID']._serialized_end = 2008
    _globals['_APPLYREMOTEREQUEST']._serialized_start = 2010
    _globals['_APPLYREMOTEREQUEST']._serialized_end = 2127
    _globals['_APPLYREMOTERESPONSE']._serialized_start = 2129
    _globals['_APPLYREMOTERESPONSE']._serialized_end = 2179
    _globals['_REASSIGNFILEIDSREQUEST']._serialized_start = 2181
    _globals['_REASSIGNFILEIDSREQUEST']._serialized_end = 2267
    _globals['_REASSIGNFILEIDSRESPONSE']._serialized_start = 2269
    _globals['_REASSIGNFILEIDSRESPONSE']._serialized_end = 2354
    _globals['_SHAREFOLDERREQUEST']._serialized_start = 2357
    _globals['_SHAREFOLDERREQUEST']._serialized_end = 2541
    _globals['_SHAREFOLDERRESPONSE']._serialized_start = 2543
    _globals['_SHAREFOLDERRESPONSE']._serialized_end = 2640
    _globals['_SHAREFOLDERSUCCESSRESPONSE']._serialized_start = 2643
    _globals['_SHAREFOLDERSUCCESSRESPONSE']._serialized_end = 2774
    _globals['_CHANGEPERMISSIONSREQUEST']._serialized_start = 2777
    _globals['_CHANGEPERMISSIONSREQUEST']._serialized_end = 3060
    _globals['_CHANGEPERMISSIONSREQUEST_ACCESS']._serialized_start = 2989
    _globals['_CHANGEPERMISSIONSREQUEST_ACCESS']._serialized_end = 3060
    _globals['_CHANGEPERMISSIONSRESPONSE']._serialized_start = 3062
    _globals['_CHANGEPERMISSIONSRESPONSE']._serialized_end = 3089
    _globals['_PROPAGATETRAVERSALREQUEST']._serialized_start = 3091
    _globals['_PROPAGATETRAVERSALREQUEST']._serialized_end = 3212
    _globals['_PROPAGATETRAVERSALRESPONSE']._serialized_start = 3214
    _globals['_PROPAGATETRAVERSALRESPONSE']._serialized_end = 3291
    _globals['_INJECTMOUNTSREQUEST']._serialized_start = 3293
    _globals['_INJECTMOUNTSREQUEST']._serialized_end = 3314
    _globals['_INJECTMOUNTSRESPONSE']._serialized_start = 3316
    _globals['_INJECTMOUNTSRESPONSE']._serialized_end = 3338
    _globals['_PURGEREQUEST']._serialized_start = 3340
    _globals['_PURGEREQUEST']._serialized_end = 3451
    _globals['_PURGERESPONSE']._serialized_start = 3453
    _globals['_PURGERESPONSE']._serialized_end = 3468
    _globals['_DRIVEXOPWORKERSREQUEST']._serialized_start = 3470
    _globals['_DRIVEXOPWORKERSREQUEST']._serialized_end = 3494
    _globals['_DRIVEXOPWORKERSRESPONSE']._serialized_start = 3496
    _globals['_DRIVEXOPWORKERSRESPONSE']._serialized_end = 3546
    _globals['_HASPENDINGXOPSREQUEST']._serialized_start = 3548
    _globals['_HASPENDINGXOPSREQUEST']._serialized_end = 3571
    _globals['_HASPENDINGXOPSRESPONSE']._serialized_start = 3573
    _globals['_HASPENDINGXOPSRESPONSE']._serialized_end = 3622
    _globals['_CREATECLOUDDOCREQUEST']._serialized_start = 3625
    _globals['_CREATECLOUDDOCREQUEST']._serialized_end = 3767
    _globals['_CREATECLOUDDOCRESPONSE']._serialized_start = 3769
    _globals['_CREATECLOUDDOCRESPONSE']._serialized_end = 3811
    _globals['_CREATENONNESTABLENAMESPACEREQUEST']._serialized_start = 3813
    _globals['_CREATENONNESTABLENAMESPACEREQUEST']._serialized_end = 3915
    _globals['_CREATENONNESTABLENAMESPACERESPONSE']._serialized_start = 3917
    _globals['_CREATENONNESTABLENAMESPACERESPONSE']._serialized_end = 4001
    _globals['_CREATETEAMFOLDERREQUEST']._serialized_start = 4003
    _globals['_CREATETEAMFOLDERREQUEST']._serialized_end = 4095
    _globals['_CREATETEAMFOLDERRESPONSE']._serialized_start = 4097
    _globals['_CREATETEAMFOLDERRESPONSE']._serialized_end = 4171
    _globals['_TMRMIGRATEREQUEST']._serialized_start = 4174
    _globals['_TMRMIGRATEREQUEST']._serialized_end = 4353
    _globals['_TMRMIGRATERESPONSE']._serialized_start = 4355
    _globals['_TMRMIGRATERESPONSE']._serialized_end = 4454
    _globals['_SYNCFRONTENDDBG']._serialized_start = 4457
    _globals['_SYNCFRONTENDDBG']._serialized_end = 6194
    return None
