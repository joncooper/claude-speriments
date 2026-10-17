# Source Generated with Decompyle++
# File: sjid_format.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Optional
from dropbox.assertions import assert_

def client_to_raw_sjid(client_sjid = None):
    if client_sjid < 0:
        return client_sjid
    return None >> 1


def raw_to_client_sjid(raw_sjid = None):
    if raw_sjid < 0:
        return raw_sjid
    return None << 1


def packed_to_client_sjid(packed_sjid = None):
    return (packed_sjid >> 32) << 1


def client_to_packed_sjid(client_sjid = None, nsid = None):
    return ((client_sjid >> 1) << 32) + nsid


def internal_packed_to_client_sjid(packed_sjid = None):
    pass
# WARNING: Decompyle incomplete


def internal_client_to_packed_sjid(client_sjid = None, nsid = None):
    pass
# WARNING: Decompyle incomplete


def assert_packed_sjid(sjid, message):
    pass
# WARNING: Decompyle incomplete


def to_server_rev(ns_id = None, client_sjid = None):
    sj_id = client_to_raw_sjid(client_sjid)
    return '{:x}'.format((sj_id << 32) + ns_id) if sj_id != 0 else None

