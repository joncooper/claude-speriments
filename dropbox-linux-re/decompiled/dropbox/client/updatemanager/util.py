# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

import os
from enum import Enum
from typing import Dict, Optional
from apex.auto_updater import get_updater_id
from apex.metrics import Metric, MetricsReporter
from dropbox.client.updatemanager.constants import DESKTOP_RELEASE_AMP_NAMESPACE
from dropbox.client.util import get_contents_root
from dropbox.event import report
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.proto.apex.auto_updater_pb2 import UpdaterEvent
if IS_MAC:
    from dropbox.client.util.mac import get_helpers_dir
    from dropbox.mac.version import BIG_SUR, MAC_VERSION
if IS_WINDOWS:
    from dropbox.win32.version import WIN10, WINDOWS_VERSION

class UpdaterInstallType(Enum):
    NASHVILLE = 'nashville'
    OMAHA4_APEX = 'omaha4_apex'
    OMAHA4_SHIM = 'omaha4_shim'


def is_omaha4_supported():
    if IS_WINDOWS:
        return WINDOWS_VERSION.version_number() >= WIN10.version_number()
    if None:
        return MAC_VERSION >= BIG_SUR


def get_update_client_path():
    if IS_WINDOWS:
        return os.path.join(get_contents_root(), 'DropboxUpdateClient.exe')
    if None:
        return os.path.join(get_helpers_dir(), 'DropboxUpdateClient')
    raise ValueError('Unable to determine update client path')


def get_updater_path():
    if IS_WINDOWS:
        return os.path.join(get_contents_root(), 'UpdaterSetup.exe')
    if None:
        return os.path.join(get_helpers_dir(), 'DropboxUpdater.app', 'Contents', 'MacOS', 'DropboxUpdater')
    raise ValueError('Unable to determine updater path')


def report_updater_event(event_name = None, extra = None):
    report('auto-updater-events', event_name = event_name, updater_id = get_updater_id(), extra = extra)


def report_should_promote_event(metrics_reporter = None):
    metric = metrics_reporter.create_counter(Metric(DESKTOP_RELEASE_AMP_NAMESPACE, 'update_manager/should_promote_event'), { })
    metric.increment(1)
    metric.record()
    report_updater_event('promotion_notification')


def report_promote_started(metrics_reporter = None):
    metric = metrics_reporter.create_counter(Metric(DESKTOP_RELEASE_AMP_NAMESPACE, 'update_manager/promotion_started'), { })
    metric.increment(1)
    metric.record()
    report_updater_event('promotion_started')


def report_promotion_success(metrics_reporter = None, method = None):
    metric = metrics_reporter.create_counter(Metric(DESKTOP_RELEASE_AMP_NAMESPACE, 'update_manager/promotion_success'), {
        'method': method })
    metric.increment(1)
    metric.record()


def report_promotion_cancelled(metrics_reporter = None):
    metric = metrics_reporter.create_counter(Metric(DESKTOP_RELEASE_AMP_NAMESPACE, 'update_manager/promotion_cancelled'), { })
    metric.increment(1)
    metric.record()
    report_updater_event('promotion_cancelled')


def report_promotion_from_helper_failure(metrics_reporter = None, result = None):
    metric = metrics_reporter.create_counter(Metric(DESKTOP_RELEASE_AMP_NAMESPACE, 'update_manager/promotion_from_helper_failure'), {
        'result': result })
    metric.increment(1)
    metric.record()
    report_updater_event('promotion_from_helper_failure', {
        'result': result })


def report_updater_install(metrics_reporter = None, updater_type = None):
    metric = metrics_reporter.create_counter(Metric(DESKTOP_RELEASE_AMP_NAMESPACE, 'update_manager/updater_install'), {
        'updater_type': updater_type.value })
    metric.increment(1)
    metric.record()
    report_updater_event('updater_install')


def updater_event_proto_to_tags(event = None):
    tags = None
    if event.HasField('flush_and_terminate'):
        tags = {
            'is_background': str(event.flush_and_terminate.is_background) }
    elif event.HasField('update_available'):
        tags = {
            'version': event.update_available.next_version }
    elif event.HasField('update_downloading'):
        tags = {
            'downloaded_bytes': str(event.update_downloading.downloaded_bytes),
            'total_bytes': str(event.update_downloading.total_bytes) }
    elif event.HasField('update_installing'):
        tags = {
            'install_progress': str(event.update_installing.install_progress) }
    elif event.HasField('error'):
        tags = {
            'message': event.error.message }
    return tags

