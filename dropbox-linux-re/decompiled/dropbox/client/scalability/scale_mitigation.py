# Source Generated with Decompyle++
# File: scale_mitigation.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum
from typing import Any, Dict, Optional, Text
from dropbox.exception.reporting import report_bad_assumption
from dropbox.shared.validated_record import Field, ValidatedRecord
from dropbox.trace import TRACE

class ScaleLimitReason(Enum):
    TOO_MANY_FILES = 'too_many_files'
    from_server_reason = (lambda cls = None, server_reason = None: reason_str = server_reason['.tag']for reason in cls:
if reason.value == reason_str:
None, reasonreport_bad_assumption('unknown scale mitigation reason: %s' % reason_str)None)()


class ScaleMitigationUserInfo(ValidatedRecord):
    reason = Field.required(ScaleLimitReason)
    scale_threshold = Field.required(int)
    user_value = Field.required(int)
    get_from_server_ret = (lambda cls = None, server_ret = None: if not server_ret:
TRACE('Scale Mitigation Server info is None.')Noneif None in server_ret:
error_summary = server_ret.get('error_summary', '')TRACE('Error %s for scale mitigation: %s', server_ret['error'], error_summary)needs_mitigation = server_ret.get('needs_scale_mitigation')if not needs_mitigation:
Nonereason_dict = None.get('reason')if not reason_dict:
report_bad_assumption('Server did not return a reason for scale')Nonereason = None.from_server_reason(reason_dict)if reason != ScaleLimitReason.TOO_MANY_FILES:
report_bad_assumption("Server returned a reason %s we don't understand" % reason)Nonescale_threshold = None['file_limit']user_value = reason_dict['approximate_file_count']cls(reason = reason, scale_threshold = scale_threshold, user_value = user_value))()

