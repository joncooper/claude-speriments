# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
if IS_LINUX:
    from dropbox.client.startup.linux import can_configure_startupitem, continue_or_abort_startup, first_run, install_early_in_boot, limit_to_one_instance, post_link_startup, pre_appdata_use_startup, pre_network_startup, reroll_startup_items, setup_omaha4_crashpad_usage_stats_settings
    return None
if None:
    from dropbox.client.startup.mac import can_configure_startupitem, continue_or_abort_startup, first_run, install_early_in_boot, limit_to_one_instance, post_link_startup, pre_appdata_use_startup, pre_network_startup, reroll_startup_items, setup_omaha4_crashpad_usage_stats_settings
    return None
if None:
    from dropbox.client.startup.win import can_configure_startupitem, continue_or_abort_startup, first_run, install_early_in_boot, limit_to_one_instance, post_link_startup, pre_appdata_use_startup, pre_network_startup, reroll_startup_items, setup_omaha4_crashpad_usage_stats_settings
    return None
