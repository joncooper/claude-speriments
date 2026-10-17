# Source Generated with Decompyle++
# File: dbxconn_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/apex/dbxconn.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.network import network_pb2 as dropbox_dot_proto_dot_network_dot_network__pb2
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from dropbox.proto.throttler import throttler_pb2 as dropbox_dot_proto_dot_throttler_dot_throttler__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n dropbox/proto/apex/dbxconn.proto\x12\x07dbxconn\x1a#dropbox/proto/network/network.proto\x1a#dropbox/proto/rust/extensions.proto\x1a\'dropbox/proto/throttler/throttler.proto\x1a\x1bgoogle/protobuf/empty.proto"\xbb\x02\n\nServerInfo\x12\x13\n\x0bserver_name\x18\x01 \x01(\t\x12$\n\x04host\x18\x02 \x01(\x0b2\x10.network.UrlInfoB\x04\xc0\xb5\x18\x00\x12(\n\nhttp_proxy\x18\x03 \x01(\x0b2\x12.network.HttpProxyH\x00\x12,\n\x0csocks4_proxy\x18\x04 \x01(\x0b2\x14.network.Socks4ProxyH\x00\x12,\n\x0csocks5_proxy\x18\x05 \x01(\x0b2\x14.network.Socks5ProxyH\x00\x120\n\tread_mode\x18\x06 \x01(\x0b2\x17.throttler.ThrottleModeB\x04\xc0\xb5\x18\x00\x121\n\nwrite_mode\x18\x07 \x01(\x0b2\x17.throttler.ThrottleModeB\x04\xc0\xb5\x18\x00B\x07\n\x05proxy".\n\x06Config\x12$\n\x07servers\x18\x01 \x03(\x0b2\x13.dbxconn.ServerInfo"%\n\x06Header\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t"\x91\x01\n\x07Request\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0e\n\x06method\x18\x02 \x01(\t\x12\x10\n\x08endpoint\x18\x03 \x01(\t\x12 \n\x07headers\x18\x04 \x03(\x0b2\x0f.dbxconn.Header\x12\x0c\n\x04body\x18\x05 \x01(\x0c\x12\x17\n\ndebug_name\x18\x06 \x01(\tH\x00\x88\x01\x01B\r\n\x0b_debug_name"\xcf\x03\n\x08Response\x12,\n\x07success\x18\x01 \x01(\x0b2\x19.dbxconn.Response.SuccessH\x00\x122\n\x10receiver_dropped\x18\x02 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12.\n\x0cinvalid_host\x18\x03 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12<\n\x1aclient_initiated_reconnect\x18\x04 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12)\n\x07timeout\x18\x05 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x129\n\x0eprotocol_error\x18\x06 \x01(\x0b2\x1f.dbxconn.Response.ProtocolErrorH\x00\x1aI\n\x07Success\x12\x0e\n\x06status\x18\x01 \x01(\r\x12 \n\x07headers\x18\x02 \x03(\x0b2\x0f.dbxconn.Header\x12\x0c\n\x04body\x18\x03 \x01(\x0c\x1a0\n\rProtocolError\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\tB\x10\n\x08response\x12\x04\x88\xb5\x18\x00B\x14\xa2\x02\x11DropboxConnectionb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.apex.dbxconn_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\x11DropboxConnection'
    _globals['_SERVERINFO'].fields_by_name['host']._loaded_options = None
    _globals['_SERVERINFO'].fields_by_name['host']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SERVERINFO'].fields_by_name['read_mode']._loaded_options = None
    _globals['_SERVERINFO'].fields_by_name['read_mode']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SERVERINFO'].fields_by_name['write_mode']._loaded_options = None
    _globals['_SERVERINFO'].fields_by_name['write_mode']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_RESPONSE'].oneofs_by_name['response']._loaded_options = None
    _globals['_RESPONSE'].oneofs_by_name['response']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_SERVERINFO']._serialized_start = 190
    _globals['_SERVERINFO']._serialized_end = 505
    _globals['_CONFIG']._serialized_start = 507
    _globals['_CONFIG']._serialized_end = 553
    _globals['_HEADER']._serialized_start = 555
    _globals['_HEADER']._serialized_end = 592
    _globals['_REQUEST']._serialized_start = 595
    _globals['_REQUEST']._serialized_end = 740
    _globals['_RESPONSE']._serialized_start = 743
    _globals['_RESPONSE']._serialized_end = 1206
    _globals['_RESPONSE_SUCCESS']._serialized_start = 1065
    _globals['_RESPONSE_SUCCESS']._serialized_end = 1138
    _globals['_RESPONSE_PROTOCOLERROR']._serialized_start = 1140
    _globals['_RESPONSE_PROTOCOLERROR']._serialized_end = 1188
    return None
