# Source Generated with Decompyle++
# File: bootloop_marker.pyc (Python 3.11)

import json
import os
import time
from typing import Dict, Text, Tuple
from dropbox.client.constants import AppDataPaths
from dropbox.event import report
from dropbox.trace import TRACE
LAST_BOOT_TIME = 'last_boot_time'
BOOT_COUNT = 'boot_count'
MARKER_PATH = 'boot_marker.dbx'
RECENT_BOOT_INTERVAL = 300
BOOT_COUNT_LOOP_THRESHOLD = 5

def _get_boot_marker_file():
    return os.path.join(AppDataPaths.dropbox_appdata_path, MARKER_PATH)


def get_boot_marker_info():
    crash_marker = _get_boot_marker_file()
    
    try:
        boot_info = json.loads(open(crash_marker, 'r', encoding = 'utf-8').read())
        last_boot = int(boot_info.get(LAST_BOOT_TIME, 0))
        boot_count = int(boot_info.get(BOOT_COUNT, 0))
        return (last_boot, boot_count)
    except Exception:
        e = None
        TRACE('Exception occurred when reading boot marker: %r', e)
        e = None
        del e
        return (0, 0)
        e = None
        del e



def set_boot_marker_info(last_boot_time = None, boot_count = None):
    crash_marker = _get_boot_marker_file()
    
    try:
        boot_info = {
            BOOT_COUNT: boot_count,
            LAST_BOOT_TIME: last_boot_time }
        marker_file = open(crash_marker, 'w+', encoding = 'utf-8')
        marker_file.write(json.dumps(boot_info, indent = 4))
        
        try:
            None(None, None)
            return None
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            return None
                        except Exception:
                            e = None
                            TRACE('Exception occurred when writing boot marker: %r', e)
                            e = None
                            del e
                            return None
                            e = None
                            del e






def assess_boot_loop():
    current_time = int(time.time())
    (last_boot_time, current_boot_loop_count) = get_boot_marker_info()
    if last_boot_time > current_time - RECENT_BOOT_INTERVAL:
        if current_boot_loop_count == BOOT_COUNT_LOOP_THRESHOLD:
            report('app-boot-looping')
        set_boot_marker_info(current_time, current_boot_loop_count + 1)
        return None
    set_boot_marker_info(current_time, 0)

