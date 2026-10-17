# Source Generated with Decompyle++
# File: consts.pyc (Python 3.11)

from typing import Optional
from dropbox.base.enum import StrEnum
from dropbox.trace import TRACE

class FlexibleFileNameStickyVariant(StrEnum):
    OPT_IN = 'opt_in'
    OPT_OUT = 'opt_out'
    DISABLE = 'disable'
    FORCE_DISABLE = 'force_disable'
    FORCE_ENABLE = 'force_enable'
    try_from_str = (lambda label = None: if label.lower() == 'opt_in':
FlexibleFileNameStickyVariant.OPT_INif None.lower() == 'opt_out':
FlexibleFileNameStickyVariant.OPT_OUTif None.lower() == 'disable':
FlexibleFileNameStickyVariant.DISABLEif None.lower() == 'force_disable':
FlexibleFileNameStickyVariant.FORCE_DISABLEif None.lower() == 'force_enable':
FlexibleFileNameStickyVariant.FORCE_ENABLETRACE('[FlexibleFilenames] Failed to parse variant: %r', label))()
    is_disable_variant = (lambda self = None: self in (FlexibleFileNameStickyVariant.DISABLE, FlexibleFileNameStickyVariant.FORCE_DISABLE))()
    is_force_enable_variant = (lambda self = None: self == FlexibleFileNameStickyVariant.FORCE_ENABLE)()
    is_notification_variant = (lambda self = None: self in (FlexibleFileNameStickyVariant.OPT_IN, FlexibleFileNameStickyVariant.OPT_OUT))()

FFN_SHOWN_KEY = 'opt_in_out_notification_shown'
FFN_VARIANT_STORMCROW = 'desktop-flexible-filenames-notification-variant'
HELP_CENTER_LINK = 'https://help.dropbox.com/sync/flexible-filenames'
