# Source Generated with Decompyle++
# File: controller.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.tour.constants import TourState, TourViewKeys
from dropbox.client.features.tour.logger import DesktopTourLogger
from dropbox.client.features.tour.ui.bridge_gen.tour_variant import TourVariant
from dropbox.client.features.tour.ui.bridge_gen.tour_variant_nav_params import TourVariantNavParams
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.navigation_service.manifest_registry import TOUR_CAROUSEL
from dropbox.foundation.navigation_service.view_interface import StandaloneViewIdentifier
from dropbox.foundation.navigation_service.window_manager_delegate import WindowManagerDelegateInterface
from dropbox.foundation.navigation_service.window_manager_delegate.types import WindowManagerDelegateType
from dropbox.foundation.raii2.singleton import SingletonActor

class TourController(SingletonActor):
    pass
# WARNING: Decompyle incomplete

