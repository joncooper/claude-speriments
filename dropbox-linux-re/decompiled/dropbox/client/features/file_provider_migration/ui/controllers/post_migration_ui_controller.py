# Source Generated with Decompyle++
# File: post_migration_ui_controller.pyc (Python 3.11)

import math
import time
from typing import List, Optional
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.apollo_alerts.model.apollo_alerts import AlertResult, ApolloAlerts
from dropbox.client.features.file_provider_migration.file_provider_migration_logger import FileProviderMigrationEvent, FileProviderMigrationLogger
from dropbox.client.features.file_provider_migration.migration_session import FPMigrationSessionData
from dropbox.client.features.file_provider_migration.ui.strings import FileProviderStrings
from dropbox.client.features.os_consent.os_consent_flow import OSConsentFlow
from dropbox.client.features.tour.constants import TourState, TourViewKeys
from dropbox.client.features.tour.controller import TourController
from dropbox.client.features.tour.ui.bridge_gen.tour_variant import TourVariant
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future, ResolvedFuture, sleep_async
from dropbox.foundation.navigation_service.interface import ViewHandle
from dropbox.foundation.navigation_service.manifest_registry import FP_MIGRATION_EDUCATION_CAROUSEL, FP_MIGRATION_INTERIM_CAROUSEL
from dropbox.foundation.navigation_service.view_interface import StandaloneViewIdentifier
from dropbox.foundation.navigation_service.window_manager_delegate import WindowManagerDelegateInterface
from dropbox.foundation.navigation_service.window_manager_delegate.types import WindowManagerDelegateType
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.sync_root.accessor import RootManagerAccessor
from dropbox.trace import TRACE
SHOW_FEEDBACK_MODAL_DELAY_SECONDS = 3
MIN_SECONDS_SHOW_INTERIM_CAROUSEL = 2
SHOW_TOUR_DELAY_SECONDS = 3
CLOSE_POST_MIGRATION_CAROUSEL_DELAY_SECONDS = 180
INTERIM_CAROUSEL_VIEW_KEY = 'interim_carousel'
FP_MIGRATION_EDUCATION_CAROUSEL_VIEW_KEY = 'education_carousel'

class FPPostMigrationFlowUiController(SingletonActor):
    pass
# WARNING: Decompyle incomplete

