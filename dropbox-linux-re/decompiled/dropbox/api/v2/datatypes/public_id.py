# Source Generated with Decompyle++
# File: public_id.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

class PublicIdAnnotation(bb.AnnotationType):
    __slots__ = [
        '_public_id',
        '_app_auth_policy',
        '_user_auth_policy',
        '_team_auth_policy',
        '_use_base64_stone_string',
        '_gate_encrypt',
        '_gate_reject_plain',
        '_deserialize_permissively']
    
    def __init__(self, public_id, app_auth_policy, user_auth_policy, team_auth_policy, use_base64_stone_string, gate_encrypt, gate_reject_plain, deserialize_permissively = (None, None, None, None, False, None, None, False)):
        self._public_id = public_id
        self._app_auth_policy = app_auth_policy
        self._user_auth_policy = user_auth_policy
        self._team_auth_policy = team_auth_policy
        self._use_base64_stone_string = use_base64_stone_string
        self._gate_encrypt = gate_encrypt
        self._gate_reject_plain = gate_reject_plain
        self._deserialize_permissively = deserialize_permissively

    public_id = (lambda self: self._public_id)()
    app_auth_policy = (lambda self: self._app_auth_policy)()
    user_auth_policy = (lambda self: self._user_auth_policy)()
    team_auth_policy = (lambda self: self._team_auth_policy)()
    use_base64_stone_string = (lambda self: self._use_base64_stone_string)()
    gate_encrypt = (lambda self: self._gate_encrypt)()
    gate_reject_plain = (lambda self: self._gate_reject_plain)()
    deserialize_permissively = (lambda self: self._deserialize_permissively)()

ROUTES = { }
