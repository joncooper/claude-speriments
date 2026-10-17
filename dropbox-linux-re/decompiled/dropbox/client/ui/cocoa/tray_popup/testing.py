# Source Generated with Decompyle++
# File: testing.pyc (Python 3.11)

import os
PATRONUS_ENV_VAR_NAME = 'PATRONUS_TRAY_TEST'

def is_patronus_tray_test():
    return PATRONUS_ENV_VAR_NAME in os.environ

