# Source Generated with Decompyle++
# File: files.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import account_id
from dropbox.api.v2.datatypes import async_
from dropbox.api.v2.datatypes import common
from dropbox.api.v2.datatypes import encryption
from dropbox.api.v2.datatypes import file_properties
from dropbox.api.v2.datatypes import file_viewer_preview_metadata
from dropbox.api.v2.datatypes import files_v2
from dropbox.api.v2.datatypes import fql
from dropbox.api.v2.datatypes import per_node_metadata
from dropbox.api.v2.datatypes import users_common
from dropbox.api.v2.datatypes import version_tree

class AddTagArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AddTagArg_validator = bv.Struct(AddTagArg)

class BaseTagError(bb.Union):
    pass
# WARNING: Decompyle incomplete

BaseTagError_validator = bv.Union(BaseTagError)

class AddTagError(BaseTagError):
    pass
# WARNING: Decompyle incomplete

AddTagError_validator = bv.Union(AddTagError)

class GetMetadataArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetMetadataArg_validator = bv.Struct(GetMetadataArg)

class AlphaGetMetadataArg(GetMetadataArg):
    pass
# WARNING: Decompyle incomplete

AlphaGetMetadataArg_validator = bv.Struct(AlphaGetMetadataArg)

class GetMetadataError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetMetadataError_validator = bv.Union(GetMetadataError)

class AlphaGetMetadataError(GetMetadataError):
    pass
# WARNING: Decompyle incomplete

AlphaGetMetadataError_validator = bv.Union(AlphaGetMetadataError)

class ApiFileIdMode(bb.Union):
    pass
# WARNING: Decompyle incomplete

ApiFileIdMode_validator = bv.Union(ApiFileIdMode)

class AsyncJobResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

AsyncJobResult_validator = bv.Union(AsyncJobResult)

class AudioSpecificMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AudioSpecificMetadata_validator = bv.Struct(AudioSpecificMetadata)

class BoltTokenResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BoltTokenResponse_validator = bv.Struct(BoltTokenResponse)

class BrowseBoltDataArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseBoltDataArg_validator = bv.Struct(BrowseBoltDataArg)

class BrowseBoltDataError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseBoltDataError_validator = bv.Struct(BrowseBoltDataError)

class BrowseBoltDataResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseBoltDataResult_validator = bv.Struct(BrowseBoltDataResult)

class BrowseContext(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseContext_validator = bv.Struct(BrowseContext)

class BrowseContextCypress(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseContextCypress_validator = bv.Struct(BrowseContextCypress)

class BrowseContextResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseContextResponse_validator = bv.Struct(BrowseContextResponse)

class BrowseContextResponseCypress(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseContextResponseCypress_validator = bv.Struct(BrowseContextResponseCypress)

class BrowseErrorStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

BrowseErrorStatus_validator = bv.Union(BrowseErrorStatus)

class BrowseGetNextResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseGetNextResponse_validator = bv.Struct(BrowseGetNextResponse)

class BrowseGetNextResponseCypress(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseGetNextResponseCypress_validator = bv.Struct(BrowseGetNextResponseCypress)

class BrowsePaginatedFileInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowsePaginatedFileInfo_validator = bv.Struct(BrowsePaginatedFileInfo)

class BrowsePaginatedObjectInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowsePaginatedObjectInfo_validator = bv.Struct(BrowsePaginatedObjectInfo)

class BrowseRecentItem(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseRecentItem_validator = bv.Struct(BrowseRecentItem)

class BrowseTeamContentArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseTeamContentArg_validator = bv.Struct(BrowseTeamContentArg)

class BrowseV2Arg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseV2Arg_validator = bv.Struct(BrowseV2Arg)

class BrowseV2ContinueArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseV2ContinueArg_validator = bv.Struct(BrowseV2ContinueArg)

class BrowseV2Error(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseV2Error_validator = bv.Struct(BrowseV2Error)

class BrowseV2Result(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseV2Result_validator = bv.Struct(BrowseV2Result)

class BrowseV3Arg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseV3Arg_validator = bv.Struct(BrowseV3Arg)

class BrowseV3ContinueArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseV3ContinueArg_validator = bv.Struct(BrowseV3ContinueArg)

class BrowseV3Result(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrowseV3Result_validator = bv.Struct(BrowseV3Result)

class Changeset(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Changeset_validator = bv.Struct(Changeset)

class ChangesetData(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ChangesetData_validator = bv.Struct(ChangesetData)

class ChannelId(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ChannelId_validator = bv.Struct(ChannelId)

class Classifier(bb.Union):
    pass
# WARNING: Decompyle incomplete

Classifier_validator = bv.Union(Classifier)

class CloudDocClass(bb.Union):
    pass
# WARNING: Decompyle incomplete

CloudDocClass_validator = bv.Union(CloudDocClass)

class CloudDocInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CloudDocInfo_validator = bv.Struct(CloudDocInfo)

class CloudDocSize(bb.Union):
    pass
# WARNING: Decompyle incomplete

CloudDocSize_validator = bv.Union(CloudDocSize)

class CloudDocType(bb.Union):
    pass
# WARNING: Decompyle incomplete

CloudDocType_validator = bv.Union(CloudDocType)

class CommitInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CommitInfo_validator = bv.Struct(CommitInfo)

class ContentSyncSetting(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContentSyncSetting_validator = bv.Struct(ContentSyncSetting)

class ContentSyncSettingArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContentSyncSettingArg_validator = bv.Struct(ContentSyncSettingArg)

class ContentTileMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContentTileMetadata_validator = bv.Struct(ContentTileMetadata)

class ContentTilesDocMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContentTilesDocMetadata_validator = bv.Struct(ContentTilesDocMetadata)

class ContentTilesFlags(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContentTilesFlags_validator = bv.Struct(ContentTilesFlags)

class ContentTilesFolderMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContentTilesFolderMetadata_validator = bv.Struct(ContentTilesFolderMetadata)

class ContentTilesImageAnalysisMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContentTilesImageAnalysisMetadata_validator = bv.Struct(ContentTilesImageAnalysisMetadata)

class ContentTilesMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContentTilesMetadata_validator = bv.Struct(ContentTilesMetadata)

class ContentTilesMetadataV2Arg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContentTilesMetadataV2Arg_validator = bv.Struct(ContentTilesMetadataV2Arg)

class ContentTilesMetadataV2Error(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContentTilesMetadataV2Error_validator = bv.Struct(ContentTilesMetadataV2Error)

class ContentTilesMetadataV2ErrorStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

ContentTilesMetadataV2ErrorStatus_validator = bv.Union(ContentTilesMetadataV2ErrorStatus)

class ContentTilesMetadataV2Result(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContentTilesMetadataV2Result_validator = bv.Struct(ContentTilesMetadataV2Result)

class ContentTilesPdfMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContentTilesPdfMetadata_validator = bv.Struct(ContentTilesPdfMetadata)

class ContentTilesVideoMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContentTilesVideoMetadata_validator = bv.Struct(ContentTilesVideoMetadata)

class CreateFolderArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreateFolderArg_validator = bv.Struct(CreateFolderArg)

class CreateFolderBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreateFolderBatchArg_validator = bv.Struct(CreateFolderBatchArg)

class CreateFolderBatchError(bb.Union):
    pass
# WARNING: Decompyle incomplete

CreateFolderBatchError_validator = bv.Union(CreateFolderBatchError)

class CreateFolderBatchJobStatus(async_.PollResultBase):
    pass
# WARNING: Decompyle incomplete

CreateFolderBatchJobStatus_validator = bv.Union(CreateFolderBatchJobStatus)

class CreateFolderBatchLaunch(async_.LaunchResultBase):
    pass
# WARNING: Decompyle incomplete

CreateFolderBatchLaunch_validator = bv.Union(CreateFolderBatchLaunch)

class FileOpsResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FileOpsResult_validator = bv.Struct(FileOpsResult)

class CreateFolderBatchResult(FileOpsResult):
    pass
# WARNING: Decompyle incomplete

CreateFolderBatchResult_validator = bv.Struct(CreateFolderBatchResult)

class CreateFolderBatchResultEntry(bb.Union):
    pass
# WARNING: Decompyle incomplete

CreateFolderBatchResultEntry_validator = bv.Union(CreateFolderBatchResultEntry)

class CreateFolderEntryError(bb.Union):
    pass
# WARNING: Decompyle incomplete

CreateFolderEntryError_validator = bv.Union(CreateFolderEntryError)

class CreateFolderEntryResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreateFolderEntryResult_validator = bv.Struct(CreateFolderEntryResult)

class CreateFolderError(bb.Union):
    pass
# WARNING: Decompyle incomplete

CreateFolderError_validator = bv.Union(CreateFolderError)

class CreateFolderResult(FileOpsResult):
    pass
# WARNING: Decompyle incomplete

CreateFolderResult_validator = bv.Struct(CreateFolderResult)

class Cursor(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Cursor_validator = bv.Struct(Cursor)

class CursorType(bb.Union):
    pass
# WARNING: Decompyle incomplete

CursorType_validator = bv.Union(CursorType)

class DateRange(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DateRange_validator = bv.Struct(DateRange)

class DcsArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DcsArgs_validator = bv.Struct(DcsArgs)

class DeleteArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeleteArg_validator = bv.Struct(DeleteArg)

class DeleteBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeleteBatchArg_validator = bv.Struct(DeleteBatchArg)

class DeleteBatchError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DeleteBatchError_validator = bv.Union(DeleteBatchError)

class DeleteBatchJobStatus(async_.PollResultBase):
    pass
# WARNING: Decompyle incomplete

DeleteBatchJobStatus_validator = bv.Union(DeleteBatchJobStatus)

class DeleteBatchLaunch(async_.LaunchResultBase):
    pass
# WARNING: Decompyle incomplete

DeleteBatchLaunch_validator = bv.Union(DeleteBatchLaunch)

class DeleteBatchResult(FileOpsResult):
    pass
# WARNING: Decompyle incomplete

DeleteBatchResult_validator = bv.Struct(DeleteBatchResult)

class DeleteBatchResultData(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeleteBatchResultData_validator = bv.Struct(DeleteBatchResultData)

class DeleteBatchResultEntry(bb.Union):
    pass
# WARNING: Decompyle incomplete

DeleteBatchResultEntry_validator = bv.Union(DeleteBatchResultEntry)

class DeleteError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DeleteError_validator = bv.Union(DeleteError)

class DeleteResult(FileOpsResult):
    pass
# WARNING: Decompyle incomplete

DeleteResult_validator = bv.Struct(DeleteResult)

class Metadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Metadata_validator = bv.StructTree(Metadata)

class DeletedMetadata(Metadata):
    pass
# WARNING: Decompyle incomplete

DeletedMetadata_validator = bv.Struct(DeletedMetadata)

class DeletedNsidInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeletedNsidInfo_validator = bv.Struct(DeletedNsidInfo)

class DeletedRootOidInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeletedRootOidInfo_validator = bv.Struct(DeletedRootOidInfo)

class DialogInfoError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DialogInfoError_validator = bv.Struct(DialogInfoError)

class Dimension(bb.Union):
    pass
# WARNING: Decompyle incomplete

Dimension_validator = bv.Union(Dimension)

class Dimensions(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Dimensions_validator = bv.Struct(Dimensions)

class DownloadArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DownloadArg_validator = bv.Struct(DownloadArg)

class DownloadError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DownloadError_validator = bv.Union(DownloadError)

class DownloadZipArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DownloadZipArg_validator = bv.Struct(DownloadZipArg)

class DownloadZipError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DownloadZipError_validator = bv.Union(DownloadZipError)

class DownloadZipResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DownloadZipResult_validator = bv.Struct(DownloadZipResult)

class ExportArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ExportArg_validator = bv.Struct(ExportArg)

class ExportError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ExportError_validator = bv.Union(ExportError)

class ExportInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ExportInfo_validator = bv.Struct(ExportInfo)

class ExportMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ExportMetadata_validator = bv.Struct(ExportMetadata)

class ExportResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ExportResult_validator = bv.Struct(ExportResult)

class ExtendedMetadata(bb.Union):
    pass
# WARNING: Decompyle incomplete

ExtendedMetadata_validator = bv.Union(ExtendedMetadata)

class ExtendedSearchMatch(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ExtendedSearchMatch_validator = bv.Struct(ExtendedSearchMatch)

class ExtendedSearchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ExtendedSearchResult_validator = bv.Struct(ExtendedSearchResult)

class Fsw(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Fsw_validator = bv.Struct(Fsw)

class FswDialogInfoError(DialogInfoError):
    pass
# WARNING: Decompyle incomplete

FswDialogInfoError_validator = bv.Struct(FswDialogInfoError)

class FswRequest(bb.Union):
    pass
# WARNING: Decompyle incomplete

FswRequest_validator = bv.Union(FswRequest)

class FileCategory(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileCategory_validator = bv.Union(FileCategory)

class FileContent(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FileContent_validator = bv.Struct(FileContent)

class FileContentNotFoundReason(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileContentNotFoundReason_validator = bv.Union(FileContentNotFoundReason)

class FileEncryptionInfoMissingEncryptionError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FileEncryptionInfoMissingEncryptionError_validator = bv.Struct(FileEncryptionInfoMissingEncryptionError)

class FileIdentifier(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileIdentifier_validator = bv.Union(FileIdentifier)

class FileInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FileInfo_validator = bv.Struct(FileInfo)

class FileLock(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FileLock_validator = bv.Struct(FileLock)

class FileLockContent(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileLockContent_validator = bv.Union(FileLockContent)

class FileLockInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FileLockInfo_validator = bv.Struct(FileLockInfo)

class FileLockMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FileLockMetadata_validator = bv.Struct(FileLockMetadata)

class FileMetadata(Metadata):
    pass
# WARNING: Decompyle incomplete

FileMetadata_validator = bv.Struct(FileMetadata)

class FileMetadataError(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileMetadataError_validator = bv.Union(FileMetadataError)

class FileMetadataStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileMetadataStatus_validator = bv.Union(FileMetadataStatus)

class SharingInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharingInfo_validator = bv.Struct(SharingInfo)

class FileSharingInfo(SharingInfo):
    pass
# WARNING: Decompyle incomplete

FileSharingInfo_validator = bv.Struct(FileSharingInfo)

class FileSpecificMetadata(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileSpecificMetadata_validator = bv.Union(FileSpecificMetadata)

class FileStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileStatus_validator = bv.Union(FileStatus)

class FileSystemWarnings(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FileSystemWarnings_validator = bv.Struct(FileSystemWarnings)

class FileType(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileType_validator = bv.Union(FileType)

class FilesTeamFolderCheckArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderCheckArg_validator = bv.Struct(FilesTeamFolderCheckArg)

class FilesTeamFolderCheckResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderCheckResult_validator = bv.Struct(FilesTeamFolderCheckResult)

class FilesTeamFolderCopyArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderCopyArg_validator = bv.Struct(FilesTeamFolderCopyArg)

class FilesTeamFolderCopyResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderCopyResponse_validator = bv.Struct(FilesTeamFolderCopyResponse)

class FilesTeamFolderCountArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderCountArg_validator = bv.Struct(FilesTeamFolderCountArg)

class FilesTeamFolderCountResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderCountResponse_validator = bv.Struct(FilesTeamFolderCountResponse)

class FilesTeamFolderCreateArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderCreateArg_validator = bv.Struct(FilesTeamFolderCreateArg)

class FilesTeamFolderCreateResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderCreateResponse_validator = bv.Struct(FilesTeamFolderCreateResponse)

class FilesTeamFolderDeleteArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderDeleteArg_validator = bv.Struct(FilesTeamFolderDeleteArg)

class FilesTeamFolderDeleteResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderDeleteResponse_validator = bv.Struct(FilesTeamFolderDeleteResponse)

class FilesTeamFolderError(bb.Union):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderError_validator = bv.Union(FilesTeamFolderError)

class FilesTeamFolderMoveArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderMoveArg_validator = bv.Struct(FilesTeamFolderMoveArg)

class FilesTeamFolderMoveResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderMoveResponse_validator = bv.Struct(FilesTeamFolderMoveResponse)

class FilesTeamFolderRenameArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderRenameArg_validator = bv.Struct(FilesTeamFolderRenameArg)

class FilesTeamFolderRenameResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderRenameResponse_validator = bv.Struct(FilesTeamFolderRenameResponse)

class FilesTeamFolderRestoreArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderRestoreArg_validator = bv.Struct(FilesTeamFolderRestoreArg)

class FilesTeamFolderRestoreResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FilesTeamFolderRestoreResponse_validator = bv.Struct(FilesTeamFolderRestoreResponse)

class FolderCollageItemMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FolderCollageItemMetadata_validator = bv.Struct(FolderCollageItemMetadata)

class FolderData(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FolderData_validator = bv.Struct(FolderData)

class FolderMetadata(Metadata):
    pass
# WARNING: Decompyle incomplete

FolderMetadata_validator = bv.Struct(FolderMetadata)

class FolderOverviewMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FolderOverviewMetadata_validator = bv.Struct(FolderOverviewMetadata)

class FolderSharingInfo(SharingInfo):
    pass
# WARNING: Decompyle incomplete

FolderSharingInfo_validator = bv.Struct(FolderSharingInfo)

class FolderSort(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FolderSort_validator = bv.Struct(FolderSort)

class GetCopyReferenceArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetCopyReferenceArg_validator = bv.Struct(GetCopyReferenceArg)

class GetCopyReferenceError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetCopyReferenceError_validator = bv.Union(GetCopyReferenceError)

class GetCopyReferenceResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetCopyReferenceResult_validator = bv.Struct(GetCopyReferenceResult)

class GetFileContentMetadataArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileContentMetadataArg_validator = bv.Struct(GetFileContentMetadataArg)

class GetUploadInfoError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetUploadInfoError_validator = bv.Union(GetUploadInfoError)

class GetFileContentMetadataError(GetUploadInfoError):
    pass
# WARNING: Decompyle incomplete

GetFileContentMetadataError_validator = bv.Union(GetFileContentMetadataError)

class GetFileContentMetadataResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileContentMetadataResult_validator = bv.Struct(GetFileContentMetadataResult)

class GetFileContentsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileContentsArg_validator = bv.Struct(GetFileContentsArg)

class GetFileContentsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetFileContentsError_validator = bv.Union(GetFileContentsError)

class GetFileContentsResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileContentsResult_validator = bv.Struct(GetFileContentsResult)

class GetFileInfoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileInfoArg_validator = bv.Struct(GetFileInfoArg)

class GetFileInfoBatchError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetFileInfoBatchError_validator = bv.Union(GetFileInfoBatchError)

class GetFileInfoBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileInfoBatchResult_validator = bv.Struct(GetFileInfoBatchResult)

class GetFileInfoBatchV2Arg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileInfoBatchV2Arg_validator = bv.Struct(GetFileInfoBatchV2Arg)

class GetFileInfoError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetFileInfoError_validator = bv.Union(GetFileInfoError)

class GetFileInfoResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileInfoResult_validator = bv.Struct(GetFileInfoResult)

class GetHomeWidgetFilesArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetHomeWidgetFilesArg_validator = bv.Struct(GetHomeWidgetFilesArg)

class GetHomeWidgetFilesError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetHomeWidgetFilesError_validator = bv.Struct(GetHomeWidgetFilesError)

class GetHomeWidgetFilesResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetHomeWidgetFilesResult_validator = bv.Struct(GetHomeWidgetFilesResult)

class GetMetadataBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetMetadataBatchArg_validator = bv.Struct(GetMetadataBatchArg)

class GetMetadataBatchError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetMetadataBatchError_validator = bv.Union(GetMetadataBatchError)

class GetMetadataBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetMetadataBatchResult_validator = bv.Struct(GetMetadataBatchResult)

class GetQuerySuggestionsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetQuerySuggestionsArg_validator = bv.Struct(GetQuerySuggestionsArg)

class GetTagsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetTagsArg_validator = bv.Struct(GetTagsArg)

class GetTagsResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetTagsResult_validator = bv.Struct(GetTagsResult)

class GetTemporaryLinkArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetTemporaryLinkArg_validator = bv.Struct(GetTemporaryLinkArg)

class GetTemporaryLinkError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetTemporaryLinkError_validator = bv.Union(GetTemporaryLinkError)

class GetTemporaryLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetTemporaryLinkResult_validator = bv.Struct(GetTemporaryLinkResult)

class GetTemporaryUploadLinkArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetTemporaryUploadLinkArg_validator = bv.Struct(GetTemporaryUploadLinkArg)

class GetTemporaryUploadLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetTemporaryUploadLinkResult_validator = bv.Struct(GetTemporaryUploadLinkResult)

class GetThumbnailBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetThumbnailBatchArg_validator = bv.Struct(GetThumbnailBatchArg)

class GetThumbnailBatchError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetThumbnailBatchError_validator = bv.Union(GetThumbnailBatchError)

class GetThumbnailBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetThumbnailBatchResult_validator = bv.Struct(GetThumbnailBatchResult)

class GetThumbnailBatchResultData(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetThumbnailBatchResultData_validator = bv.Struct(GetThumbnailBatchResultData)

class GetThumbnailBatchResultEntry(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetThumbnailBatchResultEntry_validator = bv.Union(GetThumbnailBatchResultEntry)

class GetUploadInfoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetUploadInfoArg_validator = bv.Struct(GetUploadInfoArg)

class GetUploadInfoResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetUploadInfoResult_validator = bv.Struct(GetUploadInfoResult)

class GpsCoordinates(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GpsCoordinates_validator = bv.Struct(GpsCoordinates)

class HighlightSpan(bb.Struct):
    pass
# WARNING: Decompyle incomplete

HighlightSpan_validator = bv.Struct(HighlightSpan)

class HomeWidgetFileSource(bb.Union):
    pass
# WARNING: Decompyle incomplete

HomeWidgetFileSource_validator = bv.Union(HomeWidgetFileSource)

class HomeWidgetFilesErrorStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

HomeWidgetFilesErrorStatus_validator = bv.Union(HomeWidgetFilesErrorStatus)

class HomeWidgetFilesFilter(bb.Struct):
    pass
# WARNING: Decompyle incomplete

HomeWidgetFilesFilter_validator = bv.Struct(HomeWidgetFilesFilter)

class HomeWidgetItem(bb.Struct):
    pass
# WARNING: Decompyle incomplete

HomeWidgetItem_validator = bv.Struct(HomeWidgetItem)

class ImageSpecificMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ImageSpecificMetadata_validator = bv.Struct(ImageSpecificMetadata)

class ImportFormat(bb.Union):
    pass
# WARNING: Decompyle incomplete

ImportFormat_validator = bv.Union(ImportFormat)

class InternalFileOpBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InternalFileOpBatchResult_validator = bv.Struct(InternalFileOpBatchResult)

class InternalFileOpResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InternalFileOpResult_validator = bv.Struct(InternalFileOpResult)

class InternalMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InternalMetadata_validator = bv.Struct(InternalMetadata)

class InternalTreeViewFoldersArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InternalTreeViewFoldersArgs_validator = bv.Struct(InternalTreeViewFoldersArgs)

class InternalTreeViewFoldersEntry(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InternalTreeViewFoldersEntry_validator = bv.Struct(InternalTreeViewFoldersEntry)

class InternalTreeViewFoldersResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InternalTreeViewFoldersResult_validator = bv.Struct(InternalTreeViewFoldersResult)

class ListFolderArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFolderArg_validator = bv.Struct(ListFolderArg)

class ListFolderContinueArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFolderContinueArg_validator = bv.Struct(ListFolderContinueArg)

class ListFolderContinueError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListFolderContinueError_validator = bv.Union(ListFolderContinueError)

class ListFolderError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListFolderError_validator = bv.Union(ListFolderError)

class ListFolderGetLatestCursorResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFolderGetLatestCursorResult_validator = bv.Struct(ListFolderGetLatestCursorResult)

class ListFolderGetMountInfoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFolderGetMountInfoArg_validator = bv.Struct(ListFolderGetMountInfoArg)

class ListFolderGetMountInfoResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFolderGetMountInfoResult_validator = bv.Struct(ListFolderGetMountInfoResult)

class ListFolderLongpollArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFolderLongpollArg_validator = bv.Struct(ListFolderLongpollArg)

class ListFolderLongpollError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListFolderLongpollError_validator = bv.Union(ListFolderLongpollError)

class ListFolderLongpollResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFolderLongpollResult_validator = bv.Struct(ListFolderLongpollResult)

class ListFolderResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListFolderResult_validator = bv.Struct(ListFolderResult)

class ListRevisionsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListRevisionsArg_validator = bv.Struct(ListRevisionsArg)

class ListRevisionsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListRevisionsError_validator = bv.Union(ListRevisionsError)

class ListRevisionsMode(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListRevisionsMode_validator = bv.Union(ListRevisionsMode)

class ListRevisionsResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListRevisionsResult_validator = bv.Struct(ListRevisionsResult)

class ListSubfoldersArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListSubfoldersArg_validator = bv.Struct(ListSubfoldersArg)

class ListSubfoldersError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListSubfoldersError_validator = bv.Union(ListSubfoldersError)

class ListSubfoldersResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListSubfoldersResult_validator = bv.Struct(ListSubfoldersResult)

class ListWidgetsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListWidgetsArg_validator = bv.Struct(ListWidgetsArg)

class ListWidgetsError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListWidgetsError_validator = bv.Struct(ListWidgetsError)

class ListWidgetsResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListWidgetsResult_validator = bv.Struct(ListWidgetsResult)

class LockConflictError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LockConflictError_validator = bv.Struct(LockConflictError)

class LockFileArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LockFileArg_validator = bv.Struct(LockFileArg)

class LockFileBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LockFileBatchArg_validator = bv.Struct(LockFileBatchArg)

class LockFileBatchResult(FileOpsResult):
    pass
# WARNING: Decompyle incomplete

LockFileBatchResult_validator = bv.Struct(LockFileBatchResult)

class LockFileError(bb.Union):
    pass
# WARNING: Decompyle incomplete

LockFileError_validator = bv.Union(LockFileError)

class LockFileResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LockFileResult_validator = bv.Struct(LockFileResult)

class LockFileResultEntry(bb.Union):
    pass
# WARNING: Decompyle incomplete

LockFileResultEntry_validator = bv.Union(LockFileResultEntry)

class LockedFilesSearchListArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LockedFilesSearchListArg_validator = bv.Struct(LockedFilesSearchListArg)

class LockedFilesSearchListContinueArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LockedFilesSearchListContinueArg_validator = bv.Struct(LockedFilesSearchListContinueArg)

class LockedFilesSearchListContinueError(bb.Union):
    pass
# WARNING: Decompyle incomplete

LockedFilesSearchListContinueError_validator = bv.Union(LockedFilesSearchListContinueError)

class LockedFilesSearchListResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LockedFilesSearchListResult_validator = bv.Struct(LockedFilesSearchListResult)

class LookupError(bb.Union):
    pass
# WARNING: Decompyle incomplete

LookupError_validator = bv.Union(LookupError)

class MediaFilters(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MediaFilters_validator = bv.Struct(MediaFilters)

class MediaInfo(bb.Union):
    pass
# WARNING: Decompyle incomplete

MediaInfo_validator = bv.Union(MediaInfo)

class MediaMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MediaMetadata_validator = bv.StructTree(MediaMetadata)

class MediaTranscodeArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MediaTranscodeArg_validator = bv.Struct(MediaTranscodeArg)

class MediaTranscodeError(bb.Union):
    pass
# WARNING: Decompyle incomplete

MediaTranscodeError_validator = bv.Union(MediaTranscodeError)

class MediaTranscodeResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MediaTranscodeResult_validator = bv.Struct(MediaTranscodeResult)

class MetadataV2(bb.Union):
    pass
# WARNING: Decompyle incomplete

MetadataV2_validator = bv.Union(MetadataV2)

class MinimalFileLinkMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MinimalFileLinkMetadata_validator = bv.Struct(MinimalFileLinkMetadata)

class ModifierAccountInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ModifierAccountInfo_validator = bv.Struct(ModifierAccountInfo)

class Mount(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Mount_validator = bv.Struct(Mount)

class RelocationBatchArgBase(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RelocationBatchArgBase_validator = bv.Struct(RelocationBatchArgBase)

class MoveBatchArg(RelocationBatchArgBase):
    pass
# WARNING: Decompyle incomplete

MoveBatchArg_validator = bv.Struct(MoveBatchArg)

class MoveIntoFamilyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

MoveIntoFamilyError_validator = bv.Union(MoveIntoFamilyError)

class MoveIntoVaultError(bb.Union):
    pass
# WARNING: Decompyle incomplete

MoveIntoVaultError_validator = bv.Union(MoveIntoVaultError)

class NsidInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

NsidInfo_validator = bv.Struct(NsidInfo)

class ObjectInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ObjectInfo_validator = bv.Struct(ObjectInfo)

class OfficeFileType(bb.Union):
    pass
# WARNING: Decompyle incomplete

OfficeFileType_validator = bv.Union(OfficeFileType)

class OfficeSpecificMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

OfficeSpecificMetadata_validator = bv.Struct(OfficeSpecificMetadata)

class OldPathInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

OldPathInfo_validator = bv.Struct(OldPathInfo)

class OldPathInfoCypress(bb.Struct):
    pass
# WARNING: Decompyle incomplete

OldPathInfoCypress_validator = bv.Struct(OldPathInfoCypress)

class OtherFileMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

OtherFileMetadata_validator = bv.Struct(OtherFileMetadata)

class OutputFormat(bb.Union):
    pass
# WARNING: Decompyle incomplete

OutputFormat_validator = bv.Union(OutputFormat)

class PaperContentError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PaperContentError_validator = bv.Union(PaperContentError)

class PaperCreateArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PaperCreateArg_validator = bv.Struct(PaperCreateArg)

class PaperCreateError(PaperContentError):
    pass
# WARNING: Decompyle incomplete

PaperCreateError_validator = bv.Union(PaperCreateError)

class PaperCreateResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PaperCreateResult_validator = bv.Struct(PaperCreateResult)

class PaperDocUpdatePolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

PaperDocUpdatePolicy_validator = bv.Union(PaperDocUpdatePolicy)

class PaperMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PaperMetadata_validator = bv.Struct(PaperMetadata)

class PaperUpdateArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PaperUpdateArg_validator = bv.Struct(PaperUpdateArg)

class PaperUpdateError(PaperContentError):
    pass
# WARNING: Decompyle incomplete

PaperUpdateError_validator = bv.Union(PaperUpdateError)

class PaperUpdateResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PaperUpdateResult_validator = bv.Struct(PaperUpdateResult)

class PathOrLink(bb.Union):
    pass
# WARNING: Decompyle incomplete

PathOrLink_validator = bv.Union(PathOrLink)

class PathToTags(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PathToTags_validator = bv.Struct(PathToTags)

class PdfSpecificMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PdfSpecificMetadata_validator = bv.Struct(PdfSpecificMetadata)

class PhotoMetadata(MediaMetadata):
    pass
# WARNING: Decompyle incomplete

PhotoMetadata_validator = bv.Struct(PhotoMetadata)

class PreviewArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PreviewArg_validator = bv.Struct(PreviewArg)

class PreviewArgV2(PreviewArg):
    pass
# WARNING: Decompyle incomplete

PreviewArgV2_validator = bv.Struct(PreviewArgV2)

class PreviewArgV3(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PreviewArgV3_validator = bv.Struct(PreviewArgV3)

class PreviewError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PreviewError_validator = bv.Union(PreviewError)

class PreviewErrorV2(bb.Union):
    pass
# WARNING: Decompyle incomplete

PreviewErrorV2_validator = bv.Union(PreviewErrorV2)

class PreviewErrorV3(PreviewErrorV2):
    pass
# WARNING: Decompyle incomplete

PreviewErrorV3_validator = bv.Union(PreviewErrorV3)

class PreviewInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PreviewInfo_validator = bv.Struct(PreviewInfo)

class PreviewResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PreviewResult_validator = bv.Struct(PreviewResult)

class PreviewType(bb.Union):
    pass
# WARNING: Decompyle incomplete

PreviewType_validator = bv.Union(PreviewType)

class PreviewableExtensionsResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PreviewableExtensionsResult_validator = bv.Struct(PreviewableExtensionsResult)

class ProcessType(bb.Union):
    pass
# WARNING: Decompyle incomplete

ProcessType_validator = bv.Union(ProcessType)

class QueryForFields(bb.Struct):
    pass
# WARNING: Decompyle incomplete

QueryForFields_validator = bv.Struct(QueryForFields)

class QueryIntent(bb.Union):
    pass
# WARNING: Decompyle incomplete

QueryIntent_validator = bv.Union(QueryIntent)

class QuerySuggestion(bb.Struct):
    pass
# WARNING: Decompyle incomplete

QuerySuggestion_validator = bv.Struct(QuerySuggestion)

class QuerySuggestionsResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

QuerySuggestionsResult_validator = bv.Struct(QuerySuggestionsResult)

class RecentEventType(bb.Union):
    pass
# WARNING: Decompyle incomplete

RecentEventType_validator = bv.Union(RecentEventType)

class RecentsErrorStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

RecentsErrorStatus_validator = bv.Union(RecentsErrorStatus)

class RecentsInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RecentsInfo_validator = bv.Struct(RecentsInfo)

class RecentsV2Arg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RecentsV2Arg_validator = bv.Struct(RecentsV2Arg)

class RecentsV2Error(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RecentsV2Error_validator = bv.Struct(RecentsV2Error)

class RecentsV2LegacyPaperInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RecentsV2LegacyPaperInfo_validator = bv.Struct(RecentsV2LegacyPaperInfo)

class RecentsV2Result(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RecentsV2Result_validator = bv.Struct(RecentsV2Result)

class RelocationPath(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RelocationPath_validator = bv.Struct(RelocationPath)

class RelocationArg(RelocationPath):
    pass
# WARNING: Decompyle incomplete

RelocationArg_validator = bv.Struct(RelocationArg)

class RelocationBatchArg(RelocationBatchArgBase):
    pass
# WARNING: Decompyle incomplete

RelocationBatchArg_validator = bv.Struct(RelocationBatchArg)

class RelocationError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RelocationError_validator = bv.Union(RelocationError)

class RelocationBatchError(RelocationError):
    pass
# WARNING: Decompyle incomplete

RelocationBatchError_validator = bv.Union(RelocationBatchError)

class RelocationBatchErrorEntry(bb.Union):
    pass
# WARNING: Decompyle incomplete

RelocationBatchErrorEntry_validator = bv.Union(RelocationBatchErrorEntry)

class RelocationBatchJobStatus(async_.PollResultBase):
    pass
# WARNING: Decompyle incomplete

RelocationBatchJobStatus_validator = bv.Union(RelocationBatchJobStatus)

class RelocationBatchLaunch(async_.LaunchResultBase):
    pass
# WARNING: Decompyle incomplete

RelocationBatchLaunch_validator = bv.Union(RelocationBatchLaunch)

class RelocationBatchResult(FileOpsResult):
    pass
# WARNING: Decompyle incomplete

RelocationBatchResult_validator = bv.Struct(RelocationBatchResult)

class RelocationBatchResultData(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RelocationBatchResultData_validator = bv.Struct(RelocationBatchResultData)

class RelocationBatchResultEntry(bb.Union):
    pass
# WARNING: Decompyle incomplete

RelocationBatchResultEntry_validator = bv.Union(RelocationBatchResultEntry)

class RelocationBatchV2JobStatus(async_.PollResultBase):
    pass
# WARNING: Decompyle incomplete

RelocationBatchV2JobStatus_validator = bv.Union(RelocationBatchV2JobStatus)

class RelocationBatchV2Launch(async_.LaunchResultBase):
    pass
# WARNING: Decompyle incomplete

RelocationBatchV2Launch_validator = bv.Union(RelocationBatchV2Launch)

class RelocationBatchV2Result(FileOpsResult):
    pass
# WARNING: Decompyle incomplete

RelocationBatchV2Result_validator = bv.Struct(RelocationBatchV2Result)

class RelocationResult(FileOpsResult):
    pass
# WARNING: Decompyle incomplete

RelocationResult_validator = bv.Struct(RelocationResult)

class RemoveTagArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RemoveTagArg_validator = bv.Struct(RemoveTagArg)

class RemoveTagError(BaseTagError):
    pass
# WARNING: Decompyle incomplete

RemoveTagError_validator = bv.Union(RemoveTagError)

class RestoreArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RestoreArg_validator = bv.Struct(RestoreArg)

class RestoreError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RestoreError_validator = bv.Union(RestoreError)

class RestorePathBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RestorePathBatchArg_validator = bv.Struct(RestorePathBatchArg)

class RestorePathBatchError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RestorePathBatchError_validator = bv.Union(RestorePathBatchError)

class RestorePathBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RestorePathBatchResult_validator = bv.Struct(RestorePathBatchResult)

class ResultAnnotation(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ResultAnnotation_validator = bv.Struct(ResultAnnotation)

class RootOidInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RootOidInfo_validator = bv.Struct(RootOidInfo)

class SaveCopyReferenceArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SaveCopyReferenceArg_validator = bv.Struct(SaveCopyReferenceArg)

class SaveCopyReferenceError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SaveCopyReferenceError_validator = bv.Union(SaveCopyReferenceError)

class SaveCopyReferenceResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SaveCopyReferenceResult_validator = bv.Struct(SaveCopyReferenceResult)

class SaveUrlArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SaveUrlArg_validator = bv.Struct(SaveUrlArg)

class SaveUrlError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SaveUrlError_validator = bv.Union(SaveUrlError)

class SaveUrlJobStatus(async_.PollResultBase):
    pass
# WARNING: Decompyle incomplete

SaveUrlJobStatus_validator = bv.Union(SaveUrlJobStatus)

class SaveUrlResult(async_.LaunchResultBase):
    pass
# WARNING: Decompyle incomplete

SaveUrlResult_validator = bv.Union(SaveUrlResult)

class ScrubbingItemMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ScrubbingItemMetadata_validator = bv.Struct(ScrubbingItemMetadata)

class SearchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SearchArg_validator = bv.Struct(SearchArg)

class SearchError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SearchError_validator = bv.Union(SearchError)

class SearchFields(bb.Union):
    pass
# WARNING: Decompyle incomplete

SearchFields_validator = bv.Union(SearchFields)

class SearchMatch(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SearchMatch_validator = bv.Struct(SearchMatch)

class SearchMatchFieldOptions(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SearchMatchFieldOptions_validator = bv.Struct(SearchMatchFieldOptions)

class SearchMatchType(bb.Union):
    pass
# WARNING: Decompyle incomplete

SearchMatchType_validator = bv.Union(SearchMatchType)

class SearchMatchTypeV2(bb.Union):
    pass
# WARNING: Decompyle incomplete

SearchMatchTypeV2_validator = bv.Union(SearchMatchTypeV2)

class SearchMatchV2(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SearchMatchV2_validator = bv.Struct(SearchMatchV2)

class SearchMode(bb.Union):
    pass
# WARNING: Decompyle incomplete

SearchMode_validator = bv.Union(SearchMode)

class SearchOptions(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SearchOptions_validator = bv.Struct(SearchOptions)

class SearchOrderBy(bb.Union):
    pass
# WARNING: Decompyle incomplete

SearchOrderBy_validator = bv.Union(SearchOrderBy)

class SearchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SearchResult_validator = bv.Struct(SearchResult)

class SearchV2Arg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SearchV2Arg_validator = bv.Struct(SearchV2Arg)

class SearchV2ContinueArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SearchV2ContinueArg_validator = bv.Struct(SearchV2ContinueArg)

class SearchV2Result(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SearchV2Result_validator = bv.Struct(SearchV2Result)

class SetUserSortPreferenceArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SetUserSortPreferenceArg_validator = bv.Struct(SetUserSortPreferenceArg)

class SetUserSortPreferenceError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SetUserSortPreferenceError_validator = bv.Struct(SetUserSortPreferenceError)

class SetUserSortPreferenceResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SetUserSortPreferenceResponse_validator = bv.Struct(SetUserSortPreferenceResponse)

class SharedLink(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedLink_validator = bv.Struct(SharedLink)

class SharedLinkFileInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedLinkFileInfo_validator = bv.Struct(SharedLinkFileInfo)

class SharedWithMeFileMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedWithMeFileMetadata_validator = bv.Struct(SharedWithMeFileMetadata)

class SharingInviteInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharingInviteInfo_validator = bv.Struct(SharingInviteInfo)

class SignedBoltChannelState(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SignedBoltChannelState_validator = bv.Struct(SignedBoltChannelState)

class SingleUserLock(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SingleUserLock_validator = bv.Struct(SingleUserLock)

class Snippet(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Snippet_validator = bv.Struct(Snippet)

class SortSource(bb.Union):
    pass
# WARNING: Decompyle incomplete

SortSource_validator = bv.Union(SortSource)

class SortType(bb.Union):
    pass
# WARNING: Decompyle incomplete

SortType_validator = bv.Union(SortType)

class SpellCorrection(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SpellCorrection_validator = bv.Struct(SpellCorrection)

class StarredStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

StarredStatus_validator = bv.Union(StarredStatus)

class StarredV2Arg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StarredV2Arg_validator = bv.Struct(StarredV2Arg)

class StarredV2Error(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StarredV2Error_validator = bv.Struct(StarredV2Error)

class StarredV2ErrorStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

StarredV2ErrorStatus_validator = bv.Union(StarredV2ErrorStatus)

class StarredV2Result(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StarredV2Result_validator = bv.Struct(StarredV2Result)

class SubfolderFilter(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SubfolderFilter_validator = bv.Struct(SubfolderFilter)

class SuggestedTag(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SuggestedTag_validator = bv.Struct(SuggestedTag)

class SymlinkInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SymlinkInfo_validator = bv.Struct(SymlinkInfo)

class SyncSetting(bb.Union):
    pass
# WARNING: Decompyle incomplete

SyncSetting_validator = bv.Union(SyncSetting)

class SyncSettingArg(bb.Union):
    pass
# WARNING: Decompyle incomplete

SyncSettingArg_validator = bv.Union(SyncSettingArg)

class SyncSettingsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SyncSettingsError_validator = bv.Union(SyncSettingsError)

class Tag(bb.Union):
    pass
# WARNING: Decompyle incomplete

Tag_validator = bv.Union(Tag)

class TeamFolderJsInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TeamFolderJsInfo_validator = bv.Struct(TeamFolderJsInfo)

class TeamFolderJsInfoCypress(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TeamFolderJsInfoCypress_validator = bv.Struct(TeamFolderJsInfoCypress)

class TeamFolderStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

TeamFolderStatus_validator = bv.Union(TeamFolderStatus)

class ThumbnailArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ThumbnailArg_validator = bv.Struct(ThumbnailArg)

class ThumbnailBatchLinkArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ThumbnailBatchLinkArg_validator = bv.Struct(ThumbnailBatchLinkArg)

class ThumbnailBatchLinkError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ThumbnailBatchLinkError_validator = bv.Union(ThumbnailBatchLinkError)

class ThumbnailBatchLinkResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ThumbnailBatchLinkResult_validator = bv.Struct(ThumbnailBatchLinkResult)

class ThumbnailBatchLinkResultData(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ThumbnailBatchLinkResultData_validator = bv.Struct(ThumbnailBatchLinkResultData)

class ThumbnailBatchLinkResultEntry(bb.Union):
    pass
# WARNING: Decompyle incomplete

ThumbnailBatchLinkResultEntry_validator = bv.Union(ThumbnailBatchLinkResultEntry)

class ThumbnailBatchLinkUnit(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ThumbnailBatchLinkUnit_validator = bv.Struct(ThumbnailBatchLinkUnit)

class ThumbnailError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ThumbnailError_validator = bv.Union(ThumbnailError)

class ThumbnailFormat(bb.Union):
    pass
# WARNING: Decompyle incomplete

ThumbnailFormat_validator = bv.Union(ThumbnailFormat)

class ThumbnailMode(bb.Union):
    pass
# WARNING: Decompyle incomplete

ThumbnailMode_validator = bv.Union(ThumbnailMode)

class ThumbnailQuality(bb.Union):
    pass
# WARNING: Decompyle incomplete

ThumbnailQuality_validator = bv.Union(ThumbnailQuality)

class ThumbnailSize(bb.Union):
    pass
# WARNING: Decompyle incomplete

ThumbnailSize_validator = bv.Union(ThumbnailSize)

class ThumbnailV2Arg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ThumbnailV2Arg_validator = bv.Struct(ThumbnailV2Arg)

class ThumbnailV2Error(bb.Union):
    pass
# WARNING: Decompyle incomplete

ThumbnailV2Error_validator = bv.Union(ThumbnailV2Error)

class UndoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UndoArg_validator = bv.Struct(UndoArg)

class UndoError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UndoError_validator = bv.Union(UndoError)

class UndoResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UndoResult_validator = bv.Struct(UndoResult)

class UnlockFileArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UnlockFileArg_validator = bv.Struct(UnlockFileArg)

class UnlockFileBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UnlockFileBatchArg_validator = bv.Struct(UnlockFileBatchArg)

class UnprocessedFileContentHashMismatchError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UnprocessedFileContentHashMismatchError_validator = bv.Struct(UnprocessedFileContentHashMismatchError)

class UpdateDefaultSectionArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateDefaultSectionArg_validator = bv.Struct(UpdateDefaultSectionArg)

class UpdateDefaultSectionError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateDefaultSectionError_validator = bv.Struct(UpdateDefaultSectionError)

class UpdateDefaultSectionErrorStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

UpdateDefaultSectionErrorStatus_validator = bv.Union(UpdateDefaultSectionErrorStatus)

class UpdateDefaultSectionResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateDefaultSectionResult_validator = bv.Struct(UpdateDefaultSectionResult)

class UpdateWidgetErrorStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

UpdateWidgetErrorStatus_validator = bv.Union(UpdateWidgetErrorStatus)

class UpdateWidgetsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateWidgetsArg_validator = bv.Struct(UpdateWidgetsArg)

class UpdateWidgetsError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateWidgetsError_validator = bv.Struct(UpdateWidgetsError)

class UpdateWidgetsResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateWidgetsResult_validator = bv.Struct(UpdateWidgetsResult)

class UploadArg(CommitInfo):
    pass
# WARNING: Decompyle incomplete

UploadArg_validator = bv.Struct(UploadArg)

class UploadError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UploadError_validator = bv.Union(UploadError)

class UploadResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UploadResult_validator = bv.Struct(UploadResult)

class UploadSessionAppendArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UploadSessionAppendArg_validator = bv.Struct(UploadSessionAppendArg)

class UploadSessionAppendBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UploadSessionAppendBatchArg_validator = bv.Struct(UploadSessionAppendBatchArg)

class UploadSessionAppendBatchArgEntry(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UploadSessionAppendBatchArgEntry_validator = bv.Struct(UploadSessionAppendBatchArgEntry)

class UploadSessionAppendBatchEntryError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UploadSessionAppendBatchEntryError_validator = bv.Union(UploadSessionAppendBatchEntryError)

class UploadSessionAppendBatchError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UploadSessionAppendBatchError_validator = bv.Union(UploadSessionAppendBatchError)

class UploadSessionAppendBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UploadSessionAppendBatchResult_validator = bv.Struct(UploadSessionAppendBatchResult)

class UploadSessionAppendBatchResultEntry(bb.Union):
    pass
# WARNING: Decompyle incomplete

UploadSessionAppendBatchResultEntry_validator = bv.Union(UploadSessionAppendBatchResultEntry)

class UploadSessionAppendError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UploadSessionAppendError_validator = bv.Union(UploadSessionAppendError)

class UploadSessionCursor(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UploadSessionCursor_validator = bv.Struct(UploadSessionCursor)

class UploadSessionFinishArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UploadSessionFinishArg_validator = bv.Struct(UploadSessionFinishArg)

class UploadSessionFinishBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UploadSessionFinishBatchArg_validator = bv.Struct(UploadSessionFinishBatchArg)

class UploadSessionFinishBatchJobStatus(async_.PollResultBase):
    pass
# WARNING: Decompyle incomplete

UploadSessionFinishBatchJobStatus_validator = bv.Union(UploadSessionFinishBatchJobStatus)

class UploadSessionFinishBatchLaunch(async_.LaunchResultBase):
    pass
# WARNING: Decompyle incomplete

UploadSessionFinishBatchLaunch_validator = bv.Union(UploadSessionFinishBatchLaunch)

class UploadSessionFinishBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UploadSessionFinishBatchResult_validator = bv.Struct(UploadSessionFinishBatchResult)

class UploadSessionFinishBatchResultEntry(bb.Union):
    pass
# WARNING: Decompyle incomplete

UploadSessionFinishBatchResultEntry_validator = bv.Union(UploadSessionFinishBatchResultEntry)

class UploadSessionFinishEncryptionError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UploadSessionFinishEncryptionError_validator = bv.Union(UploadSessionFinishEncryptionError)

class UploadSessionFinishError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UploadSessionFinishError_validator = bv.Union(UploadSessionFinishError)

class UploadSessionFinishProcessedArg(UploadSessionFinishArg):
    pass
# WARNING: Decompyle incomplete

UploadSessionFinishProcessedArg_validator = bv.Struct(UploadSessionFinishProcessedArg)

class UploadSessionFinishProcessedError(UploadSessionFinishError):
    pass
# WARNING: Decompyle incomplete

UploadSessionFinishProcessedError_validator = bv.Union(UploadSessionFinishProcessedError)

class UploadSessionFinishProcessedJobStatus(async_.PollResultBase):
    pass
# WARNING: Decompyle incomplete

UploadSessionFinishProcessedJobStatus_validator = bv.Union(UploadSessionFinishProcessedJobStatus)

class UploadSessionFinishProcessedLaunch(async_.LaunchResultBase):
    pass
# WARNING: Decompyle incomplete

UploadSessionFinishProcessedLaunch_validator = bv.Union(UploadSessionFinishProcessedLaunch)

class UploadSessionFinishProcessedResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

UploadSessionFinishProcessedResult_validator = bv.Union(UploadSessionFinishProcessedResult)

class UploadSessionLookupError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UploadSessionLookupError_validator = bv.Union(UploadSessionLookupError)

class UploadSessionOffsetError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UploadSessionOffsetError_validator = bv.Struct(UploadSessionOffsetError)

class UploadSessionStartArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UploadSessionStartArg_validator = bv.Struct(UploadSessionStartArg)

class UploadSessionStartBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UploadSessionStartBatchArg_validator = bv.Struct(UploadSessionStartBatchArg)

class UploadSessionStartBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UploadSessionStartBatchResult_validator = bv.Struct(UploadSessionStartBatchResult)

class UploadSessionStartError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UploadSessionStartError_validator = bv.Union(UploadSessionStartError)

class UploadSessionStartResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UploadSessionStartResult_validator = bv.Struct(UploadSessionStartResult)

class UploadSessionType(bb.Union):
    pass
# WARNING: Decompyle incomplete

UploadSessionType_validator = bv.Union(UploadSessionType)

class UploadV2Arg(CommitInfo):
    pass
# WARNING: Decompyle incomplete

UploadV2Arg_validator = bv.Struct(UploadV2Arg)

class UploadWriteFailed(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UploadWriteFailed_validator = bv.Struct(UploadWriteFailed)

class UserGeneratedTag(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UserGeneratedTag_validator = bv.Struct(UserGeneratedTag)

class ValidateUploadArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ValidateUploadArg_validator = bv.Struct(ValidateUploadArg)

class ValidateUploadError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ValidateUploadError_validator = bv.Union(ValidateUploadError)

class ValidateUploadResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ValidateUploadResult_validator = bv.Struct(ValidateUploadResult)

class VideoMetadata(MediaMetadata):
    pass
# WARNING: Decompyle incomplete

VideoMetadata_validator = bv.Struct(VideoMetadata)

class VideoSpecificMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

VideoSpecificMetadata_validator = bv.Struct(VideoSpecificMetadata)

class WriteConflictError(bb.Union):
    pass
# WARNING: Decompyle incomplete

WriteConflictError_validator = bv.Union(WriteConflictError)

class WriteError(bb.Union):
    pass
# WARNING: Decompyle incomplete

WriteError_validator = bv.Union(WriteError)

class WriteMode(bb.Union):
    pass
# WARNING: Decompyle incomplete

WriteMode_validator = bv.Union(WriteMode)

class HomeItemUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

HomeItemUnion_validator = bv.Union(HomeItemUnion)

class ItemUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

ItemUnion_validator = bv.Union(ItemUnion)

class MetadataUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

MetadataUnion_validator = bv.Union(MetadataUnion)
CopyBatchArg_validator = RelocationBatchArgBase_validator
CopyBatchArg = RelocationBatchArgBase
FileId_validator = bv.String(min_length = 4, pattern = 'id:.+')
FileId_validator._redact = bv.BlotRedactor(None)
Id_validator = bv.String(min_length = 1)
ListFolderCursor_validator = bv.String(min_length = 1)
ListFolderCursor_validator._redact = bv.BlotRedactor(None)
MalformedPathError_validator = bv.Nullable(bv.String())
Path_validator = bv.String(pattern = '/(.|[\\r\\n])*')
Path_validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
PathOrId_validator = bv.String(pattern = '/(.|[\\r\\n])*|id:.*|(ns:[0-9]+(/(.|[\\r\\n])*)?)')
PathOrId_validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
PathR_validator = bv.String(pattern = '(/(.|[\\r\\n])*)?|(ns:[0-9]+(/(.|[\\r\\n])*)?)')
PathR_validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
PathROrId_validator = bv.String(pattern = '(/(.|[\\r\\n])*)?|id:.*|(ns:[0-9]+(/(.|[\\r\\n])*)?)')
PathROrId_validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
ReadPath_validator = bv.String(pattern = '(/(.|[\\r\\n])*|id:.*)|(rev:[0-9a-f]{9,})|(ns:[0-9]+(/(.|[\\r\\n])*)?)')
ReadPath_validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
RestorePath_validator = bv.String(pattern = '(/(.|[\\r\\n])*)|(ns:[0-9]+(/.*)?)')
RestorePath_validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
Rev_validator = bv.String(min_length = 9, pattern = '[0-9a-f]+')
SearchV2Cursor_validator = bv.String(min_length = 1)
SearchV2Cursor_validator._redact = bv.BlotRedactor(None)
Sha256HexHash_validator = bv.String(min_length = 64, max_length = 64)
SharedLinkUrl_validator = bv.String()
SharedLinkUrl_validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
TagText_validator = bv.String(min_length = 1, max_length = 32, pattern = '[\\w]+')
TagText_validator._redact = bv.BlotRedactor(None)
WritePath_validator = bv.String(pattern = '(/(.|[\\r\\n])*)|(ns:[0-9]+(/(.|[\\r\\n])*)?)')
WritePath_validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
WritePathOrId_validator = bv.String(pattern = '(/(.|[\\r\\n])*)|(ns:[0-9]+(/(.|[\\r\\n])*)?)|(id:.*)')
WritePathOrId_validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
AddTagArg.path.validator = Path_validator
AddTagArg.tag_text.validator = TagText_validator
AddTagArg._all_field_names_ = set([
    'path',
    'tag_text'])
AddTagArg._all_fields_ = [
    ('path', AddTagArg.path.validator),
    ('tag_text', AddTagArg.tag_text.validator)]
BaseTagError._path_validator = LookupError_validator
BaseTagError._other_validator = bv.Void()
BaseTagError._tagmap = {
    'path': BaseTagError._path_validator,
    'other': BaseTagError._other_validator }
BaseTagError.other = BaseTagError('other')
AddTagError._too_many_tags_validator = bv.Void()
AddTagError._tagmap = {
    'too_many_tags': AddTagError._too_many_tags_validator }
AddTagError._tagmap.update(BaseTagError._tagmap)
AddTagError.too_many_tags = AddTagError('too_many_tags')
GetMetadataArg.path.validator = ReadPath_validator
GetMetadataArg.include_media_info.validator = bv.Boolean()
GetMetadataArg.include_media_info.validator._redact = bv.BlotRedactor(None)
GetMetadataArg.include_deleted.validator = bv.Boolean()
GetMetadataArg.include_deleted.validator._redact = bv.BlotRedactor(None)
GetMetadataArg.include_has_explicit_shared_members.validator = bv.Boolean()
GetMetadataArg.include_has_explicit_shared_members.validator._redact = bv.BlotRedactor(None)
GetMetadataArg.include_property_groups.validator = bv.Nullable(file_properties.TemplateFilterBase_validator)
GetMetadataArg.include_folder_overview_metadata.validator = bv.Boolean()
GetMetadataArg.include_folder_overview_metadata.validator._redact = bv.BlotRedactor(None)
GetMetadataArg.include_preview_url_for_files.validator = bv.Boolean()
GetMetadataArg.include_preview_url_for_files.validator._redact = bv.BlotRedactor(None)
GetMetadataArg._all_field_names_ = set([
    'path',
    'include_media_info',
    'include_deleted',
    'include_has_explicit_shared_members',
    'include_property_groups'])
GetMetadataArg._all_fields_ = [
    ('path', GetMetadataArg.path.validator),
    ('include_media_info', GetMetadataArg.include_media_info.validator),
    ('include_deleted', GetMetadataArg.include_deleted.validator),
    ('include_has_explicit_shared_members', GetMetadataArg.include_has_explicit_shared_members.validator),
    ('include_property_groups', GetMetadataArg.include_property_groups.validator)]
GetMetadataArg._all_internal_field_names_ = set([
    'include_folder_overview_metadata',
    'include_preview_url_for_files'])
GetMetadataArg._all_internal_fields_ = [
    ('include_folder_overview_metadata', GetMetadataArg.include_folder_overview_metadata.validator),
    ('include_preview_url_for_files', GetMetadataArg.include_preview_url_for_files.validator)]
AlphaGetMetadataArg.include_property_templates.validator = bv.Nullable(bv.List(file_properties.TemplateId_validator))
AlphaGetMetadataArg._all_field_names_ = GetMetadataArg._all_field_names_.union(set([
    'include_property_templates']))
AlphaGetMetadataArg._all_fields_ = GetMetadataArg._all_fields_ + [
    ('include_property_templates', AlphaGetMetadataArg.include_property_templates.validator)]
AlphaGetMetadataArg._all_internal_field_names_ = GetMetadataArg._all_internal_field_names_.union(set([]))
AlphaGetMetadataArg._all_internal_fields_ = GetMetadataArg._all_internal_fields_ + []
GetMetadataError._path_validator = LookupError_validator
GetMetadataError._tagmap = {
    'path': GetMetadataError._path_validator }
AlphaGetMetadataError._properties_error_validator = file_properties.LookUpPropertiesError_validator
AlphaGetMetadataError._tagmap = {
    'properties_error': AlphaGetMetadataError._properties_error_validator }
AlphaGetMetadataError._tagmap.update(GetMetadataError._tagmap)
ApiFileIdMode._file_obj_id_validator = bv.Void()
ApiFileIdMode._file_id_validator = bv.Void()
ApiFileIdMode._other_validator = bv.Void()
ApiFileIdMode._tagmap = {
    'file_obj_id': ApiFileIdMode._file_obj_id_validator,
    'file_id': ApiFileIdMode._file_id_validator,
    'other': ApiFileIdMode._other_validator }
ApiFileIdMode.file_obj_id = ApiFileIdMode('file_obj_id')
ApiFileIdMode.file_id = ApiFileIdMode('file_id')
ApiFileIdMode.other = ApiFileIdMode('other')
AsyncJobResult._not_found_validator = bv.Void()
AsyncJobResult._in_progress_validator = bv.Void()
AsyncJobResult._complete_validator = bv.Void()
AsyncJobResult._failed_validator = bv.Void()
AsyncJobResult._other_validator = bv.Void()
AsyncJobResult._tagmap = {
    'not_found': AsyncJobResult._not_found_validator,
    'in_progress': AsyncJobResult._in_progress_validator,
    'complete': AsyncJobResult._complete_validator,
    'failed': AsyncJobResult._failed_validator,
    'other': AsyncJobResult._other_validator }
AsyncJobResult.not_found = AsyncJobResult('not_found')
AsyncJobResult.in_progress = AsyncJobResult('in_progress')
AsyncJobResult.complete = AsyncJobResult('complete')
AsyncJobResult.failed = AsyncJobResult('failed')
AsyncJobResult.other = AsyncJobResult('other')
AudioSpecificMetadata.duration.validator = bv.Nullable(bv.Int64())
AudioSpecificMetadata.codec.validator = bv.Nullable(bv.String())
AudioSpecificMetadata.channels.validator = bv.Nullable(bv.Int32())
AudioSpecificMetadata.channel_layout.validator = bv.Nullable(bv.String())
AudioSpecificMetadata.sampling_rate.validator = bv.Nullable(bv.Int32())
AudioSpecificMetadata.bit_rate.validator = bv.Nullable(bv.Int32())
AudioSpecificMetadata.bits_per_sample.validator = bv.Nullable(bv.Int32())
AudioSpecificMetadata.device.validator = bv.Nullable(bv.String())
AudioSpecificMetadata.duration_precise.validator = bv.Nullable(bv.Float32())
AudioSpecificMetadata.file_type_extension.validator = bv.Nullable(bv.String())
AudioSpecificMetadata._all_field_names_ = set([
    'duration',
    'codec',
    'channels',
    'channel_layout',
    'sampling_rate',
    'bit_rate',
    'bits_per_sample',
    'device',
    'duration_precise',
    'file_type_extension'])
AudioSpecificMetadata._all_fields_ = [
    ('duration', AudioSpecificMetadata.duration.validator),
    ('codec', AudioSpecificMetadata.codec.validator),
    ('channels', AudioSpecificMetadata.channels.validator),
    ('channel_layout', AudioSpecificMetadata.channel_layout.validator),
    ('sampling_rate', AudioSpecificMetadata.sampling_rate.validator),
    ('bit_rate', AudioSpecificMetadata.bit_rate.validator),
    ('bits_per_sample', AudioSpecificMetadata.bits_per_sample.validator),
    ('device', AudioSpecificMetadata.device.validator),
    ('duration_precise', AudioSpecificMetadata.duration_precise.validator),
    ('file_type_extension', AudioSpecificMetadata.file_type_extension.validator)]
BoltTokenResponse.bolt_token.validator = bv.String()
BoltTokenResponse.bolt_token.validator._redact = bv.BlotRedactor(None)
BoltTokenResponse.bolt_unique_id.validator = bv.String()
BoltTokenResponse.bolt_unique_id.validator._redact = bv.BlotRedactor(None)
BoltTokenResponse.latest_sjid.validator = bv.UInt64()
BoltTokenResponse.latest_sjid.validator._redact = bv.BlotRedactor(None)
BoltTokenResponse._all_field_names_ = set([
    'bolt_token',
    'bolt_unique_id',
    'latest_sjid'])
BoltTokenResponse._all_fields_ = [
    ('bolt_token', BoltTokenResponse.bolt_token.validator),
    ('bolt_unique_id', BoltTokenResponse.bolt_unique_id.validator),
    ('latest_sjid', BoltTokenResponse.latest_sjid.validator)]
BrowseBoltDataArg.current_ns_id.validator = bv.UInt64()
BrowseBoltDataArg.current_ns_id.validator._redact = bv.BlotRedactor(None)
BrowseBoltDataArg._all_field_names_ = set([
    'current_ns_id'])
BrowseBoltDataArg._all_fields_ = [
    ('current_ns_id', BrowseBoltDataArg.current_ns_id.validator)]
BrowseBoltDataError.err_message.validator = bv.String()
BrowseBoltDataError.err_message.validator._redact = bv.BlotRedactor(None)
BrowseBoltDataError._all_field_names_ = set([
    'err_message'])
BrowseBoltDataError._all_fields_ = [
    ('err_message', BrowseBoltDataError.err_message.validator)]
BrowseBoltDataResult.bolt_token_response.validator = bv.Nullable(bv.List(BoltTokenResponse_validator))
BrowseBoltDataResult._all_field_names_ = set([
    'bolt_token_response'])
BrowseBoltDataResult._all_fields_ = [
    ('bolt_token_response', BrowseBoltDataResult.bolt_token_response.validator)]
BrowseContext.block_hash.validator = bv.String()
BrowseContext.block_hash.validator._redact = bv.BlotRedactor(None)
BrowseContext.containing_fq_path.validator = bv.String()
BrowseContext.containing_fq_path.validator._redact = bv.BlotRedactor(None)
BrowseContext.containing_mount_point.validator = bv.String()
BrowseContext.containing_mount_point.validator._redact = bv.BlotRedactor(None)
BrowseContext.containing_ns_id.validator = bv.UInt64()
BrowseContext.containing_ns_id.validator._redact = bv.BlotRedactor(None)
BrowseContext.containing_ns_path.validator = bv.String()
BrowseContext.containing_ns_path.validator._redact = bv.BlotRedactor(None)
BrowseContext.containing_ns_permissions.validator = bv.Nullable(bv.List(bv.String()))
BrowseContext.containing_ns_permissions.validator._redact = bv.BlotRedactor(None)
BrowseContext.in_root_dir.validator = bv.Boolean()
BrowseContext.in_root_dir.validator._redact = bv.BlotRedactor(None)
BrowseContext.inside_archived_team_folder.validator = bv.Boolean()
BrowseContext.inside_archived_team_folder.validator._redact = bv.BlotRedactor(None)
BrowseContext.inside_deleted_dir.validator = bv.Boolean()
BrowseContext.inside_deleted_dir.validator._redact = bv.BlotRedactor(None)
BrowseContext.inside_deleted_nested_shared_folder.validator = bv.Boolean()
BrowseContext.inside_deleted_nested_shared_folder.validator._redact = bv.BlotRedactor(None)
BrowseContext.inside_deleted_shared_folder.validator = bv.Boolean()
BrowseContext.inside_deleted_shared_folder.validator._redact = bv.BlotRedactor(None)
BrowseContext.inside_dir.validator = bv.Boolean()
BrowseContext.inside_dir.validator._redact = bv.BlotRedactor(None)
BrowseContext.inside_sandbox_folder.validator = bv.Boolean()
BrowseContext.inside_sandbox_folder.validator._redact = bv.BlotRedactor(None)
BrowseContext.inside_shared_folder.validator = bv.Boolean()
BrowseContext.inside_shared_folder.validator._redact = bv.BlotRedactor(None)
BrowseContext.inside_team_folder_root.validator = bv.Boolean()
BrowseContext.inside_team_folder_root.validator._redact = bv.BlotRedactor(None)
BrowseContext.inside_team_folder_tree.validator = bv.Boolean()
BrowseContext.inside_team_folder_tree.validator._redact = bv.BlotRedactor(None)
BrowseContext.inside_my_team_folder_tree.validator = bv.Boolean()
BrowseContext.inside_my_team_folder_tree.validator._redact = bv.BlotRedactor(None)
BrowseContext.is_non_user_relative_context.validator = bv.Boolean()
BrowseContext.is_non_user_relative_context.validator._redact = bv.BlotRedactor(None)
BrowseContext.paginated.validator = bv.Boolean()
BrowseContext.paginated.validator._redact = bv.BlotRedactor(None)
BrowseContext.public_app_token.validator = bv.String()
BrowseContext.public_app_token.validator._redact = bv.BlotRedactor(None)
BrowseContext.root_ns_id.validator = bv.UInt64()
BrowseContext.root_ns_id.validator._redact = bv.BlotRedactor(None)
BrowseContext.show_pinned_team_folder.validator = bv.Boolean()
BrowseContext.show_pinned_team_folder.validator._redact = bv.BlotRedactor(None)
BrowseContext.team_folder_owner_team_dbtid.validator = bv.String()
BrowseContext.team_folder_owner_team_dbtid.validator._redact = bv.BlotRedactor(None)
BrowseContext.team_folders_js_info.validator = bv.Nullable(bv.List(TeamFolderJsInfo_validator))
BrowseContext.ns_id_infos.validator = bv.Nullable(bv.List(NsidInfo_validator))
BrowseContext.deleted_ns_id_infos.validator = bv.Nullable(bv.List(DeletedNsidInfo_validator))
BrowseContext.old_path_infos.validator = bv.Nullable(bv.List(OldPathInfo_validator))
BrowseContext.in_family_shared_folder.validator = bv.Boolean()
BrowseContext.in_family_shared_folder.validator._redact = bv.BlotRedactor(None)
BrowseContext.ts.validator = bv.Int64()
BrowseContext.ts.validator._redact = bv.BlotRedactor(None)
BrowseContext.inside_family_shared_folder.validator = bv.Boolean()
BrowseContext.inside_family_shared_folder.validator._redact = bv.BlotRedactor(None)
BrowseContext.preview_file_info.validator = bv.Nullable(FileInfo_validator)
BrowseContext.is_encrypted.validator = bv.Boolean()
BrowseContext.is_encrypted.validator._redact = bv.BlotRedactor(None)
BrowseContext.is_tmf_root.validator = bv.Boolean()
BrowseContext.is_tmf_root.validator._redact = bv.BlotRedactor(None)
BrowseContext.is_in_tmf_tree.validator = bv.Boolean()
BrowseContext.is_in_tmf_tree.validator._redact = bv.BlotRedactor(None)
BrowseContext._all_field_names_ = set([
    'block_hash',
    'containing_fq_path',
    'containing_mount_point',
    'containing_ns_id',
    'containing_ns_path',
    'containing_ns_permissions',
    'in_root_dir',
    'inside_archived_team_folder',
    'inside_deleted_dir',
    'inside_deleted_nested_shared_folder',
    'inside_deleted_shared_folder',
    'inside_dir',
    'inside_sandbox_folder',
    'inside_shared_folder',
    'inside_team_folder_root',
    'inside_team_folder_tree',
    'inside_my_team_folder_tree',
    'is_non_user_relative_context',
    'paginated',
    'public_app_token',
    'root_ns_id',
    'show_pinned_team_folder',
    'team_folder_owner_team_dbtid',
    'team_folders_js_info',
    'ns_id_infos',
    'deleted_ns_id_infos',
    'old_path_infos',
    'in_family_shared_folder',
    'ts',
    'inside_family_shared_folder',
    'preview_file_info',
    'is_encrypted',
    'is_tmf_root',
    'is_in_tmf_tree'])
BrowseContext._all_fields_ = [][('block_hash', BrowseContext.block_hash.validator)][('containing_fq_path', BrowseContext.containing_fq_path.validator)][('containing_mount_point', BrowseContext.containing_mount_point.validator)][('containing_ns_id', BrowseContext.containing_ns_id.validator)][('containing_ns_path', BrowseContext.containing_ns_path.validator)][('containing_ns_permissions', BrowseContext.containing_ns_permissions.validator)][('in_root_dir', BrowseContext.in_root_dir.validator)][('inside_archived_team_folder', BrowseContext.inside_archived_team_folder.validator)][('inside_deleted_dir', BrowseContext.inside_deleted_dir.validator)][('inside_deleted_nested_shared_folder', BrowseContext.inside_deleted_nested_shared_folder.validator)][('inside_deleted_shared_folder', BrowseContext.inside_deleted_shared_folder.validator)][('inside_dir', BrowseContext.inside_dir.validator)][('inside_sandbox_folder', BrowseContext.inside_sandbox_folder.validator)][('inside_shared_folder', BrowseContext.inside_shared_folder.validator)][('inside_team_folder_root', BrowseContext.inside_team_folder_root.validator)][('inside_team_folder_tree', BrowseContext.inside_team_folder_tree.validator)][('inside_my_team_folder_tree', BrowseContext.inside_my_team_folder_tree.validator)][('is_non_user_relative_context', BrowseContext.is_non_user_relative_context.validator)][('paginated', BrowseContext.paginated.validator)][('public_app_token', BrowseContext.public_app_token.validator)][('root_ns_id', BrowseContext.root_ns_id.validator)][('show_pinned_team_folder', BrowseContext.show_pinned_team_folder.validator)][('team_folder_owner_team_dbtid', BrowseContext.team_folder_owner_team_dbtid.validator)][('team_folders_js_info', BrowseContext.team_folders_js_info.validator)][('ns_id_infos', BrowseContext.ns_id_infos.validator)][('deleted_ns_id_infos', BrowseContext.deleted_ns_id_infos.validator)][('old_path_infos', BrowseContext.old_path_infos.validator)][('in_family_shared_folder', BrowseContext.in_family_shared_folder.validator)][('ts', BrowseContext.ts.validator)][('inside_family_shared_folder', BrowseContext.inside_family_shared_folder.validator)][('preview_file_info', BrowseContext.preview_file_info.validator)][('is_encrypted', BrowseContext.is_encrypted.validator)][('is_tmf_root', BrowseContext.is_tmf_root.validator)][('is_in_tmf_tree', BrowseContext.is_in_tmf_tree.validator)]
BrowseContextCypress.block_hash.validator = bv.String()
BrowseContextCypress.block_hash.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.containing_fq_path.validator = bv.String()
BrowseContextCypress.containing_fq_path.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.containing_mount_point.validator = bv.String()
BrowseContextCypress.containing_mount_point.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.containing_ns_id.validator = bv.UInt64()
BrowseContextCypress.containing_ns_id.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.containing_ns_path.validator = bv.String()
BrowseContextCypress.containing_ns_path.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.containing_ns_permissions.validator = bv.Nullable(bv.List(bv.String()))
BrowseContextCypress.containing_ns_permissions.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.in_root_dir.validator = bv.Boolean()
BrowseContextCypress.in_root_dir.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.inside_archived_team_folder.validator = bv.Boolean()
BrowseContextCypress.inside_archived_team_folder.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.inside_deleted_dir.validator = bv.Boolean()
BrowseContextCypress.inside_deleted_dir.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.inside_deleted_nested_shared_folder.validator = bv.Boolean()
BrowseContextCypress.inside_deleted_nested_shared_folder.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.inside_deleted_shared_folder.validator = bv.Boolean()
BrowseContextCypress.inside_deleted_shared_folder.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.inside_dir.validator = bv.Boolean()
BrowseContextCypress.inside_dir.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.inside_sandbox_folder.validator = bv.Boolean()
BrowseContextCypress.inside_sandbox_folder.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.inside_shared_folder.validator = bv.Boolean()
BrowseContextCypress.inside_shared_folder.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.inside_team_folder_root.validator = bv.Boolean()
BrowseContextCypress.inside_team_folder_root.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.inside_team_folder_tree.validator = bv.Boolean()
BrowseContextCypress.inside_team_folder_tree.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.inside_my_team_folder_tree.validator = bv.Boolean()
BrowseContextCypress.inside_my_team_folder_tree.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.is_non_user_relative_context.validator = bv.Boolean()
BrowseContextCypress.is_non_user_relative_context.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.paginated.validator = bv.Boolean()
BrowseContextCypress.paginated.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.public_app_token.validator = bv.String()
BrowseContextCypress.public_app_token.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.root_ns_id.validator = bv.UInt64()
BrowseContextCypress.root_ns_id.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.show_pinned_team_folder.validator = bv.Boolean()
BrowseContextCypress.show_pinned_team_folder.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.team_folder_owner_team_dbtid.validator = bv.String()
BrowseContextCypress.team_folder_owner_team_dbtid.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.team_folders_js_info.validator = bv.Nullable(bv.List(TeamFolderJsInfoCypress_validator))
BrowseContextCypress.ns_id_infos.validator = bv.Nullable(bv.List(NsidInfo_validator))
BrowseContextCypress.deleted_nsid_infos.validator = bv.Nullable(bv.List(DeletedNsidInfo_validator))
BrowseContextCypress.deleted_root_oid_infos.validator = bv.Nullable(bv.List(DeletedRootOidInfo_validator))
BrowseContextCypress.old_path_infos.validator = bv.Nullable(bv.List(OldPathInfoCypress_validator))
BrowseContextCypress.in_family_shared_folder.validator = bv.Boolean()
BrowseContextCypress.in_family_shared_folder.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.ts.validator = bv.Int64()
BrowseContextCypress.ts.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.inside_family_shared_folder.validator = bv.Boolean()
BrowseContextCypress.inside_family_shared_folder.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.preview_file_info.validator = bv.Nullable(ObjectInfo_validator)
BrowseContextCypress.containing_root_oid.validator = bv.Nullable(version_tree.Oid_validator)
BrowseContextCypress.root_oid.validator = bv.Nullable(version_tree.Oid_validator)
BrowseContextCypress.path_from_containing_root.validator = bv.String()
BrowseContextCypress.path_from_containing_root.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.root_oid_infos.validator = bv.Nullable(bv.List(RootOidInfo_validator))
BrowseContextCypress.is_encrypted.validator = bv.Boolean()
BrowseContextCypress.is_encrypted.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.is_tmf_root.validator = bv.Boolean()
BrowseContextCypress.is_tmf_root.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress.is_in_tmf_tree.validator = bv.Boolean()
BrowseContextCypress.is_in_tmf_tree.validator._redact = bv.BlotRedactor(None)
BrowseContextCypress._all_field_names_ = set([
    'block_hash',
    'containing_fq_path',
    'containing_mount_point',
    'containing_ns_id',
    'containing_ns_path',
    'containing_ns_permissions',
    'in_root_dir',
    'inside_archived_team_folder',
    'inside_deleted_dir',
    'inside_deleted_nested_shared_folder',
    'inside_deleted_shared_folder',
    'inside_dir',
    'inside_sandbox_folder',
    'inside_shared_folder',
    'inside_team_folder_root',
    'inside_team_folder_tree',
    'inside_my_team_folder_tree',
    'is_non_user_relative_context',
    'paginated',
    'public_app_token',
    'root_ns_id',
    'show_pinned_team_folder',
    'team_folder_owner_team_dbtid',
    'team_folders_js_info',
    'ns_id_infos',
    'deleted_nsid_infos',
    'deleted_root_oid_infos',
    'old_path_infos',
    'in_family_shared_folder',
    'ts',
    'inside_family_shared_folder',
    'preview_file_info',
    'containing_root_oid',
    'root_oid',
    'path_from_containing_root',
    'root_oid_infos',
    'is_encrypted',
    'is_tmf_root',
    'is_in_tmf_tree'])
BrowseContextCypress._all_fields_ = [][('block_hash', BrowseContextCypress.block_hash.validator)][('containing_fq_path', BrowseContextCypress.containing_fq_path.validator)][('containing_mount_point', BrowseContextCypress.containing_mount_point.validator)][('containing_ns_id', BrowseContextCypress.containing_ns_id.validator)][('containing_ns_path', BrowseContextCypress.containing_ns_path.validator)][('containing_ns_permissions', BrowseContextCypress.containing_ns_permissions.validator)][('in_root_dir', BrowseContextCypress.in_root_dir.validator)][('inside_archived_team_folder', BrowseContextCypress.inside_archived_team_folder.validator)][('inside_deleted_dir', BrowseContextCypress.inside_deleted_dir.validator)][('inside_deleted_nested_shared_folder', BrowseContextCypress.inside_deleted_nested_shared_folder.validator)][('inside_deleted_shared_folder', BrowseContextCypress.inside_deleted_shared_folder.validator)][('inside_dir', BrowseContextCypress.inside_dir.validator)][('inside_sandbox_folder', BrowseContextCypress.inside_sandbox_folder.validator)][('inside_shared_folder', BrowseContextCypress.inside_shared_folder.validator)][('inside_team_folder_root', BrowseContextCypress.inside_team_folder_root.validator)][('inside_team_folder_tree', BrowseContextCypress.inside_team_folder_tree.validator)][('inside_my_team_folder_tree', BrowseContextCypress.inside_my_team_folder_tree.validator)][('is_non_user_relative_context', BrowseContextCypress.is_non_user_relative_context.validator)][('paginated', BrowseContextCypress.paginated.validator)][('public_app_token', BrowseContextCypress.public_app_token.validator)][('root_ns_id', BrowseContextCypress.root_ns_id.validator)][('show_pinned_team_folder', BrowseContextCypress.show_pinned_team_folder.validator)][('team_folder_owner_team_dbtid', BrowseContextCypress.team_folder_owner_team_dbtid.validator)][('team_folders_js_info', BrowseContextCypress.team_folders_js_info.validator)][('ns_id_infos', BrowseContextCypress.ns_id_infos.validator)][('deleted_nsid_infos', BrowseContextCypress.deleted_nsid_infos.validator)][('deleted_root_oid_infos', BrowseContextCypress.deleted_root_oid_infos.validator)][('old_path_infos', BrowseContextCypress.old_path_infos.validator)][('in_family_shared_folder', BrowseContextCypress.in_family_shared_folder.validator)][('ts', BrowseContextCypress.ts.validator)][('inside_family_shared_folder', BrowseContextCypress.inside_family_shared_folder.validator)][('preview_file_info', BrowseContextCypress.preview_file_info.validator)][('containing_root_oid', BrowseContextCypress.containing_root_oid.validator)][('root_oid', BrowseContextCypress.root_oid.validator)][('path_from_containing_root', BrowseContextCypress.path_from_containing_root.validator)][('root_oid_infos', BrowseContextCypress.root_oid_infos.validator)][('is_encrypted', BrowseContextCypress.is_encrypted.validator)][('is_tmf_root', BrowseContextCypress.is_tmf_root.validator)][('is_in_tmf_tree', BrowseContextCypress.is_in_tmf_tree.validator)]
BrowseContextResponse.context.validator = bv.Nullable(BrowseContext_validator)
BrowseContextResponse.folder_info.validator = bv.Nullable(BrowsePaginatedFileInfo_validator)
BrowseContextResponse._all_field_names_ = set([
    'context',
    'folder_info'])
BrowseContextResponse._all_fields_ = [
    ('context', BrowseContextResponse.context.validator),
    ('folder_info', BrowseContextResponse.folder_info.validator)]
BrowseContextResponseCypress.context.validator = bv.Nullable(BrowseContextCypress_validator)
BrowseContextResponseCypress.folder_info.validator = bv.Nullable(BrowsePaginatedObjectInfo_validator)
BrowseContextResponseCypress._all_field_names_ = set([
    'context',
    'folder_info'])
BrowseContextResponseCypress._all_fields_ = [
    ('context', BrowseContextResponseCypress.context.validator),
    ('folder_info', BrowseContextResponseCypress.folder_info.validator)]
BrowseErrorStatus._auth_failed_validator = bv.Void()
BrowseErrorStatus._rate_limited_validator = bv.Void()
BrowseErrorStatus._invalid_path_validator = bv.Void()
BrowseErrorStatus._folder_not_found_validator = bv.Void()
BrowseErrorStatus._folder_is_deleted_validator = bv.Void()
BrowseErrorStatus._other_validator = bv.Void()
BrowseErrorStatus._tagmap = {
    'auth_failed': BrowseErrorStatus._auth_failed_validator,
    'rate_limited': BrowseErrorStatus._rate_limited_validator,
    'invalid_path': BrowseErrorStatus._invalid_path_validator,
    'folder_not_found': BrowseErrorStatus._folder_not_found_validator,
    'folder_is_deleted': BrowseErrorStatus._folder_is_deleted_validator,
    'other': BrowseErrorStatus._other_validator }
BrowseErrorStatus.auth_failed = BrowseErrorStatus('auth_failed')
BrowseErrorStatus.rate_limited = BrowseErrorStatus('rate_limited')
BrowseErrorStatus.invalid_path = BrowseErrorStatus('invalid_path')
BrowseErrorStatus.folder_not_found = BrowseErrorStatus('folder_not_found')
BrowseErrorStatus.folder_is_deleted = BrowseErrorStatus('folder_is_deleted')
BrowseErrorStatus.other = BrowseErrorStatus('other')
BrowseGetNextResponse.paginated_file_info.validator = bv.Nullable(bv.List(BrowsePaginatedFileInfo_validator))
BrowseGetNextResponse.total_count.validator = bv.Int64()
BrowseGetNextResponse.total_count.validator._redact = bv.BlotRedactor(None)
BrowseGetNextResponse.has_more.validator = bv.Boolean()
BrowseGetNextResponse.has_more.validator._redact = bv.BlotRedactor(None)
BrowseGetNextResponse.next_request_voucher.validator = bv.String()
BrowseGetNextResponse.next_request_voucher.validator._redact = bv.BlotRedactor(None)
BrowseGetNextResponse._all_field_names_ = set([
    'paginated_file_info',
    'total_count',
    'has_more',
    'next_request_voucher'])
BrowseGetNextResponse._all_fields_ = [
    ('paginated_file_info', BrowseGetNextResponse.paginated_file_info.validator),
    ('total_count', BrowseGetNextResponse.total_count.validator),
    ('has_more', BrowseGetNextResponse.has_more.validator),
    ('next_request_voucher', BrowseGetNextResponse.next_request_voucher.validator)]
BrowseGetNextResponseCypress.paginated_file_info.validator = bv.Nullable(bv.List(BrowsePaginatedObjectInfo_validator))
BrowseGetNextResponseCypress.total_count.validator = bv.Int64()
BrowseGetNextResponseCypress.total_count.validator._redact = bv.BlotRedactor(None)
BrowseGetNextResponseCypress.has_more.validator = bv.Boolean()
BrowseGetNextResponseCypress.has_more.validator._redact = bv.BlotRedactor(None)
BrowseGetNextResponseCypress.next_request_voucher.validator = bv.String()
BrowseGetNextResponseCypress.next_request_voucher.validator._redact = bv.BlotRedactor(None)
BrowseGetNextResponseCypress._all_field_names_ = set([
    'paginated_file_info',
    'total_count',
    'has_more',
    'next_request_voucher'])
BrowseGetNextResponseCypress._all_fields_ = [
    ('paginated_file_info', BrowseGetNextResponseCypress.paginated_file_info.validator),
    ('total_count', BrowseGetNextResponseCypress.total_count.validator),
    ('has_more', BrowseGetNextResponseCypress.has_more.validator),
    ('next_request_voucher', BrowseGetNextResponseCypress.next_request_voucher.validator)]
BrowsePaginatedFileInfo.file_info.validator = bv.Nullable(FileInfo_validator)
BrowsePaginatedFileInfo.team_folder_status.validator = TeamFolderStatus_validator
BrowsePaginatedFileInfo._all_field_names_ = set([
    'file_info',
    'team_folder_status'])
BrowsePaginatedFileInfo._all_fields_ = [
    ('file_info', BrowsePaginatedFileInfo.file_info.validator),
    ('team_folder_status', BrowsePaginatedFileInfo.team_folder_status.validator)]
BrowsePaginatedObjectInfo.file_info.validator = bv.Nullable(ObjectInfo_validator)
BrowsePaginatedObjectInfo.team_folder_status.validator = TeamFolderStatus_validator
BrowsePaginatedObjectInfo._all_field_names_ = set([
    'file_info',
    'team_folder_status'])
BrowsePaginatedObjectInfo._all_fields_ = [
    ('file_info', BrowsePaginatedObjectInfo.file_info.validator),
    ('team_folder_status', BrowsePaginatedObjectInfo.team_folder_status.validator)]
BrowseRecentItem.item.validator = bv.Nullable(ItemUnion_validator)
BrowseRecentItem._all_field_names_ = set([
    'item'])
BrowseRecentItem._all_fields_ = [
    ('item', BrowseRecentItem.item.validator)]
BrowseTeamContentArg.root_ns_id.validator = bv.UInt64()
BrowseTeamContentArg.root_ns_id.validator._redact = bv.BlotRedactor(None)
BrowseTeamContentArg.fq_path.validator = bv.String()
BrowseTeamContentArg.fq_path.validator._redact = bv.BlotRedactor(None)
BrowseTeamContentArg.include_deleted.validator = bv.Boolean()
BrowseTeamContentArg.include_deleted.validator._redact = bv.BlotRedactor(None)
BrowseTeamContentArg.include_retained.validator = bv.Boolean()
BrowseTeamContentArg.include_retained.validator._redact = bv.BlotRedactor(None)
BrowseTeamContentArg.sort_type.validator = SortType_validator
BrowseTeamContentArg.sort_is_ascending.validator = bv.Boolean()
BrowseTeamContentArg.sort_is_ascending.validator._redact = bv.BlotRedactor(None)
BrowseTeamContentArg.sort_folders_first.validator = bv.Boolean()
BrowseTeamContentArg.sort_folders_first.validator._redact = bv.BlotRedactor(None)
BrowseTeamContentArg._all_field_names_ = set([
    'root_ns_id',
    'fq_path',
    'include_deleted',
    'include_retained',
    'sort_type',
    'sort_is_ascending',
    'sort_folders_first'])
BrowseTeamContentArg._all_fields_ = [
    ('root_ns_id', BrowseTeamContentArg.root_ns_id.validator),
    ('fq_path', BrowseTeamContentArg.fq_path.validator),
    ('include_deleted', BrowseTeamContentArg.include_deleted.validator),
    ('include_retained', BrowseTeamContentArg.include_retained.validator),
    ('sort_type', BrowseTeamContentArg.sort_type.validator),
    ('sort_is_ascending', BrowseTeamContentArg.sort_is_ascending.validator),
    ('sort_folders_first', BrowseTeamContentArg.sort_folders_first.validator)]
BrowseV2Arg.fq_path.validator = bv.String()
BrowseV2Arg.fq_path.validator._redact = bv.BlotRedactor(None)
BrowseV2Arg.include_deleted.validator = bv.Boolean()
BrowseV2Arg.include_deleted.validator._redact = bv.BlotRedactor(None)
BrowseV2Arg.sort_type.validator = SortType_validator
BrowseV2Arg.sort_is_ascending.validator = bv.Boolean()
BrowseV2Arg.sort_is_ascending.validator._redact = bv.BlotRedactor(None)
BrowseV2Arg.sort_folders_first.validator = bv.Boolean()
BrowseV2Arg.sort_folders_first.validator._redact = bv.BlotRedactor(None)
BrowseV2Arg.include_xattrs.validator = bv.Boolean()
BrowseV2Arg.include_xattrs.validator._redact = bv.BlotRedactor(None)
BrowseV2Arg.include_folder_overview.validator = bv.Boolean()
BrowseV2Arg.include_folder_overview.validator._redact = bv.BlotRedactor(None)
BrowseV2Arg.preview_file_name.validator = bv.String()
BrowseV2Arg.preview_file_name.validator._redact = bv.BlotRedactor(None)
BrowseV2Arg.root_ns_id.validator = bv.UInt64()
BrowseV2Arg.root_ns_id.validator._redact = bv.BlotRedactor(None)
BrowseV2Arg.api_file_id_mode.validator = ApiFileIdMode_validator
BrowseV2Arg.cypress_exp_variant.validator = bv.String()
BrowseV2Arg.cypress_exp_variant.validator._redact = bv.BlotRedactor(None)
BrowseV2Arg.content_tiles_flags.validator = bv.Nullable(ContentTilesFlags_validator)
BrowseV2Arg.sort_source.validator = SortSource_validator
BrowseV2Arg.include_starred_status.validator = bv.Boolean()
BrowseV2Arg.include_starred_status.validator._redact = bv.BlotRedactor(None)
BrowseV2Arg.include_retained.validator = bv.Boolean()
BrowseV2Arg.include_retained.validator._redact = bv.BlotRedactor(None)
BrowseV2Arg.exclude_user_unowned_folders.validator = bv.Boolean()
BrowseV2Arg.exclude_user_unowned_folders.validator._redact = bv.BlotRedactor(None)
BrowseV2Arg._all_field_names_ = set([
    'fq_path',
    'include_deleted',
    'sort_type',
    'sort_is_ascending',
    'sort_folders_first',
    'include_xattrs',
    'include_folder_overview',
    'preview_file_name',
    'root_ns_id',
    'api_file_id_mode',
    'cypress_exp_variant',
    'content_tiles_flags',
    'sort_source',
    'include_starred_status',
    'include_retained',
    'exclude_user_unowned_folders'])
BrowseV2Arg._all_fields_ = [
    ('fq_path', BrowseV2Arg.fq_path.validator),
    ('include_deleted', BrowseV2Arg.include_deleted.validator),
    ('sort_type', BrowseV2Arg.sort_type.validator),
    ('sort_is_ascending', BrowseV2Arg.sort_is_ascending.validator),
    ('sort_folders_first', BrowseV2Arg.sort_folders_first.validator),
    ('include_xattrs', BrowseV2Arg.include_xattrs.validator),
    ('include_folder_overview', BrowseV2Arg.include_folder_overview.validator),
    ('preview_file_name', BrowseV2Arg.preview_file_name.validator),
    ('root_ns_id', BrowseV2Arg.root_ns_id.validator),
    ('api_file_id_mode', BrowseV2Arg.api_file_id_mode.validator),
    ('cypress_exp_variant', BrowseV2Arg.cypress_exp_variant.validator),
    ('content_tiles_flags', BrowseV2Arg.content_tiles_flags.validator),
    ('sort_source', BrowseV2Arg.sort_source.validator),
    ('include_starred_status', BrowseV2Arg.include_starred_status.validator),
    ('include_retained', BrowseV2Arg.include_retained.validator),
    ('exclude_user_unowned_folders', BrowseV2Arg.exclude_user_unowned_folders.validator)]
BrowseV2ContinueArg.cursor.validator = bv.String()
BrowseV2ContinueArg.cursor.validator._redact = bv.BlotRedactor(None)
BrowseV2ContinueArg.cypress_exp_variant.validator = bv.String()
BrowseV2ContinueArg.cypress_exp_variant.validator._redact = bv.BlotRedactor(None)
BrowseV2ContinueArg.content_tiles_flags.validator = bv.Nullable(ContentTilesFlags_validator)
BrowseV2ContinueArg.distinct_team_space_filter.validator = bv.Boolean()
BrowseV2ContinueArg.distinct_team_space_filter.validator._redact = bv.BlotRedactor(None)
BrowseV2ContinueArg.exclude_user_unowned_folders.validator = bv.Boolean()
BrowseV2ContinueArg.exclude_user_unowned_folders.validator._redact = bv.BlotRedactor(None)
BrowseV2ContinueArg.include_starred_status.validator = bv.Boolean()
BrowseV2ContinueArg.include_starred_status.validator._redact = bv.BlotRedactor(None)
BrowseV2ContinueArg._all_field_names_ = set([
    'cursor',
    'cypress_exp_variant',
    'content_tiles_flags',
    'distinct_team_space_filter',
    'exclude_user_unowned_folders',
    'include_starred_status'])
BrowseV2ContinueArg._all_fields_ = [
    ('cursor', BrowseV2ContinueArg.cursor.validator),
    ('cypress_exp_variant', BrowseV2ContinueArg.cypress_exp_variant.validator),
    ('content_tiles_flags', BrowseV2ContinueArg.content_tiles_flags.validator),
    ('distinct_team_space_filter', BrowseV2ContinueArg.distinct_team_space_filter.validator),
    ('exclude_user_unowned_folders', BrowseV2ContinueArg.exclude_user_unowned_folders.validator),
    ('include_starred_status', BrowseV2ContinueArg.include_starred_status.validator)]
BrowseV2Error.status.validator = BrowseErrorStatus_validator
BrowseV2Error.err_message.validator = bv.String()
BrowseV2Error.err_message.validator._redact = bv.BlotRedactor(None)
BrowseV2Error.path.validator = bv.String()
BrowseV2Error.path.validator._redact = bv.BlotRedactor(None)
BrowseV2Error._all_field_names_ = set([
    'status',
    'err_message',
    'path'])
BrowseV2Error._all_fields_ = [
    ('status', BrowseV2Error.status.validator),
    ('err_message', BrowseV2Error.err_message.validator),
    ('path', BrowseV2Error.path.validator)]
BrowseV2Result.context.validator = bv.Nullable(BrowseContext_validator)
BrowseV2Result.paginated_file_info.validator = bv.Nullable(bv.List(BrowsePaginatedFileInfo_validator))
BrowseV2Result.total_count.validator = bv.Int64()
BrowseV2Result.total_count.validator._redact = bv.BlotRedactor(None)
BrowseV2Result.has_more.validator = bv.Boolean()
BrowseV2Result.has_more.validator._redact = bv.BlotRedactor(None)
BrowseV2Result.next_request_voucher.validator = bv.String()
BrowseV2Result.next_request_voucher.validator._redact = bv.BlotRedactor(None)
BrowseV2Result.folder_info.validator = bv.Nullable(BrowsePaginatedFileInfo_validator)
BrowseV2Result._all_field_names_ = set([
    'context',
    'paginated_file_info',
    'total_count',
    'has_more',
    'next_request_voucher',
    'folder_info'])
BrowseV2Result._all_fields_ = [
    ('context', BrowseV2Result.context.validator),
    ('paginated_file_info', BrowseV2Result.paginated_file_info.validator),
    ('total_count', BrowseV2Result.total_count.validator),
    ('has_more', BrowseV2Result.has_more.validator),
    ('next_request_voucher', BrowseV2Result.next_request_voucher.validator),
    ('folder_info', BrowseV2Result.folder_info.validator)]
BrowseV3Arg.fq_path.validator = bv.String()
BrowseV3Arg.fq_path.validator._redact = bv.BlotRedactor(None)
BrowseV3Arg.include_deleted.validator = bv.Boolean()
BrowseV3Arg.include_deleted.validator._redact = bv.BlotRedactor(None)
BrowseV3Arg.sort_type.validator = SortType_validator
BrowseV3Arg.sort_is_ascending.validator = bv.Boolean()
BrowseV3Arg.sort_is_ascending.validator._redact = bv.BlotRedactor(None)
BrowseV3Arg.sort_folders_first.validator = bv.Boolean()
BrowseV3Arg.sort_folders_first.validator._redact = bv.BlotRedactor(None)
BrowseV3Arg.include_xattrs.validator = bv.Boolean()
BrowseV3Arg.include_xattrs.validator._redact = bv.BlotRedactor(None)
BrowseV3Arg.include_folder_overview.validator = bv.Boolean()
BrowseV3Arg.include_folder_overview.validator._redact = bv.BlotRedactor(None)
BrowseV3Arg.preview_file_name.validator = bv.String()
BrowseV3Arg.preview_file_name.validator._redact = bv.BlotRedactor(None)
BrowseV3Arg.root_oid.validator = bv.Nullable(version_tree.Oid_validator)
BrowseV3Arg.api_file_id_mode.validator = ApiFileIdMode_validator
BrowseV3Arg.include_retained.validator = bv.Boolean()
BrowseV3Arg.include_retained.validator._redact = bv.BlotRedactor(None)
BrowseV3Arg._all_field_names_ = set([
    'fq_path',
    'include_deleted',
    'sort_type',
    'sort_is_ascending',
    'sort_folders_first',
    'include_xattrs',
    'include_folder_overview',
    'preview_file_name',
    'root_oid',
    'api_file_id_mode',
    'include_retained'])
BrowseV3Arg._all_fields_ = [
    ('fq_path', BrowseV3Arg.fq_path.validator),
    ('include_deleted', BrowseV3Arg.include_deleted.validator),
    ('sort_type', BrowseV3Arg.sort_type.validator),
    ('sort_is_ascending', BrowseV3Arg.sort_is_ascending.validator),
    ('sort_folders_first', BrowseV3Arg.sort_folders_first.validator),
    ('include_xattrs', BrowseV3Arg.include_xattrs.validator),
    ('include_folder_overview', BrowseV3Arg.include_folder_overview.validator),
    ('preview_file_name', BrowseV3Arg.preview_file_name.validator),
    ('root_oid', BrowseV3Arg.root_oid.validator),
    ('api_file_id_mode', BrowseV3Arg.api_file_id_mode.validator),
    ('include_retained', BrowseV3Arg.include_retained.validator)]
BrowseV3ContinueArg.cursor.validator = bv.String()
BrowseV3ContinueArg.cursor.validator._redact = bv.BlotRedactor(None)
BrowseV3ContinueArg._all_field_names_ = set([
    'cursor'])
BrowseV3ContinueArg._all_fields_ = [
    ('cursor', BrowseV3ContinueArg.cursor.validator)]
BrowseV3Result.context.validator = bv.Nullable(BrowseContextCypress_validator)
BrowseV3Result.paginated_file_info.validator = bv.Nullable(bv.List(BrowsePaginatedObjectInfo_validator))
BrowseV3Result.total_count.validator = bv.Int64()
BrowseV3Result.total_count.validator._redact = bv.BlotRedactor(None)
BrowseV3Result.has_more.validator = bv.Boolean()
BrowseV3Result.has_more.validator._redact = bv.BlotRedactor(None)
BrowseV3Result.next_request_voucher.validator = bv.String()
BrowseV3Result.next_request_voucher.validator._redact = bv.BlotRedactor(None)
BrowseV3Result.folder_info.validator = bv.Nullable(BrowsePaginatedObjectInfo_validator)
BrowseV3Result._all_field_names_ = set([
    'context',
    'paginated_file_info',
    'total_count',
    'has_more',
    'next_request_voucher',
    'folder_info'])
BrowseV3Result._all_fields_ = [
    ('context', BrowseV3Result.context.validator),
    ('paginated_file_info', BrowseV3Result.paginated_file_info.validator),
    ('total_count', BrowseV3Result.total_count.validator),
    ('has_more', BrowseV3Result.has_more.validator),
    ('next_request_voucher', BrowseV3Result.next_request_voucher.validator),
    ('folder_info', BrowseV3Result.folder_info.validator)]
Changeset.ns_id.validator = bv.UInt64()
Changeset.ns_id.validator._redact = bv.BlotRedactor(None)
Changeset.changes.validator = bv.List(bv.UInt64())
Changeset.changes.validator._redact = bv.BlotRedactor(None)
Changeset._all_field_names_ = set([
    'ns_id',
    'changes'])
Changeset._all_fields_ = [
    ('ns_id', Changeset.ns_id.validator),
    ('changes', Changeset.changes.validator)]
ChangesetData.ns_id.validator = bv.UInt64()
ChangesetData.ns_id.validator._redact = bv.BlotRedactor(None)
ChangesetData.op_id.validator = bv.String()
ChangesetData.op_id.validator._redact = bv.BlotRedactor(None)
ChangesetData._all_field_names_ = set([
    'ns_id',
    'op_id'])
ChangesetData._all_fields_ = [
    ('ns_id', ChangesetData.ns_id.validator),
    ('op_id', ChangesetData.op_id.validator)]
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
Classifier._document_classification_validator = bv.Void()
Classifier._image_feature_validator = bv.Void()
Classifier._other_validator = bv.Void()
Classifier._tagmap = {
    'document_classification': Classifier._document_classification_validator,
    'image_feature': Classifier._image_feature_validator,
    'other': Classifier._other_validator }
Classifier.document_classification = Classifier('document_classification')
Classifier.image_feature = Classifier('image_feature')
Classifier.other = Classifier('other')
CloudDocClass._cloud_backed_file_validator = bv.Void()
CloudDocClass._canonical_validator = bv.Void()
CloudDocClass._pointer_validator = bv.Void()
CloudDocClass._other_validator = bv.Void()
CloudDocClass._tagmap = {
    'cloud_backed_file': CloudDocClass._cloud_backed_file_validator,
    'canonical': CloudDocClass._canonical_validator,
    'pointer': CloudDocClass._pointer_validator,
    'other': CloudDocClass._other_validator }
CloudDocClass.cloud_backed_file = CloudDocClass('cloud_backed_file')
CloudDocClass.canonical = CloudDocClass('canonical')
CloudDocClass.pointer = CloudDocClass('pointer')
CloudDocClass.other = CloudDocClass('other')
CloudDocInfo.cloud_doc_type.validator = CloudDocType_validator
CloudDocInfo.size_bytes.validator = CloudDocSize_validator
CloudDocInfo.cloud_doc_class.validator = CloudDocClass_validator
CloudDocInfo.open_url.validator = bv.Nullable(bv.String())
CloudDocInfo._all_field_names_ = set([
    'cloud_doc_type',
    'size_bytes',
    'cloud_doc_class',
    'open_url'])
CloudDocInfo._all_fields_ = [
    ('cloud_doc_type', CloudDocInfo.cloud_doc_type.validator),
    ('size_bytes', CloudDocInfo.size_bytes.validator),
    ('cloud_doc_class', CloudDocInfo.cloud_doc_class.validator),
    ('open_url', CloudDocInfo.open_url.validator)]
CloudDocSize._undefined_validator = bv.Void()
CloudDocSize._size_bytes_validator = bv.Int64()
CloudDocSize._size_bytes_validator._redact = bv.BlotRedactor(None)
CloudDocSize._other_validator = bv.Void()
CloudDocSize._tagmap = {
    'undefined': CloudDocSize._undefined_validator,
    'size_bytes': CloudDocSize._size_bytes_validator,
    'other': CloudDocSize._other_validator }
CloudDocSize.undefined = CloudDocSize('undefined')
CloudDocSize.other = CloudDocSize('other')
CloudDocType._paper_validator = bv.Void()
CloudDocType._paper_template_validator = bv.Void()
CloudDocType._paper_site_validator = bv.Void()
CloudDocType._paper_binder_validator = bv.Void()
CloudDocType._google_doc_validator = bv.Void()
CloudDocType._google_sheets_validator = bv.Void()
CloudDocType._google_slides_validator = bv.Void()
CloudDocType._simple_pointer_validator = bv.Void()
CloudDocType._other_validator = bv.Void()
CloudDocType._tagmap = {
    'paper': CloudDocType._paper_validator,
    'paper_template': CloudDocType._paper_template_validator,
    'paper_site': CloudDocType._paper_site_validator,
    'paper_binder': CloudDocType._paper_binder_validator,
    'google_doc': CloudDocType._google_doc_validator,
    'google_sheets': CloudDocType._google_sheets_validator,
    'google_slides': CloudDocType._google_slides_validator,
    'simple_pointer': CloudDocType._simple_pointer_validator,
    'other': CloudDocType._other_validator }
CloudDocType.paper = CloudDocType('paper')
CloudDocType.paper_template = CloudDocType('paper_template')
CloudDocType.paper_site = CloudDocType('paper_site')
CloudDocType.paper_binder = CloudDocType('paper_binder')
CloudDocType.google_doc = CloudDocType('google_doc')
CloudDocType.google_sheets = CloudDocType('google_sheets')
CloudDocType.google_slides = CloudDocType('google_slides')
CloudDocType.simple_pointer = CloudDocType('simple_pointer')
CloudDocType.other = CloudDocType('other')
CommitInfo.path.validator = WritePathOrId_validator
CommitInfo.mode.validator = WriteMode_validator
CommitInfo.autorename.validator = bv.Boolean()
CommitInfo.autorename.validator._redact = bv.BlotRedactor(None)
CommitInfo.client_modified.validator = bv.Nullable(common.DropboxTimestamp_validator)
CommitInfo.mute.validator = bv.Boolean()
CommitInfo.mute.validator._redact = bv.BlotRedactor(None)
CommitInfo.property_groups.validator = bv.Nullable(bv.List(file_properties.PropertyGroup_validator))
CommitInfo.strict_conflict.validator = bv.Boolean()
CommitInfo.strict_conflict.validator._redact = bv.BlotRedactor(None)
CommitInfo.fsw_request.validator = bv.Nullable(FswRequest_validator)
CommitInfo.file_encryption_info.validator = bv.Nullable(encryption.EncryptedFile_validator)
CommitInfo._all_field_names_ = set([
    'path',
    'mode',
    'autorename',
    'client_modified',
    'mute',
    'property_groups',
    'strict_conflict'])
CommitInfo._all_fields_ = [
    ('path', CommitInfo.path.validator),
    ('mode', CommitInfo.mode.validator),
    ('autorename', CommitInfo.autorename.validator),
    ('client_modified', CommitInfo.client_modified.validator),
    ('mute', CommitInfo.mute.validator),
    ('property_groups', CommitInfo.property_groups.validator),
    ('strict_conflict', CommitInfo.strict_conflict.validator)]
CommitInfo._all_internal_field_names_ = set([
    'fsw_request',
    'file_encryption_info'])
CommitInfo._all_internal_fields_ = [
    ('fsw_request', CommitInfo.fsw_request.validator),
    ('file_encryption_info', CommitInfo.file_encryption_info.validator)]
ContentSyncSetting.id.validator = FileId_validator
ContentSyncSetting.sync_setting.validator = SyncSetting_validator
ContentSyncSetting._all_field_names_ = set([
    'id',
    'sync_setting'])
ContentSyncSetting._all_fields_ = [
    ('id', ContentSyncSetting.id.validator),
    ('sync_setting', ContentSyncSetting.sync_setting.validator)]
ContentSyncSettingArg.id.validator = FileId_validator
ContentSyncSettingArg.sync_setting.validator = SyncSettingArg_validator
ContentSyncSettingArg._all_field_names_ = set([
    'id',
    'sync_setting'])
ContentSyncSettingArg._all_fields_ = [
    ('id', ContentSyncSettingArg.id.validator),
    ('sync_setting', ContentSyncSettingArg.sync_setting.validator)]
ContentTileMetadata.scrubbing_items_metadata.validator = bv.Nullable(bv.List(ScrubbingItemMetadata_validator))
ContentTileMetadata.folder_collage_items_metadata.validator = bv.Nullable(bv.List(FolderCollageItemMetadata_validator))
ContentTileMetadata.folder_contains_more_item.validator = bv.Boolean()
ContentTileMetadata.folder_contains_more_item.validator._redact = bv.BlotRedactor(None)
ContentTileMetadata.descendants_count.validator = bv.Int64()
ContentTileMetadata.descendants_count.validator._redact = bv.BlotRedactor(None)
ContentTileMetadata.folder_size.validator = bv.UInt64()
ContentTileMetadata.folder_size.validator._redact = bv.BlotRedactor(None)
ContentTileMetadata.folder_size_maybe_larger.validator = bv.Boolean()
ContentTileMetadata.folder_size_maybe_larger.validator._redact = bv.BlotRedactor(None)
ContentTileMetadata._all_field_names_ = set([
    'scrubbing_items_metadata',
    'folder_collage_items_metadata',
    'folder_contains_more_item',
    'descendants_count',
    'folder_size',
    'folder_size_maybe_larger'])
ContentTileMetadata._all_fields_ = [
    ('scrubbing_items_metadata', ContentTileMetadata.scrubbing_items_metadata.validator),
    ('folder_collage_items_metadata', ContentTileMetadata.folder_collage_items_metadata.validator),
    ('folder_contains_more_item', ContentTileMetadata.folder_contains_more_item.validator),
    ('descendants_count', ContentTileMetadata.descendants_count.validator),
    ('folder_size', ContentTileMetadata.folder_size.validator),
    ('folder_size_maybe_larger', ContentTileMetadata.folder_size_maybe_larger.validator)]
ContentTilesDocMetadata.scrubbing_metadata.validator = bv.Nullable(bv.List(ScrubbingItemMetadata_validator))
ContentTilesDocMetadata._all_field_names_ = set([
    'scrubbing_metadata'])
ContentTilesDocMetadata._all_fields_ = [
    ('scrubbing_metadata', ContentTilesDocMetadata.scrubbing_metadata.validator)]
ContentTilesFlags.content_tiles_variant.validator = bv.String()
ContentTilesFlags.content_tiles_variant.validator._redact = bv.BlotRedactor(None)
ContentTilesFlags.folder_collage_variant.validator = bv.String()
ContentTilesFlags.folder_collage_variant.validator._redact = bv.BlotRedactor(None)
ContentTilesFlags.folder_scrubbing_variant.validator = bv.String()
ContentTilesFlags.folder_scrubbing_variant.validator._redact = bv.BlotRedactor(None)
ContentTilesFlags.video_interactivity_variant.validator = bv.String()
ContentTilesFlags.video_interactivity_variant.validator._redact = bv.BlotRedactor(None)
ContentTilesFlags.pdf_interactivity_variant.validator = bv.String()
ContentTilesFlags.pdf_interactivity_variant.validator._redact = bv.BlotRedactor(None)
ContentTilesFlags._all_field_names_ = set([
    'content_tiles_variant',
    'folder_collage_variant',
    'folder_scrubbing_variant',
    'video_interactivity_variant',
    'pdf_interactivity_variant'])
ContentTilesFlags._all_fields_ = [
    ('content_tiles_variant', ContentTilesFlags.content_tiles_variant.validator),
    ('folder_collage_variant', ContentTilesFlags.folder_collage_variant.validator),
    ('folder_scrubbing_variant', ContentTilesFlags.folder_scrubbing_variant.validator),
    ('video_interactivity_variant', ContentTilesFlags.video_interactivity_variant.validator),
    ('pdf_interactivity_variant', ContentTilesFlags.pdf_interactivity_variant.validator)]
ContentTilesFolderMetadata.scrubbing_metadata.validator = bv.Nullable(bv.List(ScrubbingItemMetadata_validator))
ContentTilesFolderMetadata.folder_collage_metadata.validator = bv.Nullable(bv.List(FolderCollageItemMetadata_validator))
ContentTilesFolderMetadata.folder_contains_more_item.validator = bv.Boolean()
ContentTilesFolderMetadata.folder_contains_more_item.validator._redact = bv.BlotRedactor(None)
ContentTilesFolderMetadata.descendants_count.validator = bv.Int64()
ContentTilesFolderMetadata.descendants_count.validator._redact = bv.BlotRedactor(None)
ContentTilesFolderMetadata.folder_size.validator = bv.UInt64()
ContentTilesFolderMetadata.folder_size.validator._redact = bv.BlotRedactor(None)
ContentTilesFolderMetadata.folder_size_maybe_larger.validator = bv.Boolean()
ContentTilesFolderMetadata.folder_size_maybe_larger.validator._redact = bv.BlotRedactor(None)
ContentTilesFolderMetadata._all_field_names_ = set([
    'scrubbing_metadata',
    'folder_collage_metadata',
    'folder_contains_more_item',
    'descendants_count',
    'folder_size',
    'folder_size_maybe_larger'])
ContentTilesFolderMetadata._all_fields_ = [
    ('scrubbing_metadata', ContentTilesFolderMetadata.scrubbing_metadata.validator),
    ('folder_collage_metadata', ContentTilesFolderMetadata.folder_collage_metadata.validator),
    ('folder_contains_more_item', ContentTilesFolderMetadata.folder_contains_more_item.validator),
    ('descendants_count', ContentTilesFolderMetadata.descendants_count.validator),
    ('folder_size', ContentTilesFolderMetadata.folder_size.validator),
    ('folder_size_maybe_larger', ContentTilesFolderMetadata.folder_size_maybe_larger.validator)]
ContentTilesImageAnalysisMetadata.summary.validator = bv.String()
ContentTilesImageAnalysisMetadata.summary.validator._redact = bv.BlotRedactor(None)
ContentTilesImageAnalysisMetadata._all_field_names_ = set([
    'summary'])
ContentTilesImageAnalysisMetadata._all_fields_ = [
    ('summary', ContentTilesImageAnalysisMetadata.summary.validator)]
ContentTilesMetadata.fq_path.validator = bv.String()
ContentTilesMetadata.fq_path.validator._redact = bv.BlotRedactor(None)
ContentTilesMetadata.file_id.validator = bv.String()
ContentTilesMetadata.file_id.validator._redact = bv.BlotRedactor(None)
ContentTilesMetadata.metadata.validator = bv.Nullable(MetadataUnion_validator)
ContentTilesMetadata._all_field_names_ = set([
    'fq_path',
    'file_id',
    'metadata'])
ContentTilesMetadata._all_fields_ = [
    ('fq_path', ContentTilesMetadata.fq_path.validator),
    ('file_id', ContentTilesMetadata.file_id.validator),
    ('metadata', ContentTilesMetadata.metadata.validator)]
ContentTilesMetadataV2Arg.file_ids.validator = bv.Nullable(bv.List(bv.String()))
ContentTilesMetadataV2Arg.file_ids.validator._redact = bv.BlotRedactor(None)
ContentTilesMetadataV2Arg.retrieve_non_scrubbing.validator = bv.Boolean()
ContentTilesMetadataV2Arg.retrieve_non_scrubbing.validator._redact = bv.BlotRedactor(None)
ContentTilesMetadataV2Arg.video_scrubber_frame_count.validator = bv.UInt32()
ContentTilesMetadataV2Arg.video_scrubber_frame_count.validator._redact = bv.BlotRedactor(None)
ContentTilesMetadataV2Arg._all_field_names_ = set([
    'file_ids',
    'retrieve_non_scrubbing',
    'video_scrubber_frame_count'])
ContentTilesMetadataV2Arg._all_fields_ = [
    ('file_ids', ContentTilesMetadataV2Arg.file_ids.validator),
    ('retrieve_non_scrubbing', ContentTilesMetadataV2Arg.retrieve_non_scrubbing.validator),
    ('video_scrubber_frame_count', ContentTilesMetadataV2Arg.video_scrubber_frame_count.validator)]
ContentTilesMetadataV2Error.status.validator = ContentTilesMetadataV2ErrorStatus_validator
ContentTilesMetadataV2Error.err_message.validator = bv.String()
ContentTilesMetadataV2Error.err_message.validator._redact = bv.BlotRedactor(None)
ContentTilesMetadataV2Error._all_field_names_ = set([
    'status',
    'err_message'])
ContentTilesMetadataV2Error._all_fields_ = [
    ('status', ContentTilesMetadataV2Error.status.validator),
    ('err_message', ContentTilesMetadataV2Error.err_message.validator)]
ContentTilesMetadataV2ErrorStatus._ct_unknown_validator = bv.Void()
ContentTilesMetadataV2ErrorStatus._ct_file_ids_not_found_validator = bv.Void()
ContentTilesMetadataV2ErrorStatus._ct_metadata_error_validator = bv.Void()
ContentTilesMetadataV2ErrorStatus._other_validator = bv.Void()
ContentTilesMetadataV2ErrorStatus._tagmap = {
    'ct_unknown': ContentTilesMetadataV2ErrorStatus._ct_unknown_validator,
    'ct_file_ids_not_found': ContentTilesMetadataV2ErrorStatus._ct_file_ids_not_found_validator,
    'ct_metadata_error': ContentTilesMetadataV2ErrorStatus._ct_metadata_error_validator,
    'other': ContentTilesMetadataV2ErrorStatus._other_validator }
ContentTilesMetadataV2ErrorStatus.ct_unknown = ContentTilesMetadataV2ErrorStatus('ct_unknown')
ContentTilesMetadataV2ErrorStatus.ct_file_ids_not_found = ContentTilesMetadataV2ErrorStatus('ct_file_ids_not_found')
ContentTilesMetadataV2ErrorStatus.ct_metadata_error = ContentTilesMetadataV2ErrorStatus('ct_metadata_error')
ContentTilesMetadataV2ErrorStatus.other = ContentTilesMetadataV2ErrorStatus('other')
ContentTilesMetadataV2Result.metadata.validator = bv.Nullable(bv.List(ContentTilesMetadata_validator))
ContentTilesMetadataV2Result._all_field_names_ = set([
    'metadata'])
ContentTilesMetadataV2Result._all_fields_ = [
    ('metadata', ContentTilesMetadataV2Result.metadata.validator)]
ContentTilesPdfMetadata.scrubbing_metadata.validator = bv.Nullable(bv.List(ScrubbingItemMetadata_validator))
ContentTilesPdfMetadata._all_field_names_ = set([
    'scrubbing_metadata'])
ContentTilesPdfMetadata._all_fields_ = [
    ('scrubbing_metadata', ContentTilesPdfMetadata.scrubbing_metadata.validator)]
ContentTilesVideoMetadata.thumb_scrubber_vtt_url.validator = bv.String()
ContentTilesVideoMetadata.thumb_scrubber_vtt_url.validator._redact = bv.BlotRedactor(None)
ContentTilesVideoMetadata.duration.validator = bv.Int64()
ContentTilesVideoMetadata.duration.validator._redact = bv.BlotRedactor(None)
ContentTilesVideoMetadata.thumb_scrubber_vtt_width.validator = bv.UInt32()
ContentTilesVideoMetadata.thumb_scrubber_vtt_width.validator._redact = bv.BlotRedactor(None)
ContentTilesVideoMetadata.thumb_scrubber_vtt_height.validator = bv.UInt32()
ContentTilesVideoMetadata.thumb_scrubber_vtt_height.validator._redact = bv.BlotRedactor(None)
ContentTilesVideoMetadata._all_field_names_ = set([
    'thumb_scrubber_vtt_url',
    'duration',
    'thumb_scrubber_vtt_width',
    'thumb_scrubber_vtt_height'])
ContentTilesVideoMetadata._all_fields_ = [
    ('thumb_scrubber_vtt_url', ContentTilesVideoMetadata.thumb_scrubber_vtt_url.validator),
    ('duration', ContentTilesVideoMetadata.duration.validator),
    ('thumb_scrubber_vtt_width', ContentTilesVideoMetadata.thumb_scrubber_vtt_width.validator),
    ('thumb_scrubber_vtt_height', ContentTilesVideoMetadata.thumb_scrubber_vtt_height.validator)]
CreateFolderArg.path.validator = WritePath_validator
CreateFolderArg.autorename.validator = bv.Boolean()
CreateFolderArg.autorename.validator._redact = bv.BlotRedactor(None)
CreateFolderArg.fsw_request.validator = bv.Nullable(FswRequest_validator)
CreateFolderArg._all_field_names_ = set([
    'path',
    'autorename'])
CreateFolderArg._all_fields_ = [
    ('path', CreateFolderArg.path.validator),
    ('autorename', CreateFolderArg.autorename.validator)]
CreateFolderArg._all_internal_field_names_ = set([
    'fsw_request'])
CreateFolderArg._all_internal_fields_ = [
    ('fsw_request', CreateFolderArg.fsw_request.validator)]
CreateFolderBatchArg.paths.validator = bv.List(WritePath_validator, max_items = 10000)
CreateFolderBatchArg.autorename.validator = bv.Boolean()
CreateFolderBatchArg.autorename.validator._redact = bv.BlotRedactor(None)
CreateFolderBatchArg.force_async.validator = bv.Boolean()
CreateFolderBatchArg.force_async.validator._redact = bv.BlotRedactor(None)
CreateFolderBatchArg.fsw_request.validator = bv.Nullable(FswRequest_validator)
CreateFolderBatchArg.is_paper_migration.validator = bv.Boolean()
CreateFolderBatchArg.is_paper_migration.validator._redact = bv.BlotRedactor(None)
CreateFolderBatchArg._all_field_names_ = set([
    'paths',
    'autorename',
    'force_async'])
CreateFolderBatchArg._all_fields_ = [
    ('paths', CreateFolderBatchArg.paths.validator),
    ('autorename', CreateFolderBatchArg.autorename.validator),
    ('force_async', CreateFolderBatchArg.force_async.validator)]
CreateFolderBatchArg._all_internal_field_names_ = set([
    'fsw_request',
    'is_paper_migration'])
CreateFolderBatchArg._all_internal_fields_ = [
    ('fsw_request', CreateFolderBatchArg.fsw_request.validator),
    ('is_paper_migration', CreateFolderBatchArg.is_paper_migration.validator)]
CreateFolderBatchError._too_many_files_validator = bv.Void()
CreateFolderBatchError._other_validator = bv.Void()
CreateFolderBatchError._tagmap = {
    'too_many_files': CreateFolderBatchError._too_many_files_validator,
    'other': CreateFolderBatchError._other_validator }
CreateFolderBatchError.too_many_files = CreateFolderBatchError('too_many_files')
CreateFolderBatchError.other = CreateFolderBatchError('other')
CreateFolderBatchJobStatus._complete_validator = CreateFolderBatchResult_validator
CreateFolderBatchJobStatus._failed_validator = CreateFolderBatchError_validator
CreateFolderBatchJobStatus._other_validator = bv.Void()
CreateFolderBatchJobStatus._tagmap = {
    'complete': CreateFolderBatchJobStatus._complete_validator,
    'failed': CreateFolderBatchJobStatus._failed_validator,
    'other': CreateFolderBatchJobStatus._other_validator }
CreateFolderBatchJobStatus._tagmap.update(async_.PollResultBase._tagmap)
CreateFolderBatchJobStatus.other = CreateFolderBatchJobStatus('other')
CreateFolderBatchLaunch._complete_validator = CreateFolderBatchResult_validator
CreateFolderBatchLaunch._other_validator = bv.Void()
CreateFolderBatchLaunch._tagmap = {
    'complete': CreateFolderBatchLaunch._complete_validator,
    'other': CreateFolderBatchLaunch._other_validator }
CreateFolderBatchLaunch._tagmap.update(async_.LaunchResultBase._tagmap)
CreateFolderBatchLaunch.other = CreateFolderBatchLaunch('other')
FileOpsResult.changeset_data.validator = bv.List(ChangesetData_validator)
FileOpsResult._all_field_names_ = set([])
FileOpsResult._all_fields_ = []
FileOpsResult._all_internal_field_names_ = set([
    'changeset_data'])
FileOpsResult._all_internal_fields_ = [
    ('changeset_data', FileOpsResult.changeset_data.validator)]
CreateFolderBatchResult.entries.validator = bv.List(CreateFolderBatchResultEntry_validator)
CreateFolderBatchResult._all_field_names_ = FileOpsResult._all_field_names_.union(set([
    'entries']))
CreateFolderBatchResult._all_fields_ = FileOpsResult._all_fields_ + [
    ('entries', CreateFolderBatchResult.entries.validator)]
CreateFolderBatchResult._all_internal_field_names_ = FileOpsResult._all_internal_field_names_.union(set([]))
CreateFolderBatchResult._all_internal_fields_ = FileOpsResult._all_internal_fields_ + []
CreateFolderBatchResultEntry._success_validator = CreateFolderEntryResult_validator
CreateFolderBatchResultEntry._failure_validator = CreateFolderEntryError_validator
CreateFolderBatchResultEntry._tagmap = {
    'success': CreateFolderBatchResultEntry._success_validator,
    'failure': CreateFolderBatchResultEntry._failure_validator }
CreateFolderEntryError._path_validator = WriteError_validator
CreateFolderEntryError._other_validator = bv.Void()
CreateFolderEntryError._tagmap = {
    'path': CreateFolderEntryError._path_validator,
    'other': CreateFolderEntryError._other_validator }
CreateFolderEntryError.other = CreateFolderEntryError('other')
CreateFolderEntryResult.metadata.validator = FolderMetadata_validator
CreateFolderEntryResult._all_field_names_ = set([
    'metadata'])
CreateFolderEntryResult._all_fields_ = [
    ('metadata', CreateFolderEntryResult.metadata.validator)]
CreateFolderError._path_validator = WriteError_validator
CreateFolderError._tagmap = {
    'path': CreateFolderError._path_validator }
CreateFolderResult.metadata.validator = FolderMetadata_validator
CreateFolderResult._all_field_names_ = FileOpsResult._all_field_names_.union(set([
    'metadata']))
CreateFolderResult._all_fields_ = FileOpsResult._all_fields_ + [
    ('metadata', CreateFolderResult.metadata.validator)]
CreateFolderResult._all_internal_field_names_ = FileOpsResult._all_internal_field_names_.union(set([]))
CreateFolderResult._all_internal_fields_ = FileOpsResult._all_internal_fields_ + []
Cursor.type.validator = CursorType_validator
Cursor.value.validator = bv.String()
Cursor.value.validator._redact = bv.BlotRedactor(None)
Cursor._all_field_names_ = set([
    'type',
    'value'])
Cursor._all_fields_ = [
    ('type', Cursor.type.validator),
    ('value', Cursor.value.validator)]
CursorType._last_timestamp_millis_validator = bv.Void()
CursorType._other_validator = bv.Void()
CursorType._tagmap = {
    'last_timestamp_millis': CursorType._last_timestamp_millis_validator,
    'other': CursorType._other_validator }
CursorType.last_timestamp_millis = CursorType('last_timestamp_millis')
CursorType.other = CursorType('other')
DateRange.start_date_sec.validator = bv.Nullable(bv.Int64())
DateRange.end_date_sec.validator = bv.Nullable(bv.Int64())
DateRange._all_field_names_ = set([
    'start_date_sec',
    'end_date_sec'])
DateRange._all_fields_ = [
    ('start_date_sec', DateRange.start_date_sec.validator),
    ('end_date_sec', DateRange.end_date_sec.validator)]
DcsArgs.filters_json.validator = bv.Nullable(bv.String())
DcsArgs.query_options_json.validator = bv.Nullable(bv.String())
DcsArgs.search_vertical.validator = bv.String()
DcsArgs.search_vertical.validator._redact = bv.BlotRedactor(None)
DcsArgs.query_image_id.validator = bv.String()
DcsArgs.query_image_id.validator._redact = bv.BlotRedactor(None)
DcsArgs._all_field_names_ = set([])
DcsArgs._all_fields_ = []
DcsArgs._all_internal_field_names_ = set([
    'filters_json',
    'query_options_json',
    'search_vertical',
    'query_image_id'])
DcsArgs._all_internal_fields_ = [
    ('filters_json', DcsArgs.filters_json.validator),
    ('query_options_json', DcsArgs.query_options_json.validator),
    ('search_vertical', DcsArgs.search_vertical.validator),
    ('query_image_id', DcsArgs.query_image_id.validator)]
DeleteArg.path.validator = WritePathOrId_validator
DeleteArg.parent_rev.validator = bv.Nullable(Rev_validator)
DeleteArg.fsw_request.validator = bv.Nullable(FswRequest_validator)
DeleteArg._all_field_names_ = set([
    'path',
    'parent_rev'])
DeleteArg._all_fields_ = [
    ('path', DeleteArg.path.validator),
    ('parent_rev', DeleteArg.parent_rev.validator)]
DeleteArg._all_internal_field_names_ = set([
    'fsw_request'])
DeleteArg._all_internal_fields_ = [
    ('fsw_request', DeleteArg.fsw_request.validator)]
DeleteBatchArg.entries.validator = bv.List(DeleteArg_validator, max_items = 1000)
DeleteBatchArg.fsw_request.validator = bv.Nullable(FswRequest_validator)
DeleteBatchArg._all_field_names_ = set([
    'entries'])
DeleteBatchArg._all_fields_ = [
    ('entries', DeleteBatchArg.entries.validator)]
DeleteBatchArg._all_internal_field_names_ = set([
    'fsw_request'])
DeleteBatchArg._all_internal_fields_ = [
    ('fsw_request', DeleteBatchArg.fsw_request.validator)]
DeleteBatchError._too_many_write_operations_validator = bv.Void()
DeleteBatchError._path_validator = WriteError_validator
DeleteBatchError._other_validator = bv.Void()
DeleteBatchError._permissioned_tagmaps = {
    'internal'}
DeleteBatchError._tagmap = {
    'too_many_write_operations': DeleteBatchError._too_many_write_operations_validator,
    'other': DeleteBatchError._other_validator }
DeleteBatchError._internal_tagmap = {
    'path': DeleteBatchError._path_validator }
DeleteBatchError.too_many_write_operations = DeleteBatchError('too_many_write_operations')
DeleteBatchError.other = DeleteBatchError('other')
DeleteBatchJobStatus._complete_validator = DeleteBatchResult_validator
DeleteBatchJobStatus._failed_validator = DeleteBatchError_validator
DeleteBatchJobStatus._other_validator = bv.Void()
DeleteBatchJobStatus._tagmap = {
    'complete': DeleteBatchJobStatus._complete_validator,
    'failed': DeleteBatchJobStatus._failed_validator,
    'other': DeleteBatchJobStatus._other_validator }
DeleteBatchJobStatus._tagmap.update(async_.PollResultBase._tagmap)
DeleteBatchJobStatus.other = DeleteBatchJobStatus('other')
DeleteBatchLaunch._complete_validator = DeleteBatchResult_validator
DeleteBatchLaunch._other_validator = bv.Void()
DeleteBatchLaunch._tagmap = {
    'complete': DeleteBatchLaunch._complete_validator,
    'other': DeleteBatchLaunch._other_validator }
DeleteBatchLaunch._tagmap.update(async_.LaunchResultBase._tagmap)
DeleteBatchLaunch.other = DeleteBatchLaunch('other')
DeleteBatchResult.entries.validator = bv.List(DeleteBatchResultEntry_validator)
DeleteBatchResult._all_field_names_ = FileOpsResult._all_field_names_.union(set([
    'entries']))
DeleteBatchResult._all_fields_ = FileOpsResult._all_fields_ + [
    ('entries', DeleteBatchResult.entries.validator)]
DeleteBatchResult._all_internal_field_names_ = FileOpsResult._all_internal_field_names_.union(set([]))
DeleteBatchResult._all_internal_fields_ = FileOpsResult._all_internal_fields_ + []
DeleteBatchResultData.metadata.validator = Metadata_validator
DeleteBatchResultData._all_field_names_ = set([
    'metadata'])
DeleteBatchResultData._all_fields_ = [
    ('metadata', DeleteBatchResultData.metadata.validator)]
DeleteBatchResultEntry._success_validator = DeleteBatchResultData_validator
DeleteBatchResultEntry._failure_validator = DeleteError_validator
DeleteBatchResultEntry._tagmap = {
    'success': DeleteBatchResultEntry._success_validator,
    'failure': DeleteBatchResultEntry._failure_validator }
DeleteError._path_lookup_validator = LookupError_validator
DeleteError._path_write_validator = WriteError_validator
DeleteError._too_many_write_operations_validator = bv.Void()
DeleteError._too_many_files_validator = bv.Void()
DeleteError._xop_wait_timeout_validator = bv.Void()
DeleteError._other_validator = bv.Void()
DeleteError._permissioned_tagmaps = {
    'internal'}
DeleteError._tagmap = {
    'path_lookup': DeleteError._path_lookup_validator,
    'path_write': DeleteError._path_write_validator,
    'too_many_write_operations': DeleteError._too_many_write_operations_validator,
    'too_many_files': DeleteError._too_many_files_validator,
    'other': DeleteError._other_validator }
DeleteError._internal_tagmap = {
    'xop_wait_timeout': DeleteError._xop_wait_timeout_validator }
DeleteError.too_many_write_operations = DeleteError('too_many_write_operations')
DeleteError.too_many_files = DeleteError('too_many_files')
DeleteError.xop_wait_timeout = DeleteError('xop_wait_timeout')
DeleteError.other = DeleteError('other')
DeleteResult.metadata.validator = Metadata_validator
DeleteResult._all_field_names_ = FileOpsResult._all_field_names_.union(set([
    'metadata']))
DeleteResult._all_fields_ = FileOpsResult._all_fields_ + [
    ('metadata', DeleteResult.metadata.validator)]
DeleteResult._all_internal_field_names_ = FileOpsResult._all_internal_field_names_.union(set([]))
DeleteResult._all_internal_fields_ = FileOpsResult._all_internal_fields_ + []
Metadata.name.validator = bv.String()
Metadata.name.validator._redact = bv.BlotRedactor(None)
Metadata.path_lower.validator = bv.Nullable(bv.String())
Metadata.path_lower.validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
Metadata.path_display.validator = bv.Nullable(bv.String())
Metadata.path_display.validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
Metadata.parent_shared_folder_id.validator = bv.Nullable(common.SharedFolderId_validator)
Metadata.preview_url.validator = bv.Nullable(bv.String())
Metadata.preview_url.validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
Metadata._field_names_ = set([
    'name',
    'path_lower',
    'path_display',
    'parent_shared_folder_id',
    'preview_url'])
Metadata._all_field_names_ = Metadata._field_names_
Metadata._fields_ = [
    ('name', Metadata.name.validator),
    ('path_lower', Metadata.path_lower.validator),
    ('path_display', Metadata.path_display.validator),
    ('parent_shared_folder_id', Metadata.parent_shared_folder_id.validator),
    ('preview_url', Metadata.preview_url.validator)]
Metadata._all_fields_ = Metadata._fields_
Metadata._tag_to_subtype_ = {
    ('file',): FileMetadata_validator,
    ('folder',): FolderMetadata_validator,
    ('deleted',): DeletedMetadata_validator }
Metadata._pytype_to_tag_and_subtype_ = {
    DeletedMetadata: (('deleted',), DeletedMetadata_validator),
    FolderMetadata: (('folder',), FolderMetadata_validator),
    FileMetadata: (('file',), FileMetadata_validator) }
Metadata._is_catch_all_ = False
DeletedMetadata.is_restorable.validator = bv.Nullable(bv.Boolean())
DeletedMetadata.is_dir.validator = bv.Boolean()
DeletedMetadata.is_dir.validator._redact = bv.BlotRedactor(None)
DeletedMetadata.client_modified.validator = bv.Nullable(common.DropboxTimestamp_validator)
DeletedMetadata._field_names_ = set([
    'is_restorable'])
DeletedMetadata._all_field_names_ = Metadata._all_field_names_.union(DeletedMetadata._field_names_)
DeletedMetadata._fields_ = [
    ('is_restorable', DeletedMetadata.is_restorable.validator)]
DeletedMetadata._all_fields_ = Metadata._all_fields_ + DeletedMetadata._fields_
DeletedMetadata._internal_field_names_ = set([
    'is_dir',
    'client_modified'])
DeletedMetadata._all_internal_field_names_ = DeletedMetadata._internal_field_names_
DeletedMetadata._internal_fields_ = [
    ('is_dir', DeletedMetadata.is_dir.validator),
    ('client_modified', DeletedMetadata.client_modified.validator)]
DeletedMetadata._all_internal_fields_ = DeletedMetadata._internal_fields_
DeletedNsidInfo.ns_id.validator = bv.UInt64()
DeletedNsidInfo.ns_id.validator._redact = bv.BlotRedactor(None)
DeletedNsidInfo.permanent_delete_is_disabled.validator = bv.Boolean()
DeletedNsidInfo.permanent_delete_is_disabled.validator._redact = bv.BlotRedactor(None)
DeletedNsidInfo._all_field_names_ = set([
    'ns_id',
    'permanent_delete_is_disabled'])
DeletedNsidInfo._all_fields_ = [
    ('ns_id', DeletedNsidInfo.ns_id.validator),
    ('permanent_delete_is_disabled', DeletedNsidInfo.permanent_delete_is_disabled.validator)]
DeletedRootOidInfo.root_oid.validator = bv.Nullable(version_tree.Oid_validator)
DeletedRootOidInfo.permanent_delete_is_disabled.validator = bv.Boolean()
DeletedRootOidInfo.permanent_delete_is_disabled.validator._redact = bv.BlotRedactor(None)
DeletedRootOidInfo._all_field_names_ = set([
    'root_oid',
    'permanent_delete_is_disabled'])
DeletedRootOidInfo._all_fields_ = [
    ('root_oid', DeletedRootOidInfo.root_oid.validator),
    ('permanent_delete_is_disabled', DeletedRootOidInfo.permanent_delete_is_disabled.validator)]
DialogInfoError.title.validator = bv.String()
DialogInfoError.title.validator._redact = bv.BlotRedactor(None)
DialogInfoError.text.validator = bv.String()
DialogInfoError.text.validator._redact = bv.BlotRedactor(None)
DialogInfoError.learn_more.validator = bv.String()
DialogInfoError.learn_more.validator._redact = bv.BlotRedactor(None)
DialogInfoError.confirm_text.validator = bv.Nullable(bv.String())
DialogInfoError._all_field_names_ = set([
    'title',
    'text',
    'learn_more',
    'confirm_text'])
DialogInfoError._all_fields_ = [
    ('title', DialogInfoError.title.validator),
    ('text', DialogInfoError.text.validator),
    ('learn_more', DialogInfoError.learn_more.validator),
    ('confirm_text', DialogInfoError.confirm_text.validator)]
Dimension._small_validator = bv.Void()
Dimension._medium_validator = bv.Void()
Dimension._large_validator = bv.Void()
Dimension._extra_large_validator = bv.Void()
Dimension._other_validator = bv.Void()
Dimension._tagmap = {
    'small': Dimension._small_validator,
    'medium': Dimension._medium_validator,
    'large': Dimension._large_validator,
    'extra_large': Dimension._extra_large_validator,
    'other': Dimension._other_validator }
Dimension.small = Dimension('small')
Dimension.medium = Dimension('medium')
Dimension.large = Dimension('large')
Dimension.extra_large = Dimension('extra_large')
Dimension.other = Dimension('other')
Dimensions.height.validator = bv.UInt64()
Dimensions.height.validator._redact = bv.BlotRedactor(None)
Dimensions.width.validator = bv.UInt64()
Dimensions.width.validator._redact = bv.BlotRedactor(None)
Dimensions._all_field_names_ = set([
    'height',
    'width'])
Dimensions._all_fields_ = [
    ('height', Dimensions.height.validator),
    ('width', Dimensions.width.validator)]
DownloadArg.path.validator = ReadPath_validator
DownloadArg.rev.validator = bv.Nullable(Rev_validator)
DownloadArg._all_field_names_ = set([
    'path',
    'rev'])
DownloadArg._all_fields_ = [
    ('path', DownloadArg.path.validator),
    ('rev', DownloadArg.rev.validator)]
DownloadError._path_validator = LookupError_validator
DownloadError._unsupported_file_validator = bv.Void()
DownloadError._other_validator = bv.Void()
DownloadError._tagmap = {
    'path': DownloadError._path_validator,
    'unsupported_file': DownloadError._unsupported_file_validator,
    'other': DownloadError._other_validator }
DownloadError.unsupported_file = DownloadError('unsupported_file')
DownloadError.other = DownloadError('other')
DownloadZipArg.path.validator = ReadPath_validator
DownloadZipArg._all_field_names_ = set([
    'path'])
DownloadZipArg._all_fields_ = [
    ('path', DownloadZipArg.path.validator)]
DownloadZipError._path_validator = LookupError_validator
DownloadZipError._too_large_validator = bv.Void()
DownloadZipError._too_many_files_validator = bv.Void()
DownloadZipError._other_validator = bv.Void()
DownloadZipError._tagmap = {
    'path': DownloadZipError._path_validator,
    'too_large': DownloadZipError._too_large_validator,
    'too_many_files': DownloadZipError._too_many_files_validator,
    'other': DownloadZipError._other_validator }
DownloadZipError.too_large = DownloadZipError('too_large')
DownloadZipError.too_many_files = DownloadZipError('too_many_files')
DownloadZipError.other = DownloadZipError('other')
DownloadZipResult.metadata.validator = FolderMetadata_validator
DownloadZipResult._all_field_names_ = set([
    'metadata'])
DownloadZipResult._all_fields_ = [
    ('metadata', DownloadZipResult.metadata.validator)]
ExportArg.path.validator = ReadPath_validator
ExportArg.export_format.validator = bv.Nullable(bv.String())
ExportArg._all_field_names_ = set([
    'path',
    'export_format'])
ExportArg._all_fields_ = [
    ('path', ExportArg.path.validator),
    ('export_format', ExportArg.export_format.validator)]
ExportError._path_validator = LookupError_validator
ExportError._non_exportable_validator = bv.Void()
ExportError._invalid_export_format_validator = bv.Void()
ExportError._retry_error_validator = bv.Void()
ExportError._other_validator = bv.Void()
ExportError._tagmap = {
    'path': ExportError._path_validator,
    'non_exportable': ExportError._non_exportable_validator,
    'invalid_export_format': ExportError._invalid_export_format_validator,
    'retry_error': ExportError._retry_error_validator,
    'other': ExportError._other_validator }
ExportError.non_exportable = ExportError('non_exportable')
ExportError.invalid_export_format = ExportError('invalid_export_format')
ExportError.retry_error = ExportError('retry_error')
ExportError.other = ExportError('other')
ExportInfo.export_as.validator = bv.Nullable(bv.String())
ExportInfo.export_options.validator = bv.Nullable(bv.List(bv.String()))
ExportInfo.export_options.validator._redact = bv.BlotRedactor(None)
ExportInfo._all_field_names_ = set([
    'export_as',
    'export_options'])
ExportInfo._all_fields_ = [
    ('export_as', ExportInfo.export_as.validator),
    ('export_options', ExportInfo.export_options.validator)]
ExportMetadata.name.validator = bv.String()
ExportMetadata.name.validator._redact = bv.BlotRedactor(None)
ExportMetadata.size.validator = bv.UInt64()
ExportMetadata.size.validator._redact = bv.BlotRedactor(None)
ExportMetadata.export_hash.validator = bv.Nullable(Sha256HexHash_validator)
ExportMetadata.paper_revision.validator = bv.Nullable(bv.Int64())
ExportMetadata._all_field_names_ = set([
    'name',
    'size',
    'export_hash',
    'paper_revision'])
ExportMetadata._all_fields_ = [
    ('name', ExportMetadata.name.validator),
    ('size', ExportMetadata.size.validator),
    ('export_hash', ExportMetadata.export_hash.validator),
    ('paper_revision', ExportMetadata.paper_revision.validator)]
ExportResult.export_metadata.validator = ExportMetadata_validator
ExportResult.file_metadata.validator = FileMetadata_validator
ExportResult._all_field_names_ = set([
    'export_metadata',
    'file_metadata'])
ExportResult._all_fields_ = [
    ('export_metadata', ExportResult.export_metadata.validator),
    ('file_metadata', ExportResult.file_metadata.validator)]
ExtendedMetadata._metadata_validator = Metadata_validator
ExtendedMetadata._paper_validator = PaperMetadata_validator
ExtendedMetadata._shared_with_me_file_validator = SharedWithMeFileMetadata_validator
ExtendedMetadata._other_validator = bv.Void()
ExtendedMetadata._tagmap = {
    'metadata': ExtendedMetadata._metadata_validator,
    'paper': ExtendedMetadata._paper_validator,
    'shared_with_me_file': ExtendedMetadata._shared_with_me_file_validator,
    'other': ExtendedMetadata._other_validator }
ExtendedMetadata.other = ExtendedMetadata('other')
ExtendedSearchMatch.match_type.validator = SearchMatchType_validator
ExtendedSearchMatch.extended_metadata.validator = ExtendedMetadata_validator
ExtendedSearchMatch.highlight_spans.validator = bv.Nullable(bv.List(HighlightSpan_validator))
ExtendedSearchMatch._all_field_names_ = set([
    'match_type',
    'extended_metadata',
    'highlight_spans'])
ExtendedSearchMatch._all_fields_ = [
    ('match_type', ExtendedSearchMatch.match_type.validator),
    ('extended_metadata', ExtendedSearchMatch.extended_metadata.validator),
    ('highlight_spans', ExtendedSearchMatch.highlight_spans.validator)]
ExtendedSearchResult.matches.validator = bv.List(ExtendedSearchMatch_validator)
ExtendedSearchResult.more.validator = bv.Boolean()
ExtendedSearchResult.more.validator._redact = bv.BlotRedactor(None)
ExtendedSearchResult.start.validator = bv.UInt64()
ExtendedSearchResult.start.validator._redact = bv.BlotRedactor(None)
ExtendedSearchResult._all_field_names_ = set([
    'matches',
    'more',
    'start'])
ExtendedSearchResult._all_fields_ = [
    ('matches', ExtendedSearchResult.matches.validator),
    ('more', ExtendedSearchResult.more.validator),
    ('start', ExtendedSearchResult.start.validator)]
Fsw.details_json.validator = bv.String()
Fsw.details_json.validator._redact = bv.BlotRedactor(None)
Fsw._all_field_names_ = set([
    'details_json'])
Fsw._all_fields_ = [
    ('details_json', Fsw.details_json.validator)]
FswDialogInfoError.id.validator = bv.String()
FswDialogInfoError.id.validator._redact = bv.BlotRedactor(None)
FswDialogInfoError.blocking.validator = bv.Boolean()
FswDialogInfoError.blocking.validator._redact = bv.BlotRedactor(None)
FswDialogInfoError._all_field_names_ = DialogInfoError._all_field_names_.union(set([
    'id',
    'blocking']))
FswDialogInfoError._all_fields_ = DialogInfoError._all_fields_ + [
    ('id', FswDialogInfoError.id.validator),
    ('blocking', FswDialogInfoError.blocking.validator)]
FswRequest._check_validator = bv.Void()
FswRequest._confirm_validator = bv.List(bv.String())
FswRequest._other_validator = bv.Void()
FswRequest._tagmap = {
    'check': FswRequest._check_validator,
    'confirm': FswRequest._confirm_validator,
    'other': FswRequest._other_validator }
FswRequest.check = FswRequest('check')
FswRequest.other = FswRequest('other')
FileCategory._image_validator = bv.Void()
FileCategory._document_validator = bv.Void()
FileCategory._pdf_validator = bv.Void()
FileCategory._spreadsheet_validator = bv.Void()
FileCategory._presentation_validator = bv.Void()
FileCategory._audio_validator = bv.Void()
FileCategory._video_validator = bv.Void()
FileCategory._folder_validator = bv.Void()
FileCategory._paper_validator = bv.Void()
FileCategory._others_validator = bv.Void()
FileCategory._other_validator = bv.Void()
FileCategory._tagmap = {
    'image': FileCategory._image_validator,
    'document': FileCategory._document_validator,
    'pdf': FileCategory._pdf_validator,
    'spreadsheet': FileCategory._spreadsheet_validator,
    'presentation': FileCategory._presentation_validator,
    'audio': FileCategory._audio_validator,
    'video': FileCategory._video_validator,
    'folder': FileCategory._folder_validator,
    'paper': FileCategory._paper_validator,
    'others': FileCategory._others_validator,
    'other': FileCategory._other_validator }
FileCategory.image = FileCategory('image')
FileCategory.document = FileCategory('document')
FileCategory.pdf = FileCategory('pdf')
FileCategory.spreadsheet = FileCategory('spreadsheet')
FileCategory.presentation = FileCategory('presentation')
FileCategory.audio = FileCategory('audio')
FileCategory.video = FileCategory('video')
FileCategory.folder = FileCategory('folder')
FileCategory.paper = FileCategory('paper')
FileCategory.others = FileCategory('others')
FileCategory.other = FileCategory('other')
FileContent.file_id.validator = bv.String()
FileContent.file_id.validator._redact = bv.BlotRedactor(None)
FileContent.content.validator = bv.String()
FileContent.content.validator._redact = bv.BlotRedactor(None)
FileContent.found.validator = bv.Boolean()
FileContent.found.validator._redact = bv.BlotRedactor(None)
FileContent.text_backfill_enqueued.validator = bv.Boolean()
FileContent.text_backfill_enqueued.validator._redact = bv.BlotRedactor(None)
FileContent.not_found_reason.validator = FileContentNotFoundReason_validator
FileContent._all_field_names_ = set([
    'file_id',
    'content',
    'found',
    'text_backfill_enqueued',
    'not_found_reason'])
FileContent._all_fields_ = [
    ('file_id', FileContent.file_id.validator),
    ('content', FileContent.content.validator),
    ('found', FileContent.found.validator),
    ('text_backfill_enqueued', FileContent.text_backfill_enqueued.validator),
    ('not_found_reason', FileContent.not_found_reason.validator)]
FileContentNotFoundReason._file_content_not_found_reason_unspecified_validator = bv.Void()
FileContentNotFoundReason._file_content_not_found_reason_not_indexed_validator = bv.Void()
FileContentNotFoundReason._file_content_not_found_reason_file_missing_validator = bv.Void()
FileContentNotFoundReason._file_content_not_found_reason_lookup_failed_validator = bv.Void()
FileContentNotFoundReason._other_validator = bv.Void()
FileContentNotFoundReason._tagmap = {
    'file_content_not_found_reason_unspecified': FileContentNotFoundReason._file_content_not_found_reason_unspecified_validator,
    'file_content_not_found_reason_not_indexed': FileContentNotFoundReason._file_content_not_found_reason_not_indexed_validator,
    'file_content_not_found_reason_file_missing': FileContentNotFoundReason._file_content_not_found_reason_file_missing_validator,
    'file_content_not_found_reason_lookup_failed': FileContentNotFoundReason._file_content_not_found_reason_lookup_failed_validator,
    'other': FileContentNotFoundReason._other_validator }
FileContentNotFoundReason.file_content_not_found_reason_unspecified = FileContentNotFoundReason('file_content_not_found_reason_unspecified')
FileContentNotFoundReason.file_content_not_found_reason_not_indexed = FileContentNotFoundReason('file_content_not_found_reason_not_indexed')
FileContentNotFoundReason.file_content_not_found_reason_file_missing = FileContentNotFoundReason('file_content_not_found_reason_file_missing')
FileContentNotFoundReason.file_content_not_found_reason_lookup_failed = FileContentNotFoundReason('file_content_not_found_reason_lookup_failed')
FileContentNotFoundReason.other = FileContentNotFoundReason('other')
FileEncryptionInfoMissingEncryptionError.existing_file_key_id.validator = bv.Nullable(bv.String())
FileEncryptionInfoMissingEncryptionError.ns_id.validator = bv.String()
FileEncryptionInfoMissingEncryptionError.ns_id.validator._redact = bv.BlotRedactor(None)
FileEncryptionInfoMissingEncryptionError._all_field_names_ = set([])
FileEncryptionInfoMissingEncryptionError._all_fields_ = []
FileEncryptionInfoMissingEncryptionError._all_internal_field_names_ = set([
    'existing_file_key_id',
    'ns_id'])
FileEncryptionInfoMissingEncryptionError._all_internal_fields_ = [
    ('existing_file_key_id', FileEncryptionInfoMissingEncryptionError.existing_file_key_id.validator),
    ('ns_id', FileEncryptionInfoMissingEncryptionError.ns_id.validator)]
FileIdentifier._fq_path_validator = bv.String()
FileIdentifier._fq_path_validator._redact = bv.BlotRedactor(None)
FileIdentifier._other_validator = bv.Void()
FileIdentifier._tagmap = {
    'fq_path': FileIdentifier._fq_path_validator,
    'other': FileIdentifier._other_validator }
FileIdentifier.other = FileIdentifier('other')
FileInfo.direct_blockserver_link.validator = bv.String()
FileInfo.direct_blockserver_link.validator._redact = bv.BlotRedactor(None)
FileInfo.ext.validator = bv.String()
FileInfo.ext.validator._redact = bv.BlotRedactor(None)
FileInfo.file_id.validator = bv.String()
FileInfo.file_id.validator._redact = bv.BlotRedactor(None)
FileInfo.fq_path.validator = bv.String()
FileInfo.fq_path.validator._redact = bv.BlotRedactor(None)
FileInfo.href.validator = bv.String()
FileInfo.href.validator._redact = bv.BlotRedactor(None)
FileInfo.icon.validator = bv.String()
FileInfo.icon.validator._redact = bv.BlotRedactor(None)
FileInfo.is_cloud_doc.validator = bv.Boolean()
FileInfo.is_cloud_doc.validator._redact = bv.BlotRedactor(None)
FileInfo.is_dir.validator = bv.Boolean()
FileInfo.is_dir.validator._redact = bv.BlotRedactor(None)
FileInfo.is_in_team_folder_tree.validator = bv.Boolean()
FileInfo.is_in_team_folder_tree.validator._redact = bv.BlotRedactor(None)
FileInfo.is_symlink.validator = bv.Boolean()
FileInfo.is_symlink.validator._redact = bv.BlotRedactor(None)
FileInfo.is_unmounted.validator = bv.Boolean()
FileInfo.is_unmounted.validator._redact = bv.BlotRedactor(None)
FileInfo.last_modified_name.validator = bv.String()
FileInfo.last_modified_name.validator._redact = bv.BlotRedactor(None)
FileInfo.mount_access_perms.validator = bv.Nullable(bv.List(bv.String()))
FileInfo.mount_access_perms.validator._redact = bv.BlotRedactor(None)
FileInfo.ns_id.validator = bv.UInt64()
FileInfo.ns_id.validator._redact = bv.BlotRedactor(None)
FileInfo.ns_path.validator = bv.String()
FileInfo.ns_path.validator._redact = bv.BlotRedactor(None)
FileInfo.read_only.validator = bv.Boolean()
FileInfo.read_only.validator._redact = bv.BlotRedactor(None)
FileInfo.revision_id.validator = bv.String()
FileInfo.revision_id.validator._redact = bv.BlotRedactor(None)
FileInfo.size_bytes.validator = bv.Int64()
FileInfo.size_bytes.validator._redact = bv.BlotRedactor(None)
FileInfo.sjid.validator = bv.UInt64()
FileInfo.sjid.validator._redact = bv.BlotRedactor(None)
FileInfo.deprecated_sort_key.validator = bv.Nullable(bv.List(bv.String()))
FileInfo.deprecated_sort_key.validator._redact = bv.BlotRedactor(None)
FileInfo.target_ns.validator = bv.UInt64()
FileInfo.target_ns.validator._redact = bv.BlotRedactor(None)
FileInfo.thumbnail_url_tmpl.validator = bv.String()
FileInfo.thumbnail_url_tmpl.validator._redact = bv.BlotRedactor(None)
FileInfo.ts.validator = bv.Int64()
FileInfo.ts.validator._redact = bv.BlotRedactor(None)
FileInfo.type.validator = FileType_validator
FileInfo.sort_key.validator = bv.String()
FileInfo.sort_key.validator._redact = bv.BlotRedactor(None)
FileInfo.has_mount_access_perms.validator = bv.Boolean()
FileInfo.has_mount_access_perms.validator._redact = bv.BlotRedactor(None)
FileInfo.open_to_url.validator = bv.String()
FileInfo.open_to_url.validator._redact = bv.BlotRedactor(None)
FileInfo.is_locked.validator = bv.Boolean()
FileInfo.is_locked.validator._redact = bv.BlotRedactor(None)
FileInfo.lock_info.validator = bv.Nullable(FileLockInfo_validator)
FileInfo.per_node_metadata.validator = bv.Nullable(per_node_metadata.PerNodeMetadataEntity_validator)
FileInfo.is_in_vault_folder.validator = bv.Boolean()
FileInfo.is_in_vault_folder.validator._redact = bv.BlotRedactor(None)
FileInfo.has_automated_rule.validator = bv.Boolean()
FileInfo.has_automated_rule.validator._redact = bv.BlotRedactor(None)
FileInfo.is_backup_folder.validator = bv.Boolean()
FileInfo.is_backup_folder.validator._redact = bv.BlotRedactor(None)
FileInfo.modified_ago.validator = bv.String()
FileInfo.modified_ago.validator._redact = bv.BlotRedactor(None)
FileInfo.ago_from_last_action_by_user_ts.validator = bv.String()
FileInfo.ago_from_last_action_by_user_ts.validator._redact = bv.BlotRedactor(None)
FileInfo.preview.validator = bv.Nullable(file_viewer_preview_metadata.PreviewMetadata_validator)
FileInfo.is_in_backup_folder.validator = bv.Boolean()
FileInfo.is_in_backup_folder.validator._redact = bv.BlotRedactor(None)
FileInfo.recents_info.validator = bv.Nullable(RecentsInfo_validator)
FileInfo.descendants_count.validator = bv.Int64()
FileInfo.descendants_count.validator._redact = bv.BlotRedactor(None)
FileInfo.browse_preview.validator = bv.Nullable(file_viewer_preview_metadata.PreviewMetadata_validator)
FileInfo.content_tile_metadata.validator = bv.Nullable(ContentTileMetadata_validator)
FileInfo.is_encrypted.validator = bv.Boolean()
FileInfo.is_encrypted.validator._redact = bv.BlotRedactor(None)
FileInfo.file_encryption_info.validator = bv.Nullable(encryption.EncryptedFile_validator)
FileInfo.file_owner_team_encrypted_id.validator = bv.String()
FileInfo.file_owner_team_encrypted_id.validator._redact = bv.BlotRedactor(None)
FileInfo.oid.validator = bv.String()
FileInfo.oid.validator._redact = bv.BlotRedactor(None)
FileInfo.hlc.validator = bv.String()
FileInfo.hlc.validator._redact = bv.BlotRedactor(None)
FileInfo.starred_status.validator = StarredStatus_validator
FileInfo.folder_size.validator = bv.UInt64()
FileInfo.folder_size.validator._redact = bv.BlotRedactor(None)
FileInfo.folder_size_maybe_larger.validator = bv.Boolean()
FileInfo.folder_size_maybe_larger.validator._redact = bv.BlotRedactor(None)
FileInfo._all_field_names_ = set([
    'direct_blockserver_link',
    'ext',
    'file_id',
    'fq_path',
    'href',
    'icon',
    'is_cloud_doc',
    'is_dir',
    'is_in_team_folder_tree',
    'is_symlink',
    'is_unmounted',
    'last_modified_name',
    'mount_access_perms',
    'ns_id',
    'ns_path',
    'read_only',
    'revision_id',
    'size_bytes',
    'sjid',
    'deprecated_sort_key',
    'target_ns',
    'thumbnail_url_tmpl',
    'ts',
    'type',
    'sort_key',
    'has_mount_access_perms',
    'open_to_url',
    'is_locked',
    'lock_info',
    'per_node_metadata',
    'is_in_vault_folder',
    'has_automated_rule',
    'is_backup_folder',
    'modified_ago',
    'ago_from_last_action_by_user_ts',
    'preview',
    'is_in_backup_folder',
    'recents_info',
    'descendants_count',
    'browse_preview',
    'content_tile_metadata',
    'is_encrypted',
    'file_encryption_info',
    'file_owner_team_encrypted_id',
    'oid',
    'hlc',
    'starred_status',
    'folder_size',
    'folder_size_maybe_larger'])
FileInfo._all_fields_ = [][('direct_blockserver_link', FileInfo.direct_blockserver_link.validator)][('ext', FileInfo.ext.validator)][('file_id', FileInfo.file_id.validator)][('fq_path', FileInfo.fq_path.validator)][('href', FileInfo.href.validator)][('icon', FileInfo.icon.validator)][('is_cloud_doc', FileInfo.is_cloud_doc.validator)][('is_dir', FileInfo.is_dir.validator)][('is_in_team_folder_tree', FileInfo.is_in_team_folder_tree.validator)][('is_symlink', FileInfo.is_symlink.validator)][('is_unmounted', FileInfo.is_unmounted.validator)][('last_modified_name', FileInfo.last_modified_name.validator)][('mount_access_perms', FileInfo.mount_access_perms.validator)][('ns_id', FileInfo.ns_id.validator)][('ns_path', FileInfo.ns_path.validator)][('read_only', FileInfo.read_only.validator)][('revision_id', FileInfo.revision_id.validator)][('size_bytes', FileInfo.size_bytes.validator)][('sjid', FileInfo.sjid.validator)][('deprecated_sort_key', FileInfo.deprecated_sort_key.validator)][('target_ns', FileInfo.target_ns.validator)][('thumbnail_url_tmpl', FileInfo.thumbnail_url_tmpl.validator)][('ts', FileInfo.ts.validator)][('type', FileInfo.type.validator)][('sort_key', FileInfo.sort_key.validator)][('has_mount_access_perms', FileInfo.has_mount_access_perms.validator)][('open_to_url', FileInfo.open_to_url.validator)][('is_locked', FileInfo.is_locked.validator)][('lock_info', FileInfo.lock_info.validator)][('per_node_metadata', FileInfo.per_node_metadata.validator)][('is_in_vault_folder', FileInfo.is_in_vault_folder.validator)][('has_automated_rule', FileInfo.has_automated_rule.validator)][('is_backup_folder', FileInfo.is_backup_folder.validator)][('modified_ago', FileInfo.modified_ago.validator)][('ago_from_last_action_by_user_ts', FileInfo.ago_from_last_action_by_user_ts.validator)][('preview', FileInfo.preview.validator)][('is_in_backup_folder', FileInfo.is_in_backup_folder.validator)][('recents_info', FileInfo.recents_info.validator)][('descendants_count', FileInfo.descendants_count.validator)][('browse_preview', FileInfo.browse_preview.validator)][('content_tile_metadata', FileInfo.content_tile_metadata.validator)][('is_encrypted', FileInfo.is_encrypted.validator)][('file_encryption_info', FileInfo.file_encryption_info.validator)][('file_owner_team_encrypted_id', FileInfo.file_owner_team_encrypted_id.validator)][('oid', FileInfo.oid.validator)][('hlc', FileInfo.hlc.validator)][('starred_status', FileInfo.starred_status.validator)][('folder_size', FileInfo.folder_size.validator)][('folder_size_maybe_larger', FileInfo.folder_size_maybe_larger.validator)]
FileLock.content.validator = FileLockContent_validator
FileLock._all_field_names_ = set([
    'content'])
FileLock._all_fields_ = [
    ('content', FileLock.content.validator)]
FileLockContent._unlocked_validator = bv.Void()
FileLockContent._single_user_validator = SingleUserLock_validator
FileLockContent._other_validator = bv.Void()
FileLockContent._tagmap = {
    'unlocked': FileLockContent._unlocked_validator,
    'single_user': FileLockContent._single_user_validator,
    'other': FileLockContent._other_validator }
FileLockContent.unlocked = FileLockContent('unlocked')
FileLockContent.other = FileLockContent('other')
FileLockInfo.is_lockholder.validator = bv.Boolean()
FileLockInfo.is_lockholder.validator._redact = bv.BlotRedactor(None)
FileLockInfo.lockholder_name.validator = bv.String()
FileLockInfo.lockholder_name.validator._redact = bv.BlotRedactor(None)
FileLockInfo.ts_locked.validator = bv.Int64()
FileLockInfo.ts_locked.validator._redact = bv.BlotRedactor(None)
FileLockInfo._all_field_names_ = set([
    'is_lockholder',
    'lockholder_name',
    'ts_locked'])
FileLockInfo._all_fields_ = [
    ('is_lockholder', FileLockInfo.is_lockholder.validator),
    ('lockholder_name', FileLockInfo.lockholder_name.validator),
    ('ts_locked', FileLockInfo.ts_locked.validator)]
FileLockMetadata.is_lockholder.validator = bv.Nullable(bv.Boolean())
FileLockMetadata.lockholder_name.validator = bv.Nullable(bv.String())
FileLockMetadata.lockholder_account_id.validator = bv.Nullable(users_common.AccountId_validator)
FileLockMetadata.created.validator = bv.Nullable(common.DropboxTimestamp_validator)
FileLockMetadata.is_locked.validator = bv.Nullable(bv.Boolean())
FileLockMetadata._all_field_names_ = set([
    'is_lockholder',
    'lockholder_name',
    'lockholder_account_id',
    'created'])
FileLockMetadata._all_fields_ = [
    ('is_lockholder', FileLockMetadata.is_lockholder.validator),
    ('lockholder_name', FileLockMetadata.lockholder_name.validator),
    ('lockholder_account_id', FileLockMetadata.lockholder_account_id.validator),
    ('created', FileLockMetadata.created.validator)]
FileLockMetadata._all_internal_field_names_ = set([
    'is_locked'])
FileLockMetadata._all_internal_fields_ = [
    ('is_locked', FileLockMetadata.is_locked.validator)]
FileMetadata.id.validator = Id_validator
FileMetadata.client_modified.validator = common.DropboxTimestamp_validator
FileMetadata.server_modified.validator = common.DropboxTimestamp_validator
FileMetadata.rev.validator = Rev_validator
FileMetadata.size.validator = bv.UInt64()
FileMetadata.media_info.validator = bv.Nullable(MediaInfo_validator)
FileMetadata.symlink_info.validator = bv.Nullable(SymlinkInfo_validator)
FileMetadata.sharing_info.validator = bv.Nullable(FileSharingInfo_validator)
FileMetadata.is_downloadable.validator = bv.Boolean()
FileMetadata.is_downloadable.validator._redact = bv.BlotRedactor(None)
FileMetadata.export_info.validator = bv.Nullable(ExportInfo_validator)
FileMetadata.property_groups.validator = bv.Nullable(bv.List(file_properties.PropertyGroup_validator))
FileMetadata.has_explicit_shared_members.validator = bv.Nullable(bv.Boolean())
FileMetadata.content_hash.validator = bv.Nullable(Sha256HexHash_validator)
FileMetadata.file_lock_info.validator = bv.Nullable(FileLockMetadata_validator)
FileMetadata.is_restorable.validator = bv.Nullable(bv.Boolean())
FileMetadata.size_display.validator = bv.String()
FileMetadata.size_display.validator._redact = bv.BlotRedactor(None)
FileMetadata.icon.validator = bv.String()
FileMetadata.icon.validator._redact = bv.BlotRedactor(None)
FileMetadata.mime_type.validator = bv.String()
FileMetadata.mime_type.validator._redact = bv.BlotRedactor(None)
FileMetadata.cloud_doc_info.validator = bv.Nullable(CloudDocInfo_validator)
FileMetadata.per_node_metadata.validator = bv.Nullable(per_node_metadata.PerNodeMetadataEntity_validator)
FileMetadata.is_in_vault_folder.validator = bv.Nullable(bv.Boolean())
FileMetadata.is_in_family_shared_folder.validator = bv.Nullable(bv.Boolean())
FileMetadata.open_in_cloud_editor.validator = bv.Nullable(bv.Boolean())
FileMetadata.is_in_backup_folder.validator = bv.Nullable(bv.Boolean())
FileMetadata.is_encrypted.validator = bv.Nullable(bv.Boolean())
FileMetadata.file_encryption_info.validator = bv.Nullable(encryption.EncryptedFile_validator)
FileMetadata.file_owner_team_encrypted_id.validator = bv.Nullable(bv.String())
FileMetadata._field_names_ = set([
    'id',
    'client_modified',
    'server_modified',
    'rev',
    'size',
    'media_info',
    'symlink_info',
    'sharing_info',
    'is_downloadable',
    'export_info',
    'property_groups',
    'has_explicit_shared_members',
    'content_hash',
    'file_lock_info',
    'is_restorable'])
FileMetadata._all_field_names_ = Metadata._all_field_names_.union(FileMetadata._field_names_)
FileMetadata._fields_ = [
    ('id', FileMetadata.id.validator),
    ('client_modified', FileMetadata.client_modified.validator),
    ('server_modified', FileMetadata.server_modified.validator),
    ('rev', FileMetadata.rev.validator),
    ('size', FileMetadata.size.validator),
    ('media_info', FileMetadata.media_info.validator),
    ('symlink_info', FileMetadata.symlink_info.validator),
    ('sharing_info', FileMetadata.sharing_info.validator),
    ('is_downloadable', FileMetadata.is_downloadable.validator),
    ('export_info', FileMetadata.export_info.validator),
    ('property_groups', FileMetadata.property_groups.validator),
    ('has_explicit_shared_members', FileMetadata.has_explicit_shared_members.validator),
    ('content_hash', FileMetadata.content_hash.validator),
    ('file_lock_info', FileMetadata.file_lock_info.validator),
    ('is_restorable', FileMetadata.is_restorable.validator)]
FileMetadata._all_fields_ = Metadata._all_fields_ + FileMetadata._fields_
FileMetadata._internal_field_names_ = set([
    'size_display',
    'icon',
    'mime_type',
    'cloud_doc_info',
    'per_node_metadata',
    'is_in_vault_folder',
    'is_in_family_shared_folder',
    'open_in_cloud_editor',
    'is_in_backup_folder',
    'is_encrypted',
    'file_encryption_info',
    'file_owner_team_encrypted_id'])
FileMetadata._all_internal_field_names_ = FileMetadata._internal_field_names_
FileMetadata._internal_fields_ = [
    ('size_display', FileMetadata.size_display.validator),
    ('icon', FileMetadata.icon.validator),
    ('mime_type', FileMetadata.mime_type.validator),
    ('cloud_doc_info', FileMetadata.cloud_doc_info.validator),
    ('per_node_metadata', FileMetadata.per_node_metadata.validator),
    ('is_in_vault_folder', FileMetadata.is_in_vault_folder.validator),
    ('is_in_family_shared_folder', FileMetadata.is_in_family_shared_folder.validator),
    ('open_in_cloud_editor', FileMetadata.open_in_cloud_editor.validator),
    ('is_in_backup_folder', FileMetadata.is_in_backup_folder.validator),
    ('is_encrypted', FileMetadata.is_encrypted.validator),
    ('file_encryption_info', FileMetadata.file_encryption_info.validator),
    ('file_owner_team_encrypted_id', FileMetadata.file_owner_team_encrypted_id.validator)]
FileMetadata._all_internal_fields_ = FileMetadata._internal_fields_
FileMetadataError._permission_denied_validator = bv.Void()
FileMetadataError._conflict_validator = bv.Void()
FileMetadataError._invalid_argument_validator = bv.Void()
FileMetadataError._invalid_format_version_validator = bv.Void()
FileMetadataError._other_validator = bv.Void()
FileMetadataError._tagmap = {
    'permission_denied': FileMetadataError._permission_denied_validator,
    'conflict': FileMetadataError._conflict_validator,
    'invalid_argument': FileMetadataError._invalid_argument_validator,
    'invalid_format_version': FileMetadataError._invalid_format_version_validator,
    'other': FileMetadataError._other_validator }
FileMetadataError.permission_denied = FileMetadataError('permission_denied')
FileMetadataError.conflict = FileMetadataError('conflict')
FileMetadataError.invalid_argument = FileMetadataError('invalid_argument')
FileMetadataError.invalid_format_version = FileMetadataError('invalid_format_version')
FileMetadataError.other = FileMetadataError('other')
FileMetadataStatus._ok_validator = bv.Void()
FileMetadataStatus._not_found_validator = bv.Void()
FileMetadataStatus._read_permission_denied_validator = bv.Void()
FileMetadataStatus._file_not_found_validator = bv.Void()
FileMetadataStatus._other_validator = bv.Void()
FileMetadataStatus._tagmap = {
    'ok': FileMetadataStatus._ok_validator,
    'not_found': FileMetadataStatus._not_found_validator,
    'read_permission_denied': FileMetadataStatus._read_permission_denied_validator,
    'file_not_found': FileMetadataStatus._file_not_found_validator,
    'other': FileMetadataStatus._other_validator }
FileMetadataStatus.ok = FileMetadataStatus('ok')
FileMetadataStatus.not_found = FileMetadataStatus('not_found')
FileMetadataStatus.read_permission_denied = FileMetadataStatus('read_permission_denied')
FileMetadataStatus.file_not_found = FileMetadataStatus('file_not_found')
FileMetadataStatus.other = FileMetadataStatus('other')
SharingInfo.read_only.validator = bv.Boolean()
SharingInfo._all_field_names_ = set([
    'read_only'])
SharingInfo._all_fields_ = [
    ('read_only', SharingInfo.read_only.validator)]
FileSharingInfo.parent_shared_folder_id.validator = common.SharedFolderId_validator
FileSharingInfo.modified_by.validator = bv.Nullable(users_common.AccountId_validator)
FileSharingInfo.is_parent_shared_folder_read_only.validator = bv.Boolean()
FileSharingInfo.last_modifier.validator = bv.Nullable(ModifierAccountInfo_validator)
FileSharingInfo._all_field_names_ = SharingInfo._all_field_names_.union(set([
    'parent_shared_folder_id',
    'modified_by']))
FileSharingInfo._all_fields_ = SharingInfo._all_fields_ + [
    ('parent_shared_folder_id', FileSharingInfo.parent_shared_folder_id.validator),
    ('modified_by', FileSharingInfo.modified_by.validator)]
FileSharingInfo._all_internal_field_names_ = set([
    'is_parent_shared_folder_read_only',
    'last_modifier'])
FileSharingInfo._all_internal_fields_ = [
    ('is_parent_shared_folder_read_only', FileSharingInfo.is_parent_shared_folder_read_only.validator),
    ('last_modifier', FileSharingInfo.last_modifier.validator)]
FileSpecificMetadata._image_validator = ImageSpecificMetadata_validator
FileSpecificMetadata._audio_validator = AudioSpecificMetadata_validator
FileSpecificMetadata._video_validator = VideoSpecificMetadata_validator
FileSpecificMetadata._ms_office_validator = OfficeSpecificMetadata_validator
FileSpecificMetadata._pdf_validator = PdfSpecificMetadata_validator
FileSpecificMetadata._other_file_validator = OtherFileMetadata_validator
FileSpecificMetadata._other_validator = bv.Void()
FileSpecificMetadata._tagmap = {
    'image': FileSpecificMetadata._image_validator,
    'audio': FileSpecificMetadata._audio_validator,
    'video': FileSpecificMetadata._video_validator,
    'ms_office': FileSpecificMetadata._ms_office_validator,
    'pdf': FileSpecificMetadata._pdf_validator,
    'other_file': FileSpecificMetadata._other_file_validator,
    'other': FileSpecificMetadata._other_validator }
FileSpecificMetadata.other = FileSpecificMetadata('other')
FileStatus._active_validator = bv.Void()
FileStatus._deleted_validator = bv.Void()
FileStatus._other_validator = bv.Void()
FileStatus._tagmap = {
    'active': FileStatus._active_validator,
    'deleted': FileStatus._deleted_validator,
    'other': FileStatus._other_validator }
FileStatus.active = FileStatus('active')
FileStatus.deleted = FileStatus('deleted')
FileStatus.other = FileStatus('other')
FileSystemWarnings.details.validator = bv.List(FswDialogInfoError_validator)
FileSystemWarnings._all_field_names_ = set([
    'details'])
FileSystemWarnings._all_fields_ = [
    ('details', FileSystemWarnings.details.validator)]
FileType._invalid_validator = bv.Void()
FileType._file_validator = bv.Void()
FileType._folder_validator = bv.Void()
FileType._package_validator = bv.Void()
FileType._shared_folder_validator = bv.Void()
FileType._sandbox_validator = bv.Void()
FileType._team_shared_folder_validator = bv.Void()
FileType._team_member_folder_validator = bv.Void()
FileType._vault_folder_validator = bv.Void()
FileType._family_shared_folder_validator = bv.Void()
FileType._backup_folder_validator = bv.Void()
FileType._other_validator = bv.Void()
FileType._tagmap = {
    'invalid': FileType._invalid_validator,
    'file': FileType._file_validator,
    'folder': FileType._folder_validator,
    'package': FileType._package_validator,
    'shared_folder': FileType._shared_folder_validator,
    'sandbox': FileType._sandbox_validator,
    'team_shared_folder': FileType._team_shared_folder_validator,
    'team_member_folder': FileType._team_member_folder_validator,
    'vault_folder': FileType._vault_folder_validator,
    'family_shared_folder': FileType._family_shared_folder_validator,
    'backup_folder': FileType._backup_folder_validator,
    'other': FileType._other_validator }
FileType.invalid = FileType('invalid')
FileType.file = FileType('file')
FileType.folder = FileType('folder')
FileType.package = FileType('package')
FileType.shared_folder = FileType('shared_folder')
FileType.sandbox = FileType('sandbox')
FileType.team_shared_folder = FileType('team_shared_folder')
FileType.team_member_folder = FileType('team_member_folder')
FileType.vault_folder = FileType('vault_folder')
FileType.family_shared_folder = FileType('family_shared_folder')
FileType.backup_folder = FileType('backup_folder')
FileType.other = FileType('other')
FilesTeamFolderCheckArg.async_job_id.validator = bv.String()
FilesTeamFolderCheckArg.async_job_id.validator._redact = bv.BlotRedactor(None)
FilesTeamFolderCheckArg._all_field_names_ = set([
    'async_job_id'])
FilesTeamFolderCheckArg._all_fields_ = [
    ('async_job_id', FilesTeamFolderCheckArg.async_job_id.validator)]
FilesTeamFolderCheckResult.result.validator = AsyncJobResult_validator
FilesTeamFolderCheckResult.metadata.validator = bv.Nullable(FolderMetadata_validator)
FilesTeamFolderCheckResult._all_field_names_ = set([
    'result',
    'metadata'])
FilesTeamFolderCheckResult._all_fields_ = [
    ('result', FilesTeamFolderCheckResult.result.validator),
    ('metadata', FilesTeamFolderCheckResult.metadata.validator)]
FilesTeamFolderCopyArg.autorename.validator = bv.Boolean()
FilesTeamFolderCopyArg.autorename.validator._redact = bv.BlotRedactor(None)
FilesTeamFolderCopyArg.force_async.validator = bv.Boolean()
FilesTeamFolderCopyArg.force_async.validator._redact = bv.BlotRedactor(None)
FilesTeamFolderCopyArg.from_path.validator = bv.String()
FilesTeamFolderCopyArg.from_path.validator._redact = bv.BlotRedactor(None)
FilesTeamFolderCopyArg.to_path.validator = bv.String()
FilesTeamFolderCopyArg.to_path.validator._redact = bv.BlotRedactor(None)
FilesTeamFolderCopyArg._all_field_names_ = set([
    'autorename',
    'force_async',
    'from_path',
    'to_path'])
FilesTeamFolderCopyArg._all_fields_ = [
    ('autorename', FilesTeamFolderCopyArg.autorename.validator),
    ('force_async', FilesTeamFolderCopyArg.force_async.validator),
    ('from_path', FilesTeamFolderCopyArg.from_path.validator),
    ('to_path', FilesTeamFolderCopyArg.to_path.validator)]
FilesTeamFolderCopyResponse.async_job_id.validator = bv.String()
FilesTeamFolderCopyResponse.async_job_id.validator._redact = bv.BlotRedactor(None)
FilesTeamFolderCopyResponse.metadata.validator = bv.Nullable(FolderMetadata_validator)
FilesTeamFolderCopyResponse._all_field_names_ = set([
    'async_job_id',
    'metadata'])
FilesTeamFolderCopyResponse._all_fields_ = [
    ('async_job_id', FilesTeamFolderCopyResponse.async_job_id.validator),
    ('metadata', FilesTeamFolderCopyResponse.metadata.validator)]
FilesTeamFolderCountArg._all_field_names_ = set([])
FilesTeamFolderCountArg._all_fields_ = []
FilesTeamFolderCountResponse.count.validator = bv.UInt64()
FilesTeamFolderCountResponse.count.validator._redact = bv.BlotRedactor(None)
FilesTeamFolderCountResponse._all_field_names_ = set([
    'count'])
FilesTeamFolderCountResponse._all_fields_ = [
    ('count', FilesTeamFolderCountResponse.count.validator)]
FilesTeamFolderCreateArg.name.validator = bv.String()
FilesTeamFolderCreateArg.name.validator._redact = bv.BlotRedactor(None)
FilesTeamFolderCreateArg.pap_action_surface.validator = bv.String()
FilesTeamFolderCreateArg.pap_action_surface.validator._redact = bv.BlotRedactor(None)
FilesTeamFolderCreateArg._all_field_names_ = set([
    'name',
    'pap_action_surface'])
FilesTeamFolderCreateArg._all_fields_ = [
    ('name', FilesTeamFolderCreateArg.name.validator),
    ('pap_action_surface', FilesTeamFolderCreateArg.pap_action_surface.validator)]
FilesTeamFolderCreateResponse.team_folder_id.validator = bv.UInt64()
FilesTeamFolderCreateResponse.team_folder_id.validator._redact = bv.BlotRedactor(None)
FilesTeamFolderCreateResponse.name.validator = bv.String()
FilesTeamFolderCreateResponse.name.validator._redact = bv.BlotRedactor(None)
FilesTeamFolderCreateResponse.async_job_id.validator = bv.String()
FilesTeamFolderCreateResponse.async_job_id.validator._redact = bv.BlotRedactor(None)
FilesTeamFolderCreateResponse.metadata.validator = bv.Nullable(FolderMetadata_validator)
FilesTeamFolderCreateResponse.team_folder_count.validator = bv.UInt64()
FilesTeamFolderCreateResponse.team_folder_count.validator._redact = bv.BlotRedactor(None)
FilesTeamFolderCreateResponse._all_field_names_ = set([
    'team_folder_id',
    'name',
    'async_job_id',
    'metadata',
    'team_folder_count'])
FilesTeamFolderCreateResponse._all_fields_ = [
    ('team_folder_id', FilesTeamFolderCreateResponse.team_folder_id.validator),
    ('name', FilesTeamFolderCreateResponse.name.validator),
    ('async_job_id', FilesTeamFolderCreateResponse.async_job_id.validator),
    ('metadata', FilesTeamFolderCreateResponse.metadata.validator),
    ('team_folder_count', FilesTeamFolderCreateResponse.team_folder_count.validator)]
FilesTeamFolderDeleteArg.team_folder_id.validator = bv.Nullable(bv.UInt64())
FilesTeamFolderDeleteArg.path.validator = bv.Nullable(bv.String())
FilesTeamFolderDeleteArg._all_field_names_ = set([
    'team_folder_id',
    'path'])
FilesTeamFolderDeleteArg._all_fields_ = [
    ('team_folder_id', FilesTeamFolderDeleteArg.team_folder_id.validator),
    ('path', FilesTeamFolderDeleteArg.path.validator)]
FilesTeamFolderDeleteResponse.team_folder_id.validator = bv.UInt64()
FilesTeamFolderDeleteResponse.team_folder_id.validator._redact = bv.BlotRedactor(None)
FilesTeamFolderDeleteResponse.metadata.validator = bv.Nullable(FolderMetadata_validator)
FilesTeamFolderDeleteResponse._all_field_names_ = set([
    'team_folder_id',
    'metadata'])
FilesTeamFolderDeleteResponse._all_fields_ = [
    ('team_folder_id', FilesTeamFolderDeleteResponse.team_folder_id.validator),
    ('metadata', FilesTeamFolderDeleteResponse.metadata.validator)]
FilesTeamFolderError._unknown_error_validator = bv.Void()
FilesTeamFolderError._forbidden_validator = bv.Void()
FilesTeamFolderError._name_conflict_validator = bv.Void()
FilesTeamFolderError._name_invalid_validator = bv.Void()
FilesTeamFolderError._name_reserved_validator = bv.Void()
FilesTeamFolderError._invalid_team_folder_id_validator = bv.Void()
FilesTeamFolderError._path_invalid_validator = bv.Void()
FilesTeamFolderError._ns_not_found_validator = bv.Void()
FilesTeamFolderError._both_team_folder_id_and_path_are_not_allowed_validator = bv.Void()
FilesTeamFolderError._team_folder_id_or_path_required_validator = bv.Void()
FilesTeamFolderError._team_folder_id_required_validator = bv.Void()
FilesTeamFolderError._not_a_team_folder_validator = bv.Void()
FilesTeamFolderError._team_folder_already_active_validator = bv.Void()
FilesTeamFolderError._will_not_create_cycle_validator = bv.Void()
FilesTeamFolderError._failed_acquire_lock_validator = bv.Void()
FilesTeamFolderError._throttled_validator = bv.Void()
FilesTeamFolderError._folder_count_limit_exceeded_validator = bv.Void()
FilesTeamFolderError._other_validator = bv.Void()
# WARNING: Decompyle incomplete
