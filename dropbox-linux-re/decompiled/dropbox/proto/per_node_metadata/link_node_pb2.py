# Source Generated with Decompyle++
# File: link_node_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/per_node_metadata/link_node.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.api_proxy.api_v2 import api_v2_pb2 as dropbox_dot_proto_dot_api__proxy_dot_api__v2_dot_api__v2__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/dropbox/proto/per_node_metadata/link_node.proto\x12\x11per_node_metadata\x1a+dropbox/proto/api_proxy/api_v2/api_v2.proto"C\n\x0eLinkNodeEntity\x121\n\x06action\x18\x01 \x01(\x0e2!.per_node_metadata.LinkNodeAction*\xb1\x01\n\x0eLinkNodeAction\x12\x12\n\x0eUNKNOWN_ACTION\x10\x00\x12\x1b\n\x17DEVICE_FOLDER_PRE_SETUP\x10\x01\x12\x1c\n\x14LIFE_VAULT_PRE_SETUP\x10\x02\x1a\x02\x08\x01\x12\x1d\n\x15LIFE_VAULT_POST_SETUP\x10\x03\x1a\x02\x08\x01\x12\x17\n\x13PASSWORDS_PRE_SETUP\x10\x04\x12\x18\n\x14PASSWORDS_POST_SETUP\x10\x05Ba\n#com.dropbox.proto.per_node_metadataP\x01Z\x1fdropbox/proto/per_node_metadata\x80\xa7\x1d\x01\x8a\xa7\x1d\x11per_node_metadatab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.per_node_metadata.link_node_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.dropbox.proto.per_node_metadataP\x01Z\x1fdropbox/proto/per_node_metadata\x80\xa7\x1d\x01\x8a\xa7\x1d\x11per_node_metadata'
    _globals['_LINKNODEACTION'].values_by_name['LIFE_VAULT_PRE_SETUP']._loaded_options = None
    _globals['_LINKNODEACTION'].values_by_name['LIFE_VAULT_PRE_SETUP']._serialized_options = b'\x08\x01'
    _globals['_LINKNODEACTION'].values_by_name['LIFE_VAULT_POST_SETUP']._loaded_options = None
    _globals['_LINKNODEACTION'].values_by_name['LIFE_VAULT_POST_SETUP']._serialized_options = b'\x08\x01'
    _globals['_LINKNODEACTION']._serialized_start = 185
    _globals['_LINKNODEACTION']._serialized_end = 362
    _globals['_LINKNODEENTITY']._serialized_start = 115
    _globals['_LINKNODEENTITY']._serialized_end = 182
    return None
