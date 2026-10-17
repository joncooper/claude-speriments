# Source Generated with Decompyle++
# File: encryption_types_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/encryption/encryption_types.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.api_proxy.api_v2 import api_v2_pb2 as dropbox_dot_proto_dot_api__proxy_dot_api__v2_dot_api__v2__pb2
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/dropbox/proto/encryption/encryption_types.proto\x12\nencryption\x1a+dropbox/proto/api_proxy/api_v2/api_v2.proto\x1a#dropbox/proto/rust/extensions.proto"\x17\n\x0fEncryptedFolder:\x04\xb0\xb5\x18\x01"\xf1\x02\n\rEncryptedFile\x12\r\n\x05keyid\x18\x01 \x01(\t\x127\n\x11encryption_scheme\x18\x02 \x01(\x0e2\x1c.encryption.EncryptionScheme\x127\n%plaintext_blocklist_encryption_extras\x18\x03 \x01(\x0cB\x08\x8a\xa6\x1d\x04z\x02\x10\x01\x12/\n\x1dencrypted_plaintext_blocklist\x18\x04 \x01(\x0cB\x08\x8a\xa6\x1d\x04z\x02\x10\x01\x12\x1b\n\x13plaintext_file_size\x18\x05 \x01(\x04\x12F\n\x19content_encryption_extras\x18\x07 \x01(\x0b2#.encryption.ContentEncryptionExtras\x12=\n\x15per_revision_key_info\x18\x08 \x01(\x0b2\x1e.encryption.PerRevisionKeyInfo:\x04\xb0\xb5\x18\x01J\x04\x08\x06\x10\x07"e\n\x12PerRevisionKeyInfo\x12$\n\x12encrypted_key_data\x18\x01 \x01(\x0cB\x08\x8a\xa6\x1d\x04z\x02\x10\x01\x12#\n\x11encryption_extras\x18\x02 \x01(\x0cB\x08\x8a\xa6\x1d\x04z\x02\x10\x01:\x04\xb0\xb5\x18\x01"f\n\x17ContentEncryptionExtras\x12*\n\tblockwise\x18\x01 \x01(\x0b2\x15.encryption.BlockwiseH\x00:\n\xb0\xb5\x18\x01\x8a\xa6\x1d\x02\x18\x01B\x13\n\x0bscheme_type\x12\x04\x88\xb5\x18\x01"\xe2\x01\n\tBlockwise\x12\x1e\n\x0cset_auth_tag\x18\x01 \x01(\x0cB\x08\x8a\xa6\x1d\x04z\x02\x10\x01\x12B\n\x17block_encryption_extras\x18\x02 \x03(\x0b2!.encryption.SymmetricCryptoExtras\x12$\n\x12encrypted_hmac_key\x18\x03 \x01(\x0cB\x08\x8a\xa6\x1d\x04z\x02\x10\x01\x12E\n\x1ahmac_key_encryption_extras\x18\x04 \x01(\x0b2!.encryption.SymmetricCryptoExtras:\x04\xb0\xb5\x18\x01"R\n\x15SymmetricCryptoExtras\x12\x1a\n\x08auth_tag\x18\x01 \x01(\x0cB\x08\x8a\xa6\x1d\x04z\x02\x10\x01\x12\x17\n\x05nonce\x18\x02 \x01(\x0cB\x08\x8a\xa6\x1d\x04z\x02\x10\x01:\x04\xb0\xb5\x18\x01*N\n\x10EncryptionScheme\x12\x1d\n\x19UNKNOWN_ENCRYPTION_SCHEME\x10\x00\x12\x0f\n\x0bAES_256_GCM\x10\x03"\x04\x08\x01\x10\x01"\x04\x08\x02\x10\x02BL\n\x1ccom.dropbox.proto.encryptionP\x01Z\x18dropbox/proto/encryption\x80\xa7\x1d\x01\x8a\xa7\x1d\nencryptionb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.encryption.encryption_types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.dropbox.proto.encryptionP\x01Z\x18dropbox/proto/encryption\x80\xa7\x1d\x01\x8a\xa7\x1d\nencryption'
    _globals['_ENCRYPTEDFOLDER']._loaded_options = None
    _globals['_ENCRYPTEDFOLDER']._serialized_options = b'\xb0\xb5\x18\x01'
    _globals['_ENCRYPTEDFILE'].fields_by_name['plaintext_blocklist_encryption_extras']._loaded_options = None
    _globals['_ENCRYPTEDFILE'].fields_by_name['plaintext_blocklist_encryption_extras']._serialized_options = b'\x8a\xa6\x1d\x04z\x02\x10\x01'
    _globals['_ENCRYPTEDFILE'].fields_by_name['encrypted_plaintext_blocklist']._loaded_options = None
    _globals['_ENCRYPTEDFILE'].fields_by_name['encrypted_plaintext_blocklist']._serialized_options = b'\x8a\xa6\x1d\x04z\x02\x10\x01'
    _globals['_ENCRYPTEDFILE']._loaded_options = None
    _globals['_ENCRYPTEDFILE']._serialized_options = b'\xb0\xb5\x18\x01'
    _globals['_PERREVISIONKEYINFO'].fields_by_name['encrypted_key_data']._loaded_options = None
    _globals['_PERREVISIONKEYINFO'].fields_by_name['encrypted_key_data']._serialized_options = b'\x8a\xa6\x1d\x04z\x02\x10\x01'
    _globals['_PERREVISIONKEYINFO'].fields_by_name['encryption_extras']._loaded_options = None
    _globals['_PERREVISIONKEYINFO'].fields_by_name['encryption_extras']._serialized_options = b'\x8a\xa6\x1d\x04z\x02\x10\x01'
    _globals['_PERREVISIONKEYINFO']._loaded_options = None
    _globals['_PERREVISIONKEYINFO']._serialized_options = b'\xb0\xb5\x18\x01'
    _globals['_CONTENTENCRYPTIONEXTRAS'].oneofs_by_name['scheme_type']._loaded_options = None
    _globals['_CONTENTENCRYPTIONEXTRAS'].oneofs_by_name['scheme_type']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_CONTENTENCRYPTIONEXTRAS']._loaded_options = None
    _globals['_CONTENTENCRYPTIONEXTRAS']._serialized_options = b'\xb0\xb5\x18\x01\x8a\xa6\x1d\x02\x18\x01'
    _globals['_BLOCKWISE'].fields_by_name['set_auth_tag']._loaded_options = None
    _globals['_BLOCKWISE'].fields_by_name['set_auth_tag']._serialized_options = b'\x8a\xa6\x1d\x04z\x02\x10\x01'
    _globals['_BLOCKWISE'].fields_by_name['encrypted_hmac_key']._loaded_options = None
    _globals['_BLOCKWISE'].fields_by_name['encrypted_hmac_key']._serialized_options = b'\x8a\xa6\x1d\x04z\x02\x10\x01'
    _globals['_BLOCKWISE']._loaded_options = None
    _globals['_BLOCKWISE']._serialized_options = b'\xb0\xb5\x18\x01'
    _globals['_SYMMETRICCRYPTOEXTRAS'].fields_by_name['auth_tag']._loaded_options = None
    _globals['_SYMMETRICCRYPTOEXTRAS'].fields_by_name['auth_tag']._serialized_options = b'\x8a\xa6\x1d\x04z\x02\x10\x01'
    _globals['_SYMMETRICCRYPTOEXTRAS'].fields_by_name['nonce']._loaded_options = None
    _globals['_SYMMETRICCRYPTOEXTRAS'].fields_by_name['nonce']._serialized_options = b'\x8a\xa6\x1d\x04z\x02\x10\x01'
    _globals['_SYMMETRICCRYPTOEXTRAS']._loaded_options = None
    _globals['_SYMMETRICCRYPTOEXTRAS']._serialized_options = b'\xb0\xb5\x18\x01'
    _globals['_ENCRYPTIONSCHEME']._serialized_start = 1062
    _globals['_ENCRYPTIONSCHEME']._serialized_end = 1140
    _globals['_ENCRYPTEDFOLDER']._serialized_start = 145
    _globals['_ENCRYPTEDFOLDER']._serialized_end = 168
    _globals['_ENCRYPTEDFILE']._serialized_start = 171
    _globals['_ENCRYPTEDFILE']._serialized_end = 540
    _globals['_PERREVISIONKEYINFO']._serialized_start = 542
    _globals['_PERREVISIONKEYINFO']._serialized_end = 643
    _globals['_CONTENTENCRYPTIONEXTRAS']._serialized_start = 645
    _globals['_CONTENTENCRYPTIONEXTRAS']._serialized_end = 747
    _globals['_BLOCKWISE']._serialized_start = 750
    _globals['_BLOCKWISE']._serialized_end = 976
    _globals['_SYMMETRICCRYPTOEXTRAS']._serialized_start = 978
    _globals['_SYMMETRICCRYPTOEXTRAS']._serialized_end = 1060
    return None
