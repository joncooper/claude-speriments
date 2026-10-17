# Source Generated with Decompyle++
# File: linux.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import List, Text, Union
from dropbox.foundation.native_file_opener.bridge_gen.app_info import AppInfo
from dropbox.foundation.native_file_opener.bridge_gen.app_info_list import AppInfoList
from dropbox.foundation.native_file_opener.bridge_gen.icon_info import IconInfo
from dropbox.shared.local_path import LocalPath

def get_associated_applications(local_path = None):
    return AppInfoList([])


def open_with_application(file_path = None, app = None):
    return False


def open_multiple_files_with_application(file_paths = None, app = None):
    return False


def get_dropbox_icon():
    return IconInfo()


def get_dropbox_paper_icon():
    return IconInfo()

