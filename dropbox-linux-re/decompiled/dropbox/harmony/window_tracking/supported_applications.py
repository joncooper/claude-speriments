# Source Generated with Decompyle++
# File: supported_applications.pyc (Python 3.11)

from typing import List
from dropbox.harmony.models.types import ApplicationID
from dropbox.platform import IS_MAC, IS_WINDOWS

def _core_supported_apps():
    if IS_MAC:
        return [
            'com.microsoft.Word',
            'com.microsoft.Powerpoint',
            'com.microsoft.Excel']
    if None:
        return [
            'Word.Application',
            'PowerPoint.Application',
            'Excel.Application']


def harmony_supported_apps():
    return _core_supported_apps()


def presence_supported_apps():
    return _core_supported_apps()

