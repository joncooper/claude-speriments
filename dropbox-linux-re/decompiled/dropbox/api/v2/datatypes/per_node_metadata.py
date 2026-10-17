# Source Generated with Decompyle++
# File: per_node_metadata.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

class BypassBehaviors(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BypassBehaviors_validator = bv.Struct(BypassBehaviors)

class DeviceInfoEntity(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeviceInfoEntity_validator = bv.Struct(DeviceInfoEntity)

class LinkNodeAction(bb.Union):
    pass
# WARNING: Decompyle incomplete

LinkNodeAction_validator = bv.Union(LinkNodeAction)

class LinkNodeEntity(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LinkNodeEntity_validator = bv.Struct(LinkNodeEntity)

class PerNodeMetadataEntity(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PerNodeMetadataEntity_validator = bv.Struct(PerNodeMetadataEntity)
BypassBehaviors.is_device_folder.validator = bv.Nullable(bv.Boolean())
BypassBehaviors._all_field_names_ = set([
    'is_device_folder'])
BypassBehaviors._all_fields_ = [
    ('is_device_folder', BypassBehaviors.is_device_folder.validator)]
DeviceInfoEntity.device_id.validator = bv.String()
DeviceInfoEntity.device_id.validator._redact = bv.BlotRedactor(None)
DeviceInfoEntity.user_id.validator = bv.Int64()
DeviceInfoEntity.user_id.validator._redact = bv.BlotRedactor(None)
DeviceInfoEntity._all_field_names_ = set([
    'device_id',
    'user_id'])
DeviceInfoEntity._all_fields_ = [
    ('device_id', DeviceInfoEntity.device_id.validator),
    ('user_id', DeviceInfoEntity.user_id.validator)]
LinkNodeAction._unknown_action_validator = bv.Void()
LinkNodeAction._device_folder_pre_setup_validator = bv.Void()
LinkNodeAction._life_vault_pre_setup_validator = bv.Void()
LinkNodeAction._life_vault_post_setup_validator = bv.Void()
LinkNodeAction._passwords_pre_setup_validator = bv.Void()
LinkNodeAction._passwords_post_setup_validator = bv.Void()
LinkNodeAction._other_validator = bv.Void()
LinkNodeAction._tagmap = {
    'unknown_action': LinkNodeAction._unknown_action_validator,
    'device_folder_pre_setup': LinkNodeAction._device_folder_pre_setup_validator,
    'life_vault_pre_setup': LinkNodeAction._life_vault_pre_setup_validator,
    'life_vault_post_setup': LinkNodeAction._life_vault_post_setup_validator,
    'passwords_pre_setup': LinkNodeAction._passwords_pre_setup_validator,
    'passwords_post_setup': LinkNodeAction._passwords_post_setup_validator,
    'other': LinkNodeAction._other_validator }
LinkNodeAction.unknown_action = LinkNodeAction('unknown_action')
LinkNodeAction.device_folder_pre_setup = LinkNodeAction('device_folder_pre_setup')
LinkNodeAction.life_vault_pre_setup = LinkNodeAction('life_vault_pre_setup')
LinkNodeAction.life_vault_post_setup = LinkNodeAction('life_vault_post_setup')
LinkNodeAction.passwords_pre_setup = LinkNodeAction('passwords_pre_setup')
LinkNodeAction.passwords_post_setup = LinkNodeAction('passwords_post_setup')
LinkNodeAction.other = LinkNodeAction('other')
LinkNodeEntity.action.validator = LinkNodeAction_validator
LinkNodeEntity._all_field_names_ = set([
    'action'])
LinkNodeEntity._all_fields_ = [
    ('action', LinkNodeEntity.action.validator)]
PerNodeMetadataEntity.bypass_behaviors.validator = bv.Nullable(BypassBehaviors_validator)
PerNodeMetadataEntity.suppress_delete.validator = bv.Nullable(bv.Boolean())
PerNodeMetadataEntity.suppress_move.validator = bv.Nullable(bv.Boolean())
PerNodeMetadataEntity.suppress_share.validator = bv.Nullable(bv.Boolean())
PerNodeMetadataEntity.link_node.validator = bv.Nullable(LinkNodeEntity_validator)
PerNodeMetadataEntity.suppress_ns_partition.validator = bv.Nullable(bv.Boolean())
PerNodeMetadataEntity.suppress_shared_link.validator = bv.Nullable(bv.Boolean())
PerNodeMetadataEntity.hide_extension.validator = bv.Nullable(bv.Boolean())
PerNodeMetadataEntity.suppress_remote_actions.validator = bv.Nullable(bv.Boolean())
PerNodeMetadataEntity.device_info.validator = bv.Nullable(DeviceInfoEntity_validator)
PerNodeMetadataEntity.encrypt_descendants.validator = bv.Nullable(bv.Boolean())
PerNodeMetadataEntity._all_field_names_ = set([
    'bypass_behaviors',
    'suppress_delete',
    'suppress_move',
    'suppress_share',
    'link_node',
    'suppress_ns_partition',
    'suppress_shared_link',
    'hide_extension',
    'suppress_remote_actions',
    'device_info',
    'encrypt_descendants'])
PerNodeMetadataEntity._all_fields_ = [
    ('bypass_behaviors', PerNodeMetadataEntity.bypass_behaviors.validator),
    ('suppress_delete', PerNodeMetadataEntity.suppress_delete.validator),
    ('suppress_move', PerNodeMetadataEntity.suppress_move.validator),
    ('suppress_share', PerNodeMetadataEntity.suppress_share.validator),
    ('link_node', PerNodeMetadataEntity.link_node.validator),
    ('suppress_ns_partition', PerNodeMetadataEntity.suppress_ns_partition.validator),
    ('suppress_shared_link', PerNodeMetadataEntity.suppress_shared_link.validator),
    ('hide_extension', PerNodeMetadataEntity.hide_extension.validator),
    ('suppress_remote_actions', PerNodeMetadataEntity.suppress_remote_actions.validator),
    ('device_info', PerNodeMetadataEntity.device_info.validator),
    ('encrypt_descendants', PerNodeMetadataEntity.encrypt_descendants.validator)]
DeviceInfoEntity.device_id.default = ''
DeviceInfoEntity.user_id.default = 0
LinkNodeEntity.action.default = LinkNodeAction.unknown_action
ROUTES = { }
