# Source Generated with Decompyle++
# File: app_info_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'app_info.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from  import shared_pb2 as shared__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eapp_info.proto\x12\x13dropbox.meta_engine\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0cshared.proto"\x1f\n\nClientInfo\x12\x11\n\tjson_data\x18\x01 \x01(\t""\n\x0fPlatformVersion\x12\x0f\n\x07version\x18\x01 \x01(\t"\x1b\n\x0cInstallerTag\x12\x0b\n\x03tag\x18\x01 \x01(\t"\x1f\n\x0fHostDisplayName\x12\x0c\n\x04name\x18\x01 \x01(\t"P\n\x12GetUnlinkCookieReq\x12:\n\x07account\x18\x01 \x01(\x0b2).dropbox.meta_engine.AuthenticatedAccount"5\n\x0cUnlinkCookie\x12\r\n\x05email\x18\x01 \x01(\t\x12\x16\n\x0ehidden_fileids\x18\x02 \x03(\t"\x1c\n\x0cPlatformInfo\x12\x0c\n\x04info\x18\x01 \x03(\t"~\n\nDeviceInfo\x12\x1f\n\x17cpuid_process_info_json\x18\x01 \x01(\t\x12\x13\n\x0bmac_address\x18\x02 \x01(\x04\x12\x15\n\rserial_number\x18\x03 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x04 \x01(\t\x12\r\n\x05model\x18\x05 \x01(\t"\x17\n\tMachineId\x12\n\n\x02id\x18\x01 \x01(\t"\xac\x04\n\x0cDropboxHosts\x12\x10\n\x08www_host\x18\x01 \x01(\t\x12\x13\n\x0bapiv2server\x18\x02 \x01(\t\x12\x12\n\nblock_host\x18\x04 \x01(\t\x12\x18\n\x10unity_flash_host\x18\x05 \x01(\t\x12\x16\n\x0eping_http_host\x18\x06 \x01(\t\x12\x12\n\npaper_host\x18\x07 \x01(\t\x12\x19\n\x11previews_dbx_host\x18\x08 \x01(\t\x12\x19\n\x11previews_duc_host\x18\t \x01(\t\x12\x10\n\x08sfe_host\x18\n \x01(\t\x12\x10\n\x08nsf_host\x18\x0b \x01(\t\x12\x18\n\x10apiv2blockserver\x18\x0c \x01(\t\x12\x14\n\x0cstaticserver\x18\r \x01(\t\x12\x14\n\x0cbeaconserver\x18\x0e \x01(\t\x12\x16\n\x0eblockexcserver\x18\x0f \x01(\t\x12\x12\n\nboltserver\x18\x10 \x01(\t\x12\x15\n\rmetaexcserver\x18\x11 \x01(\t\x12\x12\n\nmetaserver\x18\x12 \x01(\t\x12\x19\n\x11photo_blockserver\x18\x13 \x01(\t\x12\x15\n\rthunderserver\x18\x14 \x01(\t\x12\n\n\x02t8\x18\x15 \x01(\t\x12\n\n\x02d6\x18\x16 \x01(\t\x12\x13\n\x0breplay_host\x18\x17 \x01(\t\x12\x11\n\tpubserver\x18\x18 \x01(\t\x12\x19\n\x11edgelivecdnserver\x18\x19 \x01(\tJ\x04\x08\x03\x10\x04R\x11server_views_host2\xd9\x05\n\nAppInfoApi\x12H\n\rGetClientInfo\x12\x16.google.protobuf.Empty\x1a\x1f.dropbox.meta_engine.ClientInfo\x12R\n\x12GetPlatformVersion\x12\x16.google.protobuf.Empty\x1a$.dropbox.meta_engine.PlatformVersion\x12L\n\x0fGetInstallerTag\x12\x16.google.protobuf.Empty\x1a!.dropbox.meta_engine.InstallerTag\x12R\n\x12GetHostDisplayName\x12\x16.google.protobuf.Empty\x1a$.dropbox.meta_engine.HostDisplayName\x12]\n\x0fGetUnlinkCookie\x12\'.dropbox.meta_engine.GetUnlinkCookieReq\x1a!.dropbox.meta_engine.UnlinkCookie\x12L\n\x0fGetPlatformInfo\x12\x16.google.protobuf.Empty\x1a!.dropbox.meta_engine.PlatformInfo\x12H\n\rGetDeviceInfo\x12\x16.google.protobuf.Empty\x1a\x1f.dropbox.meta_engine.DeviceInfo\x12F\n\x0cGetMachineId\x12\x16.google.protobuf.Empty\x1a\x1e.dropbox.meta_engine.MachineId\x12L\n\x0fGetDropboxHosts\x12\x16.google.protobuf.Empty\x1a!.dropbox.meta_engine.DropboxHostsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_CLIENTINFO']._serialized_start = 82
    _globals['_CLIENTINFO']._serialized_end = 113
    _globals['_PLATFORMVERSION']._serialized_start = 115
    _globals['_PLATFORMVERSION']._serialized_end = 149
    _globals['_INSTALLERTAG']._serialized_start = 151
    _globals['_INSTALLERTAG']._serialized_end = 178
    _globals['_HOSTDISPLAYNAME']._serialized_start = 180
    _globals['_HOSTDISPLAYNAME']._serialized_end = 211
    _globals['_GETUNLINKCOOKIEREQ']._serialized_start = 213
    _globals['_GETUNLINKCOOKIEREQ']._serialized_end = 293
    _globals['_UNLINKCOOKIE']._serialized_start = 295
    _globals['_UNLINKCOOKIE']._serialized_end = 348
    _globals['_PLATFORMINFO']._serialized_start = 350
    _globals['_PLATFORMINFO']._serialized_end = 378
    _globals['_DEVICEINFO']._serialized_start = 380
    _globals['_DEVICEINFO']._serialized_end = 506
    _globals['_MACHINEID']._serialized_start = 508
    _globals['_MACHINEID']._serialized_end = 531
    _globals['_DROPBOXHOSTS']._serialized_start = 534
    _globals['_DROPBOXHOSTS']._serialized_end = 1090
    _globals['_APPINFOAPI']._serialized_start = 1093
    _globals['_APPINFOAPI']._serialized_end = 1822
    return None
