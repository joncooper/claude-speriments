# Source Generated with Decompyle++
# File: sec.pyc (Python 3.11)

from __future__ import absolute_import
import os
import ssl
import tempfile
from collections import namedtuple
from contextlib import contextmanager
from typing import Iterator, Text, Tuple
from cryptography.hazmat.backends.openssl import backend as openssl_backend
from cryptography.hazmat.primitives.serialization import BestAvailableEncryption, Encoding, load_pem_private_key, PrivateFormat
from six import integer_types
from six.moves.http_client import HTTPConnection, HTTPSConnection
from dropbox.assertions import assert_
from dropbox.fileutils import safe_remove
from dropbox.functions import make_bytes
from dropbox.threading import Lock
from dropbox.trace import TRACE
SSLData = namedtuple('SSLData', [
    'md5',
    'context',
    'private_key',
    'cert'])

class OnDiskCertManager(object):
    store_cert_on_disk_temporarily = (lambda ns_id = None, key = staticmethod, cert = contextmanager: pass# WARNING: Decompyle incomplete
)()()
    _write_to_file = (lambda suffix = None, data = staticmethod: pass# WARNING: Decompyle incomplete
)()()


class NamespaceSSLCertMap(object):
    
    def __init__(self, retain_key_material = (False,)):
        self._lock = Lock()
        self._retain_key_material = retain_key_material
        self._ns_dict = { }

    
    def update_cert(self, ns_id, key, cert, md5):
        TRACE("updating ns_id %r's keys.  md5=%r", ns_id, md5)
        (key_file, cert_file, key_pw) = OnDiskCertManager.store_cert_on_disk_temporarily(ns_id, key, cert)
        self._lock
        is_new_namespace = ns_id not in self._ns_dict
        self._ns_dict[ns_id] = SSLData(md5, self._create_context(cert_file, key_file, key_pw), key if self._retain_key_material else None, cert if self._retain_key_material else None)
        None(None, None)
        None(None, None)
        return 
        with None:
            if not None, is_new_namespace, :
                pass
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def get_md5s(self, ns_ids):
        pass
    # WARNING: Decompyle incomplete

    
    def get_nses(self):
        self._lock
        None(None, None)
        return 
        with None:
            if not None, list(self._ns_dict):
                pass

    
    def get_context(self, ns_id):
        self._lock
        None(None, None)
        return 
        with None:
            if not None, self._ns_dict[ns_id].context if ns_id in self._ns_dict else None:
                pass

    
    def get_all_key_materials(self):
        if not self._retain_key_material:
            return { }
        None._lock
        None(None, None)
        return 
        with None:
            if not (lambda .0: pass# WARNING: Decompyle incomplete
), self._ns_dict.items()():
                pass

    
    def remove_ns(self, ns_id):
        TRACE('Removing p2p keys for ns %r', ns_id)
        self._lock
        if ns_id in self._ns_dict:
            del self._ns_dict[ns_id]
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _create_context(self, cert_file, key_file, key_pw):
        context = ssl.create_default_context(purpose = ssl.Purpose.SERVER_AUTH, cafile = cert_file)
        context.check_hostname = False
        context.load_cert_chain(certfile = cert_file, keyfile = key_file, password = key_pw)
        context._dropbox_ignore_revocation = True
        return context



class P2PHTTPSConnection(HTTPSConnection):
    
    def __init__(self, host, port, timeout, context, sni_name):
        pass
    # WARNING: Decompyle incomplete

    
    def request(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete


