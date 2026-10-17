# Source Generated with Decompyle++
# File: severity.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
import socket
import sqlite3
import ssl
from enum import IntEnum
from typing import Type

class Severity(IntEnum):
    FATAL = 60
    CRITICAL = 50
    WARN = 40
    LEGACY_WARN = 39
    DEBUG = 30
    TRACE = 20

SEVERITY_CLASS_ATTRIBUTE_NAME = '_severity_class'
# WARNING: Decompyle incomplete
