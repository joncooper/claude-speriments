# Source Generated with Decompyle++
# File: eligibility_cache.pyc (Python 3.11)

from enum import StrEnum
from typing import Any, Callable, Dict, List, Mapping, Optional, TYPE_CHECKING
from dropbox.client.fenix.constants import EventHubEvents
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import ResolvedFuture
from dropbox.foundation.futures.basic import Future
from dropbox.trace import TRACE
if TYPE_CHECKING:
    from dropbox.client.fenix.event_hub import EventHub

class FenixEligibilityGates(StrEnum):
    BRIDGE_V2_ENABLED = 'bridge_v2_enabled'


class FenixEligibilityCache:
    Instance: "'Optional[FenixEligibilityCache]'" = None
    
    def __init__(self = None):
        self._eligible_by_account = { }
        self._change_callbacks = []
        self._initialized = False

    
    def initialize(self = None, event_hub = None):
        if self._initialized:
            return None
        self._initialized = None
        event_hub.register_for_invocation(EventHubEvents.FENIX_ELIGIBILITY_CHANGED, self.on_event).ground(component = DesktopComponent.FOREGROUND_SURFACE)

    
    def is_eligible(self = None, account_id = None, feature_name = None):
        return self._eligible_by_account.get(account_id, { }).get(feature_name, False)

    
    def add_change_callback(self = None, callback = None):
        if callback not in self._change_callbacks:
            self._change_callbacks.append(callback)
            return None

    
    def remove_change_callback(self = None, callback = None):
        if callback in self._change_callbacks:
            self._change_callbacks.remove(callback)
            return None

    
    def _notify_change(self = None, account_id = None):
        for callback in list(self._change_callbacks):
            callback(account_id)
            except Exception:
                report_exception(severity = Severity.WARN, component = DesktopComponent.FOREGROUND_SURFACE)
                continue
            return None

    
    def on_event(self = None, event_arg = None):
        if not isinstance(event_arg, Mapping):
            TRACE('FenixEligibilityCache.on_event: payload is not a mapping, ignoring event')
            return ResolvedFuture(None)
        account_id = None.get('account_id')
        feature_name = event_arg.get('feature_name')
        if not isinstance(account_id, str) and account_id and isinstance(feature_name, str) or feature_name:
            TRACE('FenixEligibilityCache.on_event: missing account_id or feature_name, ignoring event')
            return ResolvedFuture(None)
        eligible = None.get('eligible')
        if not isinstance(eligible, bool):
            TRACE('FenixEligibilityCache.on_event: missing or malformed eligible, ignoring event')
            return ResolvedFuture(None)
        by_feature = None._eligible_by_account.setdefault(account_id, { })
        changed = by_feature.get(feature_name) != eligible
        by_feature[feature_name] = eligible
        if changed:
            self._notify_change(account_id)
        return ResolvedFuture(None)


FenixEligibilityCache.Instance = FenixEligibilityCache()
