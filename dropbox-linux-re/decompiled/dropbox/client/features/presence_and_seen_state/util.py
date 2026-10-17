# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional, Text
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.i18n import format_number, ungettext
from dropbox.sharing.utils.date_util import convert_time_last_seen_to_seconds

class PresenceSeenStateString(UIStrings):
    viewing_now = UI('Viewing now')
    viewed_a_moment_ago = UI('Viewed a moment ago')


def get_seen_state_string(seen_state = None, username = None):
    pass
# WARNING: Decompyle incomplete


def get_seen_state_string_from_interval(secs = None, username = None):
    if secs < 15:
        return PresenceSeenStateString.viewed_a_moment_ago
    if None < 60:
        formatted = int(round(secs))
        if username:
            result = ungettext('%(name)s viewed %(time)s sec ago', '%(name)s viewed %(time)s secs ago', formatted)
        else:
            result = ungettext('Viewed %(time)s sec ago', 'Viewed %(time)s secs ago', formatted)
    elif secs < 3600:
        formatted = int(round(secs / 60))
        if username:
            result = ungettext('%(name)s viewed %(time)s min ago', '%(name)s viewed %(time)s mins ago', formatted)
        else:
            result = ungettext('Viewed %(time)s min ago', 'Viewed %(time)s mins ago', formatted)
    elif secs < 86400:
        formatted = int(round(secs / 3600))
        if username:
            result = ungettext('%(name)s viewed %(time)s hour ago', '%(name)s viewed %(time)s hours ago', formatted)
        else:
            result = ungettext('Viewed %(time)s hour ago', 'Viewed %(time)s hours ago', formatted)
    elif secs < 2592000:
        formatted = int(round(secs / 86400))
        if username:
            result = ungettext('%(name)s viewed %(time)s day ago', '%(name)s viewed %(time)s days ago', formatted)
        else:
            result = ungettext('Viewed %(time)s day ago', 'Viewed %(time)s days ago', formatted)
    elif secs < 4838400:
        formatted = int(round(secs / 604800))
        if username:
            result = ungettext('%(name)s viewed %(time)s week ago', '%(name)s viewed %(time)s weeks ago', formatted)
        else:
            result = ungettext('Viewed %(time)s week ago', 'Viewed %(time)s weeks ago', formatted)
    elif secs < 31536000:
        formatted = int(round(secs / 2592000))
        if username:
            result = ungettext('%(name)s viewed %(time)s month ago', '%(name)s viewed %(time)s months ago', formatted)
        else:
            result = ungettext('Viewed %(time)s month ago', 'Viewed %(time)s months ago', formatted)
    else:
        formatted = int(round(secs / 31536000))
        if username:
            result = ungettext('%(name)s viewed %(time)s year ago', '%(name)s viewed %(time)s years ago', formatted)
        else:
            result = ungettext('Viewed %(time)s year ago', 'Viewed %(time)s years ago', formatted)
    return result % dict(name = username, time = format_number(formatted, frac_precision = 0))

