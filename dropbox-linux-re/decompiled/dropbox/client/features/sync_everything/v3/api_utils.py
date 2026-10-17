# Source Generated with Decompyle++
# File: api_utils.pyc (Python 3.11)

from time import time
from typing import Optional, Text
from uuid import UUID
from dropbox.api.v2.datatypes.growth import UserActionPerformedArg
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.sync_everything.constants import BackupDisableType
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.device_state import DeviceState
from dropbox.client.features.sync_everything.v3.event_reporter import OperationEventSession
from dropbox.client.features.sync_everything.v3.server_interface import catch_and_convert_network_exceptions_compute_device_name, catch_and_convert_network_exceptions_device_status, catch_and_convert_network_exceptions_force_disable, catch_and_convert_network_exceptions_list_backups, ServerInterface
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingEvent
from dropbox.client.features.sync_everything.view_model.bridge_gen.list_backups_result import ListBackupsResult
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client_api.apiv2.generated.growth import Growth
from dropbox.client_api.connection.interface import HostKeyAuth
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.basic import flatten_future
from dropbox.foundation.transitional import make_delayed_network_call
from dropbox.platform import IS_MAC
from dropbox.trace import TRACE
list_backups = (lambda session_id = None, user_context = None, source = future_function, include_last_ts = (False,): pass# WARNING: Decompyle incomplete
)()
next_available_name = (lambda context = None: platform_name = 'Mac' if IS_MAC else 'PC'compute_device_name(platform_name, context))()
compute_device_name = (lambda device_name_base = None, user_context = None: session = OperationEventSession(user_context.account, user_context.metrics_reporter, session_id = None, source = None)reporter = session.new_reporter(SyncEverythingEvent.compute_device_name)server_interface = ServerInterface(user_context, UNSAFE_get_raw_machine_uuid())compute_device_name_future = catch_and_convert_network_exceptions_compute_device_name(server_interface.compute_device_name(device_name_base))reporter.wrap(compute_device_name_future))()
get_device_state = (lambda session_id = None, user_context = None, source = future_function, machine_uuid = ('session_id', 'Text', 'user_context', 'UserContext', 'source', 'Source', 'machine_uuid', 'UUID', 'return', 'Future[DeviceState]'): session = OperationEventSession(user_context.account, user_context.metrics_reporter, session_id, source)reporter = session.new_reporter(SyncEverythingEvent.get_device_state)server_interface = ServerInterface(user_context, machine_uuid)device_state_on_server = catch_and_convert_network_exceptions_device_status(server_interface.device_status(validate = False))reporter.wrap(device_state_on_server))()
force_disable_other_backups = (lambda session_id, user_context = None, source = None, device_id = future_function, backup_disable_type = ('session_id', 'Text', 'user_context', 'Optional[UserContext]', 'source', 'Source', 'device_id', 'str', 'backup_disable_type', 'BackupDisableType', 'return', 'Future[None]'): pass# WARNING: Decompyle incomplete
)()
is_user_viral_signup = (lambda connection = None, account = None: pass# WARNING: Decompyle incomplete
)()
get_plan_name = (lambda connection = None, account = None: pass# WARNING: Decompyle incomplete
)()
