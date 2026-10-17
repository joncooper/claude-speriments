# Source Generated with Decompyle++
# File: device_anchor_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/nucleus/device_anchor.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.nucleus import dbxignore_pb2 as dropbox_dot_proto_dot_nucleus_dot_dbxignore__pb2
from dropbox.proto.nucleus import types_pb2 as dropbox_dot_proto_dot_nucleus_dot_types__pb2
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from dropbox.proto.on_disk import device_anchor_pb2 as dropbox_dot_proto_dot_on__disk_dot_device__anchor__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)dropbox/proto/nucleus/device_anchor.proto\x12\x07nucleus\x1a%dropbox/proto/nucleus/dbxignore.proto\x1a!dropbox/proto/nucleus/types.proto\x1a#dropbox/proto/rust/extensions.proto\x1a)dropbox/proto/on_disk/device_anchor.proto\x1a\x1bgoogle/protobuf/empty.proto"\x96\x01\n\x0eTargetMetadata\x12)\n\x0btarget_path\x18\x01 \x01(\x0b2\x12.nucleus.LocalPathH\x00\x12\x15\n\x0bdevice_uuid\x18\x02 \x01(\tH\x00\x120\n\x12backup_folder_path\x18\x03 \x01(\x0b2\x12.nucleus.LocalPathH\x00B\x10\n\x08metadata\x12\x04\x88\xb5\x18\x00"\xa4\x05\n\x10DeviceAnchorInfo\x12-\n\x14device_anchor_fileid\x18\x01 \x01(\x0b2\x0f.nucleus.FileId\x124\n\x12device_anchor_path\x18\x02 \x01(\x0b2\x12.nucleus.LocalPathB\x04\xc0\xb5\x18\x00\x126\n\x0ftarget_metadata\x18\x03 \x01(\x0b2\x17.nucleus.TargetMetadataB\x04\xc0\xb5\x18\x00\x12\'\n\x0btarget_path\x18\x04 \x01(\x0b2\x12.nucleus.LocalPath\x12)\n\x05state\x18\x05 \x01(\x0e2\x1a.nucleus.DeviceAnchorState\x122\n\x10no_observed_hang\x18\x06 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x125\n\x04hang\x18\x07 \x01(\x0b2%.nucleus.DeviceAnchorInfo.HangDetailsH\x00\x12C\n\x12device_anchor_hang\x18\x08 \x01(\x0b2%.nucleus.DeviceAnchorInfo.HangDetailsH\x00\x12E\n\x19device_verification_attrs\x18\t \x01(\x0b2".on_disk.DeviceIdVerificationAttrs\x1a\x93\x01\n\x0bHangDetails\x12\x10\n\x08resolver\x18\x01 \x01(\x08\x12\x11\n\treindexer\x18\x02 \x01(\x08\x12\x17\n\x0fremote_frontier\x18\x03 \x01(\x08\x12\x16\n\x0elocal_frontier\x18\x04 \x01(\x08\x12\x12\n\nover_quota\x18\x05 \x01(\x08\x12\x1a\n\x12file_event_manager\x18\x06 \x01(\x08B\x12\n\nhang_state\x12\x04\x88\xb5\x18\x00"\xd9\x03\n\x15CreateDeviceAnchorReq\x124\n\x12device_anchor_path\x18\x01 \x01(\x0b2\x12.nucleus.LocalPathB\x04\xc0\xb5\x18\x00\x124\n\x16legacy_edb_target_path\x18\x02 \x01(\x0b2\x12.nucleus.LocalPathH\x00\x12\x15\n\x0bdevice_uuid\x18\x03 \x01(\tH\x00\x120\n\x12backup_folder_path\x18\x07 \x01(\x0b2\x12.nucleus.LocalPathH\x00\x12-\n\tdbxignore\x18\x04 \x01(\x0b2\x1a.nucleus.DBXIgnoreContents\x12\x17\n\x0fdevice_capacity\x18\x05 \x01(\x04\x121\n\x18existing_location_fileid\x18\x06 \x01(\x0b2\x0f.nucleus.FileId\x128\n\x1fexisting_location_parent_fileid\x18\n \x01(\x0b2\x0f.nucleus.FileId\x12+\n#allow_unsafe_skip_validation_checks\x18\x08 \x01(\x08\x12\x14\n\x0cstart_paused\x18\t \x01(\x08B\x13\n\x0btarget_args\x12\x04\x88\xb5\x18\x00"\x8f\x01\n\x17CreateDeviceAnchorReply\x127\n\x12device_anchor_info\x18\x01 \x01(\x0b2\x19.nucleus.DeviceAnchorInfoH\x00\x12+\n\x05error\x18\x02 \x01(\x0e2\x1a.nucleus.DeviceAnchorErrorH\x00B\x0e\n\x06result\x12\x04\x88\xb5\x18\x00"M\n\x16ResolveDeviceAnchorReq\x123\n\x14device_anchor_fileid\x18\x01 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00"\x90\x01\n\x18ResolveDeviceAnchorReply\x127\n\x12device_anchor_info\x18\x01 \x01(\x0b2\x19.nucleus.DeviceAnchorInfoH\x00\x12+\n\x05error\x18\x02 \x01(\x0e2\x1a.nucleus.DeviceAnchorErrorH\x00B\x0e\n\x06result\x12\x04\x88\xb5\x18\x00"K\n\x1aBreakBackupByTargetPathReq\x12-\n\x0btarget_path\x18\x01 \x01(\x0b2\x12.nucleus.LocalPathB\x04\xc0\xb5\x18\x00"\x86\x01\n\x1cBreakBackupByTargetPathReply\x12)\n\x07success\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12+\n\x05error\x18\x02 \x01(\x0e2\x1a.nucleus.DeviceAnchorErrorH\x00B\x0e\n\x06result\x12\x04\x88\xb5\x18\x00"\x7f\n\x16BreakBackupByFileIdReq\x123\n\x14device_anchor_fileid\x18\x01 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00\x120\n\x0cbreak_reason\x18\x02 \x01(\x0e2\x1a.nucleus.BreakBackupReason"\x82\x01\n\x18BreakBackupByFileIdReply\x12)\n\x07success\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12+\n\x05error\x18\x02 \x01(\x0e2\x1a.nucleus.DeviceAnchorErrorH\x00B\x0e\n\x06result\x12\x04\x88\xb5\x18\x00"L\n\x15ResumeDeviceAnchorReq\x123\n\x14device_anchor_fileid\x18\x01 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00"\x81\x01\n\x17ResumeDeviceAnchorReply\x12)\n\x07success\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12+\n\x05error\x18\x02 \x01(\x0e2\x1a.nucleus.DeviceAnchorErrorH\x00B\x0e\n\x06result\x12\x04\x88\xb5\x18\x00"s\n\x14PauseDeviceAnchorReq\x123\n\x14device_anchor_fileid\x18\x01 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00\x12&\n\x1eupdated_device_anchor_capacity\x18\x02 \x01(\x04"\x80\x01\n\x16PauseDeviceAnchorReply\x12)\n\x07success\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12+\n\x05error\x18\x02 \x01(\x0e2\x1a.nucleus.DeviceAnchorErrorH\x00B\x0e\n\x06result\x12\x04\x88\xb5\x18\x00"\xb2\x01\n\x15DeleteDeviceAnchorReq\x123\n\x14device_anchor_fileid\x18\x01 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00\x12.\n\x12device_anchor_path\x18\x02 \x01(\x0b2\x12.nucleus.LocalPath\x124\n\x0btarget_type\x18\x03 \x01(\x0e2\x1f.nucleus.DeviceAnchorTargetType"\x81\x01\n\x17DeleteDeviceAnchorReply\x12)\n\x07success\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12+\n\x05error\x18\x02 \x01(\x0e2\x1a.nucleus.DeviceAnchorErrorH\x00B\x0e\n\x06result\x12\x04\x88\xb5\x18\x00"`\n\x14ListDeviceAnchorsReq\x12\x12\n\nvalid_only\x18\x01 \x01(\x08\x124\n\x0btarget_type\x18\x02 \x01(\x0e2\x1f.nucleus.DeviceAnchorTargetType"\x9f\x02\n\x16ListDeviceAnchorResult\x121\n\x0edevice_anchors\x18\x01 \x03(\x0b2\x19.nucleus.DeviceAnchorInfo\x12A\n\x06errors\x18\x02 \x03(\x0b21.nucleus.ListDeviceAnchorResult.FileIdTaggedError\x1a\x8e\x01\n\x11FileIdTaggedError\x12 \n\x07file_id\x18\x01 \x01(\x0b2\x0f.nucleus.FileId\x12&\n\x04path\x18\x02 \x01(\x0b2\x12.nucleus.LocalPathB\x04\xc0\xb5\x18\x00\x12/\n\x05error\x18\x03 \x01(\x0e2\x1a.nucleus.DeviceAnchorErrorB\x04\xc0\xb5\x18\x00"\x89\x01\n\x16ListDeviceAnchorsReply\x122\n\x07success\x18\x01 \x01(\x0b2\x1f.nucleus.ListDeviceAnchorResultH\x00\x12+\n\x05error\x18\x02 \x01(\x0e2\x1a.nucleus.DeviceAnchorErrorH\x00B\x0e\n\x06result\x12\x04\x88\xb5\x18\x00"N\n\x17GetDbxIgnoreContentsReq\x123\n\x14device_anchor_fileid\x18\x01 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00"\xcf\x01\n\x19GetDbxIgnoreContentsReply\x12E\n\x15dbxignore_and_version\x18\x01 \x01(\x0b2$.nucleus.DBXIgnoreContentsAndVersionH\x00\x12+\n\x05error\x18\x02 \x01(\x0e2\x1a.nucleus.DeviceAnchorErrorH\x00\x12.\n\x0cno_dbxignore\x18\x03 \x01(\x0b2\x16.google.protobuf.EmptyH\x00B\x0e\n\x06result\x12\x04\x88\xb5\x18\x00"\x83\x01\n\x17SetDbxIgnoreContentsReq\x123\n\x14device_anchor_fileid\x18\x01 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00\x123\n\tdbxignore\x18\x02 \x01(\x0b2\x1a.nucleus.DBXIgnoreContentsB\x04\xc0\xb5\x18\x00"\x83\x01\n\x19SetDbxIgnoreContentsReply\x12)\n\x07success\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12+\n\x05error\x18\x02 \x01(\x0e2\x1a.nucleus.DeviceAnchorErrorH\x00B\x0e\n\x06result\x12\x04\x88\xb5\x18\x00"p\n\x17ValidateAnchorTargetReq\x12)\n\x0btarget_path\x18\x01 \x01(\x0b2\x12.nucleus.LocalPathH\x00\x12\x15\n\x0bdevice_uuid\x18\x02 \x01(\tH\x00B\x13\n\x0btarget_args\x12\x04\x88\xb5\x18\x00"\x84\x01\n\x19ValidateAnchorTargetReply\x12*\n\x08eligible\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12+\n\x05error\x18\x02 \x01(\x0e2\x1a.nucleus.DeviceAnchorErrorH\x00B\x0e\n\x06result\x12\x04\x88\xb5\x18\x00"J\n GetDeviceAnchorMetadataByPathReq\x12&\n\x04path\x18\x01 \x01(\x0b2\x12.nucleus.LocalPathB\x04\xc0\xb5\x18\x00"\x96\x01\n#GetDeviceAnchorMetadataByPathResult\x12)\n\x08metadata\x18\x01 \x01(\x0b2\x17.nucleus.TargetMetadata\x12&\n\ranchor_fileid\x18\x02 \x01(\x0b2\x0f.nucleus.FileId\x12\x1c\n\x14was_anchor_in_canopy\x18\x03 \x01(\x08"\x9c\x01\n"GetDeviceAnchorMetadataByPathReply\x12?\n\x07success\x18\x01 \x01(\x0b2,.nucleus.GetDeviceAnchorMetadataByPathResultH\x00\x12+\n\x05error\x18\x02 \x01(\x0e2\x1a.nucleus.DeviceAnchorErrorH\x00B\x08\n\x06result*\xac\x01\n\x11DeviceAnchorState\x12\x1f\n\x1bINVALID_DEVICE_ANCHOR_STATE\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x11\n\rBACKUP_PAUSED\x10\x02\x12\n\n\x06BROKEN\x10\x03\x12\r\n\tUNPLUGGED\x10\x04\x12\x16\n\x12PERMANENTLY_FAILED\x10\x05\x12\x1e\n\x1aDEVICE_ANCHOR_STATES_COUNT\x10\x06\x1a\x04\x90\xb5\x18\x01*\xcf\x03\n\x11DeviceAnchorError\x12\x1f\n\x1bUNKNOWN_DEVICE_ANCHOR_ERROR\x10\x00\x12 \n\x1cDEVICE_ANCHOR_ALREADY_EXISTS\x10\x01\x12\x1e\n\x1aDEVICE_ANCHOR_PATH_INVALID\x10\x02\x12\x1a\n\x16TARGET_NOT_A_DIRECTORY\x10\x03\x12\x18\n\x14TARGET_ALREADY_BOUND\x10\x04\x12\x17\n\x13NOT_A_DEVICE_ANCHOR\x10\x05\x12\x1b\n\x17DEVICE_ANCHOR_NOT_FOUND\x10\x06\x12\x19\n\x15INVALID_DEVICE_ANCHOR\x10\x07\x12\x1d\n\x19OTHER_DEVICE_ANCHOR_ERROR\x10\x08\x12#\n\x1fTARGET_IS_DESCENDANT_OF_DROPBOX\x10\t\x12\x19\n\x15TARGET_DOES_NOT_EXIST\x10\n\x12\x1a\n\x16TARGET_IS_NOT_WRITABLE\x10\x0b\x12\x0c\n\x08IO_ERROR\x10\x0c\x12\x0c\n\x08NO_SPACE\x10\r\x12\x13\n\x0fDBXIGNORE_ERROR\x10\x0e\x12\x1e\n\x1aDEVICE_ANCHOR_ERRORS_COUNT\x10\x0f\x1a\x04\x90\xb5\x18\x01*l\n\x16DeviceAnchorTargetType\x12"\n\x1eUNSPECIFIED_ANCHOR_TARGET_TYPE\x10\x00\x12\x12\n\x0eEXTERNAL_DRIVE\x10\x01\x12\x1a\n\x16COMPUTER_BACKUP_FOLDER\x10\x02*\xc8\x01\n\x11BreakBackupReason\x12\x1f\n\x1bUNKNOWN_BREAK_BACKUP_REASON\x10\x00\x12\x1d\n\x19FP_PREMIGRATION_REQUESTED\x10\x01\x12(\n$SEAMLESS_FISSION_MIGRATION_REQUESTED\x10\x02\x12\x1a\n\x16CBOA_ABANDONED_ANCHORS\x10\x03\x12\'\n#CBOA_ONE_WAY_SYNC_CONFLICTED_ANCHOR\x10\x04\x1a\x04\x90\xb5\x18\x01B\x0c\xa2\x02\tNucleusSEb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.nucleus.device_anchor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\tNucleusSE'
    _globals['_DEVICEANCHORSTATE']._loaded_options = None
    _globals['_DEVICEANCHORSTATE']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_DEVICEANCHORERROR']._loaded_options = None
    _globals['_DEVICEANCHORERROR']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_BREAKBACKUPREASON']._loaded_options = None
    _globals['_BREAKBACKUPREASON']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_TARGETMETADATA'].oneofs_by_name['metadata']._loaded_options = None
    _globals['_TARGETMETADATA'].oneofs_by_name['metadata']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_DEVICEANCHORINFO'].oneofs_by_name['hang_state']._loaded_options = None
    _globals['_DEVICEANCHORINFO'].oneofs_by_name['hang_state']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_DEVICEANCHORINFO'].fields_by_name['device_anchor_path']._loaded_options = None
    _globals['_DEVICEANCHORINFO'].fields_by_name['device_anchor_path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DEVICEANCHORINFO'].fields_by_name['target_metadata']._loaded_options = None
    _globals['_DEVICEANCHORINFO'].fields_by_name['target_metadata']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_CREATEDEVICEANCHORREQ'].oneofs_by_name['target_args']._loaded_options = None
    _globals['_CREATEDEVICEANCHORREQ'].oneofs_by_name['target_args']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_CREATEDEVICEANCHORREQ'].fields_by_name['device_anchor_path']._loaded_options = None
    _globals['_CREATEDEVICEANCHORREQ'].fields_by_name['device_anchor_path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_CREATEDEVICEANCHORREPLY'].oneofs_by_name['result']._loaded_options = None
    _globals['_CREATEDEVICEANCHORREPLY'].oneofs_by_name['result']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_RESOLVEDEVICEANCHORREQ'].fields_by_name['device_anchor_fileid']._loaded_options = None
    _globals['_RESOLVEDEVICEANCHORREQ'].fields_by_name['device_anchor_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_RESOLVEDEVICEANCHORREPLY'].oneofs_by_name['result']._loaded_options = None
    _globals['_RESOLVEDEVICEANCHORREPLY'].oneofs_by_name['result']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_BREAKBACKUPBYTARGETPATHREQ'].fields_by_name['target_path']._loaded_options = None
    _globals['_BREAKBACKUPBYTARGETPATHREQ'].fields_by_name['target_path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_BREAKBACKUPBYTARGETPATHREPLY'].oneofs_by_name['result']._loaded_options = None
    _globals['_BREAKBACKUPBYTARGETPATHREPLY'].oneofs_by_name['result']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_BREAKBACKUPBYFILEIDREQ'].fields_by_name['device_anchor_fileid']._loaded_options = None
    _globals['_BREAKBACKUPBYFILEIDREQ'].fields_by_name['device_anchor_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_BREAKBACKUPBYFILEIDREPLY'].oneofs_by_name['result']._loaded_options = None
    _globals['_BREAKBACKUPBYFILEIDREPLY'].oneofs_by_name['result']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_RESUMEDEVICEANCHORREQ'].fields_by_name['device_anchor_fileid']._loaded_options = None
    _globals['_RESUMEDEVICEANCHORREQ'].fields_by_name['device_anchor_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_RESUMEDEVICEANCHORREPLY'].oneofs_by_name['result']._loaded_options = None
    _globals['_RESUMEDEVICEANCHORREPLY'].oneofs_by_name['result']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_PAUSEDEVICEANCHORREQ'].fields_by_name['device_anchor_fileid']._loaded_options = None
    _globals['_PAUSEDEVICEANCHORREQ'].fields_by_name['device_anchor_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_PAUSEDEVICEANCHORREPLY'].oneofs_by_name['result']._loaded_options = None
    _globals['_PAUSEDEVICEANCHORREPLY'].oneofs_by_name['result']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_DELETEDEVICEANCHORREQ'].fields_by_name['device_anchor_fileid']._loaded_options = None
    _globals['_DELETEDEVICEANCHORREQ'].fields_by_name['device_anchor_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DELETEDEVICEANCHORREPLY'].oneofs_by_name['result']._loaded_options = None
    _globals['_DELETEDEVICEANCHORREPLY'].oneofs_by_name['result']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_LISTDEVICEANCHORRESULT_FILEIDTAGGEDERROR'].fields_by_name['path']._loaded_options = None
    _globals['_LISTDEVICEANCHORRESULT_FILEIDTAGGEDERROR'].fields_by_name['path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_LISTDEVICEANCHORRESULT_FILEIDTAGGEDERROR'].fields_by_name['error']._loaded_options = None
    _globals['_LISTDEVICEANCHORRESULT_FILEIDTAGGEDERROR'].fields_by_name['error']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_LISTDEVICEANCHORSREPLY'].oneofs_by_name['result']._loaded_options = None
    _globals['_LISTDEVICEANCHORSREPLY'].oneofs_by_name['result']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_GETDBXIGNORECONTENTSREQ'].fields_by_name['device_anchor_fileid']._loaded_options = None
    _globals['_GETDBXIGNORECONTENTSREQ'].fields_by_name['device_anchor_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_GETDBXIGNORECONTENTSREPLY'].oneofs_by_name['result']._loaded_options = None
    _globals['_GETDBXIGNORECONTENTSREPLY'].oneofs_by_name['result']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_SETDBXIGNORECONTENTSREQ'].fields_by_name['device_anchor_fileid']._loaded_options = None
    _globals['_SETDBXIGNORECONTENTSREQ'].fields_by_name['device_anchor_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SETDBXIGNORECONTENTSREQ'].fields_by_name['dbxignore']._loaded_options = None
    _globals['_SETDBXIGNORECONTENTSREQ'].fields_by_name['dbxignore']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SETDBXIGNORECONTENTSREPLY'].oneofs_by_name['result']._loaded_options = None
    _globals['_SETDBXIGNORECONTENTSREPLY'].oneofs_by_name['result']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_VALIDATEANCHORTARGETREQ'].oneofs_by_name['target_args']._loaded_options = None
    _globals['_VALIDATEANCHORTARGETREQ'].oneofs_by_name['target_args']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_VALIDATEANCHORTARGETREPLY'].oneofs_by_name['result']._loaded_options = None
    _globals['_VALIDATEANCHORTARGETREPLY'].oneofs_by_name['result']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_GETDEVICEANCHORMETADATABYPATHREQ'].fields_by_name['path']._loaded_options = None
    _globals['_GETDEVICEANCHORMETADATABYPATHREQ'].fields_by_name['path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DEVICEANCHORSTATE']._serialized_start = 4888
    _globals['_DEVICEANCHORSTATE']._serialized_end = 5060
    _globals['_DEVICEANCHORERROR']._serialized_start = 5063
    _globals['_DEVICEANCHORERROR']._serialized_end = 5526
    _globals['_DEVICEANCHORTARGETTYPE']._serialized_start = 5528
    _globals['_DEVICEANCHORTARGETTYPE']._serialized_end = 5636
    _globals['_BREAKBACKUPREASON']._serialized_start = 5639
    _globals['_BREAKBACKUPREASON']._serialized_end = 5839
    _globals['_TARGETMETADATA']._serialized_start = 238
    _globals['_TARGETMETADATA']._serialized_end = 388
    _globals['_DEVICEANCHORINFO']._serialized_start = 391
    _globals['_DEVICEANCHORINFO']._serialized_end = 1067
    _globals['_DEVICEANCHORINFO_HANGDETAILS']._serialized_start = 900
    _globals['_DEVICEANCHORINFO_HANGDETAILS']._serialized_end = 1047
    _globals['_CREATEDEVICEANCHORREQ']._serialized_start = 1070
    _globals['_CREATEDEVICEANCHORREQ']._serialized_end = 1543
    _globals['_CREATEDEVICEANCHORREPLY']._serialized_start = 1546
    _globals['_CREATEDEVICEANCHORREPLY']._serialized_end = 1689
    _globals['_RESOLVEDEVICEANCHORREQ']._serialized_start = 1691
    _globals['_RESOLVEDEVICEANCHORREQ']._serialized_end = 1768
    _globals['_RESOLVEDEVICEANCHORREPLY']._serialized_start = 1771
    _globals['_RESOLVEDEVICEANCHORREPLY']._serialized_end = 1915
    _globals['_BREAKBACKUPBYTARGETPATHREQ']._serialized_start = 1917
    _globals['_BREAKBACKUPBYTARGETPATHREQ']._serialized_end = 1992
    _globals['_BREAKBACKUPBYTARGETPATHREPLY']._serialized_start = 1995
    _globals['_BREAKBACKUPBYTARGETPATHREPLY']._serialized_end = 2129
    _globals['_BREAKBACKUPBYFILEIDREQ']._serialized_start = 2131
    _globals['_BREAKBACKUPBYFILEIDREQ']._serialized_end = 2258
    _globals['_BREAKBACKUPBYFILEIDREPLY']._serialized_start = 2261
    _globals['_BREAKBACKUPBYFILEIDREPLY']._serialized_end = 2391
    _globals['_RESUMEDEVICEANCHORREQ']._serialized_start = 2393
    _globals['_RESUMEDEVICEANCHORREQ']._serialized_end = 2469
    _globals['_RESUMEDEVICEANCHORREPLY']._serialized_start = 2472
    _globals['_RESUMEDEVICEANCHORREPLY']._serialized_end = 2601
    _globals['_PAUSEDEVICEANCHORREQ']._serialized_start = 2603
    _globals['_PAUSEDEVICEANCHORREQ']._serialized_end = 2718
    _globals['_PAUSEDEVICEANCHORREPLY']._serialized_start = 2721
    _globals['_PAUSEDEVICEANCHORREPLY']._serialized_end = 2849
    _globals['_DELETEDEVICEANCHORREQ']._serialized_start = 2852
    _globals['_DELETEDEVICEANCHORREQ']._serialized_end = 3030
    _globals['_DELETEDEVICEANCHORREPLY']._serialized_start = 3033
    _globals['_DELETEDEVICEANCHORREPLY']._serialized_end = 3162
    _globals['_LISTDEVICEANCHORSREQ']._serialized_start = 3164
    _globals['_LISTDEVICEANCHORSREQ']._serialized_end = 3260
    _globals['_LISTDEVICEANCHORRESULT']._serialized_start = 3263
    _globals['_LISTDEVICEANCHORRESULT']._serialized_end = 3550
    _globals['_LISTDEVICEANCHORRESULT_FILEIDTAGGEDERROR']._serialized_start = 3408
    _globals['_LISTDEVICEANCHORRESULT_FILEIDTAGGEDERROR']._serialized_end = 3550
    _globals['_LISTDEVICEANCHORSREPLY']._serialized_start = 3553
    _globals['_LISTDEVICEANCHORSREPLY']._serialized_end = 3690
    _globals['_GETDBXIGNORECONTENTSREQ']._serialized_start = 3692
    _globals['_GETDBXIGNORECONTENTSREQ']._serialized_end = 3770
    _globals['_GETDBXIGNORECONTENTSREPLY']._serialized_start = 3773
    _globals['_GETDBXIGNORECONTENTSREPLY']._serialized_end = 3980
    _globals['_SETDBXIGNORECONTENTSREQ']._serialized_start = 3983
    _globals['_SETDBXIGNORECONTENTSREQ']._serialized_end = 4114
    _globals['_SETDBXIGNORECONTENTSREPLY']._serialized_start = 4117
    _globals['_SETDBXIGNORECONTENTSREPLY']._serialized_end = 4248
    _globals['_VALIDATEANCHORTARGETREQ']._serialized_start = 4250
    _globals['_VALIDATEANCHORTARGETREQ']._serialized_end = 4362
    _globals['_VALIDATEANCHORTARGETREPLY']._serialized_start = 4365
    _globals['_VALIDATEANCHORTARGETREPLY']._serialized_end = 4497
    _globals['_GETDEVICEANCHORMETADATABYPATHREQ']._serialized_start = 4499
    _globals['_GETDEVICEANCHORMETADATABYPATHREQ']._serialized_end = 4573
    _globals['_GETDEVICEANCHORMETADATABYPATHRESULT']._serialized_start = 4576
    _globals['_GETDEVICEANCHORMETADATABYPATHRESULT']._serialized_end = 4726
    _globals['_GETDEVICEANCHORMETADATABYPATHREPLY']._serialized_start = 4729
    _globals['_GETDEVICEANCHORMETADATABYPATHREPLY']._serialized_end = 4885
    return None
