# Source Generated with Decompyle++
# File: auto_updater_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/apex/auto_updater.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%dropbox/proto/apex/auto_updater.proto\x12\x0cauto_updater\x1a#dropbox/proto/rust/extensions.proto\x1a\x1bgoogle/protobuf/empty.proto"\xb2\x14\n\x0cUpdaterEvent\x120\n\x0eshould_promote\x18\x02 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12K\n\x13flush_and_terminate\x18\x03 \x01(\x0b2,.auto_updater.UpdaterEvent.FlushAndTerminateH\x00\x126\n\x14checking_for_updates\x18\x04 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12F\n\x10update_available\x18\x05 \x01(\x0b2*.auto_updater.UpdaterEvent.UpdateAvailableH\x00\x126\n\x14update_not_available\x18\x06 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12J\n\x12update_downloading\x18\x07 \x01(\x0b2,.auto_updater.UpdaterEvent.UpdateDownloadingH\x00\x12H\n\x11update_installing\x18\x08 \x01(\x0b2+.auto_updater.UpdaterEvent.UpdateInstallingH\x00\x121\n\x05error\x18\t \x01(\x0b2 .auto_updater.UpdaterEvent.ErrorH\x00\x12*\n\x08promoted\x18\n \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12)\n\x07updated\x18\x0b \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12)\n\x07unknown\x18\x0c \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12-\n\x0bnot_started\x18\r \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12+\n\tno_update\x18\x0e \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12>\n\x0cupdate_error\x18\x0f \x01(\x0b2&.auto_updater.UpdaterEvent.UpdateErrorH\x00\x12K\n\x13app_install_unknown\x18\x10 \x01(\x0b2,.auto_updater.UpdaterEvent.AppInstallUnknownH\x00\x12R\n\x17app_install_not_started\x18\x11 \x01(\x0b2/.auto_updater.UpdaterEvent.AppInstallNotStartedH\x00\x12c\n app_install_checking_for_updates\x18\x12 \x01(\x0b27.auto_updater.UpdaterEvent.AppInstallCheckingForUpdatesH\x00\x12O\n\x15app_install_available\x18\x13 \x01(\x0b2..auto_updater.UpdaterEvent.AppInstallAvailableH\x00\x12V\n\x19app_install_not_available\x18\x14 \x01(\x0b21.auto_updater.UpdaterEvent.AppInstallNotAvailableH\x00\x12S\n\x17app_install_downloading\x18\x15 \x01(\x0b20.auto_updater.UpdaterEvent.AppInstallDownloadingH\x00\x12B\n\x0eapp_installing\x18\x16 \x01(\x0b2(.auto_updater.UpdaterEvent.AppInstallingH\x00\x12@\n\rapp_installed\x18\x17 \x01(\x0b2\'.auto_updater.UpdaterEvent.AppInstalledH\x00\x12N\n\x15app_install_no_update\x18\x18 \x01(\x0b2-.auto_updater.UpdaterEvent.AppInstallNoUpdateH\x00\x12G\n\x11app_install_error\x18\x19 \x01(\x0b2*.auto_updater.UpdaterEvent.AppInstallErrorH\x00\x12T\n\x18get_installed_apps_event\x18\x1a \x01(\x0b20.auto_updater.UpdaterEvent.GetInstalledAppsEventH\x00\x1a*\n\x11FlushAndTerminate\x12\x15\n\ris_background\x18\x01 \x01(\x08\x1a\'\n\x0fUpdateAvailable\x12\x14\n\x0cnext_version\x18\x01 \x01(\t\x1aB\n\x11UpdateDownloading\x12\x18\n\x10downloaded_bytes\x18\x01 \x01(\x03\x12\x13\n\x0btotal_bytes\x18\x02 \x01(\x03\x1a,\n\x10UpdateInstalling\x12\x18\n\x10install_progress\x18\x01 \x01(\x05\x1aN\n\x0bUpdateError\x12\x16\n\x0eerror_category\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x05\x12\x13\n\x0bextra_code1\x18\x03 \x01(\x05\x1a\x18\n\x05Error\x12\x0f\n\x07message\x18\x01 \x01(\t\x1a#\n\x11AppInstallUnknown\x12\x0e\n\x06app_id\x18\x01 \x01(\t\x1a&\n\x14AppInstallNotStarted\x12\x0e\n\x06app_id\x18\x01 \x01(\t\x1a.\n\x1cAppInstallCheckingForUpdates\x12\x0e\n\x06app_id\x18\x01 \x01(\t\x1a;\n\x13AppInstallAvailable\x12\x0e\n\x06app_id\x18\x01 \x01(\t\x12\x14\n\x0cnext_version\x18\x02 \x01(\t\x1a(\n\x16AppInstallNotAvailable\x12\x0e\n\x06app_id\x18\x01 \x01(\t\x1aV\n\x15AppInstallDownloading\x12\x0e\n\x06app_id\x18\x01 \x01(\t\x12\x18\n\x10downloaded_bytes\x18\x02 \x01(\x03\x12\x13\n\x0btotal_bytes\x18\x03 \x01(\x03\x1a9\n\rAppInstalling\x12\x0e\n\x06app_id\x18\x01 \x01(\t\x12\x18\n\x10install_progress\x18\x02 \x01(\x05\x1a\x1e\n\x0cAppInstalled\x12\x0e\n\x06app_id\x18\x01 \x01(\t\x1a$\n\x12AppInstallNoUpdate\x12\x0e\n\x06app_id\x18\x01 \x01(\t\x1ab\n\x0fAppInstallError\x12\x0e\n\x06app_id\x18\x01 \x01(\t\x12\x16\n\x0eerror_category\x18\x02 \x01(\x05\x12\x12\n\nerror_code\x18\x03 \x01(\x05\x12\x13\n\x0bextra_code1\x18\x04 \x01(\x05\x1a(\n\x15GetInstalledAppsEvent\x12\x0f\n\x07app_ids\x18\x01 \x03(\tB\x0f\n\x07payload\x12\x04\x88\xb5\x18\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.apex.auto_updater_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_UPDATEREVENT'].oneofs_by_name['payload']._loaded_options = None
    _globals['_UPDATEREVENT'].oneofs_by_name['payload']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_UPDATEREVENT']._serialized_start = 122
    _globals['_UPDATEREVENT']._serialized_end = 2732
    _globals['_UPDATEREVENT_FLUSHANDTERMINATE']._serialized_start = 1825
    _globals['_UPDATEREVENT_FLUSHANDTERMINATE']._serialized_end = 1867
    _globals['_UPDATEREVENT_UPDATEAVAILABLE']._serialized_start = 1869
    _globals['_UPDATEREVENT_UPDATEAVAILABLE']._serialized_end = 1908
    _globals['_UPDATEREVENT_UPDATEDOWNLOADING']._serialized_start = 1910
    _globals['_UPDATEREVENT_UPDATEDOWNLOADING']._serialized_end = 1976
    _globals['_UPDATEREVENT_UPDATEINSTALLING']._serialized_start = 1978
    _globals['_UPDATEREVENT_UPDATEINSTALLING']._serialized_end = 2022
    _globals['_UPDATEREVENT_UPDATEERROR']._serialized_start = 2024
    _globals['_UPDATEREVENT_UPDATEERROR']._serialized_end = 2102
    _globals['_UPDATEREVENT_ERROR']._serialized_start = 2104
    _globals['_UPDATEREVENT_ERROR']._serialized_end = 2128
    _globals['_UPDATEREVENT_APPINSTALLUNKNOWN']._serialized_start = 2130
    _globals['_UPDATEREVENT_APPINSTALLUNKNOWN']._serialized_end = 2165
    _globals['_UPDATEREVENT_APPINSTALLNOTSTARTED']._serialized_start = 2167
    _globals['_UPDATEREVENT_APPINSTALLNOTSTARTED']._serialized_end = 2205
    _globals['_UPDATEREVENT_APPINSTALLCHECKINGFORUPDATES']._serialized_start = 2207
    _globals['_UPDATEREVENT_APPINSTALLCHECKINGFORUPDATES']._serialized_end = 2253
    _globals['_UPDATEREVENT_APPINSTALLAVAILABLE']._serialized_start = 2255
    _globals['_UPDATEREVENT_APPINSTALLAVAILABLE']._serialized_end = 2314
    _globals['_UPDATEREVENT_APPINSTALLNOTAVAILABLE']._serialized_start = 2316
    _globals['_UPDATEREVENT_APPINSTALLNOTAVAILABLE']._serialized_end = 2356
    _globals['_UPDATEREVENT_APPINSTALLDOWNLOADING']._serialized_start = 2358
    _globals['_UPDATEREVENT_APPINSTALLDOWNLOADING']._serialized_end = 2444
    _globals['_UPDATEREVENT_APPINSTALLING']._serialized_start = 2446
    _globals['_UPDATEREVENT_APPINSTALLING']._serialized_end = 2503
    _globals['_UPDATEREVENT_APPINSTALLED']._serialized_start = 2505
    _globals['_UPDATEREVENT_APPINSTALLED']._serialized_end = 2535
    _globals['_UPDATEREVENT_APPINSTALLNOUPDATE']._serialized_start = 2537
    _globals['_UPDATEREVENT_APPINSTALLNOUPDATE']._serialized_end = 2573
    _globals['_UPDATEREVENT_APPINSTALLERROR']._serialized_start = 2575
    _globals['_UPDATEREVENT_APPINSTALLERROR']._serialized_end = 2673
    _globals['_UPDATEREVENT_GETINSTALLEDAPPSEVENT']._serialized_start = 2675
    _globals['_UPDATEREVENT_GETINSTALLEDAPPSEVENT']._serialized_end = 2715
    return None
