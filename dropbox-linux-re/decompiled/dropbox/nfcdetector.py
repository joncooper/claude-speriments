# Source Generated with Decompyle++
# File: nfcdetector.pyc (Python 3.11)

from typing import Text
from unicodedata import is_normalized, normalize

def is_nfc(x = None):
    return is_normalized('NFC', x)


def is_nfd(x = None):
    return is_normalized('NFD', x)


def components_are_nfc_or_nfd(path = None, separator = None):
    for part in path.split(separator):
        if not part:
            continue
        if not is_nfc(part) and is_nfd(part):
            return False
        return True


def canonically_equal(left = None, right = None):
    return normalize('NFC', left) == normalize('NFC', right)

