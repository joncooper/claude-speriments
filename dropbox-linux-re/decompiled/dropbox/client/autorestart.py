# Source Generated with Decompyle++
# File: autorestart.pyc (Python 3.11)

import json
import os
import time
from enum import Enum, unique
from typing import List, Optional, Tuple, TypeVar
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.device_info import get_process_start_time
from dropbox.client.flow_tracker import FlowTracker
from dropbox.client.shutdown_marker import create_crash_marker
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes, IconType
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.client.util import hard_exit
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures.basic import allow_blocking_on_main_thread
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.html_views.common.threading import assert_on_ui_thread
from dropbox.foundation.runtime import AutorestartRequestManager, CONFIG_AUTORESTART_UI_STATE, ExitCode
from dropbox.i18n import trans
from dropbox.platform import IS_LINUX
from dropbox.trace import TRACE
CONFIG_AUTORESTART_ATTEMPTS = 'restart_attempts_timestamps'
CONFIG_AUTORESTART_ATTEMPTS_FREQUENCY = 'restart_attempts_frequency'
AUTORESTART_ATTEMPTS_FREQUENCY = 2
_AutorestartLoggingEvent = <NODE:12>()
ONE_DAY = 86400
_AUTORESTART_EVENT_NAME = 'autorestart_events'

def _report_event(event_name = None):
    report(_AUTORESTART_EVENT_NAME, event_name = event_name.value, client_start_time = get_process_start_time())

show_autorestart_notification_maybe_quit = (lambda ui_kit = None: 
def dialog_callback(selection = None, _unused = None):
pass# WARNING: Decompyle incomplete
if IS_LINUX:
caption = trans('Dropbox')message = trans('<b>Dropbox is restarting</b><br>Sync and other features will resume in a moment.')else:
caption = trans('Dropbox is restarting')message = trans('Sync and other features will resume in a moment.')ui_kit.show_native_non_blocking_dialog(caption = caption, message = message, buttons = [
trans('OK')], callback = dialog_callback, dialog_source_type = DialogSourceTypes.OTHER)_report_event(_AutorestartLoggingEvent.NOTICE_DIALOG_SHOWN))()
show_hit_limit_notification_maybe_quit = (lambda ui_kit = None: if IS_LINUX:
message = trans('<b>Dropbox unexpectedly quit</b><br>Your files are safe. Restart Dropbox to resume sync and other features. <a href="https://www.dropbox.com/help/desktop-web/unexpected-quit">Learn more in our help center.</a>')caption = trans('Dropbox')else:
message = trans('Your files are safe. Restart Dropbox to resume sync and other features.')caption = trans('Dropbox unexpectedly quit')_report_event(_AutorestartLoggingEvent.HIT_LIMIT_DIALOG_SHOWN)allow_blocking_on_main_thread()dialog_future = ui_kit.show_native_blocking_dialog(caption = caption, message = message, buttons = [
trans('Restart Dropbox'),
trans('Close')], icon = IconType.WARN, help_link = 'https://www.dropbox.com/help/desktop-web/unexpected-quit', dialog_source_type = DialogSourceTypes.OTHER)dialog_future.block()selection = dialog_future.result()None(None, None))()

class RestartStatus(Enum):
    HIT_RESTART_LIMIT = 0
    NOT_HIT_RESTART_LIMIT = 1

_T = TypeVar('_T')

def read_data_from_local_db_or_default(config = None, key = None, default_value = None):
    result = default_value
    
    try:
        result = config.config_dict[key]
    except KeyError:
        TRACE('[autorestart] Error reading %s gating value from local config. Assuming %r.', key, default_value)
    except Exception:
        e = None
        TRACE('[autorestart] Exception (%r) when reading %s from local db. Fall back to default value %r.', e, key, default_value)
        e = None
        del e
    except:
        e = None
        del e

    TRACE('[autorestart] %s value is %r', key, result)
    return result


def handle_interactive_restart(ui_kit = None, was_ui_active = None, restart_status = None):
    if restart_status == RestartStatus.HIT_RESTART_LIMIT:
        TRACE('[autorestart] Hit maximum number of restarts. Show blocking message.')
        show_hit_limit_notification_maybe_quit(ui_kit)
        return None
    if None:
        TRACE('[autorestart] UI was active, show message to user.')
        show_autorestart_notification_maybe_quit(ui_kit)
        return None
    TRACE('[autorestart] UI was not active. Continue silent restart...')
    _report_event(_AutorestartLoggingEvent.SILENT_CONTINUE)


def handle_user_autorestart_choice(should_quit = None):
    if should_quit:
        create_crash_marker()
        TRACE('[autorestart] User selected to quit.')
        _report_event(_AutorestartLoggingEvent.USER_QUIT)
        hard_exit(ExitCode.SUCCESS, 'user selected to quit')
        return None
    TRACE('[autorestart] User selected to continue restart.')
    _report_event(_AutorestartLoggingEvent.USER_CONTINUE)


def read_frequency_from_local_config(config = None):
    
    try:
        freq = config.config_dict[CONFIG_AUTORESTART_ATTEMPTS_FREQUENCY]
        return freq
    except KeyError:
        TRACE('[autorestart] Autorestarted, but cannot read frequency from local config.')
        raise 
        except Exception:
            e = None
            TRACE('[autorestart] Exception when reading local db: %r.', e)
            raise 
            e = None
            del e



def handle_autorestart_startup(config = None):
    
    try:
        freq = read_frequency_from_local_config(config)
    except Exception:
        e = None
        hard_exit(ExitCode.SUCCESS, 'Could not read frequency from config.')
        e = None
        del e
        return None
        e = None
        del e

    if not freq:
        TRACE('[autorestart] Autorestarted, freq is false-y (%r), should not happen. Quitting...', freq)
        hard_exit(ExitCode.SUCCESS, 'autorestart freq false-y (%r), should exit' % freq)
        return None
    was_ui_active = bool(read_data_from_local_db_or_default(config, CONFIG_AUTORESTART_UI_STATE, True))
# WARNING: Decompyle incomplete


def read_and_update_restart_attempts_and_should_proceed(config = None, freq = None):
    pass
# WARNING: Decompyle incomplete


def setup_autorestart(config = None):
    pass
# WARNING: Decompyle incomplete

