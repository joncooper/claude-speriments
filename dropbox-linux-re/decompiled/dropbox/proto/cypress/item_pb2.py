# Source Generated with Decompyle++
# File: item_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/cypress/item.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from dropbox.proto.cypress import item_data_space_pb2 as dropbox_dot_proto_dot_cypress_dot_item__data__space__pb2
from dropbox.proto.version_tree import types_pb2 as dropbox_dot_proto_dot_version__tree_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n dropbox/proto/cypress/item.proto\x12\x07cypress\x1a#dropbox/proto/rust/extensions.proto\x1a+dropbox/proto/cypress/item_data_space.proto\x1a&dropbox/proto/version_tree/types.proto"Q\n\x0eItemDataCreate\x12#\n\x03ids\x18\x01 \x01(\x0e2\x16.cypress.ItemDataSpace\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\r\n\x05value\x18\x03 \x01(\x0c"\x8f\x01\n\x0cItemDataEdit\x12#\n\x03ids\x18\x01 \x01(\x0e2\x16.cypress.ItemDataSpace\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12/\n\x04data\x18\x03 \x01(\x0b2!.cypress.ItemDataEdit.ItemDataVal\x1a\x1c\n\x0bItemDataVal\x12\r\n\x05value\x18\x01 \x01(\x0c"w\n\x0eItemDataRecord\x12#\n\x03ids\x18\x01 \x01(\x0e2\x16.cypress.ItemDataSpace\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12$\n\x03hlc\x18\x03 \x01(\x0b2\x11.version_tree.HlcB\x04\xc0\xb5\x18\x00\x12\r\n\x05value\x18\x04 \x01(\x0cB4\n\x19com.dropbox.proto.cypressP\x01Z\x15dropbox/proto/cypressb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.cypress.item_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.dropbox.proto.cypressP\x01Z\x15dropbox/proto/cypress'
    _globals['_ITEMDATARECORD'].fields_by_name['hlc']._loaded_options = None
    _globals['_ITEMDATARECORD'].fields_by_name['hlc']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_ITEMDATACREATE']._serialized_start = 167
    _globals['_ITEMDATACREATE']._serialized_end = 248
    _globals['_ITEMDATAEDIT']._serialized_start = 251
    _globals['_ITEMDATAEDIT']._serialized_end = 394
    _globals['_ITEMDATAEDIT_ITEMDATAVAL']._serialized_start = 366
    _globals['_ITEMDATAEDIT_ITEMDATAVAL']._serialized_end = 394
    _globals['_ITEMDATARECORD']._serialized_start = 396
    _globals['_ITEMDATARECORD']._serialized_end = 515
    return None
