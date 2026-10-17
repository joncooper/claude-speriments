# Source Generated with Decompyle++
# File: device_sync.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import files

class AnchorsBackupError(bb.Union):
    pass
# WARNING: Decompyle incomplete

AnchorsBackupError_validator = bv.Union(AnchorsBackupError)

class AsyncCopyTransientError(bb.Union):
    pass
# WARNING: Decompyle incomplete

AsyncCopyTransientError_validator = bv.Union(AsyncCopyTransientError)

class BackupDisableType(bb.Union):
    pass
# WARNING: Decompyle incomplete

BackupDisableType_validator = bv.Union(BackupDisableType)

class BackupInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BackupInfo_validator = bv.Struct(BackupInfo)

class BackupRootInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BackupRootInfo_validator = bv.Struct(BackupRootInfo)

class BackupSchedule(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BackupSchedule_validator = bv.Struct(BackupSchedule)

class ClearAllQuotaExemptError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ClearAllQuotaExemptError_validator = bv.Union(ClearAllQuotaExemptError)

class ClearableUInt64(bb.Union):
    pass
# WARNING: Decompyle incomplete

ClearableUInt64_validator = bv.Union(ClearableUInt64)

class ClientMetricsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ClientMetricsArg_validator = bv.Struct(ClientMetricsArg)

class CompleteRestoreDeviceArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CompleteRestoreDeviceArg_validator = bv.Struct(CompleteRestoreDeviceArg)

class ComputeDeviceNameArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ComputeDeviceNameArg_validator = bv.Struct(ComputeDeviceNameArg)

class ComputeDeviceNameResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ComputeDeviceNameResult_validator = bv.Struct(ComputeDeviceNameResult)

class ComputerBackupFolder(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ComputerBackupFolder_validator = bv.Struct(ComputerBackupFolder)

class ComputerBackupFolderInput(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ComputerBackupFolderInput_validator = bv.Struct(ComputerBackupFolderInput)

class ComputerBackupFolderRestoreEntry(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ComputerBackupFolderRestoreEntry_validator = bv.Struct(ComputerBackupFolderRestoreEntry)

class ComputerBackupFolderState(bb.Union):
    pass
# WARNING: Decompyle incomplete

ComputerBackupFolderState_validator = bv.Union(ComputerBackupFolderState)

class ComputerBackupFolderThirdPartyProvider(bb.Union):
    pass
# WARNING: Decompyle incomplete

ComputerBackupFolderThirdPartyProvider_validator = bv.Union(ComputerBackupFolderThirdPartyProvider)

class ComputerBackupFolderType(bb.Union):
    pass
# WARNING: Decompyle incomplete

ComputerBackupFolderType_validator = bv.Union(ComputerBackupFolderType)

class ComputerBackupState(bb.Union):
    pass
# WARNING: Decompyle incomplete

ComputerBackupState_validator = bv.Union(ComputerBackupState)

class DeviceConflictError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DeviceConflictError_validator = bv.Union(DeviceConflictError)

class DeviceStatusArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeviceStatusArg_validator = bv.Struct(DeviceStatusArg)

class DeviceStatusError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DeviceStatusError_validator = bv.Union(DeviceStatusError)

class DeviceSyncResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeviceSyncResult_validator = bv.Struct(DeviceSyncResult)

class DeviceSyncStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

DeviceSyncStatus_validator = bv.Union(DeviceSyncStatus)

class DisableDeviceArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DisableDeviceArg_validator = bv.Struct(DisableDeviceArg)

class DisableDeviceError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DisableDeviceError_validator = bv.Union(DisableDeviceError)

class DisableDeviceMetric(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DisableDeviceMetric_validator = bv.Struct(DisableDeviceMetric)

class EmailType(bb.Union):
    pass
# WARNING: Decompyle incomplete

EmailType_validator = bv.Union(EmailType)

class EnableDeviceArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EnableDeviceArg_validator = bv.Struct(EnableDeviceArg)

class EnableDeviceError(bb.Union):
    pass
# WARNING: Decompyle incomplete

EnableDeviceError_validator = bv.Union(EnableDeviceError)

class ExclusionFileExtension(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ExclusionFileExtension_validator = bv.Struct(ExclusionFileExtension)

class ExclusionListArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ExclusionListArg_validator = bv.Struct(ExclusionListArg)

class ExclusionListResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ExclusionListResult_validator = bv.Struct(ExclusionListResult)

class FolderStatus(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FolderStatus_validator = bv.Struct(FolderStatus)

class ForceDisableBackupArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ForceDisableBackupArg_validator = bv.Struct(ForceDisableBackupArg)

class ForceDisableBackupError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ForceDisableBackupError_validator = bv.Union(ForceDisableBackupError)

class GetBackupRootInfoError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetBackupRootInfoError_validator = bv.Union(GetBackupRootInfoError)

class GetBackupRootInfoResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetBackupRootInfoResult_validator = bv.Struct(GetBackupRootInfoResult)

class GetBackupSubscriptionTimestampError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetBackupSubscriptionTimestampError_validator = bv.Union(GetBackupSubscriptionTimestampError)

class GetBackupSubscriptionTimestampResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetBackupSubscriptionTimestampResult_validator = bv.Struct(GetBackupSubscriptionTimestampResult)

class IcRemediationMetric(bb.Struct):
    pass
# WARNING: Decompyle incomplete

IcRemediationMetric_validator = bv.Struct(IcRemediationMetric)

class InternalError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InternalError_validator = bv.Struct(InternalError)

class InvalidRequestError(bb.Union):
    pass
# WARNING: Decompyle incomplete

InvalidRequestError_validator = bv.Union(InvalidRequestError)

class ListBackupsArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListBackupsArgs_validator = bv.Struct(ListBackupsArgs)

class ListBackupsResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListBackupsResult_validator = bv.Struct(ListBackupsResult)

class Metric(bb.Union):
    pass
# WARNING: Decompyle incomplete

Metric_validator = bv.Union(Metric)

class NamespaceInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

NamespaceInfo_validator = bv.Struct(NamespaceInfo)

class PingServerArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PingServerArg_validator = bv.Struct(PingServerArg)

class PingServerResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PingServerResult_validator = bv.Struct(PingServerResult)

class PlatformType(bb.Union):
    pass
# WARNING: Decompyle incomplete

PlatformType_validator = bv.Union(PlatformType)

class PrepareRestoreBackupError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PrepareRestoreBackupError_validator = bv.Union(PrepareRestoreBackupError)

class QuotaExemptError(bb.Union):
    pass
# WARNING: Decompyle incomplete

QuotaExemptError_validator = bv.Union(QuotaExemptError)

class RestoreBackupError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RestoreBackupError_validator = bv.Union(RestoreBackupError)

class RestoreBackupPerFolderError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RestoreBackupPerFolderError_validator = bv.Union(RestoreBackupPerFolderError)

class RestoreBackupPerFolderErrorPair(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RestoreBackupPerFolderErrorPair_validator = bv.Struct(RestoreBackupPerFolderErrorPair)

class RestoreBackupValidationError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RestoreBackupValidationError_validator = bv.Union(RestoreBackupValidationError)

class RestoreComputerBackupArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RestoreComputerBackupArg_validator = bv.Struct(RestoreComputerBackupArg)

class RestoreComputerBackupError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RestoreComputerBackupError_validator = bv.Union(RestoreComputerBackupError)

class RestoreComputerBackupFolderInput(bb.Union):
    pass
# WARNING: Decompyle incomplete

RestoreComputerBackupFolderInput_validator = bv.Union(RestoreComputerBackupFolderInput)

class RestoreFolder(bb.Union):
    pass
# WARNING: Decompyle incomplete

RestoreFolder_validator = bv.Union(RestoreFolder)

class ScheduleDetail(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ScheduleDetail_validator = bv.Struct(ScheduleDetail)

class ScheduleType(bb.Union):
    pass
# WARNING: Decompyle incomplete

ScheduleType_validator = bv.Union(ScheduleType)

class SendEmailArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SendEmailArg_validator = bv.Struct(SendEmailArg)

class SetQuotaExemptArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SetQuotaExemptArg_validator = bv.Struct(SetQuotaExemptArg)

class SetQuotaExemptError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SetQuotaExemptError_validator = bv.Union(SetQuotaExemptError)

class StartRestoreDeviceArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StartRestoreDeviceArg_validator = bv.Struct(StartRestoreDeviceArg)

class Status(bb.Union):
    pass
# WARNING: Decompyle incomplete

Status_validator = bv.Union(Status)

class SyncFolder(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SyncFolder_validator = bv.Struct(SyncFolder)

class SyncFolderStatus(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SyncFolderStatus_validator = bv.Struct(SyncFolderStatus)

class SyncFolderType(bb.Union):
    pass
# WARNING: Decompyle incomplete

SyncFolderType_validator = bv.Union(SyncFolderType)

class UpdateAnchorInfoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateAnchorInfoArg_validator = bv.Struct(UpdateAnchorInfoArg)

class UpdateAnchorInfoError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UpdateAnchorInfoError_validator = bv.Union(UpdateAnchorInfoError)

class UpdateAnchorStateInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateAnchorStateInfo_validator = bv.Struct(UpdateAnchorStateInfo)

class UpdateComputerBackupArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateComputerBackupArg_validator = bv.Struct(UpdateComputerBackupArg)

class UpdateComputerBackupResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateComputerBackupResult_validator = bv.Struct(UpdateComputerBackupResult)

class UpdateComputerBackupResultInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateComputerBackupResultInfo_validator = bv.Struct(UpdateComputerBackupResultInfo)

class UpdateDeviceMetric(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateDeviceMetric_validator = bv.Struct(UpdateDeviceMetric)

class UpdateDisplayNameArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateDisplayNameArg_validator = bv.Struct(UpdateDisplayNameArg)

class UpdateDisplayNameError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UpdateDisplayNameError_validator = bv.Union(UpdateDisplayNameError)

class UpdateSyncProgressPercentageArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateSyncProgressPercentageArg_validator = bv.Struct(UpdateSyncProgressPercentageArg)

class UpdateSyncProgressPercentageError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UpdateSyncProgressPercentageError_validator = bv.Union(UpdateSyncProgressPercentageError)
DeviceId_validator = bv.String(pattern = '[a-fA-F0-9]{8}(-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}')
DeviceId_validator._redact = bv.BlotRedactor(None)
DeviceName_validator = bv.String(pattern = '(.|[\\r\\n])*')
DeviceName_validator._redact = bv.BlotRedactor(None)
NsId_validator = bv.UInt64()
NsId_validator._redact = bv.BlotRedactor(None)
SyncFolderName_validator = bv.String(pattern = '(.|[\\r\\n])*')
SyncFolderName_validator._redact = bv.BlotRedactor(None)
AnchorsBackupError._active_non_anchors_state_validator = bv.Void()
AnchorsBackupError._backup_parent_missing_validator = bv.Void()
AnchorsBackupError._backup_parent_wrong_ns_validator = bv.Void()
AnchorsBackupError._backup_parent_moved_validator = bv.Void()
AnchorsBackupError._other_validator = bv.Void()
AnchorsBackupError._tagmap = {
    'active_non_anchors_state': AnchorsBackupError._active_non_anchors_state_validator,
    'backup_parent_missing': AnchorsBackupError._backup_parent_missing_validator,
    'backup_parent_wrong_ns': AnchorsBackupError._backup_parent_wrong_ns_validator,
    'backup_parent_moved': AnchorsBackupError._backup_parent_moved_validator,
    'other': AnchorsBackupError._other_validator }
AnchorsBackupError.active_non_anchors_state = AnchorsBackupError('active_non_anchors_state')
AnchorsBackupError.backup_parent_missing = AnchorsBackupError('backup_parent_missing')
AnchorsBackupError.backup_parent_wrong_ns = AnchorsBackupError('backup_parent_wrong_ns')
AnchorsBackupError.backup_parent_moved = AnchorsBackupError('backup_parent_moved')
AnchorsBackupError.other = AnchorsBackupError('other')
AsyncCopyTransientError._failed_folders_validator = bv.List(SyncFolder_validator)
AsyncCopyTransientError._other_validator = bv.Void()
AsyncCopyTransientError._tagmap = {
    'failed_folders': AsyncCopyTransientError._failed_folders_validator,
    'other': AsyncCopyTransientError._other_validator }
AsyncCopyTransientError.other = AsyncCopyTransientError('other')
BackupDisableType._quota_exempt_validator = bv.Void()
BackupDisableType._other_validator = bv.Void()
BackupDisableType._tagmap = {
    'quota_exempt': BackupDisableType._quota_exempt_validator,
    'other': BackupDisableType._other_validator }
BackupDisableType.quota_exempt = BackupDisableType('quota_exempt')
BackupDisableType.other = BackupDisableType('other')
BackupInfo.device_id.validator = DeviceId_validator
BackupInfo.device_status.validator = DeviceSyncStatus_validator
BackupInfo.name.validator = DeviceName_validator
BackupInfo.display_name.validator = bv.Nullable(bv.String())
BackupInfo.quota_exempt.validator = bv.Boolean()
BackupInfo.quota_exempt.validator._redact = bv.BlotRedactor(None)
BackupInfo.backup_disable_type.validator = bv.Nullable(BackupDisableType_validator)
BackupInfo.device_backup_platform.validator = PlatformType_validator
BackupInfo.sync_folders.validator = bv.List(SyncFolder_validator)
BackupInfo.last_timestamp_utc.validator = bv.Nullable(bv.UInt64())
BackupInfo.root_fileid.validator = files.FileId_validator
BackupInfo.anchor_folders.validator = bv.List(ComputerBackupFolder_validator)
BackupInfo.backup_state.validator = bv.Nullable(ComputerBackupState_validator)
BackupInfo.root_ns_id.validator = bv.Nullable(NsId_validator)
BackupInfo.backup_schedule.validator = bv.Nullable(BackupSchedule_validator)
BackupInfo.sync_progress_percentage.validator = bv.Nullable(bv.UInt64())
BackupInfo.sync_progress_last_checked_utc.validator = bv.Nullable(bv.UInt64())
BackupInfo._all_field_names_ = set([
    'device_id',
    'device_status',
    'name',
    'display_name',
    'quota_exempt',
    'backup_disable_type',
    'device_backup_platform',
    'sync_folders',
    'last_timestamp_utc',
    'root_fileid',
    'anchor_folders',
    'backup_state',
    'root_ns_id',
    'backup_schedule',
    'sync_progress_percentage',
    'sync_progress_last_checked_utc'])
BackupInfo._all_fields_ = [
    ('device_id', BackupInfo.device_id.validator),
    ('device_status', BackupInfo.device_status.validator),
    ('name', BackupInfo.name.validator),
    ('display_name', BackupInfo.display_name.validator),
    ('quota_exempt', BackupInfo.quota_exempt.validator),
    ('backup_disable_type', BackupInfo.backup_disable_type.validator),
    ('device_backup_platform', BackupInfo.device_backup_platform.validator),
    ('sync_folders', BackupInfo.sync_folders.validator),
    ('last_timestamp_utc', BackupInfo.last_timestamp_utc.validator),
    ('root_fileid', BackupInfo.root_fileid.validator),
    ('anchor_folders', BackupInfo.anchor_folders.validator),
    ('backup_state', BackupInfo.backup_state.validator),
    ('root_ns_id', BackupInfo.root_ns_id.validator),
    ('backup_schedule', BackupInfo.backup_schedule.validator),
    ('sync_progress_percentage', BackupInfo.sync_progress_percentage.validator),
    ('sync_progress_last_checked_utc', BackupInfo.sync_progress_last_checked_utc.validator)]
BackupRootInfo.namespace_info.validator = bv.Nullable(NamespaceInfo_validator)
BackupRootInfo._all_field_names_ = set([
    'namespace_info'])
BackupRootInfo._all_fields_ = [
    ('namespace_info', BackupRootInfo.namespace_info.validator)]
BackupSchedule.type.validator = ScheduleType_validator
BackupSchedule.schedule.validator = ScheduleDetail_validator
BackupSchedule._all_field_names_ = set([
    'type',
    'schedule'])
BackupSchedule._all_fields_ = [
    ('type', BackupSchedule.type.validator),
    ('schedule', BackupSchedule.schedule.validator)]
ClearAllQuotaExemptError._quota_exempt_error_validator = QuotaExemptError_validator
ClearAllQuotaExemptError._other_validator = bv.Void()
ClearAllQuotaExemptError._tagmap = {
    'quota_exempt_error': ClearAllQuotaExemptError._quota_exempt_error_validator,
    'other': ClearAllQuotaExemptError._other_validator }
ClearAllQuotaExemptError.other = ClearAllQuotaExemptError('other')
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
ClientMetricsArg.metrics.validator = bv.List(Metric_validator)
ClientMetricsArg._all_field_names_ = set([
    'metrics'])
ClientMetricsArg._all_fields_ = [
    ('metrics', ClientMetricsArg.metrics.validator)]
CompleteRestoreDeviceArg.enable_device_args.validator = EnableDeviceArg_validator
CompleteRestoreDeviceArg.restore_device_id.validator = DeviceId_validator
CompleteRestoreDeviceArg._all_field_names_ = set([
    'enable_device_args',
    'restore_device_id'])
CompleteRestoreDeviceArg._all_fields_ = [
    ('enable_device_args', CompleteRestoreDeviceArg.enable_device_args.validator),
    ('restore_device_id', CompleteRestoreDeviceArg.restore_device_id.validator)]
ComputeDeviceNameArg.device_name_base.validator = bv.String()
ComputeDeviceNameArg.device_name_base.validator._redact = bv.BlotRedactor(None)
ComputeDeviceNameArg._all_field_names_ = set([
    'device_name_base'])
ComputeDeviceNameArg._all_fields_ = [
    ('device_name_base', ComputeDeviceNameArg.device_name_base.validator)]
ComputeDeviceNameResult.device_name.validator = bv.String()
ComputeDeviceNameResult.device_name.validator._redact = bv.BlotRedactor(None)
ComputeDeviceNameResult._all_field_names_ = set([
    'device_name'])
ComputeDeviceNameResult._all_fields_ = [
    ('device_name', ComputeDeviceNameResult.device_name.validator)]
ComputerBackupFolder.mount_fileid.validator = files.FileId_validator
ComputerBackupFolder.root_entry_fileid.validator = files.FileId_validator
ComputerBackupFolder.anchor_path.validator = bv.Nullable(files.Path_validator)
ComputerBackupFolder.folder_type.validator = ComputerBackupFolderType_validator
ComputerBackupFolder.folder_path.validator = bv.String()
ComputerBackupFolder.folder_path.validator._redact = bv.BlotRedactor(None)
ComputerBackupFolder.folder_name.validator = bv.String()
ComputerBackupFolder.folder_name.validator._redact = bv.BlotRedactor(None)
ComputerBackupFolder.folder_state.validator = ComputerBackupFolderState_validator
ComputerBackupFolder.folder_third_party_providers.validator = bv.Nullable(bv.List(ComputerBackupFolderThirdPartyProvider_validator))
ComputerBackupFolder._all_field_names_ = set([
    'mount_fileid',
    'root_entry_fileid',
    'anchor_path',
    'folder_type',
    'folder_path',
    'folder_name',
    'folder_state',
    'folder_third_party_providers'])
ComputerBackupFolder._all_fields_ = [
    ('mount_fileid', ComputerBackupFolder.mount_fileid.validator),
    ('root_entry_fileid', ComputerBackupFolder.root_entry_fileid.validator),
    ('anchor_path', ComputerBackupFolder.anchor_path.validator),
    ('folder_type', ComputerBackupFolder.folder_type.validator),
    ('folder_path', ComputerBackupFolder.folder_path.validator),
    ('folder_name', ComputerBackupFolder.folder_name.validator),
    ('folder_state', ComputerBackupFolder.folder_state.validator),
    ('folder_third_party_providers', ComputerBackupFolder.folder_third_party_providers.validator)]
ComputerBackupFolderInput.folder_type.validator = ComputerBackupFolderType_validator
ComputerBackupFolderInput.folder_path.validator = bv.String()
ComputerBackupFolderInput.folder_path.validator._redact = bv.BlotRedactor(None)
ComputerBackupFolderInput.folder_name.validator = bv.String()
ComputerBackupFolderInput.folder_name.validator._redact = bv.BlotRedactor(None)
ComputerBackupFolderInput.folder_third_party_providers.validator = bv.Nullable(bv.List(ComputerBackupFolderThirdPartyProvider_validator))
ComputerBackupFolderInput.existing_fileid.validator = bv.Nullable(files.FileId_validator)
ComputerBackupFolderInput._all_field_names_ = set([
    'folder_type',
    'folder_path',
    'folder_name',
    'folder_third_party_providers',
    'existing_fileid'])
ComputerBackupFolderInput._all_fields_ = [
    ('folder_type', ComputerBackupFolderInput.folder_type.validator),
    ('folder_path', ComputerBackupFolderInput.folder_path.validator),
    ('folder_name', ComputerBackupFolderInput.folder_name.validator),
    ('folder_third_party_providers', ComputerBackupFolderInput.folder_third_party_providers.validator),
    ('existing_fileid', ComputerBackupFolderInput.existing_fileid.validator)]
ComputerBackupFolderRestoreEntry.folder_name.validator = bv.String()
ComputerBackupFolderRestoreEntry.folder_name.validator._redact = bv.BlotRedactor(None)
ComputerBackupFolderRestoreEntry.folder_type.validator = ComputerBackupFolderType_validator
ComputerBackupFolderRestoreEntry._all_field_names_ = set([
    'folder_name',
    'folder_type'])
ComputerBackupFolderRestoreEntry._all_fields_ = [
    ('folder_name', ComputerBackupFolderRestoreEntry.folder_name.validator),
    ('folder_type', ComputerBackupFolderRestoreEntry.folder_type.validator)]
ComputerBackupFolderState._created_validator = bv.Void()
ComputerBackupFolderState._active_validator = bv.Void()
ComputerBackupFolderState._broken_validator = bv.Void()
ComputerBackupFolderState._deleted_validator = bv.Void()
ComputerBackupFolderState._other_validator = bv.Void()
ComputerBackupFolderState._tagmap = {
    'created': ComputerBackupFolderState._created_validator,
    'active': ComputerBackupFolderState._active_validator,
    'broken': ComputerBackupFolderState._broken_validator,
    'deleted': ComputerBackupFolderState._deleted_validator,
    'other': ComputerBackupFolderState._other_validator }
ComputerBackupFolderState.created = ComputerBackupFolderState('created')
ComputerBackupFolderState.active = ComputerBackupFolderState('active')
ComputerBackupFolderState.broken = ComputerBackupFolderState('broken')
ComputerBackupFolderState.deleted = ComputerBackupFolderState('deleted')
ComputerBackupFolderState.other = ComputerBackupFolderState('other')
ComputerBackupFolderThirdPartyProvider._one_drive_validator = bv.Void()
ComputerBackupFolderThirdPartyProvider._google_drive_validator = bv.Void()
ComputerBackupFolderThirdPartyProvider._icloud_validator = bv.Void()
ComputerBackupFolderThirdPartyProvider._other_validator = bv.Void()
ComputerBackupFolderThirdPartyProvider._tagmap = {
    'one_drive': ComputerBackupFolderThirdPartyProvider._one_drive_validator,
    'google_drive': ComputerBackupFolderThirdPartyProvider._google_drive_validator,
    'icloud': ComputerBackupFolderThirdPartyProvider._icloud_validator,
    'other': ComputerBackupFolderThirdPartyProvider._other_validator }
ComputerBackupFolderThirdPartyProvider.one_drive = ComputerBackupFolderThirdPartyProvider('one_drive')
ComputerBackupFolderThirdPartyProvider.google_drive = ComputerBackupFolderThirdPartyProvider('google_drive')
ComputerBackupFolderThirdPartyProvider.icloud = ComputerBackupFolderThirdPartyProvider('icloud')
ComputerBackupFolderThirdPartyProvider.other = ComputerBackupFolderThirdPartyProvider('other')
ComputerBackupFolderType._desktop_validator = bv.Void()
ComputerBackupFolderType._documents_validator = bv.Void()
ComputerBackupFolderType._pictures_validator = bv.Void()
ComputerBackupFolderType._downloads_validator = bv.Void()
ComputerBackupFolderType._music_validator = bv.Void()
ComputerBackupFolderType._videos_validator = bv.Void()
ComputerBackupFolderType._movies_validator = bv.Void()
ComputerBackupFolderType._custom_folder_validator = bv.Void()
ComputerBackupFolderType._other_validator = bv.Void()
ComputerBackupFolderType._tagmap = {
    'desktop': ComputerBackupFolderType._desktop_validator,
    'documents': ComputerBackupFolderType._documents_validator,
    'pictures': ComputerBackupFolderType._pictures_validator,
    'downloads': ComputerBackupFolderType._downloads_validator,
    'music': ComputerBackupFolderType._music_validator,
    'videos': ComputerBackupFolderType._videos_validator,
    'movies': ComputerBackupFolderType._movies_validator,
    'custom_folder': ComputerBackupFolderType._custom_folder_validator,
    'other': ComputerBackupFolderType._other_validator }
ComputerBackupFolderType.desktop = ComputerBackupFolderType('desktop')
ComputerBackupFolderType.documents = ComputerBackupFolderType('documents')
ComputerBackupFolderType.pictures = ComputerBackupFolderType('pictures')
ComputerBackupFolderType.downloads = ComputerBackupFolderType('downloads')
ComputerBackupFolderType.music = ComputerBackupFolderType('music')
ComputerBackupFolderType.videos = ComputerBackupFolderType('videos')
ComputerBackupFolderType.movies = ComputerBackupFolderType('movies')
ComputerBackupFolderType.custom_folder = ComputerBackupFolderType('custom_folder')
ComputerBackupFolderType.other = ComputerBackupFolderType('other')
ComputerBackupState._unknown_validator = bv.Void()
ComputerBackupState._created_validator = bv.Void()
ComputerBackupState._active_validator = bv.Void()
ComputerBackupState._backup_paused_validator = bv.Void()
ComputerBackupState._sync_paused_validator = bv.Void()
ComputerBackupState._broken_validator = bv.Void()
ComputerBackupState._unlinked_validator = bv.Void()
ComputerBackupState._other_validator = bv.Void()
ComputerBackupState._tagmap = {
    'unknown': ComputerBackupState._unknown_validator,
    'created': ComputerBackupState._created_validator,
    'active': ComputerBackupState._active_validator,
    'backup_paused': ComputerBackupState._backup_paused_validator,
    'sync_paused': ComputerBackupState._sync_paused_validator,
    'broken': ComputerBackupState._broken_validator,
    'unlinked': ComputerBackupState._unlinked_validator,
    'other': ComputerBackupState._other_validator }
ComputerBackupState.unknown = ComputerBackupState('unknown')
ComputerBackupState.created = ComputerBackupState('created')
ComputerBackupState.active = ComputerBackupState('active')
ComputerBackupState.backup_paused = ComputerBackupState('backup_paused')
ComputerBackupState.sync_paused = ComputerBackupState('sync_paused')
ComputerBackupState.broken = ComputerBackupState('broken')
ComputerBackupState.unlinked = ComputerBackupState('unlinked')
ComputerBackupState.other = ComputerBackupState('other')
DeviceConflictError._account_validator = bv.Void()
DeviceConflictError._name_validator = bv.Void()
DeviceConflictError._folder_validator = bv.Void()
DeviceConflictError._other_validator = bv.Void()
DeviceConflictError._tagmap = {
    'account': DeviceConflictError._account_validator,
    'name': DeviceConflictError._name_validator,
    'folder': DeviceConflictError._folder_validator,
    'other': DeviceConflictError._other_validator }
DeviceConflictError.account = DeviceConflictError('account')
DeviceConflictError.name = DeviceConflictError('name')
DeviceConflictError.folder = DeviceConflictError('folder')
DeviceConflictError.other = DeviceConflictError('other')
DeviceStatusArg.device_id.validator = DeviceId_validator
DeviceStatusArg.validate.validator = bv.Boolean()
DeviceStatusArg.validate.validator._redact = bv.BlotRedactor(None)
DeviceStatusArg._all_field_names_ = set([
    'device_id',
    'validate'])
DeviceStatusArg._all_fields_ = [
    ('device_id', DeviceStatusArg.device_id.validator),
    ('validate', DeviceStatusArg.validate.validator)]
DeviceStatusError._folder_lookup_error_validator = files.LookupError_validator
DeviceStatusError._device_invalid_validator = bv.Void()
DeviceStatusError._device_not_found_validator = bv.Void()
DeviceStatusError._internal_error_validator = InternalError_validator
DeviceStatusError._other_validator = bv.Void()
DeviceStatusError._tagmap = {
    'folder_lookup_error': DeviceStatusError._folder_lookup_error_validator,
    'device_invalid': DeviceStatusError._device_invalid_validator,
    'device_not_found': DeviceStatusError._device_not_found_validator,
    'internal_error': DeviceStatusError._internal_error_validator,
    'other': DeviceStatusError._other_validator }
DeviceStatusError.device_invalid = DeviceStatusError('device_invalid')
DeviceStatusError.device_not_found = DeviceStatusError('device_not_found')
DeviceStatusError.other = DeviceStatusError('other')
DeviceSyncResult.status.validator = DeviceSyncStatus_validator
DeviceSyncResult.name.validator = DeviceName_validator
DeviceSyncResult.root_folder.validator = FolderStatus_validator
DeviceSyncResult.sync_folders.validator = bv.List(SyncFolderStatus_validator)
DeviceSyncResult.quota_exempt.validator = bv.Boolean()
DeviceSyncResult.quota_exempt.validator._redact = bv.BlotRedactor(None)
DeviceSyncResult.backup_disable_type.validator = bv.Nullable(BackupDisableType_validator)
DeviceSyncResult.device_backup_platform.validator = PlatformType_validator
DeviceSyncResult._all_field_names_ = set([
    'status',
    'name',
    'root_folder',
    'sync_folders',
    'quota_exempt',
    'backup_disable_type',
    'device_backup_platform'])
DeviceSyncResult._all_fields_ = [
    ('status', DeviceSyncResult.status.validator),
    ('name', DeviceSyncResult.name.validator),
    ('root_folder', DeviceSyncResult.root_folder.validator),
    ('sync_folders', DeviceSyncResult.sync_folders.validator),
    ('quota_exempt', DeviceSyncResult.quota_exempt.validator),
    ('backup_disable_type', DeviceSyncResult.backup_disable_type.validator),
    ('device_backup_platform', DeviceSyncResult.device_backup_platform.validator)]
DeviceSyncStatus._enabled_validator = bv.Void()
DeviceSyncStatus._disabled_validator = bv.Void()
DeviceSyncStatus._other_validator = bv.Void()
DeviceSyncStatus._tagmap = {
    'enabled': DeviceSyncStatus._enabled_validator,
    'disabled': DeviceSyncStatus._disabled_validator,
    'other': DeviceSyncStatus._other_validator }
DeviceSyncStatus.enabled = DeviceSyncStatus('enabled')
DeviceSyncStatus.disabled = DeviceSyncStatus('disabled')
DeviceSyncStatus.other = DeviceSyncStatus('other')
DisableDeviceArg.device_id.validator = DeviceId_validator
DisableDeviceArg._all_field_names_ = set([
    'device_id'])
DisableDeviceArg._all_fields_ = [
    ('device_id', DisableDeviceArg.device_id.validator)]
DisableDeviceError._device_not_found_validator = bv.Void()
DisableDeviceError._device_conflict_validator = DeviceConflictError_validator
DisableDeviceError._folder_lookup_error_validator = files.LookupError_validator
DisableDeviceError._folder_update_error_validator = files.WriteError_validator
DisableDeviceError._update_conflict_validator = bv.Void()
DisableDeviceError._audit_log_error_validator = bv.Void()
DisableDeviceError._anchor_update_error_validator = bv.Void()
DisableDeviceError._internal_error_validator = InternalError_validator
DisableDeviceError._other_validator = bv.Void()
DisableDeviceError._tagmap = {
    'device_not_found': DisableDeviceError._device_not_found_validator,
    'device_conflict': DisableDeviceError._device_conflict_validator,
    'folder_lookup_error': DisableDeviceError._folder_lookup_error_validator,
    'folder_update_error': DisableDeviceError._folder_update_error_validator,
    'update_conflict': DisableDeviceError._update_conflict_validator,
    'audit_log_error': DisableDeviceError._audit_log_error_validator,
    'anchor_update_error': DisableDeviceError._anchor_update_error_validator,
    'internal_error': DisableDeviceError._internal_error_validator,
    'other': DisableDeviceError._other_validator }
DisableDeviceError.device_not_found = DisableDeviceError('device_not_found')
DisableDeviceError.update_conflict = DisableDeviceError('update_conflict')
DisableDeviceError.audit_log_error = DisableDeviceError('audit_log_error')
DisableDeviceError.anchor_update_error = DisableDeviceError('anchor_update_error')
DisableDeviceError.other = DisableDeviceError('other')
DisableDeviceMetric.status.validator = Status_validator
DisableDeviceMetric.count.validator = bv.Int32()
DisableDeviceMetric.count.validator._redact = bv.BlotRedactor(None)
DisableDeviceMetric.platform.validator = PlatformType_validator
DisableDeviceMetric.app_version.validator = bv.String()
DisableDeviceMetric.app_version.validator._redact = bv.BlotRedactor(None)
DisableDeviceMetric.build_channel.validator = bv.String()
DisableDeviceMetric.build_channel.validator._redact = bv.BlotRedactor(None)
DisableDeviceMetric._all_field_names_ = set([
    'status',
    'count',
    'platform',
    'app_version',
    'build_channel'])
DisableDeviceMetric._all_fields_ = [
    ('status', DisableDeviceMetric.status.validator),
    ('count', DisableDeviceMetric.count.validator),
    ('platform', DisableDeviceMetric.platform.validator),
    ('app_version', DisableDeviceMetric.app_version.validator),
    ('build_channel', DisableDeviceMetric.build_channel.validator)]
EmailType._setup_complete_validator = bv.Void()
EmailType._first_sync_complete_validator = bv.Void()
EmailType._cb_setup_complete_product_survey_validator = bv.Void()
EmailType._other_validator = bv.Void()
EmailType._tagmap = {
    'setup_complete': EmailType._setup_complete_validator,
    'first_sync_complete': EmailType._first_sync_complete_validator,
    'cb_setup_complete_product_survey': EmailType._cb_setup_complete_product_survey_validator,
    'other': EmailType._other_validator }
EmailType.setup_complete = EmailType('setup_complete')
EmailType.first_sync_complete = EmailType('first_sync_complete')
EmailType.cb_setup_complete_product_survey = EmailType('cb_setup_complete_product_survey')
EmailType.other = EmailType('other')
EnableDeviceArg.device_id.validator = DeviceId_validator
EnableDeviceArg.name.validator = DeviceName_validator
EnableDeviceArg.sync_folders.validator = bv.List(SyncFolder_validator)
EnableDeviceArg.quota_exempt.validator = bv.Nullable(bv.Boolean())
EnableDeviceArg._all_field_names_ = set([
    'device_id',
    'name',
    'sync_folders',
    'quota_exempt'])
EnableDeviceArg._all_fields_ = [
    ('device_id', EnableDeviceArg.device_id.validator),
    ('name', EnableDeviceArg.name.validator),
    ('sync_folders', EnableDeviceArg.sync_folders.validator),
    ('quota_exempt', EnableDeviceArg.quota_exempt.validator)]
EnableDeviceError._invalid_request_validator = InvalidRequestError_validator
EnableDeviceError._device_conflict_validator = DeviceConflictError_validator
EnableDeviceError._folder_lookup_error_validator = files.LookupError_validator
EnableDeviceError._folder_update_error_validator = files.WriteError_validator
EnableDeviceError._update_conflict_validator = bv.Void()
EnableDeviceError._audit_log_error_validator = bv.Void()
EnableDeviceError._internal_error_validator = InternalError_validator
EnableDeviceError._quota_exempt_error_validator = QuotaExemptError_validator
EnableDeviceError._restore_backup_error_validator = RestoreBackupError_validator
EnableDeviceError._anchors_backup_error_validator = AnchorsBackupError_validator
EnableDeviceError._prepare_restore_backup_error_validator = PrepareRestoreBackupError_validator
EnableDeviceError._mixed_backup_implementation_validator = bv.Void()
EnableDeviceError._other_validator = bv.Void()
EnableDeviceError._tagmap = {
    'invalid_request': EnableDeviceError._invalid_request_validator,
    'device_conflict': EnableDeviceError._device_conflict_validator,
    'folder_lookup_error': EnableDeviceError._folder_lookup_error_validator,
    'folder_update_error': EnableDeviceError._folder_update_error_validator,
    'update_conflict': EnableDeviceError._update_conflict_validator,
    'audit_log_error': EnableDeviceError._audit_log_error_validator,
    'internal_error': EnableDeviceError._internal_error_validator,
    'quota_exempt_error': EnableDeviceError._quota_exempt_error_validator,
    'restore_backup_error': EnableDeviceError._restore_backup_error_validator,
    'anchors_backup_error': EnableDeviceError._anchors_backup_error_validator,
    'prepare_restore_backup_error': EnableDeviceError._prepare_restore_backup_error_validator,
    'mixed_backup_implementation': EnableDeviceError._mixed_backup_implementation_validator,
    'other': EnableDeviceError._other_validator }
EnableDeviceError.update_conflict = EnableDeviceError('update_conflict')
EnableDeviceError.audit_log_error = EnableDeviceError('audit_log_error')
EnableDeviceError.mixed_backup_implementation = EnableDeviceError('mixed_backup_implementation')
EnableDeviceError.other = EnableDeviceError('other')
ExclusionFileExtension.regex.validator = bv.String()
ExclusionFileExtension.regex.validator._redact = bv.BlotRedactor(None)
ExclusionFileExtension.exclude_type_id.validator = bv.UInt32()
ExclusionFileExtension.exclude_type_id.validator._redact = bv.BlotRedactor(None)
ExclusionFileExtension._all_field_names_ = set([
    'regex',
    'exclude_type_id'])
ExclusionFileExtension._all_fields_ = [
    ('regex', ExclusionFileExtension.regex.validator),
    ('exclude_type_id', ExclusionFileExtension.exclude_type_id.validator)]
ExclusionListArg.os_type.validator = PlatformType_validator
ExclusionListArg._all_field_names_ = set([
    'os_type'])
ExclusionListArg._all_fields_ = [
    ('os_type', ExclusionListArg.os_type.validator)]
ExclusionListResult.merge_exclusion_list.validator = bv.List(ExclusionFileExtension_validator)
ExclusionListResult.unmerge_exclusion_list.validator = bv.List(ExclusionFileExtension_validator)
ExclusionListResult._all_field_names_ = set([
    'merge_exclusion_list',
    'unmerge_exclusion_list'])
ExclusionListResult._all_fields_ = [
    ('merge_exclusion_list', ExclusionListResult.merge_exclusion_list.validator),
    ('unmerge_exclusion_list', ExclusionListResult.unmerge_exclusion_list.validator)]
FolderStatus.id.validator = files.FileId_validator
FolderStatus.home_ns_rel_path.validator = files.Path_validator
FolderStatus._all_field_names_ = set([
    'id',
    'home_ns_rel_path'])
FolderStatus._all_fields_ = [
    ('id', FolderStatus.id.validator),
    ('home_ns_rel_path', FolderStatus.home_ns_rel_path.validator)]
ForceDisableBackupArg.controller_device_id.validator = bv.Nullable(DeviceId_validator)
ForceDisableBackupArg.excluded_devices.validator = bv.List(DeviceId_validator)
ForceDisableBackupArg.backup_disable_type.validator = BackupDisableType_validator
ForceDisableBackupArg._all_field_names_ = set([
    'controller_device_id',
    'excluded_devices',
    'backup_disable_type'])
ForceDisableBackupArg._all_fields_ = [
    ('controller_device_id', ForceDisableBackupArg.controller_device_id.validator),
    ('excluded_devices', ForceDisableBackupArg.excluded_devices.validator),
    ('backup_disable_type', ForceDisableBackupArg.backup_disable_type.validator)]
ForceDisableBackupError._device_not_found_validator = bv.Void()
ForceDisableBackupError._update_conflict_validator = bv.Void()
ForceDisableBackupError._internal_error_validator = InternalError_validator
ForceDisableBackupError._other_validator = bv.Void()
ForceDisableBackupError._tagmap = {
    'device_not_found': ForceDisableBackupError._device_not_found_validator,
    'update_conflict': ForceDisableBackupError._update_conflict_validator,
    'internal_error': ForceDisableBackupError._internal_error_validator,
    'other': ForceDisableBackupError._other_validator }
ForceDisableBackupError.device_not_found = ForceDisableBackupError('device_not_found')
ForceDisableBackupError.update_conflict = ForceDisableBackupError('update_conflict')
ForceDisableBackupError.other = ForceDisableBackupError('other')
GetBackupRootInfoError._not_found_validator = bv.Void()
GetBackupRootInfoError._other_validator = bv.Void()
GetBackupRootInfoError._tagmap = {
    'not_found': GetBackupRootInfoError._not_found_validator,
    'other': GetBackupRootInfoError._other_validator }
GetBackupRootInfoError.not_found = GetBackupRootInfoError('not_found')
GetBackupRootInfoError.other = GetBackupRootInfoError('other')
GetBackupRootInfoResult.backup_root_info.validator = BackupRootInfo_validator
GetBackupRootInfoResult._all_field_names_ = set([
    'backup_root_info'])
GetBackupRootInfoResult._all_fields_ = [
    ('backup_root_info', GetBackupRootInfoResult.backup_root_info.validator)]
GetBackupSubscriptionTimestampError._invalid_user_validator = bv.Void()
GetBackupSubscriptionTimestampError._internal_error_validator = InternalError_validator
GetBackupSubscriptionTimestampError._other_validator = bv.Void()
GetBackupSubscriptionTimestampError._tagmap = {
    'invalid_user': GetBackupSubscriptionTimestampError._invalid_user_validator,
    'internal_error': GetBackupSubscriptionTimestampError._internal_error_validator,
    'other': GetBackupSubscriptionTimestampError._other_validator }
GetBackupSubscriptionTimestampError.invalid_user = GetBackupSubscriptionTimestampError('invalid_user')
GetBackupSubscriptionTimestampError.other = GetBackupSubscriptionTimestampError('other')
GetBackupSubscriptionTimestampResult.timestamp.validator = bv.String()
GetBackupSubscriptionTimestampResult.timestamp.validator._redact = bv.BlotRedactor(None)
GetBackupSubscriptionTimestampResult._all_field_names_ = set([
    'timestamp'])
GetBackupSubscriptionTimestampResult._all_fields_ = [
    ('timestamp', GetBackupSubscriptionTimestampResult.timestamp.validator)]
IcRemediationMetric.ic_remediation.validator = bv.String()
IcRemediationMetric.ic_remediation.validator._redact = bv.BlotRedactor(None)
IcRemediationMetric.count.validator = bv.Int32()
IcRemediationMetric.count.validator._redact = bv.BlotRedactor(None)
IcRemediationMetric.platform.validator = PlatformType_validator
IcRemediationMetric.app_version.validator = bv.String()
IcRemediationMetric.app_version.validator._redact = bv.BlotRedactor(None)
IcRemediationMetric.build_channel.validator = bv.String()
IcRemediationMetric.build_channel.validator._redact = bv.BlotRedactor(None)
IcRemediationMetric.ic_mode.validator = bv.String()
IcRemediationMetric.ic_mode.validator._redact = bv.BlotRedactor(None)
IcRemediationMetric._all_field_names_ = set([
    'ic_remediation',
    'count',
    'platform',
    'app_version',
    'build_channel',
    'ic_mode'])
IcRemediationMetric._all_fields_ = [
    ('ic_remediation', IcRemediationMetric.ic_remediation.validator),
    ('count', IcRemediationMetric.count.validator),
    ('platform', IcRemediationMetric.platform.validator),
    ('app_version', IcRemediationMetric.app_version.validator),
    ('build_channel', IcRemediationMetric.build_channel.validator),
    ('ic_mode', IcRemediationMetric.ic_mode.validator)]
InternalError.debug_message.validator = bv.Nullable(bv.String())
InternalError.source_exception.validator = bv.Nullable(bv.String())
InternalError._all_field_names_ = set([])
InternalError._all_fields_ = []
InternalError._all_internal_field_names_ = set([
    'debug_message',
    'source_exception'])
InternalError._all_internal_fields_ = [
    ('debug_message', InternalError.debug_message.validator),
    ('source_exception', InternalError.source_exception.validator)]
InvalidRequestError._invalid_device_name_validator = bv.Void()
InvalidRequestError._invalid_sync_folder_name_validator = bv.Void()
InvalidRequestError._no_sync_folders_validator = bv.Void()
InvalidRequestError._duplicate_sync_folders_validator = bv.Void()
InvalidRequestError._other_validator = bv.Void()
InvalidRequestError._tagmap = {
    'invalid_device_name': InvalidRequestError._invalid_device_name_validator,
    'invalid_sync_folder_name': InvalidRequestError._invalid_sync_folder_name_validator,
    'no_sync_folders': InvalidRequestError._no_sync_folders_validator,
    'duplicate_sync_folders': InvalidRequestError._duplicate_sync_folders_validator,
    'other': InvalidRequestError._other_validator }
InvalidRequestError.invalid_device_name = InvalidRequestError('invalid_device_name')
InvalidRequestError.invalid_sync_folder_name = InvalidRequestError('invalid_sync_folder_name')
InvalidRequestError.no_sync_folders = InvalidRequestError('no_sync_folders')
InvalidRequestError.duplicate_sync_folders = InvalidRequestError('duplicate_sync_folders')
InvalidRequestError.other = InvalidRequestError('other')
ListBackupsArgs.include_last_ts.validator = bv.Nullable(bv.Boolean())
ListBackupsArgs._all_field_names_ = set([
    'include_last_ts'])
ListBackupsArgs._all_fields_ = [
    ('include_last_ts', ListBackupsArgs.include_last_ts.validator)]
ListBackupsResult.backups_list.validator = bv.List(BackupInfo_validator)
ListBackupsResult.max_quota_exempt.validator = bv.Int64()
ListBackupsResult.max_quota_exempt.validator._redact = bv.BlotRedactor(None)
ListBackupsResult._all_field_names_ = set([
    'backups_list',
    'max_quota_exempt'])
ListBackupsResult._all_fields_ = [
    ('backups_list', ListBackupsResult.backups_list.validator),
    ('max_quota_exempt', ListBackupsResult.max_quota_exempt.validator)]
Metric._update_device_validator = UpdateDeviceMetric_validator
Metric._disable_device_validator = DisableDeviceMetric_validator
Metric._ic_remediation_validator = IcRemediationMetric_validator
Metric._other_validator = bv.Void()
Metric._tagmap = {
    'update_device': Metric._update_device_validator,
    'disable_device': Metric._disable_device_validator,
    'ic_remediation': Metric._ic_remediation_validator,
    'other': Metric._other_validator }
Metric.other = Metric('other')
NamespaceInfo.ns_id.validator = bv.UInt64()
NamespaceInfo.ns_id.validator._redact = bv.BlotRedactor(None)
NamespaceInfo.fileid.validator = files.FileId_validator
NamespaceInfo._all_field_names_ = set([
    'ns_id',
    'fileid'])
NamespaceInfo._all_fields_ = [
    ('ns_id', NamespaceInfo.ns_id.validator),
    ('fileid', NamespaceInfo.fileid.validator)]
PingServerArg.req.validator = bv.Nullable(bv.String())
PingServerArg._all_field_names_ = set([
    'req'])
PingServerArg._all_fields_ = [
    ('req', PingServerArg.req.validator)]
PingServerResult.resp.validator = bv.Nullable(bv.String())
PingServerResult._all_field_names_ = set([
    'resp'])
PingServerResult._all_fields_ = [
    ('resp', PingServerResult.resp.validator)]
PlatformType._unknown_validator = bv.Void()
PlatformType._mac_validator = bv.Void()
PlatformType._win_validator = bv.Void()
PlatformType._other_validator = bv.Void()
PlatformType._tagmap = {
    'unknown': PlatformType._unknown_validator,
    'mac': PlatformType._mac_validator,
    'win': PlatformType._win_validator,
    'other': PlatformType._other_validator }
PlatformType.unknown = PlatformType('unknown')
PlatformType.mac = PlatformType('mac')
PlatformType.win = PlatformType('win')
PlatformType.other = PlatformType('other')
PrepareRestoreBackupError._validate_restore_error_validator = RestoreBackupValidationError_validator
PrepareRestoreBackupError._internal_error_validator = InternalError_validator
PrepareRestoreBackupError._other_validator = bv.Void()
PrepareRestoreBackupError._tagmap = {
    'validate_restore_error': PrepareRestoreBackupError._validate_restore_error_validator,
    'internal_error': PrepareRestoreBackupError._internal_error_validator,
    'other': PrepareRestoreBackupError._other_validator }
PrepareRestoreBackupError.other = PrepareRestoreBackupError('other')
QuotaExemptError._lookup_devices_validator = bv.Void()
QuotaExemptError._unexempt_existing_validator = bv.Void()
QuotaExemptError._not_allowed_validator = bv.Void()
QuotaExemptError._update_conflict_validator = bv.Void()
QuotaExemptError._other_validator = bv.Void()
QuotaExemptError._tagmap = {
    'lookup_devices': QuotaExemptError._lookup_devices_validator,
    'unexempt_existing': QuotaExemptError._unexempt_existing_validator,
    'not_allowed': QuotaExemptError._not_allowed_validator,
    'update_conflict': QuotaExemptError._update_conflict_validator,
    'other': QuotaExemptError._other_validator }
QuotaExemptError.lookup_devices = QuotaExemptError('lookup_devices')
QuotaExemptError.unexempt_existing = QuotaExemptError('unexempt_existing')
QuotaExemptError.not_allowed = QuotaExemptError('not_allowed')
QuotaExemptError.update_conflict = QuotaExemptError('update_conflict')
QuotaExemptError.other = QuotaExemptError('other')
RestoreBackupError._not_found_validator = bv.Void()
RestoreBackupError._backup_disabled_validator = bv.Void()
RestoreBackupError._backup_id_conflict_validator = bv.Void()
RestoreBackupError._missing_folder_validator = bv.Void()
RestoreBackupError._destination_exists_validator = bv.Void()
RestoreBackupError._retry_missing_root_validator = bv.Void()
RestoreBackupError._async_copy_failed_validator = bv.Void()
RestoreBackupError._async_copy_invalid_validator = bv.Void()
RestoreBackupError._async_copy_transient_validator = AsyncCopyTransientError_validator
RestoreBackupError._restore_not_started_validator = bv.Void()
RestoreBackupError._restore_not_ready_validator = bv.Void()
RestoreBackupError._other_validator = bv.Void()
RestoreBackupError._tagmap = {
    'not_found': RestoreBackupError._not_found_validator,
    'backup_disabled': RestoreBackupError._backup_disabled_validator,
    'backup_id_conflict': RestoreBackupError._backup_id_conflict_validator,
    'missing_folder': RestoreBackupError._missing_folder_validator,
    'destination_exists': RestoreBackupError._destination_exists_validator,
    'retry_missing_root': RestoreBackupError._retry_missing_root_validator,
    'async_copy_failed': RestoreBackupError._async_copy_failed_validator,
    'async_copy_invalid': RestoreBackupError._async_copy_invalid_validator,
    'async_copy_transient': RestoreBackupError._async_copy_transient_validator,
    'restore_not_started': RestoreBackupError._restore_not_started_validator,
    'restore_not_ready': RestoreBackupError._restore_not_ready_validator,
    'other': RestoreBackupError._other_validator }
RestoreBackupError.not_found = RestoreBackupError('not_found')
RestoreBackupError.backup_disabled = RestoreBackupError('backup_disabled')
RestoreBackupError.backup_id_conflict = RestoreBackupError('backup_id_conflict')
RestoreBackupError.missing_folder = RestoreBackupError('missing_folder')
RestoreBackupError.destination_exists = RestoreBackupError('destination_exists')
RestoreBackupError.retry_missing_root = RestoreBackupError('retry_missing_root')
RestoreBackupError.async_copy_failed = RestoreBackupError('async_copy_failed')
RestoreBackupError.async_copy_invalid = RestoreBackupError('async_copy_invalid')
RestoreBackupError.restore_not_started = RestoreBackupError('restore_not_started')
RestoreBackupError.restore_not_ready = RestoreBackupError('restore_not_ready')
RestoreBackupError.other = RestoreBackupError('other')
RestoreBackupPerFolderError._async_copy_invalid_validator = bv.Void()
RestoreBackupPerFolderError._async_copy_transient_validator = bv.Void()
RestoreBackupPerFolderError._async_copy_failed_validator = bv.Void()
RestoreBackupPerFolderError._other_validator = bv.Void()
RestoreBackupPerFolderError._tagmap = {
    'async_copy_invalid': RestoreBackupPerFolderError._async_copy_invalid_validator,
    'async_copy_transient': RestoreBackupPerFolderError._async_copy_transient_validator,
    'async_copy_failed': RestoreBackupPerFolderError._async_copy_failed_validator,
    'other': RestoreBackupPerFolderError._other_validator }
RestoreBackupPerFolderError.async_copy_invalid = RestoreBackupPerFolderError('async_copy_invalid')
RestoreBackupPerFolderError.async_copy_transient = RestoreBackupPerFolderError('async_copy_transient')
RestoreBackupPerFolderError.async_copy_failed = RestoreBackupPerFolderError('async_copy_failed')
RestoreBackupPerFolderError.other = RestoreBackupPerFolderError('other')
RestoreBackupPerFolderErrorPair.restore_folder.validator = RestoreFolder_validator
RestoreBackupPerFolderErrorPair.folder_error.validator = RestoreBackupPerFolderError_validator
RestoreBackupPerFolderErrorPair._all_field_names_ = set([
    'restore_folder',
    'folder_error'])
RestoreBackupPerFolderErrorPair._all_fields_ = [
    ('restore_folder', RestoreBackupPerFolderErrorPair.restore_folder.validator),
    ('folder_error', RestoreBackupPerFolderErrorPair.folder_error.validator)]
RestoreBackupValidationError._not_found_validator = bv.Void()
RestoreBackupValidationError._backup_disabled_validator = bv.Void()
RestoreBackupValidationError._backup_id_conflict_validator = bv.Void()
RestoreBackupValidationError._missing_folder_validator = bv.Void()
RestoreBackupValidationError._invalid_request_validator = bv.Void()
RestoreBackupValidationError._destination_not_found_validator = bv.Void()
RestoreBackupValidationError._destination_exists_validator = bv.Void()
RestoreBackupValidationError._other_validator = bv.Void()
RestoreBackupValidationError._tagmap = {
    'not_found': RestoreBackupValidationError._not_found_validator,
    'backup_disabled': RestoreBackupValidationError._backup_disabled_validator,
    'backup_id_conflict': RestoreBackupValidationError._backup_id_conflict_validator,
    'missing_folder': RestoreBackupValidationError._missing_folder_validator,
    'invalid_request': RestoreBackupValidationError._invalid_request_validator,
    'destination_not_found': RestoreBackupValidationError._destination_not_found_validator,
    'destination_exists': RestoreBackupValidationError._destination_exists_validator,
    'other': RestoreBackupValidationError._other_validator }
RestoreBackupValidationError.not_found = RestoreBackupValidationError('not_found')
RestoreBackupValidationError.backup_disabled = RestoreBackupValidationError('backup_disabled')
RestoreBackupValidationError.backup_id_conflict = RestoreBackupValidationError('backup_id_conflict')
RestoreBackupValidationError.missing_folder = RestoreBackupValidationError('missing_folder')
RestoreBackupValidationError.invalid_request = RestoreBackupValidationError('invalid_request')
RestoreBackupValidationError.destination_not_found = RestoreBackupValidationError('destination_not_found')
RestoreBackupValidationError.destination_exists = RestoreBackupValidationError('destination_exists')
RestoreBackupValidationError.other = RestoreBackupValidationError('other')
RestoreComputerBackupArg.update_computer_backup_arg.validator = UpdateComputerBackupArg_validator
RestoreComputerBackupArg.folders_to_restore.validator = RestoreComputerBackupFolderInput_validator
RestoreComputerBackupArg.restore_device_id.validator = DeviceId_validator
RestoreComputerBackupArg.folder_suffix.validator = bv.Nullable(bv.String())
RestoreComputerBackupArg.restore_in_root.validator = bv.Nullable(bv.Boolean())
RestoreComputerBackupArg._all_field_names_ = set([
    'update_computer_backup_arg',
    'folders_to_restore',
    'restore_device_id',
    'folder_suffix',
    'restore_in_root'])
RestoreComputerBackupArg._all_fields_ = [
    ('update_computer_backup_arg', RestoreComputerBackupArg.update_computer_backup_arg.validator),
    ('folders_to_restore', RestoreComputerBackupArg.folders_to_restore.validator),
    ('restore_device_id', RestoreComputerBackupArg.restore_device_id.validator),
    ('folder_suffix', RestoreComputerBackupArg.folder_suffix.validator),
    ('restore_in_root', RestoreComputerBackupArg.restore_in_root.validator)]
RestoreComputerBackupError._common_validate_restore_error_validator = RestoreBackupValidationError_validator
RestoreComputerBackupError._per_folder_errors_validator = bv.List(RestoreBackupPerFolderErrorPair_validator)
RestoreComputerBackupError._other_validator = bv.Void()
RestoreComputerBackupError._tagmap = {
    'common_validate_restore_error': RestoreComputerBackupError._common_validate_restore_error_validator,
    'per_folder_errors': RestoreComputerBackupError._per_folder_errors_validator,
    'other': RestoreComputerBackupError._other_validator }
RestoreComputerBackupError.other = RestoreComputerBackupError('other')
RestoreComputerBackupFolderInput._cb_folder_entries_validator = bv.List(ComputerBackupFolderRestoreEntry_validator)
RestoreComputerBackupFolderInput._se_folder_types_validator = bv.List(SyncFolderType_validator)
RestoreComputerBackupFolderInput._other_validator = bv.Void()
RestoreComputerBackupFolderInput._tagmap = {
    'cb_folder_entries': RestoreComputerBackupFolderInput._cb_folder_entries_validator,
    'se_folder_types': RestoreComputerBackupFolderInput._se_folder_types_validator,
    'other': RestoreComputerBackupFolderInput._other_validator }
RestoreComputerBackupFolderInput.other = RestoreComputerBackupFolderInput('other')
RestoreFolder._cb_folder_entry_validator = ComputerBackupFolderRestoreEntry_validator
RestoreFolder._folder_type_validator = SyncFolderType_validator
RestoreFolder._other_validator = bv.Void()
RestoreFolder._tagmap = {
    'cb_folder_entry': RestoreFolder._cb_folder_entry_validator,
    'folder_type': RestoreFolder._folder_type_validator,
    'other': RestoreFolder._other_validator }
RestoreFolder.other = RestoreFolder('other')
ScheduleDetail.custom.validator = bv.List(bv.Nullable(bv.Int32()))
ScheduleDetail.cadence.validator = bv.Nullable(bv.Int32())
ScheduleDetail.day_mark.validator = bv.Nullable(bv.Int32())
ScheduleDetail.hour_mark.validator = bv.Nullable(bv.Int32())
ScheduleDetail.minute_mark.validator = bv.Nullable(bv.Int32())
ScheduleDetail._all_field_names_ = set([
    'custom',
    'cadence',
    'day_mark',
    'hour_mark',
    'minute_mark'])
ScheduleDetail._all_fields_ = [
    ('custom', ScheduleDetail.custom.validator),
    ('cadence', ScheduleDetail.cadence.validator),
    ('day_mark', ScheduleDetail.day_mark.validator),
    ('hour_mark', ScheduleDetail.hour_mark.validator),
    ('minute_mark', ScheduleDetail.minute_mark.validator)]
ScheduleType._periodic_validator = bv.Void()
ScheduleType._daily_validator = bv.Void()
ScheduleType._weekly_validator = bv.Void()
ScheduleType._custom_validator = bv.Void()
ScheduleType._other_validator = bv.Void()
ScheduleType._tagmap = {
    'periodic': ScheduleType._periodic_validator,
    'daily': ScheduleType._daily_validator,
    'weekly': ScheduleType._weekly_validator,
    'custom': ScheduleType._custom_validator,
    'other': ScheduleType._other_validator }
ScheduleType.periodic = ScheduleType('periodic')
ScheduleType.daily = ScheduleType('daily')
ScheduleType.weekly = ScheduleType('weekly')
ScheduleType.custom = ScheduleType('custom')
ScheduleType.other = ScheduleType('other')
SendEmailArg.email_type.validator = EmailType_validator
SendEmailArg.device_name.validator = bv.String()
SendEmailArg.device_name.validator._redact = bv.BlotRedactor(None)
SendEmailArg.device_id.validator = DeviceId_validator
SendEmailArg.os_type.validator = PlatformType_validator
SendEmailArg._all_field_names_ = set([
    'email_type',
    'device_name',
    'device_id',
    'os_type'])
SendEmailArg._all_fields_ = [
    ('email_type', SendEmailArg.email_type.validator),
    ('device_name', SendEmailArg.device_name.validator),
    ('device_id', SendEmailArg.device_id.validator),
    ('os_type', SendEmailArg.os_type.validator)]
SetQuotaExemptArg.device_id.validator = DeviceId_validator
SetQuotaExemptArg._all_field_names_ = set([
    'device_id'])
SetQuotaExemptArg._all_fields_ = [
    ('device_id', SetQuotaExemptArg.device_id.validator)]
SetQuotaExemptError._quota_exempt_error_validator = QuotaExemptError_validator
SetQuotaExemptError._device_not_found_validator = bv.Void()
SetQuotaExemptError._device_disabled_validator = bv.Void()
SetQuotaExemptError._other_validator = bv.Void()
SetQuotaExemptError._tagmap = {
    'quota_exempt_error': SetQuotaExemptError._quota_exempt_error_validator,
    'device_not_found': SetQuotaExemptError._device_not_found_validator,
    'device_disabled': SetQuotaExemptError._device_disabled_validator,
    'other': SetQuotaExemptError._other_validator }
SetQuotaExemptError.device_not_found = SetQuotaExemptError('device_not_found')
SetQuotaExemptError.device_disabled = SetQuotaExemptError('device_disabled')
SetQuotaExemptError.other = SetQuotaExemptError('other')
StartRestoreDeviceArg.enable_device_args.validator = EnableDeviceArg_validator
StartRestoreDeviceArg.restore_device_id.validator = DeviceId_validator
StartRestoreDeviceArg.is_async_retry.validator = bv.Nullable(bv.Boolean())
StartRestoreDeviceArg._all_field_names_ = set([
    'enable_device_args',
    'restore_device_id',
    'is_async_retry'])
StartRestoreDeviceArg._all_fields_ = [
    ('enable_device_args', StartRestoreDeviceArg.enable_device_args.validator),
    ('restore_device_id', StartRestoreDeviceArg.restore_device_id.validator),
    ('is_async_retry', StartRestoreDeviceArg.is_async_retry.validator)]
Status._done_validator = bv.Void()
Status._fail_validator = bv.Void()
Status._other_validator = bv.Void()
Status._tagmap = {
    'done': Status._done_validator,
    'fail': Status._fail_validator,
    'other': Status._other_validator }
Status.done = Status('done')
Status.fail = Status('fail')
Status.other = Status('other')
SyncFolder.type.validator = SyncFolderType_validator
SyncFolder.name.validator = SyncFolderName_validator
SyncFolder._all_field_names_ = set([
    'type',
    'name'])
SyncFolder._all_fields_ = [
    ('type', SyncFolder.type.validator),
    ('name', SyncFolder.name.validator)]
SyncFolderStatus.folder.validator = SyncFolder_validator
SyncFolderStatus.status.validator = FolderStatus_validator
SyncFolderStatus._all_field_names_ = set([
    'folder',
    'status'])
SyncFolderStatus._all_fields_ = [
    ('folder', SyncFolderStatus.folder.validator),
    ('status', SyncFolderStatus.status.validator)]
SyncFolderType._desktop_validator = bv.Void()
SyncFolderType._documents_validator = bv.Void()
SyncFolderType._pictures_validator = bv.Void()
SyncFolderType._downloads_validator = bv.Void()
SyncFolderType._music_validator = bv.Void()
SyncFolderType._videos_validator = bv.Void()
SyncFolderType._movies_validator = bv.Void()
SyncFolderType._screenshots_validator = bv.Void()
SyncFolderType._other_validator = bv.Void()
SyncFolderType._tagmap = {
    'desktop': SyncFolderType._desktop_validator,
    'documents': SyncFolderType._documents_validator,
    'pictures': SyncFolderType._pictures_validator,
    'downloads': SyncFolderType._downloads_validator,
    'music': SyncFolderType._music_validator,
    'videos': SyncFolderType._videos_validator,
    'movies': SyncFolderType._movies_validator,
    'screenshots': SyncFolderType._screenshots_validator,
    'other': SyncFolderType._other_validator }
SyncFolderType.desktop = SyncFolderType('desktop')
SyncFolderType.documents = SyncFolderType('documents')
SyncFolderType.pictures = SyncFolderType('pictures')
SyncFolderType.downloads = SyncFolderType('downloads')
SyncFolderType.music = SyncFolderType('music')
SyncFolderType.videos = SyncFolderType('videos')
SyncFolderType.movies = SyncFolderType('movies')
SyncFolderType.screenshots = SyncFolderType('screenshots')
SyncFolderType.other = SyncFolderType('other')
UpdateAnchorInfoArg.device_id.validator = DeviceId_validator
UpdateAnchorInfoArg.backup_state.validator = ComputerBackupState_validator
UpdateAnchorInfoArg.folder_info.validator = bv.List(UpdateAnchorStateInfo_validator)
UpdateAnchorInfoArg._all_field_names_ = set([
    'device_id',
    'backup_state',
    'folder_info'])
UpdateAnchorInfoArg._all_fields_ = [
    ('device_id', UpdateAnchorInfoArg.device_id.validator),
    ('backup_state', UpdateAnchorInfoArg.backup_state.validator),
    ('folder_info', UpdateAnchorInfoArg.folder_info.validator)]
UpdateAnchorInfoError._device_update_error_validator = bv.Void()
UpdateAnchorInfoError._anchor_update_error_validator = bv.Void()
UpdateAnchorInfoError._backup_not_found_validator = bv.Void()
UpdateAnchorInfoError._anchor_not_found_validator = bv.Void()
UpdateAnchorInfoError._update_conflict_validator = bv.Void()
UpdateAnchorInfoError._other_validator = bv.Void()
UpdateAnchorInfoError._tagmap = {
    'device_update_error': UpdateAnchorInfoError._device_update_error_validator,
    'anchor_update_error': UpdateAnchorInfoError._anchor_update_error_validator,
    'backup_not_found': UpdateAnchorInfoError._backup_not_found_validator,
    'anchor_not_found': UpdateAnchorInfoError._anchor_not_found_validator,
    'update_conflict': UpdateAnchorInfoError._update_conflict_validator,
    'other': UpdateAnchorInfoError._other_validator }
UpdateAnchorInfoError.device_update_error = UpdateAnchorInfoError('device_update_error')
UpdateAnchorInfoError.anchor_update_error = UpdateAnchorInfoError('anchor_update_error')
UpdateAnchorInfoError.backup_not_found = UpdateAnchorInfoError('backup_not_found')
UpdateAnchorInfoError.anchor_not_found = UpdateAnchorInfoError('anchor_not_found')
UpdateAnchorInfoError.update_conflict = UpdateAnchorInfoError('update_conflict')
UpdateAnchorInfoError.other = UpdateAnchorInfoError('other')
UpdateAnchorStateInfo.root_entry_fileid.validator = files.FileId_validator
UpdateAnchorStateInfo.backup_folder_state.validator = ComputerBackupFolderState_validator
UpdateAnchorStateInfo.initial_timestamp_utc.validator = bv.Nullable(ClearableUInt64_validator)
UpdateAnchorStateInfo._all_field_names_ = set([
    'root_entry_fileid',
    'backup_folder_state',
    'initial_timestamp_utc'])
UpdateAnchorStateInfo._all_fields_ = [
    ('root_entry_fileid', UpdateAnchorStateInfo.root_entry_fileid.validator),
    ('backup_folder_state', UpdateAnchorStateInfo.backup_folder_state.validator),
    ('initial_timestamp_utc', UpdateAnchorStateInfo.initial_timestamp_utc.validator)]
UpdateComputerBackupArg.device_id.validator = DeviceId_validator
UpdateComputerBackupArg.name.validator = DeviceName_validator
UpdateComputerBackupArg.device_quota_exempt.validator = bv.Boolean()
UpdateComputerBackupArg.device_quota_exempt.validator._redact = bv.BlotRedactor(None)
UpdateComputerBackupArg.folders.validator = bv.List(ComputerBackupFolderInput_validator)
UpdateComputerBackupArg._all_field_names_ = set([
    'device_id',
    'name',
    'device_quota_exempt',
    'folders'])
UpdateComputerBackupArg._all_fields_ = [
    ('device_id', UpdateComputerBackupArg.device_id.validator),
    ('name', UpdateComputerBackupArg.name.validator),
    ('device_quota_exempt', UpdateComputerBackupArg.device_quota_exempt.validator),
    ('folders', UpdateComputerBackupArg.folders.validator)]
UpdateComputerBackupResult.folders_list.validator = bv.List(UpdateComputerBackupResultInfo_validator)
UpdateComputerBackupResult.quota_exempt.validator = bv.Boolean()
UpdateComputerBackupResult.quota_exempt.validator._redact = bv.BlotRedactor(None)
UpdateComputerBackupResult.name.validator = DeviceName_validator
UpdateComputerBackupResult.root_fileid.validator = files.FileId_validator
UpdateComputerBackupResult._all_field_names_ = set([
    'folders_list',
    'quota_exempt',
    'name',
    'root_fileid'])
UpdateComputerBackupResult._all_fields_ = [
    ('folders_list', UpdateComputerBackupResult.folders_list.validator),
    ('quota_exempt', UpdateComputerBackupResult.quota_exempt.validator),
    ('name', UpdateComputerBackupResult.name.validator),
    ('root_fileid', UpdateComputerBackupResult.root_fileid.validator)]
UpdateComputerBackupResultInfo.folder_path.validator = bv.String()
UpdateComputerBackupResultInfo.folder_path.validator._redact = bv.BlotRedactor(None)
UpdateComputerBackupResultInfo.success.validator = bv.Boolean()
UpdateComputerBackupResultInfo.success.validator._redact = bv.BlotRedactor(None)
UpdateComputerBackupResultInfo.folder_info.validator = bv.Nullable(ComputerBackupFolder_validator)
UpdateComputerBackupResultInfo._all_field_names_ = set([
    'folder_path',
    'success',
    'folder_info'])
UpdateComputerBackupResultInfo._all_fields_ = [
    ('folder_path', UpdateComputerBackupResultInfo.folder_path.validator),
    ('success', UpdateComputerBackupResultInfo.success.validator),
    ('folder_info', UpdateComputerBackupResultInfo.folder_info.validator)]
UpdateDeviceMetric.status.validator = Status_validator
UpdateDeviceMetric.count.validator = bv.Int32()
UpdateDeviceMetric.count.validator._redact = bv.BlotRedactor(None)
UpdateDeviceMetric.platform.validator = PlatformType_validator
UpdateDeviceMetric.build_channel.validator = bv.String()
UpdateDeviceMetric.build_channel.validator._redact = bv.BlotRedactor(None)
UpdateDeviceMetric.app_version.validator = bv.String()
UpdateDeviceMetric.app_version.validator._redact = bv.BlotRedactor(None)
UpdateDeviceMetric._all_field_names_ = set([
    'status',
    'count',
    'platform',
    'build_channel',
    'app_version'])
UpdateDeviceMetric._all_fields_ = [
    ('status', UpdateDeviceMetric.status.validator),
    ('count', UpdateDeviceMetric.count.validator),
    ('platform', UpdateDeviceMetric.platform.validator),
    ('build_channel', UpdateDeviceMetric.build_channel.validator),
    ('app_version', UpdateDeviceMetric.app_version.validator)]
UpdateDisplayNameArg.device_id.validator = DeviceId_validator
UpdateDisplayNameArg.display_name.validator = bv.String()
UpdateDisplayNameArg.display_name.validator._redact = bv.BlotRedactor(None)
UpdateDisplayNameArg._all_field_names_ = set([
    'device_id',
    'display_name'])
UpdateDisplayNameArg._all_fields_ = [
    ('device_id', UpdateDisplayNameArg.device_id.validator),
    ('display_name', UpdateDisplayNameArg.display_name.validator)]
UpdateDisplayNameError._duplicate_name_validator = bv.Void()
UpdateDisplayNameError._invalid_name_validator = bv.Void()
UpdateDisplayNameError._device_not_found_validator = bv.Void()
UpdateDisplayNameError._device_disabled_validator = bv.Void()
UpdateDisplayNameError._internal_error_validator = InternalError_validator
UpdateDisplayNameError._other_validator = bv.Void()
UpdateDisplayNameError._tagmap = {
    'duplicate_name': UpdateDisplayNameError._duplicate_name_validator,
    'invalid_name': UpdateDisplayNameError._invalid_name_validator,
    'device_not_found': UpdateDisplayNameError._device_not_found_validator,
    'device_disabled': UpdateDisplayNameError._device_disabled_validator,
    'internal_error': UpdateDisplayNameError._internal_error_validator,
    'other': UpdateDisplayNameError._other_validator }
UpdateDisplayNameError.duplicate_name = UpdateDisplayNameError('duplicate_name')
UpdateDisplayNameError.invalid_name = UpdateDisplayNameError('invalid_name')
UpdateDisplayNameError.device_not_found = UpdateDisplayNameError('device_not_found')
UpdateDisplayNameError.device_disabled = UpdateDisplayNameError('device_disabled')
UpdateDisplayNameError.other = UpdateDisplayNameError('other')
UpdateSyncProgressPercentageArg.device_id.validator = DeviceId_validator
UpdateSyncProgressPercentageArg.sync_progress_percentage.validator = bv.UInt64()
UpdateSyncProgressPercentageArg.sync_progress_percentage.validator._redact = bv.BlotRedactor(None)
UpdateSyncProgressPercentageArg._all_field_names_ = set([
    'device_id',
    'sync_progress_percentage'])
UpdateSyncProgressPercentageArg._all_fields_ = [
    ('device_id', UpdateSyncProgressPercentageArg.device_id.validator),
    ('sync_progress_percentage', UpdateSyncProgressPercentageArg.sync_progress_percentage.validator)]
UpdateSyncProgressPercentageError._device_not_found_validator = bv.Void()
UpdateSyncProgressPercentageError._device_disabled_validator = bv.Void()
UpdateSyncProgressPercentageError._percentage_not_in_range_validator = bv.Void()
UpdateSyncProgressPercentageError._internal_error_validator = InternalError_validator
UpdateSyncProgressPercentageError._other_validator = bv.Void()
UpdateSyncProgressPercentageError._tagmap = {
    'device_not_found': UpdateSyncProgressPercentageError._device_not_found_validator,
    'device_disabled': UpdateSyncProgressPercentageError._device_disabled_validator,
    'percentage_not_in_range': UpdateSyncProgressPercentageError._percentage_not_in_range_validator,
    'internal_error': UpdateSyncProgressPercentageError._internal_error_validator,
    'other': UpdateSyncProgressPercentageError._other_validator }
UpdateSyncProgressPercentageError.device_not_found = UpdateSyncProgressPercentageError('device_not_found')
UpdateSyncProgressPercentageError.device_disabled = UpdateSyncProgressPercentageError('device_disabled')
UpdateSyncProgressPercentageError.percentage_not_in_range = UpdateSyncProgressPercentageError('percentage_not_in_range')
UpdateSyncProgressPercentageError.other = UpdateSyncProgressPercentageError('other')
# WARNING: Decompyle incomplete
