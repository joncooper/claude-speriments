# Source Generated with Decompyle++
# File: strings.pyc (Python 3.11)

from __future__ import absolute_import
import inspect
from typing import Any, Dict, List, Optional, Text
from build_number.i18n import AccountStringBase, PlatformString
from six import add_metaclass, iteritems
from dropbox.functions import snippet
from dropbox.i18n import trans
DONT_TRANSLATE = "DON'T TRANSLATE"
MYPY = False

def shorten_filename(filename = None, max_length = None):
    max_length = max(max_length, 15)
    if len(filename) > max_length:
        filename = trans('%(folder_name_prefix)s ... %(folder_name_last_5)s') % {
            'folder_name_prefix': filename[:max_length - 10],
            'folder_name_last_5': filename[-5:] }
    return filename


class UIStringsMeta2(type):
    pass
# WARNING: Decompyle incomplete

UIStrings = <NODE:12>()
UIStrings2 = UIStrings

class AccountString(AccountStringBase):
    personal = (lambda self = None: trans(self._personal))()
    business = (lambda self = None: trans(self._business))()
    with_name = (lambda self = None: trans(self._with_name))()
    single = (lambda self = None: trans(self._single))()
    
    def maybe_team(self = None, team_name_ = None, max_len = None, **kw):
        pass
    # WARNING: Decompyle incomplete


EMPTY_STRING = PlatformString('')
