# Source Generated with Decompyle++
# File: logger.pyc (Python 3.11)

from dataclasses import dataclass, field
from enum import Enum
from typing import cast, Optional, Text
from mypy_extensions import TypedDict
from dropbox.client.features.transfer.network_utils import make_api_request
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.futures import Future, ResolvedFuture

class UserFlow(Enum):
    CREATION = 'creation'

# WARNING: Decompyle incomplete
