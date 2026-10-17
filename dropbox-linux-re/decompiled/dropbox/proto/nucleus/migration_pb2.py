# Source Generated with Decompyle++
# File: migration_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/nucleus/migration.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%dropbox/proto/nucleus/migration.proto\x12\x07nucleus\x1a#dropbox/proto/rust/extensions.proto\x1a\x1bgoogle/protobuf/empty.proto"\r\n\x0bNucleusArgs"\x8c\x02\n\x16UpgradeFromClassicArgs\x12!\n\x19initial_hidden_fileid_set\x18\x01 \x03(\t\x12#\n\x1bfilecache_migration_db_path\x18\x02 \x01(\t\x12\x1e\n\x14bounded_timeout_secs\x18\x03 \x01(\x04H\x00\x121\n\x0fforever_timeout\x18\x05 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12F\n\x17initial_ignore_path_set\x18\x04 \x03(\x0b2%.nucleus.UpgradeFromClassicIgnorePathB\x0f\n\x07timeout\x12\x04\x88\xb5\x18\x00"@\n\x1cUpgradeFromClassicIgnorePath\x12 \n\x18cased_root_relative_path\x18\x01 \x01(\t"~\n\x04Mode\x12\'\n\x07nucleus\x18\x01 \x01(\x0b2\x14.nucleus.NucleusArgsH\x00\x12?\n\x14upgrade_from_classic\x18\x02 \x01(\x0b2\x1f.nucleus.UpgradeFromClassicArgsH\x00B\x0c\n\x04args\x12\x04\x88\xb5\x18\x00B\x0c\xa2\x02\tNucleusSEb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.nucleus.migration_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\tNucleusSE'
    _globals['_UPGRADEFROMCLASSICARGS'].oneofs_by_name['timeout']._loaded_options = None
    _globals['_UPGRADEFROMCLASSICARGS'].oneofs_by_name['timeout']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_MODE'].oneofs_by_name['args']._loaded_options = None
    _globals['_MODE'].oneofs_by_name['args']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_NUCLEUSARGS']._serialized_start = 116
    _globals['_NUCLEUSARGS']._serialized_end = 129
    _globals['_UPGRADEFROMCLASSICARGS']._serialized_start = 132
    _globals['_UPGRADEFROMCLASSICARGS']._serialized_end = 400
    _globals['_UPGRADEFROMCLASSICIGNOREPATH']._serialized_start = 402
    _globals['_UPGRADEFROMCLASSICIGNOREPATH']._serialized_end = 466
    _globals['_MODE']._serialized_start = 468
    _globals['_MODE']._serialized_end = 594
    return None
