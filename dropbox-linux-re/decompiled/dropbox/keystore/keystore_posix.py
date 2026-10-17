# Source Generated with Decompyle++
# File: keystore_posix.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import base64
import errno
import hashlib
import hmac
import json
import os
import struct
from abc import ABCMeta, abstractmethod
from typing import Dict, Optional, Text, Tuple
from six import add_metaclass
from _exceptions import KeystoreItemUnexpectedlyMissing, KeystoreMissingItem
from base import KeyStoreBase
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.legacy_crypto import aes_decrypt, aes_encrypt
from dropbox.threading import Lock
from dropbox.trace import TRACE
KeyStoreFileBacked = <NODE:12>()
