# Source Generated with Decompyle++
# File: welcome_flow_view_response.pyc (Python 3.11)

from enum import Enum, StrEnum
from typing import NamedTuple, Optional
from dropbox.foundation.html_views.electron.ipc import JSONDict

class WelcomeFlowVariant(StrEnum):
    DEFAULT = 'DEFAULT'
    CONTEXT_ONBOARDING = 'CONTEXT_ONBOARDING'
    CONTEXT_ONBOARDING_EDGE_CASES = 'CONTEXT_ONBOARDING_EDGE_CASES'


class UpsellVariant(StrEnum):
    OFF = 'UPSELL_OFF'
    CONTROL = 'UPSELL_CONTROL'
    V1 = 'UPSELL_V1'
    V2 = 'UPSELL_V2'
    V3 = 'UPSELL_V3'


class WelcomeFlowViewStatus(Enum):
    FULFILLED = 1
    REJECTED = 2
    UNKNOWN = 3


class WelcomeFlowViewResponse(NamedTuple):
    restart_on_exception: 'bool' = 'WelcomeFlowViewResponse'
    from_json = (lambda response_proto = None: response = response_proto['handlerResponses'][0]if response['status'] == 'rejected':
WelcomeFlowViewResponse(status = WelcomeFlowViewStatus.REJECTED, has_exception = True, account_linked = False, user_journey_already_active = False, exception_reason = response.get('reason', None), restart_on_exception = False)if None['status'] == 'fulfilled':
WelcomeFlowViewResponse(status = WelcomeFlowViewStatus.FULFILLED, has_exception = response['value'].get('hasException', False), account_linked = response['value'].get('accountLinked', False), user_journey_already_active = response['value'].get('userJourneyAlreadyActive', False), exception_reason = response['value'].get('exceptionReason', None), restart_on_exception = response['value'].get('restartOnException', False))WelcomeFlowViewResponse(status = WelcomeFlowViewStatus.UNKNOWN, has_exception = True, account_linked = False, user_journey_already_active = False, exception_reason = 'Future was not resolved', restart_on_exception = response['value'].get('restartOnException', False)))()

