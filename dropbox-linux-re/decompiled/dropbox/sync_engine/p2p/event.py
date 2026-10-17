# Source Generated with Decompyle++
# File: event.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import threading
from dropbox.event import report
from dropbox.trace import TRACE

class P2PLogger(object):
    ARGS = {
        'discovery_new_peer': {
            'ns_id',
            'my_uuid',
            'peer_uuid'},
        'discovery_summary': {
            'my_uuid',
            'num_peers',
            'ns_num_peer_map'},
        'client_get_start': {
            'ns_id',
            'num_peers',
            'peer_uuids',
            'request_id',
            'num_possible_peers'},
        'client_get_failure': {
            'reason',
            'expected',
            'request_id'},
        'client_get_success': {
            'request_id',
            'size'},
        'client_get_peer_failure': {
            'state',
            'reason',
            'expected',
            'peer_uuid',
            'request_id'},
        'client_get_state_change': {
            'state',
            'peer_uuid',
            'request_id'},
        'client_get_atypical_ns_number': {
            'nses',
            'num_nses',
            'request_id'},
        'client_get_timeouts': {
            'timeouts',
            'request_id',
            'no_timeouts'},
        'conn_pool_dead': {
            'ns_id',
            'reopened',
            'exception',
            'peer_uuid',
            'retry_count'} }
    _PREFIX = 'report_'
    
    def __init__(self):
        self._enabled = None
        self.enabled = False

    
    def __getattr__(self, key):
        pass
    # WARNING: Decompyle incomplete

    enabled = (lambda self: self._enabled)()
    enabled = (lambda self, value: if value != self._enabled:
TRACE('Setting P2P verbose event logging to %sabled', 'en' if value else 'dis')self._enabled = value)()

