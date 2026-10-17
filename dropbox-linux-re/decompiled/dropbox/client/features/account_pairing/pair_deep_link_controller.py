# Source Generated with Decompyle++
# File: pair_deep_link_controller.pyc (Python 3.11)

from typing import List, Mapping
from dropbox.client.features.account_pairing.pairing_controller import PairingController
from dropbox.client.multiaccount.role import Roles
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.navigation_service import NavigationServiceInterface
MYPY = False
if MYPY:
    from dropbox.app.machine_ui_dispatcher import AttemptLinkFunc

class PairDeepLinkController:
    pair_link_handler = (lambda _path, query = None, _navigation_service = None, machine_context = staticmethod, attempt_link = ('query', 'Mapping[str, List[str]]', '_navigation_service', 'NavigationServiceInterface', 'machine_context', 'MachineContext', 'attempt_link', 'AttemptLinkFunc', 'return', 'None'): PairingController.start_pairing_flow(machine_context.account_manager, attempt_link, query.get('token', [
''])[0], query.get('email', [
''])[0], query.get('id', [
''])[0], query.get('pair_origin', [
''])[0], Roles.from_server(query.get('role', [
''])[0])))()

