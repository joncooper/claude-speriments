# Source Generated with Decompyle++
# File: cffi_transport_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/cffi_transport/cffi_transport.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1dropbox/proto/cffi_transport/cffi_transport.proto\x12\x0ecffi_transport\x1a#dropbox/proto/rust/extensions.proto\x1a\x1bgoogle/protobuf/empty.proto"[\n\x07Request\x12\x0e\n\x06msg_id\x18\x01 \x01(\x04\x12\x13\n\x0bmethod_name\x18\x02 \x01(\t\x12\x12\n\nmethod_req\x18\x03 \x01(\x0c\x12\x17\n\x0fstream_response\x18\x04 \x01(\x08"\xbf\x01\n\x08Response\x12\x0e\n\x06msg_id\x18\x01 \x01(\x04\x12\x11\n\x07success\x18\x02 \x01(\x0cH\x00\x12+\n\tcancelled\x18\x03 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12\x0f\n\x05error\x18\x04 \x01(\tH\x00\x12\x15\n\x0bstream_item\x18\x05 \x01(\x0cH\x00\x12-\n\x0bstream_done\x18\x06 \x01(\x0b2\x16.google.protobuf.EmptyH\x00B\x0c\n\x04resp\x12\x04\x88\xb5\x18\x00"\x1a\n\x0bEchoMessage\x12\x0b\n\x03msg\x18\x01 \x01(\t"\xa5\x01\n\x0eTransportEvent\x12*\n\x08finished\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12,\n\x08response\x18\x02 \x01(\x0b2\x18.cffi_transport.ResponseH\x00\x12*\n\x07request\x18\x03 \x01(\x0b2\x17.cffi_transport.RequestH\x00B\r\n\x05event\x12\x04\x88\xb5\x18\x002\x96\x01\n\x04Test\x12B\n\x04Echo\x12\x1b.cffi_transport.EchoMessage\x1a\x1b.cffi_transport.EchoMessage"\x00\x12J\n\nEchoStream\x12\x1b.cffi_transport.EchoMessage\x1a\x1b.cffi_transport.EchoMessage"\x000\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.cffi_transport.cffi_transport_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_RESPONSE'].oneofs_by_name['resp']._loaded_options = None
    _globals['_RESPONSE'].oneofs_by_name['resp']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_TRANSPORTEVENT'].oneofs_by_name['event']._loaded_options = None
    _globals['_TRANSPORTEVENT'].oneofs_by_name['event']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_REQUEST']._serialized_start = 135
    _globals['_REQUEST']._serialized_end = 226
    _globals['_RESPONSE']._serialized_start = 229
    _globals['_RESPONSE']._serialized_end = 420
    _globals['_ECHOMESSAGE']._serialized_start = 422
    _globals['_ECHOMESSAGE']._serialized_end = 448
    _globals['_TRANSPORTEVENT']._serialized_start = 451
    _globals['_TRANSPORTEVENT']._serialized_end = 616
    _globals['_TEST']._serialized_start = 619
    _globals['_TEST']._serialized_end = 769
    return None
