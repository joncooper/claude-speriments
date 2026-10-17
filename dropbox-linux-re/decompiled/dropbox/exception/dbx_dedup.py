# Source Generated with Decompyle++
# File: dbx_dedup.pyc (Python 3.11)

from apex.metrics import Metric, MetricsReporter
import sentry_sdk
from dropbox.event import report
from sentry_sdk.utils import ContextVar
from sentry_sdk.integrations import Integration
from sentry_sdk.scope import add_global_event_processor
from typing import TYPE_CHECKING, Union, Dict, Any, Tuple, Set
from dropbox.client.device_info import get_machine_uuid
if TYPE_CHECKING:
    from typing import Optional
    from sentry_sdk._types import Event, Hint
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.main_utility import DropboxApplicationUtility

class DbxDedupeIntegration(Integration):
    identifier = 'dbx_dedupe'
    
    def __init__(self = None, app = None):
        self._last_seen = ContextVar('last-seen')
        self._app = app

    
    def _flatten_context_to_map(self = None, d = None, parent_key = None, sep = ('', '_', None), exclude_contexts = ('exclude_contexts', 'Optional[Set[str]]', 'return', 'Dict[str, str]')):
        if not exclude_contexts:
            pass
        exclude_contexts = set()
        items = { }
    # WARNING: Decompyle incomplete

    
    def _convert_tags_to_map(self = None, tags_dict = None, exclude_tags = None):
        if not exclude_tags:
            pass
        exclude_tags = set()
        result = { }
    # WARNING: Decompyle incomplete

    
    def _extract_exception_info(self = None, event = None):
        exception_type = 'unknown'
        exception_value = 'unknown'
        exception_data = event.get('exception', { })
        if exception_data and 'values' in exception_data:
            exception_values = exception_data.get('values', [])
            if exception_values and len(exception_values) > 0:
                first_exception = exception_values[0]
                exception_type = first_exception.get('type', 'unknown')
                exception_value = first_exception.get('value', 'unknown')
        return (exception_type, exception_value)

    setup_once = (lambda : processor = (lambda event = None, hint = None: pass# WARNING: Decompyle incomplete
)()
)()
    reset_last_seen = (lambda : integration = sentry_sdk.get_client().get_integration(DbxDedupeIntegration)# WARNING: Decompyle incomplete
)()

