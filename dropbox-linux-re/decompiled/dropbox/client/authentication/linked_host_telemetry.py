# Source Generated with Decompyle++
# File: linked_host_telemetry.pyc (Python 3.11)

from typing import Dict, List, Optional, Set
LINKED_HOST_COUNT_TAG = 'linked_host_count'
HAS_MTI_TEAM_ACCOUNTS_TAG = 'has_mti_team_accounts'
_linked_host_ids: 'Set[int]' = set()
_linked_team_host_ids: 'Set[int]' = set()

def add_linked_host_id_for_telemetry(host_id = None):
    pass
# WARNING: Decompyle incomplete


def remove_linked_host_id_for_telemetry(host_id = None):
    pass
# WARNING: Decompyle incomplete


def get_linked_host_ids_for_telemetry():
    return sorted(_linked_host_ids.copy())


def get_linked_host_count_for_telemetry():
    return len(get_linked_host_ids_for_telemetry())


def linked_host_count_tag():
    return {
        LINKED_HOST_COUNT_TAG: str(get_linked_host_count_for_telemetry()) }


def add_linked_team_host_id_for_telemetry(host_id = None):
    pass
# WARNING: Decompyle incomplete


def remove_linked_team_host_id_for_telemetry(host_id = None):
    pass
# WARNING: Decompyle incomplete


def get_linked_team_host_count_for_telemetry():
    return len(_linked_team_host_ids)


def has_mti_team_accounts():
    return get_linked_team_host_count_for_telemetry() >= 2


def has_mti_team_accounts_tag():
    return {
        HAS_MTI_TEAM_ACCOUNTS_TAG: str(has_mti_team_accounts()).lower() }

