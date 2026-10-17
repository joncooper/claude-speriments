# Source Generated with Decompyle++
# File: sharing.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import account_id
from dropbox.api.v2.datatypes import async_
from dropbox.api.v2.datatypes import common
from dropbox.api.v2.datatypes import ekms
from dropbox.api.v2.datatypes import files
from dropbox.api.v2.datatypes import seen_state
from dropbox.api.v2.datatypes import team_common
from dropbox.api.v2.datatypes import team_policies
from dropbox.api.v2.datatypes import users
from dropbox.api.v2.datatypes import users_common

class AccessAlreadyGranted(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AccessAlreadyGranted_validator = bv.Struct(AccessAlreadyGranted)

class AccessInheritance(bb.Union):
    pass
# WARNING: Decompyle incomplete

AccessInheritance_validator = bv.Union(AccessInheritance)

class AccessLevel(bb.Union):
    pass
# WARNING: Decompyle incomplete

AccessLevel_validator = bv.Union(AccessLevel)

class AccessType(bb.Union):
    pass
# WARNING: Decompyle incomplete

AccessType_validator = bv.Union(AccessType)

class AccountSelectionRequiredOpenLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AccountSelectionRequiredOpenLinkResult_validator = bv.Struct(AccountSelectionRequiredOpenLinkResult)

class AccountSelectionResolvedOpenLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AccountSelectionResolvedOpenLinkResult_validator = bv.Struct(AccountSelectionResolvedOpenLinkResult)

class AccountSelectionStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

AccountSelectionStatus_validator = bv.Union(AccountSelectionStatus)

class AclUpdatePolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

AclUpdatePolicy_validator = bv.Union(AclUpdatePolicy)

class AddFileMemberArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AddFileMemberArgs_validator = bv.Struct(AddFileMemberArgs)

class AddFileMemberError(bb.Union):
    pass
# WARNING: Decompyle incomplete

AddFileMemberError_validator = bv.Union(AddFileMemberError)

class AddFolderMemberArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AddFolderMemberArg_validator = bv.Struct(AddFolderMemberArg)

class AddFolderMemberEncryptionError(bb.Union):
    pass
# WARNING: Decompyle incomplete

AddFolderMemberEncryptionError_validator = bv.Union(AddFolderMemberEncryptionError)

class AddFolderMemberError(bb.Union):
    pass
# WARNING: Decompyle incomplete

AddFolderMemberError_validator = bv.Union(AddFolderMemberError)

class AddFolderMemberResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AddFolderMemberResult_validator = bv.Struct(AddFolderMemberResult)

class AddMember(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AddMember_validator = bv.Struct(AddMember)

class AddMemberArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AddMemberArg_validator = bv.Struct(AddMemberArg)

class AddMemberError(bb.Union):
    pass
# WARNING: Decompyle incomplete

AddMemberError_validator = bv.Union(AddMemberError)

class AddMemberResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

AddMemberResult_validator = bv.Union(AddMemberResult)

class AddMemberSelectorError(bb.Union):
    pass
# WARNING: Decompyle incomplete

AddMemberSelectorError_validator = bv.Union(AddMemberSelectorError)

class AlphaCreateSharedLinkWithSettingsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaCreateSharedLinkWithSettingsArg_validator = bv.Struct(AlphaCreateSharedLinkWithSettingsArg)

class FileAction(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileAction_validator = bv.Union(FileAction)

class AlphaFileAction(FileAction):
    pass
# WARNING: Decompyle incomplete

AlphaFileAction_validator = bv.Union(AlphaFileAction)

class AlphaSharedLinkMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaSharedLinkMetadata_validator = bv.StructTree(AlphaSharedLinkMetadata)

class AlphaFileLinkMetadata(AlphaSharedLinkMetadata):
    pass
# WARNING: Decompyle incomplete

AlphaFileLinkMetadata_validator = bv.Struct(AlphaFileLinkMetadata)

class AlphaFilePermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaFilePermission_validator = bv.Struct(AlphaFilePermission)

class FolderAction(bb.Union):
    pass
# WARNING: Decompyle incomplete

FolderAction_validator = bv.Union(FolderAction)

class InternalFolderAction(FolderAction):
    pass
# WARNING: Decompyle incomplete

InternalFolderAction_validator = bv.Union(InternalFolderAction)

class AlphaFolderAction(InternalFolderAction):
    pass
# WARNING: Decompyle incomplete

AlphaFolderAction_validator = bv.Union(AlphaFolderAction)

class AlphaFolderLinkMetadata(AlphaSharedLinkMetadata):
    pass
# WARNING: Decompyle incomplete

AlphaFolderLinkMetadata_validator = bv.Struct(AlphaFolderLinkMetadata)

class AlphaFolderPermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaFolderPermission_validator = bv.Struct(AlphaFolderPermission)

class AlphaFolderPolicy(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaFolderPolicy_validator = bv.Struct(AlphaFolderPolicy)

class AlphaGetFileMetadataArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaGetFileMetadataArg_validator = bv.Struct(AlphaGetFileMetadataArg)

class AlphaGetFileMetadataBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaGetFileMetadataBatchArg_validator = bv.Struct(AlphaGetFileMetadataBatchArg)

class AlphaGetFileMetadataBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaGetFileMetadataBatchResult_validator = bv.Struct(AlphaGetFileMetadataBatchResult)

class AlphaGetFileMetadataIndividualResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

AlphaGetFileMetadataIndividualResult_validator = bv.Union(AlphaGetFileMetadataIndividualResult)

class AlphaGetMetadataArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaGetMetadataArgs_validator = bv.Struct(AlphaGetMetadataArgs)

class LinkAudience(bb.Union):
    pass
# WARNING: Decompyle incomplete

LinkAudience_validator = bv.Union(LinkAudience)

class AlphaLinkAudience(LinkAudience):
    pass
# WARNING: Decompyle incomplete

AlphaLinkAudience_validator = bv.Union(AlphaLinkAudience)

class AlphaLinkPermissions(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaLinkPermissions_validator = bv.Struct(AlphaLinkPermissions)

class AlphaLinkSettings(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaLinkSettings_validator = bv.Struct(AlphaLinkSettings)

class ListFileMembersArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFileMembersArg_validator = bv.Struct(ListFileMembersArg)

class AlphaListFileMembersArg(ListFileMembersArg):
    pass
# WARNING: Decompyle incomplete

AlphaListFileMembersArg_validator = bv.Struct(AlphaListFileMembersArg)

class ListFileMembersContinueArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFileMembersContinueArg_validator = bv.Struct(ListFileMembersContinueArg)

class AlphaListFileMembersContinueArg(ListFileMembersContinueArg):
    pass
# WARNING: Decompyle incomplete

AlphaListFileMembersContinueArg_validator = bv.Struct(AlphaListFileMembersContinueArg)

class AlphaListFilesResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaListFilesResult_validator = bv.Struct(AlphaListFilesResult)

class AlphaListFoldersArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaListFoldersArgs_validator = bv.Struct(AlphaListFoldersArgs)

class AlphaListFoldersResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaListFoldersResult_validator = bv.Struct(AlphaListFoldersResult)

class AlphaListSharedLinksResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaListSharedLinksResult_validator = bv.Struct(AlphaListSharedLinksResult)

class AlphaModifySharedLinkSettingsArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaModifySharedLinkSettingsArgs_validator = bv.Struct(AlphaModifySharedLinkSettingsArgs)

class RequestedVisibility(bb.Union):
    pass
# WARNING: Decompyle incomplete

RequestedVisibility_validator = bv.Union(RequestedVisibility)

class ResolvedVisibility(RequestedVisibility):
    pass
# WARNING: Decompyle incomplete

ResolvedVisibility_validator = bv.Union(ResolvedVisibility)

class AlphaResolvedVisibility(ResolvedVisibility):
    pass
# WARNING: Decompyle incomplete

AlphaResolvedVisibility_validator = bv.Union(AlphaResolvedVisibility)

class ShareFolderArgBase(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ShareFolderArgBase_validator = bv.Struct(ShareFolderArgBase)

class AlphaShareFolderArg(ShareFolderArgBase):
    pass
# WARNING: Decompyle incomplete

AlphaShareFolderArg_validator = bv.Struct(AlphaShareFolderArg)

class ShareFolderErrorBase(bb.Union):
    pass
# WARNING: Decompyle incomplete

ShareFolderErrorBase_validator = bv.Union(ShareFolderErrorBase)

class ShareFolderError(ShareFolderErrorBase):
    pass
# WARNING: Decompyle incomplete

ShareFolderError_validator = bv.Union(ShareFolderError)

class AlphaShareFolderError(ShareFolderError):
    pass
# WARNING: Decompyle incomplete

AlphaShareFolderError_validator = bv.Union(AlphaShareFolderError)

class AlphaShareFolderLaunch(async_.LaunchResultBase):
    pass
# WARNING: Decompyle incomplete

AlphaShareFolderLaunch_validator = bv.Union(AlphaShareFolderLaunch)

class AlphaSharedFileMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaSharedFileMetadata_validator = bv.Struct(AlphaSharedFileMetadata)

class SharedFolderMetadataBase(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedFolderMetadataBase_validator = bv.Struct(SharedFolderMetadataBase)

class AlphaSharedFolderMetadata(SharedFolderMetadataBase):
    pass
# WARNING: Decompyle incomplete

AlphaSharedFolderMetadata_validator = bv.Struct(AlphaSharedFolderMetadata)

class SharedLinkSettings(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedLinkSettings_validator = bv.Struct(SharedLinkSettings)

class AlphaSharedLinkSettings(SharedLinkSettings):
    pass
# WARNING: Decompyle incomplete

AlphaSharedLinkSettings_validator = bv.Struct(AlphaSharedLinkSettings)

class AlphaUnuploadedLinkMetadata(AlphaSharedLinkMetadata):
    pass
# WARNING: Decompyle incomplete

AlphaUnuploadedLinkMetadata_validator = bv.Struct(AlphaUnuploadedLinkMetadata)

class AlphaUpdateFilePolicyArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaUpdateFilePolicyArg_validator = bv.Struct(AlphaUpdateFilePolicyArg)

class AlphaUpdateFolderPolicyArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AlphaUpdateFolderPolicyArg_validator = bv.Struct(AlphaUpdateFolderPolicyArg)

class AppUpdateRequiredOpenLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AppUpdateRequiredOpenLinkResult_validator = bv.Struct(AppUpdateRequiredOpenLinkResult)

class AudienceExceptionContentInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AudienceExceptionContentInfo_validator = bv.Struct(AudienceExceptionContentInfo)

class AudienceExceptions(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AudienceExceptions_validator = bv.Struct(AudienceExceptions)

class AudienceRestrictingSharedFolder(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AudienceRestrictingSharedFolder_validator = bv.Struct(AudienceRestrictingSharedFolder)

class ChangeLinkExpirationPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

ChangeLinkExpirationPolicy_validator = bv.Union(ChangeLinkExpirationPolicy)

class ChangePoliciesFilePermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ChangePoliciesFilePermission_validator = bv.Struct(ChangePoliciesFilePermission)

class ChangePoliciesFolderPermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ChangePoliciesFolderPermission_validator = bv.Struct(ChangePoliciesFolderPermission)

class ClaimMembershipArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ClaimMembershipArgs_validator = bv.Struct(ClaimMembershipArgs)

class ClaimMembershipError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ClaimMembershipError_validator = bv.Union(ClaimMembershipError)

class ClaimMembershipOpenLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ClaimMembershipOpenLinkResult_validator = bv.Struct(ClaimMembershipOpenLinkResult)

class ClientOpenLinkAction(bb.Union):
    pass
# WARNING: Decompyle incomplete

ClientOpenLinkAction_validator = bv.Union(ClientOpenLinkAction)

class CloudDocClass(bb.Union):
    pass
# WARNING: Decompyle incomplete

CloudDocClass_validator = bv.Union(CloudDocClass)

class LinkMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LinkMetadata_validator = bv.StructTree(LinkMetadata)

class CollectionLinkMetadata(LinkMetadata):
    pass
# WARNING: Decompyle incomplete

CollectionLinkMetadata_validator = bv.Struct(CollectionLinkMetadata)

class CommonMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CommonMetadata_validator = bv.Struct(CommonMetadata)

class ConfidentialityArgs(bb.Union):
    pass
# WARNING: Decompyle incomplete

ConfidentialityArgs_validator = bv.Union(ConfidentialityArgs)

class ContainsAppFolder(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContainsAppFolder_validator = bv.Struct(ContainsAppFolder)

class Content(bb.Union):
    pass
# WARNING: Decompyle incomplete

Content_validator = bv.Union(Content)

class ContentType(bb.Union):
    pass
# WARNING: Decompyle incomplete

ContentType_validator = bv.Union(ContentType)

class CreateDirectLinkArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreateDirectLinkArg_validator = bv.Struct(CreateDirectLinkArg)

class CreateDirectLinkError(bb.Union):
    pass
# WARNING: Decompyle incomplete

CreateDirectLinkError_validator = bv.Union(CreateDirectLinkError)

class CreateEditLinkFilePermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreateEditLinkFilePermission_validator = bv.Struct(CreateEditLinkFilePermission)

class CreateEditLinkFolderPermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreateEditLinkFolderPermission_validator = bv.Struct(CreateEditLinkFolderPermission)

class CreateSharedLinkArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreateSharedLinkArg_validator = bv.Struct(CreateSharedLinkArg)

class CreateSharedLinkError(bb.Union):
    pass
# WARNING: Decompyle incomplete

CreateSharedLinkError_validator = bv.Union(CreateSharedLinkError)

class CreateSharedLinkWithSettingsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreateSharedLinkWithSettingsArg_validator = bv.Struct(CreateSharedLinkWithSettingsArg)

class CreateSharedLinkWithSettingsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

CreateSharedLinkWithSettingsError_validator = bv.Union(CreateSharedLinkWithSettingsError)

class CreateViewLinkFilePermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreateViewLinkFilePermission_validator = bv.Struct(CreateViewLinkFilePermission)

class CreateViewLinkFolderPermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreateViewLinkFolderPermission_validator = bv.Struct(CreateViewLinkFolderPermission)

class DefaultLinkExpirationDaysPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

DefaultLinkExpirationDaysPolicy_validator = bv.Union(DefaultLinkExpirationDaysPolicy)

class DirectLinkMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DirectLinkMetadata_validator = bv.Struct(DirectLinkMetadata)

class DisableViewerInfoFilePermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DisableViewerInfoFilePermission_validator = bv.Struct(DisableViewerInfoFilePermission)

class DisableViewerInfoFolderPermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DisableViewerInfoFolderPermission_validator = bv.Struct(DisableViewerInfoFolderPermission)

class DismissInviteNotificationArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DismissInviteNotificationArg_validator = bv.Struct(DismissInviteNotificationArg)

class DismissInviteNotificationError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DismissInviteNotificationError_validator = bv.Union(DismissInviteNotificationError)

class DownloadPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

DownloadPolicy_validator = bv.Union(DownloadPolicy)

class EnableViewerInfoFilePermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EnableViewerInfoFilePermission_validator = bv.Struct(EnableViewerInfoFilePermission)

class EnableViewerInfoFolderPermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EnableViewerInfoFolderPermission_validator = bv.Struct(EnableViewerInfoFolderPermission)

class EncryptedKeyPairDraftArg(ekms.EncryptedKeyPairDraft):
    pass
# WARNING: Decompyle incomplete

EncryptedKeyPairDraftArg_validator = bv.Struct(EncryptedKeyPairDraftArg)

class EnforceLinkPasswordPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

EnforceLinkPasswordPolicy_validator = bv.Union(EnforceLinkPasswordPolicy)

class SharedContentLinkMetadataBase(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedContentLinkMetadataBase_validator = bv.Struct(SharedContentLinkMetadataBase)

class ExpectedSharedContentLinkMetadata(SharedContentLinkMetadataBase):
    pass
# WARNING: Decompyle incomplete

ExpectedSharedContentLinkMetadata_validator = bv.Struct(ExpectedSharedContentLinkMetadata)

class ExpectedSharedFolderMetadata(SharedFolderMetadataBase):
    pass
# WARNING: Decompyle incomplete

ExpectedSharedFolderMetadata_validator = bv.Struct(ExpectedSharedFolderMetadata)

class SharedLinkError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedLinkError_validator = bv.Union(SharedLinkError)

class GetSharedLinkFileError(SharedLinkError):
    pass
# WARNING: Decompyle incomplete

GetSharedLinkFileError_validator = bv.Union(GetSharedLinkFileError)

class ExportSharedLinkError(GetSharedLinkFileError):
    pass
# WARNING: Decompyle incomplete

ExportSharedLinkError_validator = bv.Union(ExportSharedLinkError)

class ExportSharedLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ExportSharedLinkResult_validator = bv.Struct(ExportSharedLinkResult)

class FileErrorResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileErrorResult_validator = bv.Union(FileErrorResult)

class SharedLinkMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedLinkMetadata_validator = bv.StructTree(SharedLinkMetadata)

class FileLinkMetadata(SharedLinkMetadata):
    pass
# WARNING: Decompyle incomplete

FileLinkMetadata_validator = bv.Struct(FileLinkMetadata)

class FileMemberActionError(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileMemberActionError_validator = bv.Union(FileMemberActionError)

class FileMemberActionIndividualResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileMemberActionIndividualResult_validator = bv.Union(FileMemberActionIndividualResult)

class FileMemberActionResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FileMemberActionResult_validator = bv.Struct(FileMemberActionResult)

class FileMemberCounts(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FileMemberCounts_validator = bv.Struct(FileMemberCounts)

class FileMemberRemoveActionResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileMemberRemoveActionResult_validator = bv.Union(FileMemberRemoveActionResult)

class FileMetadataResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FileMetadataResponse_validator = bv.Struct(FileMetadataResponse)

class FilePermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilePermission_validator = bv.Struct(FilePermission)

class FlattenGroupAccessArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FlattenGroupAccessArg_validator = bv.Struct(FlattenGroupAccessArg)

class FlattenGroupAccessError(bb.Union):
    pass
# WARNING: Decompyle incomplete

FlattenGroupAccessError_validator = bv.Union(FlattenGroupAccessError)

class FlattenGroupAccessJobCheckResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

FlattenGroupAccessJobCheckResult_validator = bv.Union(FlattenGroupAccessJobCheckResult)

class FlattenGroupAccessJobError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FlattenGroupAccessJobError_validator = bv.Struct(FlattenGroupAccessJobError)

class FlattenGroupAccessJobResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FlattenGroupAccessJobResult_validator = bv.Struct(FlattenGroupAccessJobResult)

class FlattenGroupAccessResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FlattenGroupAccessResponse_validator = bv.Struct(FlattenGroupAccessResponse)

class FlattenGroupAccessSubscriberArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FlattenGroupAccessSubscriberArg_validator = bv.Struct(FlattenGroupAccessSubscriberArg)

class FlattenedSubjectResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FlattenedSubjectResponse_validator = bv.Struct(FlattenedSubjectResponse)

class FolderLinkMetadata(SharedLinkMetadata):
    pass
# WARNING: Decompyle incomplete

FolderLinkMetadata_validator = bv.Struct(FolderLinkMetadata)

class FolderMetadataResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FolderMetadataResponse_validator = bv.Struct(FolderMetadataResponse)

class FolderPermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FolderPermission_validator = bv.Struct(FolderPermission)

class FolderPolicy(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FolderPolicy_validator = bv.Struct(FolderPolicy)

class FolderSharedWithInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FolderSharedWithInfo_validator = bv.Struct(FolderSharedWithInfo)

class GetFileMemberCountsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileMemberCountsArg_validator = bv.Struct(GetFileMemberCountsArg)

class GetFileMemberCountsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetFileMemberCountsError_validator = bv.Union(GetFileMemberCountsError)

class GetFileMetadataArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileMetadataArg_validator = bv.Struct(GetFileMetadataArg)

class GetFileMetadataBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileMetadataBatchArg_validator = bv.Struct(GetFileMetadataBatchArg)

class GetFileMetadataBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileMetadataBatchResult_validator = bv.Struct(GetFileMetadataBatchResult)

class GetFileMetadataError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetFileMetadataError_validator = bv.Union(GetFileMetadataError)

class GetFileMetadataIndividualResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetFileMetadataIndividualResult_validator = bv.Union(GetFileMetadataIndividualResult)

class GetFileSharedContentLinkArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileSharedContentLinkArg_validator = bv.Struct(GetFileSharedContentLinkArg)

class GetFolderItemCountArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFolderItemCountArg_validator = bv.Struct(GetFolderItemCountArg)

class GetFolderItemCountError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetFolderItemCountError_validator = bv.Union(GetFolderItemCountError)

class GetFolderItemCountResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFolderItemCountResponse_validator = bv.Struct(GetFolderItemCountResponse)

class GetFolderMemberCountsArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFolderMemberCountsArgs_validator = bv.Struct(GetFolderMemberCountsArgs)

class GetFolderMemberCountsBatchEntry(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFolderMemberCountsBatchEntry_validator = bv.Struct(GetFolderMemberCountsBatchEntry)

class GetFolderMemberCountsBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFolderMemberCountsBatchResult_validator = bv.Struct(GetFolderMemberCountsBatchResult)

class GetFolderMemberCountsIndividualResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetFolderMemberCountsIndividualResult_validator = bv.Union(GetFolderMemberCountsIndividualResult)

class GetFolderSharedContentLinkArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFolderSharedContentLinkArg_validator = bv.Struct(GetFolderSharedContentLinkArg)

class GetMetadataArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetMetadataArgs_validator = bv.Struct(GetMetadataArgs)

class GetParentFolderAccessArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetParentFolderAccessArg_validator = bv.Struct(GetParentFolderAccessArg)

class GetShareModalObjectMetadataArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetShareModalObjectMetadataArg_validator = bv.Struct(GetShareModalObjectMetadataArg)

class GetShareModalObjectMetadataError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetShareModalObjectMetadataError_validator = bv.Union(GetShareModalObjectMetadataError)

class GetShareModalObjectMetadataResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetShareModalObjectMetadataResponse_validator = bv.Struct(GetShareModalObjectMetadataResponse)

class GetSharedLinkMetadataArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetSharedLinkMetadataArg_validator = bv.Struct(GetSharedLinkMetadataArg)

class GetSharedLinksArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetSharedLinksArg_validator = bv.Struct(GetSharedLinksArg)

class GetSharedLinksError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetSharedLinksError_validator = bv.Union(GetSharedLinksError)

class GetSharedLinksResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetSharedLinksResult_validator = bv.Struct(GetSharedLinksResult)

class GetSharingAccountInfoResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetSharingAccountInfoResult_validator = bv.Struct(GetSharingAccountInfoResult)

class GrantAccessActionArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GrantAccessActionArg_validator = bv.Struct(GrantAccessActionArg)

class GrantAccessActionError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GrantAccessActionError_validator = bv.Union(GrantAccessActionError)

class GrantAccessActionResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

GrantAccessActionResult_validator = bv.Union(GrantAccessActionResult)

class GroupInfo(team_common.GroupSummary):
    pass
# WARNING: Decompyle incomplete

GroupInfo_validator = bv.Struct(GroupInfo)

class MembershipInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MembershipInfo_validator = bv.Struct(MembershipInfo)

class GroupMembershipInfo(MembershipInfo):
    pass
# WARNING: Decompyle incomplete

GroupMembershipInfo_validator = bv.Struct(GroupMembershipInfo)

class Target(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Target_validator = bv.StructTree(Target)

class GroupTarget(Target):
    pass
# WARNING: Decompyle incomplete

GroupTarget_validator = bv.Struct(GroupTarget)

class InsideAppFolder(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InsideAppFolder_validator = bv.Struct(InsideAppFolder)

class InsufficientPlan(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InsufficientPlan_validator = bv.Struct(InsufficientPlan)

class InsufficientQuotaAmounts(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InsufficientQuotaAmounts_validator = bv.Struct(InsufficientQuotaAmounts)

class InternalFolderPermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InternalFolderPermission_validator = bv.Struct(InternalFolderPermission)

class InternalGetMetadataArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InternalGetMetadataArgs_validator = bv.Struct(InternalGetMetadataArgs)

class SharePathErrorBaseV2(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharePathErrorBaseV2_validator = bv.Union(SharePathErrorBaseV2)

class InternalSharePathError(SharePathErrorBaseV2):
    pass
# WARNING: Decompyle incomplete

InternalSharePathError_validator = bv.Union(InternalSharePathError)

class InternalSharedFolderMetadata(SharedFolderMetadataBase):
    pass
# WARNING: Decompyle incomplete

InternalSharedFolderMetadata_validator = bv.Struct(InternalSharedFolderMetadata)

class InvitationAccessStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

InvitationAccessStatus_validator = bv.Union(InvitationAccessStatus)

class InviteEditorFilePermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InviteEditorFilePermission_validator = bv.Struct(InviteEditorFilePermission)

class InviteEditorFolderPermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InviteEditorFolderPermission_validator = bv.Struct(InviteEditorFolderPermission)

class InviteViewerFilePermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InviteViewerFilePermission_validator = bv.Struct(InviteViewerFilePermission)

class InviteViewerFolderPermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InviteViewerFolderPermission_validator = bv.Struct(InviteViewerFolderPermission)

class InviteeInfo(bb.Union):
    pass
# WARNING: Decompyle incomplete

InviteeInfo_validator = bv.Union(InviteeInfo)

class InviteeMembershipInfo(MembershipInfo):
    pass
# WARNING: Decompyle incomplete

InviteeMembershipInfo_validator = bv.Struct(InviteeMembershipInfo)

class IsAppFolder(bb.Struct):
    pass
# WARNING: Decompyle incomplete

IsAppFolder_validator = bv.Struct(IsAppFolder)

class IsConfidentialFolder(bb.Struct):
    pass
# WARNING: Decompyle incomplete

IsConfidentialFolder_validator = bv.Struct(IsConfidentialFolder)

class IsFamilyFolder(bb.Struct):
    pass
# WARNING: Decompyle incomplete

IsFamilyFolder_validator = bv.Struct(IsFamilyFolder)

class JobError(bb.Union):
    pass
# WARNING: Decompyle incomplete

JobError_validator = bv.Union(JobError)

class JobStatus(async_.PollResultBase):
    pass
# WARNING: Decompyle incomplete

JobStatus_validator = bv.Union(JobStatus)

class JoinTeamOpenLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

JoinTeamOpenLinkResult_validator = bv.Struct(JoinTeamOpenLinkResult)

class LinkAccessLevel(bb.Union):
    pass
# WARNING: Decompyle incomplete

LinkAccessLevel_validator = bv.Union(LinkAccessLevel)

class LinkAction(bb.Union):
    pass
# WARNING: Decompyle incomplete

LinkAction_validator = bv.Union(LinkAction)

class VisibilityPolicyDisallowedReason(bb.Union):
    pass
# WARNING: Decompyle incomplete

VisibilityPolicyDisallowedReason_validator = bv.Union(VisibilityPolicyDisallowedReason)

class LinkAudienceDisallowedReason(VisibilityPolicyDisallowedReason):
    pass
# WARNING: Decompyle incomplete

LinkAudienceDisallowedReason_validator = bv.Union(LinkAudienceDisallowedReason)

class LinkAudienceOption(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LinkAudienceOption_validator = bv.Struct(LinkAudienceOption)

class LinkExpiry(bb.Union):
    pass
# WARNING: Decompyle incomplete

LinkExpiry_validator = bv.Union(LinkExpiry)

class LinkPassword(bb.Union):
    pass
# WARNING: Decompyle incomplete

LinkPassword_validator = bv.Union(LinkPassword)

class LinkPermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LinkPermission_validator = bv.Struct(LinkPermission)

class LinkPermissions(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LinkPermissions_validator = bv.Struct(LinkPermissions)

class LinkSettings(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LinkSettings_validator = bv.Struct(LinkSettings)

class LinkType(bb.Union):
    pass
# WARNING: Decompyle incomplete

LinkType_validator = bv.Union(LinkType)

class ListFileMembersBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFileMembersBatchArg_validator = bv.Struct(ListFileMembersBatchArg)

class ListFileMembersBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFileMembersBatchResult_validator = bv.Struct(ListFileMembersBatchResult)

class ListFileMembersContinueError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListFileMembersContinueError_validator = bv.Union(ListFileMembersContinueError)

class ListFileMembersCountResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFileMembersCountResult_validator = bv.Struct(ListFileMembersCountResult)

class ListFileMembersError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListFileMembersError_validator = bv.Union(ListFileMembersError)

class ListFileMembersIndividualResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListFileMembersIndividualResult_validator = bv.Union(ListFileMembersIndividualResult)

class ListFilesArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFilesArg_validator = bv.Struct(ListFilesArg)

class ListFilesContinueArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFilesContinueArg_validator = bv.Struct(ListFilesContinueArg)

class ListFilesContinueError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListFilesContinueError_validator = bv.Union(ListFilesContinueError)

class ListFilesResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFilesResult_validator = bv.Struct(ListFilesResult)

class ListFolderMembersCursorArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFolderMembersCursorArg_validator = bv.Struct(ListFolderMembersCursorArg)

class ListFolderMembersArgs(ListFolderMembersCursorArg):
    pass
# WARNING: Decompyle incomplete

ListFolderMembersArgs_validator = bv.Struct(ListFolderMembersArgs)

class ListFolderMembersBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFolderMembersBatchArg_validator = bv.Struct(ListFolderMembersBatchArg)

class ListFolderMembersBatchEntry(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFolderMembersBatchEntry_validator = bv.Struct(ListFolderMembersBatchEntry)

class ListFolderMembersBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFolderMembersBatchResult_validator = bv.Struct(ListFolderMembersBatchResult)

class ListFolderMembersContinueArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFolderMembersContinueArg_validator = bv.Struct(ListFolderMembersContinueArg)

class ListFolderMembersContinueError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListFolderMembersContinueError_validator = bv.Union(ListFolderMembersContinueError)

class ListFolderMembersIndividualResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListFolderMembersIndividualResult_validator = bv.Union(ListFolderMembersIndividualResult)

class ListFoldersArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFoldersArgs_validator = bv.Struct(ListFoldersArgs)

class ListFoldersContinueArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFoldersContinueArg_validator = bv.Struct(ListFoldersContinueArg)

class ListFoldersContinueError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListFoldersContinueError_validator = bv.Union(ListFoldersContinueError)

class ListFoldersResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFoldersResult_validator = bv.Struct(ListFoldersResult)

class ListSharedLinksArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListSharedLinksArg_validator = bv.Struct(ListSharedLinksArg)

class ListSharedLinksError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListSharedLinksError_validator = bv.Union(ListSharedLinksError)

class ListSharedLinksResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListSharedLinksResult_validator = bv.Struct(ListSharedLinksResult)

class ListUserVisitedLinksArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListUserVisitedLinksArg_validator = bv.Struct(ListUserVisitedLinksArg)

class ListUserVisitedLinksError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListUserVisitedLinksError_validator = bv.Union(ListUserVisitedLinksError)

class MediaHubInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MediaHubInfo_validator = bv.Struct(MediaHubInfo)

class MemberAccessLevelResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MemberAccessLevelResult_validator = bv.Struct(MemberAccessLevelResult)

class MemberAction(bb.Union):
    pass
# WARNING: Decompyle incomplete

MemberAction_validator = bv.Union(MemberAction)

class MemberCounts(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MemberCounts_validator = bv.Struct(MemberCounts)

class MemberPermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MemberPermission_validator = bv.Struct(MemberPermission)

class MemberPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

MemberPolicy_validator = bv.Union(MemberPolicy)

class MemberSelector(bb.Union):
    pass
# WARNING: Decompyle incomplete

MemberSelector_validator = bv.Union(MemberSelector)

class ModifySharedLinkSettingsArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ModifySharedLinkSettingsArgs_validator = bv.Struct(ModifySharedLinkSettingsArgs)

class ModifySharedLinkSettingsError(SharedLinkError):
    pass
# WARNING: Decompyle incomplete

ModifySharedLinkSettingsError_validator = bv.Union(ModifySharedLinkSettingsError)

class MountContentOpenLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MountContentOpenLinkResult_validator = bv.Struct(MountContentOpenLinkResult)

class MountExceededError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MountExceededError_validator = bv.Struct(MountExceededError)

class MountFolderArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MountFolderArg_validator = bv.Struct(MountFolderArg)

class MountFolderError(bb.Union):
    pass
# WARNING: Decompyle incomplete

MountFolderError_validator = bv.Union(MountFolderError)

class MountLimitType(bb.Union):
    pass
# WARNING: Decompyle incomplete

MountLimitType_validator = bv.Union(MountLimitType)

class MountLimitsError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MountLimitsError_validator = bv.Struct(MountLimitsError)

class MountLimitsExceededDenied(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MountLimitsExceededDenied_validator = bv.Struct(MountLimitsExceededDenied)

class MountLimitsInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MountLimitsInfo_validator = bv.Struct(MountLimitsInfo)

class MountSharedFolder(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MountSharedFolder_validator = bv.Struct(MountSharedFolder)

class NamespaceCannotBeNested(bb.Struct):
    pass
# WARNING: Decompyle incomplete

NamespaceCannotBeNested_validator = bv.Struct(NamespaceCannotBeNested)

class NamespaceCannotBeTeamFolder(bb.Struct):
    pass
# WARNING: Decompyle incomplete

NamespaceCannotBeTeamFolder_validator = bv.Struct(NamespaceCannotBeTeamFolder)

class NoPermissionDenied(bb.Struct):
    pass
# WARNING: Decompyle incomplete

NoPermissionDenied_validator = bv.Struct(NoPermissionDenied)

class NotifyInheritedMembersArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

NotifyInheritedMembersArg_validator = bv.Struct(NotifyInheritedMembersArg)

class NotifyInheritedMembersError(bb.Union):
    pass
# WARNING: Decompyle incomplete

NotifyInheritedMembersError_validator = bv.Union(NotifyInheritedMembersError)

class NotifyInheritedMembersResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

NotifyInheritedMembersResponse_validator = bv.Struct(NotifyInheritedMembersResponse)

class NsIdNsPath(bb.Struct):
    pass
# WARNING: Decompyle incomplete

NsIdNsPath_validator = bv.Struct(NsIdNsPath)

class ObjectSharingPolicies(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ObjectSharingPolicies_validator = bv.Struct(ObjectSharingPolicies)

class ObjectType(bb.Union):
    pass
# WARNING: Decompyle incomplete

ObjectType_validator = bv.Union(ObjectType)

class OpenContentOpenLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

OpenContentOpenLinkResult_validator = bv.Struct(OpenContentOpenLinkResult)

class OpenLinkActionArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

OpenLinkActionArg_validator = bv.Struct(OpenLinkActionArg)

class OpenLinkActionError(bb.Union):
    pass
# WARNING: Decompyle incomplete

OpenLinkActionError_validator = bv.Union(OpenLinkActionError)

class OpenLinkActionResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

OpenLinkActionResult_validator = bv.Struct(OpenLinkActionResult)

class ParentFolderAccessError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ParentFolderAccessError_validator = bv.Union(ParentFolderAccessError)

class ParentFolderAccessInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ParentFolderAccessInfo_validator = bv.Struct(ParentFolderAccessInfo)

class PasswordRequiredOpenLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PasswordRequiredOpenLinkResult_validator = bv.Struct(PasswordRequiredOpenLinkResult)

class PathLinkMetadata(LinkMetadata):
    pass
# WARNING: Decompyle incomplete

PathLinkMetadata_validator = bv.Struct(PathLinkMetadata)

class PendingResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PendingResult_validator = bv.Struct(PendingResult)

class PendingUploadMode(bb.Union):
    pass
# WARNING: Decompyle incomplete

PendingUploadMode_validator = bv.Union(PendingUploadMode)

class PermissionDeniedReason(bb.Union):
    pass
# WARNING: Decompyle incomplete

PermissionDeniedReason_validator = bv.Union(PermissionDeniedReason)

class PreviewRestoredAclBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PreviewRestoredAclBatchArg_validator = bv.Struct(PreviewRestoredAclBatchArg)

class PreviewRestoredAclBatchEntry(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PreviewRestoredAclBatchEntry_validator = bv.Struct(PreviewRestoredAclBatchEntry)

class PreviewRestoredAclBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PreviewRestoredAclBatchResult_validator = bv.Struct(PreviewRestoredAclBatchResult)

class PreviewRestoredAclError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PreviewRestoredAclError_validator = bv.Union(PreviewRestoredAclError)

class PreviewRestoredAclIndividualResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

PreviewRestoredAclIndividualResult_validator = bv.Union(PreviewRestoredAclIndividualResult)

class PreviewThumbnailInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PreviewThumbnailInfo_validator = bv.Struct(PreviewThumbnailInfo)

class PromptToOpenOrMountContentOpenLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PromptToOpenOrMountContentOpenLinkResult_validator = bv.Struct(PromptToOpenOrMountContentOpenLinkResult)

class ReceivedResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ReceivedResult_validator = bv.Struct(ReceivedResult)

class RedirectToBrowseOpenLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RedirectToBrowseOpenLinkResult_validator = bv.Struct(RedirectToBrowseOpenLinkResult)

class RelinquishAccessArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RelinquishAccessArg_validator = bv.Struct(RelinquishAccessArg)

class RelinquishAccessError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RelinquishAccessError_validator = bv.Union(RelinquishAccessError)

class RelinquishAccessResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RelinquishAccessResult_validator = bv.Struct(RelinquishAccessResult)

class RelinquishFileMembershipArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RelinquishFileMembershipArg_validator = bv.Struct(RelinquishFileMembershipArg)

class RelinquishFileMembershipError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RelinquishFileMembershipError_validator = bv.Union(RelinquishFileMembershipError)

class RelinquishFolderMembershipArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RelinquishFolderMembershipArg_validator = bv.Struct(RelinquishFolderMembershipArg)

class RelinquishFolderMembershipError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RelinquishFolderMembershipError_validator = bv.Union(RelinquishFolderMembershipError)

class RelinquishMembershipFolderPermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RelinquishMembershipFolderPermission_validator = bv.Struct(RelinquishMembershipFolderPermission)

class RemoveFileMemberArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RemoveFileMemberArg_validator = bv.Struct(RemoveFileMemberArg)

class RemoveFileMemberError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RemoveFileMemberError_validator = bv.Union(RemoveFileMemberError)

class RemoveFolderMemberArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RemoveFolderMemberArg_validator = bv.Struct(RemoveFolderMemberArg)

class RemoveFolderMemberError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RemoveFolderMemberError_validator = bv.Union(RemoveFolderMemberError)

class RemoveLinkVisitorArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RemoveLinkVisitorArg_validator = bv.Struct(RemoveLinkVisitorArg)

class RemoveLinkVisitorError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RemoveLinkVisitorError_validator = bv.Union(RemoveLinkVisitorError)

class RemoveMemberJobStatus(async_.PollResultBase):
    pass
# WARNING: Decompyle incomplete

RemoveMemberJobStatus_validator = bv.Union(RemoveMemberJobStatus)

class RequestAccessArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RequestAccessArg_validator = bv.Struct(RequestAccessArg)

class RequestAccessError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RequestAccessError_validator = bv.Union(RequestAccessError)

class RequestAccessOpenLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RequestAccessOpenLinkResult_validator = bv.Struct(RequestAccessOpenLinkResult)

class RequestedContentMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RequestedContentMetadata_validator = bv.Struct(RequestedContentMetadata)

class RequestedLinkAccessLevel(bb.Union):
    pass
# WARNING: Decompyle incomplete

RequestedLinkAccessLevel_validator = bv.Union(RequestedLinkAccessLevel)

class RequireUser(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RequireUser_validator = bv.Struct(RequireUser)

class RestrictedByParentFolder(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RestrictedByParentFolder_validator = bv.Struct(RestrictedByParentFolder)

class RestrictedByTeam(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RestrictedByTeam_validator = bv.Struct(RestrictedByTeam)

class RevokeSharedLinkArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RevokeSharedLinkArg_validator = bv.Struct(RevokeSharedLinkArg)

class RevokeSharedLinkError(SharedLinkError):
    pass
# WARNING: Decompyle incomplete

RevokeSharedLinkError_validator = bv.Union(RevokeSharedLinkError)

class SentResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SentResult_validator = bv.Struct(SentResult)

class SetAccessInheritanceArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SetAccessInheritanceArg_validator = bv.Struct(SetAccessInheritanceArg)

class SetAccessInheritanceError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SetAccessInheritanceError_validator = bv.Union(SetAccessInheritanceError)

class SetConfidentialityArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SetConfidentialityArgs_validator = bv.Struct(SetConfidentialityArgs)

class SetConfidentialityError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SetConfidentialityError_validator = bv.Union(SetConfidentialityError)

class ShareFolderArg(ShareFolderArgBase):
    pass
# WARNING: Decompyle incomplete

ShareFolderArg_validator = bv.Struct(ShareFolderArg)

class ShareFolderErrorBaseV2(bb.Union):
    pass
# WARNING: Decompyle incomplete

ShareFolderErrorBaseV2_validator = bv.Union(ShareFolderErrorBaseV2)

class ShareFolderErrorV2(ShareFolderErrorBaseV2):
    pass
# WARNING: Decompyle incomplete

ShareFolderErrorV2_validator = bv.Union(ShareFolderErrorV2)

class ShareFolderInternalArg(ShareFolderArgBase):
    pass
# WARNING: Decompyle incomplete

ShareFolderInternalArg_validator = bv.Struct(ShareFolderInternalArg)

class ShareFolderInternalJobStatus(async_.PollResultBase):
    pass
# WARNING: Decompyle incomplete

ShareFolderInternalJobStatus_validator = bv.Union(ShareFolderInternalJobStatus)

class ShareFolderInternalLaunch(async_.LaunchResultBase):
    pass
# WARNING: Decompyle incomplete

ShareFolderInternalLaunch_validator = bv.Union(ShareFolderInternalLaunch)

class ShareFolderJobStatus(async_.PollResultBase):
    pass
# WARNING: Decompyle incomplete

ShareFolderJobStatus_validator = bv.Union(ShareFolderJobStatus)

class ShareFolderLaunch(async_.LaunchResultBase):
    pass
# WARNING: Decompyle incomplete

ShareFolderLaunch_validator = bv.Union(ShareFolderLaunch)

class ShareMessageAsCommentFilePermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ShareMessageAsCommentFilePermission_validator = bv.Struct(ShareMessageAsCommentFilePermission)

class ShareMountedContent(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ShareMountedContent_validator = bv.Struct(ShareMountedContent)

class SharePathError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharePathError_validator = bv.Union(SharePathError)

class SharePathErrorV2(SharePathErrorBaseV2):
    pass
# WARNING: Decompyle incomplete

SharePathErrorV2_validator = bv.Union(SharePathErrorV2)

class SharedContentContinueError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedContentContinueError_validator = bv.Union(SharedContentContinueError)

class SharedContentLinkMetadata(SharedContentLinkMetadataBase):
    pass
# WARNING: Decompyle incomplete

SharedContentLinkMetadata_validator = bv.Struct(SharedContentLinkMetadata)

class SharedContentMetadata(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedContentMetadata_validator = bv.Union(SharedContentMetadata)

class SharedContentShareTypeFilter(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedContentShareTypeFilter_validator = bv.Union(SharedContentShareTypeFilter)

class SharedContentType(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedContentType_validator = bv.Union(SharedContentType)

class SharedFileMembers(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedFileMembers_validator = bv.Struct(SharedFileMembers)

class SharedFileMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedFileMetadata_validator = bv.Struct(SharedFileMetadata)

class SharedFolderAccessError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedFolderAccessError_validator = bv.Union(SharedFolderAccessError)

class SharedFolderMemberError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedFolderMemberError_validator = bv.Union(SharedFolderMemberError)

class SharedFolderMembers(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedFolderMembers_validator = bv.Struct(SharedFolderMembers)

class SharedFolderMetadata(SharedFolderMetadataBase):
    pass
# WARNING: Decompyle incomplete

SharedFolderMetadata_validator = bv.Struct(SharedFolderMetadata)

class SharedFolderPreviewRestoredAclResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedFolderPreviewRestoredAclResult_validator = bv.Struct(SharedFolderPreviewRestoredAclResult)

class SharedLinkAccessFailureReason(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedLinkAccessFailureReason_validator = bv.Union(SharedLinkAccessFailureReason)

class SharedLinkAlreadyExistsMetadata(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedLinkAlreadyExistsMetadata_validator = bv.Union(SharedLinkAlreadyExistsMetadata)

class SharedLinkMetadataError(SharedLinkError):
    pass
# WARNING: Decompyle incomplete

SharedLinkMetadataError_validator = bv.Union(SharedLinkMetadataError)

class SharedLinkPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedLinkPolicy_validator = bv.Union(SharedLinkPolicy)

class SharedLinkSettingsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedLinkSettingsError_validator = bv.Union(SharedLinkSettingsError)

class SharedNamespaceKeyMissingEncryptionError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedNamespaceKeyMissingEncryptionError_validator = bv.Struct(SharedNamespaceKeyMissingEncryptionError)

class SharedWithAccessLevel(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedWithAccessLevel_validator = bv.Union(SharedWithAccessLevel)

class SharedWithArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedWithArg_validator = bv.Struct(SharedWithArg)

class SharedWithByPathArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedWithByPathArg_validator = bv.Struct(SharedWithByPathArg)

class SharedWithError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedWithError_validator = bv.Union(SharedWithError)

class SharedWithGroupInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedWithGroupInfo_validator = bv.Struct(SharedWithGroupInfo)

class SharedWithInvitationInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedWithInvitationInfo_validator = bv.Struct(SharedWithInvitationInfo)

class SharedWithMemberInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedWithMemberInfo_validator = bv.Struct(SharedWithMemberInfo)

class SharedWithResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedWithResponse_validator = bv.Struct(SharedWithResponse)

class SharingFileAccessError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharingFileAccessError_validator = bv.Union(SharingFileAccessError)

class SharingUserError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharingUserError_validator = bv.Union(SharingUserError)

class SignInOpenLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SignInOpenLinkResult_validator = bv.Struct(SignInOpenLinkResult)

class StackInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StackInfo_validator = bv.Struct(StackInfo)

class SwitchAccount(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SwitchAccount_validator = bv.Struct(SwitchAccount)

class TargetInviteEligibilityState(bb.Union):
    pass
# WARNING: Decompyle incomplete

TargetInviteEligibilityState_validator = bv.Union(TargetInviteEligibilityState)

class TargetValidateResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TargetValidateResult_validator = bv.Struct(TargetValidateResult)

class TargetsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TargetsArg_validator = bv.Struct(TargetsArg)

class TargetsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

TargetsError_validator = bv.Union(TargetsError)

class TargetsSearchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TargetsSearchResult_validator = bv.Struct(TargetsSearchResult)

class TargetsValidateArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TargetsValidateArg_validator = bv.Struct(TargetsValidateArg)

class TargetsValidateError(bb.Union):
    pass
# WARNING: Decompyle incomplete

TargetsValidateError_validator = bv.Union(TargetsValidateError)

class TargetsValidateResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TargetsValidateResult_validator = bv.Struct(TargetsValidateResult)

class Team(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Team_validator = bv.Struct(Team)

class TeamMemberInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TeamMemberInfo_validator = bv.Struct(TeamMemberInfo)

class TempPathBasedFileMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TempPathBasedFileMetadata_validator = bv.Struct(TempPathBasedFileMetadata)

class TooManyMountsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

TooManyMountsError_validator = bv.Union(TooManyMountsError)

class TooManyMountsErrorV2(bb.Union):
    pass
# WARNING: Decompyle incomplete

TooManyMountsErrorV2_validator = bv.Union(TooManyMountsErrorV2)

class TransferFolderArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TransferFolderArg_validator = bv.Struct(TransferFolderArg)

class TransferFolderError(bb.Union):
    pass
# WARNING: Decompyle incomplete

TransferFolderError_validator = bv.Union(TransferFolderError)

class UnmountFolderArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UnmountFolderArg_validator = bv.Struct(UnmountFolderArg)

class UnmountFolderError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UnmountFolderError_validator = bv.Union(UnmountFolderError)

class UnshareFileArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UnshareFileArg_validator = bv.Struct(UnshareFileArg)

class UnshareFileError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UnshareFileError_validator = bv.Union(UnshareFileError)

class UnshareFilePermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UnshareFilePermission_validator = bv.Struct(UnshareFilePermission)

class UnshareFolderArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UnshareFolderArg_validator = bv.Struct(UnshareFolderArg)

class UnshareFolderError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UnshareFolderError_validator = bv.Union(UnshareFolderError)

class UnshareFolderPermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UnshareFolderPermission_validator = bv.Struct(UnshareFolderPermission)

class UpdateConfidentialityFolderPermission(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateConfidentialityFolderPermission_validator = bv.Struct(UpdateConfidentialityFolderPermission)

class UpdateFileMemberArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateFileMemberArgs_validator = bv.Struct(UpdateFileMemberArgs)

class UpdateFilePolicyArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateFilePolicyArg_validator = bv.Struct(UpdateFilePolicyArg)

class UpdateFilePolicyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UpdateFilePolicyError_validator = bv.Union(UpdateFilePolicyError)

class UpdateFolderMemberArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateFolderMemberArg_validator = bv.Struct(UpdateFolderMemberArg)

class UpdateFolderMemberError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UpdateFolderMemberError_validator = bv.Union(UpdateFolderMemberError)

class UpdateFolderPolicyArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateFolderPolicyArg_validator = bv.Struct(UpdateFolderPolicyArg)

class UpdateFolderPolicyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UpdateFolderPolicyError_validator = bv.Union(UpdateFolderPolicyError)

class UseAnotherAccountOpenLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UseAnotherAccountOpenLinkResult_validator = bv.Struct(UseAnotherAccountOpenLinkResult)

class UserMembershipInfo(MembershipInfo):
    pass
# WARNING: Decompyle incomplete

UserMembershipInfo_validator = bv.Struct(UserMembershipInfo)

class UserFileMembershipInfo(UserMembershipInfo):
    pass
# WARNING: Decompyle incomplete

UserFileMembershipInfo_validator = bv.Struct(UserFileMembershipInfo)

class UserInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UserInfo_validator = bv.Struct(UserInfo)

class UserSubject(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UserSubject_validator = bv.Struct(UserSubject)

class UserTarget(Target):
    pass
# WARNING: Decompyle incomplete

UserTarget_validator = bv.Struct(UserTarget)

class ValidateFolderCreationArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ValidateFolderCreationArg_validator = bv.Struct(ValidateFolderCreationArg)

class ValidateFolderCreationError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ValidateFolderCreationError_validator = bv.Union(ValidateFolderCreationError)

class ValidateFolderCreationResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ValidateFolderCreationResponse_validator = bv.Struct(ValidateFolderCreationResponse)

class ValidateFolderNameArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ValidateFolderNameArg_validator = bv.Struct(ValidateFolderNameArg)

class ValidateFolderNameError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ValidateFolderNameError_validator = bv.Union(ValidateFolderNameError)

class ValidateFolderNameInvalidReason(bb.Union):
    pass
# WARNING: Decompyle incomplete

ValidateFolderNameInvalidReason_validator = bv.Union(ValidateFolderNameInvalidReason)

class ValidateFolderNameResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ValidateFolderNameResponse_validator = bv.Struct(ValidateFolderNameResponse)

class ValidateFolderPathArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ValidateFolderPathArg_validator = bv.Struct(ValidateFolderPathArg)

class ValidateFolderPathBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ValidateFolderPathBatchArg_validator = bv.Struct(ValidateFolderPathBatchArg)

class ValidateFolderPathBatchEntry(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ValidateFolderPathBatchEntry_validator = bv.Struct(ValidateFolderPathBatchEntry)

class ValidateFolderPathBatchEntryV2(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ValidateFolderPathBatchEntryV2_validator = bv.Struct(ValidateFolderPathBatchEntryV2)

class ValidateFolderPathBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ValidateFolderPathBatchResult_validator = bv.Struct(ValidateFolderPathBatchResult)

class ValidateFolderPathBatchResultV2(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ValidateFolderPathBatchResultV2_validator = bv.Struct(ValidateFolderPathBatchResultV2)

class ValidateFolderPathError(ShareFolderErrorBase):
    pass
# WARNING: Decompyle incomplete

ValidateFolderPathError_validator = bv.Union(ValidateFolderPathError)

class ValidateFolderPathErrorV2(ShareFolderErrorBaseV2):
    pass
# WARNING: Decompyle incomplete

ValidateFolderPathErrorV2_validator = bv.Union(ValidateFolderPathErrorV2)

class ValidateFolderPathIndividualResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

ValidateFolderPathIndividualResult_validator = bv.Union(ValidateFolderPathIndividualResult)

class ValidateFolderPathIndividualResultV2(bb.Union):
    pass
# WARNING: Decompyle incomplete

ValidateFolderPathIndividualResultV2_validator = bv.Union(ValidateFolderPathIndividualResultV2)

class ValidationError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ValidationError_validator = bv.Union(ValidationError)

class ValidationResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

ValidationResult_validator = bv.Union(ValidationResult)

class ValidationWarning(bb.Union):
    pass
# WARNING: Decompyle incomplete

ValidationWarning_validator = bv.Union(ValidationWarning)

class VerifyEmailOpenLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

VerifyEmailOpenLinkResult_validator = bv.Struct(VerifyEmailOpenLinkResult)

class ViewerInfoPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

ViewerInfoPolicy_validator = bv.Union(ViewerInfoPolicy)

class Visibility(bb.Union):
    pass
# WARNING: Decompyle incomplete

Visibility_validator = bv.Union(Visibility)

class VisibilityPolicy(bb.Struct):
    pass
# WARNING: Decompyle incomplete

VisibilityPolicy_validator = bv.Struct(VisibilityPolicy)

class AccessOrDenyReasonUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

AccessOrDenyReasonUnion_validator = bv.Union(AccessOrDenyReasonUnion)

class CreateEditLinkFolderDeniedReasonUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

CreateEditLinkFolderDeniedReasonUnion_validator = bv.Union(CreateEditLinkFolderDeniedReasonUnion)

class CreateSharedFolderDeniedReasonUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

CreateSharedFolderDeniedReasonUnion_validator = bv.Union(CreateSharedFolderDeniedReasonUnion)

class CreateViewLinkFolderDeniedReasonUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

CreateViewLinkFolderDeniedReasonUnion_validator = bv.Union(CreateViewLinkFolderDeniedReasonUnion)

class DisableViewerInfoFileDeniedReasonUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

DisableViewerInfoFileDeniedReasonUnion_validator = bv.Union(DisableViewerInfoFileDeniedReasonUnion)

class DisableViewerInfoFolderDeniedReasonUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

DisableViewerInfoFolderDeniedReasonUnion_validator = bv.Union(DisableViewerInfoFolderDeniedReasonUnion)

class EnableViewerInfoFileDeniedReasonUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

EnableViewerInfoFileDeniedReasonUnion_validator = bv.Union(EnableViewerInfoFileDeniedReasonUnion)

class EnableViewerInfoFolderDeniedReasonUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

EnableViewerInfoFolderDeniedReasonUnion_validator = bv.Union(EnableViewerInfoFolderDeniedReasonUnion)

class InviteEditorFolderDeniedReasonUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

InviteEditorFolderDeniedReasonUnion_validator = bv.Union(InviteEditorFolderDeniedReasonUnion)

class InviteViewerFolderDeniedReasonUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

InviteViewerFolderDeniedReasonUnion_validator = bv.Union(InviteViewerFolderDeniedReasonUnion)

class MetadataResponseUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

MetadataResponseUnion_validator = bv.Union(MetadataResponseUnion)

class SubjectIdUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

SubjectIdUnion_validator = bv.Union(SubjectIdUnion)

class SubjectUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

SubjectUnion_validator = bv.Union(SubjectUnion)

class UnshareFolderDeniedReasonUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

UnshareFolderDeniedReasonUnion_validator = bv.Union(UnshareFolderDeniedReasonUnion)
DropboxId_validator = bv.String(min_length = 1)
ExportSharedLinkArg_validator = GetSharedLinkMetadataArg_validator
ExportSharedLinkArg = GetSharedLinkMetadataArg
FileOrFolderContentId_validator = bv.String(pattern = '(file_obj_id|ns_id):.*')
FileOrFolderContentId_validator._redact = bv.BlotRedactor(None)
FqPathOrNsPath_validator = bv.String(min_length = 1, pattern = '(/.*|nspath:[0-9]+:.*)|ns:[0-9]+(/.*)?')
FqPathOrNsPath_validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
GetSharedLinkFileArg_validator = GetSharedLinkMetadataArg_validator
GetSharedLinkFileArg = GetSharedLinkMetadataArg
GrantAccessNotificationTargetObjectKey_validator = bv.String(pattern = 'sharing:grant_access-(file_obj_id|ns_id):.*-[0-9]+')
GrantAccessNotificationTargetObjectKey_validator._redact = bv.BlotRedactor(None)
Id_validator = files.Id_validator
InvitationSig_validator = bv.String()
Path_validator = files.Path_validator
PathOrId_validator = bv.String(min_length = 1, pattern = '((/|id:).*|nspath:[0-9]+:.*)|ns:[0-9]+(/.*)?')
PathOrId_validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
PathR_validator = bv.String(pattern = '(/(.|[\\r\\n])*)?|(ns:[0-9]+(/.*)?)')
PathR_validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
ReadPath_validator = files.ReadPath_validator
Rev_validator = files.Rev_validator
TeamInfo_validator = users.Team_validator
TeamInfo = users.Team
AccessAlreadyGranted.content_name.validator = bv.String()
AccessAlreadyGranted.content_name.validator._redact = bv.BlotRedactor(None)
AccessAlreadyGranted.content_type.validator = SharedContentType_validator
AccessAlreadyGranted._all_field_names_ = set([
    'content_name',
    'content_type'])
AccessAlreadyGranted._all_fields_ = [
    ('content_name', AccessAlreadyGranted.content_name.validator),
    ('content_type', AccessAlreadyGranted.content_type.validator)]
AccessInheritance._inherit_validator = bv.Void()
AccessInheritance._no_inherit_validator = bv.Void()
AccessInheritance._other_validator = bv.Void()
AccessInheritance._tagmap = {
    'inherit': AccessInheritance._inherit_validator,
    'no_inherit': AccessInheritance._no_inherit_validator,
    'other': AccessInheritance._other_validator }
AccessInheritance.inherit = AccessInheritance('inherit')
AccessInheritance.no_inherit = AccessInheritance('no_inherit')
AccessInheritance.other = AccessInheritance('other')
AccessLevel._owner_validator = bv.Void()
AccessLevel._editor_validator = bv.Void()
AccessLevel._viewer_validator = bv.Void()
AccessLevel._viewer_no_comment_validator = bv.Void()
AccessLevel._traverse_validator = bv.Void()
AccessLevel._no_access_validator = bv.Void()
AccessLevel._other_validator = bv.Void()
AccessLevel._tagmap = {
    'owner': AccessLevel._owner_validator,
    'editor': AccessLevel._editor_validator,
    'viewer': AccessLevel._viewer_validator,
    'viewer_no_comment': AccessLevel._viewer_no_comment_validator,
    'traverse': AccessLevel._traverse_validator,
    'no_access': AccessLevel._no_access_validator,
    'other': AccessLevel._other_validator }
AccessLevel.owner = AccessLevel('owner')
AccessLevel.editor = AccessLevel('editor')
AccessLevel.viewer = AccessLevel('viewer')
AccessLevel.viewer_no_comment = AccessLevel('viewer_no_comment')
AccessLevel.traverse = AccessLevel('traverse')
AccessLevel.no_access = AccessLevel('no_access')
AccessLevel.other = AccessLevel('other')
AccessType._access_type_unspecified_validator = bv.Void()
AccessType._owner_validator = bv.Void()
AccessType._editor_validator = bv.Void()
AccessType._viewer_validator = bv.Void()
AccessType._other_validator = bv.Void()
AccessType._tagmap = {
    'access_type_unspecified': AccessType._access_type_unspecified_validator,
    'owner': AccessType._owner_validator,
    'editor': AccessType._editor_validator,
    'viewer': AccessType._viewer_validator,
    'other': AccessType._other_validator }
AccessType.access_type_unspecified = AccessType('access_type_unspecified')
AccessType.owner = AccessType('owner')
AccessType.editor = AccessType('editor')
AccessType.viewer = AccessType('viewer')
AccessType.other = AccessType('other')
AccountSelectionRequiredOpenLinkResult._all_field_names_ = set([])
AccountSelectionRequiredOpenLinkResult._all_fields_ = []
AccountSelectionResolvedOpenLinkResult.uid.validator = bv.Int64()
AccountSelectionResolvedOpenLinkResult._all_field_names_ = set([
    'uid'])
AccountSelectionResolvedOpenLinkResult._all_fields_ = [
    ('uid', AccountSelectionResolvedOpenLinkResult.uid.validator)]
AccountSelectionStatus._unselected_validator = bv.Void()
AccountSelectionStatus._selected_validator = bv.Void()
AccountSelectionStatus._other_validator = bv.Void()
AccountSelectionStatus._tagmap = {
    'unselected': AccountSelectionStatus._unselected_validator,
    'selected': AccountSelectionStatus._selected_validator,
    'other': AccountSelectionStatus._other_validator }
AccountSelectionStatus.unselected = AccountSelectionStatus('unselected')
AccountSelectionStatus.selected = AccountSelectionStatus('selected')
AccountSelectionStatus.other = AccountSelectionStatus('other')
AclUpdatePolicy._owner_validator = bv.Void()
AclUpdatePolicy._editors_validator = bv.Void()
AclUpdatePolicy._other_validator = bv.Void()
AclUpdatePolicy._tagmap = {
    'owner': AclUpdatePolicy._owner_validator,
    'editors': AclUpdatePolicy._editors_validator,
    'other': AclUpdatePolicy._other_validator }
AclUpdatePolicy.owner = AclUpdatePolicy('owner')
AclUpdatePolicy.editors = AclUpdatePolicy('editors')
AclUpdatePolicy.other = AclUpdatePolicy('other')
AddFileMemberArgs.file.validator = PathOrId_validator
AddFileMemberArgs.members.validator = bv.List(MemberSelector_validator)
AddFileMemberArgs.custom_message.validator = bv.Nullable(bv.String())
AddFileMemberArgs.quiet.validator = bv.Boolean()
AddFileMemberArgs.quiet.validator._redact = bv.BlotRedactor(None)
AddFileMemberArgs.access_level.validator = bv.Nullable(AccessLevel_validator)
AddFileMemberArgs.add_message_as_comment.validator = bv.Boolean()
AddFileMemberArgs.add_message_as_comment.validator._redact = bv.BlotRedactor(None)
AddFileMemberArgs.fp_sealed_result.validator = bv.Nullable(bv.String())
AddFileMemberArgs.is_paper_migration.validator = bv.Boolean()
AddFileMemberArgs._all_field_names_ = set([
    'file',
    'members',
    'custom_message',
    'quiet',
    'access_level',
    'add_message_as_comment'])
AddFileMemberArgs._all_fields_ = [
    ('file', AddFileMemberArgs.file.validator),
    ('members', AddFileMemberArgs.members.validator),
    ('custom_message', AddFileMemberArgs.custom_message.validator),
    ('quiet', AddFileMemberArgs.quiet.validator),
    ('access_level', AddFileMemberArgs.access_level.validator),
    ('add_message_as_comment', AddFileMemberArgs.add_message_as_comment.validator)]
AddFileMemberArgs._all_internal_field_names_ = set([
    'fp_sealed_result',
    'is_paper_migration'])
AddFileMemberArgs._all_internal_fields_ = [
    ('fp_sealed_result', AddFileMemberArgs.fp_sealed_result.validator),
    ('is_paper_migration', AddFileMemberArgs.is_paper_migration.validator)]
AddFileMemberError._user_error_validator = SharingUserError_validator
AddFileMemberError._access_error_validator = SharingFileAccessError_validator
AddFileMemberError._rate_limit_validator = bv.Void()
AddFileMemberError._invalid_comment_validator = bv.Void()
AddFileMemberError._banned_member_validator = bv.Void()
AddFileMemberError._other_validator = bv.Void()
AddFileMemberError._tagmap = {
    'user_error': AddFileMemberError._user_error_validator,
    'access_error': AddFileMemberError._access_error_validator,
    'rate_limit': AddFileMemberError._rate_limit_validator,
    'invalid_comment': AddFileMemberError._invalid_comment_validator,
    'banned_member': AddFileMemberError._banned_member_validator,
    'other': AddFileMemberError._other_validator }
AddFileMemberError.rate_limit = AddFileMemberError('rate_limit')
AddFileMemberError.invalid_comment = AddFileMemberError('invalid_comment')
AddFileMemberError.banned_member = AddFileMemberError('banned_member')
AddFileMemberError.other = AddFileMemberError('other')
AddFolderMemberArg.shared_folder_id.validator = common.SharedFolderId_validator
AddFolderMemberArg.members.validator = bv.List(AddMember_validator)
AddFolderMemberArg.quiet.validator = bv.Boolean()
AddFolderMemberArg.quiet.validator._redact = bv.BlotRedactor(None)
AddFolderMemberArg.custom_message.validator = bv.Nullable(bv.String(min_length = 1))
AddFolderMemberArg.fp_sealed_result.validator = bv.Nullable(bv.String())
AddFolderMemberArg.is_paper_migration.validator = bv.Boolean()
AddFolderMemberArg._all_field_names_ = set([
    'shared_folder_id',
    'members',
    'quiet',
    'custom_message'])
AddFolderMemberArg._all_fields_ = [
    ('shared_folder_id', AddFolderMemberArg.shared_folder_id.validator),
    ('members', AddFolderMemberArg.members.validator),
    ('quiet', AddFolderMemberArg.quiet.validator),
    ('custom_message', AddFolderMemberArg.custom_message.validator)]
AddFolderMemberArg._all_internal_field_names_ = set([
    'fp_sealed_result',
    'is_paper_migration'])
AddFolderMemberArg._all_internal_fields_ = [
    ('fp_sealed_result', AddFolderMemberArg.fp_sealed_result.validator),
    ('is_paper_migration', AddFolderMemberArg.is_paper_migration.validator)]
AddFolderMemberEncryptionError._namespace_key_not_found_validator = bv.Void()
AddFolderMemberEncryptionError._not_team_member_validator = bv.Void()
AddFolderMemberEncryptionError._not_team_group_validator = bv.Void()
AddFolderMemberEncryptionError._user_has_no_account_validator = bv.Void()
AddFolderMemberEncryptionError._team_key_not_found_validator = bv.Void()
AddFolderMemberEncryptionError._shared_namespace_key_missing_validator = SharedNamespaceKeyMissingEncryptionError_validator
AddFolderMemberEncryptionError._not_supported_with_key_verification_enabled_validator = bv.Void()
AddFolderMemberEncryptionError._other_validator = bv.Void()
AddFolderMemberEncryptionError._permissioned_tagmaps = {
    'internal'}
AddFolderMemberEncryptionError._tagmap = {
    'other': AddFolderMemberEncryptionError._other_validator }
AddFolderMemberEncryptionError._internal_tagmap = {
    'namespace_key_not_found': AddFolderMemberEncryptionError._namespace_key_not_found_validator,
    'not_team_member': AddFolderMemberEncryptionError._not_team_member_validator,
    'not_team_group': AddFolderMemberEncryptionError._not_team_group_validator,
    'user_has_no_account': AddFolderMemberEncryptionError._user_has_no_account_validator,
    'team_key_not_found': AddFolderMemberEncryptionError._team_key_not_found_validator,
    'shared_namespace_key_missing': AddFolderMemberEncryptionError._shared_namespace_key_missing_validator,
    'not_supported_with_key_verification_enabled': AddFolderMemberEncryptionError._not_supported_with_key_verification_enabled_validator }
AddFolderMemberEncryptionError.namespace_key_not_found = AddFolderMemberEncryptionError('namespace_key_not_found')
AddFolderMemberEncryptionError.not_team_member = AddFolderMemberEncryptionError('not_team_member')
AddFolderMemberEncryptionError.not_team_group = AddFolderMemberEncryptionError('not_team_group')
AddFolderMemberEncryptionError.user_has_no_account = AddFolderMemberEncryptionError('user_has_no_account')
AddFolderMemberEncryptionError.team_key_not_found = AddFolderMemberEncryptionError('team_key_not_found')
AddFolderMemberEncryptionError.not_supported_with_key_verification_enabled = AddFolderMemberEncryptionError('not_supported_with_key_verification_enabled')
AddFolderMemberEncryptionError.other = AddFolderMemberEncryptionError('other')
AddFolderMemberError._access_error_validator = SharedFolderAccessError_validator
AddFolderMemberError._email_unverified_validator = bv.Void()
AddFolderMemberError._banned_member_validator = bv.Void()
AddFolderMemberError._bad_member_validator = AddMemberSelectorError_validator
AddFolderMemberError._cant_share_outside_team_validator = bv.Void()
AddFolderMemberError._too_many_members_validator = bv.UInt64()
AddFolderMemberError._too_many_members_validator._redact = bv.BlotRedactor(None)
AddFolderMemberError._too_many_pending_invites_validator = bv.UInt64()
AddFolderMemberError._too_many_pending_invites_validator._redact = bv.BlotRedactor(None)
AddFolderMemberError._rate_limit_validator = bv.Void()
AddFolderMemberError._too_many_invitees_validator = bv.Void()
AddFolderMemberError._insufficient_plan_validator = bv.Void()
AddFolderMemberError._team_folder_validator = bv.Void()
AddFolderMemberError._no_permission_validator = bv.Void()
AddFolderMemberError._invalid_shared_folder_validator = bv.Void()
AddFolderMemberError._encryption_error_validator = AddFolderMemberEncryptionError_validator
AddFolderMemberError._other_validator = bv.Void()
AddFolderMemberError._permissioned_tagmaps = {
    'internal'}
AddFolderMemberError._tagmap = {
    'access_error': AddFolderMemberError._access_error_validator,
    'email_unverified': AddFolderMemberError._email_unverified_validator,
    'banned_member': AddFolderMemberError._banned_member_validator,
    'bad_member': AddFolderMemberError._bad_member_validator,
    'cant_share_outside_team': AddFolderMemberError._cant_share_outside_team_validator,
    'too_many_members': AddFolderMemberError._too_many_members_validator,
    'too_many_pending_invites': AddFolderMemberError._too_many_pending_invites_validator,
    'rate_limit': AddFolderMemberError._rate_limit_validator,
    'too_many_invitees': AddFolderMemberError._too_many_invitees_validator,
    'insufficient_plan': AddFolderMemberError._insufficient_plan_validator,
    'team_folder': AddFolderMemberError._team_folder_validator,
    'no_permission': AddFolderMemberError._no_permission_validator,
    'invalid_shared_folder': AddFolderMemberError._invalid_shared_folder_validator,
    'other': AddFolderMemberError._other_validator }
AddFolderMemberError._internal_tagmap = {
    'encryption_error': AddFolderMemberError._encryption_error_validator }
AddFolderMemberError.email_unverified = AddFolderMemberError('email_unverified')
AddFolderMemberError.banned_member = AddFolderMemberError('banned_member')
AddFolderMemberError.cant_share_outside_team = AddFolderMemberError('cant_share_outside_team')
AddFolderMemberError.rate_limit = AddFolderMemberError('rate_limit')
AddFolderMemberError.too_many_invitees = AddFolderMemberError('too_many_invitees')
AddFolderMemberError.insufficient_plan = AddFolderMemberError('insufficient_plan')
AddFolderMemberError.team_folder = AddFolderMemberError('team_folder')
AddFolderMemberError.no_permission = AddFolderMemberError('no_permission')
AddFolderMemberError.invalid_shared_folder = AddFolderMemberError('invalid_shared_folder')
AddFolderMemberError.other = AddFolderMemberError('other')
AddFolderMemberResult.sckey_sha1.validator = bv.String()
AddFolderMemberResult.sckey_sha1.validator._redact = bv.BlotRedactor(None)
AddFolderMemberResult.invitation_signature.validator = bv.List(bv.String())
AddFolderMemberResult.invitation_signature.validator._redact = bv.BlotRedactor(None)
AddFolderMemberResult._all_field_names_ = set([
    'sckey_sha1',
    'invitation_signature'])
AddFolderMemberResult._all_fields_ = [
    ('sckey_sha1', AddFolderMemberResult.sckey_sha1.validator),
    ('invitation_signature', AddFolderMemberResult.invitation_signature.validator)]
AddMember.member.validator = MemberSelector_validator
AddMember.access_level.validator = bv.Nullable(AccessLevel_validator)
AddMember._all_field_names_ = set([
    'member',
    'access_level'])
AddMember._all_fields_ = [
    ('member', AddMember.member.validator),
    ('access_level', AddMember.access_level.validator)]
AddMemberArg.content.validator = Content_validator
AddMemberArg.members.validator = bv.List(MemberSelector_validator)
AddMemberArg.access_level.validator = bv.Nullable(AccessLevel_validator)
AddMemberArg.custom_message.validator = bv.Nullable(bv.String())
AddMemberArg.allow_unuploaded.validator = bv.Boolean()
AddMemberArg.allow_unuploaded.validator._redact = bv.BlotRedactor(None)
AddMemberArg._all_field_names_ = set([
    'content',
    'members',
    'access_level',
    'custom_message',
    'allow_unuploaded'])
AddMemberArg._all_fields_ = [
    ('content', AddMemberArg.content.validator),
    ('members', AddMemberArg.members.validator),
    ('access_level', AddMemberArg.access_level.validator),
    ('custom_message', AddMemberArg.custom_message.validator),
    ('allow_unuploaded', AddMemberArg.allow_unuploaded.validator)]
AddMemberError._generic_error_validator = bv.Nullable(bv.String())
AddMemberError._other_validator = bv.Void()
AddMemberError._tagmap = {
    'generic_error': AddMemberError._generic_error_validator,
    'other': AddMemberError._other_validator }
AddMemberError.other = AddMemberError('other')
AddMemberResult._success_validator = bv.List(FileMemberActionResult_validator)
AddMemberResult._pending_validator = PendingResult_validator
AddMemberResult._other_validator = bv.Void()
AddMemberResult._tagmap = {
    'success': AddMemberResult._success_validator,
    'pending': AddMemberResult._pending_validator,
    'other': AddMemberResult._other_validator }
AddMemberResult.other = AddMemberResult('other')
AddMemberSelectorError._automatic_group_validator = bv.Void()
AddMemberSelectorError._invalid_dropbox_id_validator = DropboxId_validator
AddMemberSelectorError._invalid_email_validator = common.EmailAddress_validator
AddMemberSelectorError._invalid_group_validator = bv.Void()
AddMemberSelectorError._unverified_dropbox_id_validator = DropboxId_validator
AddMemberSelectorError._group_deleted_validator = bv.Void()
AddMemberSelectorError._group_not_on_team_validator = bv.Void()
AddMemberSelectorError._other_validator = bv.Void()
AddMemberSelectorError._tagmap = {
    'automatic_group': AddMemberSelectorError._automatic_group_validator,
    'invalid_dropbox_id': AddMemberSelectorError._invalid_dropbox_id_validator,
    'invalid_email': AddMemberSelectorError._invalid_email_validator,
    'invalid_group': AddMemberSelectorError._invalid_group_validator,
    'unverified_dropbox_id': AddMemberSelectorError._unverified_dropbox_id_validator,
    'group_deleted': AddMemberSelectorError._group_deleted_validator,
    'group_not_on_team': AddMemberSelectorError._group_not_on_team_validator,
    'other': AddMemberSelectorError._other_validator }
AddMemberSelectorError.automatic_group = AddMemberSelectorError('automatic_group')
AddMemberSelectorError.invalid_group = AddMemberSelectorError('invalid_group')
AddMemberSelectorError.group_deleted = AddMemberSelectorError('group_deleted')
AddMemberSelectorError.group_not_on_team = AddMemberSelectorError('group_not_on_team')
AddMemberSelectorError.other = AddMemberSelectorError('other')
AlphaCreateSharedLinkWithSettingsArg.path.validator = ReadPath_validator
AlphaCreateSharedLinkWithSettingsArg.pending_upload.validator = bv.Nullable(PendingUploadMode_validator)
AlphaCreateSharedLinkWithSettingsArg.settings.validator = bv.Nullable(AlphaSharedLinkSettings_validator)
AlphaCreateSharedLinkWithSettingsArg.app_key.validator = bv.Nullable(bv.String())
AlphaCreateSharedLinkWithSettingsArg.debug_hashless.validator = bv.Nullable(bv.Boolean())
AlphaCreateSharedLinkWithSettingsArg._all_field_names_ = set([
    'path',
    'pending_upload',
    'settings'])
AlphaCreateSharedLinkWithSettingsArg._all_fields_ = [
    ('path', AlphaCreateSharedLinkWithSettingsArg.path.validator),
    ('pending_upload', AlphaCreateSharedLinkWithSettingsArg.pending_upload.validator),
    ('settings', AlphaCreateSharedLinkWithSettingsArg.settings.validator)]
AlphaCreateSharedLinkWithSettingsArg._all_internal_field_names_ = set([
    'app_key',
    'debug_hashless'])
AlphaCreateSharedLinkWithSettingsArg._all_internal_fields_ = [
    ('app_key', AlphaCreateSharedLinkWithSettingsArg.app_key.validator),
    ('debug_hashless', AlphaCreateSharedLinkWithSettingsArg.debug_hashless.validator)]
FileAction._disable_viewer_info_validator = bv.Void()
FileAction._edit_contents_validator = bv.Void()
FileAction._enable_viewer_info_validator = bv.Void()
FileAction._invite_viewer_validator = bv.Void()
FileAction._invite_viewer_no_comment_validator = bv.Void()
FileAction._invite_editor_validator = bv.Void()
FileAction._unshare_validator = bv.Void()
FileAction._relinquish_membership_validator = bv.Void()
FileAction._share_link_validator = bv.Void()
FileAction._create_link_validator = bv.Void()
FileAction._create_view_link_validator = bv.Void()
FileAction._create_edit_link_validator = bv.Void()
FileAction._other_validator = bv.Void()
FileAction._tagmap = {
    'disable_viewer_info': FileAction._disable_viewer_info_validator,
    'edit_contents': FileAction._edit_contents_validator,
    'enable_viewer_info': FileAction._enable_viewer_info_validator,
    'invite_viewer': FileAction._invite_viewer_validator,
    'invite_viewer_no_comment': FileAction._invite_viewer_no_comment_validator,
    'invite_editor': FileAction._invite_editor_validator,
    'unshare': FileAction._unshare_validator,
    'relinquish_membership': FileAction._relinquish_membership_validator,
    'share_link': FileAction._share_link_validator,
    'create_link': FileAction._create_link_validator,
    'create_view_link': FileAction._create_view_link_validator,
    'create_edit_link': FileAction._create_edit_link_validator,
    'other': FileAction._other_validator }
FileAction.disable_viewer_info = FileAction('disable_viewer_info')
FileAction.edit_contents = FileAction('edit_contents')
FileAction.enable_viewer_info = FileAction('enable_viewer_info')
FileAction.invite_viewer = FileAction('invite_viewer')
FileAction.invite_viewer_no_comment = FileAction('invite_viewer_no_comment')
FileAction.invite_editor = FileAction('invite_editor')
FileAction.unshare = FileAction('unshare')
FileAction.relinquish_membership = FileAction('relinquish_membership')
FileAction.share_link = FileAction('share_link')
FileAction.create_link = FileAction('create_link')
FileAction.create_view_link = FileAction('create_view_link')
FileAction.create_edit_link = FileAction('create_edit_link')
FileAction.other = FileAction('other')
AlphaFileAction._change_options_validator = bv.Void()
AlphaFileAction._remove_download_policy_validator = bv.Void()
AlphaFileAction._set_download_policy_validator = bv.Void()
AlphaFileAction._share_message_as_comment_validator = bv.Void()
AlphaFileAction._tagmap = {
    'change_options': AlphaFileAction._change_options_validator,
    'remove_download_policy': AlphaFileAction._remove_download_policy_validator,
    'set_download_policy': AlphaFileAction._set_download_policy_validator,
    'share_message_as_comment': AlphaFileAction._share_message_as_comment_validator }
AlphaFileAction._tagmap.update(FileAction._tagmap)
AlphaFileAction.change_options = AlphaFileAction('change_options')
AlphaFileAction.remove_download_policy = AlphaFileAction('remove_download_policy')
AlphaFileAction.set_download_policy = AlphaFileAction('set_download_policy')
AlphaFileAction.share_message_as_comment = AlphaFileAction('share_message_as_comment')
AlphaSharedLinkMetadata.url.validator = bv.String()
AlphaSharedLinkMetadata.url.validator._redact = bv.HashRedactor(None)
AlphaSharedLinkMetadata.id.validator = bv.Nullable(Id_validator)
AlphaSharedLinkMetadata.name.validator = bv.String()
AlphaSharedLinkMetadata.name.validator._redact = bv.BlotRedactor(None)
AlphaSharedLinkMetadata.expires.validator = bv.Nullable(common.DropboxTimestamp_validator)
AlphaSharedLinkMetadata.path_lower.validator = bv.Nullable(bv.String())
AlphaSharedLinkMetadata.path_lower.validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
AlphaSharedLinkMetadata.link_permissions.validator = AlphaLinkPermissions_validator
AlphaSharedLinkMetadata.team_member_info.validator = bv.Nullable(TeamMemberInfo_validator)
AlphaSharedLinkMetadata.content_owner_team_info.validator = bv.Nullable(TeamInfo_validator)
AlphaSharedLinkMetadata.preview_type.validator = bv.Nullable(bv.String())
AlphaSharedLinkMetadata.icon_url.validator = bv.Nullable(bv.String())
AlphaSharedLinkMetadata.invitation_sig.validator = bv.Nullable(InvitationSig_validator)
AlphaSharedLinkMetadata.created_timestamp.validator = bv.Nullable(common.DropboxTimestamp_validator)
AlphaSharedLinkMetadata._field_names_ = set([
    'url',
    'id',
    'name',
    'expires',
    'path_lower',
    'link_permissions',
    'team_member_info',
    'content_owner_team_info',
    'preview_type',
    'icon_url',
    'created_timestamp'])
AlphaSharedLinkMetadata._all_field_names_ = AlphaSharedLinkMetadata._field_names_
AlphaSharedLinkMetadata._fields_ = [
    ('url', AlphaSharedLinkMetadata.url.validator),
    ('id', AlphaSharedLinkMetadata.id.validator),
    ('name', AlphaSharedLinkMetadata.name.validator),
    ('expires', AlphaSharedLinkMetadata.expires.validator),
    ('path_lower', AlphaSharedLinkMetadata.path_lower.validator),
    ('link_permissions', AlphaSharedLinkMetadata.link_permissions.validator),
    ('team_member_info', AlphaSharedLinkMetadata.team_member_info.validator),
    ('content_owner_team_info', AlphaSharedLinkMetadata.content_owner_team_info.validator),
    ('preview_type', AlphaSharedLinkMetadata.preview_type.validator),
    ('icon_url', AlphaSharedLinkMetadata.icon_url.validator),
    ('created_timestamp', AlphaSharedLinkMetadata.created_timestamp.validator)]
AlphaSharedLinkMetadata._all_fields_ = AlphaSharedLinkMetadata._fields_
AlphaSharedLinkMetadata._internal_field_names_ = set([
    'invitation_sig'])
AlphaSharedLinkMetadata._all_internal_field_names_ = AlphaSharedLinkMetadata._internal_field_names_
AlphaSharedLinkMetadata._internal_fields_ = [
    ('invitation_sig', AlphaSharedLinkMetadata.invitation_sig.validator)]
AlphaSharedLinkMetadata._all_internal_fields_ = AlphaSharedLinkMetadata._internal_fields_
AlphaSharedLinkMetadata._tag_to_subtype_ = {
    ('file',): AlphaFileLinkMetadata_validator,
    ('folder',): AlphaFolderLinkMetadata_validator,
    ('unuploaded',): AlphaUnuploadedLinkMetadata_validator }
AlphaSharedLinkMetadata._pytype_to_tag_and_subtype_ = {
    AlphaUnuploadedLinkMetadata: (('unuploaded',), AlphaUnuploadedLinkMetadata_validator),
    AlphaFolderLinkMetadata: (('folder',), AlphaFolderLinkMetadata_validator),
    AlphaFileLinkMetadata: (('file',), AlphaFileLinkMetadata_validator) }
AlphaSharedLinkMetadata._is_catch_all_ = True
AlphaFileLinkMetadata.client_modified.validator = common.DropboxTimestamp_validator
AlphaFileLinkMetadata.server_modified.validator = common.DropboxTimestamp_validator
AlphaFileLinkMetadata.rev.validator = Rev_validator
AlphaFileLinkMetadata.size.validator = bv.UInt64()
AlphaFileLinkMetadata.size.validator._redact = bv.BlotRedactor(None)
AlphaFileLinkMetadata.thumbnail_urls.validator = bv.Nullable(bv.Map(bv.String(), bv.String()))
AlphaFileLinkMetadata._field_names_ = set([
    'client_modified',
    'server_modified',
    'rev',
    'size',
    'thumbnail_urls'])
AlphaFileLinkMetadata._all_field_names_ = AlphaSharedLinkMetadata._all_field_names_.union(AlphaFileLinkMetadata._field_names_)
AlphaFileLinkMetadata._fields_ = [
    ('client_modified', AlphaFileLinkMetadata.client_modified.validator),
    ('server_modified', AlphaFileLinkMetadata.server_modified.validator),
    ('rev', AlphaFileLinkMetadata.rev.validator),
    ('size', AlphaFileLinkMetadata.size.validator),
    ('thumbnail_urls', AlphaFileLinkMetadata.thumbnail_urls.validator)]
AlphaFileLinkMetadata._all_fields_ = AlphaSharedLinkMetadata._all_fields_ + AlphaFileLinkMetadata._fields_
AlphaFileLinkMetadata._all_internal_field_names_ = AlphaSharedLinkMetadata._all_internal_field_names_.union(AlphaFileLinkMetadata._internal_field_names_)
AlphaFileLinkMetadata._internal_fields_ = []
AlphaFileLinkMetadata._all_internal_fields_ = AlphaSharedLinkMetadata._all_internal_fields_ + AlphaFileLinkMetadata._internal_fields_
AlphaFilePermission.action.validator = AlphaFileAction_validator
AlphaFilePermission.allow.validator = bv.Boolean()
AlphaFilePermission.allow.validator._redact = bv.BlotRedactor(None)
AlphaFilePermission.reason.validator = bv.Nullable(PermissionDeniedReason_validator)
AlphaFilePermission._all_field_names_ = set([
    'action',
    'allow',
    'reason'])
AlphaFilePermission._all_fields_ = [
    ('action', AlphaFilePermission.action.validator),
    ('allow', AlphaFilePermission.allow.validator),
    ('reason', AlphaFilePermission.reason.validator)]
FolderAction._change_options_validator = bv.Void()
FolderAction._disable_viewer_info_validator = bv.Void()
FolderAction._edit_contents_validator = bv.Void()
FolderAction._enable_viewer_info_validator = bv.Void()
FolderAction._invite_editor_validator = bv.Void()
FolderAction._invite_viewer_validator = bv.Void()
FolderAction._invite_viewer_no_comment_validator = bv.Void()
FolderAction._relinquish_membership_validator = bv.Void()
FolderAction._unmount_validator = bv.Void()
FolderAction._unshare_validator = bv.Void()
FolderAction._leave_a_copy_validator = bv.Void()
FolderAction._share_link_validator = bv.Void()
FolderAction._create_link_validator = bv.Void()
FolderAction._create_view_link_validator = bv.Void()
FolderAction._create_edit_link_validator = bv.Void()
FolderAction._set_access_inheritance_validator = bv.Void()
FolderAction._other_validator = bv.Void()
# WARNING: Decompyle incomplete
