# Source Generated with Decompyle++
# File: bridge_interface_apollo_alerts_vm.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import List, Optional
from dropbox.foundation.futures import Future
from dropbox.client.features.apollo_alerts.view_model.bridge_gen.alert_result_record import AlertResultRecord

class ApolloAlertsVMBridgeInterface(ABC):
    show_alert = (lambda self, caption, message, buttons = None, detailed_text = None, default_active_button_index = abstractmethod, checkbox_text = ('caption', 'str', 'message', 'str', 'buttons', 'List[str]', 'detailed_text', 'Optional[str]', 'default_active_button_index', 'Optional[int]', 'checkbox_text', 'Optional[str]', 'return', 'Future[AlertResultRecord]'): pass)()

