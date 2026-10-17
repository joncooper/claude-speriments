# Source Generated with Decompyle++
# File: external_drive_backup.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import device_sync
from dropbox.api.v2.datatypes import files

class Backup(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Backup_validator = bv.Struct(Backup)

class BackupConflictInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BackupConflictInfo_validator = bv.Struct(BackupConflictInfo)

class BackupStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

BackupStatus_validator = bv.Union(BackupStatus)

class ClearAllQuotaExemptError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ClearAllQuotaExemptError_validator = bv.Union(ClearAllQuotaExemptError)

class ClearableString(bb.Union):
    pass
# WARNING: Decompyle incomplete

ClearableString_validator = bv.Union(ClearableString)

class ClearableUInt64(bb.Union):
    pass
# WARNING: Decompyle incomplete

ClearableUInt64_validator = bv.Union(ClearableUInt64)

class CreateBackupArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreateBackupArg_validator = bv.Struct(CreateBackupArg)

class CreateBackupError(bb.Union):
    pass
# WARNING: Decompyle incomplete

CreateBackupError_validator = bv.Union(CreateBackupError)

class CreateBackupResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreateBackupResult_validator = bv.Struct(CreateBackupResult)

class CreateBackupWithBackupRootInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreateBackupWithBackupRootInfo_validator = bv.Struct(CreateBackupWithBackupRootInfo)

class DanglingFolder(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DanglingFolder_validator = bv.Struct(DanglingFolder)

class DeleteBackupArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeleteBackupArg_validator = bv.Struct(DeleteBackupArg)

class DeleteBackupError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DeleteBackupError_validator = bv.Union(DeleteBackupError)

class DeleteBackupResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeleteBackupResult_validator = bv.Struct(DeleteBackupResult)

class DriveInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DriveInfo_validator = bv.Struct(DriveInfo)

class EligibleMigrationType(bb.Union):
    pass
# WARNING: Decompyle incomplete

EligibleMigrationType_validator = bv.Union(EligibleMigrationType)

class ExternalDriveBackupStateEnum(bb.Union):
    pass
# WARNING: Decompyle incomplete

ExternalDriveBackupStateEnum_validator = bv.Union(ExternalDriveBackupStateEnum)

class ExternalDriveEntry(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ExternalDriveEntry_validator = bv.Struct(ExternalDriveEntry)

class GetEligibilityInfoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetEligibilityInfoArg_validator = bv.Struct(GetEligibilityInfoArg)

class GetEligibilityInfoError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetEligibilityInfoError_validator = bv.Union(GetEligibilityInfoError)

class GetEligibilityInfoResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetEligibilityInfoResult_validator = bv.Struct(GetEligibilityInfoResult)

class IneligibleReason(bb.Union):
    pass
# WARNING: Decompyle incomplete

IneligibleReason_validator = bv.Union(IneligibleReason)

class InvalidRequestError(bb.Union):
    pass
# WARNING: Decompyle incomplete

InvalidRequestError_validator = bv.Union(InvalidRequestError)

class IsEligibleForSeamlessMigrationArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

IsEligibleForSeamlessMigrationArg_validator = bv.Struct(IsEligibleForSeamlessMigrationArg)

class IsEligibleForSeamlessMigrationBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

IsEligibleForSeamlessMigrationBatchArg_validator = bv.Struct(IsEligibleForSeamlessMigrationBatchArg)

class IsEligibleForSeamlessMigrationError(bb.Union):
    pass
# WARNING: Decompyle incomplete

IsEligibleForSeamlessMigrationError_validator = bv.Union(IsEligibleForSeamlessMigrationError)

class IsEligibleForSeamlessMigrationResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

IsEligibleForSeamlessMigrationResult_validator = bv.Struct(IsEligibleForSeamlessMigrationResult)

class ListAllBackupsResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListAllBackupsResult_validator = bv.Struct(ListAllBackupsResult)

class ListBackupsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListBackupsArg_validator = bv.Struct(ListBackupsArg)

class ListBackupsResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListBackupsResult_validator = bv.Struct(ListBackupsResult)

class NamespaceInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

NamespaceInfo_validator = bv.Struct(NamespaceInfo)

class NotEligibleMigrationEnum(bb.Union):
    pass
# WARNING: Decompyle incomplete

NotEligibleMigrationEnum_validator = bv.Union(NotEligibleMigrationEnum)

class PollXopStatusArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PollXopStatusArg_validator = bv.Struct(PollXopStatusArg)

class PollXopStatusBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PollXopStatusBatchArg_validator = bv.Struct(PollXopStatusBatchArg)

class PollXopStatusBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PollXopStatusBatchResult_validator = bv.Struct(PollXopStatusBatchResult)

class PollXopStatusError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PollXopStatusError_validator = bv.Union(PollXopStatusError)

class PollXopStatusResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PollXopStatusResult_validator = bv.Struct(PollXopStatusResult)

class ReadSeamlessMigrationStateArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ReadSeamlessMigrationStateArg_validator = bv.Struct(ReadSeamlessMigrationStateArg)

class ReadSeamlessMigrationStateError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ReadSeamlessMigrationStateError_validator = bv.Union(ReadSeamlessMigrationStateError)

class ReadSeamlessMigrationStateResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ReadSeamlessMigrationStateResult_validator = bv.Struct(ReadSeamlessMigrationStateResult)

class SeamlessFissionMigrationStateEnum(bb.Union):
    pass
# WARNING: Decompyle incomplete

SeamlessFissionMigrationStateEnum_validator = bv.Union(SeamlessFissionMigrationStateEnum)

class SeamlessMigrationError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SeamlessMigrationError_validator = bv.Union(SeamlessMigrationError)

class SetQuotaExemptArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SetQuotaExemptArg_validator = bv.Struct(SetQuotaExemptArg)

class SetQuotaExemptError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SetQuotaExemptError_validator = bv.Union(SetQuotaExemptError)

class SetupPredictionArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SetupPredictionArg_validator = bv.Struct(SetupPredictionArg)

class SetupPredictionError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SetupPredictionError_validator = bv.Union(SetupPredictionError)

class SetupPredictionResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SetupPredictionResult_validator = bv.Struct(SetupPredictionResult)

class SetupSeamlessMigrationArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SetupSeamlessMigrationArg_validator = bv.Struct(SetupSeamlessMigrationArg)

class SetupSeamlessMigrationError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SetupSeamlessMigrationError_validator = bv.Union(SetupSeamlessMigrationError)

class SetupSeamlessMigrationResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SetupSeamlessMigrationResult_validator = bv.Struct(SetupSeamlessMigrationResult)

class StartBackupArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StartBackupArg_validator = bv.Struct(StartBackupArg)

class StartBackupError(bb.Union):
    pass
# WARNING: Decompyle incomplete

StartBackupError_validator = bv.Union(StartBackupError)

class StartBackupResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StartBackupResult_validator = bv.Struct(StartBackupResult)

class StartSeamlessMigrationArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StartSeamlessMigrationArg_validator = bv.Struct(StartSeamlessMigrationArg)

class StartSeamlessMigrationError(bb.Union):
    pass
# WARNING: Decompyle incomplete

StartSeamlessMigrationError_validator = bv.Union(StartSeamlessMigrationError)

class StartSeamlessMigrationResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StartSeamlessMigrationResult_validator = bv.Struct(StartSeamlessMigrationResult)

class UpdateBackupArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateBackupArg_validator = bv.Struct(UpdateBackupArg)

class UpdateBackupError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UpdateBackupError_validator = bv.Union(UpdateBackupError)

class UpdateBackupResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateBackupResult_validator = bv.Struct(UpdateBackupResult)

class UpdateDisplayNameArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateDisplayNameArg_validator = bv.Struct(UpdateDisplayNameArg)

class UpdateDisplayNameError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UpdateDisplayNameError_validator = bv.Union(UpdateDisplayNameError)

class UpdateSeamlessMigrationStateArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateSeamlessMigrationStateArg_validator = bv.Struct(UpdateSeamlessMigrationStateArg)

class UpdateSeamlessMigrationStateError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UpdateSeamlessMigrationStateError_validator = bv.Union(UpdateSeamlessMigrationStateError)

class UpdateSeamlessMigrationStateResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateSeamlessMigrationStateResult_validator = bv.Struct(UpdateSeamlessMigrationStateResult)

class XopStatusEnum(bb.Union):
    pass
# WARNING: Decompyle incomplete

XopStatusEnum_validator = bv.Union(XopStatusEnum)
NamespaceId_validator = bv.UInt64()
NamespaceId_validator._redact = bv.BlotRedactor(None)
Backup.backup_id.validator = bv.String()
Backup.backup_id.validator._redact = bv.BlotRedactor(None)
Backup.name.validator = bv.String()
Backup.name.validator._redact = bv.BlotRedactor(None)
Backup.namespace_info.validator = bv.Nullable(NamespaceInfo_validator)
Backup.status.validator = BackupStatus_validator
Backup._all_field_names_ = set([
    'backup_id',
    'name',
    'namespace_info',
    'status'])
Backup._all_fields_ = [
    ('backup_id', Backup.backup_id.validator),
    ('name', Backup.name.validator),
    ('namespace_info', Backup.namespace_info.validator),
    ('status', Backup.status.validator)]
BackupConflictInfo.path.validator = files.Path_validator
BackupConflictInfo.fileid.validator = files.FileId_validator
BackupConflictInfo._all_field_names_ = set([
    'path',
    'fileid'])
BackupConflictInfo._all_fields_ = [
    ('path', BackupConflictInfo.path.validator),
    ('fileid', BackupConflictInfo.fileid.validator)]
BackupStatus._created_validator = bv.Void()
BackupStatus._in_progress_validator = bv.Void()
BackupStatus._completed_validator = bv.Void()
BackupStatus._broken_validator = bv.Void()
BackupStatus._other_validator = bv.Void()
BackupStatus._tagmap = {
    'created': BackupStatus._created_validator,
    'in_progress': BackupStatus._in_progress_validator,
    'completed': BackupStatus._completed_validator,
    'broken': BackupStatus._broken_validator,
    'other': BackupStatus._other_validator }
BackupStatus.created = BackupStatus('created')
BackupStatus.in_progress = BackupStatus('in_progress')
BackupStatus.completed = BackupStatus('completed')
BackupStatus.broken = BackupStatus('broken')
BackupStatus.other = BackupStatus('other')
ClearAllQuotaExemptError._quota_exempt_error_validator = device_sync.QuotaExemptError_validator
ClearAllQuotaExemptError._other_validator = bv.Void()
ClearAllQuotaExemptError._tagmap = {
    'quota_exempt_error': ClearAllQuotaExemptError._quota_exempt_error_validator,
    'other': ClearAllQuotaExemptError._other_validator }
ClearAllQuotaExemptError.other = ClearAllQuotaExemptError('other')
ClearableString._value_validator = bv.String()
ClearableString._value_validator._redact = bv.BlotRedactor(None)
ClearableString._clear_validator = bv.Void()
ClearableString._other_validator = bv.Void()
ClearableString._tagmap = {
    'value': ClearableString._value_validator,
    'clear': ClearableString._clear_validator,
    'other': ClearableString._other_validator }
ClearableString.clear = ClearableString('clear')
ClearableString.other = ClearableString('other')
ClearableUInt64._value_validator = bv.UInt64()
ClearableUInt64._value_validator._redact = bv.BlotRedactor(None)
ClearableUInt64._clear_validator = bv.Void()
ClearableUInt64._other_validator = bv.Void()
ClearableUInt64._tagmap = {
    'value': ClearableUInt64._value_validator,
    'clear': ClearableUInt64._clear_validator,
    'other': ClearableUInt64._other_validator }
ClearableUInt64.clear = ClearableUInt64('clear')
ClearableUInt64.other = ClearableUInt64('other')
CreateBackupArg.device_id.validator = device_sync.DeviceId_validator
CreateBackupArg.drive_uuid.validator = bv.String()
CreateBackupArg.drive_uuid.validator._redact = bv.BlotRedactor(None)
CreateBackupArg.drive_name.validator = bv.String()
CreateBackupArg.drive_name.validator._redact = bv.BlotRedactor(None)
CreateBackupArg.fs_type.validator = bv.String()
CreateBackupArg.fs_type.validator._redact = bv.BlotRedactor(None)
CreateBackupArg.supports_backup_root.validator = bv.Boolean()
CreateBackupArg.supports_backup_root.validator._redact = bv.BlotRedactor(None)
CreateBackupArg._all_field_names_ = set([
    'device_id',
    'drive_uuid',
    'drive_name',
    'fs_type',
    'supports_backup_root'])
CreateBackupArg._all_fields_ = [
    ('device_id', CreateBackupArg.device_id.validator),
    ('drive_uuid', CreateBackupArg.drive_uuid.validator),
    ('drive_name', CreateBackupArg.drive_name.validator),
    ('fs_type', CreateBackupArg.fs_type.validator),
    ('supports_backup_root', CreateBackupArg.supports_backup_root.validator)]
CreateBackupError._invalid_request_validator = InvalidRequestError_validator
CreateBackupError._internal_error_validator = device_sync.InternalError_validator
CreateBackupError._create_error_validator = bv.Void()
CreateBackupError._es_update_conflict_validator = bv.Void()
CreateBackupError._non_fission_client_with_fission_anchor_validator = bv.Void()
CreateBackupError._fission_client_with_non_fission_anchor_validator = bv.Void()
CreateBackupError._audit_log_error_validator = bv.Void()
CreateBackupError._other_validator = bv.Void()
CreateBackupError._tagmap = {
    'invalid_request': CreateBackupError._invalid_request_validator,
    'internal_error': CreateBackupError._internal_error_validator,
    'create_error': CreateBackupError._create_error_validator,
    'es_update_conflict': CreateBackupError._es_update_conflict_validator,
    'non_fission_client_with_fission_anchor': CreateBackupError._non_fission_client_with_fission_anchor_validator,
    'fission_client_with_non_fission_anchor': CreateBackupError._fission_client_with_non_fission_anchor_validator,
    'audit_log_error': CreateBackupError._audit_log_error_validator,
    'other': CreateBackupError._other_validator }
CreateBackupError.create_error = CreateBackupError('create_error')
CreateBackupError.es_update_conflict = CreateBackupError('es_update_conflict')
CreateBackupError.non_fission_client_with_fission_anchor = CreateBackupError('non_fission_client_with_fission_anchor')
CreateBackupError.fission_client_with_non_fission_anchor = CreateBackupError('fission_client_with_non_fission_anchor')
CreateBackupError.audit_log_error = CreateBackupError('audit_log_error')
CreateBackupError.other = CreateBackupError('other')
CreateBackupResult.create_backup_result.validator = bv.Nullable(CreateBackupWithBackupRootInfo_validator)
CreateBackupResult._all_field_names_ = set([
    'create_backup_result'])
CreateBackupResult._all_fields_ = [
    ('create_backup_result', CreateBackupResult.create_backup_result.validator)]
CreateBackupWithBackupRootInfo.anchor_fileid.validator = files.FileId_validator
CreateBackupWithBackupRootInfo.anchor_path.validator = files.Path_validator
CreateBackupWithBackupRootInfo.mount_point_fileid.validator = files.FileId_validator
CreateBackupWithBackupRootInfo.mount_point_path.validator = files.Path_validator
CreateBackupWithBackupRootInfo._all_field_names_ = set([
    'anchor_fileid',
    'anchor_path',
    'mount_point_fileid',
    'mount_point_path'])
CreateBackupWithBackupRootInfo._all_fields_ = [
    ('anchor_fileid', CreateBackupWithBackupRootInfo.anchor_fileid.validator),
    ('anchor_path', CreateBackupWithBackupRootInfo.anchor_path.validator),
    ('mount_point_fileid', CreateBackupWithBackupRootInfo.mount_point_fileid.validator),
    ('mount_point_path', CreateBackupWithBackupRootInfo.mount_point_path.validator)]
DanglingFolder.file_id.validator = files.FileId_validator
DanglingFolder.fq_path.validator = bv.String()
DanglingFolder.fq_path.validator._redact = bv.BlotRedactor(None)
DanglingFolder.root_ns_id.validator = bv.Nullable(NamespaceId_validator)
DanglingFolder._all_field_names_ = set([
    'file_id',
    'fq_path',
    'root_ns_id'])
DanglingFolder._all_fields_ = [
    ('file_id', DanglingFolder.file_id.validator),
    ('fq_path', DanglingFolder.fq_path.validator),
    ('root_ns_id', DanglingFolder.root_ns_id.validator)]
DeleteBackupArg.anchor_fileid.validator = files.FileId_validator
DeleteBackupArg._all_field_names_ = set([
    'anchor_fileid'])
DeleteBackupArg._all_fields_ = [
    ('anchor_fileid', DeleteBackupArg.anchor_fileid.validator)]
DeleteBackupError._invalid_request_validator = InvalidRequestError_validator
DeleteBackupError._internal_error_validator = device_sync.InternalError_validator
DeleteBackupError._not_latest_validator = bv.Void()
DeleteBackupError._transient_error_validator = bv.Void()
DeleteBackupError._delete_error_validator = bv.Void()
DeleteBackupError._folder_lookup_error_validator = files.LookupError_validator
DeleteBackupError._other_validator = bv.Void()
DeleteBackupError._tagmap = {
    'invalid_request': DeleteBackupError._invalid_request_validator,
    'internal_error': DeleteBackupError._internal_error_validator,
    'not_latest': DeleteBackupError._not_latest_validator,
    'transient_error': DeleteBackupError._transient_error_validator,
    'delete_error': DeleteBackupError._delete_error_validator,
    'folder_lookup_error': DeleteBackupError._folder_lookup_error_validator,
    'other': DeleteBackupError._other_validator }
DeleteBackupError.not_latest = DeleteBackupError('not_latest')
DeleteBackupError.transient_error = DeleteBackupError('transient_error')
DeleteBackupError.delete_error = DeleteBackupError('delete_error')
DeleteBackupError.other = DeleteBackupError('other')
DeleteBackupResult.xop_id.validator = bv.String()
DeleteBackupResult.xop_id.validator._redact = bv.BlotRedactor(None)
DeleteBackupResult._all_field_names_ = set([
    'xop_id'])
DeleteBackupResult._all_fields_ = [
    ('xop_id', DeleteBackupResult.xop_id.validator)]
DriveInfo.account_subscription.validator = bv.String()
DriveInfo.account_subscription.validator._redact = bv.BlotRedactor(None)
DriveInfo.device_protocol.validator = bv.Nullable(bv.String())
DriveInfo.device_vendor.validator = bv.Nullable(bv.String())
DriveInfo.is_business_domain.validator = bv.Nullable(bv.Boolean())
DriveInfo.media_removable.validator = bv.Nullable(bv.Boolean())
DriveInfo.platform.validator = bv.Nullable(bv.String())
DriveInfo.quota_percent.validator = bv.Float64()
DriveInfo.quota_percent.validator._redact = bv.BlotRedactor(None)
DriveInfo.shared_quota_frac.validator = bv.Float64()
DriveInfo.shared_quota_frac.validator._redact = bv.BlotRedactor(None)
DriveInfo.total_quota_usage.validator = bv.Float64()
DriveInfo.total_quota_usage.validator._redact = bv.BlotRedactor(None)
DriveInfo.volume_capacity.validator = bv.Float64()
DriveInfo.volume_capacity.validator._redact = bv.BlotRedactor(None)
DriveInfo.volume_fs_type.validator = bv.String()
DriveInfo.volume_fs_type.validator._redact = bv.BlotRedactor(None)
DriveInfo.volume_usage.validator = bv.Float64()
DriveInfo.volume_usage.validator._redact = bv.BlotRedactor(None)
DriveInfo._all_field_names_ = set([
    'account_subscription',
    'device_protocol',
    'device_vendor',
    'is_business_domain',
    'media_removable',
    'platform',
    'quota_percent',
    'shared_quota_frac',
    'total_quota_usage',
    'volume_capacity',
    'volume_fs_type',
    'volume_usage'])
DriveInfo._all_fields_ = [
    ('account_subscription', DriveInfo.account_subscription.validator),
    ('device_protocol', DriveInfo.device_protocol.validator),
    ('device_vendor', DriveInfo.device_vendor.validator),
    ('is_business_domain', DriveInfo.is_business_domain.validator),
    ('media_removable', DriveInfo.media_removable.validator),
    ('platform', DriveInfo.platform.validator),
    ('quota_percent', DriveInfo.quota_percent.validator),
    ('shared_quota_frac', DriveInfo.shared_quota_frac.validator),
    ('total_quota_usage', DriveInfo.total_quota_usage.validator),
    ('volume_capacity', DriveInfo.volume_capacity.validator),
    ('volume_fs_type', DriveInfo.volume_fs_type.validator),
    ('volume_usage', DriveInfo.volume_usage.validator)]
EligibleMigrationType._not_eligible_validator = NotEligibleMigrationEnum_validator
EligibleMigrationType._move_eligible_validator = bv.Void()
EligibleMigrationType._copy_eligible_validator = bv.Void()
EligibleMigrationType._other_validator = bv.Void()
EligibleMigrationType._tagmap = {
    'not_eligible': EligibleMigrationType._not_eligible_validator,
    'move_eligible': EligibleMigrationType._move_eligible_validator,
    'copy_eligible': EligibleMigrationType._copy_eligible_validator,
    'other': EligibleMigrationType._other_validator }
EligibleMigrationType.move_eligible = EligibleMigrationType('move_eligible')
EligibleMigrationType.copy_eligible = EligibleMigrationType('copy_eligible')
EligibleMigrationType.other = EligibleMigrationType('other')
ExternalDriveBackupStateEnum._active_validator = bv.Void()
ExternalDriveBackupStateEnum._unplugged_validator = bv.Void()
ExternalDriveBackupStateEnum._account_overquota_validator = bv.Void()
ExternalDriveBackupStateEnum._backup_paused_validator = bv.Void()
ExternalDriveBackupStateEnum._sync_paused_validator = bv.Void()
ExternalDriveBackupStateEnum._broken_validator = bv.Void()
ExternalDriveBackupStateEnum._broken_server_deleted_validator = bv.Void()
ExternalDriveBackupStateEnum._backup_hung_type_nucleus_reason_resolver_validator = bv.Void()
ExternalDriveBackupStateEnum._backup_hung_type_nucleus_reason_reindexer_validator = bv.Void()
ExternalDriveBackupStateEnum._backup_hung_type_nucleus_reason_frontier_validator = bv.Void()
ExternalDriveBackupStateEnum._backup_hung_type_nucleus_reason_unknown_validator = bv.Void()
ExternalDriveBackupStateEnum._backup_hung_type_edb_reason_resolver_validator = bv.Void()
ExternalDriveBackupStateEnum._backup_hung_type_edb_reason_reindexer_validator = bv.Void()
ExternalDriveBackupStateEnum._backup_hung_type_edb_reason_frontier_validator = bv.Void()
ExternalDriveBackupStateEnum._backup_hung_type_edb_reason_unknown_validator = bv.Void()
ExternalDriveBackupStateEnum._deleted_validator = bv.Void()
ExternalDriveBackupStateEnum._permanently_failed_validator = bv.Void()
ExternalDriveBackupStateEnum._other_validator = bv.Void()
# WARNING: Decompyle incomplete
