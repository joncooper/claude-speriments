# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from typing import Optional, Sequence
from dropbox.client.features.backup_auto_selsync.constants import AUTO_SEL_SYNC_FEATURE_OFF_VARIANTS, AUTO_SEL_SYNC_GATE_NAME, BI_AUTO_SEL_SYNC_FEATURE_OFF_VARIANTS, BI_CONFLICTED_ENTRY_MAX_SELSYNCS_DEFAULT, BI_CONFLICTED_ENTRY_MAX_SELSYNCS_GATE_NAME, BI_CONFLICTED_ENTRY_SYNCING_DEFER_TIME_GATE_NAME, BI_CONFLICTED_ENTRY_SYNCING_DEFER_TIME_SEC_DEFAULT
from dropbox.client.features.backup_instance.gating import BackupInstanceFeature
from dropbox.client.features.backup_instance.utils import BI_WARN
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext

class BackupAutoSelSyncFeature:
    is_on_variant_bi = (lambda variants = None: if not variants:
False# WARNING: Decompyle incomplete
)()
    is_allowed_for_any_user_bi = (lambda machine_context = None: (lambda .0: pass# WARNING: Decompyle incomplete
)(machine_context.account_manager.account_models.values()())
)()
    is_allowed_for_specific_user_bi = (lambda user_context = None: BackupInstanceFeature.is_allowed_for_user(user_context))()
    is_on_variant = (lambda variants = None: if not variants:
False# WARNING: Decompyle incomplete
)()
    is_allowed_for_any_user = (lambda machine_context = None: (lambda .0: pass# WARNING: Decompyle incomplete
)(machine_context.account_manager.account_models.values()())
)()
    is_allowed_for_specific_user = (lambda user_context = None: BackupAutoSelSyncFeature.is_on_variant([
user_context.stormcrow.get_variant(AUTO_SEL_SYNC_GATE_NAME)]))()
    conflicted_entry_syncing_defer_time_sec = (lambda user_context = None: defer_sec = BI_CONFLICTED_ENTRY_SYNCING_DEFER_TIME_SEC_DEFAULTvariant_str = user_context.stormcrow.get_variant(BI_CONFLICTED_ENTRY_SYNCING_DEFER_TIME_GATE_NAME)if variant_str and BackupAutoSelSyncFeature.is_on_variant_bi([
variant_str]):
try:
defer_sec = int(variant_str) * 60except Exception:
BI_WARN('invalid conflicted entry defer time variant: %r', None, variant_str)defer_sec)()
    conflicted_entry_max_selsyncs_per_backup = (lambda user_context = None: max_runs = BI_CONFLICTED_ENTRY_MAX_SELSYNCS_DEFAULTvariant_str = user_context.stormcrow.get_variant(BI_CONFLICTED_ENTRY_MAX_SELSYNCS_GATE_NAME)if variant_str and BackupAutoSelSyncFeature.is_on_variant_bi([
variant_str]):
try:
max_runs = int(variant_str)except Exception:
BI_WARN('invalid conflicted entry max runs variant: %r', None, variant_str)max_runs)()

