# Source Generated with Decompyle++
# File: ekms.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import common

class AsymmetricEncryptionAlgorithm(bb.Union):
    pass
# WARNING: Decompyle incomplete

AsymmetricEncryptionAlgorithm_validator = bv.Union(AsymmetricEncryptionAlgorithm)

class BackupKey(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BackupKey_validator = bv.Struct(BackupKey)

class BinaryPosition(bb.Union):
    pass
# WARNING: Decompyle incomplete

BinaryPosition_validator = bv.Union(BinaryPosition)

class BoltChannelToken(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BoltChannelToken_validator = bv.Struct(BoltChannelToken)

class CancelKeyRotationArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CancelKeyRotationArg_validator = bv.Struct(CancelKeyRotationArg)

class CancelKeyRotationError(bb.Union):
    pass
# WARNING: Decompyle incomplete

CancelKeyRotationError_validator = bv.Union(CancelKeyRotationError)

class ChannelId(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ChannelId_validator = bv.Struct(ChannelId)

class ClientDetails(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ClientDetails_validator = bv.Struct(ClientDetails)

class ClientKeyEnrollmentStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

ClientKeyEnrollmentStatus_validator = bv.Union(ClientKeyEnrollmentStatus)

class EncryptedFileKey(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EncryptedFileKey_validator = bv.Struct(EncryptedFileKey)

class EncryptedFileKeyDraft(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EncryptedFileKeyDraft_validator = bv.Struct(EncryptedFileKeyDraft)

class EncryptedKeyPair(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EncryptedKeyPair_validator = bv.Struct(EncryptedKeyPair)

class EncryptedKeyPairDraft(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EncryptedKeyPairDraft_validator = bv.Struct(EncryptedKeyPairDraft)

class EncryptedNamespaceKey(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EncryptedNamespaceKey_validator = bv.Struct(EncryptedNamespaceKey)

class EncryptedNamespaceKeyDraft(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EncryptedNamespaceKeyDraft_validator = bv.Struct(EncryptedNamespaceKeyDraft)

class EncryptedTeamKey(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EncryptedTeamKey_validator = bv.Struct(EncryptedTeamKey)

class EncryptedTeamKeyDraft(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EncryptedTeamKeyDraft_validator = bv.Struct(EncryptedTeamKeyDraft)

class EnrollBackupKeyForTeamArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EnrollBackupKeyForTeamArg_validator = bv.Struct(EnrollBackupKeyForTeamArg)

class EnrollBackupKeyForTeamError(bb.Union):
    pass
# WARNING: Decompyle incomplete

EnrollBackupKeyForTeamError_validator = bv.Union(EnrollBackupKeyForTeamError)

class EnrollClientsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EnrollClientsArg_validator = bv.Struct(EnrollClientsArg)

class EnrollClientsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

EnrollClientsError_validator = bv.Union(EnrollClientsError)

class EnrollTeamArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EnrollTeamArg_validator = bv.Struct(EnrollTeamArg)

class EnrollTeamError(bb.Union):
    pass
# WARNING: Decompyle incomplete

EnrollTeamError_validator = bv.Union(EnrollTeamError)

class EnrollTeamKeyDraftForBackupKeysArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EnrollTeamKeyDraftForBackupKeysArg_validator = bv.Struct(EnrollTeamKeyDraftForBackupKeysArg)

class EnrollTeamKeyDraftForBackupKeysError(bb.Union):
    pass
# WARNING: Decompyle incomplete

EnrollTeamKeyDraftForBackupKeysError_validator = bv.Union(EnrollTeamKeyDraftForBackupKeysError)

class EnrollTeamKeyDraftForBackupKeysResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EnrollTeamKeyDraftForBackupKeysResponse_validator = bv.Struct(EnrollTeamKeyDraftForBackupKeysResponse)

class EnrollTeamKeyDraftForClientKeysArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EnrollTeamKeyDraftForClientKeysArg_validator = bv.Struct(EnrollTeamKeyDraftForClientKeysArg)

class EnrollTeamKeyDraftForClientKeysError(bb.Union):
    pass
# WARNING: Decompyle incomplete

EnrollTeamKeyDraftForClientKeysError_validator = bv.Union(EnrollTeamKeyDraftForClientKeysError)

class EnrollTeamKeyDraftForClientKeysResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EnrollTeamKeyDraftForClientKeysResponse_validator = bv.Struct(EnrollTeamKeyDraftForClientKeysResponse)

class EnrollTeamResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EnrollTeamResponse_validator = bv.Struct(EnrollTeamResponse)

class GetBackupKeysArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetBackupKeysArg_validator = bv.Struct(GetBackupKeysArg)

class GetBackupKeysError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetBackupKeysError_validator = bv.Union(GetBackupKeysError)

class GetBackupKeysResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetBackupKeysResponse_validator = bv.Struct(GetBackupKeysResponse)

class GetClientKeyEnrollmentStatusArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetClientKeyEnrollmentStatusArg_validator = bv.Struct(GetClientKeyEnrollmentStatusArg)

class GetClientKeyEnrollmentStatusError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetClientKeyEnrollmentStatusError_validator = bv.Union(GetClientKeyEnrollmentStatusError)

class GetClientKeyEnrollmentStatusResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetClientKeyEnrollmentStatusResponse_validator = bv.Struct(GetClientKeyEnrollmentStatusResponse)

class GetEncryptedDraftTeamKeyWithBackupKeyArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetEncryptedDraftTeamKeyWithBackupKeyArg_validator = bv.Struct(GetEncryptedDraftTeamKeyWithBackupKeyArg)

class GetEncryptedDraftTeamKeyWithBackupKeyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetEncryptedDraftTeamKeyWithBackupKeyError_validator = bv.Union(GetEncryptedDraftTeamKeyWithBackupKeyError)

class GetEncryptedDraftTeamKeyWithBackupKeyResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetEncryptedDraftTeamKeyWithBackupKeyResponse_validator = bv.Struct(GetEncryptedDraftTeamKeyWithBackupKeyResponse)

class GetEncryptedTeamKeyListWithBackupKeyArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetEncryptedTeamKeyListWithBackupKeyArg_validator = bv.Struct(GetEncryptedTeamKeyListWithBackupKeyArg)

class GetEncryptedTeamKeyListWithBackupKeyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetEncryptedTeamKeyListWithBackupKeyError_validator = bv.Union(GetEncryptedTeamKeyListWithBackupKeyError)

class GetEncryptedTeamKeyListWithBackupKeyResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetEncryptedTeamKeyListWithBackupKeyResponse_validator = bv.Struct(GetEncryptedTeamKeyListWithBackupKeyResponse)

class GetEncryptedTeamKeyListWithClientKeyArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetEncryptedTeamKeyListWithClientKeyArg_validator = bv.Struct(GetEncryptedTeamKeyListWithClientKeyArg)

class GetEncryptedTeamKeyListWithClientKeyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetEncryptedTeamKeyListWithClientKeyError_validator = bv.Union(GetEncryptedTeamKeyListWithClientKeyError)

class GetEncryptedTeamKeyListWithClientKeyResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetEncryptedTeamKeyListWithClientKeyResponse_validator = bv.Struct(GetEncryptedTeamKeyListWithClientKeyResponse)

class GetEncryptedTeamKeyWithClientKeyArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetEncryptedTeamKeyWithClientKeyArg_validator = bv.Struct(GetEncryptedTeamKeyWithClientKeyArg)

class GetEncryptedTeamKeyWithClientKeyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetEncryptedTeamKeyWithClientKeyError_validator = bv.Union(GetEncryptedTeamKeyWithClientKeyError)

class GetEncryptedTeamKeyWithClientKeyResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetEncryptedTeamKeyWithClientKeyResponse_validator = bv.Struct(GetEncryptedTeamKeyWithClientKeyResponse)

class GetFileKeysArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileKeysArg_validator = bv.Struct(GetFileKeysArg)

class GetFileKeysError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetFileKeysError_validator = bv.Union(GetFileKeysError)

class GetFileKeysResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileKeysResponse_validator = bv.Struct(GetFileKeysResponse)

class GetNamespaceKeyArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetNamespaceKeyArg_validator = bv.Struct(GetNamespaceKeyArg)

class GetNamespaceKeyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetNamespaceKeyError_validator = bv.Union(GetNamespaceKeyError)

class GetNamespaceKeyResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetNamespaceKeyResponse_validator = bv.Struct(GetNamespaceKeyResponse)

class GetNamespaceKeysArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetNamespaceKeysArg_validator = bv.Struct(GetNamespaceKeysArg)

class GetNamespaceKeysError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetNamespaceKeysError_validator = bv.Union(GetNamespaceKeysError)

class GetNamespaceKeysInfoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetNamespaceKeysInfoArg_validator = bv.Struct(GetNamespaceKeysInfoArg)

class GetNamespaceKeysInfoError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetNamespaceKeysInfoError_validator = bv.Union(GetNamespaceKeysInfoError)

class GetNamespaceKeysInfoResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetNamespaceKeysInfoResponse_validator = bv.Struct(GetNamespaceKeysInfoResponse)

class GetNamespaceKeysResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetNamespaceKeysResponse_validator = bv.Struct(GetNamespaceKeysResponse)

class GetNamespacePublicKeyArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetNamespacePublicKeyArg_validator = bv.Struct(GetNamespacePublicKeyArg)

class GetNamespacePublicKeyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetNamespacePublicKeyError_validator = bv.Union(GetNamespacePublicKeyError)

class GetNamespacePublicKeyResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetNamespacePublicKeyResponse_validator = bv.Struct(GetNamespacePublicKeyResponse)

class GetPendingClientsDetailsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetPendingClientsDetailsError_validator = bv.Union(GetPendingClientsDetailsError)

class GetPendingClientsDetailsResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetPendingClientsDetailsResponse_validator = bv.Struct(GetPendingClientsDetailsResponse)

class GetPendingClientsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetPendingClientsError_validator = bv.Union(GetPendingClientsError)

class GetPendingClientsResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetPendingClientsResponse_validator = bv.Struct(GetPendingClientsResponse)

class GetRegisteredClientPublicKeysByIdArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetRegisteredClientPublicKeysByIdArg_validator = bv.Struct(GetRegisteredClientPublicKeysByIdArg)

class GetRegisteredClientPublicKeysByIdError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetRegisteredClientPublicKeysByIdError_validator = bv.Union(GetRegisteredClientPublicKeysByIdError)

class GetRegisteredClientPublicKeysByIdResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetRegisteredClientPublicKeysByIdResponse_validator = bv.Struct(GetRegisteredClientPublicKeysByIdResponse)

class GetRegisteredClientPublicKeysPagedArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetRegisteredClientPublicKeysPagedArg_validator = bv.Struct(GetRegisteredClientPublicKeysPagedArg)

class GetRegisteredClientPublicKeysPagedError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetRegisteredClientPublicKeysPagedError_validator = bv.Union(GetRegisteredClientPublicKeysPagedError)

class GetRegisteredClientPublicKeysPagedResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetRegisteredClientPublicKeysPagedResponse_validator = bv.Struct(GetRegisteredClientPublicKeysPagedResponse)

class GetTeamEnrollmentStatusArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetTeamEnrollmentStatusArg_validator = bv.Struct(GetTeamEnrollmentStatusArg)

class GetTeamEnrollmentStatusError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetTeamEnrollmentStatusError_validator = bv.Union(GetTeamEnrollmentStatusError)

class GetTeamEnrollmentStatusResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetTeamEnrollmentStatusResponse_validator = bv.Struct(GetTeamEnrollmentStatusResponse)

class GetTeamKeyRotationInfoError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetTeamKeyRotationInfoError_validator = bv.Union(GetTeamKeyRotationInfoError)

class GetTeamKeyRotationInfoResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetTeamKeyRotationInfoResponse_validator = bv.Struct(GetTeamKeyRotationInfoResponse)

class GetTeamPublicKeyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetTeamPublicKeyError_validator = bv.Union(GetTeamPublicKeyError)

class GetTeamPublicKeyResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetTeamPublicKeyResponse_validator = bv.Struct(GetTeamPublicKeyResponse)

class InitTeamKeyRotationArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InitTeamKeyRotationArg_validator = bv.Struct(InitTeamKeyRotationArg)

class InitTeamKeyRotationError(bb.Union):
    pass
# WARNING: Decompyle incomplete

InitTeamKeyRotationError_validator = bv.Union(InitTeamKeyRotationError)

class InitTeamKeyRotationResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InitTeamKeyRotationResponse_validator = bv.Struct(InitTeamKeyRotationResponse)

class MerkleProof(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MerkleProof_validator = bv.Struct(MerkleProof)

class MerkleProofHash(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MerkleProofHash_validator = bv.Struct(MerkleProofHash)

class NamespaceKeyDraft(bb.Struct):
    pass
# WARNING: Decompyle incomplete

NamespaceKeyDraft_validator = bv.Struct(NamespaceKeyDraft)

class NamespaceKeyInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

NamespaceKeyInfo_validator = bv.Struct(NamespaceKeyInfo)

class PublicKey(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PublicKey_validator = bv.Struct(PublicKey)

class PublicKeyDraft(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PublicKeyDraft_validator = bv.Struct(PublicKeyDraft)

class RegisterBackupKeyArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RegisterBackupKeyArg_validator = bv.Struct(RegisterBackupKeyArg)

class RegisterBackupKeyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RegisterBackupKeyError_validator = bv.Union(RegisterBackupKeyError)

class RegisterBackupKeyResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RegisterBackupKeyResponse_validator = bv.Struct(RegisterBackupKeyResponse)

class RegisterClientArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RegisterClientArg_validator = bv.Struct(RegisterClientArg)

class RegisterClientError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RegisterClientError_validator = bv.Union(RegisterClientError)

class RegisterClientResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RegisterClientResponse_validator = bv.Struct(RegisterClientResponse)

class RegisterFileKeyBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RegisterFileKeyBatchArg_validator = bv.Struct(RegisterFileKeyBatchArg)

class RegisterFileKeyBatchError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RegisterFileKeyBatchError_validator = bv.Union(RegisterFileKeyBatchError)

class RegisterFileKeyBatchResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RegisterFileKeyBatchResponse_validator = bv.Struct(RegisterFileKeyBatchResponse)

class RegisterFileKeyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RegisterFileKeyError_validator = bv.Union(RegisterFileKeyError)

class RegisterFileKeyRequest(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RegisterFileKeyRequest_validator = bv.Struct(RegisterFileKeyRequest)

class RegisterFileKeyResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RegisterFileKeyResponse_validator = bv.Struct(RegisterFileKeyResponse)

class RegisterNamespaceKeyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RegisterNamespaceKeyError_validator = bv.Union(RegisterNamespaceKeyError)

class RegisterNamespaceKeysForDraftTeamKeyArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RegisterNamespaceKeysForDraftTeamKeyArg_validator = bv.Struct(RegisterNamespaceKeysForDraftTeamKeyArg)

class RegisterNamespaceKeysForDraftTeamKeyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RegisterNamespaceKeysForDraftTeamKeyError_validator = bv.Union(RegisterNamespaceKeysForDraftTeamKeyError)

class RemoveBackupKeyArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RemoveBackupKeyArg_validator = bv.Struct(RemoveBackupKeyArg)

class RemoveBackupKeyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RemoveBackupKeyError_validator = bv.Union(RemoveBackupKeyError)

class RotateTeamKeyArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RotateTeamKeyArg_validator = bv.Struct(RotateTeamKeyArg)

class RotateTeamKeyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RotateTeamKeyError_validator = bv.Union(RotateTeamKeyError)

class RotateTeamKeyResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RotateTeamKeyResponse_validator = bv.Struct(RotateTeamKeyResponse)

class RotateTeamKeyResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

RotateTeamKeyResult_validator = bv.Union(RotateTeamKeyResult)

class SelectedBackupKeys(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SelectedBackupKeys_validator = bv.Struct(SelectedBackupKeys)

class SelectedNamespaceKeys(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SelectedNamespaceKeys_validator = bv.Struct(SelectedNamespaceKeys)

class ShareNamespaceArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ShareNamespaceArg_validator = bv.Struct(ShareNamespaceArg)

class ShareNamespaceError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ShareNamespaceError_validator = bv.Union(ShareNamespaceError)

class ShareNamespaceKeysRotatedError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ShareNamespaceKeysRotatedError_validator = bv.Struct(ShareNamespaceKeysRotatedError)

class SymmetricEncryptionAlgorithm(bb.Union):
    pass
# WARNING: Decompyle incomplete

SymmetricEncryptionAlgorithm_validator = bv.Union(SymmetricEncryptionAlgorithm)

class TeamEnrollmentStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

TeamEnrollmentStatus_validator = bv.Union(TeamEnrollmentStatus)

class TeamKeyInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TeamKeyInfo_validator = bv.Struct(TeamKeyInfo)
AsymmetricEncryptionAlgorithm._unknown_asymmetric_encryption_algorithm_validator = bv.Void()
AsymmetricEncryptionAlgorithm._hpke_dhkem_p256_hkdf_sha256_hkdf_sha256_aes256_gcm_validator = bv.Void()
AsymmetricEncryptionAlgorithm._sender_auth_hpke_dhkem_p256_hkdf_sha256_hkdf_sha256_aes256_gcm_validator = bv.Void()
AsymmetricEncryptionAlgorithm._other_validator = bv.Void()
AsymmetricEncryptionAlgorithm._tagmap = {
    'unknown_asymmetric_encryption_algorithm': AsymmetricEncryptionAlgorithm._unknown_asymmetric_encryption_algorithm_validator,
    'hpke_dhkem_p256_hkdf_sha256_hkdf_sha256_aes256_gcm': AsymmetricEncryptionAlgorithm._hpke_dhkem_p256_hkdf_sha256_hkdf_sha256_aes256_gcm_validator,
    'sender_auth_hpke_dhkem_p256_hkdf_sha256_hkdf_sha256_aes256_gcm': AsymmetricEncryptionAlgorithm._sender_auth_hpke_dhkem_p256_hkdf_sha256_hkdf_sha256_aes256_gcm_validator,
    'other': AsymmetricEncryptionAlgorithm._other_validator }
AsymmetricEncryptionAlgorithm.unknown_asymmetric_encryption_algorithm = AsymmetricEncryptionAlgorithm('unknown_asymmetric_encryption_algorithm')
AsymmetricEncryptionAlgorithm.hpke_dhkem_p256_hkdf_sha256_hkdf_sha256_aes256_gcm = AsymmetricEncryptionAlgorithm('hpke_dhkem_p256_hkdf_sha256_hkdf_sha256_aes256_gcm')
AsymmetricEncryptionAlgorithm.sender_auth_hpke_dhkem_p256_hkdf_sha256_hkdf_sha256_aes256_gcm = AsymmetricEncryptionAlgorithm('sender_auth_hpke_dhkem_p256_hkdf_sha256_hkdf_sha256_aes256_gcm')
AsymmetricEncryptionAlgorithm.other = AsymmetricEncryptionAlgorithm('other')
BackupKey.key_id.validator = bv.String()
BackupKey.key_id.validator._redact = bv.BlotRedactor(None)
BackupKey.algorithm.validator = AsymmetricEncryptionAlgorithm_validator
BackupKey.created.validator = bv.Nullable(common.DropboxTimestamp_validator)
BackupKey.enrolled.validator = bv.Nullable(common.DropboxTimestamp_validator)
BackupKey.public_key_data.validator = bv.Bytes()
BackupKey.public_key_data.validator._redact = bv.BlotRedactor(None)
BackupKey._all_field_names_ = set([
    'key_id',
    'algorithm',
    'created',
    'enrolled',
    'public_key_data'])
BackupKey._all_fields_ = [
    ('key_id', BackupKey.key_id.validator),
    ('algorithm', BackupKey.algorithm.validator),
    ('created', BackupKey.created.validator),
    ('enrolled', BackupKey.enrolled.validator),
    ('public_key_data', BackupKey.public_key_data.validator)]
BinaryPosition._left_validator = bv.Void()
BinaryPosition._right_validator = bv.Void()
BinaryPosition._other_validator = bv.Void()
BinaryPosition._tagmap = {
    'left': BinaryPosition._left_validator,
    'right': BinaryPosition._right_validator,
    'other': BinaryPosition._other_validator }
BinaryPosition.left = BinaryPosition('left')
BinaryPosition.right = BinaryPosition('right')
BinaryPosition.other = BinaryPosition('other')
BoltChannelToken.channel_id.validator = bv.Nullable(ChannelId_validator)
BoltChannelToken.revision.validator = bv.UInt64()
BoltChannelToken.revision.validator._redact = bv.BlotRedactor(None)
BoltChannelToken.token.validator = bv.String()
BoltChannelToken.token.validator._redact = bv.BlotRedactor(None)
BoltChannelToken.rev.validator = bv.String()
BoltChannelToken.rev.validator._redact = bv.BlotRedactor(None)
BoltChannelToken.deprecated_revision.validator = bv.UInt64()
BoltChannelToken.deprecated_revision.validator._redact = bv.BlotRedactor(None)
BoltChannelToken._all_field_names_ = set([
    'channel_id',
    'revision',
    'token',
    'rev',
    'deprecated_revision'])
BoltChannelToken._all_fields_ = [
    ('channel_id', BoltChannelToken.channel_id.validator),
    ('revision', BoltChannelToken.revision.validator),
    ('token', BoltChannelToken.token.validator),
    ('rev', BoltChannelToken.rev.validator),
    ('deprecated_revision', BoltChannelToken.deprecated_revision.validator)]
CancelKeyRotationArg.draft_team_key_id.validator = bv.String()
CancelKeyRotationArg.draft_team_key_id.validator._redact = bv.BlotRedactor(None)
CancelKeyRotationArg._all_field_names_ = set([
    'draft_team_key_id'])
CancelKeyRotationArg._all_fields_ = [
    ('draft_team_key_id', CancelKeyRotationArg.draft_team_key_id.validator)]
CancelKeyRotationError._permission_denied_validator = bv.Void()
CancelKeyRotationError._team_key_not_found_validator = bv.Void()
CancelKeyRotationError._namespace_key_not_found_validator = bv.Void()
CancelKeyRotationError._missing_arguments_validator = bv.Void()
CancelKeyRotationError._other_validator = bv.Void()
CancelKeyRotationError._tagmap = {
    'permission_denied': CancelKeyRotationError._permission_denied_validator,
    'team_key_not_found': CancelKeyRotationError._team_key_not_found_validator,
    'namespace_key_not_found': CancelKeyRotationError._namespace_key_not_found_validator,
    'missing_arguments': CancelKeyRotationError._missing_arguments_validator,
    'other': CancelKeyRotationError._other_validator }
CancelKeyRotationError.permission_denied = CancelKeyRotationError('permission_denied')
CancelKeyRotationError.team_key_not_found = CancelKeyRotationError('team_key_not_found')
CancelKeyRotationError.namespace_key_not_found = CancelKeyRotationError('namespace_key_not_found')
CancelKeyRotationError.missing_arguments = CancelKeyRotationError('missing_arguments')
CancelKeyRotationError.other = CancelKeyRotationError('other')
ChannelId.app_id.validator = bv.String()
ChannelId.app_id.validator._redact = bv.BlotRedactor(None)
ChannelId.unique_id.validator = bv.String()
ChannelId.unique_id.validator._redact = bv.BlotRedactor(None)
ChannelId._all_field_names_ = set([
    'app_id',
    'unique_id'])
ChannelId._all_fields_ = [
    ('app_id', ChannelId.app_id.validator),
    ('unique_id', ChannelId.unique_id.validator)]
ClientDetails.public_key.validator = bv.Nullable(PublicKey_validator)
ClientDetails.display_name.validator = bv.String()
ClientDetails.display_name.validator._redact = bv.BlotRedactor(None)
ClientDetails.email.validator = bv.String()
ClientDetails.email.validator._redact = bv.BlotRedactor(None)
ClientDetails.account_photo_url.validator = bv.String()
ClientDetails.account_photo_url.validator._redact = bv.BlotRedactor(None)
ClientDetails.registration_date.validator = bv.Nullable(common.DropboxTimestamp_validator)
ClientDetails._all_field_names_ = set([
    'public_key',
    'display_name',
    'email',
    'account_photo_url',
    'registration_date'])
ClientDetails._all_fields_ = [
    ('public_key', ClientDetails.public_key.validator),
    ('display_name', ClientDetails.display_name.validator),
    ('email', ClientDetails.email.validator),
    ('account_photo_url', ClientDetails.account_photo_url.validator),
    ('registration_date', ClientDetails.registration_date.validator)]
ClientKeyEnrollmentStatus._client_not_registered_validator = bv.Void()
ClientKeyEnrollmentStatus._client_not_enrolled_validator = bv.Void()
ClientKeyEnrollmentStatus._client_enrolled_validator = bv.Void()
ClientKeyEnrollmentStatus._other_validator = bv.Void()
ClientKeyEnrollmentStatus._tagmap = {
    'client_not_registered': ClientKeyEnrollmentStatus._client_not_registered_validator,
    'client_not_enrolled': ClientKeyEnrollmentStatus._client_not_enrolled_validator,
    'client_enrolled': ClientKeyEnrollmentStatus._client_enrolled_validator,
    'other': ClientKeyEnrollmentStatus._other_validator }
ClientKeyEnrollmentStatus.client_not_registered = ClientKeyEnrollmentStatus('client_not_registered')
ClientKeyEnrollmentStatus.client_not_enrolled = ClientKeyEnrollmentStatus('client_not_enrolled')
ClientKeyEnrollmentStatus.client_enrolled = ClientKeyEnrollmentStatus('client_enrolled')
ClientKeyEnrollmentStatus.other = ClientKeyEnrollmentStatus('other')
EncryptedFileKey.key_id.validator = bv.String()
EncryptedFileKey.key_id.validator._redact = bv.BlotRedactor(None)
EncryptedFileKey.encrypted_key_data.validator = bv.Bytes()
EncryptedFileKey.encrypted_key_data.validator._redact = bv.BlotRedactor(None)
EncryptedFileKey.encrypting_key_id.validator = bv.String()
EncryptedFileKey.encrypting_key_id.validator._redact = bv.BlotRedactor(None)
EncryptedFileKey.algorithm.validator = SymmetricEncryptionAlgorithm_validator
EncryptedFileKey._all_field_names_ = set([
    'key_id',
    'encrypted_key_data',
    'encrypting_key_id',
    'algorithm'])
EncryptedFileKey._all_fields_ = [
    ('key_id', EncryptedFileKey.key_id.validator),
    ('encrypted_key_data', EncryptedFileKey.encrypted_key_data.validator),
    ('encrypting_key_id', EncryptedFileKey.encrypting_key_id.validator),
    ('algorithm', EncryptedFileKey.algorithm.validator)]
EncryptedFileKeyDraft.encrypted_key_data.validator = bv.Bytes()
EncryptedFileKeyDraft.encrypted_key_data.validator._redact = bv.BlotRedactor(None)
EncryptedFileKeyDraft.encrypting_key_id.validator = bv.String()
EncryptedFileKeyDraft.encrypting_key_id.validator._redact = bv.BlotRedactor(None)
EncryptedFileKeyDraft.algorithm.validator = SymmetricEncryptionAlgorithm_validator
EncryptedFileKeyDraft._all_field_names_ = set([
    'encrypted_key_data',
    'encrypting_key_id',
    'algorithm'])
EncryptedFileKeyDraft._all_fields_ = [
    ('encrypted_key_data', EncryptedFileKeyDraft.encrypted_key_data.validator),
    ('encrypting_key_id', EncryptedFileKeyDraft.encrypting_key_id.validator),
    ('algorithm', EncryptedFileKeyDraft.algorithm.validator)]
EncryptedKeyPair.key_id.validator = bv.String()
EncryptedKeyPair.key_id.validator._redact = bv.BlotRedactor(None)
EncryptedKeyPair.encrypted_private_key_data.validator = bv.Bytes()
EncryptedKeyPair.encrypted_private_key_data.validator._redact = bv.BlotRedactor(None)
EncryptedKeyPair.public_key_data.validator = bv.Bytes()
EncryptedKeyPair.public_key_data.validator._redact = bv.BlotRedactor(None)
EncryptedKeyPair.encrypting_key_id.validator = bv.String()
EncryptedKeyPair.encrypting_key_id.validator._redact = bv.BlotRedactor(None)
EncryptedKeyPair.algorithm.validator = AsymmetricEncryptionAlgorithm_validator
EncryptedKeyPair.merkle_proof.validator = bv.Nullable(MerkleProof_validator)
EncryptedKeyPair._all_field_names_ = set([
    'key_id',
    'encrypted_private_key_data',
    'public_key_data',
    'encrypting_key_id',
    'algorithm',
    'merkle_proof'])
EncryptedKeyPair._all_fields_ = [
    ('key_id', EncryptedKeyPair.key_id.validator),
    ('encrypted_private_key_data', EncryptedKeyPair.encrypted_private_key_data.validator),
    ('public_key_data', EncryptedKeyPair.public_key_data.validator),
    ('encrypting_key_id', EncryptedKeyPair.encrypting_key_id.validator),
    ('algorithm', EncryptedKeyPair.algorithm.validator),
    ('merkle_proof', EncryptedKeyPair.merkle_proof.validator)]
EncryptedKeyPairDraft.encrypted_private_key_data.validator = bv.Bytes()
EncryptedKeyPairDraft.encrypted_private_key_data.validator._redact = bv.BlotRedactor(None)
EncryptedKeyPairDraft.public_key_data.validator = bv.Bytes()
EncryptedKeyPairDraft.public_key_data.validator._redact = bv.BlotRedactor(None)
EncryptedKeyPairDraft.algorithm.validator = AsymmetricEncryptionAlgorithm_validator
EncryptedKeyPairDraft._all_field_names_ = set([
    'encrypted_private_key_data',
    'public_key_data',
    'algorithm'])
EncryptedKeyPairDraft._all_fields_ = [
    ('encrypted_private_key_data', EncryptedKeyPairDraft.encrypted_private_key_data.validator),
    ('public_key_data', EncryptedKeyPairDraft.public_key_data.validator),
    ('algorithm', EncryptedKeyPairDraft.algorithm.validator)]
EncryptedNamespaceKey.namespace_key_id.validator = bv.String()
EncryptedNamespaceKey.namespace_key_id.validator._redact = bv.BlotRedactor(None)
EncryptedNamespaceKey.encrypted_private_key_data.validator = bv.Bytes()
EncryptedNamespaceKey.encrypted_private_key_data.validator._redact = bv.BlotRedactor(None)
EncryptedNamespaceKey.encrypting_key_id.validator = bv.String()
EncryptedNamespaceKey.encrypting_key_id.validator._redact = bv.BlotRedactor(None)
EncryptedNamespaceKey._all_field_names_ = set([
    'namespace_key_id',
    'encrypted_private_key_data',
    'encrypting_key_id'])
EncryptedNamespaceKey._all_fields_ = [
    ('namespace_key_id', EncryptedNamespaceKey.namespace_key_id.validator),
    ('encrypted_private_key_data', EncryptedNamespaceKey.encrypted_private_key_data.validator),
    ('encrypting_key_id', EncryptedNamespaceKey.encrypting_key_id.validator)]
EncryptedNamespaceKeyDraft.encrypting_key_id.validator = bv.String()
EncryptedNamespaceKeyDraft.encrypting_key_id.validator._redact = bv.BlotRedactor(None)
EncryptedNamespaceKeyDraft.encrypted_private_key_data.validator = bv.Bytes()
EncryptedNamespaceKeyDraft.encrypted_private_key_data.validator._redact = bv.BlotRedactor(None)
EncryptedNamespaceKeyDraft._all_field_names_ = set([
    'encrypting_key_id',
    'encrypted_private_key_data'])
EncryptedNamespaceKeyDraft._all_fields_ = [
    ('encrypting_key_id', EncryptedNamespaceKeyDraft.encrypting_key_id.validator),
    ('encrypted_private_key_data', EncryptedNamespaceKeyDraft.encrypted_private_key_data.validator)]
EncryptedTeamKey.team_key_id.validator = bv.String()
EncryptedTeamKey.team_key_id.validator._redact = bv.BlotRedactor(None)
EncryptedTeamKey.encrypted_private_key_data.validator = bv.Bytes()
EncryptedTeamKey.encrypted_private_key_data.validator._redact = bv.BlotRedactor(None)
EncryptedTeamKey.encrypting_key_id.validator = bv.String()
EncryptedTeamKey.encrypting_key_id.validator._redact = bv.BlotRedactor(None)
EncryptedTeamKey._all_field_names_ = set([
    'team_key_id',
    'encrypted_private_key_data',
    'encrypting_key_id'])
EncryptedTeamKey._all_fields_ = [
    ('team_key_id', EncryptedTeamKey.team_key_id.validator),
    ('encrypted_private_key_data', EncryptedTeamKey.encrypted_private_key_data.validator),
    ('encrypting_key_id', EncryptedTeamKey.encrypting_key_id.validator)]
EncryptedTeamKeyDraft.encrypting_key_id.validator = bv.String()
EncryptedTeamKeyDraft.encrypting_key_id.validator._redact = bv.BlotRedactor(None)
EncryptedTeamKeyDraft.encrypted_private_key_data.validator = bv.Bytes()
EncryptedTeamKeyDraft.encrypted_private_key_data.validator._redact = bv.BlotRedactor(None)
EncryptedTeamKeyDraft._all_field_names_ = set([
    'encrypting_key_id',
    'encrypted_private_key_data'])
EncryptedTeamKeyDraft._all_fields_ = [
    ('encrypting_key_id', EncryptedTeamKeyDraft.encrypting_key_id.validator),
    ('encrypted_private_key_data', EncryptedTeamKeyDraft.encrypted_private_key_data.validator)]
EnrollBackupKeyForTeamArg.backup_key_id.validator = bv.String()
EnrollBackupKeyForTeamArg.backup_key_id.validator._redact = bv.BlotRedactor(None)
EnrollBackupKeyForTeamArg.encrypted_team_keys.validator = bv.Nullable(bv.List(EncryptedTeamKey_validator))
EnrollBackupKeyForTeamArg._all_field_names_ = set([
    'backup_key_id',
    'encrypted_team_keys'])
EnrollBackupKeyForTeamArg._all_fields_ = [
    ('backup_key_id', EnrollBackupKeyForTeamArg.backup_key_id.validator),
    ('encrypted_team_keys', EnrollBackupKeyForTeamArg.encrypted_team_keys.validator)]
EnrollBackupKeyForTeamError._permission_denied_validator = bv.Void()
EnrollBackupKeyForTeamError._missing_arguments_validator = bv.Void()
EnrollBackupKeyForTeamError._backup_key_not_found_validator = bv.Void()
EnrollBackupKeyForTeamError._backup_key_already_enrolled_validator = bv.Void()
EnrollBackupKeyForTeamError._team_enrollment_not_yet_finished_validator = bv.Void()
EnrollBackupKeyForTeamError._multiple_encrypting_keys_not_supported_validator = bv.Void()
EnrollBackupKeyForTeamError._team_key_not_found_validator = bv.Void()
EnrollBackupKeyForTeamError._wrong_id_length_validator = bv.Void()
EnrollBackupKeyForTeamError._wrong_key_length_validator = bv.Void()
EnrollBackupKeyForTeamError._other_validator = bv.Void()
EnrollBackupKeyForTeamError._tagmap = {
    'permission_denied': EnrollBackupKeyForTeamError._permission_denied_validator,
    'missing_arguments': EnrollBackupKeyForTeamError._missing_arguments_validator,
    'backup_key_not_found': EnrollBackupKeyForTeamError._backup_key_not_found_validator,
    'backup_key_already_enrolled': EnrollBackupKeyForTeamError._backup_key_already_enrolled_validator,
    'team_enrollment_not_yet_finished': EnrollBackupKeyForTeamError._team_enrollment_not_yet_finished_validator,
    'multiple_encrypting_keys_not_supported': EnrollBackupKeyForTeamError._multiple_encrypting_keys_not_supported_validator,
    'team_key_not_found': EnrollBackupKeyForTeamError._team_key_not_found_validator,
    'wrong_id_length': EnrollBackupKeyForTeamError._wrong_id_length_validator,
    'wrong_key_length': EnrollBackupKeyForTeamError._wrong_key_length_validator,
    'other': EnrollBackupKeyForTeamError._other_validator }
EnrollBackupKeyForTeamError.permission_denied = EnrollBackupKeyForTeamError('permission_denied')
EnrollBackupKeyForTeamError.missing_arguments = EnrollBackupKeyForTeamError('missing_arguments')
EnrollBackupKeyForTeamError.backup_key_not_found = EnrollBackupKeyForTeamError('backup_key_not_found')
EnrollBackupKeyForTeamError.backup_key_already_enrolled = EnrollBackupKeyForTeamError('backup_key_already_enrolled')
EnrollBackupKeyForTeamError.team_enrollment_not_yet_finished = EnrollBackupKeyForTeamError('team_enrollment_not_yet_finished')
EnrollBackupKeyForTeamError.multiple_encrypting_keys_not_supported = EnrollBackupKeyForTeamError('multiple_encrypting_keys_not_supported')
EnrollBackupKeyForTeamError.team_key_not_found = EnrollBackupKeyForTeamError('team_key_not_found')
EnrollBackupKeyForTeamError.wrong_id_length = EnrollBackupKeyForTeamError('wrong_id_length')
EnrollBackupKeyForTeamError.wrong_key_length = EnrollBackupKeyForTeamError('wrong_key_length')
EnrollBackupKeyForTeamError.other = EnrollBackupKeyForTeamError('other')
EnrollClientsArg.encrypted_team_keys.validator = bv.Nullable(bv.List(EncryptedTeamKey_validator))
EnrollClientsArg._all_field_names_ = set([
    'encrypted_team_keys'])
EnrollClientsArg._all_fields_ = [
    ('encrypted_team_keys', EnrollClientsArg.encrypted_team_keys.validator)]
EnrollClientsError._permission_denied_validator = bv.Void()
EnrollClientsError._missing_arguments_validator = bv.Void()
EnrollClientsError._team_key_not_found_validator = bv.Void()
EnrollClientsError._client_key_not_found_validator = bv.Void()
EnrollClientsError._team_key_missing_validator = bv.Void()
EnrollClientsError._other_validator = bv.Void()
EnrollClientsError._tagmap = {
    'permission_denied': EnrollClientsError._permission_denied_validator,
    'missing_arguments': EnrollClientsError._missing_arguments_validator,
    'team_key_not_found': EnrollClientsError._team_key_not_found_validator,
    'client_key_not_found': EnrollClientsError._client_key_not_found_validator,
    'team_key_missing': EnrollClientsError._team_key_missing_validator,
    'other': EnrollClientsError._other_validator }
EnrollClientsError.permission_denied = EnrollClientsError('permission_denied')
EnrollClientsError.missing_arguments = EnrollClientsError('missing_arguments')
EnrollClientsError.team_key_not_found = EnrollClientsError('team_key_not_found')
EnrollClientsError.client_key_not_found = EnrollClientsError('client_key_not_found')
EnrollClientsError.team_key_missing = EnrollClientsError('team_key_missing')
EnrollClientsError.other = EnrollClientsError('other')
EnrollTeamArg.team_key_pair.validator = bv.Nullable(EncryptedKeyPairDraft_validator)
EnrollTeamArg.encrypting_backup_key_id.validator = bv.String()
EnrollTeamArg.encrypting_backup_key_id.validator._redact = bv.BlotRedactor(None)
EnrollTeamArg._all_field_names_ = set([
    'team_key_pair',
    'encrypting_backup_key_id'])
EnrollTeamArg._all_fields_ = [
    ('team_key_pair', EnrollTeamArg.team_key_pair.validator),
    ('encrypting_backup_key_id', EnrollTeamArg.encrypting_backup_key_id.validator)]
EnrollTeamError._permission_denied_validator = bv.Void()
EnrollTeamError._missing_arguments_validator = bv.Void()
EnrollTeamError._team_key_already_exists_validator = bv.Void()
EnrollTeamError._feature_disabled_validator = bv.Void()
EnrollTeamError._backup_key_not_found_validator = bv.Void()
EnrollTeamError._backup_key_already_enrolled_validator = bv.Void()
EnrollTeamError._invalid_algorithm_validator = bv.Void()
EnrollTeamError._wrong_id_length_validator = bv.Void()
EnrollTeamError._wrong_key_length_validator = bv.Void()
EnrollTeamError._other_validator = bv.Void()
EnrollTeamError._tagmap = {
    'permission_denied': EnrollTeamError._permission_denied_validator,
    'missing_arguments': EnrollTeamError._missing_arguments_validator,
    'team_key_already_exists': EnrollTeamError._team_key_already_exists_validator,
    'feature_disabled': EnrollTeamError._feature_disabled_validator,
    'backup_key_not_found': EnrollTeamError._backup_key_not_found_validator,
    'backup_key_already_enrolled': EnrollTeamError._backup_key_already_enrolled_validator,
    'invalid_algorithm': EnrollTeamError._invalid_algorithm_validator,
    'wrong_id_length': EnrollTeamError._wrong_id_length_validator,
    'wrong_key_length': EnrollTeamError._wrong_key_length_validator,
    'other': EnrollTeamError._other_validator }
EnrollTeamError.permission_denied = EnrollTeamError('permission_denied')
EnrollTeamError.missing_arguments = EnrollTeamError('missing_arguments')
EnrollTeamError.team_key_already_exists = EnrollTeamError('team_key_already_exists')
EnrollTeamError.feature_disabled = EnrollTeamError('feature_disabled')
EnrollTeamError.backup_key_not_found = EnrollTeamError('backup_key_not_found')
EnrollTeamError.backup_key_already_enrolled = EnrollTeamError('backup_key_already_enrolled')
EnrollTeamError.invalid_algorithm = EnrollTeamError('invalid_algorithm')
EnrollTeamError.wrong_id_length = EnrollTeamError('wrong_id_length')
EnrollTeamError.wrong_key_length = EnrollTeamError('wrong_key_length')
EnrollTeamError.other = EnrollTeamError('other')
EnrollTeamKeyDraftForBackupKeysArg.encrypted_team_keys.validator = bv.Nullable(bv.List(EncryptedTeamKey_validator))
EnrollTeamKeyDraftForBackupKeysArg._all_field_names_ = set([
    'encrypted_team_keys'])
EnrollTeamKeyDraftForBackupKeysArg._all_fields_ = [
    ('encrypted_team_keys', EnrollTeamKeyDraftForBackupKeysArg.encrypted_team_keys.validator)]
EnrollTeamKeyDraftForBackupKeysError._permission_denied_validator = bv.Void()
EnrollTeamKeyDraftForBackupKeysError._missing_arguments_validator = bv.Void()
EnrollTeamKeyDraftForBackupKeysError._wrong_key_length_validator = bv.Void()
EnrollTeamKeyDraftForBackupKeysError._multiple_team_keys_not_supported_validator = bv.Void()
EnrollTeamKeyDraftForBackupKeysError._team_key_not_found_validator = bv.Void()
EnrollTeamKeyDraftForBackupKeysError._team_key_not_draft_validator = bv.Void()
EnrollTeamKeyDraftForBackupKeysError._backup_key_not_found_validator = bv.Void()
EnrollTeamKeyDraftForBackupKeysError._wrong_id_length_validator = bv.Void()
EnrollTeamKeyDraftForBackupKeysError._other_validator = bv.Void()
EnrollTeamKeyDraftForBackupKeysError._tagmap = {
    'permission_denied': EnrollTeamKeyDraftForBackupKeysError._permission_denied_validator,
    'missing_arguments': EnrollTeamKeyDraftForBackupKeysError._missing_arguments_validator,
    'wrong_key_length': EnrollTeamKeyDraftForBackupKeysError._wrong_key_length_validator,
    'multiple_team_keys_not_supported': EnrollTeamKeyDraftForBackupKeysError._multiple_team_keys_not_supported_validator,
    'team_key_not_found': EnrollTeamKeyDraftForBackupKeysError._team_key_not_found_validator,
    'team_key_not_draft': EnrollTeamKeyDraftForBackupKeysError._team_key_not_draft_validator,
    'backup_key_not_found': EnrollTeamKeyDraftForBackupKeysError._backup_key_not_found_validator,
    'wrong_id_length': EnrollTeamKeyDraftForBackupKeysError._wrong_id_length_validator,
    'other': EnrollTeamKeyDraftForBackupKeysError._other_validator }
EnrollTeamKeyDraftForBackupKeysError.permission_denied = EnrollTeamKeyDraftForBackupKeysError('permission_denied')
EnrollTeamKeyDraftForBackupKeysError.missing_arguments = EnrollTeamKeyDraftForBackupKeysError('missing_arguments')
EnrollTeamKeyDraftForBackupKeysError.wrong_key_length = EnrollTeamKeyDraftForBackupKeysError('wrong_key_length')
EnrollTeamKeyDraftForBackupKeysError.multiple_team_keys_not_supported = EnrollTeamKeyDraftForBackupKeysError('multiple_team_keys_not_supported')
EnrollTeamKeyDraftForBackupKeysError.team_key_not_found = EnrollTeamKeyDraftForBackupKeysError('team_key_not_found')
EnrollTeamKeyDraftForBackupKeysError.team_key_not_draft = EnrollTeamKeyDraftForBackupKeysError('team_key_not_draft')
EnrollTeamKeyDraftForBackupKeysError.backup_key_not_found = EnrollTeamKeyDraftForBackupKeysError('backup_key_not_found')
EnrollTeamKeyDraftForBackupKeysError.wrong_id_length = EnrollTeamKeyDraftForBackupKeysError('wrong_id_length')
EnrollTeamKeyDraftForBackupKeysError.other = EnrollTeamKeyDraftForBackupKeysError('other')
EnrollTeamKeyDraftForBackupKeysResponse.not_found_backup_key_ids.validator = bv.Nullable(bv.List(bv.String()))
EnrollTeamKeyDraftForBackupKeysResponse.not_found_backup_key_ids.validator._redact = bv.BlotRedactor(None)
EnrollTeamKeyDraftForBackupKeysResponse._all_field_names_ = set([
    'not_found_backup_key_ids'])
EnrollTeamKeyDraftForBackupKeysResponse._all_fields_ = [
    ('not_found_backup_key_ids', EnrollTeamKeyDraftForBackupKeysResponse.not_found_backup_key_ids.validator)]
EnrollTeamKeyDraftForClientKeysArg.encrypted_team_keys.validator = bv.Nullable(bv.List(EncryptedTeamKey_validator))
EnrollTeamKeyDraftForClientKeysArg._all_field_names_ = set([
    'encrypted_team_keys'])
EnrollTeamKeyDraftForClientKeysArg._all_fields_ = [
    ('encrypted_team_keys', EnrollTeamKeyDraftForClientKeysArg.encrypted_team_keys.validator)]
EnrollTeamKeyDraftForClientKeysError._permission_denied_validator = bv.Void()
EnrollTeamKeyDraftForClientKeysError._missing_arguments_validator = bv.Void()
EnrollTeamKeyDraftForClientKeysError._wrong_key_length_validator = bv.Void()
EnrollTeamKeyDraftForClientKeysError._multiple_team_keys_not_supported_validator = bv.Void()
EnrollTeamKeyDraftForClientKeysError._team_key_not_found_validator = bv.Void()
EnrollTeamKeyDraftForClientKeysError._team_key_does_not_belong_to_users_team_validator = bv.Void()
EnrollTeamKeyDraftForClientKeysError._team_key_not_draft_validator = bv.Void()
EnrollTeamKeyDraftForClientKeysError._client_key_not_found_validator = bv.Void()
EnrollTeamKeyDraftForClientKeysError._wrong_id_length_validator = bv.Void()
EnrollTeamKeyDraftForClientKeysError._other_validator = bv.Void()
EnrollTeamKeyDraftForClientKeysError._tagmap = {
    'permission_denied': EnrollTeamKeyDraftForClientKeysError._permission_denied_validator,
    'missing_arguments': EnrollTeamKeyDraftForClientKeysError._missing_arguments_validator,
    'wrong_key_length': EnrollTeamKeyDraftForClientKeysError._wrong_key_length_validator,
    'multiple_team_keys_not_supported': EnrollTeamKeyDraftForClientKeysError._multiple_team_keys_not_supported_validator,
    'team_key_not_found': EnrollTeamKeyDraftForClientKeysError._team_key_not_found_validator,
    'team_key_does_not_belong_to_users_team': EnrollTeamKeyDraftForClientKeysError._team_key_does_not_belong_to_users_team_validator,
    'team_key_not_draft': EnrollTeamKeyDraftForClientKeysError._team_key_not_draft_validator,
    'client_key_not_found': EnrollTeamKeyDraftForClientKeysError._client_key_not_found_validator,
    'wrong_id_length': EnrollTeamKeyDraftForClientKeysError._wrong_id_length_validator,
    'other': EnrollTeamKeyDraftForClientKeysError._other_validator }
EnrollTeamKeyDraftForClientKeysError.permission_denied = EnrollTeamKeyDraftForClientKeysError('permission_denied')
EnrollTeamKeyDraftForClientKeysError.missing_arguments = EnrollTeamKeyDraftForClientKeysError('missing_arguments')
EnrollTeamKeyDraftForClientKeysError.wrong_key_length = EnrollTeamKeyDraftForClientKeysError('wrong_key_length')
EnrollTeamKeyDraftForClientKeysError.multiple_team_keys_not_supported = EnrollTeamKeyDraftForClientKeysError('multiple_team_keys_not_supported')
EnrollTeamKeyDraftForClientKeysError.team_key_not_found = EnrollTeamKeyDraftForClientKeysError('team_key_not_found')
EnrollTeamKeyDraftForClientKeysError.team_key_does_not_belong_to_users_team = EnrollTeamKeyDraftForClientKeysError('team_key_does_not_belong_to_users_team')
EnrollTeamKeyDraftForClientKeysError.team_key_not_draft = EnrollTeamKeyDraftForClientKeysError('team_key_not_draft')
EnrollTeamKeyDraftForClientKeysError.client_key_not_found = EnrollTeamKeyDraftForClientKeysError('client_key_not_found')
EnrollTeamKeyDraftForClientKeysError.wrong_id_length = EnrollTeamKeyDraftForClientKeysError('wrong_id_length')
EnrollTeamKeyDraftForClientKeysError.other = EnrollTeamKeyDraftForClientKeysError('other')
EnrollTeamKeyDraftForClientKeysResponse.not_found_client_key_ids.validator = bv.Nullable(bv.List(bv.String()))
EnrollTeamKeyDraftForClientKeysResponse.not_found_client_key_ids.validator._redact = bv.BlotRedactor(None)
EnrollTeamKeyDraftForClientKeysResponse._all_field_names_ = set([
    'not_found_client_key_ids'])
EnrollTeamKeyDraftForClientKeysResponse._all_fields_ = [
    ('not_found_client_key_ids', EnrollTeamKeyDraftForClientKeysResponse.not_found_client_key_ids.validator)]
EnrollTeamResponse.team_key.validator = bv.Nullable(PublicKey_validator)
EnrollTeamResponse._all_field_names_ = set([
    'team_key'])
EnrollTeamResponse._all_fields_ = [
    ('team_key', EnrollTeamResponse.team_key.validator)]
GetBackupKeysArg.selected_backup_keys.validator = bv.Nullable(SelectedBackupKeys_validator)
GetBackupKeysArg._all_field_names_ = set([
    'selected_backup_keys'])
GetBackupKeysArg._all_fields_ = [
    ('selected_backup_keys', GetBackupKeysArg.selected_backup_keys.validator)]
GetBackupKeysError._permission_denied_validator = bv.Void()
GetBackupKeysError._backup_key_does_not_belong_to_users_team_validator = bv.Void()
GetBackupKeysError._other_validator = bv.Void()
GetBackupKeysError._tagmap = {
    'permission_denied': GetBackupKeysError._permission_denied_validator,
    'backup_key_does_not_belong_to_users_team': GetBackupKeysError._backup_key_does_not_belong_to_users_team_validator,
    'other': GetBackupKeysError._other_validator }
GetBackupKeysError.permission_denied = GetBackupKeysError('permission_denied')
GetBackupKeysError.backup_key_does_not_belong_to_users_team = GetBackupKeysError('backup_key_does_not_belong_to_users_team')
GetBackupKeysError.other = GetBackupKeysError('other')
GetBackupKeysResponse.backup_keys.validator = bv.Nullable(bv.List(BackupKey_validator))
GetBackupKeysResponse.failed_backup_keys.validator = bv.Nullable(bv.List(bv.String()))
GetBackupKeysResponse.failed_backup_keys.validator._redact = bv.BlotRedactor(None)
GetBackupKeysResponse._all_field_names_ = set([
    'backup_keys',
    'failed_backup_keys'])
GetBackupKeysResponse._all_fields_ = [
    ('backup_keys', GetBackupKeysResponse.backup_keys.validator),
    ('failed_backup_keys', GetBackupKeysResponse.failed_backup_keys.validator)]
GetClientKeyEnrollmentStatusArg.client_key_id.validator = bv.String()
GetClientKeyEnrollmentStatusArg.client_key_id.validator._redact = bv.BlotRedactor(None)
GetClientKeyEnrollmentStatusArg._all_field_names_ = set([
    'client_key_id'])
GetClientKeyEnrollmentStatusArg._all_fields_ = [
    ('client_key_id', GetClientKeyEnrollmentStatusArg.client_key_id.validator)]
GetClientKeyEnrollmentStatusError._permission_denied_validator = bv.Void()
GetClientKeyEnrollmentStatusError._not_team_member_validator = bv.Void()
GetClientKeyEnrollmentStatusError._other_validator = bv.Void()
GetClientKeyEnrollmentStatusError._tagmap = {
    'permission_denied': GetClientKeyEnrollmentStatusError._permission_denied_validator,
    'not_team_member': GetClientKeyEnrollmentStatusError._not_team_member_validator,
    'other': GetClientKeyEnrollmentStatusError._other_validator }
GetClientKeyEnrollmentStatusError.permission_denied = GetClientKeyEnrollmentStatusError('permission_denied')
GetClientKeyEnrollmentStatusError.not_team_member = GetClientKeyEnrollmentStatusError('not_team_member')
GetClientKeyEnrollmentStatusError.other = GetClientKeyEnrollmentStatusError('other')
GetClientKeyEnrollmentStatusResponse.enrollment_status.validator = ClientKeyEnrollmentStatus_validator
GetClientKeyEnrollmentStatusResponse._all_field_names_ = set([
    'enrollment_status'])
GetClientKeyEnrollmentStatusResponse._all_fields_ = [
    ('enrollment_status', GetClientKeyEnrollmentStatusResponse.enrollment_status.validator)]
GetEncryptedDraftTeamKeyWithBackupKeyArg.backup_key_id.validator = bv.String()
GetEncryptedDraftTeamKeyWithBackupKeyArg.backup_key_id.validator._redact = bv.BlotRedactor(None)
GetEncryptedDraftTeamKeyWithBackupKeyArg._all_field_names_ = set([
    'backup_key_id'])
GetEncryptedDraftTeamKeyWithBackupKeyArg._all_fields_ = [
    ('backup_key_id', GetEncryptedDraftTeamKeyWithBackupKeyArg.backup_key_id.validator)]
GetEncryptedDraftTeamKeyWithBackupKeyError._permission_denied_validator = bv.Void()
GetEncryptedDraftTeamKeyWithBackupKeyError._missing_arguments_validator = bv.Void()
GetEncryptedDraftTeamKeyWithBackupKeyError._backup_key_not_found_validator = bv.Void()
GetEncryptedDraftTeamKeyWithBackupKeyError._backup_key_not_enrolled_validator = bv.Void()
GetEncryptedDraftTeamKeyWithBackupKeyError._team_key_not_found_validator = bv.Void()
GetEncryptedDraftTeamKeyWithBackupKeyError._team_key_not_encrypted_with_backup_key_validator = bv.Void()
GetEncryptedDraftTeamKeyWithBackupKeyError._backup_key_does_not_belong_to_users_team_validator = bv.Void()
GetEncryptedDraftTeamKeyWithBackupKeyError._other_validator = bv.Void()
GetEncryptedDraftTeamKeyWithBackupKeyError._tagmap = {
    'permission_denied': GetEncryptedDraftTeamKeyWithBackupKeyError._permission_denied_validator,
    'missing_arguments': GetEncryptedDraftTeamKeyWithBackupKeyError._missing_arguments_validator,
    'backup_key_not_found': GetEncryptedDraftTeamKeyWithBackupKeyError._backup_key_not_found_validator,
    'backup_key_not_enrolled': GetEncryptedDraftTeamKeyWithBackupKeyError._backup_key_not_enrolled_validator,
    'team_key_not_found': GetEncryptedDraftTeamKeyWithBackupKeyError._team_key_not_found_validator,
    'team_key_not_encrypted_with_backup_key': GetEncryptedDraftTeamKeyWithBackupKeyError._team_key_not_encrypted_with_backup_key_validator,
    'backup_key_does_not_belong_to_users_team': GetEncryptedDraftTeamKeyWithBackupKeyError._backup_key_does_not_belong_to_users_team_validator,
    'other': GetEncryptedDraftTeamKeyWithBackupKeyError._other_validator }
GetEncryptedDraftTeamKeyWithBackupKeyError.permission_denied = GetEncryptedDraftTeamKeyWithBackupKeyError('permission_denied')
GetEncryptedDraftTeamKeyWithBackupKeyError.missing_arguments = GetEncryptedDraftTeamKeyWithBackupKeyError('missing_arguments')
GetEncryptedDraftTeamKeyWithBackupKeyError.backup_key_not_found = GetEncryptedDraftTeamKeyWithBackupKeyError('backup_key_not_found')
GetEncryptedDraftTeamKeyWithBackupKeyError.backup_key_not_enrolled = GetEncryptedDraftTeamKeyWithBackupKeyError('backup_key_not_enrolled')
GetEncryptedDraftTeamKeyWithBackupKeyError.team_key_not_found = GetEncryptedDraftTeamKeyWithBackupKeyError('team_key_not_found')
GetEncryptedDraftTeamKeyWithBackupKeyError.team_key_not_encrypted_with_backup_key = GetEncryptedDraftTeamKeyWithBackupKeyError('team_key_not_encrypted_with_backup_key')
GetEncryptedDraftTeamKeyWithBackupKeyError.backup_key_does_not_belong_to_users_team = GetEncryptedDraftTeamKeyWithBackupKeyError('backup_key_does_not_belong_to_users_team')
GetEncryptedDraftTeamKeyWithBackupKeyError.other = GetEncryptedDraftTeamKeyWithBackupKeyError('other')
GetEncryptedDraftTeamKeyWithBackupKeyResponse.encrypted_team_key.validator = bv.Nullable(EncryptedKeyPair_validator)
GetEncryptedDraftTeamKeyWithBackupKeyResponse._all_field_names_ = set([
    'encrypted_team_key'])
GetEncryptedDraftTeamKeyWithBackupKeyResponse._all_fields_ = [
    ('encrypted_team_key', GetEncryptedDraftTeamKeyWithBackupKeyResponse.encrypted_team_key.validator)]
GetEncryptedTeamKeyListWithBackupKeyArg.backup_key_id.validator = bv.String()
GetEncryptedTeamKeyListWithBackupKeyArg.backup_key_id.validator._redact = bv.BlotRedactor(None)
GetEncryptedTeamKeyListWithBackupKeyArg._all_field_names_ = set([
    'backup_key_id'])
GetEncryptedTeamKeyListWithBackupKeyArg._all_fields_ = [
    ('backup_key_id', GetEncryptedTeamKeyListWithBackupKeyArg.backup_key_id.validator)]
GetEncryptedTeamKeyListWithBackupKeyError._permission_denied_validator = bv.Void()
GetEncryptedTeamKeyListWithBackupKeyError._missing_arguments_validator = bv.Void()
GetEncryptedTeamKeyListWithBackupKeyError._backup_key_not_found_validator = bv.Void()
GetEncryptedTeamKeyListWithBackupKeyError._encrypted_team_key_not_found_validator = bv.Void()
GetEncryptedTeamKeyListWithBackupKeyError._backup_key_not_enrolled_validator = bv.Void()
GetEncryptedTeamKeyListWithBackupKeyError._backup_key_does_not_belong_to_users_team_validator = bv.Void()
GetEncryptedTeamKeyListWithBackupKeyError._other_validator = bv.Void()
GetEncryptedTeamKeyListWithBackupKeyError._tagmap = {
    'permission_denied': GetEncryptedTeamKeyListWithBackupKeyError._permission_denied_validator,
    'missing_arguments': GetEncryptedTeamKeyListWithBackupKeyError._missing_arguments_validator,
    'backup_key_not_found': GetEncryptedTeamKeyListWithBackupKeyError._backup_key_not_found_validator,
    'encrypted_team_key_not_found': GetEncryptedTeamKeyListWithBackupKeyError._encrypted_team_key_not_found_validator,
    'backup_key_not_enrolled': GetEncryptedTeamKeyListWithBackupKeyError._backup_key_not_enrolled_validator,
    'backup_key_does_not_belong_to_users_team': GetEncryptedTeamKeyListWithBackupKeyError._backup_key_does_not_belong_to_users_team_validator,
    'other': GetEncryptedTeamKeyListWithBackupKeyError._other_validator }
GetEncryptedTeamKeyListWithBackupKeyError.permission_denied = GetEncryptedTeamKeyListWithBackupKeyError('permission_denied')
GetEncryptedTeamKeyListWithBackupKeyError.missing_arguments = GetEncryptedTeamKeyListWithBackupKeyError('missing_arguments')
GetEncryptedTeamKeyListWithBackupKeyError.backup_key_not_found = GetEncryptedTeamKeyListWithBackupKeyError('backup_key_not_found')
GetEncryptedTeamKeyListWithBackupKeyError.encrypted_team_key_not_found = GetEncryptedTeamKeyListWithBackupKeyError('encrypted_team_key_not_found')
GetEncryptedTeamKeyListWithBackupKeyError.backup_key_not_enrolled = GetEncryptedTeamKeyListWithBackupKeyError('backup_key_not_enrolled')
GetEncryptedTeamKeyListWithBackupKeyError.backup_key_does_not_belong_to_users_team = GetEncryptedTeamKeyListWithBackupKeyError('backup_key_does_not_belong_to_users_team')
GetEncryptedTeamKeyListWithBackupKeyError.other = GetEncryptedTeamKeyListWithBackupKeyError('other')
GetEncryptedTeamKeyListWithBackupKeyResponse.encrypted_team_keys.validator = bv.Nullable(bv.List(EncryptedKeyPair_validator))
GetEncryptedTeamKeyListWithBackupKeyResponse._all_field_names_ = set([
    'encrypted_team_keys'])
GetEncryptedTeamKeyListWithBackupKeyResponse._all_fields_ = [
    ('encrypted_team_keys', GetEncryptedTeamKeyListWithBackupKeyResponse.encrypted_team_keys.validator)]
GetEncryptedTeamKeyListWithClientKeyArg.client_key_id.validator = bv.String()
GetEncryptedTeamKeyListWithClientKeyArg.client_key_id.validator._redact = bv.BlotRedactor(None)
GetEncryptedTeamKeyListWithClientKeyArg._all_field_names_ = set([
    'client_key_id'])
GetEncryptedTeamKeyListWithClientKeyArg._all_fields_ = [
    ('client_key_id', GetEncryptedTeamKeyListWithClientKeyArg.client_key_id.validator)]
GetEncryptedTeamKeyListWithClientKeyError._permission_denied_validator = bv.Void()
GetEncryptedTeamKeyListWithClientKeyError._missing_arguments_validator = bv.Void()
GetEncryptedTeamKeyListWithClientKeyError._client_key_not_found_validator = bv.Void()
GetEncryptedTeamKeyListWithClientKeyError._encrypted_team_key_not_found_validator = bv.Void()
GetEncryptedTeamKeyListWithClientKeyError._key_not_yet_enrolled_validator = bv.Void()
GetEncryptedTeamKeyListWithClientKeyError._other_validator = bv.Void()
GetEncryptedTeamKeyListWithClientKeyError._tagmap = {
    'permission_denied': GetEncryptedTeamKeyListWithClientKeyError._permission_denied_validator,
    'missing_arguments': GetEncryptedTeamKeyListWithClientKeyError._missing_arguments_validator,
    'client_key_not_found': GetEncryptedTeamKeyListWithClientKeyError._client_key_not_found_validator,
    'encrypted_team_key_not_found': GetEncryptedTeamKeyListWithClientKeyError._encrypted_team_key_not_found_validator,
    'key_not_yet_enrolled': GetEncryptedTeamKeyListWithClientKeyError._key_not_yet_enrolled_validator,
    'other': GetEncryptedTeamKeyListWithClientKeyError._other_validator }
GetEncryptedTeamKeyListWithClientKeyError.permission_denied = GetEncryptedTeamKeyListWithClientKeyError('permission_denied')
GetEncryptedTeamKeyListWithClientKeyError.missing_arguments = GetEncryptedTeamKeyListWithClientKeyError('missing_arguments')
GetEncryptedTeamKeyListWithClientKeyError.client_key_not_found = GetEncryptedTeamKeyListWithClientKeyError('client_key_not_found')
GetEncryptedTeamKeyListWithClientKeyError.encrypted_team_key_not_found = GetEncryptedTeamKeyListWithClientKeyError('encrypted_team_key_not_found')
GetEncryptedTeamKeyListWithClientKeyError.key_not_yet_enrolled = GetEncryptedTeamKeyListWithClientKeyError('key_not_yet_enrolled')
GetEncryptedTeamKeyListWithClientKeyError.other = GetEncryptedTeamKeyListWithClientKeyError('other')
GetEncryptedTeamKeyListWithClientKeyResponse.encrypted_team_keys.validator = bv.Nullable(bv.List(EncryptedKeyPair_validator))
GetEncryptedTeamKeyListWithClientKeyResponse._all_field_names_ = set([
    'encrypted_team_keys'])
GetEncryptedTeamKeyListWithClientKeyResponse._all_fields_ = [
    ('encrypted_team_keys', GetEncryptedTeamKeyListWithClientKeyResponse.encrypted_team_keys.validator)]
GetEncryptedTeamKeyWithClientKeyArg.client_key_id.validator = bv.String()
GetEncryptedTeamKeyWithClientKeyArg.client_key_id.validator._redact = bv.BlotRedactor(None)
GetEncryptedTeamKeyWithClientKeyArg._all_field_names_ = set([
    'client_key_id'])
GetEncryptedTeamKeyWithClientKeyArg._all_fields_ = [
    ('client_key_id', GetEncryptedTeamKeyWithClientKeyArg.client_key_id.validator)]
GetEncryptedTeamKeyWithClientKeyError._permission_denied_validator = bv.Void()
GetEncryptedTeamKeyWithClientKeyError._missing_arguments_validator = bv.Void()
GetEncryptedTeamKeyWithClientKeyError._client_key_not_found_validator = bv.Void()
GetEncryptedTeamKeyWithClientKeyError._encrypted_team_key_not_found_validator = bv.Void()
GetEncryptedTeamKeyWithClientKeyError._key_not_yet_enrolled_validator = bv.Void()
GetEncryptedTeamKeyWithClientKeyError._multiple_team_keys_not_supported_validator = bv.Void()
GetEncryptedTeamKeyWithClientKeyError._other_validator = bv.Void()
GetEncryptedTeamKeyWithClientKeyError._tagmap = {
    'permission_denied': GetEncryptedTeamKeyWithClientKeyError._permission_denied_validator,
    'missing_arguments': GetEncryptedTeamKeyWithClientKeyError._missing_arguments_validator,
    'client_key_not_found': GetEncryptedTeamKeyWithClientKeyError._client_key_not_found_validator,
    'encrypted_team_key_not_found': GetEncryptedTeamKeyWithClientKeyError._encrypted_team_key_not_found_validator,
    'key_not_yet_enrolled': GetEncryptedTeamKeyWithClientKeyError._key_not_yet_enrolled_validator,
    'multiple_team_keys_not_supported': GetEncryptedTeamKeyWithClientKeyError._multiple_team_keys_not_supported_validator,
    'other': GetEncryptedTeamKeyWithClientKeyError._other_validator }
GetEncryptedTeamKeyWithClientKeyError.permission_denied = GetEncryptedTeamKeyWithClientKeyError('permission_denied')
GetEncryptedTeamKeyWithClientKeyError.missing_arguments = GetEncryptedTeamKeyWithClientKeyError('missing_arguments')
GetEncryptedTeamKeyWithClientKeyError.client_key_not_found = GetEncryptedTeamKeyWithClientKeyError('client_key_not_found')
GetEncryptedTeamKeyWithClientKeyError.encrypted_team_key_not_found = GetEncryptedTeamKeyWithClientKeyError('encrypted_team_key_not_found')
GetEncryptedTeamKeyWithClientKeyError.key_not_yet_enrolled = GetEncryptedTeamKeyWithClientKeyError('key_not_yet_enrolled')
GetEncryptedTeamKeyWithClientKeyError.multiple_team_keys_not_supported = GetEncryptedTeamKeyWithClientKeyError('multiple_team_keys_not_supported')
GetEncryptedTeamKeyWithClientKeyError.other = GetEncryptedTeamKeyWithClientKeyError('other')
GetEncryptedTeamKeyWithClientKeyResponse.encrypted_team_key.validator = bv.Nullable(EncryptedKeyPair_validator)
GetEncryptedTeamKeyWithClientKeyResponse._all_field_names_ = set([
    'encrypted_team_key'])
GetEncryptedTeamKeyWithClientKeyResponse._all_fields_ = [
    ('encrypted_team_key', GetEncryptedTeamKeyWithClientKeyResponse.encrypted_team_key.validator)]
GetFileKeysArg.root_key_id.validator = bv.String()
GetFileKeysArg.root_key_id.validator._redact = bv.BlotRedactor(None)
GetFileKeysArg.file_key_ids.validator = bv.Nullable(bv.List(bv.String()))
GetFileKeysArg.file_key_ids.validator._redact = bv.BlotRedactor(None)
GetFileKeysArg._all_field_names_ = set([
    'root_key_id',
    'file_key_ids'])
GetFileKeysArg._all_fields_ = [
    ('root_key_id', GetFileKeysArg.root_key_id.validator),
    ('file_key_ids', GetFileKeysArg.file_key_ids.validator)]
GetFileKeysError._permission_denied_validator = bv.Void()
GetFileKeysError._missing_arguments_validator = bv.Void()
GetFileKeysError._root_key_not_found_validator = bv.Void()
GetFileKeysError._file_key_not_found_validator = bv.Void()
GetFileKeysError._namespace_key_not_found_validator = bv.Void()
GetFileKeysError._no_chain_to_key_validator = bv.Void()
GetFileKeysError._key_not_yet_enrolled_validator = bv.Void()
GetFileKeysError._too_many_keys_validator = bv.Void()
GetFileKeysError._other_validator = bv.Void()
GetFileKeysError._tagmap = {
    'permission_denied': GetFileKeysError._permission_denied_validator,
    'missing_arguments': GetFileKeysError._missing_arguments_validator,
    'root_key_not_found': GetFileKeysError._root_key_not_found_validator,
    'file_key_not_found': GetFileKeysError._file_key_not_found_validator,
    'namespace_key_not_found': GetFileKeysError._namespace_key_not_found_validator,
    'no_chain_to_key': GetFileKeysError._no_chain_to_key_validator,
    'key_not_yet_enrolled': GetFileKeysError._key_not_yet_enrolled_validator,
    'too_many_keys': GetFileKeysError._too_many_keys_validator,
    'other': GetFileKeysError._other_validator }
GetFileKeysError.permission_denied = GetFileKeysError('permission_denied')
GetFileKeysError.missing_arguments = GetFileKeysError('missing_arguments')
GetFileKeysError.root_key_not_found = GetFileKeysError('root_key_not_found')
GetFileKeysError.file_key_not_found = GetFileKeysError('file_key_not_found')
GetFileKeysError.namespace_key_not_found = GetFileKeysError('namespace_key_not_found')
GetFileKeysError.no_chain_to_key = GetFileKeysError('no_chain_to_key')
GetFileKeysError.key_not_yet_enrolled = GetFileKeysError('key_not_yet_enrolled')
GetFileKeysError.too_many_keys = GetFileKeysError('too_many_keys')
GetFileKeysError.other = GetFileKeysError('other')
GetFileKeysResponse.encrypting_keys.validator = bv.Nullable(bv.List(EncryptedKeyPair_validator))
GetFileKeysResponse.file_keys.validator = bv.Nullable(bv.List(EncryptedFileKey_validator))
GetFileKeysResponse._all_field_names_ = set([
    'encrypting_keys',
    'file_keys'])
GetFileKeysResponse._all_fields_ = [
    ('encrypting_keys', GetFileKeysResponse.encrypting_keys.validator),
    ('file_keys', GetFileKeysResponse.file_keys.validator)]
GetNamespaceKeyArg.root_key_id.validator = bv.String()
GetNamespaceKeyArg.root_key_id.validator._redact = bv.BlotRedactor(None)
GetNamespaceKeyArg.ns_id.validator = bv.UInt64()
GetNamespaceKeyArg.ns_id.validator._redact = bv.BlotRedactor(None)
GetNamespaceKeyArg._all_field_names_ = set([
    'root_key_id',
    'ns_id'])
GetNamespaceKeyArg._all_fields_ = [
    ('root_key_id', GetNamespaceKeyArg.root_key_id.validator),
    ('ns_id', GetNamespaceKeyArg.ns_id.validator)]
GetNamespaceKeyError._permission_denied_validator = bv.Void()
GetNamespaceKeyError._missing_arguments_validator = bv.Void()
GetNamespaceKeyError._root_key_not_found_validator = bv.Void()
GetNamespaceKeyError._namespace_not_found_validator = bv.Void()
GetNamespaceKeyError._namespace_key_not_found_validator = bv.Void()
GetNamespaceKeyError._no_chain_to_key_validator = bv.Void()
GetNamespaceKeyError._key_not_yet_enrolled_validator = bv.Void()
GetNamespaceKeyError._other_validator = bv.Void()
GetNamespaceKeyError._tagmap = {
    'permission_denied': GetNamespaceKeyError._permission_denied_validator,
    'missing_arguments': GetNamespaceKeyError._missing_arguments_validator,
    'root_key_not_found': GetNamespaceKeyError._root_key_not_found_validator,
    'namespace_not_found': GetNamespaceKeyError._namespace_not_found_validator,
    'namespace_key_not_found': GetNamespaceKeyError._namespace_key_not_found_validator,
    'no_chain_to_key': GetNamespaceKeyError._no_chain_to_key_validator,
    'key_not_yet_enrolled': GetNamespaceKeyError._key_not_yet_enrolled_validator,
    'other': GetNamespaceKeyError._other_validator }
GetNamespaceKeyError.permission_denied = GetNamespaceKeyError('permission_denied')
GetNamespaceKeyError.missing_arguments = GetNamespaceKeyError('missing_arguments')
GetNamespaceKeyError.root_key_not_found = GetNamespaceKeyError('root_key_not_found')
GetNamespaceKeyError.namespace_not_found = GetNamespaceKeyError('namespace_not_found')
GetNamespaceKeyError.namespace_key_not_found = GetNamespaceKeyError('namespace_key_not_found')
GetNamespaceKeyError.no_chain_to_key = GetNamespaceKeyError('no_chain_to_key')
GetNamespaceKeyError.key_not_yet_enrolled = GetNamespaceKeyError('key_not_yet_enrolled')
GetNamespaceKeyError.other = GetNamespaceKeyError('other')
GetNamespaceKeyResponse.encrypted_keys.validator = bv.Nullable(bv.List(EncryptedKeyPair_validator))
GetNamespaceKeyResponse._all_field_names_ = set([
    'encrypted_keys'])
GetNamespaceKeyResponse._all_fields_ = [
    ('encrypted_keys', GetNamespaceKeyResponse.encrypted_keys.validator)]
GetNamespaceKeysArg.root_key_id.validator = bv.String()
GetNamespaceKeysArg.root_key_id.validator._redact = bv.BlotRedactor(None)
GetNamespaceKeysArg.ns_id.validator = bv.UInt64()
GetNamespaceKeysArg.ns_id.validator._redact = bv.BlotRedactor(None)
GetNamespaceKeysArg._all_field_names_ = set([
    'root_key_id',
    'ns_id'])
GetNamespaceKeysArg._all_fields_ = [
    ('root_key_id', GetNamespaceKeysArg.root_key_id.validator),
    ('ns_id', GetNamespaceKeysArg.ns_id.validator)]
GetNamespaceKeysError._permission_denied_validator = bv.Void()
GetNamespaceKeysError._missing_arguments_validator = bv.Void()
GetNamespaceKeysError._root_key_not_found_validator = bv.Void()
GetNamespaceKeysError._namespace_not_found_validator = bv.Void()
GetNamespaceKeysError._namespace_key_not_found_validator = bv.Void()
GetNamespaceKeysError._no_chain_to_key_validator = bv.Void()
GetNamespaceKeysError._key_not_yet_enrolled_validator = bv.Void()
GetNamespaceKeysError._other_validator = bv.Void()
GetNamespaceKeysError._tagmap = {
    'permission_denied': GetNamespaceKeysError._permission_denied_validator,
    'missing_arguments': GetNamespaceKeysError._missing_arguments_validator,
    'root_key_not_found': GetNamespaceKeysError._root_key_not_found_validator,
    'namespace_not_found': GetNamespaceKeysError._namespace_not_found_validator,
    'namespace_key_not_found': GetNamespaceKeysError._namespace_key_not_found_validator,
    'no_chain_to_key': GetNamespaceKeysError._no_chain_to_key_validator,
    'key_not_yet_enrolled': GetNamespaceKeysError._key_not_yet_enrolled_validator,
    'other': GetNamespaceKeysError._other_validator }
GetNamespaceKeysError.permission_denied = GetNamespaceKeysError('permission_denied')
GetNamespaceKeysError.missing_arguments = GetNamespaceKeysError('missing_arguments')
GetNamespaceKeysError.root_key_not_found = GetNamespaceKeysError('root_key_not_found')
GetNamespaceKeysError.namespace_not_found = GetNamespaceKeysError('namespace_not_found')
GetNamespaceKeysError.namespace_key_not_found = GetNamespaceKeysError('namespace_key_not_found')
GetNamespaceKeysError.no_chain_to_key = GetNamespaceKeysError('no_chain_to_key')
GetNamespaceKeysError.key_not_yet_enrolled = GetNamespaceKeysError('key_not_yet_enrolled')
GetNamespaceKeysError.other = GetNamespaceKeysError('other')
GetNamespaceKeysInfoArg.selected_namespace_keys.validator = bv.Nullable(SelectedNamespaceKeys_validator)
GetNamespaceKeysInfoArg._all_field_names_ = set([
    'selected_namespace_keys'])
GetNamespaceKeysInfoArg._all_fields_ = [
    ('selected_namespace_keys', GetNamespaceKeysInfoArg.selected_namespace_keys.validator)]
GetNamespaceKeysInfoError._permission_denied_validator = bv.Void()
GetNamespaceKeysInfoError._team_key_not_found_validator = bv.Void()
GetNamespaceKeysInfoError._namespace_key_not_found_validator = bv.Void()
GetNamespaceKeysInfoError._other_validator = bv.Void()
GetNamespaceKeysInfoError._tagmap = {
    'permission_denied': GetNamespaceKeysInfoError._permission_denied_validator,
    'team_key_not_found': GetNamespaceKeysInfoError._team_key_not_found_validator,
    'namespace_key_not_found': GetNamespaceKeysInfoError._namespace_key_not_found_validator,
    'other': GetNamespaceKeysInfoError._other_validator }
GetNamespaceKeysInfoError.permission_denied = GetNamespaceKeysInfoError('permission_denied')
GetNamespaceKeysInfoError.team_key_not_found = GetNamespaceKeysInfoError('team_key_not_found')
GetNamespaceKeysInfoError.namespace_key_not_found = GetNamespaceKeysInfoError('namespace_key_not_found')
GetNamespaceKeysInfoError.other = GetNamespaceKeysInfoError('other')
GetNamespaceKeysInfoResponse.encrypting_keys.validator = bv.Nullable(bv.List(PublicKey_validator))
GetNamespaceKeysInfoResponse.namespace_keys_info.validator = bv.Nullable(bv.List(NamespaceKeyInfo_validator))
GetNamespaceKeysInfoResponse.not_found_namespace_keys.validator = bv.Nullable(bv.List(bv.String()))
GetNamespaceKeysInfoResponse.not_found_namespace_keys.validator._redact = bv.BlotRedactor(None)
GetNamespaceKeysInfoResponse.active_team_key_id.validator = bv.String()
GetNamespaceKeysInfoResponse.active_team_key_id.validator._redact = bv.BlotRedactor(None)
GetNamespaceKeysInfoResponse._all_field_names_ = set([
    'encrypting_keys',
    'namespace_keys_info',
    'not_found_namespace_keys',
    'active_team_key_id'])
GetNamespaceKeysInfoResponse._all_fields_ = [
    ('encrypting_keys', GetNamespaceKeysInfoResponse.encrypting_keys.validator),
    ('namespace_keys_info', GetNamespaceKeysInfoResponse.namespace_keys_info.validator),
    ('not_found_namespace_keys', GetNamespaceKeysInfoResponse.not_found_namespace_keys.validator),
    ('active_team_key_id', GetNamespaceKeysInfoResponse.active_team_key_id.validator)]
GetNamespaceKeysResponse.encrypted_keys.validator = bv.Nullable(bv.List(EncryptedKeyPair_validator))
GetNamespaceKeysResponse._all_field_names_ = set([
    'encrypted_keys'])
GetNamespaceKeysResponse._all_fields_ = [
    ('encrypted_keys', GetNamespaceKeysResponse.encrypted_keys.validator)]
GetNamespacePublicKeyArg.ns_id.validator = bv.UInt64()
GetNamespacePublicKeyArg.ns_id.validator._redact = bv.BlotRedactor(None)
GetNamespacePublicKeyArg._all_field_names_ = set([
    'ns_id'])
GetNamespacePublicKeyArg._all_fields_ = [
    ('ns_id', GetNamespacePublicKeyArg.ns_id.validator)]
GetNamespacePublicKeyError._permission_denied_validator = bv.Void()
GetNamespacePublicKeyError._missing_arguments_validator = bv.Void()
GetNamespacePublicKeyError._namespace_not_found_validator = bv.Void()
GetNamespacePublicKeyError._namespace_key_not_found_validator = bv.Void()
GetNamespacePublicKeyError._other_validator = bv.Void()
GetNamespacePublicKeyError._tagmap = {
    'permission_denied': GetNamespacePublicKeyError._permission_denied_validator,
    'missing_arguments': GetNamespacePublicKeyError._missing_arguments_validator,
    'namespace_not_found': GetNamespacePublicKeyError._namespace_not_found_validator,
    'namespace_key_not_found': GetNamespacePublicKeyError._namespace_key_not_found_validator,
    'other': GetNamespacePublicKeyError._other_validator }
GetNamespacePublicKeyError.permission_denied = GetNamespacePublicKeyError('permission_denied')
GetNamespacePublicKeyError.missing_arguments = GetNamespacePublicKeyError('missing_arguments')
GetNamespacePublicKeyError.namespace_not_found = GetNamespacePublicKeyError('namespace_not_found')
GetNamespacePublicKeyError.namespace_key_not_found = GetNamespacePublicKeyError('namespace_key_not_found')
GetNamespacePublicKeyError.other = GetNamespacePublicKeyError('other')
GetNamespacePublicKeyResponse.namespace_key.validator = bv.Nullable(PublicKey_validator)
GetNamespacePublicKeyResponse._all_field_names_ = set([
    'namespace_key'])
GetNamespacePublicKeyResponse._all_fields_ = [
    ('namespace_key', GetNamespacePublicKeyResponse.namespace_key.validator)]
GetPendingClientsDetailsError._permission_denied_validator = bv.Void()
GetPendingClientsDetailsError._team_key_not_found_validator = bv.Void()
GetPendingClientsDetailsError._other_validator = bv.Void()
GetPendingClientsDetailsError._tagmap = {
    'permission_denied': GetPendingClientsDetailsError._permission_denied_validator,
    'team_key_not_found': GetPendingClientsDetailsError._team_key_not_found_validator,
    'other': GetPendingClientsDetailsError._other_validator }
GetPendingClientsDetailsError.permission_denied = GetPendingClientsDetailsError('permission_denied')
GetPendingClientsDetailsError.team_key_not_found = GetPendingClientsDetailsError('team_key_not_found')
GetPendingClientsDetailsError.other = GetPendingClientsDetailsError('other')
GetPendingClientsDetailsResponse.pending_clients.validator = bv.Nullable(bv.List(ClientDetails_validator))
GetPendingClientsDetailsResponse._all_field_names_ = set([
    'pending_clients'])
GetPendingClientsDetailsResponse._all_fields_ = [
    ('pending_clients', GetPendingClientsDetailsResponse.pending_clients.validator)]
GetPendingClientsError._permission_denied_validator = bv.Void()
GetPendingClientsError._team_key_not_found_validator = bv.Void()
GetPendingClientsError._other_validator = bv.Void()
GetPendingClientsError._tagmap = {
    'permission_denied': GetPendingClientsError._permission_denied_validator,
    'team_key_not_found': GetPendingClientsError._team_key_not_found_validator,
    'other': GetPendingClientsError._other_validator }
GetPendingClientsError.permission_denied = GetPendingClientsError('permission_denied')
GetPendingClientsError.team_key_not_found = GetPendingClientsError('team_key_not_found')
GetPendingClientsError.other = GetPendingClientsError('other')
GetPendingClientsResponse.client_public_keys.validator = bv.Nullable(bv.List(PublicKey_validator))
GetPendingClientsResponse.bolt_token.validator = bv.Nullable(BoltChannelToken_validator)
GetPendingClientsResponse._all_field_names_ = set([
    'client_public_keys',
    'bolt_token'])
GetPendingClientsResponse._all_fields_ = [
    ('client_public_keys', GetPendingClientsResponse.client_public_keys.validator),
    ('bolt_token', GetPendingClientsResponse.bolt_token.validator)]
GetRegisteredClientPublicKeysByIdArg.client_key_ids.validator = bv.Nullable(bv.List(bv.String()))
GetRegisteredClientPublicKeysByIdArg.client_key_ids.validator._redact = bv.BlotRedactor(None)
GetRegisteredClientPublicKeysByIdArg._all_field_names_ = set([
    'client_key_ids'])
GetRegisteredClientPublicKeysByIdArg._all_fields_ = [
    ('client_key_ids', GetRegisteredClientPublicKeysByIdArg.client_key_ids.validator)]
GetRegisteredClientPublicKeysByIdError._permission_denied_validator = bv.Void()
GetRegisteredClientPublicKeysByIdError._invalid_argument_validator = bv.Void()
GetRegisteredClientPublicKeysByIdError._team_key_not_found_validator = bv.Void()
GetRegisteredClientPublicKeysByIdError._client_key_does_not_belong_to_users_team_validator = bv.Void()
GetRegisteredClientPublicKeysByIdError._other_validator = bv.Void()
GetRegisteredClientPublicKeysByIdError._tagmap = {
    'permission_denied': GetRegisteredClientPublicKeysByIdError._permission_denied_validator,
    'invalid_argument': GetRegisteredClientPublicKeysByIdError._invalid_argument_validator,
    'team_key_not_found': GetRegisteredClientPublicKeysByIdError._team_key_not_found_validator,
    'client_key_does_not_belong_to_users_team': GetRegisteredClientPublicKeysByIdError._client_key_does_not_belong_to_users_team_validator,
    'other': GetRegisteredClientPublicKeysByIdError._other_validator }
GetRegisteredClientPublicKeysByIdError.permission_denied = GetRegisteredClientPublicKeysByIdError('permission_denied')
GetRegisteredClientPublicKeysByIdError.invalid_argument = GetRegisteredClientPublicKeysByIdError('invalid_argument')
GetRegisteredClientPublicKeysByIdError.team_key_not_found = GetRegisteredClientPublicKeysByIdError('team_key_not_found')
GetRegisteredClientPublicKeysByIdError.client_key_does_not_belong_to_users_team = GetRegisteredClientPublicKeysByIdError('client_key_does_not_belong_to_users_team')
GetRegisteredClientPublicKeysByIdError.other = GetRegisteredClientPublicKeysByIdError('other')
GetRegisteredClientPublicKeysByIdResponse.client_public_keys.validator = bv.Nullable(bv.List(PublicKey_validator))
GetRegisteredClientPublicKeysByIdResponse.failed_client_keys.validator = bv.Nullable(bv.List(bv.String()))
GetRegisteredClientPublicKeysByIdResponse.failed_client_keys.validator._redact = bv.BlotRedactor(None)
GetRegisteredClientPublicKeysByIdResponse._all_field_names_ = set([
    'client_public_keys',
    'failed_client_keys'])
GetRegisteredClientPublicKeysByIdResponse._all_fields_ = [
    ('client_public_keys', GetRegisteredClientPublicKeysByIdResponse.client_public_keys.validator),
    ('failed_client_keys', GetRegisteredClientPublicKeysByIdResponse.failed_client_keys.validator)]
GetRegisteredClientPublicKeysPagedArg.page_size.validator = bv.Nullable(bv.UInt64())
GetRegisteredClientPublicKeysPagedArg.page_token.validator = bv.Nullable(bv.String())
GetRegisteredClientPublicKeysPagedArg._all_field_names_ = set([
    'page_size',
    'page_token'])
GetRegisteredClientPublicKeysPagedArg._all_fields_ = [
    ('page_size', GetRegisteredClientPublicKeysPagedArg.page_size.validator),
    ('page_token', GetRegisteredClientPublicKeysPagedArg.page_token.validator)]
GetRegisteredClientPublicKeysPagedError._permission_denied_validator = bv.Void()
GetRegisteredClientPublicKeysPagedError._invalid_argument_validator = bv.Void()
GetRegisteredClientPublicKeysPagedError._team_key_not_found_validator = bv.Void()
GetRegisteredClientPublicKeysPagedError._client_key_not_found_validator = bv.Void()
GetRegisteredClientPublicKeysPagedError._other_validator = bv.Void()
GetRegisteredClientPublicKeysPagedError._tagmap = {
    'permission_denied': GetRegisteredClientPublicKeysPagedError._permission_denied_validator,
    'invalid_argument': GetRegisteredClientPublicKeysPagedError._invalid_argument_validator,
    'team_key_not_found': GetRegisteredClientPublicKeysPagedError._team_key_not_found_validator,
    'client_key_not_found': GetRegisteredClientPublicKeysPagedError._client_key_not_found_validator,
    'other': GetRegisteredClientPublicKeysPagedError._other_validator }
GetRegisteredClientPublicKeysPagedError.permission_denied = GetRegisteredClientPublicKeysPagedError('permission_denied')
GetRegisteredClientPublicKeysPagedError.invalid_argument = GetRegisteredClientPublicKeysPagedError('invalid_argument')
GetRegisteredClientPublicKeysPagedError.team_key_not_found = GetRegisteredClientPublicKeysPagedError('team_key_not_found')
GetRegisteredClientPublicKeysPagedError.client_key_not_found = GetRegisteredClientPublicKeysPagedError('client_key_not_found')
GetRegisteredClientPublicKeysPagedError.other = GetRegisteredClientPublicKeysPagedError('other')
GetRegisteredClientPublicKeysPagedResponse.client_public_keys.validator = bv.Nullable(bv.List(PublicKey_validator))
GetRegisteredClientPublicKeysPagedResponse.next_page_token.validator = bv.Nullable(bv.String())
GetRegisteredClientPublicKeysPagedResponse._all_field_names_ = set([
    'client_public_keys',
    'next_page_token'])
GetRegisteredClientPublicKeysPagedResponse._all_fields_ = [
    ('client_public_keys', GetRegisteredClientPublicKeysPagedResponse.client_public_keys.validator),
    ('next_page_token', GetRegisteredClientPublicKeysPagedResponse.next_page_token.validator)]
GetTeamEnrollmentStatusArg._all_field_names_ = set([])
GetTeamEnrollmentStatusArg._all_fields_ = []
GetTeamEnrollmentStatusError._permission_denied_validator = bv.Void()
GetTeamEnrollmentStatusError._not_team_member_validator = bv.Void()
GetTeamEnrollmentStatusError._other_validator = bv.Void()
GetTeamEnrollmentStatusError._tagmap = {
    'permission_denied': GetTeamEnrollmentStatusError._permission_denied_validator,
    'not_team_member': GetTeamEnrollmentStatusError._not_team_member_validator,
    'other': GetTeamEnrollmentStatusError._other_validator }
GetTeamEnrollmentStatusError.permission_denied = GetTeamEnrollmentStatusError('permission_denied')
GetTeamEnrollmentStatusError.not_team_member = GetTeamEnrollmentStatusError('not_team_member')
GetTeamEnrollmentStatusError.other = GetTeamEnrollmentStatusError('other')
GetTeamEnrollmentStatusResponse.enrollment_status.validator = TeamEnrollmentStatus_validator
GetTeamEnrollmentStatusResponse.bolt_token.validator = bv.Nullable(BoltChannelToken_validator)
GetTeamEnrollmentStatusResponse._all_field_names_ = set([
    'enrollment_status',
    'bolt_token'])
GetTeamEnrollmentStatusResponse._all_fields_ = [
    ('enrollment_status', GetTeamEnrollmentStatusResponse.enrollment_status.validator),
    ('bolt_token', GetTeamEnrollmentStatusResponse.bolt_token.validator)]
GetTeamKeyRotationInfoError._permission_denied_validator = bv.Void()
GetTeamKeyRotationInfoError._team_key_not_found_validator = bv.Void()
GetTeamKeyRotationInfoError._other_validator = bv.Void()
GetTeamKeyRotationInfoError._tagmap = {
    'permission_denied': GetTeamKeyRotationInfoError._permission_denied_validator,
    'team_key_not_found': GetTeamKeyRotationInfoError._team_key_not_found_validator,
    'other': GetTeamKeyRotationInfoError._other_validator }
GetTeamKeyRotationInfoError.permission_denied = GetTeamKeyRotationInfoError('permission_denied')
GetTeamKeyRotationInfoError.team_key_not_found = GetTeamKeyRotationInfoError('team_key_not_found')
GetTeamKeyRotationInfoError.other = GetTeamKeyRotationInfoError('other')
GetTeamKeyRotationInfoResponse.active_team_key.validator = bv.Nullable(TeamKeyInfo_validator)
GetTeamKeyRotationInfoResponse.draft_team_key.validator = bv.Nullable(TeamKeyInfo_validator)
GetTeamKeyRotationInfoResponse._all_field_names_ = set([
    'active_team_key',
    'draft_team_key'])
GetTeamKeyRotationInfoResponse._all_fields_ = [
    ('active_team_key', GetTeamKeyRotationInfoResponse.active_team_key.validator),
    ('draft_team_key', GetTeamKeyRotationInfoResponse.draft_team_key.validator)]
GetTeamPublicKeyError._permission_denied_validator = bv.Void()
GetTeamPublicKeyError._team_key_not_found_validator = bv.Void()
GetTeamPublicKeyError._other_validator = bv.Void()
GetTeamPublicKeyError._tagmap = {
    'permission_denied': GetTeamPublicKeyError._permission_denied_validator,
    'team_key_not_found': GetTeamPublicKeyError._team_key_not_found_validator,
    'other': GetTeamPublicKeyError._other_validator }
GetTeamPublicKeyError.permission_denied = GetTeamPublicKeyError('permission_denied')
GetTeamPublicKeyError.team_key_not_found = GetTeamPublicKeyError('team_key_not_found')
GetTeamPublicKeyError.other = GetTeamPublicKeyError('other')
GetTeamPublicKeyResponse.team_key.validator = bv.Nullable(PublicKey_validator)
GetTeamPublicKeyResponse._all_field_names_ = set([
    'team_key'])
GetTeamPublicKeyResponse._all_fields_ = [
    ('team_key', GetTeamPublicKeyResponse.team_key.validator)]
InitTeamKeyRotationArg.team_public_key.validator = bv.Nullable(PublicKeyDraft_validator)
InitTeamKeyRotationArg.encrypted_team_keys.validator = bv.Nullable(bv.List(EncryptedTeamKeyDraft_validator))
InitTeamKeyRotationArg._all_field_names_ = set([
    'team_public_key',
    'encrypted_team_keys'])
InitTeamKeyRotationArg._all_fields_ = [
    ('team_public_key', InitTeamKeyRotationArg.team_public_key.validator),
    ('encrypted_team_keys', InitTeamKeyRotationArg.encrypted_team_keys.validator)]
InitTeamKeyRotationError._permission_denied_validator = bv.Void()
InitTeamKeyRotationError._missing_arguments_validator = bv.Void()
InitTeamKeyRotationError._invalid_algorithm_validator = bv.Void()
InitTeamKeyRotationError._wrong_key_length_validator = bv.Void()
InitTeamKeyRotationError._team_enrollment_not_yet_finished_validator = bv.Void()
InitTeamKeyRotationError._team_key_rotation_in_progress_validator = bv.Void()
InitTeamKeyRotationError._backup_key_missing_validator = bv.Void()
InitTeamKeyRotationError._key_rotation_not_supported_with_key_verification_enabled_validator = bv.Void()
InitTeamKeyRotationError._wrong_id_length_validator = bv.Void()
InitTeamKeyRotationError._other_validator = bv.Void()
InitTeamKeyRotationError._tagmap = {
    'permission_denied': InitTeamKeyRotationError._permission_denied_validator,
    'missing_arguments': InitTeamKeyRotationError._missing_arguments_validator,
    'invalid_algorithm': InitTeamKeyRotationError._invalid_algorithm_validator,
    'wrong_key_length': InitTeamKeyRotationError._wrong_key_length_validator,
    'team_enrollment_not_yet_finished': InitTeamKeyRotationError._team_enrollment_not_yet_finished_validator,
    'team_key_rotation_in_progress': InitTeamKeyRotationError._team_key_rotation_in_progress_validator,
    'backup_key_missing': InitTeamKeyRotationError._backup_key_missing_validator,
    'key_rotation_not_supported_with_key_verification_enabled': InitTeamKeyRotationError._key_rotation_not_supported_with_key_verification_enabled_validator,
    'wrong_id_length': InitTeamKeyRotationError._wrong_id_length_validator,
    'other': InitTeamKeyRotationError._other_validator }
InitTeamKeyRotationError.permission_denied = InitTeamKeyRotationError('permission_denied')
InitTeamKeyRotationError.missing_arguments = InitTeamKeyRotationError('missing_arguments')
InitTeamKeyRotationError.invalid_algorithm = InitTeamKeyRotationError('invalid_algorithm')
InitTeamKeyRotationError.wrong_key_length = InitTeamKeyRotationError('wrong_key_length')
InitTeamKeyRotationError.team_enrollment_not_yet_finished = InitTeamKeyRotationError('team_enrollment_not_yet_finished')
InitTeamKeyRotationError.team_key_rotation_in_progress = InitTeamKeyRotationError('team_key_rotation_in_progress')
InitTeamKeyRotationError.backup_key_missing = InitTeamKeyRotationError('backup_key_missing')
InitTeamKeyRotationError.key_rotation_not_supported_with_key_verification_enabled = InitTeamKeyRotationError('key_rotation_not_supported_with_key_verification_enabled')
InitTeamKeyRotationError.wrong_id_length = InitTeamKeyRotationError('wrong_id_length')
InitTeamKeyRotationError.other = InitTeamKeyRotationError('other')
InitTeamKeyRotationResponse.team_key_id.validator = bv.String()
InitTeamKeyRotationResponse.team_key_id.validator._redact = bv.BlotRedactor(None)
InitTeamKeyRotationResponse._all_field_names_ = set([
    'team_key_id'])
InitTeamKeyRotationResponse._all_fields_ = [
    ('team_key_id', InitTeamKeyRotationResponse.team_key_id.validator)]
MerkleProof.hashes.validator = bv.Nullable(bv.List(MerkleProofHash_validator))
MerkleProof._all_field_names_ = set([
    'hashes'])
MerkleProof._all_fields_ = [
    ('hashes', MerkleProof.hashes.validator)]
MerkleProofHash.positioned.validator = BinaryPosition_validator
MerkleProofHash.hash.validator = bv.Bytes()
MerkleProofHash.hash.validator._redact = bv.BlotRedactor(None)
MerkleProofHash._all_field_names_ = set([
    'positioned',
    'hash'])
MerkleProofHash._all_fields_ = [
    ('positioned', MerkleProofHash.positioned.validator),
    ('hash', MerkleProofHash.hash.validator)]
NamespaceKeyDraft.ns_id.validator = bv.UInt64()
NamespaceKeyDraft.ns_id.validator._redact = bv.BlotRedactor(None)
NamespaceKeyDraft.public_key_draft.validator = bv.Nullable(PublicKeyDraft_validator)
NamespaceKeyDraft.encrypted_namespace_key_drafts.validator = bv.Nullable(bv.List(EncryptedNamespaceKeyDraft_validator))
NamespaceKeyDraft._all_field_names_ = set([
    'ns_id',
    'public_key_draft',
    'encrypted_namespace_key_drafts'])
NamespaceKeyDraft._all_fields_ = [
    ('ns_id', NamespaceKeyDraft.ns_id.validator),
    ('public_key_draft', NamespaceKeyDraft.public_key_draft.validator),
    ('encrypted_namespace_key_drafts', NamespaceKeyDraft.encrypted_namespace_key_drafts.validator)]
NamespaceKeyInfo.ns_id.validator = bv.UInt64()
NamespaceKeyInfo.ns_id.validator._redact = bv.BlotRedactor(None)
NamespaceKeyInfo.encrypting_key_ids.validator = bv.Nullable(bv.List(bv.String()))
NamespaceKeyInfo.encrypting_key_ids.validator._redact = bv.BlotRedactor(None)
NamespaceKeyInfo._all_field_names_ = set([
    'ns_id',
    'encrypting_key_ids'])
NamespaceKeyInfo._all_fields_ = [
    ('ns_id', NamespaceKeyInfo.ns_id.validator),
    ('encrypting_key_ids', NamespaceKeyInfo.encrypting_key_ids.validator)]
PublicKey.key_id.validator = bv.String()
PublicKey.key_id.validator._redact = bv.BlotRedactor(None)
PublicKey.key_data.validator = bv.Bytes()
PublicKey.key_data.validator._redact = bv.BlotRedactor(None)
PublicKey.algorithm.validator = AsymmetricEncryptionAlgorithm_validator
PublicKey.merkle_proof.validator = bv.Nullable(MerkleProof_validator)
PublicKey._all_field_names_ = set([
    'key_id',
    'key_data',
    'algorithm',
    'merkle_proof'])
PublicKey._all_fields_ = [
    ('key_id', PublicKey.key_id.validator),
    ('key_data', PublicKey.key_data.validator),
    ('algorithm', PublicKey.algorithm.validator),
    ('merkle_proof', PublicKey.merkle_proof.validator)]
PublicKeyDraft.key_data.validator = bv.Bytes()
PublicKeyDraft.key_data.validator._redact = bv.BlotRedactor(None)
PublicKeyDraft.algorithm.validator = AsymmetricEncryptionAlgorithm_validator
PublicKeyDraft._all_field_names_ = set([
    'key_data',
    'algorithm'])
PublicKeyDraft._all_fields_ = [
    ('key_data', PublicKeyDraft.key_data.validator),
    ('algorithm', PublicKeyDraft.algorithm.validator)]
RegisterBackupKeyArg.backup_key.validator = bv.Nullable(PublicKeyDraft_validator)
RegisterBackupKeyArg._all_field_names_ = set([
    'backup_key'])
RegisterBackupKeyArg._all_fields_ = [
    ('backup_key', RegisterBackupKeyArg.backup_key.validator)]
RegisterBackupKeyError._permission_denied_validator = bv.Void()
RegisterBackupKeyError._missing_arguments_validator = bv.Void()
RegisterBackupKeyError._invalid_algorithm_validator = bv.Void()
RegisterBackupKeyError._wrong_key_length_validator = bv.Void()
RegisterBackupKeyError._other_validator = bv.Void()
RegisterBackupKeyError._tagmap = {
    'permission_denied': RegisterBackupKeyError._permission_denied_validator,
    'missing_arguments': RegisterBackupKeyError._missing_arguments_validator,
    'invalid_algorithm': RegisterBackupKeyError._invalid_algorithm_validator,
    'wrong_key_length': RegisterBackupKeyError._wrong_key_length_validator,
    'other': RegisterBackupKeyError._other_validator }
RegisterBackupKeyError.permission_denied = RegisterBackupKeyError('permission_denied')
RegisterBackupKeyError.missing_arguments = RegisterBackupKeyError('missing_arguments')
RegisterBackupKeyError.invalid_algorithm = RegisterBackupKeyError('invalid_algorithm')
RegisterBackupKeyError.wrong_key_length = RegisterBackupKeyError('wrong_key_length')
RegisterBackupKeyError.other = RegisterBackupKeyError('other')
RegisterBackupKeyResponse.backup_key.validator = bv.Nullable(PublicKey_validator)
RegisterBackupKeyResponse._all_field_names_ = set([
    'backup_key'])
RegisterBackupKeyResponse._all_fields_ = [
    ('backup_key', RegisterBackupKeyResponse.backup_key.validator)]
RegisterClientArg.client_key.validator = bv.Nullable(PublicKeyDraft_validator)
RegisterClientArg._all_field_names_ = set([
    'client_key'])
RegisterClientArg._all_fields_ = [
    ('client_key', RegisterClientArg.client_key.validator)]
RegisterClientError._permission_denied_validator = bv.Void()
RegisterClientError._missing_arguments_validator = bv.Void()
RegisterClientError._team_key_not_found_validator = bv.Void()
RegisterClientError._team_enrollment_not_yet_finished_validator = bv.Void()
RegisterClientError._invalid_algorithm_validator = bv.Void()
RegisterClientError._team_keys_changed_validator = bv.Void()
RegisterClientError._wrong_key_length_validator = bv.Void()
RegisterClientError._other_validator = bv.Void()
RegisterClientError._tagmap = {
    'permission_denied': RegisterClientError._permission_denied_validator,
    'missing_arguments': RegisterClientError._missing_arguments_validator,
    'team_key_not_found': RegisterClientError._team_key_not_found_validator,
    'team_enrollment_not_yet_finished': RegisterClientError._team_enrollment_not_yet_finished_validator,
    'invalid_algorithm': RegisterClientError._invalid_algorithm_validator,
    'team_keys_changed': RegisterClientError._team_keys_changed_validator,
    'wrong_key_length': RegisterClientError._wrong_key_length_validator,
    'other': RegisterClientError._other_validator }
RegisterClientError.permission_denied = RegisterClientError('permission_denied')
RegisterClientError.missing_arguments = RegisterClientError('missing_arguments')
RegisterClientError.team_key_not_found = RegisterClientError('team_key_not_found')
RegisterClientError.team_enrollment_not_yet_finished = RegisterClientError('team_enrollment_not_yet_finished')
RegisterClientError.invalid_algorithm = RegisterClientError('invalid_algorithm')
RegisterClientError.team_keys_changed = RegisterClientError('team_keys_changed')
RegisterClientError.wrong_key_length = RegisterClientError('wrong_key_length')
RegisterClientError.other = RegisterClientError('other')
RegisterClientResponse.client_key.validator = bv.Nullable(PublicKey_validator)
RegisterClientResponse.bolt_token.validator = bv.Nullable(BoltChannelToken_validator)
RegisterClientResponse._all_field_names_ = set([
    'client_key',
    'bolt_token'])
RegisterClientResponse._all_fields_ = [
    ('client_key', RegisterClientResponse.client_key.validator),
    ('bolt_token', RegisterClientResponse.bolt_token.validator)]
RegisterFileKeyBatchArg.file_keys.validator = bv.Nullable(bv.List(EncryptedFileKeyDraft_validator))
RegisterFileKeyBatchArg._all_field_names_ = set([
    'file_keys'])
RegisterFileKeyBatchArg._all_fields_ = [
    ('file_keys', RegisterFileKeyBatchArg.file_keys.validator)]
RegisterFileKeyBatchError._permission_denied_validator = bv.Void()
RegisterFileKeyBatchError._missing_arguments_validator = bv.Void()
RegisterFileKeyBatchError._encrypting_key_not_found_validator = bv.Void()
RegisterFileKeyBatchError._invalid_algorithm_validator = bv.Void()
RegisterFileKeyBatchError._multiple_encrypting_keys_not_supported_validator = bv.Void()
RegisterFileKeyBatchError._too_many_keys_validator = bv.Void()
RegisterFileKeyBatchError._expired_encrypting_key_validator = bv.Void()
RegisterFileKeyBatchError._wrong_id_length_validator = bv.Void()
RegisterFileKeyBatchError._wrong_key_length_validator = bv.Void()
RegisterFileKeyBatchError._other_validator = bv.Void()
RegisterFileKeyBatchError._tagmap = {
    'permission_denied': RegisterFileKeyBatchError._permission_denied_validator,
    'missing_arguments': RegisterFileKeyBatchError._missing_arguments_validator,
    'encrypting_key_not_found': RegisterFileKeyBatchError._encrypting_key_not_found_validator,
    'invalid_algorithm': RegisterFileKeyBatchError._invalid_algorithm_validator,
    'multiple_encrypting_keys_not_supported': RegisterFileKeyBatchError._multiple_encrypting_keys_not_supported_validator,
    'too_many_keys': RegisterFileKeyBatchError._too_many_keys_validator,
    'expired_encrypting_key': RegisterFileKeyBatchError._expired_encrypting_key_validator,
    'wrong_id_length': RegisterFileKeyBatchError._wrong_id_length_validator,
    'wrong_key_length': RegisterFileKeyBatchError._wrong_key_length_validator,
    'other': RegisterFileKeyBatchError._other_validator }
RegisterFileKeyBatchError.permission_denied = RegisterFileKeyBatchError('permission_denied')
RegisterFileKeyBatchError.missing_arguments = RegisterFileKeyBatchError('missing_arguments')
RegisterFileKeyBatchError.encrypting_key_not_found = RegisterFileKeyBatchError('encrypting_key_not_found')
RegisterFileKeyBatchError.invalid_algorithm = RegisterFileKeyBatchError('invalid_algorithm')
RegisterFileKeyBatchError.multiple_encrypting_keys_not_supported = RegisterFileKeyBatchError('multiple_encrypting_keys_not_supported')
RegisterFileKeyBatchError.too_many_keys = RegisterFileKeyBatchError('too_many_keys')
RegisterFileKeyBatchError.expired_encrypting_key = RegisterFileKeyBatchError('expired_encrypting_key')
RegisterFileKeyBatchError.wrong_id_length = RegisterFileKeyBatchError('wrong_id_length')
RegisterFileKeyBatchError.wrong_key_length = RegisterFileKeyBatchError('wrong_key_length')
RegisterFileKeyBatchError.other = RegisterFileKeyBatchError('other')
RegisterFileKeyBatchResponse.file_keys.validator = bv.Nullable(bv.List(EncryptedFileKey_validator))
RegisterFileKeyBatchResponse._all_field_names_ = set([
    'file_keys'])
RegisterFileKeyBatchResponse._all_fields_ = [
    ('file_keys', RegisterFileKeyBatchResponse.file_keys.validator)]
RegisterFileKeyError._permission_denied_validator = bv.Void()
RegisterFileKeyError._missing_arguments_validator = bv.Void()
RegisterFileKeyError._encrypting_key_not_found_validator = bv.Void()
RegisterFileKeyError._invalid_algorithm_validator = bv.Void()
RegisterFileKeyError._expired_encrypting_key_validator = bv.Void()
RegisterFileKeyError._wrong_id_length_validator = bv.Void()
RegisterFileKeyError._wrong_key_length_validator = bv.Void()
RegisterFileKeyError._other_validator = bv.Void()
RegisterFileKeyError._tagmap = {
    'permission_denied': RegisterFileKeyError._permission_denied_validator,
    'missing_arguments': RegisterFileKeyError._missing_arguments_validator,
    'encrypting_key_not_found': RegisterFileKeyError._encrypting_key_not_found_validator,
    'invalid_algorithm': RegisterFileKeyError._invalid_algorithm_validator,
    'expired_encrypting_key': RegisterFileKeyError._expired_encrypting_key_validator,
    'wrong_id_length': RegisterFileKeyError._wrong_id_length_validator,
    'wrong_key_length': RegisterFileKeyError._wrong_key_length_validator,
    'other': RegisterFileKeyError._other_validator }
RegisterFileKeyError.permission_denied = RegisterFileKeyError('permission_denied')
RegisterFileKeyError.missing_arguments = RegisterFileKeyError('missing_arguments')
RegisterFileKeyError.encrypting_key_not_found = RegisterFileKeyError('encrypting_key_not_found')
RegisterFileKeyError.invalid_algorithm = RegisterFileKeyError('invalid_algorithm')
RegisterFileKeyError.expired_encrypting_key = RegisterFileKeyError('expired_encrypting_key')
RegisterFileKeyError.wrong_id_length = RegisterFileKeyError('wrong_id_length')
RegisterFileKeyError.wrong_key_length = RegisterFileKeyError('wrong_key_length')
RegisterFileKeyError.other = RegisterFileKeyError('other')
RegisterFileKeyRequest.file_key.validator = bv.Nullable(EncryptedFileKeyDraft_validator)
RegisterFileKeyRequest._all_field_names_ = set([
    'file_key'])
RegisterFileKeyRequest._all_fields_ = [
    ('file_key', RegisterFileKeyRequest.file_key.validator)]
RegisterFileKeyResponse.file_key.validator = bv.Nullable(EncryptedFileKey_validator)
RegisterFileKeyResponse._all_field_names_ = set([
    'file_key'])
RegisterFileKeyResponse._all_fields_ = [
    ('file_key', RegisterFileKeyResponse.file_key.validator)]
RegisterNamespaceKeyError._permission_denied_validator = bv.Void()
RegisterNamespaceKeyError._missing_arguments_validator = bv.Void()
RegisterNamespaceKeyError._namespace_key_already_exists_validator = bv.Void()
RegisterNamespaceKeyError._team_key_not_found_validator = bv.Void()
RegisterNamespaceKeyError._namespace_not_found_validator = bv.Void()
RegisterNamespaceKeyError._not_team_member_validator = bv.Void()
RegisterNamespaceKeyError._not_team_admin_validator = bv.Void()
RegisterNamespaceKeyError._edgestore_edge_deleted_exception_validator = bv.Void()
RegisterNamespaceKeyError._unauthorized_validator = bv.Void()
RegisterNamespaceKeyError._team_key_expired_validator = bv.Void()
RegisterNamespaceKeyError._team_key_in_wrong_state_validator = bv.Void()
RegisterNamespaceKeyError._wrong_id_length_validator = bv.Void()
RegisterNamespaceKeyError._wrong_key_length_validator = bv.Void()
RegisterNamespaceKeyError._invalid_algorithm_validator = bv.Void()
RegisterNamespaceKeyError._other_validator = bv.Void()
RegisterNamespaceKeyError._tagmap = {
    'permission_denied': RegisterNamespaceKeyError._permission_denied_validator,
    'missing_arguments': RegisterNamespaceKeyError._missing_arguments_validator,
    'namespace_key_already_exists': RegisterNamespaceKeyError._namespace_key_already_exists_validator,
    'team_key_not_found': RegisterNamespaceKeyError._team_key_not_found_validator,
    'namespace_not_found': RegisterNamespaceKeyError._namespace_not_found_validator,
    'not_team_member': RegisterNamespaceKeyError._not_team_member_validator,
    'not_team_admin': RegisterNamespaceKeyError._not_team_admin_validator,
    'edgestore_edge_deleted_exception': RegisterNamespaceKeyError._edgestore_edge_deleted_exception_validator,
    'unauthorized': RegisterNamespaceKeyError._unauthorized_validator,
    'team_key_expired': RegisterNamespaceKeyError._team_key_expired_validator,
    'team_key_in_wrong_state': RegisterNamespaceKeyError._team_key_in_wrong_state_validator,
    'wrong_id_length': RegisterNamespaceKeyError._wrong_id_length_validator,
    'wrong_key_length': RegisterNamespaceKeyError._wrong_key_length_validator,
    'invalid_algorithm': RegisterNamespaceKeyError._invalid_algorithm_validator,
    'other': RegisterNamespaceKeyError._other_validator }
RegisterNamespaceKeyError.permission_denied = RegisterNamespaceKeyError('permission_denied')
RegisterNamespaceKeyError.missing_arguments = RegisterNamespaceKeyError('missing_arguments')
RegisterNamespaceKeyError.namespace_key_already_exists = RegisterNamespaceKeyError('namespace_key_already_exists')
RegisterNamespaceKeyError.team_key_not_found = RegisterNamespaceKeyError('team_key_not_found')
RegisterNamespaceKeyError.namespace_not_found = RegisterNamespaceKeyError('namespace_not_found')
RegisterNamespaceKeyError.not_team_member = RegisterNamespaceKeyError('not_team_member')
RegisterNamespaceKeyError.not_team_admin = RegisterNamespaceKeyError('not_team_admin')
RegisterNamespaceKeyError.edgestore_edge_deleted_exception = RegisterNamespaceKeyError('edgestore_edge_deleted_exception')
RegisterNamespaceKeyError.unauthorized = RegisterNamespaceKeyError('unauthorized')
RegisterNamespaceKeyError.team_key_expired = RegisterNamespaceKeyError('team_key_expired')
RegisterNamespaceKeyError.team_key_in_wrong_state = RegisterNamespaceKeyError('team_key_in_wrong_state')
RegisterNamespaceKeyError.wrong_id_length = RegisterNamespaceKeyError('wrong_id_length')
RegisterNamespaceKeyError.wrong_key_length = RegisterNamespaceKeyError('wrong_key_length')
RegisterNamespaceKeyError.invalid_algorithm = RegisterNamespaceKeyError('invalid_algorithm')
RegisterNamespaceKeyError.other = RegisterNamespaceKeyError('other')
RegisterNamespaceKeysForDraftTeamKeyArg.namespace_key_drafts.validator = bv.Nullable(bv.List(NamespaceKeyDraft_validator))
RegisterNamespaceKeysForDraftTeamKeyArg._all_field_names_ = set([
    'namespace_key_drafts'])
RegisterNamespaceKeysForDraftTeamKeyArg._all_fields_ = [
    ('namespace_key_drafts', RegisterNamespaceKeysForDraftTeamKeyArg.namespace_key_drafts.validator)]
RegisterNamespaceKeysForDraftTeamKeyError._permission_denied_validator = bv.Void()
RegisterNamespaceKeysForDraftTeamKeyError._missing_arguments_validator = bv.Void()
RegisterNamespaceKeysForDraftTeamKeyError._wrong_key_length_validator = bv.Void()
RegisterNamespaceKeysForDraftTeamKeyError._no_draft_team_key_exists_validator = bv.Void()
RegisterNamespaceKeysForDraftTeamKeyError._team_key_not_found_validator = bv.Void()
RegisterNamespaceKeysForDraftTeamKeyError._namespace_key_draft_not_encrypted_with_draft_team_key_validator = bv.Void()
RegisterNamespaceKeysForDraftTeamKeyError._namespace_key_not_found_validator = bv.Void()
RegisterNamespaceKeysForDraftTeamKeyError._team_keys_changed_validator = bv.Void()
RegisterNamespaceKeysForDraftTeamKeyError._wrong_id_length_validator = bv.Void()
RegisterNamespaceKeysForDraftTeamKeyError._other_validator = bv.Void()
RegisterNamespaceKeysForDraftTeamKeyError._tagmap = {
    'permission_denied': RegisterNamespaceKeysForDraftTeamKeyError._permission_denied_validator,
    'missing_arguments': RegisterNamespaceKeysForDraftTeamKeyError._missing_arguments_validator,
    'wrong_key_length': RegisterNamespaceKeysForDraftTeamKeyError._wrong_key_length_validator,
    'no_draft_team_key_exists': RegisterNamespaceKeysForDraftTeamKeyError._no_draft_team_key_exists_validator,
    'team_key_not_found': RegisterNamespaceKeysForDraftTeamKeyError._team_key_not_found_validator,
    'namespace_key_draft_not_encrypted_with_draft_team_key': RegisterNamespaceKeysForDraftTeamKeyError._namespace_key_draft_not_encrypted_with_draft_team_key_validator,
    'namespace_key_not_found': RegisterNamespaceKeysForDraftTeamKeyError._namespace_key_not_found_validator,
    'team_keys_changed': RegisterNamespaceKeysForDraftTeamKeyError._team_keys_changed_validator,
    'wrong_id_length': RegisterNamespaceKeysForDraftTeamKeyError._wrong_id_length_validator,
    'other': RegisterNamespaceKeysForDraftTeamKeyError._other_validator }
RegisterNamespaceKeysForDraftTeamKeyError.permission_denied = RegisterNamespaceKeysForDraftTeamKeyError('permission_denied')
RegisterNamespaceKeysForDraftTeamKeyError.missing_arguments = RegisterNamespaceKeysForDraftTeamKeyError('missing_arguments')
RegisterNamespaceKeysForDraftTeamKeyError.wrong_key_length = RegisterNamespaceKeysForDraftTeamKeyError('wrong_key_length')
RegisterNamespaceKeysForDraftTeamKeyError.no_draft_team_key_exists = RegisterNamespaceKeysForDraftTeamKeyError('no_draft_team_key_exists')
RegisterNamespaceKeysForDraftTeamKeyError.team_key_not_found = RegisterNamespaceKeysForDraftTeamKeyError('team_key_not_found')
RegisterNamespaceKeysForDraftTeamKeyError.namespace_key_draft_not_encrypted_with_draft_team_key = RegisterNamespaceKeysForDraftTeamKeyError('namespace_key_draft_not_encrypted_with_draft_team_key')
RegisterNamespaceKeysForDraftTeamKeyError.namespace_key_not_found = RegisterNamespaceKeysForDraftTeamKeyError('namespace_key_not_found')
RegisterNamespaceKeysForDraftTeamKeyError.team_keys_changed = RegisterNamespaceKeysForDraftTeamKeyError('team_keys_changed')
RegisterNamespaceKeysForDraftTeamKeyError.wrong_id_length = RegisterNamespaceKeysForDraftTeamKeyError('wrong_id_length')
RegisterNamespaceKeysForDraftTeamKeyError.other = RegisterNamespaceKeysForDraftTeamKeyError('other')
RemoveBackupKeyArg.key_id.validator = bv.String()
RemoveBackupKeyArg.key_id.validator._redact = bv.BlotRedactor(None)
RemoveBackupKeyArg._all_field_names_ = set([
    'key_id'])
RemoveBackupKeyArg._all_fields_ = [
    ('key_id', RemoveBackupKeyArg.key_id.validator)]
RemoveBackupKeyError._permission_denied_validator = bv.Void()
RemoveBackupKeyError._missing_arguments_validator = bv.Void()
RemoveBackupKeyError._backup_key_not_found_validator = bv.Void()
RemoveBackupKeyError._cannot_delete_last_backup_key_validator = bv.Void()
RemoveBackupKeyError._other_validator = bv.Void()
RemoveBackupKeyError._tagmap = {
    'permission_denied': RemoveBackupKeyError._permission_denied_validator,
    'missing_arguments': RemoveBackupKeyError._missing_arguments_validator,
    'backup_key_not_found': RemoveBackupKeyError._backup_key_not_found_validator,
    'cannot_delete_last_backup_key': RemoveBackupKeyError._cannot_delete_last_backup_key_validator,
    'other': RemoveBackupKeyError._other_validator }
RemoveBackupKeyError.permission_denied = RemoveBackupKeyError('permission_denied')
RemoveBackupKeyError.missing_arguments = RemoveBackupKeyError('missing_arguments')
RemoveBackupKeyError.backup_key_not_found = RemoveBackupKeyError('backup_key_not_found')
RemoveBackupKeyError.cannot_delete_last_backup_key = RemoveBackupKeyError('cannot_delete_last_backup_key')
RemoveBackupKeyError.other = RemoveBackupKeyError('other')
RotateTeamKeyArg.draft_team_key_id.validator = bv.String()
RotateTeamKeyArg.draft_team_key_id.validator._redact = bv.BlotRedactor(None)
RotateTeamKeyArg._all_field_names_ = set([
    'draft_team_key_id'])
RotateTeamKeyArg._all_fields_ = [
    ('draft_team_key_id', RotateTeamKeyArg.draft_team_key_id.validator)]
RotateTeamKeyError._permission_denied_validator = bv.Void()
RotateTeamKeyError._missing_arguments_validator = bv.Void()
RotateTeamKeyError._team_key_draft_not_found_validator = bv.Void()
RotateTeamKeyError._team_key_not_in_draft_state_validator = bv.Void()
RotateTeamKeyError._namespace_key_not_found_validator = bv.Void()
RotateTeamKeyError._namespace_key_draft_not_encrypted_with_all_team_keys_validator = bv.Void()
RotateTeamKeyError._namespace_not_found_validator = bv.Void()
RotateTeamKeyError._namespace_keys_changed_validator = bv.Void()
RotateTeamKeyError._other_validator = bv.Void()
RotateTeamKeyError._tagmap = {
    'permission_denied': RotateTeamKeyError._permission_denied_validator,
    'missing_arguments': RotateTeamKeyError._missing_arguments_validator,
    'team_key_draft_not_found': RotateTeamKeyError._team_key_draft_not_found_validator,
    'team_key_not_in_draft_state': RotateTeamKeyError._team_key_not_in_draft_state_validator,
    'namespace_key_not_found': RotateTeamKeyError._namespace_key_not_found_validator,
    'namespace_key_draft_not_encrypted_with_all_team_keys': RotateTeamKeyError._namespace_key_draft_not_encrypted_with_all_team_keys_validator,
    'namespace_not_found': RotateTeamKeyError._namespace_not_found_validator,
    'namespace_keys_changed': RotateTeamKeyError._namespace_keys_changed_validator,
    'other': RotateTeamKeyError._other_validator }
RotateTeamKeyError.permission_denied = RotateTeamKeyError('permission_denied')
RotateTeamKeyError.missing_arguments = RotateTeamKeyError('missing_arguments')
RotateTeamKeyError.team_key_draft_not_found = RotateTeamKeyError('team_key_draft_not_found')
RotateTeamKeyError.team_key_not_in_draft_state = RotateTeamKeyError('team_key_not_in_draft_state')
RotateTeamKeyError.namespace_key_not_found = RotateTeamKeyError('namespace_key_not_found')
RotateTeamKeyError.namespace_key_draft_not_encrypted_with_all_team_keys = RotateTeamKeyError('namespace_key_draft_not_encrypted_with_all_team_keys')
RotateTeamKeyError.namespace_not_found = RotateTeamKeyError('namespace_not_found')
RotateTeamKeyError.namespace_keys_changed = RotateTeamKeyError('namespace_keys_changed')
RotateTeamKeyError.other = RotateTeamKeyError('other')
RotateTeamKeyResponse.result.validator = RotateTeamKeyResult_validator
RotateTeamKeyResponse.missing_backup_key_ids.validator = bv.Nullable(bv.List(bv.String()))
RotateTeamKeyResponse.missing_backup_key_ids.validator._redact = bv.BlotRedactor(None)
RotateTeamKeyResponse.missing_client_key_ids.validator = bv.Nullable(bv.List(bv.String()))
RotateTeamKeyResponse.missing_client_key_ids.validator._redact = bv.BlotRedactor(None)
RotateTeamKeyResponse.missing_replacement_for_namespace_keys.validator = bv.Nullable(bv.List(bv.String()))
RotateTeamKeyResponse.missing_replacement_for_namespace_keys.validator._redact = bv.BlotRedactor(None)
RotateTeamKeyResponse._all_field_names_ = set([
    'result',
    'missing_backup_key_ids',
    'missing_client_key_ids',
    'missing_replacement_for_namespace_keys'])
RotateTeamKeyResponse._all_fields_ = [
    ('result', RotateTeamKeyResponse.result.validator),
    ('missing_backup_key_ids', RotateTeamKeyResponse.missing_backup_key_ids.validator),
    ('missing_client_key_ids', RotateTeamKeyResponse.missing_client_key_ids.validator),
    ('missing_replacement_for_namespace_keys', RotateTeamKeyResponse.missing_replacement_for_namespace_keys.validator)]
RotateTeamKeyResult._key_rotation_successful_validator = bv.Void()
RotateTeamKeyResult._keys_missing_validator = bv.Void()
RotateTeamKeyResult._other_validator = bv.Void()
RotateTeamKeyResult._tagmap = {
    'key_rotation_successful': RotateTeamKeyResult._key_rotation_successful_validator,
    'keys_missing': RotateTeamKeyResult._keys_missing_validator,
    'other': RotateTeamKeyResult._other_validator }
RotateTeamKeyResult.key_rotation_successful = RotateTeamKeyResult('key_rotation_successful')
RotateTeamKeyResult.keys_missing = RotateTeamKeyResult('keys_missing')
RotateTeamKeyResult.other = RotateTeamKeyResult('other')
SelectedBackupKeys.key_ids.validator = bv.Nullable(bv.List(bv.String()))
SelectedBackupKeys.key_ids.validator._redact = bv.BlotRedactor(None)
SelectedBackupKeys._all_field_names_ = set([
    'key_ids'])
SelectedBackupKeys._all_fields_ = [
    ('key_ids', SelectedBackupKeys.key_ids.validator)]
SelectedNamespaceKeys.key_ids.validator = bv.Nullable(bv.List(bv.String()))
SelectedNamespaceKeys.key_ids.validator._redact = bv.BlotRedactor(None)
SelectedNamespaceKeys._all_field_names_ = set([
    'key_ids'])
SelectedNamespaceKeys._all_fields_ = [
    ('key_ids', SelectedNamespaceKeys.key_ids.validator)]
ShareNamespaceArg.ns_id.validator = bv.UInt64()
ShareNamespaceArg.ns_id.validator._redact = bv.BlotRedactor(None)
ShareNamespaceArg.encrypted_namespace_keys.validator = bv.Nullable(bv.List(EncryptedNamespaceKey_validator))
ShareNamespaceArg._all_field_names_ = set([
    'ns_id',
    'encrypted_namespace_keys'])
ShareNamespaceArg._all_fields_ = [
    ('ns_id', ShareNamespaceArg.ns_id.validator),
    ('encrypted_namespace_keys', ShareNamespaceArg.encrypted_namespace_keys.validator)]
ShareNamespaceError._permission_denied_validator = bv.Void()
ShareNamespaceError._missing_arguments_validator = bv.Void()
ShareNamespaceError._namespace_not_found_validator = bv.Void()
ShareNamespaceError._namespace_key_not_found_validator = bv.Void()
ShareNamespaceError._team_key_not_found_validator = bv.Void()
ShareNamespaceError._not_supported_with_key_verification_enabled_validator = bv.Void()
ShareNamespaceError._keys_rotated_validator = ShareNamespaceKeysRotatedError_validator
ShareNamespaceError._other_validator = bv.Void()
ShareNamespaceError._tagmap = {
    'permission_denied': ShareNamespaceError._permission_denied_validator,
    'missing_arguments': ShareNamespaceError._missing_arguments_validator,
    'namespace_not_found': ShareNamespaceError._namespace_not_found_validator,
    'namespace_key_not_found': ShareNamespaceError._namespace_key_not_found_validator,
    'team_key_not_found': ShareNamespaceError._team_key_not_found_validator,
    'not_supported_with_key_verification_enabled': ShareNamespaceError._not_supported_with_key_verification_enabled_validator,
    'keys_rotated': ShareNamespaceError._keys_rotated_validator,
    'other': ShareNamespaceError._other_validator }
ShareNamespaceError.permission_denied = ShareNamespaceError('permission_denied')
ShareNamespaceError.missing_arguments = ShareNamespaceError('missing_arguments')
ShareNamespaceError.namespace_not_found = ShareNamespaceError('namespace_not_found')
ShareNamespaceError.namespace_key_not_found = ShareNamespaceError('namespace_key_not_found')
ShareNamespaceError.team_key_not_found = ShareNamespaceError('team_key_not_found')
ShareNamespaceError.not_supported_with_key_verification_enabled = ShareNamespaceError('not_supported_with_key_verification_enabled')
ShareNamespaceError.other = ShareNamespaceError('other')
ShareNamespaceKeysRotatedError.ns_id.validator = bv.UInt64()
ShareNamespaceKeysRotatedError.ns_id.validator._redact = bv.BlotRedactor(None)
ShareNamespaceKeysRotatedError.team_public_keys.validator = bv.Nullable(bv.List(PublicKey_validator))
ShareNamespaceKeysRotatedError._all_field_names_ = set([
    'ns_id',
    'team_public_keys'])
ShareNamespaceKeysRotatedError._all_fields_ = [
    ('ns_id', ShareNamespaceKeysRotatedError.ns_id.validator),
    ('team_public_keys', ShareNamespaceKeysRotatedError.team_public_keys.validator)]
SymmetricEncryptionAlgorithm._unknown_symmetric_encryption_algorithm_validator = bv.Void()
SymmetricEncryptionAlgorithm._aes256_gcm_extras_validator = bv.Void()
SymmetricEncryptionAlgorithm._other_validator = bv.Void()
SymmetricEncryptionAlgorithm._tagmap = {
    'unknown_symmetric_encryption_algorithm': SymmetricEncryptionAlgorithm._unknown_symmetric_encryption_algorithm_validator,
    'aes256_gcm_extras': SymmetricEncryptionAlgorithm._aes256_gcm_extras_validator,
    'other': SymmetricEncryptionAlgorithm._other_validator }
SymmetricEncryptionAlgorithm.unknown_symmetric_encryption_algorithm = SymmetricEncryptionAlgorithm('unknown_symmetric_encryption_algorithm')
SymmetricEncryptionAlgorithm.aes256_gcm_extras = SymmetricEncryptionAlgorithm('aes256_gcm_extras')
SymmetricEncryptionAlgorithm.other = SymmetricEncryptionAlgorithm('other')
TeamEnrollmentStatus._not_enrolled_validator = bv.Void()
TeamEnrollmentStatus._enrolled_validator = bv.Void()
TeamEnrollmentStatus._other_validator = bv.Void()
TeamEnrollmentStatus._tagmap = {
    'not_enrolled': TeamEnrollmentStatus._not_enrolled_validator,
    'enrolled': TeamEnrollmentStatus._enrolled_validator,
    'other': TeamEnrollmentStatus._other_validator }
TeamEnrollmentStatus.not_enrolled = TeamEnrollmentStatus('not_enrolled')
TeamEnrollmentStatus.enrolled = TeamEnrollmentStatus('enrolled')
TeamEnrollmentStatus.other = TeamEnrollmentStatus('other')
TeamKeyInfo.creation_date.validator = bv.Nullable(common.DropboxTimestamp_validator)
TeamKeyInfo.algorithm.validator = AsymmetricEncryptionAlgorithm_validator
TeamKeyInfo.key_id.validator = bv.String()
TeamKeyInfo.key_id.validator._redact = bv.BlotRedactor(None)
TeamKeyInfo._all_field_names_ = set([
    'creation_date',
    'algorithm',
    'key_id'])
TeamKeyInfo._all_fields_ = [
    ('creation_date', TeamKeyInfo.creation_date.validator),
    ('algorithm', TeamKeyInfo.algorithm.validator),
    ('key_id', TeamKeyInfo.key_id.validator)]
BackupKey.key_id.default = ''
BackupKey.algorithm.default = AsymmetricEncryptionAlgorithm.unknown_asymmetric_encryption_algorithm
BoltChannelToken.revision.default = 0
BoltChannelToken.token.default = ''
BoltChannelToken.rev.default = ''
BoltChannelToken.deprecated_revision.default = 0
CancelKeyRotationArg.draft_team_key_id.default = ''
ChannelId.app_id.default = ''
ChannelId.unique_id.default = ''
ClientDetails.display_name.default = ''
ClientDetails.email.default = ''
ClientDetails.account_photo_url.default = ''
EncryptedFileKey.key_id.default = ''
EncryptedFileKey.encrypting_key_id.default = ''
EncryptedFileKey.algorithm.default = SymmetricEncryptionAlgorithm.unknown_symmetric_encryption_algorithm
EncryptedFileKeyDraft.encrypting_key_id.default = ''
EncryptedFileKeyDraft.algorithm.default = SymmetricEncryptionAlgorithm.unknown_symmetric_encryption_algorithm
EncryptedKeyPair.key_id.default = ''
EncryptedKeyPair.encrypting_key_id.default = ''
EncryptedKeyPair.algorithm.default = AsymmetricEncryptionAlgorithm.unknown_asymmetric_encryption_algorithm
EncryptedKeyPairDraft.algorithm.default = AsymmetricEncryptionAlgorithm.unknown_asymmetric_encryption_algorithm
EncryptedNamespaceKey.namespace_key_id.default = ''
EncryptedNamespaceKey.encrypting_key_id.default = ''
EncryptedNamespaceKeyDraft.encrypting_key_id.default = ''
EncryptedTeamKey.team_key_id.default = ''
EncryptedTeamKey.encrypting_key_id.default = ''
EncryptedTeamKeyDraft.encrypting_key_id.default = ''
EnrollBackupKeyForTeamArg.backup_key_id.default = ''
EnrollTeamArg.encrypting_backup_key_id.default = ''
GetClientKeyEnrollmentStatusArg.client_key_id.default = ''
GetClientKeyEnrollmentStatusResponse.enrollment_status.default = ClientKeyEnrollmentStatus.client_not_registered
GetEncryptedDraftTeamKeyWithBackupKeyArg.backup_key_id.default = ''
GetEncryptedTeamKeyListWithBackupKeyArg.backup_key_id.default = ''
GetEncryptedTeamKeyListWithClientKeyArg.client_key_id.default = ''
GetEncryptedTeamKeyWithClientKeyArg.client_key_id.default = ''
GetFileKeysArg.root_key_id.default = ''
GetNamespaceKeyArg.root_key_id.default = ''
GetNamespaceKeyArg.ns_id.default = 0
GetNamespaceKeysArg.root_key_id.default = ''
GetNamespaceKeysArg.ns_id.default = 0
GetNamespaceKeysInfoResponse.active_team_key_id.default = ''
GetNamespacePublicKeyArg.ns_id.default = 0
GetTeamEnrollmentStatusResponse.enrollment_status.default = TeamEnrollmentStatus.not_enrolled
InitTeamKeyRotationResponse.team_key_id.default = ''
MerkleProofHash.positioned.default = BinaryPosition.left
NamespaceKeyDraft.ns_id.default = 0
NamespaceKeyInfo.ns_id.default = 0
PublicKey.key_id.default = ''
PublicKey.algorithm.default = AsymmetricEncryptionAlgorithm.unknown_asymmetric_encryption_algorithm
PublicKeyDraft.algorithm.default = AsymmetricEncryptionAlgorithm.unknown_asymmetric_encryption_algorithm
RemoveBackupKeyArg.key_id.default = ''
RotateTeamKeyArg.draft_team_key_id.default = ''
RotateTeamKeyResponse.result.default = RotateTeamKeyResult.key_rotation_successful
ShareNamespaceArg.ns_id.default = 0
ShareNamespaceKeysRotatedError.ns_id.default = 0
TeamKeyInfo.algorithm.default = AsymmetricEncryptionAlgorithm.unknown_asymmetric_encryption_algorithm
TeamKeyInfo.key_id.default = ''
# WARNING: Decompyle incomplete
