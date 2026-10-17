# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional, Text
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.exception.reporting import report_bad_assumption

class IncompletePayloadException(Exception):
    pass


class MalformedPayloadException(Exception):
    pass


class MalformedRawNotification(Exception):
    pass


class MalformedTemplatizedNotification(Exception):
    pass


class StickyNotificationKeyError(Exception):
    pass
# WARNING: Decompyle incomplete


class UnsupportedPayloadException(Exception):
    pass


class UnsupportedNotification(Exception):
    
    def __init__(self = None, message = None, type_id = None, version = (None, None, None), campaign_id = ('message', 'Text', 'type_id', 'Optional[int]', 'version', 'Optional[int]', 'campaign_id', 'Optional[str]', 'return', 'None')):
        Exception.__init__(self, message)
        self.type_id = type_id
        self.version = version
        self.campaign_id = campaign_id



class UnsupportedNotificationType(UnsupportedNotification):
    pass


class UnsupportedNotificationVersion(UnsupportedNotification):
    pass


class UnsupportedNotificationDisabled(UnsupportedNotification):
    pass


class UserNotificationActionStringError(Exception):
    pass
# WARNING: Decompyle incomplete


class UserNotificationActionError(Exception):
    
    def __init__(self, identifier, wrapped = (None,)):
        self.identifier = identifier
        self.wrapped = wrapped
        localized_message = getattr(UserNotificationStrings, identifier, None)
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        return f'''<{self.__class__.__name__!s}({self.identifier!r}){': %s' % self.wrapped if self.wrapped else ''!s}>'''

    
    def __reduce__(self):
        return (UserNotificationActionError, (self.identifier,))



class UserNotificationActionNotAvailableError(Exception):
    pass


class UserNotificationInvalidBehaviorError(Exception):
    pass

