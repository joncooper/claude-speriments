# Source Generated with Decompyle++
# File: tray_service.pyc (Python 3.11)

import os
from typing import Dict, Optional, Tuple
from urllib.parse import parse_qs, urlparse
from uuid import uuid4
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.types import AccountId
from dropbox.client.client_shmodel import ClientShmodelOrigin
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.features.home_feed.shared.model.feed_update_client import AssistantFeedUpdateClient
from dropbox.client.features.notification_dialog.constants import NotificationDialogEntryPoint
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.journeys.tray.tray_utils import parse_bool_arg, parse_optional_str_arg
from dropbox.client.fenix.utils import get_account_linked_or_from_cache
from dropbox.client.ui.common.tray_popup_constants import TrayTriggerReason
from dropbox.client.ui.common.tray_upgrade_button import TrayUpgradeButtonController
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.basic import EasyFuture, IncompleteFutureException
from dropbox.foundation.futures.helpers import FutureHelpers
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.html_views.electron.ipc._interface import JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.navigation_service.manifest_registry import AccountSwitcherNavParams, SETUP_WIZARD, SHARE_DIALOG, SharingDialogParams
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.model.types import FileId
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import ServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
_DROPBOX_SHARED_LINK_HOSTS = frozenset(('dropbox.com', 'www.dropbox.com'))
_PAPER_SHARED_LINK_HOST = 'paper.dropbox.com'

class TrayService(Actor):
    pass
# WARNING: Decompyle incomplete

