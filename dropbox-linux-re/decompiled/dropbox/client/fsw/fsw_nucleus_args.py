# Source Generated with Decompyle++
# File: fsw_nucleus_args.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Callable, NamedTuple, Text
from dropbox.client.fsw.migration import FSWSuppressionSettings
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.shared.local_path import LocalPath

class FSWManagerArgs(NamedTuple):
    make_path_func: 'Callable[[Text], LocalPath]' = 'FSWManagerArgs'

