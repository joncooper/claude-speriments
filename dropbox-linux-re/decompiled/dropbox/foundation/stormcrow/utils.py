# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from typing import Text
from dropbox.foundation.stormcrow.user import UserStormcrow
from dropbox.trace import TRACE

def get_variant_as_int(stormcrow = None, stormcrow_rule = None, default_value = None, positive_only = (False,)):
    
    try:
        variant_value = stormcrow.get_variant(stormcrow_rule)
        if variant_value:
            TRACE('Fetching variant for %r and get value of %r', stormcrow_rule, variant_value)
            parsed_val = int(variant_value)
            return parsed_val if not parsed_val > 0 or positive_only else default_value
    except ValueError:
        pass

    return default_value

