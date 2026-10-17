# Source Generated with Decompyle++
# File: fp_shadow_migration_dfc.pyc (Python 3.11)

import functools
import os
import shutil
from datetime import datetime, timedelta
from typing import Any, Dict, Optional
from apex.metrics import Metric
from nucleus_python import FpDfc
from dropbox import threading
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.configuration.interface import ConfigurationManagerInterface, LocalConfigurationInterface
from dropbox.client.periodic import PeriodicScheduler
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.localized_strings.common import localized_strings
from dropbox.proto.nucleus_fp_shadow.fp_shadow_pb2 import PollFpDfcArgs, PollFpDfcResponse
from dropbox.sync_root.constants import SyncRootConstants
from dropbox.sync_root.fp_shadow_migration_constants import DFC_DATABASE_FOLDER_NAME, DFC_FOLDER_NAME, DFC_TTL_DAYS, FP_SHADOW_FASTER_PERIOD_STORMCROW, FP_SHADOW_MIGRATION_EVENTS, POLL_DFC_JOB_NAME, POLL_DFC_PERIOD_MINUTES
from dropbox.sync_root.fp_shadow_migration_interface import FPShadowMigrationDfcControllerInterface
from dropbox.trace import TRACE

class FPShadowMigrationDfcController(FPShadowMigrationDfcControllerInterface, Actor):
    pass
# WARNING: Decompyle incomplete

