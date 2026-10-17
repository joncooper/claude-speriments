# Source Generated with Decompyle++
# File: dynamic_texts.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from collections import defaultdict
from typing import Dict, Text
from dropbox.threading import RWLock

class DynamicTexts(object):
    
    def __init__(self = None):
        self.texts = defaultdict(dict)
        self.lock = RWLock()

    
    def has_text(self = None, stormcrow_rule = None, key = None):
        self.lock.acquire_read()
        
        try:
            self.lock.release_read()
            return self._has_text_unlocked(stormcrow_rule, key)
        except:
            self.lock.release_read()


    
    def get_text(self = None, stormcrow_rule = None, key = None, default_value = ('stormcrow_rule', 'str', 'key', 'str', 'default_value', 'Text', 'return', 'Text')):
        converted = self._stormcrow_conversion(stormcrow_rule)
        self.lock.acquire_read()
        
        try:
            if self._has_text_unlocked(stormcrow_rule, key):
                self.lock.release_read()
                return list(self.texts[converted].values())[0][key]
            self.lock.release_read()
            return None
        except:
            self.lock.release_read()


    
    def update_texts_batch(self = None, texts = None):
        self.lock.acquire_write()
        
        try:
            self.texts = texts.copy()
            self.lock.release_write()
            return None
        except:
            self.lock.release_write()


    
    def _stormcrow_conversion(self = None, stormcrow_rule = None):
        return stormcrow_rule.replace('-', '_')

    
    def _has_text_unlocked(self = None, stormcrow_rule = None, key = None):
