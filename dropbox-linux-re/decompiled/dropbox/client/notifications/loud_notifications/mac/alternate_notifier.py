# Source Generated with Decompyle++
# File: alternate_notifier.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from enum import Enum
from typing import Any, Callable, cast, Dict, Optional, SupportsFloat, Text, Union
from AppKit import NSImage, NSUserNotification
from macffi.xpc import XPCCallbacks, XPCClient, XPCMessage, XPCMessageContentType
from build_number import BUILD_KEY
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.loud_notifications.events import report_delivered_xpc_notification, report_received_xpc_metrics_response, report_received_xpc_response
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification
from dropbox.client.notifications.loud_notifications.mac.nsusernotification_builder import NSUserNotificationBuilder
from dropbox.client.ui.common.uikit import on_ui_thread_future
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.futures import Future
from dropbox.platform import IS_MAC
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.mac.version import BIG_SUR, MAC_VERSION, MOJAVE, VENTURA

class SerializedNotification(object):
    
    def __init__(self = None, notification = None, avatar_image = None):
        self.fields = dict(title = notification.title(), informative_text = notification.informativeText(), has_action_button = notification.hasActionButton(), user_info = dict(notification.userInfo()))
        if notification.contentImage():
            self.fields['content_image'] = self._serialize_image(notification.contentImage())
        if avatar_image:
            if not MAC_VERSION >= BIG_SUR and notification.contentImage():
                self.fields['content_image'] = self._serialize_image(avatar_image)
            elif notification.respondsToSelector_('set_identityImage:'):
                self.fields['identity_image'] = self._serialize_image(avatar_image)
        if notification.respondsToSelector_('set_showsButtons:') and notification.actionButtonTitle():
            self.fields['action_button_title'] = notification.actionButtonTitle()
        if notification.hasReplyButton():
            self.fields['has_reply_button'] = True
            return None

    _serialize_image = (lambda image = None: image_data = image.TIFFRepresentation()image_data.bytes().tobytes())()
    
    def to_xpc_message(self = None, extra_fields = None):
        all_fields = self.fields.copy()
    # WARNING: Decompyle incomplete



class AlternateNotifierMessageTypes(Enum):
    ACTIVATED = 'ACTIVATED'
    DELIVERED = 'DELIVERED'
    RECEIVED = 'RECEIVED'
    RECEIVED_FOR_METRICS = 'RECEIVED_FOR_METRICS'


class AlternateNotifier(object):
    _XPC_SERVICE_NAME = f'''com.getdropbox.{BUILD_KEY.lower()}.alternatenotificationservice'''.encode('utf-8')
    is_supported = (lambda gandalf = None: gandalf.allows_any_account('desktop-alternate-notification-service'))()
    
    def __init__(self = None, on_delivered = None, on_activated = None):
        callbacks = XPCCallbacks(self._message_callback, self._client_interruption, self._client_invalidation)
        client = XPCClient.client_with_name(AlternateNotifier._XPC_SERVICE_NAME, callbacks)
        self._client = client
        self._on_delivered = on_delivered
        self._on_activated = on_activated

    
    def cancel_connection(self = None):
        pass
    # WARNING: Decompyle incomplete

    should_be_used = (lambda loud_notification = None, gandalf = None: if MAC_VERSION >= VENTURA:
False# WARNING: Decompyle incomplete
)()
    
    def _send_message(self = None, message = None):
        pass
    # WARNING: Decompyle incomplete

    
    def remove_all_notifications(self = None):
        self._send_message(XPCMessage({
            'message_type': 'remove_all_notifications' }))

    
    def remove_notification(self = None, identifier = None):
        self._send_message(XPCMessage({
            'message_type': 'remove_notification',
            'identifier': identifier }))

    
    def deliver_serialized_notification(self = None, serialized_notification = None):
        self._send_message(serialized_notification.to_xpc_message({
            'message_type': 'deliver_notification' }))

    
    def deliver_notification(self = None, notification = None, avatar_image = None):
        serialized_notification = SerializedNotification(notification, avatar_image)
        self.deliver_serialized_notification(serialized_notification)

    
    def _client_invalidation(self = None):
        self._client = None
        TRACE('!! XPC Notification Service connection was invalidated')

    
    def _client_interruption(self = None):
        TRACE('!! XPC Notification Service connection was interrupted')

    _deserialize = (lambda cls = None, message = None: title = message.content.get('title')informative_text = message.content.get('informative_text')action_button_title = message.content.get('action_button_title')image_content = message.content.get('image_content')avatar_image = message.content.get('avatar_image')activation_type = message.content.get('activation_type')response = message.content.get('response')presented = message.content.get('presented')image_content = NSImage.alloc().initWithData_(image_content) if image_content else Noneavatar_image = NSImage.alloc().initWithData_(avatar_image) if avatar_image else Noneactivation_type = activation_type if isinstance(activation_type, int) else Noneresponse = Text(response) if activation_type else Noneuser_info = message.content.get('user_info')if not isinstance(user_info, Dict):
TRACE('!! unexpected type for user_info %s, user_info is:', type(user_info), user_info)user_info = { }# WARNING: Decompyle incomplete
)()
    
    def _message_callback(self = None, message = None, reply = None):
        self._message_callback_ui_async(message, reply).ground(component = DesktopComponent.NATIVE_NOTIFICATIONS)

    _message_callback_ui_async = (lambda self = None, message = None, reply = on_ui_thread_future: deserialized_message = self._deserialize(message)user_info = deserialized_message.userInfo()# WARNING: Decompyle incomplete
)()

