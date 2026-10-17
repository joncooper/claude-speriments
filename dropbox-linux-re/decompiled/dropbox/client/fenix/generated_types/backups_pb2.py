# Source Generated with Decompyle++
# File: backups_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'backups.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.nucleus import types_pb2 as dropbox_dot_proto_dot_nucleus_dot_types__pb2
from dropbox.proto.nucleus import reactive_api_pb2 as dropbox_dot_proto_dot_nucleus_dot_reactive__api__pb2
from  import shared_pb2 as shared__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbackups.proto\x12\x13dropbox.meta_engine\x1a!dropbox/proto/nucleus/types.proto\x1a(dropbox/proto/nucleus/reactive_api.proto\x1a\x0cshared.proto"n\n\x16ListComputerBackupsReq\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x17\n\x0finclude_last_ts\x18\x03 \x01(\x08\x12\x13\n\x0bremote_only\x18\x04 \x01(\x08"e\n\x18ListComputerBackupsReply\x128\n\x07backups\x18\x01 \x03(\x0b2\'.dropbox.meta_engine.DeviceBackupRecord\x12\x0f\n\x07success\x18\x02 \x01(\x08"s\n\x1bListExternalDriveBackupsReq\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x17\n\x0finclude_last_ts\x18\x03 \x01(\x08\x12\x13\n\x0bremote_only\x18\x04 \x01(\x08"q\n\x1dListExternalDriveBackupsReply\x12?\n\x07backups\x18\x01 \x03(\x0b2..dropbox.meta_engine.ExternalDriveBackupRecord\x12\x0f\n\x07success\x18\x02 \x01(\x08"\xbe\x03\n\x12DeviceBackupRecord\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x123\n\x08platform\x18\x03 \x01(\x0e2!.dropbox.meta_engine.PlatformType\x12\x0f\n\x07folders\x18\x04 \x03(\t\x121\n\x06status\x18\x05 \x01(\x0e2!.dropbox.meta_engine.BackupStatus\x12\x14\n\x0cquota_exempt\x18\x06 \x01(\x08\x12\x11\n\tis_remote\x18\x07 \x01(\x08\x12\x1c\n\x14has_migration_status\x18\x08 \x01(\x08\x129\n\x0eanchor_folders\x18\t \x03(\x0b2!.dropbox.meta_engine.AnchorFolder\x12.\n\x04role\x18\n \x01(\x0e2 .dropbox.meta_engine.AccountRole\x12$\n\x0broot_fileid\x18\x0b \x01(\x0b2\x0f.nucleus.FileId\x12\x19\n\x11last_backed_up_ms\x18\x0c \x01(\x03\x12\x0c\n\x04path\x18\r \x01(\t\x12\x14\n\x0cdisplay_name\x18\x0e \x01(\t"\xe0\x03\n\x19ExternalDriveBackupRecord\x12\n\n\x02id\x18\x01 \x01(\t\x12&\n\ranchor_fileid\x18\x02 \x01(\x0b2\x0f.nucleus.FileId\x12\x12\n\ndrive_uuid\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x121\n\x06status\x18\x05 \x01(\x0e2!.dropbox.meta_engine.BackupStatus\x12\x14\n\x0cquota_exempt\x18\x06 \x01(\x08\x12\x11\n\tis_remote\x18\x07 \x01(\x08\x12\x15\n\ris_plugged_in\x18\x08 \x01(\x08\x12.\n\x04role\x18\t \x01(\x0e2 .dropbox.meta_engine.AccountRole\x12\x19\n\x11last_backed_up_ms\x18\n \x01(\x03\x12\x19\n\x11creation_time_utc\x18\x0b \x01(\x03\x12\x0c\n\x04path\x18\x0c \x01(\t\x12\x0f\n\x07fq_path\x18\r \x01(\t\x12\x14\n\x0cis_migrating\x18\x0e \x01(\x08\x12\x1d\n\x15is_in_basic_migration\x18\x0f \x01(\x08\x12\x12\n\nis_fission\x18\x10 \x01(\x08\x12\x14\n\x0cdisplay_name\x18\x11 \x01(\t\x12\x16\n\x0eis_large_drive\x18\x12 \x01(\x08*\x82\x01\n\x0cBackupStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bNOT_ENABLED\x10\x01\x12\x0f\n\x0bIN_PROGRESS\x10\x02\x12\x08\n\x04DONE\x10\x03\x12\n\n\x06PAUSED\x10\x04\x12\t\n\x05ERROR\x10\x05\x12\r\n\tOVERQUOTA\x10\x06\x12\x13\n\x0fSERVER_DISABLED\x10\x07*0\n\x0cPlatformType\x12\x0e\n\nUNKNOWN_OS\x10\x00\x12\x07\n\x03MAC\x10\x01\x12\x07\n\x03WIN\x10\x022\xd8\x02\n\x10BackupServiceApi\x12q\n\x13ListComputerBackups\x12+.dropbox.meta_engine.ListComputerBackupsReq\x1a-.dropbox.meta_engine.ListComputerBackupsReply\x12\x80\x01\n\x18ListExternalDriveBackups\x120.dropbox.meta_engine.ListExternalDriveBackupsReq\x1a2.dropbox.meta_engine.ListExternalDriveBackupsReply\x12N\n\x18GetBackupPublishedEvents\x12\x18.nucleus.ReactiveRequest\x1a\x16.nucleus.ReactiveEvent0\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'backups_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_BACKUPSTATUS']._serialized_start = 1509
    _globals['_BACKUPSTATUS']._serialized_end = 1639
    _globals['_PLATFORMTYPE']._serialized_start = 1641
    _globals['_PLATFORMTYPE']._serialized_end = 1689
    _globals['_LISTCOMPUTERBACKUPSREQ']._serialized_start = 129
    _globals['_LISTCOMPUTERBACKUPSREQ']._serialized_end = 239
    _globals['_LISTCOMPUTERBACKUPSREPLY']._serialized_start = 241
    _globals['_LISTCOMPUTERBACKUPSREPLY']._serialized_end = 342
    _globals['_LISTEXTERNALDRIVEBACKUPSREQ']._serialized_start = 344
    _globals['_LISTEXTERNALDRIVEBACKUPSREQ']._serialized_end = 459
    _globals['_LISTEXTERNALDRIVEBACKUPSREPLY']._serialized_start = 461
    _globals['_LISTEXTERNALDRIVEBACKUPSREPLY']._serialized_end = 574
    _globals['_DEVICEBACKUPRECORD']._serialized_start = 577
    _globals['_DEVICEBACKUPRECORD']._serialized_end = 1023
    _globals['_EXTERNALDRIVEBACKUPRECORD']._serialized_start = 1026
    _globals['_EXTERNALDRIVEBACKUPRECORD']._serialized_end = 1506
    _globals['_BACKUPSERVICEAPI']._serialized_start = 1692
    _globals['_BACKUPSERVICEAPI']._serialized_end = 2036
    return None
