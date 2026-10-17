# Source Generated with Decompyle++
# File: api_utils.pyc (Python 3.11)

from typing import Optional, Text
from dropbox.api.v2.datatypes.external_drive_backup import GetEligibilityInfoResult, ListBackupsResult
from dropbox.api.v2.datatypes.growth import NpTrialStartArg, NpTrialStartResult
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.external_drive_backup.event_reporter import OperationEventSession
from dropbox.client.features.external_drive_backup.server_interface import catch_and_convert_network_exceptions, ServerInterface
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client_api.apiv2.generated.growth import Growth
from dropbox.client_api.connection.interface import HostKeyAuth
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.basic import flatten_future
from dropbox.foundation.transitional import make_delayed_network_call
from dropbox.trace import TRACE
start_ncct_trial = (lambda user_context = None, session_id = None: pass# WARNING: Decompyle incomplete
)()
list_backups = (lambda session_id = None, user_context = None, source = future_function, include_last_ts = (False,): session = OperationEventSession(user_context.account, user_context.metrics_reporter, session_id, source, trace_only = False)reporter = session.new_reporter(ExternalBackupEvent.call_server_list_backups, amp_only = True)server_interface = ServerInterface(user_context, UNSAFE_get_raw_machine_uuid())list_backups_future = catch_and_convert_network_exceptions(server_interface.list_backups(include_last_ts))reporter.wrap(list_backups_future))()
get_eligibility_info = (lambda session_id = None, user_context = None, source = future_function: 
def _process_res(res = None):
if not res.is_ineligible:
ResolvedFuture(False)ResolvedFuture(True)session = OperationEventSession(user_context.account, user_context.metrics_reporter, session_id, source, trace_only = False)reporter = session.new_reporter(ExternalBackupEvent.call_get_eligibility_info, amp_only = True)server_interface = ServerInterface(user_context, UNSAFE_get_raw_machine_uuid())get_eligiblity_info_future = catch_and_convert_network_exceptions(server_interface.get_eligibility_info())reporter.wrap(get_eligiblity_info_future).then(_process_res))()
