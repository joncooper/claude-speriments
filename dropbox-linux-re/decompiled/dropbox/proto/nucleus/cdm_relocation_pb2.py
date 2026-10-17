# Source Generated with Decompyle++
# File: cdm_relocation_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/nucleus/cdm_relocation.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*dropbox/proto/nucleus/cdm_relocation.proto\x12\x07nucleus\x1a\x1bgoogle/protobuf/empty.proto"P\n\x07CdmJoin\x12"\n\x1apost_relocate_home_ns_path\x18\x04 \x01(\t\x12!\n\x19post_relocate_home_fileid\x18\x05 \x01(\t"\xec\x01\n\x18NucleusCdmRelocationArgs\x12\x1f\n\x17pre_relocate_root_ns_id\x18\x01 \x01(\x04\x12#\n\x1bpre_relocate_root_ns_fileid\x18\x02 \x01(\t\x12 \n\x18post_relocate_root_ns_id\x18\x03 \x01(\x04\x12%\n\tteam_join\x18\x04 \x01(\x0b2\x10.nucleus.CdmJoinH\x00\x12,\n\nteam_leave\x18\x05 \x01(\x0b2\x16.google.protobuf.EmptyH\x00B\x13\n\x11relocate_scenariob\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.nucleus.cdm_relocation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_CDMJOIN']._serialized_start = 84
    _globals['_CDMJOIN']._serialized_end = 164
    _globals['_NUCLEUSCDMRELOCATIONARGS']._serialized_start = 167
    _globals['_NUCLEUSCDMRELOCATIONARGS']._serialized_end = 403
    return None
