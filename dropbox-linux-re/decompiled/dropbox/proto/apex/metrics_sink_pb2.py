# Source Generated with Decompyle++
# File: metrics_sink_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/apex/metrics_sink.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%dropbox/proto/apex/metrics_sink.proto\x12\x04apex"6\n\x12MetricsSinkRequest\x12 \n\x05spans\x18\x01 \x03(\x0b2\x11.apex.MetricsSpan"X\n\x0bMetricsSpan\x12\n\n\x02ns\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1e\n\x04tags\x18\x03 \x03(\x0b2\x10.apex.MetricsTag\x12\x0f\n\x07samples\x18\x04 \x03(\x01"&\n\nMetricsTag\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0b\n\x03val\x18\x02 \x01(\t"\x15\n\x13MetricsSinkResponse"1\n\x1eMetricsDaemonHeartbeatResponse\x12\x0f\n\x07version\x18\x01 \x01(\t2S\n\x0bMetricsSink\x12D\n\x0bSubmitSpans\x12\x18.apex.MetricsSinkRequest\x1a\x19.apex.MetricsSinkResponse"\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.apex.metrics_sink_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_METRICSSINKREQUEST']._serialized_start = 47
    _globals['_METRICSSINKREQUEST']._serialized_end = 101
    _globals['_METRICSSPAN']._serialized_start = 103
    _globals['_METRICSSPAN']._serialized_end = 191
    _globals['_METRICSTAG']._serialized_start = 193
    _globals['_METRICSTAG']._serialized_end = 231
    _globals['_METRICSSINKRESPONSE']._serialized_start = 233
    _globals['_METRICSSINKRESPONSE']._serialized_end = 254
    _globals['_METRICSDAEMONHEARTBEATRESPONSE']._serialized_start = 256
    _globals['_METRICSDAEMONHEARTBEATRESPONSE']._serialized_end = 305
    _globals['_METRICSSINK']._serialized_start = 307
    _globals['_METRICSSINK']._serialized_end = 390
    return None
