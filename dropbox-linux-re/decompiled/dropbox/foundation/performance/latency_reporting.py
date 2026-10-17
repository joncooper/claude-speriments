# Source Generated with Decompyle++
# File: latency_reporting.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Dict, Text
from dropbox.foundation.performance.bridge_gen.bridge_interface_latency_reporting_functions import LatencyReportingFunctionsBridgeInterface
from dropbox.platform import IS_MAC

class LatencyReportingFunctions(LatencyReportingFunctionsBridgeInterface):
    get_machine_state = (lambda : if IS_MAC:
get_platform_machine_state = get_platform_machine_stateimport macmachine_state = get_platform_machine_state()else:
machine_state = { }machine_state)()
    simple_bridge_call = (lambda : pass)()

