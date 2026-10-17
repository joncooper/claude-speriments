# Source Generated with Decompyle++
# File: exception_constants.pyc (Python 3.11)

from typing import List, NamedTuple, Optional
EXC_TYPE_CRASH = 'app_crash'
EXC_TYPE_EXCEPTION = 'app_exception'
ImportCycleAttrs = NamedTuple('ImportCycleAttrs', [
    ('during_shutdown', bool),
    ('machine_id', Optional[str]),
    ('platform_version', Optional[str]),
    ('seen_hosts', Optional[List[int]]),
    ('sync_engine_version', Optional[str])])
