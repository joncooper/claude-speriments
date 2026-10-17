# Source Generated with Decompyle++
# File: data_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/gatekeeper/data.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.godbx import extensions_pb2 as dropbox_dot_proto_dot_godbx_dot_extensions__pb2
from dropbox.proto.mypy import mypy_pb2 as dropbox_dot_proto_dot_mypy_dot_mypy__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#dropbox/proto/gatekeeper/data.proto\x12\ngatekeeper\x1a$dropbox/proto/godbx/extensions.proto\x1a\x1ddropbox/proto/mypy/mypy.proto"\x17\n\x05Token\x12\x0e\n\x06opaque\x18\x01 \x01(\x0c"\x95\x03\n\nCapability\x121\n\x08read_all\x18\x01 \x01(\x0b2\x1d.gatekeeper.ReadAllCapabilityH\x00\x12,\n\x05write\x18\x02 \x01(\x0b2\x1b.gatekeeper.WriteCapabilityH\x00\x122\n\x08traverse\x18\x03 \x01(\x0b2\x1e.gatekeeper.TraverseCapabilityH\x00\x12>\n\x0fread_mount_name\x18\x04 \x01(\x0b2#.gatekeeper.ReadMountNameCapabilityH\x00\x129\n\x0cnucleus_read\x18\x05 \x01(\x0b2!.gatekeeper.NucleusReadCapabilityH\x00\x12;\n\rnucleus_write\x18\x06 \x01(\x0b2".gatekeeper.NucleusWriteCapabilityH\x00\x12,\n\x05purge\x18\x07 \x01(\x0b2\x1b.gatekeeper.PurgeCapabilityH\x00B\x0c\n\ncapability"Y\n\x11ReadAllCapability\x12D\n\x05ns_id\x18\x01 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace"W\n\x0fWriteCapability\x12D\n\x05ns_id\x18\x01 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace"Z\n\x12TraverseCapability\x12D\n\x05ns_id\x18\x01 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace"_\n\x17ReadMountNameCapability\x12D\n\x05ns_id\x18\x01 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace"]\n\x15NucleusReadCapability\x12D\n\x05ns_id\x18\x01 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace"^\n\x16NucleusWriteCapability\x12D\n\x05ns_id\x18\x01 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace"W\n\x0fPurgeCapability\x12D\n\x05ns_id\x18\x01 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace"\x82\x02\n\x0cNSPermission\x12D\n\x05ns_id\x18\x01 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace\x12\r\n\x05write\x18\x02 \x01(\x08\x12\x10\n\x08read_all\x18\x03 \x01(\x08\x12\x10\n\x08traverse\x18\x04 \x01(\x08\x12\x17\n\x0fread_mount_name\x18\x05 \x01(\x08\x12\x14\n\x0cfilter_paths\x18\x06 \x03(\t\x12J\n\x0bfilterNSIDs\x18\x07 \x03(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace*P\n\x0fPermissionState\x12\x16\n\x12PERMISSION_UNKNOWN\x10\x00\x12\x12\n\x0eHAS_CAPABILITY\x10\x01\x12\x11\n\rNO_CAPABILITY\x10\x02B:\n\x1ccom.dropbox.proto.gatekeeperP\x01Z\x18dropbox/proto/gatekeeperb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.gatekeeper.data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.dropbox.proto.gatekeeperP\x01Z\x18dropbox/proto/gatekeeper'
    _globals['_READALLCAPABILITY'].fields_by_name['ns_id']._loaded_options = None
    _globals['_READALLCAPABILITY'].fields_by_name['ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_WRITECAPABILITY'].fields_by_name['ns_id']._loaded_options = None
    _globals['_WRITECAPABILITY'].fields_by_name['ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_TRAVERSECAPABILITY'].fields_by_name['ns_id']._loaded_options = None
    _globals['_TRAVERSECAPABILITY'].fields_by_name['ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_READMOUNTNAMECAPABILITY'].fields_by_name['ns_id']._loaded_options = None
    _globals['_READMOUNTNAMECAPABILITY'].fields_by_name['ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_NUCLEUSREADCAPABILITY'].fields_by_name['ns_id']._loaded_options = None
    _globals['_NUCLEUSREADCAPABILITY'].fields_by_name['ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_NUCLEUSWRITECAPABILITY'].fields_by_name['ns_id']._loaded_options = None
    _globals['_NUCLEUSWRITECAPABILITY'].fields_by_name['ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_PURGECAPABILITY'].fields_by_name['ns_id']._loaded_options = None
    _globals['_PURGECAPABILITY'].fields_by_name['ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_NSPERMISSION'].fields_by_name['ns_id']._loaded_options = None
    _globals['_NSPERMISSION'].fields_by_name['ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_NSPERMISSION'].fields_by_name['filterNSIDs']._loaded_options = None
    _globals['_NSPERMISSION'].fields_by_name['filterNSIDs']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_PERMISSIONSTATE']._serialized_start = 1463
    _globals['_PERMISSIONSTATE']._serialized_end = 1543
    _globals['_TOKEN']._serialized_start = 120
    _globals['_TOKEN']._serialized_end = 143
    _globals['_CAPABILITY']._serialized_start = 146
    _globals['_CAPABILITY']._serialized_end = 551
    _globals['_READALLCAPABILITY']._serialized_start = 553
    _globals['_READALLCAPABILITY']._serialized_end = 642
    _globals['_WRITECAPABILITY']._serialized_start = 644
    _globals['_WRITECAPABILITY']._serialized_end = 731
    _globals['_TRAVERSECAPABILITY']._serialized_start = 733
    _globals['_TRAVERSECAPABILITY']._serialized_end = 823
    _globals['_READMOUNTNAMECAPABILITY']._serialized_start = 825
    _globals['_READMOUNTNAMECAPABILITY']._serialized_end = 920
    _globals['_NUCLEUSREADCAPABILITY']._serialized_start = 922
    _globals['_NUCLEUSREADCAPABILITY']._serialized_end = 1015
    _globals['_NUCLEUSWRITECAPABILITY']._serialized_start = 1017
    _globals['_NUCLEUSWRITECAPABILITY']._serialized_end = 1111
    _globals['_PURGECAPABILITY']._serialized_start = 1113
    _globals['_PURGECAPABILITY']._serialized_end = 1200
    _globals['_NSPERMISSION']._serialized_start = 1203
    _globals['_NSPERMISSION']._serialized_end = 1461
    return None
