# Source Generated with Decompyle++
# File: fs_api_service_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/fs_api/fs_api_service.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.nucleus import app_service_pb2 as dropbox_dot_proto_dot_nucleus_dot_app__service__pb2
from dropbox.proto.nucleus import device_anchor_pb2 as dropbox_dot_proto_dot_nucleus_dot_device__anchor__pb2
from dropbox.proto.nucleus import feature_configs_pb2 as dropbox_dot_proto_dot_nucleus_dot_feature__configs__pb2
from dropbox.proto.nucleus import published_event_pb2 as dropbox_dot_proto_dot_nucleus_dot_published__event__pb2
from dropbox.proto.nucleus import sync_engine_pb2 as dropbox_dot_proto_dot_nucleus_dot_sync__engine__pb2
from dropbox.proto.nucleus import types_pb2 as dropbox_dot_proto_dot_nucleus_dot_types__pb2
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from dropbox.proto.sync import xattr_pb2 as dropbox_dot_proto_dot_sync_dot_xattr__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)dropbox/proto/fs_api/fs_api_service.proto\x12\x06fs_api\x1a\'dropbox/proto/nucleus/app_service.proto\x1a)dropbox/proto/nucleus/device_anchor.proto\x1a+dropbox/proto/nucleus/feature_configs.proto\x1a+dropbox/proto/nucleus/published_event.proto\x1a\'dropbox/proto/nucleus/sync_engine.proto\x1a!dropbox/proto/nucleus/types.proto\x1a#dropbox/proto/rust/extensions.proto\x1a\x1edropbox/proto/sync/xattr.proto\x1a\x1bgoogle/protobuf/empty.proto"J\n\x16TemporaryDirectoryArgs\x12\x0e\n\x04path\x18\x01 \x01(\tH\x00\x12\x14\n\nuse_domain\x18\x02 \x01(\x08H\x00B\n\n\x08location"\xc1\x04\n\x0fFsApiCreateArgs\x12\x15\n\rdbx_root_path\x18\x01 \x01(\t\x120\n\x07account\x18\x02 \x01(\x0b2\x1f.fs_api.FsApiCreateArgs.Account\x12\x1c\n\x14use_hql_event_logger\x18\x03 \x01(\x08\x12\x17\n\x0fuse_cloud_files\x18\x04 \x01(\x08\x12:\n\x11localized_strings\x18\x05 \x01(\x0b2\x19.nucleus.LocalizedStringsB\x04\xc0\xb5\x18\x00\x12\x1c\n\x14sync_engine_build_no\x18\x06 \x01(\t\x12\x19\n\x11client_session_id\x18\x07 \x01(\t\x12@\n\x18temporary_directory_args\x18\x08 \x01(\x0b2\x1e.fs_api.TemporaryDirectoryArgs\x12C\n\x16server_feature_configs\x18\t \x01(\x0b2\x1d.nucleus.ServerFeatureConfigsB\x04\xc0\xb5\x18\x00\x12.\n&set_dataless_file_iopolicy_on_platform\x18\n \x01(\x08\x12,\n\x0bbackup_mode\x18\x0b \x01(\x0b2\x17.nucleus.BackupModeArgs\x1aT\n\x07Account\x12\x0f\n\x07host_id\x18\x01 \x01(\x04\x12\x0f\n\x07user_id\x18\x02 \x01(\x03\x12\x16\n\x0epaired_user_id\x18\x03 \x01(\x03\x12\x0f\n\x07team_id\x18\x04 \x01(\x03"R\n\x13CreateTempVolumeReq\x12-\n\x0bfile_system\x18\x01 \x01(\x0e2\x12.fs_api.FilesystemB\x04\xc0\xb5\x18\x00\x12\x0c\n\x04size\x18\x02 \x01(\x04"\x80\x01\n\nTempVolume\x12\x13\n\x0bvolume_name\x18\x01 \x01(\t\x12\'\n\x0bfile_system\x18\x02 \x01(\x0e2\x12.fs_api.Filesystem\x12\x0c\n\x04uuid\x18\x03 \x01(\t\x12&\n\nmount_path\x18\x04 \x01(\x0b2\x12.nucleus.LocalPath"c\n\x15CreateTempVolumeReply\x12)\n\x0btemp_volume\x18\x01 \x01(\x0b2\x12.fs_api.TempVolumeH\x00\x12\x0f\n\x05error\x18\x02 \x01(\tH\x00B\x0e\n\x06result\x12\x04\x88\xb5\x18\x00"A\n\x11DropTempVolumeReq\x12,\n\nmount_path\x18\x01 \x01(\x0b2\x12.nucleus.LocalPathB\x04\xc0\xb5\x18\x00"[\n\x13DropTempVolumeReply\x12)\n\x07succeed\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12\x0f\n\x05error\x18\x02 \x01(\tH\x00B\x08\n\x06result"\xe0\x01\n\x18RenameIntoDropboxRequest\x125\n\x16destination_dir_fileid\x18\x01 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00\x12\x1f\n\x17destination_dir_rr_path\x18\x02 \x01(\t\x12\x1c\n\x14destination_filename\x18\x03 \x01(\t\x12"\n\x1asource_local_absolute_path\x18\x04 \x01(\t\x12*\n\x06xattrs\x18\x05 \x03(\x0b2\x1a.sync.RawExtendedAttribute"\x0c\n\nExampleReq"\x0e\n\x0cExampleReply*P\n\nFilesystem\x12\x0e\n\nINVALID_FS\x10\x00\x12\r\n\tOsDefault\x10\x01\x12\t\n\x05FAT32\x10\x02\x12\t\n\x05ExFAT\x10\x03\x12\x07\n\x03UDF\x10\x04\x1a\x04\x90\xb5\x18\x01*&\n\x04Size\x12\x10\n\x0cUNKNOWN_SIZE\x10\x00\x12\x06\n\x02MB\x10\x01\x1a\x04\x90\xb5\x18\x012\xa8\n\n\x05FsApi\x125\n\x07Example\x12\x12.fs_api.ExampleReq\x1a\x14.fs_api.ExampleReply"\x00\x12O\n\x0fGetOSFolderPath\x12\x1b.nucleus.GetOSFolderPathReq\x1a\x1d.nucleus.GetOSFolderPathReply"\x00\x12U\n\x11CreateBreadcrumbs\x12\x1d.nucleus.CreateBreadcrumbsReq\x1a\x1f.nucleus.CreateBreadcrumbsReply"\x00\x12U\n\x11RemoveBreadcrumbs\x12\x1d.nucleus.RemoveBreadcrumbsReq\x1a\x1f.nucleus.RemoveBreadcrumbsReply"\x00\x12L\n\x0eDenyUserAccess\x12\x1a.nucleus.DenyUserAccessReq\x1a\x1c.nucleus.DenyUserAccessReply"\x00\x12O\n\x0fAllowUserAccess\x12\x1b.nucleus.AllowUserAccessReq\x1a\x1d.nucleus.AllowUserAccessReply"\x00\x12O\n\x0fBindIntoDropbox\x12\x1b.nucleus.BindIntoDropboxReq\x1a\x1d.nucleus.BindIntoDropboxReply"\x00\x12U\n\x11UnbindFromDropbox\x12\x1d.nucleus.UnbindFromDropboxReq\x1a\x1f.nucleus.UnbindFromDropboxReply"\x00\x12X\n\x12UnmergeFromDropbox\x12\x1e.nucleus.UnmergeFromDropboxReq\x1a .nucleus.UnmergeFromDropboxReply"\x00\x12R\n\x10MergeIntoDropbox\x12\x1c.nucleus.MergeIntoDropboxReq\x1a\x1e.nucleus.MergeIntoDropboxReply"\x00\x12X\n\x16CreateEphemeralTempDir\x12\x16.google.protobuf.Empty\x1a$.nucleus.CreateEphemeralTempDirReply"\x00\x12O\n\x11RenameIntoDropbox\x12 .fs_api.RenameIntoDropboxRequest\x1a\x16.google.protobuf.Empty"\x00\x12Q\n\x12GetPublishedEvents\x12\x1e.nucleus.GetPublishedEventsReq\x1a\x17.nucleus.PublishedEvent"\x000\x01\x12X\n\x12DeleteDeviceAnchor\x12\x1e.nucleus.DeleteDeviceAnchorReq\x1a .nucleus.DeleteDeviceAnchorReply"\x00\x12P\n\x10CreateTempVolume\x12\x1b.fs_api.CreateTempVolumeReq\x1a\x1d.fs_api.CreateTempVolumeReply"\x00\x12J\n\x0eDropTempVolume\x12\x19.fs_api.DropTempVolumeReq\x1a\x1b.fs_api.DropTempVolumeReply"\x00B\x12\x90\x01\x01\xa2\x02\x0cFsApiServiceb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.fs_api.fs_api_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\x90\x01\x01\xa2\x02\x0cFsApiService'
    _globals['_FILESYSTEM']._loaded_options = None
    _globals['_FILESYSTEM']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_SIZE']._loaded_options = None
    _globals['_SIZE']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_FSAPICREATEARGS'].fields_by_name['localized_strings']._loaded_options = None
    _globals['_FSAPICREATEARGS'].fields_by_name['localized_strings']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_FSAPICREATEARGS'].fields_by_name['server_feature_configs']._loaded_options = None
    _globals['_FSAPICREATEARGS'].fields_by_name['server_feature_configs']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_CREATETEMPVOLUMEREQ'].fields_by_name['file_system']._loaded_options = None
    _globals['_CREATETEMPVOLUMEREQ'].fields_by_name['file_system']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_CREATETEMPVOLUMEREPLY'].oneofs_by_name['result']._loaded_options = None
    _globals['_CREATETEMPVOLUMEREPLY'].oneofs_by_name['result']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_DROPTEMPVOLUMEREQ'].fields_by_name['mount_path']._loaded_options = None
    _globals['_DROPTEMPVOLUMEREQ'].fields_by_name['mount_path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_RENAMEINTODROPBOXREQUEST'].fields_by_name['destination_dir_fileid']._loaded_options = None
    _globals['_RENAMEINTODROPBOXREQUEST'].fields_by_name['destination_dir_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_FILESYSTEM']._serialized_start = 1790
    _globals['_FILESYSTEM']._serialized_end = 1870
    _globals['_SIZE']._serialized_start = 1872
    _globals['_SIZE']._serialized_end = 1910
    _globals['_TEMPORARYDIRECTORYARGS']._serialized_start = 401
    _globals['_TEMPORARYDIRECTORYARGS']._serialized_end = 475
    _globals['_FSAPICREATEARGS']._serialized_start = 478
    _globals['_FSAPICREATEARGS']._serialized_end = 1055
    _globals['_FSAPICREATEARGS_ACCOUNT']._serialized_start = 971
    _globals['_FSAPICREATEARGS_ACCOUNT']._serialized_end = 1055
    _globals['_CREATETEMPVOLUMEREQ']._serialized_start = 1057
    _globals['_CREATETEMPVOLUMEREQ']._serialized_end = 1139
    _globals['_TEMPVOLUME']._serialized_start = 1142
    _globals['_TEMPVOLUME']._serialized_end = 1270
    _globals['_CREATETEMPVOLUMEREPLY']._serialized_start = 1272
    _globals['_CREATETEMPVOLUMEREPLY']._serialized_end = 1371
    _globals['_DROPTEMPVOLUMEREQ']._serialized_start = 1373
    _globals['_DROPTEMPVOLUMEREQ']._serialized_end = 1438
    _globals['_DROPTEMPVOLUMEREPLY']._serialized_start = 1440
    _globals['_DROPTEMPVOLUMEREPLY']._serialized_end = 1531
    _globals['_RENAMEINTODROPBOXREQUEST']._serialized_start = 1534
    _globals['_RENAMEINTODROPBOXREQUEST']._serialized_end = 1758
    _globals['_EXAMPLEREQ']._serialized_start = 1760
    _globals['_EXAMPLEREQ']._serialized_end = 1772
    _globals['_EXAMPLEREPLY']._serialized_start = 1774
    _globals['_EXAMPLEREPLY']._serialized_end = 1788
    _globals['_FSAPI']._serialized_start = 1913
    _globals['_FSAPI']._serialized_end = 3233
_builder.BuildServices(DESCRIPTOR, 'dropbox.proto.fs_api.fs_api_service_pb2', _globals)
