# Source Generated with Decompyle++
# File: disk_space_state_machine.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from functools import partial
from typing import Callable, Dict, Optional, Text
from disk_space_state import DiskSpaceState, DiskSpaceStateMachineState, LocalFolderSelsyncState
from disk_space_threshold import DiskSpaceThreshold
from disk_space_variant import DiskSpaceVariant, DiskSpaceVariantReason, FullDiskSpaceSelsyncVariant, FullDiskSpaceVariant, LowDiskSpaceSelsyncVariant, LowDiskSpaceVariant
from logging import DiskSpaceLogger, DiskSpaceLoggerEvent, DiskSpaceLoggerTrigger, FULL_HARD_DRIVE_CLEANUP_MODULE, FULL_HARD_DRIVE_SEL_SYNC_MODULE, LOW_HARD_DRIVE_CLEANUP_MODULE, LOW_HARD_DRIVE_SEL_SYNC_MODULE
from notification_manager import BubbleManager, StickyManager
from dropbox.client.features.desktop_rtt_client.rtt_client import DesktopRTTClient
from dropbox.client.high_trace import TRACE
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.proto.growth_platform.rtt.triggers_pb2 import DesktopUserActionType
MYPY = False
if MYPY:
    from dropbox.client.authentication.interface import AccountManagerInterface
LOW_UI_RETRIGGER_PERIOD = 86400
FULL_UI_RETRIGGER_PERIOD = 1800

class TimerStrategy(object):
    _RETRIGGER_PERIOD = {
        DiskSpaceState.HEALTHY: None,
        DiskSpaceState.LOW: LOW_UI_RETRIGGER_PERIOD,
        DiskSpaceState.FULL: FULL_UI_RETRIGGER_PERIOD }
    
    def __init__(self = None, show_ui_callback = None):
        self._last_time_shown_map = DiskSpaceState()
        self._show_ui_callback = show_ui_callback

    
    def _trigger_callback_if_timeout_exceeded(self = None, state = None):
        if not self.should_block_retrigger(state):
            self._show_ui_callback()
            self.reset_last_shown_time(state)
            return None

    
    def should_block_retrigger(self = None, state = None):
        pass
    # WARNING: Decompyle incomplete

    
    def reset_last_shown_time(self = None, state = None):
        self._last_time_shown_map[state.space_state] = get_monotonic_time_seconds()

    
    def on_heartbeat(self = None, state = None, variant = None):
        if state.space_state == DiskSpaceState.FULL:
            self._trigger_callback_if_timeout_exceeded(state)
            return None
        if None.space_state == DiskSpaceState.LOW or variant.low_disk == LowDiskSpaceVariant.V2:
            self._trigger_callback_if_timeout_exceeded(state)
            return None
        return None

    
    def on_dismiss_sticky(self = None, state = None):
        self.reset_last_shown_time(state)



class DiskSpaceStateMachine(object):
    
    def __init__(self, sticky_manager, bubble_manager = None, variant = None, get_machine_context = None, get_account_manager = ('sticky_manager', 'StickyManager', 'bubble_manager', 'BubbleManager', 'variant', 'DiskSpaceVariant', 'get_machine_context', 'Callable[[], object]', 'get_account_manager', "Callable[[], Optional['AccountManagerInterface']]", 'return', 'None')):
        self._cur_state = DiskSpaceStateMachineState.default()
        self._sticky_manager = sticky_manager
        self._bubble_manager = bubble_manager
        self.variant = variant
        self._get_machine_context = get_machine_context
        self._get_account_manager = get_account_manager
        self._timer_strategy = TimerStrategy(self._show_ui_callback)
        self.effective_threshold = DiskSpaceThreshold.default()

    state = (lambda self = None: self._cur_state)()
    state = (lambda self = None, state = None: if state == self._cur_state:
self._timer_strategy.on_heartbeat(state, self.variant)NoneTRACE('DiskSpaceStateMachine: Attempting to transition to %r, adding notifications', state)self._clear_ui(self._cur_state)if self._show_ui(state, DiskSpaceLoggerTrigger.STATE_TRANSITION):
TRACE('DiskSpaceStateMachine: Transitioned to %r', state)self._cur_state = stateself._fire_rtt_trigger(state)self._timer_strategy.on_heartbeat(state, self.variant)None)()
    
    def reset(self = None):
        self._timer_strategy = TimerStrategy(self._show_ui_callback)
        self.effective_threshold = DiskSpaceThreshold.default()
        self.state = DiskSpaceStateMachineState.default()

    _DISK_SPACE_RTT_ACTIONS = {
        (DiskSpaceState.FULL, LocalFolderSelsyncState.ABLE_TO_FREE): DesktopUserActionType.DISK_SPACE_FULL_SELSYNC,
        (DiskSpaceState.FULL, LocalFolderSelsyncState.UNABLE_TO_FREE): DesktopUserActionType.DISK_SPACE_FULL,
        (DiskSpaceState.LOW, LocalFolderSelsyncState.ABLE_TO_FREE): DesktopUserActionType.DISK_SPACE_LOW_SELSYNC,
        (DiskSpaceState.LOW, LocalFolderSelsyncState.UNABLE_TO_FREE): DesktopUserActionType.DISK_SPACE_LOW }
    
    def _fire_rtt_trigger(self = None, state = None):
        if state.space_state == DiskSpaceState.HEALTHY:
            return None
        account_manager = None._get_account_manager()
        account = account_manager.primary if account_manager else None
    # WARNING: Decompyle incomplete

    _create_logger = (lambda state = None, trigger = None, variant_name = staticmethod: if state.selsync_state == LocalFolderSelsyncState.ABLE_TO_FREE:
if state.space_state == DiskSpaceState.FULL:
DiskSpaceLogger(FULL_HARD_DRIVE_SEL_SYNC_MODULE, trigger, variant_name)if None.space_state == DiskSpaceState.LOW:
DiskSpaceLogger(LOW_HARD_DRIVE_SEL_SYNC_MODULE, trigger, variant_name)if state.space_state == DiskSpaceState.FULL:
DiskSpaceLogger(FULL_HARD_DRIVE_CLEANUP_MODULE, trigger, variant_name)if None.space_state == DiskSpaceState.LOW:
DiskSpaceLogger(LOW_HARD_DRIVE_CLEANUP_MODULE, trigger, variant_name)raise 'Unable to create a logger for state %r' % state.space_state())()
    
    def _clear_ui(self = None, state = None):
        self._sticky_manager.remove_sticky_if_exist()
        if state.space_state in (DiskSpaceState.LOW, DiskSpaceState.FULL):
            self._bubble_manager.remove_bubble(state.space_state, state.selsync_state)
            return None

    
    def _show_ui(self = None, state = None, logger_trigger = None):
        if state.space_state == DiskSpaceState.HEALTHY:
            return True
        if None.space_state == DiskSpaceState.LOW:
            low_disk_v1 = self.variant.low_disk == LowDiskSpaceVariant.V1
            if state.space_state == DiskSpaceState.FULL:
                full_disk_v1 = self.variant.full_disk == FullDiskSpaceVariant.V1
                if state.space_state == DiskSpaceState.LOW:
                    low_selsync_v1 = self.variant.low_disk_selsync == LowDiskSpaceSelsyncVariant.V1
                    if state.space_state == DiskSpaceState.FULL:
                        full_selsync_v1 = self.variant.full_disk_selsync == FullDiskSpaceSelsyncVariant.V1
                        if state.selsync_state == LocalFolderSelsyncState.ABLE_TO_FREE:
                            if low_disk_v1 or full_disk_v1:
                                pass
        effective_variant = DiskSpaceVariant.all_v1(DiskSpaceVariantReason.SELECTIVE_SYNC_SUFFICIENT) if low_selsync_v1 or full_selsync_v1 else self.variant
        logger = DiskSpaceStateMachine._create_logger(state, logger_trigger, effective_variant.sub_name_for_state(state.space_state))
        logger.report(DiskSpaceLoggerEvent.NOTIFICATION_TRIGGERED, variant_reason = effective_variant.variant_reason.value)
        if not self._sticky_manager.add_sticky(state, effective_variant, self.effective_threshold, logger, partial(self._timer_strategy.on_dismiss_sticky, state)):
            return False
        if not None._timer_strategy.should_block_retrigger(state):
            self._bubble_manager.show_bubble(state, effective_variant, self.effective_threshold, logger)
            self._timer_strategy.reset_last_shown_time(state)
        return True

    
    def _show_ui_callback(self = None):
        self._show_ui(self._cur_state, DiskSpaceLoggerTrigger.TIMEOUT)


