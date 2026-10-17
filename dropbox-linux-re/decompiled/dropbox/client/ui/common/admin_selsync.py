# Source Generated with Decompyle++
# File: admin_selsync.pyc (Python 3.11)

from collections import defaultdict
from typing import Callable, Collection, Dict, Iterable, List, Mapping, Optional
from six import iteritems
from six.moves.urllib import parse as urlparse
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.desktop_login import DesktopLogin
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_rare_event
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2.singleton import Singleton
from dropbox.i18n import ungettext
from dropbox.model.types import FileId
from dropbox.shared.server_path import get_depth, RRCasedServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types import CallbackRemovalToken
from dropbox.sync_engine_boundary.types.remote_props import RemoteLocationProperties
from dropbox.trace import TRACE

class AdminSelsyncUIController(Singleton):
    pass
# WARNING: Decompyle incomplete

