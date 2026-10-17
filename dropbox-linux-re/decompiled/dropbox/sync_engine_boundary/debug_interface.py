# Source Generated with Decompyle++
# File: debug_interface.pyc (Python 3.11)

from functools import partial
from typing import Callable, Dict, Set, Text
from dropbox.trace import WARNING

class SyncEngineDebugInterface:
    _trace_calls: 'bool' = False
    _simulate_disconnect: 'bool' = False
    _simulate_service_not_available: 'bool' = False
    _simulate_delay: 'int' = 0
    _excluded_functions: 'Set[Text]' = set()
    _excluded_delay_functions: 'Set[Text]' = {
        'stop',
        'root_ns',
        'get_queue_stats',
        'lookup_by_fileid',
        'lookup_local_properties_by_fileid',
        'lookup_remote_properties_by_fileid'}
    fake_disconnect = (lambda cls = None: WARNING('Begin: Simulated NucleusThinClient disconnect.')cls._simulate_disconnect = True)()
    fake_reconnect = (lambda cls = None: WARNING('End: Simulated NucleusThinClient disconnect.')cls._simulate_disconnect = False)()
    start_fake_delay = (lambda cls = None, delay = None: pass# WARNING: Decompyle incomplete
)()
    end_fake_delay = (lambda cls = None: WARNING('End: Simulated NucleusThinClient delay.')cls._simulate_delay = 0)()
    start_fake_service_not_available = (lambda cls = None: WARNING('Begin: Simulated NucleusThinClient service not available.')cls._simulate_service_not_available = True)()
    end_fake_service_not_available = (lambda cls = None: WARNING('End: Simulated NucleusThinClient service not available.')cls._simulate_service_not_available = False)()
    start_call_tracing = (lambda cls = None: WARNING('Start: NucleusThinClient tracing.')cls._trace_calls = True)()
    end_call_tracing = (lambda cls = None: WARNING('End: NucleusThinClient tracing.')cls._trace_calls = False)()
    exclude_function = (lambda cls = None, func_name = None: WARNING('Excluding: %s', func_name)cls._excluded_functions.add(func_name))()
    remove_exclusion = (lambda cls = None, func_name = None: WARNING('Removing exclusion: %s', func_name)cls._excluded_functions.discard(func_name))()
    reset_all = (lambda cls = None: WARNING('Reset all debug behaviors')cls._trace_calls = Falsecls._simulate_disconnect = Falsecls._simulate_service_not_available = Falsecls._simulate_delay = 0cls._excluded_functions.clear())()
    debug_menu_commands = (lambda cls = None: {
'End ThinClient delay': SyncEngineDebugInterface.end_fake_delay,
'Start ThinClient tracing': SyncEngineDebugInterface.start_call_tracing,
'End ThinClient tracing': SyncEngineDebugInterface.end_call_tracing,
'Fake ThinClient disconnect': SyncEngineDebugInterface.fake_disconnect,
'Fake ThinClient reconnect': SyncEngineDebugInterface.fake_reconnect,
'Start ThinClient service not available': SyncEngineDebugInterface.start_fake_service_not_available,
'End ThinClient service not available': SyncEngineDebugInterface.end_fake_service_not_available,
'Reset All': SyncEngineDebugInterface.reset_all })()
    debug_menu_delay_commands = (lambda cls = None: {
'1 second': partial(SyncEngineDebugInterface.start_fake_delay, 1),
'5 seconds': partial(SyncEngineDebugInterface.start_fake_delay, 5),
'10 seconds': partial(SyncEngineDebugInterface.start_fake_delay, 10),
'20 seconds': partial(SyncEngineDebugInterface.start_fake_delay, 20) })()

