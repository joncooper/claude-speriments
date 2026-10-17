# Source Generated with Decompyle++
# File: role.pyc (Python 3.11)

from typing import Optional
from dropbox.client.multiaccount.constants import Role
from dropbox.exception.reporting import report_bad_assumption
from dropbox.proto.nucleus.published_event_pb2 import CDMRelocationRequestRestart

class InvalidRoleException(Exception):
    pass


class Roles(object):
    UNSPECIFIED = Role(0)
    PERSONAL = Role(1)
    BUSINESS = Role(2)
    _sort_order = {
        UNSPECIFIED: 300,
        BUSINESS: 200,
        PERSONAL: 100 }
    _mapping = {
        BUSINESS: 'business',
        PERSONAL: 'personal',
        UNSPECIFIED: 'unspecified' }
    _server_to_role = {
        'work': BUSINESS,
        'personal': PERSONAL,
        'unspecified': UNSPECIFIED }
    _role_to_server = _server_to_role.items()()
    from_proto = (lambda cls = None, account_role = (lambda .0: pass# WARNING: Decompyle incomplete
): if account_role == CDMRelocationRequestRestart.Role.PERSONAL:
Roles.PERSONALif None == CDMRelocationRequestRestart.Role.BUSINESS:
Roles.BUSINESS# WARNING: Decompyle incomplete
)()
    sort_key = (lambda cls = None, role = None: try:
cls._sort_order[Role(role)]except KeyError:
report_bad_assumption('Invalid role %s specified', role))()
    flip = (lambda cls = None, role = None: if role == Roles.UNSPECIFIED:
Roles.UNSPECIFIEDif None == Roles.PERSONAL:
Roles.BUSINESSif None == Roles.BUSINESS:
Roles.PERSONALraise None)()
    to_str = (lambda cls = None, role = None: pass# WARNING: Decompyle incomplete
)()
    from_server = (lambda cls = None, role = None: cls._server_to_role.get(role, Roles.UNSPECIFIED))()
    to_server = (lambda cls = None, role = None: if role not in cls._role_to_server:
raise InvalidRoleExceptionif role == Roles.UNSPECIFIED:
NoneNone._role_to_server[role])()

