# Source Generated with Decompyle++
# File: mapreduce.pyc (Python 3.11)

from __future__ import absolute_import
import os
import time
from abc import abstractmethod
from collections import deque
from typing import Deque, Dict, Optional, Tuple
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.keystore import get_keystore, KeystoreItemUnexpectedlyMissing, KeystoreMissingItem
from dropbox.keystore.pbkdf2 import pbkdf2
from dropbox.trace import TRACE
KEYCHAIN_SLEEP_DURATION = 5
KEYCHAIN_ATTEMPTS = 5
BAD_UNLINK_COOKIE_KEY = 2
MISSING_ITEM = 3
UNKNOWN_ERROR = 4

class DBKeyStore:
    
    def __init__(self = None, appdata_path = None, instance_id = None, create = (None, True)):
        self.errors = deque()
        self.ks = LegacyKeyStore(appdata_path, instance_id)
        if create:
            
            try:
                self._get_user_key_with_retries()
                TRACE('KEYSTORE: Loaded previous user key')
                return None
            except KeystoreMissingItem:
                TRACE('KEYSTORE: creating new user key: Reason KeystoreMissingItem')
                self.new_user_key()
                return None
                except KeystoreItemUnexpectedlyMissing:
                    self.report_error(MISSING_ITEM)
                    TRACE('KEYSTORE: creating new user key: Reason KeystoreItemUnexpectedlyMissing')
                    self.new_user_key()
                    return None
                except Exception:
                    report_exception(component = DesktopComponent.UNKNOWN)
                    TRACE('KEYSTORE: creating new user key: Reason Exception')
                    self.new_user_key()
                    return None
                self.get_user_key()
                TRACE('KEYSTORE: Loaded previous user key')
                return None


    
    def _get_user_key_with_retries(self = None):
        for i in range(KEYCHAIN_ATTEMPTS):
            self.get_user_key()
            return None
            except KeystoreItemUnexpectedlyMissing:
                if i == 0:
                    report_exception(trace_locals = False, component = DesktopComponent.UNKNOWN)
                if i == KEYCHAIN_ATTEMPTS - 1:
                    report_bad_assumption('KeychainItemMissing: Failed to get key after %d tries %d seconds apart', KEYCHAIN_ATTEMPTS, KEYCHAIN_SLEEP_DURATION, full_stack = True)
                    raise 
                TRACE('KEYSTORE: KeychainItemMissing: Attempt %d of %d failed. Retrying in %r seconds', i + 1, KEYCHAIN_ATTEMPTS, KEYCHAIN_SLEEP_DURATION)
                time.sleep(KEYCHAIN_SLEEP_DURATION)
                continue
            except Exception:
                raise 
            return None

    
    def new_user_key(self = None):
        return self.ks.new_user_key()

    
    def get_user_key(self = None):
        return self.ks.get_user_key()

    
    def get_database_key(self = None, version = None):
        if version:
            raise Exception('invalid version number')
        return self.ks.get_database_key()

    
    def report_errors_to_server(self = None):
        ret = False
    # WARNING: Decompyle incomplete

    
    def report_error(self = None, error = None):
        self.errors.append(error)



class KeyStore:
    new_user_key = (lambda self = None: pass)()
    get_user_key = (lambda self = None: pass)()
    get_database_key = (lambda self = None: pass)()

CLIENT_KEY_NAME = 'Client'
DBKEY_CACHE: 'Dict[bytes, bytes]' = { }

class Version0:
    USER_HMAC_KEY = b'\xd1\x14\xa5R\x12e_t\xbdw.7\xe6J\xee\x9b'
    APP_KEY = b'\rc\x8c\t.\x8b\x82\xfcE(\x83\xf9_5[\x8e'
    APP_IV = b'\xd8\x9bC\x1f\xb6\x1d\xde\x1a\xfd\xa4\xb7\xf9\xf4\xb8\r\x05'
    APP_ITER = 1066
    USER_KEYLEN = 16
    DB_KEYLEN = 16
    
    def new_user_key_and_hmac(self = None):
        return (os.urandom(self.USER_KEYLEN), self.USER_HMAC_KEY)

    
    def get_database_key(self = None, user_key = None):
        if user_key not in DBKEY_CACHE:
            DBKEY_CACHE[user_key] = pbkdf2(user_key, self.APP_KEY, self.APP_ITER, self.DB_KEYLEN)
        return DBKEY_CACHE[user_key]



class LegacyKeyStore(KeyStore):
    
    def __init__(self = None, appdata_path = None, instance_id = None):
        pass
    # WARNING: Decompyle incomplete

    
    def new_user_key(self = None):
        parser = self.parsers[self.max_version]
    # WARNING: Decompyle incomplete

    
    def get_user_key(self = None):
        return self.ks.get_versioned_key(CLIENT_KEY_NAME, self.hmac_keys)

    
    def get_database_key(self = None):
        (version, user_key) = self.ks.get_versioned_key(CLIENT_KEY_NAME, self.hmac_keys)
        return self.parsers[version].get_database_key(user_key)


