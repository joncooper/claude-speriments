# Source Generated with Decompyle++
# File: tray_metrics_helpers.pyc (Python 3.11)

from typing import Any, Mapping, Optional
from dropbox.client.tray.tray_metrics.tray_action_metrics import TrayActionMetrics, TrayMetricsActionItem, TrayMetricsActionMetric, TrayMetricsView

def report_tray_metrics_from_pro_event(*, event, extra):
    metrics_view_map = {
        'dt_oq_menu_tray': TrayMetricsView.MENU_FALLBACK_AND_GEAR_MENU,
        'dt_nq_menu_tray': TrayMetricsView.MENU_FALLBACK_AND_GEAR_MENU,
        'dt_oq_tray': TrayMetricsView.NOTIFICATION_STICKY,
        'dt_oq_ln': TrayMetricsView.NOTIFICATION_LOUD,
        'dt_nq_ln': TrayMetricsView.NOTIFICATION_LOUD,
        'dt_oq_shm': TrayMetricsView.MODAL_DIALOG,
        'dt_nq_shm': TrayMetricsView.MODAL_DIALOG }
    metrics_action_item_map = {
        'over': TrayMetricsActionItem.OVER_QUOTA,
        'near': TrayMetricsActionItem.NEAR_QUOTA }
    metrics_action_metric_map = {
        'view': TrayMetricsActionMetric.SHOW,
        'click': TrayMetricsActionMetric.CLICK }
    metrics_view = metrics_view_map.get(event, None)
# WARNING: Decompyle incomplete

