# Source Generated with Decompyle++
# File: network_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/network/network.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#dropbox/proto/network/network.proto\x12\x07network\x1a#dropbox/proto/rust/extensions.proto"*\n\x07UrlInfo\x12\x11\n\thost_name\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r"[\n\tHttpProxy\x12*\n\nproxy_host\x18\x01 \x01(\x0b2\x10.network.UrlInfoB\x04\xc0\xb5\x18\x00\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t"9\n\x0bSocks4Proxy\x12*\n\nproxy_host\x18\x01 \x01(\x0b2\x10.network.UrlInfoB\x04\xc0\xb5\x18\x00"]\n\x0bSocks5Proxy\x12*\n\nproxy_host\x18\x01 \x01(\x0b2\x10.network.UrlInfoB\x04\xc0\xb5\x18\x00\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\tB\x11\xa2\x02\x0eDropboxNetworkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.network.network_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\x0eDropboxNetwork'
    _globals['_HTTPPROXY'].fields_by_name['proxy_host']._loaded_options = None
    _globals['_HTTPPROXY'].fields_by_name['proxy_host']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SOCKS4PROXY'].fields_by_name['proxy_host']._loaded_options = None
    _globals['_SOCKS4PROXY'].fields_by_name['proxy_host']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SOCKS5PROXY'].fields_by_name['proxy_host']._loaded_options = None
    _globals['_SOCKS5PROXY'].fields_by_name['proxy_host']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_URLINFO']._serialized_start = 85
    _globals['_URLINFO']._serialized_end = 127
    _globals['_HTTPPROXY']._serialized_start = 129
    _globals['_HTTPPROXY']._serialized_end = 220
    _globals['_SOCKS4PROXY']._serialized_start = 222
    _globals['_SOCKS4PROXY']._serialized_end = 279
    _globals['_SOCKS5PROXY']._serialized_start = 281
    _globals['_SOCKS5PROXY']._serialized_end = 374
    return None
