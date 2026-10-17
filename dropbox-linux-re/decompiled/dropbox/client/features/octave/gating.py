# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional, Text
from dropbox.client.gandalf import Gandalf
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.stormcrow import MachineStormcrowInterface
from dropbox.harmony.models.types import ApplicationVersion
DESKTOP_OCTAVE_STORMCROW = 'desktop-octave'
DESKTOP_OCTAVE_EXPANDED_VARIANT = 'EXPANDED'

def desktop_octave_enabled_from_gandalf(gandalf = None):
    return gandalf.allows_any_account(DESKTOP_OCTAVE_STORMCROW)


def desktop_octave_enabled(stormcrow = None):
    return stormcrow.allows_any_account(DESKTOP_OCTAVE_STORMCROW)


def desktop_octave_expanded(stormcrow = None):
    return DESKTOP_OCTAVE_EXPANDED_VARIANT in stormcrow.get_variants_all_accounts(DESKTOP_OCTAVE_STORMCROW)

EXCEL_AID = 'com.microsoft.Excel'
POWERPOINT_AID = 'com.microsoft.Powerpoint'
WORD_AID = 'com.microsoft.Word'
OFFICE_AIDS = [
    EXCEL_AID,
    POWERPOINT_AID,
    WORD_AID]
EXCEL_MIN_VERSION = 16
OFFICE_MIN_VERSION = 14
PREVIEW_AID = 'com.apple.Preview'
TEXTEDIT_AID = 'com.apple.TextEdit'
KEYNOTE_AID = 'com.apple.iWork.Keynote'
NUMBERS_AID = 'com.apple.iWork.Numbers'
PAGES_AID = 'com.apple.iWork.Pages'
ACROBAT_AID = 'com.adobe.Acrobat.Pro'
ADOBE_READER_AID = 'com.adobe.Reader'
PHOTOSHOP_AID = 'com.adobe.Photoshop'
SKETCH_AID = 'com.bohemiancoding.sketch3'
SUPPORTED_AIDS = {
    PREVIEW_AID,
    TEXTEDIT_AID,
    KEYNOTE_AID,
    NUMBERS_AID,
    PAGES_AID,
    ACROBAT_AID,
    ADOBE_READER_AID,
    PHOTOSHOP_AID}

def _get_major_version(version = None):
    pass
# WARNING: Decompyle incomplete


def octave_supports_application(aid = None, version = None):
    if aid in SUPPORTED_AIDS:
        return True
    if None == EXCEL_AID:
        return _get_major_version(version) >= EXCEL_MIN_VERSION
    if None in OFFICE_AIDS:
        return _get_major_version(version) >= OFFICE_MIN_VERSION

