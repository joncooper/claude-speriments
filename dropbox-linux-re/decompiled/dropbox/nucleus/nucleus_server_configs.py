# Source Generated with Decompyle++
# File: nucleus_server_configs.pyc (Python 3.11)

from typing import Callable, Dict, Optional, Union
from build_number.nucleus_features import NUCLEUS_STORMCROW_CONFIGS, NUCLEUS_TEST_CONFIGS
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.gandalf import Gandalf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception, Severity
from dropbox.proto.nucleus.feature_configs_pb2 import ServerFeatureConfig, ServerFeatureConfigs, StormcrowConfig

def get_server_configs(account = None, gandalf = None):
    server_feature_configs = []
    if gandalf:
        
        try:
            for rule in NUCLEUS_STORMCROW_CONFIGS:
                if rule in NUCLEUS_TEST_CONFIGS:
                    continue
                gandalf_rule_name = rule.replace('_', '-')
                allows = gandalf.allows(gandalf_rule_name, account)
                if allows:
                    variant = gandalf.get_variant(gandalf_rule_name, account)
                    server_feature_configs.append(ServerFeatureConfig(stormcrow = StormcrowConfig(feature_name = rule, variant = variant if variant else 'ON')))
        except Exception:
            report_exception(severity = Severity.WARN, component = DesktopComponent.NUCLEUS)
        except:
            report_bad_assumption('Gandalf object should not be None')

        return ServerFeatureConfigs(server_feature_configs = server_feature_configs)


class FeatureConfigs:
    
    def __init__(self, account = None, gandalf = None, monotonic_time = None, jittered_hours_in_seconds = ('account', 'AccountInterface', 'gandalf', 'Gandalf', 'monotonic_time', 'Callable[[], float]', 'jittered_hours_in_seconds', 'Callable[[Union[int, float]], int]', 'return', 'None')):
        self._account = account
        self._gandalf = gandalf
        self._monotonic_time = monotonic_time
        self._jittered_hours_in_seconds = jittered_hours_in_seconds
        self.next_allowed_update = self._monotonic_time()

    
    def to_dict(self = None, configs = None):
        translated = { }
        for config in configs.server_feature_configs:
            feature = getattr(config, config.WhichOneof('feature'))
            if isinstance(feature, StormcrowConfig):
                translated[config.stormcrow.feature_name] = config.stormcrow.variant
                continue
            report_bad_assumption('Expected ServerFeatureConfig to be StormcrowConfig')
            return translated


