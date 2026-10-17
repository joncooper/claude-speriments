# Source Generated with Decompyle++
# File: encryption.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

class Blockwise(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Blockwise_validator = bv.Struct(Blockwise)

class ContentEncryptionExtras(bb.Union):
    pass
# WARNING: Decompyle incomplete

ContentEncryptionExtras_validator = bv.Union(ContentEncryptionExtras)

class EncryptedFile(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EncryptedFile_validator = bv.Struct(EncryptedFile)

class EncryptedFolder(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EncryptedFolder_validator = bv.Struct(EncryptedFolder)

class EncryptionScheme(bb.Union):
    pass
# WARNING: Decompyle incomplete

EncryptionScheme_validator = bv.Union(EncryptionScheme)

class PerRevisionKeyInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PerRevisionKeyInfo_validator = bv.Struct(PerRevisionKeyInfo)

class SymmetricCryptoExtras(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SymmetricCryptoExtras_validator = bv.Struct(SymmetricCryptoExtras)
Blockwise.set_auth_tag.validator = bv.Bytes()
Blockwise.set_auth_tag.validator._redact = bv.BlotRedactor(None)
Blockwise.block_encryption_extras.validator = bv.Nullable(bv.List(SymmetricCryptoExtras_validator))
Blockwise.encrypted_hmac_key.validator = bv.Bytes()
Blockwise.encrypted_hmac_key.validator._redact = bv.BlotRedactor(None)
Blockwise.hmac_key_encryption_extras.validator = bv.Nullable(SymmetricCryptoExtras_validator)
Blockwise._all_field_names_ = set([
    'set_auth_tag',
    'block_encryption_extras',
    'encrypted_hmac_key',
    'hmac_key_encryption_extras'])
Blockwise._all_fields_ = [
    ('set_auth_tag', Blockwise.set_auth_tag.validator),
    ('block_encryption_extras', Blockwise.block_encryption_extras.validator),
    ('encrypted_hmac_key', Blockwise.encrypted_hmac_key.validator),
    ('hmac_key_encryption_extras', Blockwise.hmac_key_encryption_extras.validator)]
ContentEncryptionExtras._blockwise_validator = Blockwise_validator
ContentEncryptionExtras._other_validator = bv.Void()
ContentEncryptionExtras._tagmap = {
    'blockwise': ContentEncryptionExtras._blockwise_validator,
    'other': ContentEncryptionExtras._other_validator }
ContentEncryptionExtras.other = ContentEncryptionExtras('other')
EncryptedFile.keyid.validator = bv.String()
EncryptedFile.keyid.validator._redact = bv.BlotRedactor(None)
EncryptedFile.encryption_scheme.validator = EncryptionScheme_validator
EncryptedFile.plaintext_blocklist_encryption_extras.validator = bv.Bytes()
EncryptedFile.plaintext_blocklist_encryption_extras.validator._redact = bv.BlotRedactor(None)
EncryptedFile.encrypted_plaintext_blocklist.validator = bv.Bytes()
EncryptedFile.encrypted_plaintext_blocklist.validator._redact = bv.BlotRedactor(None)
EncryptedFile.plaintext_file_size.validator = bv.UInt64()
EncryptedFile.plaintext_file_size.validator._redact = bv.BlotRedactor(None)
EncryptedFile.content_encryption_extras.validator = bv.Nullable(ContentEncryptionExtras_validator)
EncryptedFile.per_revision_key_info.validator = bv.Nullable(PerRevisionKeyInfo_validator)
EncryptedFile._all_field_names_ = set([
    'keyid',
    'encryption_scheme',
    'plaintext_blocklist_encryption_extras',
    'encrypted_plaintext_blocklist',
    'plaintext_file_size',
    'content_encryption_extras',
    'per_revision_key_info'])
EncryptedFile._all_fields_ = [
    ('keyid', EncryptedFile.keyid.validator),
    ('encryption_scheme', EncryptedFile.encryption_scheme.validator),
    ('plaintext_blocklist_encryption_extras', EncryptedFile.plaintext_blocklist_encryption_extras.validator),
    ('encrypted_plaintext_blocklist', EncryptedFile.encrypted_plaintext_blocklist.validator),
    ('plaintext_file_size', EncryptedFile.plaintext_file_size.validator),
    ('content_encryption_extras', EncryptedFile.content_encryption_extras.validator),
    ('per_revision_key_info', EncryptedFile.per_revision_key_info.validator)]
EncryptedFolder._all_field_names_ = set([])
EncryptedFolder._all_fields_ = []
EncryptionScheme._unknown_encryption_scheme_validator = bv.Void()
EncryptionScheme._aes_256_gcm_validator = bv.Void()
EncryptionScheme._other_validator = bv.Void()
EncryptionScheme._tagmap = {
    'unknown_encryption_scheme': EncryptionScheme._unknown_encryption_scheme_validator,
    'aes_256_gcm': EncryptionScheme._aes_256_gcm_validator,
    'other': EncryptionScheme._other_validator }
EncryptionScheme.unknown_encryption_scheme = EncryptionScheme('unknown_encryption_scheme')
EncryptionScheme.aes_256_gcm = EncryptionScheme('aes_256_gcm')
EncryptionScheme.other = EncryptionScheme('other')
PerRevisionKeyInfo.encrypted_key_data.validator = bv.Bytes()
PerRevisionKeyInfo.encrypted_key_data.validator._redact = bv.BlotRedactor(None)
PerRevisionKeyInfo.encryption_extras.validator = bv.Bytes()
PerRevisionKeyInfo.encryption_extras.validator._redact = bv.BlotRedactor(None)
PerRevisionKeyInfo._all_field_names_ = set([
    'encrypted_key_data',
    'encryption_extras'])
PerRevisionKeyInfo._all_fields_ = [
    ('encrypted_key_data', PerRevisionKeyInfo.encrypted_key_data.validator),
    ('encryption_extras', PerRevisionKeyInfo.encryption_extras.validator)]
SymmetricCryptoExtras.auth_tag.validator = bv.Bytes()
SymmetricCryptoExtras.auth_tag.validator._redact = bv.BlotRedactor(None)
SymmetricCryptoExtras.nonce.validator = bv.Bytes()
SymmetricCryptoExtras.nonce.validator._redact = bv.BlotRedactor(None)
SymmetricCryptoExtras._all_field_names_ = set([
    'auth_tag',
    'nonce'])
SymmetricCryptoExtras._all_fields_ = [
    ('auth_tag', SymmetricCryptoExtras.auth_tag.validator),
    ('nonce', SymmetricCryptoExtras.nonce.validator)]
EncryptedFile.keyid.default = ''
EncryptedFile.encryption_scheme.default = EncryptionScheme.unknown_encryption_scheme
EncryptedFile.plaintext_file_size.default = 0
ROUTES = { }
