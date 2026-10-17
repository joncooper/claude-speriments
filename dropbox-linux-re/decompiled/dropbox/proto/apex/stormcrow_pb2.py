# Source Generated with Decompyle++
# File: stormcrow_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/apex/stormcrow.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"dropbox/proto/apex/stormcrow.proto\x12\tstormcrow\x1a#dropbox/proto/rust/extensions.proto"\x8d\x01\n\x07Feature\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07variant\x18\x02 \x01(\t\x122\n\x08metadata\x18\x03 \x03(\x0b2 .stormcrow.Feature.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"N\n\x12PerAccountFeatures\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12$\n\x08features\x18\x02 \x03(\x0b2\x12.stormcrow.Feature";\n\x08Features\x12/\n\x08features\x18\x01 \x03(\x0b2\x1d.stormcrow.PerAccountFeatures"B\n\x08CacheKey\x12\x1f\n\x12successful_startup\x18\x01 \x01(\tH\x00\x88\x01\x01B\x15\n\x13_successful_startup"f\n\x0cFeatureCache\x12(\n\x05cache\x18\x01 \x01(\x0b2\x13.stormcrow.FeaturesB\x04\xc0\xb5\x18\x00\x12,\n\tcache_key\x18\x02 \x01(\x0b2\x13.stormcrow.CacheKeyB\x04\xc0\xb5\x18\x00"[\n\x0fObservedAccount\x124\n\x0caccount_type\x18\x01 \x01(\x0e2\x1e.stormcrow.ObservedAccountType\x12\x12\n\naccount_id\x18\x02 \x01(\t"[\n\x10ObservedFeatures\x125\n\x0cfeature_type\x18\x01 \x01(\x0e2\x1f.stormcrow.ObservedFeaturesType\x12\x10\n\x08features\x18\x02 \x03(\t"\xb2\x01\n\nUpdateInfo\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12D\n\x10updated_features\x18\x02 \x03(\x0b2*.stormcrow.UpdateInfo.UpdatedFeaturesEntry\x1aJ\n\x14UpdatedFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b2\x12.stormcrow.Feature:\x028\x01*8\n\x13ObservedAccountType\x12\x0b\n\x07MACHINE\x10\x00\x12\x0b\n\x07ACCOUNT\x10\x01\x12\x07\n\x03ANY\x10\x02*)\n\x14ObservedFeaturesType\x12\x07\n\x03ALL\x10\x00\x12\x08\n\x04LIST\x10\x01B\x13\xa2\x02\x10DropboxStormcrowb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.apex.stormcrow_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\x10DropboxStormcrow'
    _globals['_FEATURE_METADATAENTRY']._loaded_options = None
    _globals['_FEATURE_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_FEATURECACHE'].fields_by_name['cache']._loaded_options = None
    _globals['_FEATURECACHE'].fields_by_name['cache']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_FEATURECACHE'].fields_by_name['cache_key']._loaded_options = None
    _globals['_FEATURECACHE'].fields_by_name['cache_key']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_UPDATEINFO_UPDATEDFEATURESENTRY']._loaded_options = None
    _globals['_UPDATEINFO_UPDATEDFEATURESENTRY']._serialized_options = b'8\x01'
    _globals['_OBSERVEDACCOUNTTYPE']._serialized_start = 910
    _globals['_OBSERVEDACCOUNTTYPE']._serialized_end = 966
    _globals['_OBSERVEDFEATURESTYPE']._serialized_start = 968
    _globals['_OBSERVEDFEATURESTYPE']._serialized_end = 1009
    _globals['_FEATURE']._serialized_start = 87
    _globals['_FEATURE']._serialized_end = 228
    _globals['_FEATURE_METADATAENTRY']._serialized_start = 181
    _globals['_FEATURE_METADATAENTRY']._serialized_end = 228
    _globals['_PERACCOUNTFEATURES']._serialized_start = 230
    _globals['_PERACCOUNTFEATURES']._serialized_end = 308
    _globals['_FEATURES']._serialized_start = 310
    _globals['_FEATURES']._serialized_end = 369
    _globals['_CACHEKEY']._serialized_start = 371
    _globals['_CACHEKEY']._serialized_end = 437
    _globals['_FEATURECACHE']._serialized_start = 439
    _globals['_FEATURECACHE']._serialized_end = 541
    _globals['_OBSERVEDACCOUNT']._serialized_start = 543
    _globals['_OBSERVEDACCOUNT']._serialized_end = 634
    _globals['_OBSERVEDFEATURES']._serialized_start = 636
    _globals['_OBSERVEDFEATURES']._serialized_end = 727
    _globals['_UPDATEINFO']._serialized_start = 730
    _globals['_UPDATEINFO']._serialized_end = 908
    _globals['_UPDATEINFO_UPDATEDFEATURESENTRY']._serialized_start = 834
    _globals['_UPDATEINFO_UPDATEDFEATURESENTRY']._serialized_end = 908
    return None
