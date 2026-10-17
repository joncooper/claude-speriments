# Source Generated with Decompyle++
# File: fsw_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/nucleus/fsw.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from dropbox.proto.nucleus import types_pb2 as dropbox_dot_proto_dot_nucleus_dot_types__pb2
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fdropbox/proto/nucleus/fsw.proto\x12\x07nucleus\x1a\x1bgoogle/protobuf/empty.proto\x1a!dropbox/proto/nucleus/types.proto\x1a#dropbox/proto/rust/extensions.proto"!\n\x12AuxButtonLearnMore\x12\x0b\n\x03url\x18\x01 \x01(\t"B\n\x0eAuxButtonShare\x120\n\x11location_rr_paths\x18\x01 \x03(\x0b2\x15.nucleus.RRServerPath"\xaa\x01\n\x0cAuxFSWButton\x121\n\nlearn_more\x18\x01 \x01(\x0b2\x1b.nucleus.AuxButtonLearnMoreH\x00\x12(\n\x05share\x18\x02 \x01(\x0b2\x17.nucleus.AuxButtonShareH\x00\x123\n\rbutton_action\x18\x03 \x01(\x0e2\x16.nucleus.UserFSWActionB\x04\xc0\xb5\x18\x00B\x08\n\x06button"\x9d\x01\n\x11FSWDialogDecision\x12-\n\x0bno_checkbox\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12\x18\n\x0echeckbox_state\x18\x02 \x01(\x08H\x00\x123\n\rbutton_action\x18\x03 \x01(\x0e2\x16.nucleus.UserFSWActionB\x04\xc0\xb5\x18\x00B\n\n\x08checkbox*\xe6\x01\n\rUserFSWAction\x12\x16\n\x12UNKNOWN_FSW_ACTION\x10\x00\x12\t\n\x05ALLOW\x10\x01\x12\n\n\x06REVERT\x10\x02\x12\x0f\n\x0bMOVE_TO_TMF\x10\x03\x12\x10\n\x0cCLOSE_DIALOG\x10\x04\x12\x1f\n\x1bLEARN_MORE_AND_CLOSE_DIALOG\x10\x05\x12\x1a\n\x16SHARE_AND_CLOSE_DIALOG\x10\x06\x12\x14\n\x10SHARE_AND_REVERT\x10\x07\x12\x10\n\x0cDELETE_ITEMS\x10\x08\x12\x18\n\x14LEARN_MORE_AND_ALLOW\x10\t\x1a\x04\x90\xb5\x18\x01B\x0c\xa2\x02\tNucleusSEb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.nucleus.fsw_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\tNucleusSE'
    _globals['_USERFSWACTION']._loaded_options = None
    _globals['_USERFSWACTION']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_AUXFSWBUTTON'].fields_by_name['button_action']._loaded_options = None
    _globals['_AUXFSWBUTTON'].fields_by_name['button_action']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_FSWDIALOGDECISION'].fields_by_name['button_action']._loaded_options = None
    _globals['_FSWDIALOGDECISION'].fields_by_name['button_action']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_USERFSWACTION']._serialized_start = 582
    _globals['_USERFSWACTION']._serialized_end = 812
    _globals['_AUXBUTTONLEARNMORE']._serialized_start = 145
    _globals['_AUXBUTTONLEARNMORE']._serialized_end = 178
    _globals['_AUXBUTTONSHARE']._serialized_start = 180
    _globals['_AUXBUTTONSHARE']._serialized_end = 246
    _globals['_AUXFSWBUTTON']._serialized_start = 249
    _globals['_AUXFSWBUTTON']._serialized_end = 419
    _globals['_FSWDIALOGDECISION']._serialized_start = 422
    _globals['_FSWDIALOGDECISION']._serialized_end = 579
    return None
