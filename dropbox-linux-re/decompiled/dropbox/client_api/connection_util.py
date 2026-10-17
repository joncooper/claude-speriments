# Source Generated with Decompyle++
# File: connection_util.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import threading
import time
from typing import Any, cast, Dict, List, NamedTuple, Text, Tuple
from build_number import dropbox_version
from dropbox.foundation.environment import debugging_features_are_enabled
from dropbox.overrides import TRACE
from dropbox.threadutils import Stoppable
ENDPOINT_IMPORTANCE = {
    'important_methods': {
        'register_host',
        'subscribe'},
    'essential_endpoints': {
        'unlink',
        'subscribe',
        'preauth_link',
        'check_preauth',
        'register_host',
        'host_nonce_gen',
        'check_for_unlink',
        'check_preauth_tag',
        'cli_link_nonce_gen',
        'link_host_with_ret',
        'list_legacy_out_of_band',
        'client/hourly_refresh'} }
ConnectionResponse = NamedTuple('ConnectionResponse', [
    ('headers', List[Tuple[(Text, Text)]]),
    ('json', Dict[(Text, Any)]),
    ('data', bytes)])

def should_connect_to_stage():
    if debugging_features_are_enabled() and 'DBUSESTAGE' in os.environ:
        return True
    if None in os.environ:
        return False
    return dropbox_version.is_internal_alpha()


def sleep_using_stoppable_if_possible(seconds = None):
    current_thread = threading.current_thread()
    if isinstance(current_thread, Stoppable):
        cast(Stoppable, current_thread).sleep(seconds)
        return None
    TRACE('Warning: Thread is not sleepable and may block forever.')
    time.sleep(seconds)

