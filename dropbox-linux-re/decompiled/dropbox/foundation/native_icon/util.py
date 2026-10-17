# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from __future__ import absolute_import
import base64
from typing import Dict, Optional, Text
from apex.metrics import MetricsReporter
from dropbox.foundation.context import Context
from dropbox.foundation.environment import is_integration_tests, is_under_automation
BUILD_ENV_TAG_NAME = 'build_environment'
PNG_DATA_URL_PREFIX = 'data:image/png;base64,'
if is_integration_tests():
    BUILD_ENV = 'integration'
elif is_under_automation():
    BUILD_ENV = 'automation'
else:
    BUILD_ENV = 'normal'

def bytes_to_data_url(icon_bytes = None):
    return PNG_DATA_URL_PREFIX + base64.b64encode(icon_bytes).decode('utf-8')


def create_metrics_reporter(context = None, extra_tags = None):
    tags = {
        BUILD_ENV_TAG_NAME: BUILD_ENV }
# WARNING: Decompyle incomplete

