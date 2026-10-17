# Source Generated with Decompyle++
# File: recovery.pyc (Python 3.11)

import os
import subprocess
from apex.metrics import Metric, MetricsReporter
from build_number.features import feature_enabled
from dropbox.client.message_queue import InstrumentedMessageQueueThread
from dropbox.client.updatemanager import UpdateManager
from dropbox.client.updatemanager.constants import DESKTOP_RELEASE_AMP_NAMESPACE
from dropbox.components.desktop_components import DesktopComponent
from dropbox.connection_backoff import get_jittered_seconds
from dropbox.db_thread import db_thread_with_task_timing
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.trace import TRACE

class _RecoveryThreadImpl(InstrumentedMessageQueueThread):
    instrumented_name = (lambda cls = None: 'UPDATE_MANAGER_RECOVERY')()

RecoveryThread = db_thread_with_task_timing(_RecoveryThreadImpl, DesktopComponent.DROPBOX_UPDATE, _RecoveryThreadImpl.instrumented_name())
on_recovery_thread = RecoveryThread.on_queue

class RecoveryManager:
    
    def __init__(self = None, metrics_reporter = None):
        self._thread = RecoveryThread()
        self._thread.start()
        self._metrics_reporter = metrics_reporter

    
    def _record_recovery_check_failure(self = None, error_type = None, result = None):
        metric = self._metrics_reporter.create_counter(Metric(DESKTOP_RELEASE_AMP_NAMESPACE, 'update_manager/recovery_check'), {
            'error_type': error_type,
            'result': result })
        metric.increment(1)
        metric.record()

    
    def _poll_for_recovery(self = None):
        
        try:
            UpdateManager.recover_update_manager_if_necessary()
        except subprocess.CalledProcessError:
            e = None
            self._record_recovery_check_failure('CalledProcessError', str(e.returncode))
            e = None
            del e
        except subprocess.TimeoutExpired:
            self._record_recovery_check_failure('TimeoutExpired', 'timeout')
        except Exception:
            report_exception(component = DesktopComponent.DROPBOX_UPDATE, severity = Severity.WARN)

        wait_period = get_jittered_seconds(hours = 8)
        on_recovery_thread(f = self._poll_for_recovery, delay = wait_period)()

    
    def start_polling_for_recovery(self = None):
        if not feature_enabled('omaha4-recovery'):
            return None
        TRACE('Update manager recovery polling starting.')
        if os.environ.get('DBDEV_DISABLE_RECOVERY_CHECK_DELAY') == '1':
            wait_period = 0
        else:
            wait_period = get_jittered_seconds(hours = 1)
        on_recovery_thread(f = self._poll_for_recovery, delay = wait_period)()


