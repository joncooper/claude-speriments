# Source Generated with Decompyle++
# File: features.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import NamedTuple, Optional, Text
from build_number.features import feature_enabled
from support import is_hardware_supported, is_platform_supported
from dropbox.client.gandalf import Gandalf
from dropbox.foundation.stormcrow import MachineStormcrowInterface
from dropbox.foundation.stormcrow.user import UserStormcrow
from dropbox.platform import IS_MAC, IS_WINDOWS

def HtmlViewFeatureFlag():
    '''HtmlViewFeatureFlag'''
    flag_prefix = (lambda cls = None: '')()
    create = (lambda cls = None, name = None: prefix = cls.flag_prefix()cls(f'''{prefix!s}-{name!s}''', f'''desktop-{prefix!s}-{name!s}'''))()
    create_custom_names = (lambda cls = None, feature_name = None, gandalf_name = classmethod: cls(feature_name, gandalf_name))()
    create_without_gandalf = (lambda cls = None, name = None: cls(f'''{cls.flag_prefix()!s}-{name!s}''', None))()
    
    def enabled_any_account(self = None, gandalf = None, allow_when_gandalf_none = None):
        feature_allowed = feature_enabled(self.feature)
    # WARNING: Decompyle incomplete

    
    def enabled_skipgandalfcheck(self = None):
        return self.enabled_any_account(None, allow_when_gandalf_none = True)

    
    def enabled_with_user_stormcrow(self = None, stormcrow = None):
        pass
    # WARNING: Decompyle incomplete

    
    def enabled_with_machine_stormcrow(self = None, stormcrow = None):
        pass
    # WARNING: Decompyle incomplete


HtmlViewFeatureFlag = <NODE:27>(HtmlViewFeatureFlag, 'HtmlViewFeatureFlag', NamedTuple('HtmlViewFeatureFlag', [
    ('feature', Text),
    ('gandalf', Optional[Text])]))

class HtmlViewFeatures(object):
    is_feature_only_enabled = (lambda cls = None: 