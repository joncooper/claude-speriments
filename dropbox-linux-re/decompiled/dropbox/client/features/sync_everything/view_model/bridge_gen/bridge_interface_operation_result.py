# Source Generated with Decompyle++
# File: bridge_interface_operation_result.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Dict
from dropbox.foundation.futures import Future
from dropbox.client.features.sync_everything.view_model.bridge_gen.bridge_interface_folder_status import FolderStatusBridgeInterface
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus

class OperationResultBridgeInterface(ABC):
    folder_map = (lambda self = None: pass)()
    overall_future = (lambda self = None: pass)()

