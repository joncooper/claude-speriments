# Source Generated with Decompyle++
# File: capture_pap_logger.pyc (Python 3.11)

from typing import Text
from dropbox.client.analytics import log_pap_event
from dropbox.pap.events.enums.share_link_type_pb2 import ShareLinkType
from dropbox.pap.events.enums.shared_link_origin_pb2 import SharedLinkOrigin
from dropbox.pap.events.share.copy_capture_shared_link_pb2 import Copy_CaptureSharedLink
from dropbox.pap_event_logging.utils import get_enum_value_for_string
from dropbox.proto.pap.event_state_pb2 import EventState
from dropbox.sharing.sharing_logger import ShareDesktopTiburonEvent
_TIBURON_EVENTS_TO_EVENT_STATE_MAP = {
    ShareDesktopTiburonEvent.COPY_CAPTURE_SHARED_LINK_OVERQUOTA: EventState.FAILED,
    ShareDesktopTiburonEvent.INITIATE_COPY_CAPTURE_SHARED_LINK: EventState.START,
    ShareDesktopTiburonEvent.COPY_CAPTURE_SHARED_LINK_SUCCESS: EventState.SUCCESS,
    ShareDesktopTiburonEvent.COPY_CAPTURE_SHARED_LINK_ERROR: EventState.FAILED }

def log_to_pap_for_eligible_events(is_dir = None, share_link_type = None, shared_link_origin = None, tib_event = ('is_dir', 'bool', 'share_link_type', 'Text', 'shared_link_origin', 'Text', 'tib_event', 'ShareDesktopTiburonEvent')):
    event_state = _TIBURON_EVENTS_TO_EVENT_STATE_MAP.get(tib_event, None)
    if not event_state:
        return None
    is_capture_overquota = bool(tib_event == ShareDesktopTiburonEvent.COPY_CAPTURE_SHARED_LINK_OVERQUOTA)
    shared_link_origin_enum_value = get_enum_value_for_string(SharedLinkOrigin, shared_link_origin)
    share_link_type_enum_value = get_enum_value_for_string(ShareLinkType, share_link_type)
    log_pap_event(Copy_CaptureSharedLink(shared_link_origin = shared_link_origin_enum_value, is_capture_over_quota = is_capture_overquota, event_state = event_state, share_link_type = share_link_type_enum_value, is_dir = is_dir))

