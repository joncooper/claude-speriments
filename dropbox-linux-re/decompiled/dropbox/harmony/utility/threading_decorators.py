# Source Generated with Decompyle++
# File: threading_decorators.pyc (Python 3.11)

from __future__ import absolute_import
from dropbox.harmony.utility.threading import HarmonyBackgroundThread, HarmonyPluginThread, HarmonyThread
from dropbox.platform import IS_WINDOWS
if IS_WINDOWS:
    from dropbox.harmony.win.threading import WinHarmonyBackgroundThread, WinHarmonyPluginThread, WinHarmonyThread
    on_harmony_thread = WinHarmonyThread.on_queue_returns_none
    on_harmony_thread_untyped = WinHarmonyThread.on_queue
    assert_on_harmony_thread = WinHarmonyThread.assert_on_queue
    on_harmony_plugin_thread = WinHarmonyPluginThread.on_queue
    assert_on_plugin_thread = WinHarmonyPluginThread.assert_on_queue
    on_harmony_background_thread = WinHarmonyBackgroundThread.on_queue
    return None
on_harmony_thread = None.on_queue_returns_none
on_harmony_thread_untyped = HarmonyThread.on_queue
assert_on_harmony_thread = HarmonyThread.assert_on_queue
on_harmony_plugin_thread = HarmonyPluginThread.on_queue
assert_on_plugin_thread = HarmonyPluginThread.assert_on_queue
on_harmony_background_thread = HarmonyBackgroundThread.on_queue
