# Source Generated with Decompyle++
# File: remote_command_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/sync_frontend/remote_command.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from dropbox.proto.sync_frontend import bolt_pb2 as dropbox_dot_proto_dot_sync__frontend_dot_bolt__pb2
from dropbox.proto.sync_frontend import context_pb2 as dropbox_dot_proto_dot_sync__frontend_dot_context__pb2
from dropbox.proto.sync_frontend import cursors_pb2 as dropbox_dot_proto_dot_sync__frontend_dot_cursors__pb2
from dropbox.proto.sync_frontend import debug_file_status_pb2 as dropbox_dot_proto_dot_sync__frontend_dot_debug__file__status__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0dropbox/proto/sync_frontend/remote_command.proto\x12\rsync_frontend\x1a#dropbox/proto/rust/extensions.proto\x1a&dropbox/proto/sync_frontend/bolt.proto\x1a)dropbox/proto/sync_frontend/context.proto\x1a)dropbox/proto/sync_frontend/cursors.proto\x1a3dropbox/proto/sync_frontend/debug_file_status.proto\x1a\x1bgoogle/protobuf/empty.proto"\r\n\x0bPingRequest"\x0e\n\x0cPingResponse"\x15\n\x13BasicMetricsRequest"\x92\x02\n\x14BasicMetricsResponse\x12\x17\n\x0flocal_tree_size\x18\x01 \x01(\r\x12\x18\n\x10synced_tree_size\x18\x02 \x01(\r\x12\x18\n\x10remote_tree_size\x18\x03 \x01(\r\x12\x1e\n\x16local_diff_approx_size\x18\x04 \x01(\r\x12\x1f\n\x17remote_diff_approx_size\x18\x05 \x01(\r\x12"\n\x1alocal_memory_usage_summary\x18\x06 \x01(\t\x12#\n\x1bsynced_memory_usage_summary\x18\x07 \x01(\t\x12#\n\x1bremote_memory_usage_summary\x18\x08 \x01(\t"\x1c\n\rErrorResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t"\x16\n\x14CurrentCursorRequest"V\n\x15CurrentCursorResponse\x12=\n\x0ecurrent_cursor\x18\x01 \x01(\x0b2%.sync_frontend.SignedLinearizedCursor":\n\x11FileStatusRequest\x12%\n\x06fileId\x18\x01 \x01(\x0b2\x15.sync_frontend.FileId"\xb6\x02\n\x12FileStatusResponse\x12,\n\x05local\x18\x01 \x01(\x0b2\x1d.sync_frontend.FileStatusNode\x12-\n\x06synced\x18\x02 \x01(\x0b2\x1d.sync_frontend.FileStatusNode\x12-\n\x06remote\x18\x03 \x01(\x0b2\x1d.sync_frontend.FileStatusNode\x12&\n\tlocalPath\x18\x05 \x01(\x0b2\x13.sync_frontend.Path\x12\'\n\nsyncedPath\x18\x06 \x01(\x0b2\x13.sync_frontend.Path\x12\'\n\nremotePath\x18\x07 \x01(\x0b2\x13.sync_frontend.Path\x12\x1a\n\x12userDomainContents\x18\x08 \x01(\t"C\n\x1aFolderChildrenStatsRequest\x12%\n\x06fileId\x18\x01 \x01(\x0b2\x15.sync_frontend.FileId"\xb9\x02\n\x1bFolderChildrenStatsResponse\x12\x1e\n\x16total_placeholder_size\x18\x01 \x01(\x04\x12\x17\n\x0ftotal_num_items\x18\x02 \x01(\r\x12\x1f\n\x17total_num_ignored_items\x18\x03 \x01(\r\x12 \n\x18total_ignored_items_size\x18\x04 \x01(\x04\x12*\n"total_num_implicitly_ignored_items\x18\x05 \x01(\r\x12+\n#total_implicitly_ignored_items_size\x18\x06 \x01(\x04\x12\x1e\n\x16total_local_items_size\x18\x07 \x01(\x04\x12%\n\x1dnum_dir_skipped_due_to_errors\x18\x08 \x01(\r"!\n\x1fRemoteConsistencyCheckerRequest""\n RemoteConsistencyCheckerResponse"\xc4\x02\n\x17FileProviderDumpRequest\x12=\n\x06flavor\x18\x01 \x01(\x0e2-.sync_frontend.FileProviderDumpRequest.Flavor\x12\x12\n\nstart_date\x18\x02 \x01(\t\x12\x10\n\x08end_date\x18\x03 \x01(\t\x12\x12\n\nlocal_path\x18\x04 \x01(\t\x12\x0e\n\x06itemid\x18\x05 \x01(\t\x12\x15\n\rmdutil_fileid\x18\x06 \x01(\x04"\x88\x01\n\x06Flavor\x12\x08\n\x04DUMP\x10\x00\x12\r\n\tFULL_DUMP\x10\x01\x12\x0f\n\x0bDAEMON_LOGS\x10\x02\x12\x14\n\x10FS_STATE_BY_PATH\x10\x03\x12\x16\n\x12FULL_DUMP_AND_TRIM\x10\x04\x12\x17\n\x13FS_STATE_BY_ITEM_ID\x10\x05\x12\r\n\tFS_MDUTIL\x10\x06"+\n\x18FileProviderDumpResponse\x12\x0f\n\x07payload\x18\x01 \x01(\t"$\n"DBXIgnoreConsistencyCheckerRequest"\x99\x03\n#DBXIgnoreConsistencyCheckerResponse\x12P\n\x07results\x18\x01 \x03(\x0b2?.sync_frontend.DBXIgnoreConsistencyCheckerResponse.AnchorResult\x1a\x9f\x02\n\x0cAnchorResult\x122\n\ranchor_fileid\x18\x01 \x01(\x0b2\x15.sync_frontend.FileIdB\x04\xc0\xb5\x18\x00\x12\x0e\n\x06result\x18\x02 \x01(\t\x121\n\x12unexpected_backups\x18\x03 \x03(\x0b2\x15.sync_frontend.FileId\x121\n\x12unexpected_ignores\x18\x04 \x03(\x0b2\x15.sync_frontend.FileId\x12,\n\rxattr_ignores\x18\x05 \x03(\x0b2\x15.sync_frontend.FileId\x12\x16\n\x0esilly_labrador\x18\x06 \x01(\x08\x12\x1f\n\x17dumped_dbxignore_base64\x18\x07 \x01(\t" \n\x1eRecoverCorruptedPackageRequest"\x8e\x02\n\x1fRecoverCorruptedPackageResponse\x12P\n\x07results\x18\x01 \x03(\x0b2?.sync_frontend.RecoverCorruptedPackageResponse.RecoveredPackage\x12 \n\x18total_recovered_packages\x18\x02 \x01(\r\x1aw\n\x10RecoveredPackage\x123\n\x0epackage_fileid\x18\x01 \x01(\x0b2\x15.sync_frontend.FileIdB\x04\xc0\xb5\x18\x00\x12\x1e\n\x16package_file_extension\x18\x02 \x01(\t\x12\x0e\n\x06result\x18\x03 \x01(\t"#\n!ListProcessesWithOpenFilesRequest"\xc7\x01\n"ListProcessesWithOpenFilesResponse\x12P\n\tprocesses\x18\x01 \x03(\x0b2=.sync_frontend.ListProcessesWithOpenFilesResponse.ProcessInfo\x12\x1d\n\x15unnamed_process_count\x18\x02 \x01(\r\x1a0\n\x0bProcessInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bhandle_info\x18\x02 \x01(\r"T\n\rRemoteCommand\x12\x11\n\tassoc_gid\x18\x01 \x01(\x0c\x120\n\x07command\x18\x02 \x01(\x0b2\x1f.sync_frontend.CommandContainer"/\n\x1dFileProviderItemLookupRequest\x12\x0e\n\x06itemid\x18\x01 \x01(\x04"2\n\x1eFileProviderItemLookupResponse\x12\x10\n\x08response\x18\x01 \x01(\t"\x96\x07\n\x10CommandContainer\x12*\n\x04ping\x18\x01 \x01(\x0b2\x1a.sync_frontend.PingRequestH\x00\x12;\n\rbasic_metrics\x18\x02 \x01(\x0b2".sync_frontend.BasicMetricsRequestH\x00\x12=\n\x0ecurrent_cursor\x18\x03 \x01(\x0b2#.sync_frontend.CurrentCursorRequestH\x00\x127\n\x0bfile_status\x18\x04 \x01(\x0b2 .sync_frontend.FileStatusRequestH\x00\x12T\n\x1aremote_consistency_checker\x18\x05 \x01(\x0b2..sync_frontend.RemoteConsistencyCheckerRequestH\x00\x12J\n\x15folder_children_stats\x18\x06 \x01(\x0b2).sync_frontend.FolderChildrenStatsRequestH\x00\x12D\n\x12file_provider_dump\x18\x07 \x01(\x0b2&.sync_frontend.FileProviderDumpRequestH\x00\x12Z\n\x1ddbxignore_consistency_checker\x18\x08 \x01(\x0b21.sync_frontend.DBXIgnoreConsistencyCheckerRequestH\x00\x12Z\n!recover_corrupted_package_request\x18\t \x01(\x0b2-.sync_frontend.RecoverCorruptedPackageRequestH\x00\x12Z\n\x1elist_processes_with_open_files\x18\n \x01(\x0b20.sync_frontend.ListProcessesWithOpenFilesRequestH\x00\x12Q\n\x19file_provider_item_lookup\x18\x0b \x01(\x0b2,.sync_frontend.FileProviderItemLookupRequestH\x00\x12B\n\x11refresh_sync_gold\x18\x0c \x01(\x0b2%.sync_frontend.RefreshSyncGoldRequestH\x00B\x0e\n\x06action\x12\x04\x88\xb5\x18\x00"\xbd\x08\n\x0fReportContainer\x124\n\rping_response\x18\x01 \x01(\x0b2\x1b.sync_frontend.PingResponseH\x00\x12E\n\x16basic_metrics_response\x18\x02 \x01(\x0b2#.sync_frontend.BasicMetricsResponseH\x00\x126\n\x0eerror_response\x18\x03 \x01(\x0b2\x1c.sync_frontend.ErrorResponseH\x00\x12G\n\x17current_cursor_response\x18\x04 \x01(\x0b2$.sync_frontend.CurrentCursorResponseH\x00\x12A\n\x14file_status_response\x18\x05 \x01(\x0b2!.sync_frontend.FileStatusResponseH\x00\x12^\n#remote_consistency_checker_response\x18\x06 \x01(\x0b2/.sync_frontend.RemoteConsistencyCheckerResponseH\x00\x12T\n\x1efolder_children_stats_response\x18\x07 \x01(\x0b2*.sync_frontend.FolderChildrenStatsResponseH\x00\x12N\n\x1bfile_provider_dump_response\x18\x08 \x01(\x0b2\'.sync_frontend.FileProviderDumpResponseH\x00\x12d\n&dbxignore_consistency_checker_response\x18\t \x01(\x0b22.sync_frontend.DBXIgnoreConsistencyCheckerResponseH\x00\x12\\\n"recover_corrupted_package_response\x18\n \x01(\x0b2..sync_frontend.RecoverCorruptedPackageResponseH\x00\x12d\n\'list_processes_with_open_files_response\x18\x0b \x01(\x0b21.sync_frontend.ListProcessesWithOpenFilesResponseH\x00\x12[\n"file_provider_item_lookup_response\x18\x0c \x01(\x0b2-.sync_frontend.FileProviderItemLookupResponseH\x00\x12L\n\x1arefresh_sync_gold_response\x18\r \x01(\x0b2&.sync_frontend.RefreshSyncGoldResponseH\x00B\x0e\n\x06report\x12\x04\x88\xb5\x18\x00"U\n\x10CommandRunReport\x12\x11\n\tassoc_gid\x18\x01 \x01(\x0c\x12.\n\x06report\x18\x02 \x01(\x0b2\x1e.sync_frontend.ReportContainer"\xe1\x01\n\x19CommunicateCommandRequest\x126\n\x0frequest_context\x18\x01 \x01(\x0b2\x1d.sync_frontend.RequestContext\x128\n\x16request_latest_command\x18\x02 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12B\n\x17respond_to_last_command\x18\x03 \x01(\x0b2\x1f.sync_frontend.CommandRunReportH\x00B\x0e\n\x06action\x12\x04\x88\xb5\x18\x00"\xda\x01\n\x1aCommunicateCommandResponse\x128\n\x10response_context\x18\x01 \x01(\x0b2\x1e.sync_frontend.ResponseContext\x125\n\nbolt_token\x18\x02 \x01(\x0b2\x1f.sync_frontend.BoltChannelTokenH\x00\x124\n\x0cnext_command\x18\x03 \x01(\x0b2\x1c.sync_frontend.RemoteCommandH\x00B\x15\n\rresponse_body\x12\x04\x88\xb5\x18\x00"\x18\n\x16RefreshSyncGoldRequest"\x19\n\x17RefreshSyncGoldResponseB\x1dZ\x1bdropbox/proto/sync_frontendb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.sync_frontend.remote_command_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1bdropbox/proto/sync_frontend'
    _globals['_DBXIGNORECONSISTENCYCHECKERRESPONSE_ANCHORRESULT'].fields_by_name['anchor_fileid']._loaded_options = None
    _globals['_DBXIGNORECONSISTENCYCHECKERRESPONSE_ANCHORRESULT'].fields_by_name['anchor_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_RECOVERCORRUPTEDPACKAGERESPONSE_RECOVEREDPACKAGE'].fields_by_name['package_fileid']._loaded_options = None
    _globals['_RECOVERCORRUPTEDPACKAGERESPONSE_RECOVEREDPACKAGE'].fields_by_name['package_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_COMMANDCONTAINER'].oneofs_by_name['action']._loaded_options = None
    _globals['_COMMANDCONTAINER'].oneofs_by_name['action']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_REPORTCONTAINER'].oneofs_by_name['report']._loaded_options = None
    _globals['_REPORTCONTAINER'].oneofs_by_name['report']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_COMMUNICATECOMMANDREQUEST'].oneofs_by_name['action']._loaded_options = None
    _globals['_COMMUNICATECOMMANDREQUEST'].oneofs_by_name['action']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_COMMUNICATECOMMANDRESPONSE'].oneofs_by_name['response_body']._loaded_options = None
    _globals['_COMMUNICATECOMMANDRESPONSE'].oneofs_by_name['response_body']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_PINGREQUEST']._serialized_start = 312
    _globals['_PINGREQUEST']._serialized_end = 325
    _globals['_PINGRESPONSE']._serialized_start = 327
    _globals['_PINGRESPONSE']._serialized_end = 341
    _globals['_BASICMETRICSREQUEST']._serialized_start = 343
    _globals['_BASICMETRICSREQUEST']._serialized_end = 364
    _globals['_BASICMETRICSRESPONSE']._serialized_start = 367
    _globals['_BASICMETRICSRESPONSE']._serialized_end = 641
    _globals['_ERRORRESPONSE']._serialized_start = 643
    _globals['_ERRORRESPONSE']._serialized_end = 671
    _globals['_CURRENTCURSORREQUEST']._serialized_start = 673
    _globals['_CURRENTCURSORREQUEST']._serialized_end = 695
    _globals['_CURRENTCURSORRESPONSE']._serialized_start = 697
    _globals['_CURRENTCURSORRESPONSE']._serialized_end = 783
    _globals['_FILESTATUSREQUEST']._serialized_start = 785
    _globals['_FILESTATUSREQUEST']._serialized_end = 843
    _globals['_FILESTATUSRESPONSE']._serialized_start = 846
    _globals['_FILESTATUSRESPONSE']._serialized_end = 1156
    _globals['_FOLDERCHILDRENSTATSREQUEST']._serialized_start = 1158
    _globals['_FOLDERCHILDRENSTATSREQUEST']._serialized_end = 1225
    _globals['_FOLDERCHILDRENSTATSRESPONSE']._serialized_start = 1228
    _globals['_FOLDERCHILDRENSTATSRESPONSE']._serialized_end = 1541
    _globals['_REMOTECONSISTENCYCHECKERREQUEST']._serialized_start = 1543
    _globals['_REMOTECONSISTENCYCHECKERREQUEST']._serialized_end = 1576
    _globals['_REMOTECONSISTENCYCHECKERRESPONSE']._serialized_start = 1578
    _globals['_REMOTECONSISTENCYCHECKERRESPONSE']._serialized_end = 1612
    _globals['_FILEPROVIDERDUMPREQUEST']._serialized_start = 1615
    _globals['_FILEPROVIDERDUMPREQUEST']._serialized_end = 1939
    _globals['_FILEPROVIDERDUMPREQUEST_FLAVOR']._serialized_start = 1803
    _globals['_FILEPROVIDERDUMPREQUEST_FLAVOR']._serialized_end = 1939
    _globals['_FILEPROVIDERDUMPRESPONSE']._serialized_start = 1941
    _globals['_FILEPROVIDERDUMPRESPONSE']._serialized_end = 1984
    _globals['_DBXIGNORECONSISTENCYCHECKERREQUEST']._serialized_start = 1986
    _globals['_DBXIGNORECONSISTENCYCHECKERREQUEST']._serialized_end = 2022
    _globals['_DBXIGNORECONSISTENCYCHECKERRESPONSE']._serialized_start = 2025
    _globals['_DBXIGNORECONSISTENCYCHECKERRESPONSE']._serialized_end = 2434
    _globals['_DBXIGNORECONSISTENCYCHECKERRESPONSE_ANCHORRESULT']._serialized_start = 2147
    _globals['_DBXIGNORECONSISTENCYCHECKERRESPONSE_ANCHORRESULT']._serialized_end = 2434
    _globals['_RECOVERCORRUPTEDPACKAGEREQUEST']._serialized_start = 2436
    _globals['_RECOVERCORRUPTEDPACKAGEREQUEST']._serialized_end = 2468
    _globals['_RECOVERCORRUPTEDPACKAGERESPONSE']._serialized_start = 2471
    _globals['_RECOVERCORRUPTEDPACKAGERESPONSE']._serialized_end = 2741
    _globals['_RECOVERCORRUPTEDPACKAGERESPONSE_RECOVEREDPACKAGE']._serialized_start = 2622
    _globals['_RECOVERCORRUPTEDPACKAGERESPONSE_RECOVEREDPACKAGE']._serialized_end = 2741
    _globals['_LISTPROCESSESWITHOPENFILESREQUEST']._serialized_start = 2743
    _globals['_LISTPROCESSESWITHOPENFILESREQUEST']._serialized_end = 2778
    _globals['_LISTPROCESSESWITHOPENFILESRESPONSE']._serialized_start = 2781
    _globals['_LISTPROCESSESWITHOPENFILESRESPONSE']._serialized_end = 2980
    _globals['_LISTPROCESSESWITHOPENFILESRESPONSE_PROCESSINFO']._serialized_start = 2932
    _globals['_LISTPROCESSESWITHOPENFILESRESPONSE_PROCESSINFO']._serialized_end = 2980
    _globals['_REMOTECOMMAND']._serialized_start = 2982
    _globals['_REMOTECOMMAND']._serialized_end = 3066
    _globals['_FILEPROVIDERITEMLOOKUPREQUEST']._serialized_start = 3068
    _globals['_FILEPROVIDERITEMLOOKUPREQUEST']._serialized_end = 3115
    _globals['_FILEPROVIDERITEMLOOKUPRESPONSE']._serialized_start = 3117
    _globals['_FILEPROVIDERITEMLOOKUPRESPONSE']._serialized_end = 3167
    _globals['_COMMANDCONTAINER']._serialized_start = 3170
    _globals['_COMMANDCONTAINER']._serialized_end = 4088
    _globals['_REPORTCONTAINER']._serialized_start = 4091
    _globals['_REPORTCONTAINER']._serialized_end = 5176
    _globals['_COMMANDRUNREPORT']._serialized_start = 5178
    _globals['_COMMANDRUNREPORT']._serialized_end = 5263
    _globals['_COMMUNICATECOMMANDREQUEST']._serialized_start = 5266
    _globals['_COMMUNICATECOMMANDREQUEST']._serialized_end = 5491
    _globals['_COMMUNICATECOMMANDRESPONSE']._serialized_start = 5494
    _globals['_COMMUNICATECOMMANDRESPONSE']._serialized_end = 5712
    _globals['_REFRESHSYNCGOLDREQUEST']._serialized_start = 5714
    _globals['_REFRESHSYNCGOLDREQUEST']._serialized_end = 5738
    _globals['_REFRESHSYNCGOLDRESPONSE']._serialized_start = 5740
    _globals['_REFRESHSYNCGOLDRESPONSE']._serialized_end = 5765
    return None
