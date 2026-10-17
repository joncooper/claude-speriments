# Source Generated with Decompyle++
# File: pap_logging_helpers.pyc (Python 3.11)

from typing import Any, Dict, List, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import PAPLoggingEvent
from dropbox.client.ui.common.context_menu_verbs import CONTEXT_MENU_VERB_TO_DESKTOP_COMPONENT_MAP, ContextMenuVerb
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import sanitize_event_extra_dict
from dropbox.pap.events.desktop.view_desktop_surface_pb2 import View_DesktopSurface
from dropbox.pap.events.desktop_context_menu.attempt_desktop_login_and_redirect_to_web_pb2 import Attempt_DesktopLoginAndRedirectToWeb
from dropbox.pap.events.enums.content_action_pb2 import ContentAction
from dropbox.pap.events.enums.content_type_pb2 import ContentType
from dropbox.pap.events.navigation.select_content_action_pb2 import Select_ContentAction
SOURCE_CONTEXT_MENU = 'os_context_menu'
# WARNING: Decompyle incomplete
