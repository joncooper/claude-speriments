# Source Generated with Decompyle++
# File: toast.pyc (Python 3.11)

import hashlib
import html
import json
import os
import re
from time import time as _time
from typing import Any, Callable, Dict, NamedTuple, Optional, Text
import six
from six import iteritems
from windisplaytoast.api import clear_history, display_toast, get_displayed_toasts, register_toast_activator, remove_toast, set_toast_callbacks, TOAST_ERROR_DISABLED_APP, TOAST_ERROR_DISABLED_GROUPPOLICY, TOAST_ERROR_DISABLED_MANIFEST, TOAST_ERROR_DISABLED_USER
_WPN_E_NOTIFICATION_SIZE = -2143419895
_WPN_E_PLATFORM_UNAVAILABLE = -2143420155
from pynt.constants import ERROR_ACCESS_DENIED
from types import BubbleContextRef
from regutils import is_dropbox_banners_disabled, is_quiet_hours_enabled
from toast_startmenu_verifier import ToastStartMenuVerifier
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.loud_notifications.constants import LoudNotificationActivationType, ToastDismissedReason
from dropbox.client.notifications.loud_notifications.events import NoInteractionWhenPoppedReason, report_notclicked_bubble
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationId, LoudNotificationType
from dropbox.client.notifications.loud_notifications.win.toast_interface import ActivatedToast, DisplayToastResult, ToastNotifierInterface
from dropbox.client.shortcut.windows import check_and_fix_startmenu_shortcut_in_background
from dropbox.client.ui.common.uikit import on_ui_thread, on_ui_thread_blocking
from dropbox.client.ui.win32.theme import get_os_theme, WindowsOSTheme
from dropbox.client.util import get_contents_root
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception, report_unexpected_none
from dropbox.exception.severity import Severity
from dropbox.functions import lrudict, make_bytes
from dropbox.i18n import trans
from dropbox.trace import TRACE
from dropbox.webdebugger.server import WebDebugger
_TOAST_XML = '\n<toast {persistent_xml} launch="{action_arguments}">\n    <visual>\n        <binding template="ToastGeneric">\n            <text>{caption}</text>\n            <text>{message}</text>\n            {avatar_xml}\n            {content_image_xml}\n        </binding>\n    </visual>\n    {action_xml}\n</toast>\n'
_TOAST_ACTIONS_XML = '<actions>%s</actions>'
_TOAST_ACTION_BUTTON_XML = '<action activationType="background" content="{content}" arguments="{action_arguments}" />'
_TOAST_ACTION_COMMENT_XML = '\n        <input id="answer" type="text" placeHolderContent="{textbox_placeholder}"/>\n        <action\n          content="{button_send}"\n          hint-inputId="answer"\n          activationType="background"\n          arguments="{action_arguments}"/>\n'
_TOAST_AVATAR_XML = '<image src="{image_file_url}" placement="AppLogoOverride" hint-crop="circle"/>'
_TOAST_CONTENT_IMAGE_XML = '<image src="{image_file_url}" />'

class ToastActionArgument(NamedTuple):
    activation_type: 'LoudNotificationActivationType' = 'ToastActionArgument'
    to_str = (lambda proc_id = None, loud_notification_type = None, action_ctxt_ref = staticmethod, activation_type = ('proc_id', 'int', 'loud_notification_type', 'LoudNotificationType', 'action_ctxt_ref', 'Optional[BubbleContextRef]', 'activation_type', 'LoudNotificationActivationType', 'return', 'Text'): '{proc_id}:{loud_notification_type}:{action_ctxt_ref}:{activation_type}'.format(proc_id = proc_id, loud_notification_type = loud_notification_type.value, action_ctxt_ref = action_ctxt_ref, activation_type = activation_type.value))()
    from_str = (lambda argument = None: try:
(str_proc_id, notif_type, str_ctxt_ref, activation_type_str) = argument.split(':')activation_type = LoudNotificationActivationType(activation_type_str)except ValueError:
encoded_argument = argument.encode('utf-8', 'ignore')TRACE('Toast activation badly formatted. Argument was: {}, {!r}'.format(argument, encoded_argument))Noneexcept Exception:
report_exception(severity = Severity.WARN, component = DesktopComponent.NATIVE_NOTIFICATIONS)Nonetry:
ctxt_ref = BubbleContextRef(int(str_ctxt_ref))except ValueError:
Nonetry:
proc_id = int(str_proc_id)except ValueError:
NoneToastActionArgument(proc_id, LoudNotificationType(str(notif_type)), ctxt_ref, activation_type))()

CONTEXTLESS_HEADER = 'CLTA1|'

class ContextLessActionArgument(NamedTuple):
    bluenote_id: 'Optional[int]' = 'ContextLessActionArgument'
    create_str = (lambda loud_notification_type, activation_type, action_name, action_parameters, account_id, tag, notification_id, notification_key = None, is_persistent = None, process_session_id = staticmethod, display_time = (-1, None, None), bluenote_id = ('loud_notification_type', 'LoudNotificationType', 'activation_type', 'LoudNotificationActivationType', 'action_name', 'Text', 'action_parameters', 'Optional[Dict[Text, Any]]', 'account_id', 'Optional[int]', 'tag', 'Text', 'notification_id', 'Optional[int]', 'notification_key', 'Optional[Text]', 'is_persistent', 'bool', 'process_session_id', 'int', 'display_time', 'Optional[float]', 'bluenote_id', 'Optional[int]', 'return', 'Text'): CONTEXTLESS_HEADER + json.dumps({
'type': loud_notification_type,
'activation': activation_type.value,
'action': action_name,
'params': action_parameters if action_parameters else { },
'account': account_id,
'tag': tag,
'nid': notification_id,
'nkey': notification_key,
'pers': is_persistent,
'pid': process_session_id,
'time': display_time,
'bluenote_id': bluenote_id }))()
    from_str = (lambda argument = None: if not ContextLessActionArgument.is_instance(argument):
Nonetry:
dict = json.loads(argument[6:])ContextLessActionArgument(LoudNotificationType(dict['type']), LoudNotificationActivationType(dict['activation']), dict['action'], dict['params'], dict['account'], dict['tag'], dict['nid'], dict['nkey'], dict['pers'], dict.get('pid', -1), dict.get('time', -1), dict.get('bluenote_id'))except ValueError:
TRACE('!! Contextless Toast activation badly formatted. Argument was: %s', argument)None)()
    is_instance = (lambda argument = None: if argument is not None:
passargument.startswith(CONTEXTLESS_HEADER))()


def _get_toast_xml(loud_notification = None, process_session_id = None, avatar_filepath = None, content_image_filepath = (None, None, False), contextless_supported = ('loud_notification', 'LoudNotification', 'process_session_id', 'int', 'avatar_filepath', 'Optional[Text]', 'content_image_filepath', 'Optional[Text]', 'contextless_supported', 'bool', 'return', 'Text')):
    action_xml = ''
    avatar_xml = ''
    content_image_xml = ''
    list_actions = []
    max_num_buttons = 5
    if loud_notification.can_reply():
        placeholder_text = trans('Enter your reply')
        send_button_text = trans('Send')
        if loud_notification.reply_button_params:
            placeholder_text = loud_notification.reply_button_params.reply_placeholder_text
            send_button_text = loud_notification.reply_button_params.send_button_title
        max_num_buttons = 4
        list_actions.append(_validate_and_sanitize_xml(_TOAST_ACTION_COMMENT_XML, textbox_placeholder = placeholder_text, button_send = send_button_text, action_arguments = ToastActionArgument.to_str(process_session_id, loud_notification.loud_notification_type, loud_notification.reply_callback_ctxt_ref, LoudNotificationActivationType.REPLY_ACTION)))
    if loud_notification.buttons:
        for i in range(0, min(max_num_buttons, len(loud_notification.buttons))):
            button = loud_notification.buttons[i]
            if contextless_supported and loud_notification.account and button.contextless_action:
                button_action_arguments = ContextLessActionArgument.create_str(loud_notification.loud_notification_type, LoudNotificationActivationType.BUTTON_ACTION, button.contextless_action.action_name, button.contextless_action.action_parameters, loud_notification.account.uid, 'button_' + Text(i), loud_notification.notification_id, loud_notification.key, loud_notification.is_persistent, process_session_id, _time())
            else:
                button_action_arguments = ToastActionArgument.to_str(process_session_id, loud_notification.loud_notification_type, loud_notification.button_ctxt_refs[i], LoudNotificationActivationType.BUTTON_ACTION)
            list_actions.append(_validate_and_sanitize_xml(_TOAST_ACTION_BUTTON_XML, content = loud_notification.buttons[i].title, action_arguments = button_action_arguments))
            if len(list_actions) > 0:
                action_xml = _TOAST_ACTIONS_XML % '\n'.join(list_actions)
    if avatar_filepath:
        avatar_xml = _validate_and_sanitize_xml(_TOAST_AVATAR_XML, image_file_url = 'file:///' + avatar_filepath)
    if content_image_filepath:
        content_image_xml = _validate_and_sanitize_xml(_TOAST_CONTENT_IMAGE_XML, image_file_url = 'file:///' + content_image_filepath)
    if contextless_supported and loud_notification.account and loud_notification.contextless_action:
        action_arguments = ContextLessActionArgument.create_str(loud_notification.loud_notification_type, LoudNotificationActivationType.SURFACE_ACTION, loud_notification.contextless_action.action_name, loud_notification.contextless_action.action_parameters, loud_notification.account.uid, 'surface', loud_notification.notification_id, loud_notification.key, loud_notification.is_persistent, process_session_id, _time(), loud_notification.bluenote_id)
    else:
        action_arguments = ToastActionArgument.to_str(process_session_id, loud_notification.loud_notification_type, loud_notification.ctxt_ref, LoudNotificationActivationType.SURFACE_ACTION)
    toast_xml_string = _validate_and_sanitize_xml(_TOAST_XML, persistent_xml = 'scenario="reminder"' if loud_notification.is_persistent else '', action_arguments = action_arguments, caption = loud_notification.caption, message = loud_notification.msg, avatar_xml = avatar_xml, content_image_xml = content_image_xml, action_xml = action_xml)
    return toast_xml_string


def _validate_and_sanitize_xml(xml, **kwargs):
    sanitized_kwargs = { }
# WARNING: Decompyle incomplete


class WindowsToastNotifier(ToastNotifierInterface):
    _STORMCROW_LINK_ACCOUNT = 'desktop-win10-toasts-linked-with-account'
    _STORMCROW_CONTEXTLESS = 'desktop-win10-toasts-contextless'
    _DEFAULT_TAG_GROUP = 'DbxTagGroup'
    _ACCOUNT_TAG_GROUP = 'DbxTagGroupAccount_'
    _ID_CACHE_SIZE = 50
    _DEBUG_NOTIFICATION_CACHE_SIZE = 50
    _DISMISS_REASONS = {
        ToastDismissedReason.ApplicationHidden: NoInteractionWhenPoppedReason.APPLICATION_HIDDEN,
        ToastDismissedReason.TimedOut: NoInteractionWhenPoppedReason.TIMED_OUT,
        ToastDismissedReason.UserCanceled: NoInteractionWhenPoppedReason.USER_DISMISSED }
    
    def __init__(self = None, toast_activated_callback = None, toast_activated_contextless_callback = None, toast_dismissed_callback = ('toast_activated_callback', 'Callable[[ActivatedToast], Any]', 'toast_activated_contextless_callback', 'Callable[[ContextLessActionArgument, bool], Any]', 'toast_dismissed_callback', 'Callable[[Optional[Text], ToastDismissedReason], Any]', 'return', 'None')):
        self._gandalf = None
        self._activated_callback = toast_activated_callback
        self._activated_contextless_callback = toast_activated_contextless_callback
        self._dismissed_callback = toast_dismissed_callback
        self._debug_enabled = WebDebugger.is_enabled()
        self._debug_notification_messages = lrudict(cache_size = self._DEBUG_NOTIFICATION_CACHE_SIZE)
        self._process_session_id = int(_time())
        
        try:
            register_toast_activator(self._on_toast_activated_from_background)
            TRACE('Registered callback for toast clicks.')
        except WindowsError:
            report_exception(component = DesktopComponent.NATIVE_NOTIFICATIONS)

        
        try:
            set_toast_callbacks(self._on_toast_dismissed, self._on_toast_failed)
        except WindowsError:
            report_exception(component = DesktopComponent.NATIVE_NOTIFICATIONS)

        if self._debug_enabled:
            WebDebugger.register('notifications/get_delivered_windows_notification_texts', self._debug_get_delivered_notification_texts)
            return None

    _debug_get_delivered_notification_texts = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def _get_default_toast_logo_path(self = None):
        if get_os_theme() == WindowsOSTheme.LIGHT:
            exe_icon_path = os.path.join(get_contents_root(), 'Assets/logo.targetsize-256_contrast-white.png')
        else:
            exe_icon_path = os.path.join(get_contents_root(), 'Assets/logo.targetsize-256_contrast-black.png')
        if os.path.exists(exe_icon_path):
            return exe_icon_path

    
    def set_gandalf(self = None, gandalf = None):
        self._gandalf = gandalf
        check_and_fix_startmenu_shortcut_in_background(gandalf)

    
    def get_toast_group(self = None, account = None):
        if account and account.uid and self._gandalf and 'LINKED' in self._gandalf.get_variants_all_accounts(self._STORMCROW_LINK_ACCOUNT):
            notif_hash = hashlib.sha256(make_bytes('Ac[%d]' % account.uid))
            return self._ACCOUNT_TAG_GROUP + Text(notif_hash.hexdigest())[:24]
        return None._DEFAULT_TAG_GROUP

    
    def clear_toasts(self = None, account = None):
        if self._gandalf or 'LINKED' in self._gandalf.get_variants_all_accounts(self._STORMCROW_LINK_ACCOUNT):
            
            try:
                clear_history(self.get_toast_group(account))
                return None
            except Exception:
                report_exception(severity = Severity.TRACE, component = DesktopComponent.NATIVE_NOTIFICATIONS)
                return None
                return None
                return None


    
    def _get_toast_tag(self = None, loud_notification_id = None):
        notif_hash = hashlib.sha256(make_bytes(loud_notification_id))
        tag = Text(notif_hash.hexdigest())[:16]
        return tag

    render_toast = (lambda self = None, loud_notification = None, avatar_filepath = on_ui_thread, toast_rendered_callback = (None, None): self.render_toast_same_thread(loud_notification, avatar_filepath))()
    
    def render_toast_same_thread(self = None, loud_notification = None, avatar_filepath = None, toast_rendered_callback = (None, None)):
        if not avatar_filepath or os.path.exists(avatar_filepath):
            avatar_filepath = self._get_default_toast_logo_path()
        if not ToastStartMenuVerifier.is_valid():
            report_notclicked_bubble(loud_notification.loud_notification_type, None, NoInteractionWhenPoppedReason.STARTMENU_MISSING, None, loud_notification.bluenote_id)
        content_image_filepath = None
        if loud_notification.content_image:
            content_image_filepath = os.path.abspath(loud_notification.content_image)
        if self._gandalf is not None:
            can_use_contextless = 'ON' in self._gandalf.get_variants_all_accounts(self._STORMCROW_CONTEXTLESS)
            toast_xml_string = _get_toast_xml(loud_notification, self._process_session_id, avatar_filepath = avatar_filepath, content_image_filepath = content_image_filepath, contextless_supported = can_use_contextless)
            filtered_xml = re.sub('<text>.*?</text>', '<text>REDACTED</text>', toast_xml_string, re.DOTALL)
            if not loud_notification.is_persistent and loud_notification.buttons:
                report_bad_assumption('Persistent notification without buttons (id: %s)' % loud_notification.id)
        toast_tag = self._get_toast_tag(loud_notification.id)
        group = self.get_toast_group(loud_notification.account)
        if group != self._DEFAULT_TAG_GROUP:
            self._hide_toast_using_tag(toast_tag, self._DEFAULT_TAG_GROUP)
        TRACE('Displaying toast with tag "%s" XML: %s', toast_tag, filtered_xml.replace('\n', ' '))
        
        try:
            display_toast(toast_xml_string, group, toast_tag, loud_notification.id, loud_notification.loud_notification_type.value, str(loud_notification.bluenote_id) if loud_notification.bluenote_id else None, loud_notification.add_to_notification_center, loud_notification.delay_in_minutes)
        except WindowsError:
            e = None
            reason = NoInteractionWhenPoppedReason.API_ERROR
            result = DisplayToastResult.FAILED
            hresult = e.winerror
            if hresult == TOAST_ERROR_DISABLED_USER or hresult == TOAST_ERROR_DISABLED_GROUPPOLICY:
                reason = NoInteractionWhenPoppedReason.ALL_NOTIFICATIONS_DISABLED
                result = DisplayToastResult.REJECTED_BY_OS
            elif hresult == TOAST_ERROR_DISABLED_APP or hresult == TOAST_ERROR_DISABLED_MANIFEST:
                reason = NoInteractionWhenPoppedReason.DROPBOX_NOTIFICATIONS_DISABLED
                result = DisplayToastResult.REJECTED_BY_OS
            elif hresult == _WPN_E_NOTIFICATION_SIZE and hresult == _WPN_E_PLATFORM_UNAVAILABLE or hresult == ERROR_ACCESS_DENIED:
                result = DisplayToastResult.REJECTED_BY_OS
            else:
                report_exception(component = DesktopComponent.NATIVE_NOTIFICATIONS, severity = Severity.WARN)
            report_notclicked_bubble(loud_notification.loud_notification_type, None, reason, hresult, loud_notification.bluenote_id)
            del e
            return None
            None = 
            del e

        if self._debug_enabled:
            self._debug_notification_messages[toast_tag] = loud_notification.msg
        return DisplayToastResult.DISPLAYED

    hide_toast = (lambda self = None, loud_notification_id = None: toast_tag = self._get_toast_tag(loud_notification_id)self._hide_toast_using_tag(toast_tag))()
    
    def _hide_toast_using_tag(self = None, toast_tag = None, group = None):
        TRACE('Attempting to remove toast with tag "' + toast_tag + '"')
        
        try:
            remove_toast(toast_tag, group)
            return True
        except WindowsError:
            e = None
            TRACE('%r', e)
            e = None
            del e
            return False
            e = None
            del e


    
    def _on_toast_activated_from_background(self = None, argument = None, inputs = None):
        if ContextLessActionArgument.is_instance(argument):
            contextless_toast_argument = ContextLessActionArgument.from_str(argument)
            if contextless_toast_argument:
                self._activated_contextless_callback(contextless_toast_argument, contextless_toast_argument.process_session_id == self._process_session_id)
                return None
            report_unexpected_none('contextless toast argument not correctly parsed: %s' % argument)
            return None
        toast_argument = None.from_str(argument)
        if toast_argument:
            is_same_process = toast_argument.proc_id == self._process_session_id
            self._activated_callback(ActivatedToast(is_same_process, False, _time(), toast_argument.loud_notification_type, toast_argument.action_ctxt_ref, toast_argument.activation_type, inputs))
            return None

    
    def _on_toast_dismissed(self, reason, notification_id = None, notification_type_str = None, bluenote_id_str = None, elapsed_time = ('reason', 'ToastDismissedReason', 'notification_id', 'Optional[str]', 'notification_type_str', 'Optional[str]', 'bluenote_id_str', 'Optional[str]', 'elapsed_time', 'float', 'return', 'None')):
        if notification_type_str:
            notification_type = LoudNotificationType(notification_type_str)
        else:
            notification_type = LoudNotificationType.UNKNOWN
        bluenote_id = int(bluenote_id_str) if bluenote_id_str else None
        notclicked_reason = self._DISMISS_REASONS.get(reason, NoInteractionWhenPoppedReason.UNKNOWN)
        if notclicked_reason == NoInteractionWhenPoppedReason.TIMED_OUT:
            if is_quiet_hours_enabled():
                report_notclicked_bubble(notification_type, elapsed_time, NoInteractionWhenPoppedReason.DO_NOT_DISTURB, reason.value, bluenote_id)
            if is_dropbox_banners_disabled():
                report_notclicked_bubble(notification_type, elapsed_time, NoInteractionWhenPoppedReason.BANNERS_DISABLED, reason.value, bluenote_id)
        report_notclicked_bubble(notification_type, elapsed_time, notclicked_reason, reason.value, bluenote_id)
        self._dismissed_callback(notification_id, reason)

    
    def _on_toast_failed(self, error_code, notification_id = None, notification_type_str = None, bluenote_id_str = None, elapsed_time = ('error_code', 'int', 'notification_id', 'Optional[str]', 'notification_type_str', 'Optional[str]', 'bluenote_id_str', 'Optional[str]', 'elapsed_time', 'float', 'return', 'None')):
        if notification_type_str:
            notification_type = LoudNotificationType(notification_type_str)
        else:
            notification_type = LoudNotificationType.UNKNOWN
        bluenote_id = int(bluenote_id_str) if bluenote_id_str else None
        report_notclicked_bubble(notification_type, elapsed_time, NoInteractionWhenPoppedReason.UNKNOWN, error_code, bluenote_id)

    
    def _time_since_display(self = None, display_time = None):
        if display_time:
            return _time() - display_time


