# Source Generated with Decompyle++
# File: select_overquota_restrictions_modal_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/quota/select_overquota_restrictions_modal.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.pap import options_pb2 as dropbox_dot_proto_dot_pap_dot_options__pb2
from dropbox.pap.events.enums import over_quota_sweep_blocking_modal_action_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_over__quota__sweep__blocking__modal__action__pb2
from dropbox.pap.events.enums import organic_or_churned_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_organic__or__churned__pb2
from dropbox.pap.events.enums import plan_shown_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_plan__shown__pb2
from dropbox.pap.events.enums import discount_source_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_discount__source__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBdropbox/pap/events/quota/select_overquota_restrictions_modal.proto\x12\x10pap.events.quota\x1a\x1fdropbox/proto/pap/options.proto\x1aEdropbox/pap/events/enums/over_quota_sweep_blocking_modal_action.proto\x1a1dropbox/pap/events/enums/organic_or_churned.proto\x1a)dropbox/pap/events/enums/plan_shown.proto\x1a.dropbox/pap/events/enums/discount_source.proto"\xba\x05\n!Select_OverquotaRestrictionsModal\x12\x16\n\x0eaction_surface\x18\x01 \x01(\t\x12T\n\x0bevent_class\x18\xcd\x08 \x01(\x0e2>.pap.events.quota.Select_OverquotaRestrictionsModal.EventClass\x12\x7f\n&over_quota_sweep_blocking_modal_action\x18\x02 \x01(\x0e2O.enums.over_quota_sweep_blocking_modal_action.OverQuotaSweepBlockingModalAction\x12\x13\n\x0bquota_limit\x18\x03 \x01(\x03\x12\x12\n\nquota_used\x18\x04 \x01(\x03\x12\x19\n\x11seconds_overquota\x18\x05 \x01(\x03\x12\x12\n\nhardlocked\x18\x06 \x01(\x08\x12F\n\x12organic_or_churned\x18\x07 \x01(\x0e2*.enums.organic_or_churned.OrganicOrChurned\x12/\n\nplan_shown\x18\x08 \x01(\x0e2\x1b.enums.plan_shown.PlanShown\x12%\n\x1drestrictions_start_date_shown\x18\t \x01(\x08\x12\x13\n\x0bhardblocked\x18\n \x01(\x08\x12\x16\n\x0eaction_element\x18\x0b \x01(\t\x12>\n\x0fdiscount_source\x18\x0c \x01(\x0e2%.enums.discount_source.DiscountSource"\x17\n\nEventClass\x12\t\n\x05QUOTA\x10\x00:(\xca>\x06select\xd2>\x1coverquota_restrictions_modalB\x1aZ\x18dropbox/pap/events/quotab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.quota.select_overquota_restrictions_modal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x18dropbox/pap/events/quota'
    _globals['_SELECT_OVERQUOTARESTRICTIONSMODAL']._loaded_options = None
    _globals['_SELECT_OVERQUOTARESTRICTIONSMODAL']._serialized_options = b'\xca>\x06select\xd2>\x1coverquota_restrictions_modal'
    _globals['_SELECT_OVERQUOTARESTRICTIONSMODAL']._serialized_start = 335
    _globals['_SELECT_OVERQUOTARESTRICTIONSMODAL']._serialized_end = 1033
    _globals['_SELECT_OVERQUOTARESTRICTIONSMODAL_EVENTCLASS']._serialized_start = 968
    _globals['_SELECT_OVERQUOTARESTRICTIONSMODAL_EVENTCLASS']._serialized_end = 991
    return None
