# Source Generated with Decompyle++
# File: enums_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/pap_event_logging/enums.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.api_proxy.api_v2 import api_v2_pb2 as dropbox_dot_proto_dot_api__proxy_dot_api__v2_dot_api__v2__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+dropbox/proto/pap_event_logging/enums.proto\x12\x11pap_event_logging\x1a+dropbox/proto/api_proxy/api_v2/api_v2.proto*\x85\x01\n\x0fOperatingSystem\x12\x1c\n\x18UNKNOWN_OPERATING_SYSTEM\x10\x00\x12\x07\n\x03IOS\x10\x01\x12\x0b\n\x07ANDROID\x10\x02\x12\x0e\n\nBLACKBERRY\x10\x03\x12\x0b\n\x07WINDOWS\x10\n\x12\x07\n\x03MAC\x10\x0b\x12\t\n\x05LINUX\x10\x0c\x12\r\n\tCHROME_OS\x10\r*I\n\nDeviceType\x12\x17\n\x13UNKNOWN_DEVICE_TYPE\x10\x00\x12\t\n\x05PHONE\x10\x01\x12\n\n\x06TABLET\x10\x02\x12\x0b\n\x07DESKTOP\x10\x03*\\\n\x14DeviceConnectionType\x12"\n\x1eUNKNOWN_DEVICE_CONNECTION_TYPE\x10\x00\x12\x08\n\x04WIFI\x10\x01\x12\x0c\n\x08CELLULAR\x10\x02\x12\x08\n\x04NONE\x10\x03*N\n\x12DeviceBatteryLevel\x12\x19\n\x15UNKNOWN_BATTERY_LEVEL\x10\x00\x12\x07\n\x03LOW\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\x08\n\x04HIGH\x10\x03*p\n\x0cBuildChannel\x12\x19\n\x15UNKNOWN_BUILD_CHANNEL\x10\x00\x12\x12\n\x0eINTERNAL_ALPHA\x10\x01\x12\x08\n\x04BETA\x10\x02\x12\n\n\x06STABLE\x10\x03\x12\x07\n\x03DEV\x10\x04\x12\x12\n\x0eEXTERNAL_ALPHA\x10\x05*`\n\x16ForeignAccountProvider\x12\x16\n\x12NO_FOREIGN_ACCOUNT\x10\x00\x12\r\n\tHELLOSIGN\x10\x01\x12\x0b\n\x07DOCSEND\x10\x02\x12\x12\n\x0eDBX_ACCOUNT_ID\x10\x03BL\n#com.dropbox.proto.pap_event_loggingP\x01Z\x1fdropbox/proto/pap_event_logging\x80\xa7\x1d\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.pap_event_logging.enums_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.dropbox.proto.pap_event_loggingP\x01Z\x1fdropbox/proto/pap_event_logging\x80\xa7\x1d\x01'
    _globals['_OPERATINGSYSTEM']._serialized_start = 112
    _globals['_OPERATINGSYSTEM']._serialized_end = 245
    _globals['_DEVICETYPE']._serialized_start = 247
    _globals['_DEVICETYPE']._serialized_end = 320
    _globals['_DEVICECONNECTIONTYPE']._serialized_start = 322
    _globals['_DEVICECONNECTIONTYPE']._serialized_end = 414
    _globals['_DEVICEBATTERYLEVEL']._serialized_start = 416
    _globals['_DEVICEBATTERYLEVEL']._serialized_end = 494
    _globals['_BUILDCHANNEL']._serialized_start = 496
    _globals['_BUILDCHANNEL']._serialized_end = 608
    _globals['_FOREIGNACCOUNTPROVIDER']._serialized_start = 610
    _globals['_FOREIGNACCOUNTPROVIDER']._serialized_end = 706
    return None
