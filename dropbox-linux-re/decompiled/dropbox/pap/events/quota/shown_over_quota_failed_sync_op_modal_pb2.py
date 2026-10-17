# Source Generated with Decompyle++
# File: shown_over_quota_failed_sync_op_modal_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/quota/shown_over_quota_failed_sync_op_modal.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.pap import options_pb2 as dropbox_dot_proto_dot_pap_dot_options__pb2
from dropbox.pap.events.enums import sync_op_type_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_sync__op__type__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDdropbox/pap/events/quota/shown_over_quota_failed_sync_op_modal.proto\x12\x10pap.events.quota\x1a\x1fdropbox/proto/pap/options.proto\x1a+dropbox/pap/events/enums/sync_op_type.proto"\xd9\x02\n Shown_OverQuotaFailedSyncOpModal\x12\x16\n\x0eaction_surface\x18\x01 \x01(\t\x12S\n\x0bevent_class\x18\xcd\x08 \x01(\x0e2=.pap.events.quota.Shown_OverQuotaFailedSyncOpModal.EventClass\x124\n\x0csync_op_type\x18\x02 \x01(\x0e2\x1e.enums.sync_op_type.SyncOpType\x12\x0f\n\x07host_id\x18\x03 \x01(\t\x12\x18\n\x10in_control_group\x18\x04 \x01(\x08\x12"\n\x1ain_control_group_corrected\x18\x05 \x01(\x08"\x17\n\nEventClass\x12\t\n\x05QUOTA\x10\x00:*\xca>\x05shown\xd2>\x1fover_quota_failed_sync_op_modalB\x1aZ\x18dropbox/pap/events/quotab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.quota.shown_over_quota_failed_sync_op_modal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x18dropbox/pap/events/quota'
    _globals['_SHOWN_OVERQUOTAFAILEDSYNCOPMODAL']._loaded_options = None
    _globals['_SHOWN_OVERQUOTAFAILEDSYNCOPMODAL']._serialized_options = b'\xca>\x05shown\xd2>\x1fover_quota_failed_sync_op_modal'
    _globals['_SHOWN_OVERQUOTAFAILEDSYNCOPMODAL']._serialized_start = 169
    _globals['_SHOWN_OVERQUOTAFAILEDSYNCOPMODAL']._serialized_end = 514
    _globals['_SHOWN_OVERQUOTAFAILEDSYNCOPMODAL_EVENTCLASS']._serialized_start = 447
    _globals['_SHOWN_OVERQUOTAFAILEDSYNCOPMODAL_EVENTCLASS']._serialized_end = 470
    return None
