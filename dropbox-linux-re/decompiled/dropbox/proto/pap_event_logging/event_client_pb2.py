# Source Generated with Decompyle++
# File: event_client_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/pap_event_logging/event_client.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.pap_event_logging import enums_pb2 as dropbox_dot_proto_dot_pap__event__logging_dot_enums__pb2
from dropbox.proto.pap import event_state_pb2 as dropbox_dot_proto_dot_pap_dot_event__state__pb2
from dropbox.proto.pap import product_pb2 as dropbox_dot_proto_dot_pap_dot_product__pb2
from dropbox.proto.api_proxy.api_v2 import api_v2_pb2 as dropbox_dot_proto_dot_api__proxy_dot_api__v2_dot_api__v2__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2dropbox/proto/pap_event_logging/event_client.proto\x12\x11pap_event_logging\x1a+dropbox/proto/pap_event_logging/enums.proto\x1a#dropbox/proto/pap/event_state.proto\x1a\x1fdropbox/proto/pap/product.proto\x1a+dropbox/proto/api_proxy/api_v2/api_v2.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x91\x02\n\x12ClientEventEntries\x12@\n\x12application_fields\x18\x01 \x01(\x0b2$.pap_event_logging.ApplicationFields\x12<\n\rdevice_fields\x18\x02 \x01(\x0b2%.pap_event_logging.ClientDeviceFields\x12G\n\x16client_identity_fields\x18\x03 \x01(\x0b2\'.pap_event_logging.ClientIdentityFields\x122\n\x06events\x18\x04 \x03(\x0b2".pap_event_logging.ClientEventData"\xf3\x01\n\x11ApplicationFields\x12"\n\x0cproduct_name\x18\x01 \x01(\x0e2\x0c.pap.Product\x12\x15\n\rbuild_version\x18\x02 \x01(\t\x12<\n\x10operating_system\x18\x03 \x01(\x0e2".pap_event_logging.OperatingSystem\x12\x12\n\nos_version\x18\x04 \x01(\t\x126\n\rbuild_channel\x18\x05 \x01(\x0e2\x1f.pap_event_logging.BuildChannel\x12\x19\n\x11amplitude_api_key\x18\x06 \x01(\t"\xaa\x04\n\x12ClientDeviceFields\x122\n\x0bdevice_type\x18\x02 \x01(\x0e2\x1d.pap_event_logging.DeviceType\x12\x0e\n\x06locale\x18\x03 \x01(\t\x12F\n\x18client_web_device_fields\x18\n \x01(\x0b2".pap_event_logging.ClientWebFieldsH\x00\x12L\n\x1bclient_mobile_device_fields\x18\x0b \x01(\x0b2%.pap_event_logging.ClientMobileFieldsH\x00\x12N\n\x1cclient_desktop_device_fields\x18\x0c \x01(\x0b2&.pap_event_logging.ClientDesktopFieldsH\x00\x128\n\rserver_fields\x18\x0e \x01(\x0b2\x1f.pap_event_logging.ServerFieldsH\x00\x128\n\rcanary_fields\x18\x0f \x01(\x0b2\x1f.pap_event_logging.CanaryFieldsH\x00\x12A\n\x11web_device_fields\x18\r \x01(\x0b2$.pap_event_logging.InferredWebFieldsH\x01B\x11\n\x0fplatform_fieldsB\x1a\n\x18inferred_platform_fieldsJ\x04\x08\x01\x10\x02"\xef\x02\n\x14ClientIdentityFields\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x16\n\x0epaired_user_id\x18\x02 \x01(\x03\x12\x0f\n\x07team_id\x18\x03 \x01(\x03\x12\x1f\n\x0fforeign_user_id\x18\x05 \x01(\tB\x06\xa2\xa6\x1d\x02\x08\x01\x12H\n\x15foreign_user_provider\x18\x06 \x01(\x0e2).pap_event_logging.ForeignAccountProvider\x12T\n\x0fuser_properties\x18\x14 \x03(\x0b2;.pap_event_logging.ClientIdentityFields.UserPropertiesEntry\x12\x1f\n\x0fencoded_team_id\x18\x15 \x01(\tB\x06\xa2\xa6\x1d\x02\x08\x01\x1a5\n\x13UserPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01J\x04\x08\x04\x10\x05"=\n\x0fPredefinedEvent\x12\x14\n\x0cevent_action\x18\x01 \x01(\t\x12\x14\n\x0cevent_object\x18\x02 \x01(\t"!\n\x0bCustomEvent\x12\x12\n\nevent_name\x18\x01 \x01(\t"\xb4\x01\n\x16StormcrowExposureEvent\x12\x0f\n\x07feature\x18\x01 \x01(\t\x12\x1a\n\x12experiment_variant\x18\x02 \x01(\t\x12\x15\n\rpopulation_id\x18\x03 \x01(\t\x12\x14\n\x0cidentity_gid\x18\x04 \x01(\t\x12\x0f\n\x07host_id\x18\x05 \x01(\t\x12\x0e\n\x06app_id\x18\x06 \x01(\t\x12\x1f\n\x17stormcrow_metadata_json\x18\x07 \x01(\t"\xb7\x04\n\x0fClientEventData\x12\x1b\n\x13platform_session_id\x18\x01 \x01(\t\x12,\n\x08event_ts\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x12\n\nevent_guid\x18\x03 \x01(\t\x12>\n\x10predefined_event\x18\x04 \x01(\x0b2".pap_event_logging.PredefinedEventH\x00\x126\n\x0ccustom_event\x18\x05 \x01(\x0b2\x1e.pap_event_logging.CustomEventH\x00\x12M\n\x18stormcrow_exposure_event\x18\x0b \x01(\x0b2).pap_event_logging.StormcrowExposureEventH\x00\x12\x16\n\x0eaction_surface\x18\x06 \x01(\t\x12Y\n\x10event_properties\x18\x08 \x03(\x0b27.pap_event_logging.ClientEventData.EventPropertiesEntryB\x06\xa2\xa6\x1d\x02\x08\x01\x12$\n\x0bevent_state\x18\t \x01(\x0e2\x0f.pap.EventState\x12\x13\n\x0bevent_class\x18\n \x01(\t\x1a6\n\x14EventPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x12\n\x10event_identifierJ\x04\x08\x07\x10\x08"\x9f\x02\n\x0fClientWebFields\x12\x13\n\x03url\x18\x02 \x01(\tB\x06\xa2\xa6\x1d\x02\x08\x01\x12\x18\n\x08referrer\x18\x03 \x01(\tB\x06\xa2\xa6\x1d\x02\x08\x01\x12\x1d\n\x15is_br_cookies_enabled\x18\x05 \x01(\x08\x12\x17\n\x0fua_browser_lang\x18\x08 \x01(\t\x12\x19\n\x11ua_br_color_depth\x18\n \x01(\x03\x12\x1d\n\x15ua_br_viewport_height\x18\x0b \x01(\x03\x12\x1c\n\x14ua_br_viewport_width\x18\x0c \x01(\x03\x12\x1c\n\x14device_screen_height\x18\r \x01(\x03\x12\x1b\n\x13device_screen_width\x18\x0e \x01(\x03\x12\x12\n\nrequest_id\x18\x0f \x01(\t"\x8d\x01\n\x11InferredWebFields\x12\x12\n\nuser_agent\x18\x01 \x01(\t\x12\x11\n\tcookie_id\x18\x04 \x01(\t\x12\x17\n\x0fua_browser_name\x18\x06 \x01(\t\x12\x1a\n\x12ua_browser_version\x18\x07 \x01(\t\x12\x1c\n\x14locale_user_selected\x18\t \x01(\t"\x92\x02\n\x12ClientMobileFields\x12A\n\x10device_conn_type\x18\x01 \x01(\x0e2\'.pap_event_logging.DeviceConnectionType\x12\x14\n\x0cdevice_model\x18\x03 \x01(\t\x12\x1b\n\x13device_manufacturer\x18\x04 \x01(\t\x12\x12\n\nuptime_sec\x18\x05 \x01(\x03\x12C\n\x14device_battery_level\x18\x06 \x01(\x0e2%.pap_event_logging.DeviceBatteryLevel\x12\x1a\n\x12is_device_charging\x18\x07 \x01(\x08\x12\x11\n\tdevice_id\x18\x08 \x01(\t"(\n\x13ClientDesktopFields\x12\x11\n\tdevice_id\x18\x08 \x01(\t"\x0e\n\x0cServerFields"*\n\x0cCanaryFields\x12\x1a\n\x12is_device_charging\x18\x01 \x01(\x08BL\n#com.dropbox.proto.pap_event_loggingP\x01Z\x1fdropbox/proto/pap_event_logging\x80\xa7\x1d\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.pap_event_logging.event_client_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.dropbox.proto.pap_event_loggingP\x01Z\x1fdropbox/proto/pap_event_logging\x80\xa7\x1d\x01'
    _globals['_CLIENTIDENTITYFIELDS_USERPROPERTIESENTRY']._loaded_options = None
    _globals['_CLIENTIDENTITYFIELDS_USERPROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_CLIENTIDENTITYFIELDS'].fields_by_name['foreign_user_id']._loaded_options = None
    _globals['_CLIENTIDENTITYFIELDS'].fields_by_name['foreign_user_id']._serialized_options = b'\xa2\xa6\x1d\x02\x08\x01'
    _globals['_CLIENTIDENTITYFIELDS'].fields_by_name['encoded_team_id']._loaded_options = None
    _globals['_CLIENTIDENTITYFIELDS'].fields_by_name['encoded_team_id']._serialized_options = b'\xa2\xa6\x1d\x02\x08\x01'
    _globals['_CLIENTEVENTDATA_EVENTPROPERTIESENTRY']._loaded_options = None
    _globals['_CLIENTEVENTDATA_EVENTPROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_CLIENTEVENTDATA'].fields_by_name['event_properties']._loaded_options = None
    _globals['_CLIENTEVENTDATA'].fields_by_name['event_properties']._serialized_options = b'\xa2\xa6\x1d\x02\x08\x01'
    _globals['_CLIENTWEBFIELDS'].fields_by_name['url']._loaded_options = None
    _globals['_CLIENTWEBFIELDS'].fields_by_name['url']._serialized_options = b'\xa2\xa6\x1d\x02\x08\x01'
    _globals['_CLIENTWEBFIELDS'].fields_by_name['referrer']._loaded_options = None
    _globals['_CLIENTWEBFIELDS'].fields_by_name['referrer']._serialized_options = b'\xa2\xa6\x1d\x02\x08\x01'
    _globals['_CLIENTEVENTENTRIES']._serialized_start = 267
    _globals['_CLIENTEVENTENTRIES']._serialized_end = 540
    _globals['_APPLICATIONFIELDS']._serialized_start = 543
    _globals['_APPLICATIONFIELDS']._serialized_end = 786
    _globals['_CLIENTDEVICEFIELDS']._serialized_start = 789
    _globals['_CLIENTDEVICEFIELDS']._serialized_end = 1343
    _globals['_CLIENTIDENTITYFIELDS']._serialized_start = 1346
    _globals['_CLIENTIDENTITYFIELDS']._serialized_end = 1713
    _globals['_CLIENTIDENTITYFIELDS_USERPROPERTIESENTRY']._serialized_start = 1654
    _globals['_CLIENTIDENTITYFIELDS_USERPROPERTIESENTRY']._serialized_end = 1707
    _globals['_PREDEFINEDEVENT']._serialized_start = 1715
    _globals['_PREDEFINEDEVENT']._serialized_end = 1776
    _globals['_CUSTOMEVENT']._serialized_start = 1778
    _globals['_CUSTOMEVENT']._serialized_end = 1811
    _globals['_STORMCROWEXPOSUREEVENT']._serialized_start = 1814
    _globals['_STORMCROWEXPOSUREEVENT']._serialized_end = 1994
    _globals['_CLIENTEVENTDATA']._serialized_start = 1997
    _globals['_CLIENTEVENTDATA']._serialized_end = 2564
    _globals['_CLIENTEVENTDATA_EVENTPROPERTIESENTRY']._serialized_start = 2484
    _globals['_CLIENTEVENTDATA_EVENTPROPERTIESENTRY']._serialized_end = 2538
    _globals['_CLIENTWEBFIELDS']._serialized_start = 2567
    _globals['_CLIENTWEBFIELDS']._serialized_end = 2854
    _globals['_INFERREDWEBFIELDS']._serialized_start = 2857
    _globals['_INFERREDWEBFIELDS']._serialized_end = 2998
    _globals['_CLIENTMOBILEFIELDS']._serialized_start = 3001
    _globals['_CLIENTMOBILEFIELDS']._serialized_end = 3275
    _globals['_CLIENTDESKTOPFIELDS']._serialized_start = 3277
    _globals['_CLIENTDESKTOPFIELDS']._serialized_end = 3317
    _globals['_SERVERFIELDS']._serialized_start = 3319
    _globals['_SERVERFIELDS']._serialized_end = 3333
    _globals['_CANARYFIELDS']._serialized_start = 3335
    _globals['_CANARYFIELDS']._serialized_end = 3377
    return None
