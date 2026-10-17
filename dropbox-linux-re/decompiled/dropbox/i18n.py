# Source Generated with Decompyle++
# File: i18n.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import ctypes
import locale
import math
import os
import time
from datetime import datetime
from gettext import NullTranslations
from typing import Dict, Iterable, List, Optional, Sequence, Text, Tuple
import babel
import babel.dates as babel
import babel.numbers as babel
from build_number import dropbox_version, is_frozen
from build_number.language_data import DEFAULT_CODE, DESKTOP_LANGUAGE_EXCLUSION_BETA, DESKTOP_LANGUAGE_EXCLUSION_INTERNAL, DESKTOP_LANGUAGE_EXCLUSION_STABLE, get_english_name_for_code, get_lang_from_mac_english_name, get_lang_mapped_to_variant, get_native_name_for_code, get_translation, IGNORABLE_SYSTEM_LANGUAGES, LOCALE_SPLITCHAR, NULL_CODES, ORDERED_LANGUAGE_CODES, ORDERED_LANGUAGE_CODES_DEV, POSSIBLE_CODES_FOR_LANG, SYSTEM_LANG_CODE, trans_explicit as _trans
from dateutil.relativedelta import relativedelta
from dateutil.tz import tzlocal
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.exception.util import raise_boot_error_internally
from dropbox.foundation.environment import is_integration_tests
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.trace import debugging_features_are_enabled, TRACE
APPLE_LANGUAGES = 'AppleLanguages'
_translation = NullTranslations()
_curr_code = DEFAULT_CODE
_requested_code = SYSTEM_LANG_CODE
_translation_activated = False

class TranslationInitializationException(Exception):
    pass


class TranslationAlreadyInitialized(TranslationInitializationException):
    pass


class TranslationLanguageError(TranslationInitializationException):
    pass


def ago(dt = None, now = None, abbreviate = None):
    pass
# WARNING: Decompyle incomplete


def format_time(date_time = None, _locale = None):
    pass
# WARNING: Decompyle incomplete


def format_date(date_time = None, _locale = None):
