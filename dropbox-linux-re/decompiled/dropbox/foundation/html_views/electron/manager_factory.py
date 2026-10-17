# Source Generated with Decompyle++
# File: manager_factory.pyc (Python 3.11)

from typing import Callable
import dropbox.client.features.model_registry as dropbox
from dropbox.callbacks import Handler
from dropbox.foundation.context import Context
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.html_views.common.manager import HtmlViewManager
from dropbox.foundation.html_views.common.navigation_rules import KNOWN_SCHEME_HANDLER_LOCAL, LOCAL_VIEW_CONTENT_DOMAIN
from dropbox.foundation.html_views.electron.host_driver import ElectronHostDriver
from dropbox.foundation.html_views.electron.scheme_handler_bridge import ElectronSchemeHandlerBridge
from dropbox.foundation.html_views.electron.view import ElectronWebContents
from dropbox.foundation.html_views.electron.view_factory import ElectronHtmlViewFactory
from dropbox.foundation.html_views.local.common.html_previews_handler import LocalViewHtmlPreviewsHandler
from dropbox.foundation.html_views.local.common.img_handler import LocalViewNativeImgHandler
from dropbox.foundation.html_views.local.common.local_view_factory import check_if_js_bundles_were_build_with_prod, LocalViewFactory, LocalViewManagerStrategy
from dropbox.foundation.html_views.local.common.previews_handler import LocalViewPreviewsAssetHandler
from dropbox.foundation.html_views.local.common.view import create_local_view_state_machine_strategy
from dropbox.foundation.navigation_service.bridge_gen.bridge_interface_activity_monitor import ActivityMonitorBridgeInterface
from dropbox.foundation.navigation_service.interface import NavigationServiceInterface
from dropbox.foundation.navigation_service.view_manager_interface import ViewManagerInterface
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.raii2.wrappers import Transferable
from dropbox.foundation.scheme_handler.router import CustomSchemeRouter

def ElectronHtmlViewManager():
    '''ElectronHtmlViewManager'''
    embeddable_view_type = (lambda self = None: ElectronWebContents)()

ElectronHtmlViewManager = <NODE:27>(ElectronHtmlViewManager, 'ElectronHtmlViewManager', HtmlViewManager[(ElectronWebContents, Context)])

class ElectronViewManagerFactory(Destroyable):
    pass
# WARNING: Decompyle incomplete

