# Source Generated with Decompyle++
# File: generated.pyc (Python 3.11)

from typing import List, Optional, Text, Tuple
from dropbox.i18n import trans, ungettext
from dropbox.proto.nucleus.fsw_pb2 import ALLOW, CLOSE_DIALOG, LEARN_MORE_AND_CLOSE_DIALOG, MOVE_TO_TMF, REVERT, SHARE_AND_CLOSE_DIALOG, SHARE_AND_REVERT, DELETE_ITEMS, LEARN_MORE_AND_ALLOW
from dropbox.shared.util import format_html, format_text
from dropbox.url_info import dropbox_url_info
from dropbox.trace import TRACE
from base import FswDialogInterface
from dropbox.proto.nucleus.fsw_pb2 import AuxFSWButton, AuxButtonLearnMore, AuxButtonShare, UserFSWAction
from dropbox.proto.nucleus.types_pb2 import RRServerPath
from dropbox.proto.nucleus.fsw_generated_pb2 import ShowFSWDialogReq, AllowMoveFileOrFlatFolderOutOfTsd, AllowMoveNsOutOfTsd, AllowMoveToForbidNonTeamSharing, AllowMoveToForbidSharingWhenOwnerAclOnly, BlockMoveConfidentialNsOutOfTeamSpace, BlockMoveFileOrFlatFolderOutOfTeamSpace, BlockMoveForbidNonTeamSharingNsFromTsd, BlockMoveFromTeamSpaceToOutsideByViewer, BlockMoveNsOutOfTeamFolderByActorWithoutEditAccessToContainingNs, BlockMoveNsWithNestedNsFromTsd, BlockMoveOnlyOwnerCanUpdateAclNsFromTsd, BlockMoveSfToTfByEditorWhenNonOwnerCannotManageMembership, BlockMoveSfToTfByViewer, BlockMoveSfToTfNonOwnerDiffTeam, BlockMoveSharedFolderOutOfTsdByViewer, BlockMoveSharedFolderToVault, BlockNonLimitedTeamAndOwnerRemoveNsFromTeamFolder, BlockNonOwnerRemoveNsFromTeamFolder, BlockTmrMoveOutOfTeamSpace, CatchAllCopy, CdmOnboardingCopy, CdmOnboardingCreate, CdmOnboardingMove, CloudDocsCopyToIgnored, CloudDocsCreate, CloudDocsMoveOutside, CloudDocsMoveOutside2, CloudDocsMoveToIgnored, CloudDocsMoveToTrash, CloudDocsMoveToTrash2, CloudDocsMoveToTrashInaccessible, CloudDocsMoveToTrashInaccessible2, ConfidentialCopy, ConfidentialMove, DeviceFolderContentMoveToTrash, DeviceFolderContentMoveToTrashInaccessible, DeviceFolderMoveToTrash, DeviceFolderMoveToTrashInaccessible, DeviceFolderSuggestSelsync, DeviceFolderSuggestSelsyncTrashInaccessible, FileIsMovedFromUnencryptedToEncryptedFolder, FileIsMovedOutOfEncryptedFolder, MoveSfToTfNonOwnerConfirmation, PerNodeMetadataDeletableEntrypoint, PerNodeMetadataDeletableEntrypointTrashInaccessible, PerNodeMetadataMove, PerNodeMetadataMoveToTrash, PerNodeMetadataMoveToTrashInaccessible, PerNodeMetadataRename, Restorations1, Restorations1And3Inaccessible, Restorations2, Restorations3, Restorations4, Restorations5, Restorations5Inaccessible, Restorations6a, Restorations6aExample, Restorations6b, SharedFolderNesting, SharedFolderNestingImplicitShareOnMove, SharedFolderNestingOwnershipSteal, SharedFolderNestingOwnershipSurrender, SmartSyncMoveToTrash, SmartSyncMoveToTrashInaccessible, TeamFolderMove, TeamFolderMoveToTrash, TeamFolderMoveToTrashInaccessible, TeamMemberFolderCopy, TeamMemberFolderMove, TeamMemberFolderMoveToTrash, TeamMemberFolderMoveToTrashInaccessible, WarningTmrMoveOutOfTeamSpace

class AllowMoveFileOrFlatFolderOutOfTsdUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized AllowMoveFileOrFlatFolderOutOfTsdUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_src_tsd_top_level:
            if self._proto.num_others == 0:
                return format_text(trans('Move "%(name)s" out of the %(team_name)s team space?'), name = self._proto.name, team_name = self._proto.team_name)
            return format_text(ungettext('Move "%(name)s" and %(num_others)s other item out of the %(team_name)s team space?', 'Move "%(name)s" and %(num_others)s other items out of the %(team_name)s team space?', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others, team_name = self._proto.team_name)
        if None._proto.num_others == 0:
            return format_text(trans('Move "%(name)s" out of the shared folder "%(src_parent)s"?'), name = self._proto.name, src_parent = self._proto.src_parent)
        return format_text(ungettext('Move "%(name)s" and %(num_others)s other item out of the shared folder "%(src_parent)s"?', 'Move "%(name)s" and %(num_others)s other items out of the shared folder "%(src_parent)s"?', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others, src_parent = self._proto.src_parent)

    
    def get_message(self):
        if self._proto.is_src_tsd_top_level:
            if self._proto.is_file:
                if self._proto.num_others == 0:
                    return format_html(trans('Moving this file to <b>%(dest)s</b> will remove it for everyone at %(team_name)s.'), dest = self._proto.dest, team_name = self._proto.team_name)
                return format_html(trans('Moving these items to <b>%(dest)s</b> will remove them for everyone at %(team_name)s.'), dest = self._proto.dest, team_name = self._proto.team_name)
            if None._proto.num_others == 0:
                return format_html(trans('Moving this folder to <b>%(dest)s</b> will remove it for everyone at %(team_name)s.'), dest = self._proto.dest, team_name = self._proto.team_name)
            return format_html(trans('Moving these items to <b>%(dest)s</b> will remove them for everyone at %(team_name)s.'), dest = self._proto.dest, team_name = self._proto.team_name)
        if None._proto.is_file:
            if self._proto.num_others == 0:
                return format_html(trans('Moving this file to <b>%(dest)s</b> will remove it for members of <b>%(src_parent)s</b>.'), dest = self._proto.dest, src_parent = self._proto.src_parent)
            return format_html(trans('Moving these items to <b>%(dest)s</b> will remove them for members of <b>%(src_parent)s</b>.'), dest = self._proto.dest, src_parent = self._proto.src_parent)
        if None._proto.num_others == 0:
            return format_html(trans('Moving this folder to <b>%(dest)s</b> will remove it for members of <b>%(src_parent)s</b>.'), dest = self._proto.dest, src_parent = self._proto.src_parent)
        return format_html(trans('Moving these items to <b>%(dest)s</b> will remove them for members of <b>%(src_parent)s</b>.'), dest = self._proto.dest, src_parent = self._proto.src_parent)

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Move anyway'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class AllowMoveNsOutOfTsdUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized AllowMoveNsOutOfTsdUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_src_tsd_top_level:
            if self._proto.num_others == 0:
                return format_text(trans('Move "%(name)s" out of the %(team_name)s team space?'), name = self._proto.name, team_name = self._proto.team_name)
            return format_text(ungettext('Move "%(name)s" and %(num_others)s other item out of the %(team_name)s team space?', 'Move "%(name)s" and %(num_others)s other items out of the %(team_name)s team space?', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others, team_name = self._proto.team_name)
        if None._proto.num_others == 0:
            return format_text(trans('Move "%(name)s" out of the shared folder "%(src_parent)s"?'), name = self._proto.name, src_parent = self._proto.src_parent)
        return format_text(ungettext('Move "%(name)s" and %(num_others)s other item out of the shared folder "%(src_parent)s"?', 'Move "%(name)s" and %(num_others)s other items out of the shared folder "%(src_parent)s"?', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others, src_parent = self._proto.src_parent)

    
    def get_message(self):
        if self._proto.is_src_tsd_top_level:
            if self._proto.num_others == 0:
                return format_html(trans('Moving this folder to <b>%(dest)s</b> will remove it for everyone at %(team_name)s.'), dest = self._proto.dest, team_name = self._proto.team_name)
            return format_html(trans('Moving these items to <b>%(dest)s</b> will remove them for everyone at %(team_name)s.'), dest = self._proto.dest, team_name = self._proto.team_name)
        if None._proto.num_others == 0:
            return format_html(trans('Moving this folder to <b>%(dest)s</b> will remove it for members of <b>%(src_parent)s</b>.'), dest = self._proto.dest, src_parent = self._proto.src_parent)
        return format_html(trans('Moving these items to <b>%(dest)s</b> will remove them for members of <b>%(src_parent)s</b>.'), dest = self._proto.dest, src_parent = self._proto.src_parent)

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Move anyway'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class AllowMoveToForbidNonTeamSharingUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized AllowMoveToForbidNonTeamSharingUI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('Move item to location with more limited access?'))
        return format_text(trans('Move items to location with more limited access?'))

    
    def get_message(self):
        if self._proto.num_others == 0:
            return format_html(trans('Anyone who was directly invited to <b>%(name)s</b> will keep their access.  <a href="%(help_url)s">How to manage access</a>'), name = self._proto.name, help_url = dropbox_url_info.help_url('folder_permissions'))
        return format_html(ungettext('Anyone who was directly invited to <b>%(name)s</b> and %(num_others)s other item will keep their access.  <a href="%(help_url)s">How to manage access</a>', 'Anyone who was directly invited to <b>%(name)s</b> and %(num_others)s other items will keep their access.  <a href="%(help_url)s">How to manage access</a>', self._proto.num_others), help_url = dropbox_url_info.help_url('folder_permissions'), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Move'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class AllowMoveToForbidSharingWhenOwnerAclOnlyUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized AllowMoveToForbidSharingWhenOwnerAclOnlyUI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('Move item to location with more limited access?'))
        return format_text(trans('Move items to location with more limited access?'))

    
    def get_message(self):
        if self._proto.num_others == 0:
            return format_html(trans('Anyone who was directly invited to <b>%(name)s</b> will keep their access.  <a href="%(help_url)s">How to manage access</a>'), name = self._proto.name, help_url = dropbox_url_info.help_url('folder_permissions'))
        return format_html(ungettext('Anyone who was directly invited to <b>%(name)s</b> and %(num_others)s other item will keep their access.  <a href="%(help_url)s">How to manage access</a>', 'Anyone who was directly invited to <b>%(name)s</b> and %(num_others)s other items will keep their access.  <a href="%(help_url)s">How to manage access</a>', self._proto.num_others), help_url = dropbox_url_info.help_url('folder_permissions'), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Move'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class BlockMoveConfidentialNsOutOfTeamSpaceUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized BlockMoveConfidentialNsOutOfTeamSpaceUI %r', proto)

    
    def get_caption(self):
        if self._proto.num == 0:
            return format_text(trans('Can\'t move "%(name)s" out of the %(team_name)s team space'), name = self._proto.name, team_name = self._proto.team_name)
        return format_text(ungettext('Can\'t move "%(name)s" out of the %(team_name)s team space', "Can't move %(num)s items", self._proto.num), name = self._proto.name, num = self._proto.num, team_name = self._proto.team_name)

    
    def get_message(self):
        if self._proto.num == 0:
            return format_html(trans('Moving this folder here would change who can access it. If you need to change who can access the folder, right-click it and select Share.'))
        return format_html(ungettext('Moving this folder here would change who can access it. If you need to change who can access the folder, right-click it and select Share.', "You don't have permission to move some of these items. Try moving items individually.", self._proto.num))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('confidential_move')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class BlockMoveFileOrFlatFolderOutOfTeamSpaceUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized BlockMoveFileOrFlatFolderOutOfTeamSpaceUI %r', proto)

    
    def get_caption(self):
        if self._proto.num == 0:
            return format_text(trans('Can\'t move "%(name)s" out of the %(team_name)s team space'), name = self._proto.name, team_name = self._proto.team_name)
        return format_text(ungettext('Can\'t move "%(name)s" out of the %(team_name)s team space', "Can't move %(num)s items", self._proto.num), name = self._proto.name, num = self._proto.num, team_name = self._proto.team_name)

    
    def get_message(self):
        if self._proto.is_file:
            if self._proto.num == 0:
                return format_html(trans('To move this file, you need access to edit the folder it is in. Ask your admin for permission.'))
            return format_html(ungettext('To move this file, you need access to edit the folder it is in. Ask your admin for permission.', "You don't have permission to move some of these items. Try moving items individually.", self._proto.num))
        if None._proto.num == 0:
            return format_html(trans('To move this folder, you need access to edit the folder it is in. Ask your admin for permission.'))
        return format_html(ungettext('To move this folder, you need access to edit the folder it is in. Ask your admin for permission.', "You don't have permission to move some of these items. Try moving items individually.", self._proto.num))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('remove_from_tsd')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class BlockMoveForbidNonTeamSharingNsFromTsdUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized BlockMoveForbidNonTeamSharingNsFromTsdUI %r', proto)

    
    def get_caption(self):
        if self._proto.num == 0:
            return format_text(trans('Can\'t move "%(name)s" out of the %(team_name)s team space'), name = self._proto.name, team_name = self._proto.team_name)
        return format_text(ungettext('Can\'t move "%(name)s" out of the %(team_name)s team space', "Can't move %(num)s items", self._proto.num), name = self._proto.name, num = self._proto.num, team_name = self._proto.team_name)

    
    def get_message(self):
        if self._proto.num == 0:
            return format_html(trans('If you need to move this folder, ask your admin to move it for you.'))
        return format_html(ungettext('If you need to move this folder, ask your admin to move it for you.', "You don't have permission to move some of these items. Try moving items individually.", self._proto.num))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('remove_from_tsd')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class BlockMoveFromTeamSpaceToOutsideByViewerUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized BlockMoveFromTeamSpaceToOutsideByViewerUI %r', proto)

    
    def get_caption(self):
        if self._proto.num == 0:
            return format_text(trans('Can\'t move "%(name)s" to "%(dest)s" folder'), name = self._proto.name, dest = self._proto.dest)
        return format_text(ungettext('Can\'t move "%(name)s" to "%(dest)s" folder', 'Can\'t move %(num)s items to "%(dest)s" folder', self._proto.num), dest = self._proto.dest, name = self._proto.name, num = self._proto.num)

    
    def get_message(self):
        if self._proto.is_file:
            if self._proto.is_source_account_cdm:
                if self._proto.num == 0:
                    return format_html(trans('Moving this shared file to your <b>%(dest)s</b> folder would remove it for everyone else at %(team_name)s. <a href="%(cdm_help_url)s">Learn more about sharing</a>'), dest = self._proto.dest, team_name = self._proto.team_name, cdm_help_url = dropbox_url_info.help_url('remove_from_tsd'))
                return format_html(ungettext('Moving this shared file to your <b>%(dest)s</b> folder would remove it for everyone else at %(team_name)s. <a href="%(cdm_help_url)s">Learn more about sharing</a>', 'Moving these items to your <b>%(dest)s</b> folder would remove it for everyone else at %(team_name)s. <a href="%(cdm_help_url)s">Learn more about sharing</a>', self._proto.num), cdm_help_url = dropbox_url_info.help_url('remove_from_tsd'), dest = self._proto.dest, team_name = self._proto.team_name)
            if None._proto.num == 0:
                return format_html(trans('This file can\'t be moved out of a team folder. <a href="%(gg_help_url)s">Learn more about sharing</a>'), gg_help_url = dropbox_url_info.help_url('fsw_ggtf_content_move'))
            return format_html(ungettext('This file can\'t be moved out of a team folder. <a href="%(gg_help_url)s">Learn more about sharing</a>', 'These items can\'t be moved out of a team folder. <a href="%(gg_help_url)s">Learn more about sharing</a>', self._proto.num), gg_help_url = dropbox_url_info.help_url('fsw_ggtf_content_move'))
        if None._proto.is_source_account_cdm:
            if self._proto.num == 0:
                return format_html(trans('Moving this shared folder to your <b>%(dest)s</b> folder would remove it for everyone else at %(team_name)s. <a href="%(cdm_help_url)s">Learn more about sharing</a>'), dest = self._proto.dest, team_name = self._proto.team_name, cdm_help_url = dropbox_url_info.help_url('remove_from_tsd'))
            return format_html(ungettext('Moving this shared folder to your <b>%(dest)s</b> folder would remove it for everyone else at %(team_name)s. <a href="%(cdm_help_url)s">Learn more about sharing</a>', 'Moving these items to your <b>%(dest)s</b> folder would remove it for everyone else at %(team_name)s. <a href="%(cdm_help_url)s">Learn more about sharing</a>', self._proto.num), cdm_help_url = dropbox_url_info.help_url('remove_from_tsd'), dest = self._proto.dest, team_name = self._proto.team_name)
        if None._proto.num == 0:
            return format_html(trans('This folder can\'t be moved out of a team folder. <a href="%(gg_help_url)s">Learn more about sharing</a>'), gg_help_url = dropbox_url_info.help_url('fsw_ggtf_content_move'))
        return format_html(ungettext('This folder can\'t be moved out of a team folder. <a href="%(gg_help_url)s">Learn more about sharing</a>', 'These items can\'t be moved out of a team folder. <a href="%(gg_help_url)s">Learn more about sharing</a>', self._proto.num), gg_help_url = dropbox_url_info.help_url('fsw_ggtf_content_move'))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class BlockMoveNsOutOfTeamFolderByActorWithoutEditAccessToContainingNsUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized BlockMoveNsOutOfTeamFolderByActorWithoutEditAccessToContainingNsUI %r', proto)

    
    def get_caption(self):
        if self._proto.num == 0:
            return format_text(trans('Can\'t move "%(name)s" to "%(dest)s"'), name = self._proto.name, dest = self._proto.dest)
        return format_text(ungettext('Can\'t move "%(name)s" to "%(dest)s"', "Can't move %(num)s items", self._proto.num), dest = self._proto.dest, name = self._proto.name, num = self._proto.num)

    
    def get_message(self):
        if self._proto.num == 0:
            return format_html(trans('To move this folder, you need access to edit it and the folder it is in.'))
        return format_html(ungettext('To move this folder, you need access to edit it and the folder it is in.', "You don't have permission to move some of these items. Try moving items individually.", self._proto.num))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('remove_from_tsd')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class BlockMoveNsWithNestedNsFromTsdUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized BlockMoveNsWithNestedNsFromTsdUI %r', proto)

    
    def get_caption(self):
        if self._proto.num == 0:
            return format_text(trans('Can\'t move "%(name)s" out of the %(team_name)s team space'), name = self._proto.name, team_name = self._proto.team_name)
        return format_text(ungettext('Can\'t move "%(name)s" out of the %(team_name)s team space', "Can't move %(num)s items", self._proto.num), name = self._proto.name, num = self._proto.num, team_name = self._proto.team_name)

    
    def get_message(self):
        if self._proto.num == 0:
            return format_html(trans('This folder has other shared folders inside it. Try moving each shared folder individually.'))
        return format_html(ungettext('This folder has other shared folders inside it. Try moving each shared folder individually.', "You don't have permission to move some of these items. Try moving items individually.", self._proto.num))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('remove_from_tsd')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class BlockMoveOnlyOwnerCanUpdateAclNsFromTsdUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized BlockMoveOnlyOwnerCanUpdateAclNsFromTsdUI %r', proto)

    
    def get_caption(self):
        if self._proto.num == 0:
            return format_text(trans('Can\'t move "%(name)s" out of the %(team_name)s team space'), name = self._proto.name, team_name = self._proto.team_name)
        return format_text(ungettext('Can\'t move "%(name)s" out of the %(team_name)s team space', "Can't move %(num)s items", self._proto.num), name = self._proto.name, num = self._proto.num, team_name = self._proto.team_name)

    
    def get_message(self):
        if self._proto.num == 0:
            return format_html(trans('If you need to move this folder, ask your admin to move it for you.'))
        return format_html(ungettext('If you need to move this folder, ask your admin to move it for you.', "You don't have permission to move some of these items. Try moving items individually.", self._proto.num))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('remove_from_tsd')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class BlockMoveSfToTfByEditorWhenNonOwnerCannotManageMembershipUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized BlockMoveSfToTfByEditorWhenNonOwnerCannotManageMembershipUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_source_account_cdm:
            if self._proto.num == 0:
                return format_text(trans('Can\'t move the "%(src_name)s" shared folder into the %(team_name)s team space'), src_name = self._proto.src_name, team_name = self._proto.team_name)
            return format_text(ungettext('Can\'t move the "%(src_name)s" shared folder into the %(team_name)s team space', "Can't move shared folders into the %(team_name)s team space", self._proto.num), src_name = self._proto.src_name, team_name = self._proto.team_name)
        if None._proto.num == 0:
            return format_text(trans('Can\'t move the "%(src_name)s" shared folder to a team folder'), src_name = self._proto.src_name)
        return format_text(ungettext('Can\'t move the "%(src_name)s" shared folder to a team folder', "Can't move shared folders to a team folder", self._proto.num), src_name = self._proto.src_name)

    
    def get_message(self):
        if self._proto.is_source_account_cdm:
            if self._proto.num == 0:
                return format_html(trans('Only the owner of this shared folder can move it to the %(team_name)s team space.'), team_name = self._proto.team_name)
            return format_html(ungettext('Only the owner of this shared folder can move it to the %(team_name)s team space.', "You don't have permission to move some of these items. Try moving items individually.", self._proto.num), team_name = self._proto.team_name)
        if None._proto.num == 0:
            return format_html(trans('Only the owner of this shared folder can move it to a team folder.'))
        return format_html(ungettext('Only the owner of this shared folder can move it to a team folder.', "You don't have permission to move some of these items. Try moving items individually.", self._proto.num))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('See owner'))

        
        def get_button1():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(share = AuxButtonShare(location_rr_paths = fsw_dialog.block_move_sf_to_tf_by_editor_when_non_owner_cannot_manage_membership.share_button_rr_paths), button_action = SHARE_AND_CLOSE_DIALOG)),
            (get_button1(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('fsw_ownership_change')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class BlockMoveSfToTfByViewerUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized BlockMoveSfToTfByViewerUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_source_account_cdm:
            if self._proto.num == 0:
                return format_text(trans('Can\'t move the "%(src_name)s" shared folder into the %(team_name)s team space'), src_name = self._proto.src_name, team_name = self._proto.team_name)
            return format_text(ungettext('Can\'t move the "%(src_name)s" shared folder into the %(team_name)s team space', "Can't move shared folders into the %(team_name)s team space", self._proto.num), src_name = self._proto.src_name, team_name = self._proto.team_name)
        if None._proto.num == 0:
            return format_text(trans('Can\'t move the "%(src_name)s" shared folder to a team folder'), src_name = self._proto.src_name)
        return format_text(ungettext('Can\'t move the "%(src_name)s" shared folder to a team folder', "Can't move shared folders to a team folder", self._proto.num), src_name = self._proto.src_name)

    
    def get_message(self):
        if self._proto.num == 0:
            return format_html(trans('You can only view this shared folder. Ask an owner or editor of the folder for access to edit it.'))
        return format_html(ungettext('You can only view this shared folder. Ask an owner or editor of the folder for access to edit it.', "You don't have permission to move some of these items. Try moving items individually.", self._proto.num))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('See owner'))

        
        def get_button1():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(share = AuxButtonShare(location_rr_paths = fsw_dialog.block_move_sf_to_tf_by_viewer.share_button_rr_paths), button_action = SHARE_AND_CLOSE_DIALOG)),
            (get_button1(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('fsw_ownership_change')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class BlockMoveSfToTfNonOwnerDiffTeamUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized BlockMoveSfToTfNonOwnerDiffTeamUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_source_account_cdm:
            if self._proto.num == 0:
                return format_text(trans('Can\'t move the "%(src_name)s" shared folder into the %(team_name)s team space'), src_name = self._proto.src_name, team_name = self._proto.team_name)
            return format_text(ungettext('Can\'t move the "%(src_name)s" shared folder into the %(team_name)s team space', "Can't move shared folders into the %(team_name)s team space", self._proto.num), src_name = self._proto.src_name, team_name = self._proto.team_name)
        if None._proto.num == 0:
            return format_text(trans('Can\'t move the "%(src_name)s" shared folder to a team folder'), src_name = self._proto.src_name)
        return format_text(ungettext('Can\'t move the "%(src_name)s" shared folder to a team folder', "Can't move shared folders to a team folder", self._proto.num), src_name = self._proto.src_name)

    
    def get_message(self):
        if self._proto.is_team:
            if self._proto.num == 0:
                return format_html(trans("The owner of this shared folder isn't a member of %(team_name)s."), team_name = self._proto.team_name)
            return format_html(ungettext("The owner of this shared folder isn't a member of %(team_name)s.", "You don't have permission to move some of these items. Try moving items individually.", self._proto.num), team_name = self._proto.team_name)
        if None._proto.num == 0:
            return format_html(trans('The owner of this shared folder is a member of another team.'))
        return format_html(ungettext('The owner of this shared folder is a member of another team.', "You don't have permission to move some of these items. Try moving items individually.", self._proto.num))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('See owner'))

        
        def get_button1():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(share = AuxButtonShare(location_rr_paths = fsw_dialog.block_move_sf_to_tf_non_owner_diff_team.share_button_rr_paths), button_action = SHARE_AND_CLOSE_DIALOG)),
            (get_button1(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('fsw_ownership_change')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class BlockMoveSharedFolderOutOfTsdByViewerUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized BlockMoveSharedFolderOutOfTsdByViewerUI %r', proto)

    
    def get_caption(self):
        if self._proto.num == 0:
            return format_text(trans('Can\'t move "%(name)s" out of the %(team_name)s team space'), name = self._proto.name, team_name = self._proto.team_name)
        return format_text(ungettext('Can\'t move "%(name)s" out of the %(team_name)s team space', "Can't move %(num)s items", self._proto.num), name = self._proto.name, num = self._proto.num, team_name = self._proto.team_name)

    
    def get_message(self):
        if self._proto.num == 0:
            return format_html(trans('To move this folder, you need access to edit it. Ask your admin for permission.'))
        return format_html(ungettext('To move this folder, you need access to edit it. Ask your admin for permission.', "You don't have permission to move some of these items. Try moving items individually.", self._proto.num))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('remove_from_tsd')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class BlockMoveSharedFolderToVaultUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized BlockMoveSharedFolderToVaultUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Can’t move shared folders into vault'))

    
    def get_message(self):
        if self._proto.num_others == 0:
            return format_text(trans('Unshare "%(source_path)s" first, or add a copy of this folder to vault instead.'), source_path = self._proto.source_path)
        return format_text(trans('Unshare these folders first, or add copies of these folders to vault instead.'))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn more'))

        
        def get_button0_url():
            return dropbox_url_info.construct_full_url('help/files-folders/sort-preview/dropbox-vault')

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = get_button0_url()), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class BlockNonLimitedTeamAndOwnerRemoveNsFromTeamFolderUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized BlockNonLimitedTeamAndOwnerRemoveNsFromTeamFolderUI %r', proto)

    
    def get_caption(self):
        if self._proto.num == 0:
            return format_text(trans('Can\'t move "%(name)s" to "%(dest)s"'), name = self._proto.name, dest = self._proto.dest)
        return format_text(ungettext('Can\'t move "%(name)s" to "%(dest)s"', "Can't move %(num)s items", self._proto.num), dest = self._proto.dest, name = self._proto.name, num = self._proto.num)

    
    def get_message(self):
        if self._proto.num == 0:
            return format_html(trans('To move this folder out of its team folder, go to the Dropbox.com website.'))
        return format_html(ungettext('To move this folder out of its team folder, go to the Dropbox.com website.', 'To move these items, go to the Dropbox.com website.', self._proto.num))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('fsw_ggtf_owner_content_move')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class BlockNonOwnerRemoveNsFromTeamFolderUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized BlockNonOwnerRemoveNsFromTeamFolderUI %r', proto)

    
    def get_caption(self):
        if self._proto.num == 0:
            return format_text(trans('Can\'t move "%(name)s" to "%(dest)s"'), name = self._proto.name, dest = self._proto.dest)
        return format_text(ungettext('Can\'t move "%(name)s" to "%(dest)s"', "Can't move %(num)s items", self._proto.num), dest = self._proto.dest, name = self._proto.name, num = self._proto.num)

    
    def get_message(self):
        if self._proto.num == 0:
            return format_html(trans("This folder can't be moved out of a team folder."))
        return format_html(ungettext("This folder can't be moved out of a team folder.", "These items can't be moved out of a team folder.", self._proto.num))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('fsw_ggtf_content_move')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class BlockTmrMoveOutOfTeamSpaceUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized BlockTmrMoveOutOfTeamSpaceUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_file:
            return format_text(trans('Files stay here, for the team'))
        return format_text(trans('Team folders stay here, for the team'))

    
    def get_message(self):
        if self._proto.is_file:
            if self._proto.num == 0:
                return format_html(trans('To change who can access this file, right-click it and select Share. To make a copy, right-click and select Copy.'))
            return format_html(ungettext('To change who can access this file, right-click it and select Share. To make a copy, right-click and select Copy.', 'To change who can access these files, right-click them and select Share. To make a copy, right-click and select Copy.', self._proto.num))
        if None._proto.num == 0:
            return format_html(trans('To change who can access this folder, right-click it and select Share. To make a copy, right-click and select Copy.'))
        return format_html(ungettext('To change who can access this folder, right-click it and select Share. To make a copy, right-click and select Copy.', 'To change who can access these folders, right-click them and select Share. To make a copy, right-click and select Copy.', self._proto.num))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('remove_from_tsd')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class CatchAllCopyUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized CatchAllCopyUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Dropbox detected that you copied %(src_name)s and %(num_others)s other files to %(dst_folder_name)s'), src_name = self._proto.src_name, num_others = self._proto.num_others, dst_folder_name = self._proto.dst_folder_name)

    
    def get_message(self):
        return format_html(trans('If this is incorrect, please file a bug through the desktop bug reporter, providing as many details as possible. You can also reach out to us on Slack at #sync-help.'))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class CdmOnboardingCopyUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized CdmOnboardingCopyUI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('Save "%(dest_name)s" to the %(team_name)s team space?'), dest_name = self._proto.dest_name, team_name = self._proto.team_name)
        return format_text(ungettext('Save "%(dest_name)s" and %(num_others)s other item to the %(team_name)s team space?', 'Save "%(dest_name)s" and %(num_others)s other items to the %(team_name)s team space?', self._proto.num_others), dest_name = self._proto.dest_name, num_others = self._proto.num_others, team_name = self._proto.team_name)

    
    def get_message(self):
        if self._proto.num_others == 0:
            return format_html(trans('If you save this item here, everyone at <b>%(team_name)s</b> will be able to access it. Otherwise, you can save them to your member folder <b>%(home_name)s</b>, and only you will have access.'), team_name = self._proto.team_name, home_name = self._proto.home_name)
        return format_html(trans('If you save these items here, everyone at <b>%(team_name)s</b> will be able to access them. Otherwise, you can save them to your member folder <b>%(home_name)s</b>, and only you will have access.'), team_name = self._proto.team_name, home_name = self._proto.home_name)

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Save to team space'))

        
        def get_button1():
            return format_text(trans('Move to member folder'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), MOVE_TO_TMF)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class CdmOnboardingCreateUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized CdmOnboardingCreateUI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('Save "%(dest_name)s" to the %(team_name)s team space?'), dest_name = self._proto.dest_name, team_name = self._proto.team_name)
        return format_text(ungettext('Save "%(dest_name)s" and %(num_others)s other item to the %(team_name)s team space?', 'Save "%(dest_name)s" and %(num_others)s other items to the %(team_name)s team space?', self._proto.num_others), dest_name = self._proto.dest_name, num_others = self._proto.num_others, team_name = self._proto.team_name)

    
    def get_message(self):
        if self._proto.num_others == 0:
            return format_html(trans('If you save this item here, everyone at <b>%(team_name)s</b> will be able to access it. Otherwise, you can save them to your member folder <b>%(home_name)s</b>, and only you will have access.'), team_name = self._proto.team_name, home_name = self._proto.home_name)
        return format_html(trans('If you save these items here, everyone at <b>%(team_name)s</b> will be able to access them. Otherwise, you can save them to your member folder <b>%(home_name)s</b>, and only you will have access.'), team_name = self._proto.team_name, home_name = self._proto.home_name)

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Save to team space'))

        
        def get_button1():
            return format_text(trans('Move to member folder'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), MOVE_TO_TMF)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class CdmOnboardingMoveUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized CdmOnboardingMoveUI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('Share "%(src_name)s" with everyone at %(team_name)s?'), src_name = self._proto.src_name, team_name = self._proto.team_name)
        return format_text(ungettext('Share "%(src_name)s" and %(num_others)s other item with everyone at %(team_name)s?', 'Share "%(src_name)s" and %(num_others)s other items with everyone at %(team_name)s?', self._proto.num_others), num_others = self._proto.num_others, src_name = self._proto.src_name, team_name = self._proto.team_name)

    
    def get_message(self):
        if self._proto.num_others == 0:
            return format_html(trans('If you move this item here, everyone at <b>%(team_name)s</b> will be able to access it.'), team_name = self._proto.team_name)
        return format_html(trans('If you move these items here, everyone at <b>%(team_name)s</b> will be able to access them.'), team_name = self._proto.team_name)

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Share'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class CloudDocsCopyToIgnoredUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized CloudDocsCopyToIgnoredUI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('Can’t copy online-only content “%(name)s” into an ignored folder that is not syncing to dropbox.com'), name = self._proto.name)
        return format_text(ungettext('Can’t copy online-only content “%(name)s” and %(num_others)s other file into an ignored folder that is not syncing to dropbox.com', 'Can’t copy online-only content “%(name)s” and %(num_others)s other files into an ignored folder that is not syncing to dropbox.com', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.num_others == 0:
            return format_html(trans('Warning, copying this file into an ignored folder will mean it will stop working.'))
        return format_html(trans('Warning, copying these files into an ignored folder will mean it will stop working.'))

    
    def get_checkbox_message(self):
        return format_text(trans('Don’t tell me this again'))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn more'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('cloud_docs_upload')), button_action = LEARN_MORE_AND_ALLOW))]



class CloudDocsCreateUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized CloudDocsCreateUI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('Web-based file “%(name)s” might not work in Dropbox'), name = self._proto.name)
        return format_text(ungettext('“%(name)s” and %(num_others)s other web-based file might not work in Dropbox', '“%(name)s” and %(num_others)s other web-based files might not work in Dropbox', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.num_others == 0:
            return format_html(trans('Because this web-based file was created outside Dropbox, it might not work in Dropbox.'))
        return format_html(trans('Because these web-based files were created outside Dropbox, they might not work in Dropbox.'))

    
    def get_checkbox_message(self):
        return format_text(trans('Don’t tell me this again'))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn more'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('cloud_docs_upload')), button_action = LEARN_MORE_AND_ALLOW))]



class CloudDocsMoveOutsideUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized CloudDocsMoveOutsideUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_folder:
            if self._proto.num_others == 0:
                return format_text(trans('Can’t move “%(name)s” out of Dropbox because it has web-based files inside'), name = self._proto.name)
            return format_text(ungettext('Can’t move “%(name)s” and %(num_others)s other folder out of Dropbox because they have web-based files inside', 'Can’t move “%(name)s” and %(num_others)s other folders out of Dropbox because they have web-based files inside', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)
        if None._proto.num_others == 0:
            return format_text(trans('Can’t move web-based file “%(name)s” out of Dropbox'), name = self._proto.name)
        return format_text(ungettext('Can’t move “%(name)s” and %(num_others)s other web-based file out of Dropbox', 'Can’t move “%(name)s” and %(num_others)s other web-based files out of Dropbox', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.is_folder:
            if self._proto.is_single_folder:
                if self._proto.num_files == 0:
                    return format_html(trans('This folder has %(num_files)s web-based file inside.<br><br>Web-based file types like .gdoc and .gsheet will only work in Dropbox.'), num_files = self._proto.num_files)
                return format_html(ungettext('This folder has %(num_files)s web-based file inside.<br><br>Web-based file types like .gdoc and .gsheet will only work in Dropbox.', 'This folder has %(num_files)s web-based files inside.<br><br>Web-based file types like .gdoc and .gsheet will only work in Dropbox.', self._proto.num_files), num_files = self._proto.num_files)
            if None._proto.num_files == 0:
                return format_html(trans('These folders have %(num_files)s web-based file inside.<br><br>Web-based file types like .gdoc and .gsheet will only work in Dropbox.'), num_files = self._proto.num_files)
            return format_html(ungettext('These folders have %(num_files)s web-based file inside.<br><br>Web-based file types like .gdoc and .gsheet will only work in Dropbox.', 'These folders have %(num_files)s web-based files inside.<br><br>Web-based file types like .gdoc and .gsheet will only work in Dropbox.', self._proto.num_files), num_files = self._proto.num_files)
        if None._proto.is_single_folder:
            if self._proto.num_files == 0:
                return format_html(trans('Web-based file types like .gdoc and .gsheet will only work in Dropbox.'))
            return format_html(trans('Web-based file types like .gdoc and .gsheet will only work in Dropbox.'))
        if None._proto.num_files == 0:
            return format_html(trans('Web-based file types like .gdoc and .gsheet will only work in Dropbox.'))
        return format_html(trans('Web-based file types like .gdoc and .gsheet will only work in Dropbox.'))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class CloudDocsMoveOutside2UI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized CloudDocsMoveOutside2UI %r', proto)

    
    def get_caption(self):
        if self._proto.is_folder:
            if self._proto.num_others == 0:
                return format_text(trans('Can’t move “%(name)s” out of Dropbox because it has web-based files inside'), name = self._proto.name)
            return format_text(ungettext('Can’t move “%(name)s” and %(num_others)s other folder out of Dropbox because they have web-based files inside', 'Can’t move “%(name)s” and %(num_others)s other folders out of Dropbox because they have web-based files inside', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)
        if None._proto.num_others == 0:
            return format_text(trans('Can’t move web-based file “%(name)s” out of Dropbox'), name = self._proto.name)
        return format_text(ungettext('Can’t move “%(name)s” and %(num_others)s other web-based file out of Dropbox', 'Can’t move “%(name)s” and %(num_others)s other web-based files out of Dropbox', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.is_folder:
            if self._proto.is_single_folder:
                if self._proto.num_other_files == 0:
                    return format_html(trans('<b>%(file_name)s</b> is a web-based file and will only work in Dropbox.'), file_name = self._proto.file_name)
                return format_html(ungettext('<b>%(file_name)s</b>  and %(num_other_files)s other web-based file will only work in Dropbox.', '<b>%(file_name)s</b>  and %(num_other_files)s other web-based files will only work in Dropbox.', self._proto.num_other_files), file_name = self._proto.file_name, num_other_files = self._proto.num_other_files)
            if None._proto.num_other_files == 0:
                return format_html(trans('<b>%(file_name)s</b> is a web-based file and will only work in Dropbox.'), file_name = self._proto.file_name)
            return format_html(ungettext('<b>%(file_name)s</b>  and %(num_other_files)s other web-based file will only work in Dropbox.', '<b>%(file_name)s</b>  and %(num_other_files)s other web-based files will only work in Dropbox.', self._proto.num_other_files), file_name = self._proto.file_name, num_other_files = self._proto.num_other_files)
        if None._proto.is_single_folder:
            if self._proto.num_other_files == 0:
                return format_html(trans('Web-based files will only work in Dropbox.'))
            return format_html(trans('Web-based files will only work in Dropbox.'))
        if None._proto.num_other_files == 0:
            return format_html(trans('Web-based files will only work in Dropbox.'))
        return format_html(trans('Web-based files will only work in Dropbox.'))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class CloudDocsMoveToIgnoredUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized CloudDocsMoveToIgnoredUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_folder:
            if self._proto.num_others == 0:
                return format_text(trans('Can’t move “%(name)s” into an ignored folder that is not syncing to dropbox.com because it contains online-only content'), name = self._proto.name)
            return format_text(ungettext('Can’t move “%(name)s” and %(num_others)s other folder into an ignored folder that is not syncing to dropbox.com because they contain online-only content', 'Can’t move “%(name)s” and %(num_others)s other folders into an ignored folder that is not syncing to dropbox.com because they contain online-only content', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)
        if None._proto.num_others == 0:
            return format_text(trans('Can’t move online-only content “%(name)s” into an ignored folder that is not syncing to dropbox.com'), name = self._proto.name)
        return format_text(ungettext('Can’t move online-only content “%(name)s” and %(num_others)s other file into an ignored folder that is not syncing to dropbox.com', 'Can’t move online-only content “%(name)s” and %(num_others)s other files into an ignored folder that is not syncing to dropbox.com', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.is_folder:
            if self._proto.is_single_folder:
                if self._proto.num_files == 0:
                    return format_html(trans('You can change this ignored setting at any time by right clicking your folder and selecting Sync to dropbox.com.'))
                return format_html(trans('You can change this ignored setting at any time by right clicking your folder and selecting Sync to dropbox.com.'))
            if None._proto.num_files == 0:
                return format_html(trans('You can change this ignored setting at any time by right clicking your folder and selecting Sync to dropbox.com.'))
            return format_html(trans('You can change this ignored setting at any time by right clicking your folder and selecting Sync to dropbox.com.'))
        if None._proto.is_single_folder:
            if self._proto.num_files == 0:
                return format_html(trans('You can change this ignored setting at any time by right clicking your folder and selecting Sync to dropbox.com.'))
            return format_html(trans('You can change this ignored setting at any time by right clicking your folder and selecting Sync to dropbox.com.'))
        if None._proto.num_files == 0:
            return format_html(trans('You can change this ignored setting at any time by right clicking your folder and selecting Sync to dropbox.com.'))
        return format_html(trans('You can change this ignored setting at any time by right clicking your folder and selecting Sync to dropbox.com.'))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class CloudDocsMoveToTrashUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized CloudDocsMoveToTrashUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_folder:
            if self._proto.num_others == 0:
                return format_text(trans('Delete “%(name)s” from your Dropbox account?'), name = self._proto.name)
            return format_text(ungettext('Delete “%(name)s” and %(num_others)s other folder from your Dropbox account?', 'Delete “%(name)s” and %(num_others)s other folders from your Dropbox account?', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)
        if None._proto.num_others == 0:
            return format_text(trans('Delete “%(name)s” from your Dropbox account?'), name = self._proto.name)
        return format_text(ungettext('Delete “%(name)s” and %(num_others)s other web-based file from your Dropbox account?', 'Delete “%(name)s” and %(num_others)s other web-based files from your Dropbox account?', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.is_folder:
            if self._proto.is_single_folder:
                if self._proto.is_windows:
                    if self._proto.num_files == 0:
                        return format_html(trans('This folder has %(num_files)s web-based file inside.<br><br>Web-based file types like .gdoc and .gsheet can’t be moved to your Recycle Bin.'), num_files = self._proto.num_files)
                    return format_html(ungettext('This folder has %(num_files)s web-based file inside.<br><br>Web-based file types like .gdoc and .gsheet can’t be moved to your Recycle Bin.', 'This folder has %(num_files)s web-based files inside.<br><br>Web-based file types like .gdoc and .gsheet can’t be moved to your Recycle Bin.', self._proto.num_files), num_files = self._proto.num_files)
                if None._proto.num_files == 0:
                    return format_html(trans('This folder has %(num_files)s web-based file inside.<br><br>Web-based file types like .gdoc and .gsheet can’t be moved to your Trash.'), num_files = self._proto.num_files)
                return format_html(ungettext('This folder has %(num_files)s web-based file inside.<br><br>Web-based file types like .gdoc and .gsheet can’t be moved to your Trash.', 'This folder has %(num_files)s web-based files inside.<br><br>Web-based file types like .gdoc and .gsheet can’t be moved to your Trash.', self._proto.num_files), num_files = self._proto.num_files)
            if None._proto.is_windows:
                if self._proto.num_files == 0:
                    return format_html(trans('These folders have %(num_files)s web-based file inside.<br><br>Web-based file types like .gdoc and .gsheet can’t be moved to your Recycle Bin.'), num_files = self._proto.num_files)
                return format_html(ungettext('These folders have %(num_files)s web-based file inside.<br><br>Web-based file types like .gdoc and .gsheet can’t be moved to your Recycle Bin.', 'These folders have %(num_files)s web-based files inside.<br><br>Web-based file types like .gdoc and .gsheet can’t be moved to your Recycle Bin.', self._proto.num_files), num_files = self._proto.num_files)
            if None._proto.num_files == 0:
                return format_html(trans('These folders have %(num_files)s web-based file inside.<br><br>Web-based file types like .gdoc and .gsheet can’t be moved to your Trash.'), num_files = self._proto.num_files)
            return format_html(ungettext('These folders have %(num_files)s web-based file inside.<br><br>Web-based file types like .gdoc and .gsheet can’t be moved to your Trash.', 'These folders have %(num_files)s web-based files inside.<br><br>Web-based file types like .gdoc and .gsheet can’t be moved to your Trash.', self._proto.num_files), num_files = self._proto.num_files)
        if None._proto.is_single_folder:
            if self._proto.is_windows:
                if self._proto.num_files == 0:
                    return format_html(trans('Web-based file types like .gdoc and .gsheet can’t be moved to your Recycle Bin.'))
                return format_html(trans('Web-based file types like .gdoc and .gsheet can’t be moved to your Recycle Bin.'))
            if None._proto.num_files == 0:
                return format_html(trans('Web-based file types like .gdoc and .gsheet can’t be moved to your Trash.'))
            return format_html(trans('Web-based file types like .gdoc and .gsheet can’t be moved to your Trash.'))
        if None._proto.is_windows:
            if self._proto.num_files == 0:
                return format_html(trans('Web-based file types like .gdoc and .gsheet can’t be moved to your Recycle Bin.'))
            return format_html(trans('Web-based file types like .gdoc and .gsheet can’t be moved to your Recycle Bin.'))
        if None._proto.num_files == 0:
            return format_html(trans('Web-based file types like .gdoc and .gsheet can’t be moved to your Trash.'))
        return format_html(trans('Web-based file types like .gdoc and .gsheet can’t be moved to your Trash.'))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Delete'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), DELETE_ITEMS),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class CloudDocsMoveToTrash2UI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized CloudDocsMoveToTrash2UI %r', proto)

    
    def get_caption(self):
        if self._proto.is_folder:
            if self._proto.num_others == 0:
                return format_text(trans('Delete “%(name)s” from your Dropbox account?'), name = self._proto.name)
            return format_text(ungettext('Delete “%(name)s” and %(num_others)s other folder from your Dropbox account?', 'Delete “%(name)s” and %(num_others)s other folders from your Dropbox account?', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)
        if None._proto.num_others == 0:
            return format_text(trans('Delete “%(name)s” from your Dropbox account?'), name = self._proto.name)
        return format_text(ungettext('Delete “%(name)s” and %(num_others)s other web-based file from your Dropbox account?', 'Delete “%(name)s” and %(num_others)s other web-based files from your Dropbox account?', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.is_folder:
            if self._proto.is_single_folder:
                if self._proto.is_windows:
                    if self._proto.num_other_files == 0:
                        return format_html(trans('This folder has “%(file_name)s” inside.<br><br>Files that are web-based can’t be moved to your Recycle Bin, but recently deleted files can be restored on dropbox.com.'), file_name = self._proto.file_name)
                    return format_html(ungettext('This folder has “%(file_name)s” and %(num_other_files)s other web-based file inside.<br><br>Files that are web-based can’t be moved to your Recycle Bin, but recently deleted files can be restored on dropbox.com.', 'This folder has “%(file_name)s” and %(num_other_files)s other web-based files inside.<br><br>Files that are web-based can’t be moved to your Recycle Bin, but recently deleted files can be restored on dropbox.com.', self._proto.num_other_files), file_name = self._proto.file_name, num_other_files = self._proto.num_other_files)
                if None._proto.num_other_files == 0:
                    return format_html(trans('This folder has “%(file_name)s” inside.<br><br>Files that are web-based can’t be moved to your Trash, but recently deleted files can be restored on dropbox.com.'), file_name = self._proto.file_name)
                return format_html(ungettext('This folder has “%(file_name)s” and %(num_other_files)s other web-based file inside.<br><br>Files that are web-based can’t be moved to your Trash, but recently deleted files can be restored on dropbox.com.', 'This folder has “%(file_name)s” and %(num_other_files)s other web-based files inside.<br><br>Files that are web-based can’t be moved to your Trash, but recently deleted files can be restored on dropbox.com.', self._proto.num_other_files), file_name = self._proto.file_name, num_other_files = self._proto.num_other_files)
            if None._proto.is_windows:
                if self._proto.num_other_files == 0:
                    return format_html(trans('These folders have “%(file_name)s” inside.<br><br>Files that are web-based can’t be moved to your Recycle Bin, but recently deleted files can be restored on dropbox.com.'), file_name = self._proto.file_name)
                return format_html(ungettext('These folders have “%(file_name)s” and %(num_other_files)s other web-based file inside.<br><br>Files that are web-based can’t be moved to your Recycle Bin, but recently deleted files can be restored on dropbox.com.', 'These folders have “%(file_name)s” and %(num_other_files)s other web-based files inside.<br><br>Files that are web-based can’t be moved to your Recycle Bin, but recently deleted files can be restored on dropbox.com.', self._proto.num_other_files), file_name = self._proto.file_name, num_other_files = self._proto.num_other_files)
            if None._proto.num_other_files == 0:
                return format_html(trans('These folders have “%(file_name)s” inside.<br><br>Files that are web-based can’t be moved to your Trash, but recently deleted files can be restored on dropbox.com.'), file_name = self._proto.file_name)
            return format_html(ungettext('These folders have “%(file_name)s” and %(num_other_files)s other web-based file inside.<br><br>Files that are web-based can’t be moved to your Trash, but recently deleted files can be restored on dropbox.com.', 'These folders have “%(file_name)s” and %(num_other_files)s other web-based files inside.<br><br>Files that are web-based can’t be moved to your Trash, but recently deleted files can be restored on dropbox.com.', self._proto.num_other_files), file_name = self._proto.file_name, num_other_files = self._proto.num_other_files)
        if None._proto.is_single_folder:
            if self._proto.is_windows:
                if self._proto.num_other_files == 0:
                    return format_html(trans('Files that are web-based can’t be moved to your Recycle Bin, but recently deleted files can be restored on dropbox.com.'))
                return format_html(trans('Files that are web-based can’t be moved to your Recycle Bin, but recently deleted files can be restored on dropbox.com.'))
            if None._proto.num_other_files == 0:
                return format_html(trans('Files that are web-based can’t be moved to your Trash, but recently deleted files can be restored on dropbox.com.'))
            return format_html(trans('Files that are web-based can’t be moved to your Trash, but recently deleted files can be restored on dropbox.com.'))
        if None._proto.is_windows:
            if self._proto.num_other_files == 0:
                return format_html(trans('Files that are web-based can’t be moved to your Recycle Bin, but recently deleted files can be restored on dropbox.com.'))
            return format_html(trans('Files that are web-based can’t be moved to your Recycle Bin, but recently deleted files can be restored on dropbox.com.'))
        if None._proto.num_other_files == 0:
            return format_html(trans('Files that are web-based can’t be moved to your Trash, but recently deleted files can be restored on dropbox.com.'))
        return format_html(trans('Files that are web-based can’t be moved to your Trash, but recently deleted files can be restored on dropbox.com.'))

    
    def get_checkbox_message(self):
        return format_text(trans('Don’t ask me this again'))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Delete'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), DELETE_ITEMS),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class CloudDocsMoveToTrashInaccessibleUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized CloudDocsMoveToTrashInaccessibleUI %r', proto)

    
    def get_caption(self):
        if self._proto.num_cloud_files == 0:
            return format_text(trans('A web-based file was deleted'))
        return format_text(ungettext('A web-based file was deleted', 'Some web-based files were deleted', self._proto.num_cloud_files))

    
    def get_message(self):
        return format_text(trans('Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.'))

    
    def get_checkbox_message(self):
        return format_text(trans('Don’t tell me this again'))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class CloudDocsMoveToTrashInaccessible2UI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized CloudDocsMoveToTrashInaccessible2UI %r', proto)

    
    def get_caption(self):
        if self._proto.is_folder:
            if self._proto.num_others == 0:
                return format_text(trans('Deleted “%(name)s” from your Dropbox account'), name = self._proto.name)
            return format_text(ungettext('Deleted “%(name)s” and %(num_others)s other folder from your Dropbox account', 'Deleted “%(name)s” and %(num_others)s other folders from your Dropbox account', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)
        if None._proto.num_others == 0:
            return format_text(trans('Deleted “%(name)s” from your Dropbox account'), name = self._proto.name)
        return format_text(ungettext('Deleted “%(name)s” and %(num_others)s other web-based file from your Dropbox account', 'Deleted “%(name)s” and %(num_others)s other web-based files from your Dropbox account', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.is_folder:
            if self._proto.is_single_folder:
                if self._proto.is_windows:
                    if self._proto.num_other_files == 0:
                        return format_html(trans('This folder has “%(file_name)s” inside.<br><br>Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.'), file_name = self._proto.file_name)
                    return format_html(ungettext('This folder has “%(file_name)s” and %(num_other_files)s other web-based file inside.<br><br>Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.', 'This folder has “%(file_name)s” and %(num_other_files)s other web-based files inside.<br><br>Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.', self._proto.num_other_files), file_name = self._proto.file_name, num_other_files = self._proto.num_other_files)
                if None._proto.num_other_files == 0:
                    return format_html(trans('This folder has “%(file_name)s” inside.<br><br>Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.'), file_name = self._proto.file_name)
                return format_html(ungettext('This folder has “%(file_name)s” and %(num_other_files)s other web-based file inside.<br><br>Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.', 'This folder has “%(file_name)s” and %(num_other_files)s other web-based files inside.<br><br>Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.', self._proto.num_other_files), file_name = self._proto.file_name, num_other_files = self._proto.num_other_files)
            if None._proto.is_windows:
                if self._proto.num_other_files == 0:
                    return format_html(trans('These folders have “%(file_name)s” inside.<br><br>Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.'), file_name = self._proto.file_name)
                return format_html(ungettext('These folders have “%(file_name)s” and %(num_other_files)s other web-based file inside.<br><br>Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.', 'These folders have “%(file_name)s” and %(num_other_files)s other web-based files inside.<br><br>Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.', self._proto.num_other_files), file_name = self._proto.file_name, num_other_files = self._proto.num_other_files)
            if None._proto.num_other_files == 0:
                return format_html(trans('These folders have “%(file_name)s” inside.<br><br>Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.'), file_name = self._proto.file_name)
            return format_html(ungettext('These folders have “%(file_name)s” and %(num_other_files)s other web-based file inside.<br><br>Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.', 'These folders have “%(file_name)s” and %(num_other_files)s other web-based files inside.<br><br>Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.', self._proto.num_other_files), file_name = self._proto.file_name, num_other_files = self._proto.num_other_files)
        if None._proto.is_single_folder:
            if self._proto.is_windows:
                if self._proto.num_other_files == 0:
                    return format_html(trans('Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.'))
                return format_html(trans('Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.'))
            if None._proto.num_other_files == 0:
                return format_html(trans('Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.'))
            return format_html(trans('Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.'))
        if None._proto.is_windows:
            if self._proto.num_other_files == 0:
                return format_html(trans('Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.'))
            return format_html(trans('Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.'))
        if None._proto.num_other_files == 0:
            return format_html(trans('Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.'))
        return format_html(trans('Web-based files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.'))

    
    def get_checkbox_message(self):
        return format_text(trans('Don’t tell me this again'))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class ConfidentialCopyUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized ConfidentialCopyUI %r', proto)

    
    def get_caption(self):
        if self._proto.num_all == 0:
            return format_text(trans('Copied %(num_all)s item to "%(dst_folder_name)s"'), num_all = self._proto.num_all, dst_folder_name = self._proto.dst_folder_name)
        return format_text(ungettext('Copied %(num_all)s item to "%(dst_folder_name)s"', 'Copied %(num_all)s items to "%(dst_folder_name)s"', self._proto.num_all), dst_folder_name = self._proto.dst_folder_name, num_all = self._proto.num_all)

    
    def get_message(self):
        if self._proto.num_all == 0:
            return format_html(trans("The item that you copied can now be accessed by everyone who can access <b>%(dst_folder_name)s</b>. If you didn't mean to copy it here, delete the item."), dst_folder_name = self._proto.dst_folder_name)
        return format_html(ungettext("The item that you copied can now be accessed by everyone who can access <b>%(dst_folder_name)s</b>. If you didn't mean to copy it here, delete the item.", "The items that you copied can now be accessed by everyone who can access <b>%(dst_folder_name)s</b>. If you didn't mean to copy them here, delete the items.", self._proto.num_all), dst_folder_name = self._proto.dst_folder_name)

    
    def get_checkbox_message(self):
        return format_text(trans("Don't show me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('confidential_copy')), button_action = LEARN_MORE_AND_ALLOW))]



class ConfidentialMoveUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized ConfidentialMoveUI %r', proto)

    
    def get_caption(self):
        if self._proto.num == 0:
            return format_text(trans('Share "%(src_name)s" with everyone who can access "%(dst_folder_name)s"?'), src_name = self._proto.src_name, dst_folder_name = self._proto.dst_folder_name)
        return format_text(ungettext('Share "%(src_name)s" and %(num)s other item with everyone who can access "%(dst_folder_name)s"?', 'Share "%(src_name)s" and %(num)s other items with everyone who can access "%(dst_folder_name)s"?', self._proto.num), dst_folder_name = self._proto.dst_folder_name, num = self._proto.num, src_name = self._proto.src_name)

    
    def get_message(self):
        if self._proto.num_all == 0:
            return format_html(trans('If you move this item here, it will be shared with everyone who can access <b>%(dst_folder_name)s</b>.'), dst_folder_name = self._proto.dst_folder_name)
        return format_html(ungettext('If you move this item here, it will be shared with everyone who can access <b>%(dst_folder_name)s</b>.', 'If you move these items here, they will be shared with everyone who can access <b>%(dst_folder_name)s</b>.', self._proto.num_all), dst_folder_name = self._proto.dst_folder_name)

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Share'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class DeviceFolderContentMoveToTrashUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized DeviceFolderContentMoveToTrashUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Delete from "%(device_folder_name)s" in both Dropbox and your computer?'), device_folder_name = self._proto.device_folder_name)

    
    def get_message(self):
        if self._proto.num_others == 0:
            return format_html(trans('<b>%(first_filename)s</b> will be deleted from your Dropbox account and all devices.<br /><a href="%(help_url)s">More info on deleting item</a>'), first_filename = self._proto.first_filename, help_url = dropbox_url_info.construct_full_url('help/installs-integrations/sync-uploads/automatic-computer-backup-faqs', [
                'oqa=dfsw']))
        return format_html(trans('<b>%(first_filename)s</b> and %(num_others)s other items will be deleted from your Dropbox account and all devices.<br /><a href="%(help_url)s">More info on deleting items</a>'), first_filename = self._proto.first_filename, num_others = self._proto.num_others, help_url = dropbox_url_info.construct_full_url('help/installs-integrations/sync-uploads/automatic-computer-backup-faqs', [
            'oqa=dfsw']))

    
    def get_checkbox_message(self):
        return format_text(trans('Don’t ask me this again'))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Delete everywhere'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class DeviceFolderContentMoveToTrashInaccessibleUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized DeviceFolderContentMoveToTrashInaccessibleUI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('Deleted item from "%(device_folder_name)s" in both Dropbox and your computer'), device_folder_name = self._proto.device_folder_name)
        return format_text(trans('Deleted items from "%(device_folder_name)s" in both Dropbox and your computer'), device_folder_name = self._proto.device_folder_name)

    
    def get_message(self):
        if self._proto.num_others == 0:
            return format_html(trans('If you change your mind, you can move <b>%(first_filename)s</b> out of your Trash or restore recently deleted items on dropbox.com<br /><a href="%(help_url)s">More info on deleting item</a>'), first_filename = self._proto.first_filename, help_url = dropbox_url_info.construct_full_url('help/installs-integrations/sync-uploads/automatic-computer-backup-faqs', [
                'oqa=dfsw']))
        return format_html(trans('If you change your mind, you can move <b>%(first_filename)s</b> and %(num_others)s other items out of your Trash or restore recently deleted items on dropbox.com<br /><a href="%(help_url)s">More info on deleting items</a>'), first_filename = self._proto.first_filename, num_others = self._proto.num_others, help_url = dropbox_url_info.construct_full_url('help/installs-integrations/sync-uploads/automatic-computer-backup-faqs', [
            'oqa=dfsw']))

    
    def get_checkbox_message(self):
        return format_text(trans("Don't tell me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Restore on web'))

        
        def get_button0_url():
            return dropbox_url_info.construct_full_url('deleted_files/')

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = get_button0_url()), button_action = LEARN_MORE_AND_ALLOW))]



class DeviceFolderMoveToTrashUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized DeviceFolderMoveToTrashUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Can’t remove while still backing up files'))

    
    def get_message(self):
        return format_text(trans('To stop backing up %(folder_name)s, go to your Dropbox app preferences.'), folder_name = self._proto.folder_name)

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class DeviceFolderMoveToTrashInaccessibleUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized DeviceFolderMoveToTrashInaccessibleUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Can’t remove while still backing up files'))

    
    def get_message(self):
        return format_text(trans('To stop backing up %(folder_name)s, go to your Dropbox app preferences.'), folder_name = self._proto.folder_name)

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class DeviceFolderSuggestSelsyncUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized DeviceFolderSuggestSelsyncUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Can’t remove backup'))

    
    def get_message(self):
        return format_text(trans('If you want to hide %(folder_name)s, use selective sync in your Dropbox app preferences.'), folder_name = self._proto.folder_name)

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class DeviceFolderSuggestSelsyncTrashInaccessibleUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized DeviceFolderSuggestSelsyncTrashInaccessibleUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Can’t remove backup'))

    
    def get_message(self):
        return format_text(trans('If you want to hide %(folder_name)s, use selective sync in your Dropbox app preferences.'), folder_name = self._proto.folder_name)

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class FileIsMovedFromUnencryptedToEncryptedFolderUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized FileIsMovedFromUnencryptedToEncryptedFolderUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Can’t move to encrypted team folder'))

    
    def get_message(self):
        return format_html(trans('Instead, drag this file onto your desktop to move it out of Dropbox. Then try uploading it to the encrypted team folder.'))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Got it'))

        return [
            (get_button0(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class FileIsMovedOutOfEncryptedFolderUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized FileIsMovedOutOfEncryptedFolderUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Can’t move files out of encrypted team folders'))

    
    def get_message(self):
        return format_html(trans('This is currently not supported. Instead, copy the files and paste them where you need to.'))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Close'))

        return [
            (get_button0(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class MoveSfToTfNonOwnerConfirmationUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized MoveSfToTfNonOwnerConfirmationUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_source_account_cdm:
            if self._proto.is_source_shared_folder:
                if self._proto.num_others == 0:
                    return format_text(trans('Move the "%(src_name)s" shared folder to the %(team_name)s team space?'), src_name = self._proto.src_name, team_name = self._proto.team_name)
                return format_text(ungettext('Move the "%(src_name)s" shared folder and %(num_others)s other item to the %(team_name)s team space?', 'Move the "%(src_name)s" shared folder and %(num_others)s other items to the %(team_name)s team space?', self._proto.num_others), num_others = self._proto.num_others, src_name = self._proto.src_name, team_name = self._proto.team_name)
            if None._proto.num_others == 0:
                return format_text(trans('Move the "%(src_name)s" folder to the %(team_name)s team space?'), src_name = self._proto.src_name, team_name = self._proto.team_name)
            return format_text(ungettext('Move the "%(src_name)s" folder and %(num_others)s other item to the %(team_name)s team space?', 'Move the "%(src_name)s" folder and %(num_others)s other items to the %(team_name)s team space?', self._proto.num_others), num_others = self._proto.num_others, src_name = self._proto.src_name, team_name = self._proto.team_name)
        if None._proto.is_source_shared_folder:
            if self._proto.num_others == 0:
                return format_text(trans('Move the "%(src_name)s" shared folder to a team folder?'), src_name = self._proto.src_name)
            return format_text(ungettext('Move the "%(src_name)s" shared folder and %(num_others)s other item to a team folder?', 'Move the "%(src_name)s" shared folder and %(num_others)s other items to a team folder?', self._proto.num_others), num_others = self._proto.num_others, src_name = self._proto.src_name)
        if None._proto.num_others == 0:
            return format_text(trans('Move the "%(src_name)s" folder to a team folder?'), src_name = self._proto.src_name)
        return format_text(ungettext('Move the "%(src_name)s" folder and %(num_others)s other item to a team folder?', 'Move the "%(src_name)s" folder and %(num_others)s other items to a team folder?', self._proto.num_others), num_others = self._proto.num_others, src_name = self._proto.src_name)

    
    def get_message(self):
        if self._proto.is_dst_tsd_top_level:
            if self._proto.is_source_shared_folder:
                if self._proto.num_others == 0:
                    return format_html(trans("You're not the owner of <b>%(src_name)s</b>. If you move this folder, everyone at %(team_name)s will have access."), src_name = self._proto.src_name, team_name = self._proto.team_name)
                return format_html(trans("You're not the owner of some of these items. If you move these items, everyone at %(team_name)s will have access."), team_name = self._proto.team_name)
            if None._proto.num_others == 0:
                return format_html(trans("You're not the owner of some subfolders in <b>%(src_name)s</b>. If you move this folder, everyone at %(team_name)s will have access."), src_name = self._proto.src_name, team_name = self._proto.team_name)
            return format_html(trans("You're not the owner of some subfolders in some of these items. If you move these items, everyone at %(team_name)s will have access."), team_name = self._proto.team_name)
        if None._proto.is_source_shared_folder:
            if self._proto.num_others == 0:
                return format_html(trans("You're not the owner of <b>%(src_name)s</b>. If you move this folder, members will be able to find it in <b>%(dst_folder_name)s</b>."), src_name = self._proto.src_name, dst_folder_name = self._proto.dst_folder_name)
            return format_html(trans("You're not the owner of some of these items. If you move these items, members will be able to find it in <b>%(dst_folder_name)s</b>."), dst_folder_name = self._proto.dst_folder_name)
        if None._proto.num_others == 0:
            return format_html(trans("You're not the owner of some subfolders in <b>%(src_name)s</b>. If you move this folder, members will be able to find it in <b>%(dst_folder_name)s</b>."), src_name = self._proto.src_name, dst_folder_name = self._proto.dst_folder_name)
        return format_html(trans("You're not the owner of some subfolders in some of these items. If you move these items, members will be able to find it in <b>%(dst_folder_name)s</b>."), dst_folder_name = self._proto.dst_folder_name)

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Move anyway'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class PerNodeMetadataDeletableEntrypointUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized PerNodeMetadataDeletableEntrypointUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Remove %(filename)s from your Dropbox?'), filename = self._proto.filename)

    
    def get_message(self):
        return format_text(trans('If you want to set up %(filename)s later, you can find it in your Dropbox app preferences or settings.'), filename = self._proto.filename)

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Cancel'))

        
        def get_button1():
            return format_text(trans('Delete anyway'))

        return [
            (get_button0(), REVERT),
            (get_button1(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class PerNodeMetadataDeletableEntrypointTrashInaccessibleUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized PerNodeMetadataDeletableEntrypointTrashInaccessibleUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Remove %(filename)s from your Dropbox?'), filename = self._proto.filename)

    
    def get_message(self):
        return format_text(trans('If you want to set up %(filename)s later, you can find it in your Dropbox app preferences or settings.'), filename = self._proto.filename)

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class PerNodeMetadataMoveUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized PerNodeMetadataMoveUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Can’t move %(filename)s'), filename = self._proto.filename)

    
    def get_message(self):
        return format_text(trans('This is a Dropbox feature, so you can’t move it.'))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class PerNodeMetadataMoveToTrashUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized PerNodeMetadataMoveToTrashUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Can’t delete %(filename)s'), filename = self._proto.filename)

    
    def get_message(self):
        return format_text(trans('This is a Dropbox feature, so you can’t delete it.'))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class PerNodeMetadataMoveToTrashInaccessibleUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized PerNodeMetadataMoveToTrashInaccessibleUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Can’t delete %(filename)s'), filename = self._proto.filename)

    
    def get_message(self):
        return format_text(trans('This is a Dropbox feature, so you can’t delete it.'))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class PerNodeMetadataRenameUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized PerNodeMetadataRenameUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Can’t rename %(filename)s'), filename = self._proto.filename)

    
    def get_message(self):
        return format_text(trans('This is a Dropbox feature, so you can’t rename it.'))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class Restorations1UI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized Restorations1UI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('Delete "%(name)s" from your Dropbox account and all devices?'), name = self._proto.name)
        return format_text(ungettext('Delete "%(name)s" and %(num_others)s other item from your Dropbox account and all devices?', 'Delete "%(name)s" and %(num_others)s other items from your Dropbox account and all devices?', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.has_smart_sync:
            if self._proto.num_others == 0:
                return format_html(trans('If you just want to save hard drive space on this computer, cancel and make it <a href="%(url)s">online-only</a>.'), url = dropbox_url_info.help_url('smart_sync'))
            return format_html(trans('If you just want to save hard drive space on this computer, cancel and make them <a href="%(url)s">online-only</a>.'), url = dropbox_url_info.help_url('smart_sync'))
        if None._proto.num_others == 0:
            return format_html(trans('If you just want to save hard drive space, <a href="%(help_url)s">see sync options</a>.'), help_url = dropbox_url_info.construct_full_url('help/syncing-uploads/selective-sync-overview', [
                'oqa=dfsw']))
        return format_html(trans('If you just want to save hard drive space, <a href="%(help_url)s">see sync options</a>.'), help_url = dropbox_url_info.construct_full_url('help/syncing-uploads/selective-sync-overview', [
            'oqa=dfsw']))

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Delete everywhere'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class Restorations1And3InaccessibleUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized Restorations1And3InaccessibleUI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('You deleted "%(name)s" from your Dropbox account and all devices'), name = self._proto.name)
        return format_text(ungettext('You deleted "%(name)s" and %(num_others)s other item from your Dropbox account and all devices', 'You deleted "%(name)s" and %(num_others)s other items from your Dropbox account and all devices', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.num_others == 0:
            return format_html(trans('If you change your mind, you can move it out of your Trash or restore recently deleted files on dropbox.com.'))
        return format_html(trans('If you change your mind, you can move them out of your Trash or restore recently deleted files on dropbox.com.'))

    
    def get_checkbox_message(self):
        return format_text(trans("Don't tell me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Restore on web'))

        
        def get_button0_url():
            return dropbox_url_info.construct_full_url('deleted_files/')

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = get_button0_url()), button_action = LEARN_MORE_AND_ALLOW))]



class Restorations2UI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized Restorations2UI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('Remove "%(name)s" from your Dropbox account and all devices?'), name = self._proto.name)
        return format_text(ungettext('Remove "%(name)s" and %(num_others)s other item from your Dropbox account and all devices?', 'Remove "%(name)s" and %(num_others)s other items from your Dropbox account and all devices?', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.is_file:
            if self._proto.num_others == 0:
                return format_html(trans("If you move this file to <b>%(dest)s</b>, it won't be available in Dropbox or on any devices."), dest = self._proto.dest)
            return format_html(trans("If you move these items to <b>%(dest)s</b>, they won't be available in Dropbox or on any devices."), dest = self._proto.dest)
        if None._proto.num_others == 0:
            return format_html(trans("If you move this folder to <b>%(dest)s</b>, it won't be available in Dropbox or on any devices."), dest = self._proto.dest)
        return format_html(trans("If you move these items to <b>%(dest)s</b>, they won't be available in Dropbox or on any devices."), dest = self._proto.dest)

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Move out of Dropbox'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class Restorations3UI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized Restorations3UI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('"%(name)s" will be deleted from your account and devices, but other members will still have access'), name = self._proto.name)
        return format_text(ungettext('"%(name)s" and %(num_others)s other shared folder will be deleted from your account and devices, but other members will still have access', '"%(name)s" and %(num_others)s other shared folders will be deleted from your account and devices, but other members will still have access', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.has_smart_sync:
            if self._proto.num_others == 0:
                return format_html(trans('If you just want to save hard drive space on this computer, cancel and make the folder <a href="%(url)s">online-only</a>.'), url = dropbox_url_info.help_url('smart_sync'))
            return format_html(trans('If you just want to save hard drive space on this computer, cancel and make them <a href="%(url)s">online-only</a>.'), url = dropbox_url_info.help_url('smart_sync'))
        if None._proto.num_others == 0:
            return format_html(trans('To remove this folder from just this computer, cancel and use <a href="%(help_url)s">selective sync</a>.'), help_url = dropbox_url_info.construct_full_url('help/syncing-uploads/selective-sync-overview', [
                'oqa=dfsw']))
        return format_html(trans('To remove these folders from just this computer, cancel and use <a href="%(help_url)s">selective sync</a>.'), help_url = dropbox_url_info.construct_full_url('help/syncing-uploads/selective-sync-overview', [
            'oqa=dfsw']))

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Delete anyway'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        pass
    # WARNING: Decompyle incomplete



class Restorations4UI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized Restorations4UI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('"%(name)s" will be removed from your Dropbox account and devices, but everyone else will still have access'), name = self._proto.name)
        return format_text(ungettext('"%(name)s" and %(num_others)s other shared folder will be removed from your Dropbox account and devices, but everyone else will still have access', '"%(name)s" and %(num_others)s other shared folders will be removed from your Dropbox account and devices, but everyone else will still have access', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.num_others == 0:
            return format_html(trans('If you move this folder to <b>%(dest)s</b>, any changes you make will no longer be shared with anyone else.'), dest = self._proto.dest)
        return format_html(trans('If you move these folders to <b>%(dest)s</b>, any changes you make will no longer be shared with anyone else.'), dest = self._proto.dest)

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Move anyway'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        pass
    # WARNING: Decompyle incomplete



class Restorations5UI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized Restorations5UI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('Delete "%(name)s" from everyone\'s account and all devices?'), name = self._proto.name)
        return format_text(ungettext('Delete "%(name)s" and %(num_others)s other item from everyone\'s account and all devices?', 'Delete "%(name)s" and %(num_others)s other items from everyone\'s account and all devices?', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.has_smart_sync:
            if self._proto.num_others == 0:
                return format_html(trans('If you just want to save hard drive space on this computer, cancel and make it <a href="%(url)s">online-only</a>.'), url = dropbox_url_info.help_url('smart_sync'))
            return format_html(trans('If you just want to save hard drive space on this computer, cancel and make them <a href="%(url)s">online-only</a>.'), url = dropbox_url_info.help_url('smart_sync'))
        if None._proto.num_others == 0:
            return format_html(trans('If you just want to save hard drive space, <a href="%(help_url)s">see sync options</a>.'), help_url = dropbox_url_info.construct_full_url('help/syncing-uploads/selective-sync-overview', [
                'oqa=dfsw']))
        return format_html(trans('If you just want to save hard drive space, <a href="%(help_url)s">see sync options</a>.'), help_url = dropbox_url_info.construct_full_url('help/syncing-uploads/selective-sync-overview', [
            'oqa=dfsw']))

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Delete for everyone'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class Restorations5InaccessibleUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized Restorations5InaccessibleUI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('You deleted "%(name)s" from everyone\'s account and all devices.'), name = self._proto.name)
        return format_text(ungettext('You deleted "%(name)s" and %(num_others)s other item from everyone\'s account and all devices.', 'You deleted "%(name)s" and %(num_others)s other items from everyone\'s account and all devices.', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.num_others == 0:
            return format_html(trans('If you change your mind, you can move it out of your Trash or restore recently deleted files on dropbox.com.'))
        return format_html(trans('If you change your mind, you can move them out of your Trash or restore recently deleted files on dropbox.com.'))

    
    def get_checkbox_message(self):
        return format_text(trans("Don't tell me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Restore on web'))

        
        def get_button0_url():
            return dropbox_url_info.construct_full_url('deleted_files/')

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = get_button0_url()), button_action = LEARN_MORE_AND_ALLOW))]



class Restorations6aUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized Restorations6aUI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('Move "%(name)s" out of the shared folder "%(src_parent)s"?'), name = self._proto.name, src_parent = self._proto.src_parent)
        return format_text(ungettext('Move "%(name)s" and %(num_others)s other item out of the shared folder "%(src_parent)s"?', 'Move "%(name)s" and %(num_others)s other items out of the shared folder "%(src_parent)s"?', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others, src_parent = self._proto.src_parent)

    
    def get_message(self):
        if self._proto.is_file:
            if self._proto.num_others == 0:
                return format_html(trans('Moving this file to <b>%(dest)s</b> will remove it for members of <b>%(src_parent)s</b>.'), dest = self._proto.dest, src_parent = self._proto.src_parent)
            return format_html(trans('Moving these items to <b>%(dest)s</b> will remove them for members of <b>%(src_parent)s</b>.'), dest = self._proto.dest, src_parent = self._proto.src_parent)
        if None._proto.num_others == 0:
            return format_html(trans('Moving this folder to <b>%(dest)s</b> will remove it for members of <b>%(src_parent)s</b>.'), dest = self._proto.dest, src_parent = self._proto.src_parent)
        return format_html(trans('Moving these items to <b>%(dest)s</b> will remove them for members of <b>%(src_parent)s</b>.'), dest = self._proto.dest, src_parent = self._proto.src_parent)

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Move anyway'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class Restorations6aExampleUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized Restorations6aExampleUI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('Move "%(name)s" out of the shared folder "%(src_parent)s"?'), name = self._proto.name, src_parent = self._proto.src_parent)
        return format_text(ungettext('Move "%(name)s" and %(num_others)s other item out of the shared folder "%(src_parent)s"?', 'Move "%(name)s" and %(num_others)s other items out of the shared folder "%(src_parent)s"?', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others, src_parent = self._proto.src_parent)

    
    def get_message(self):
        if self._proto.is_file:
            if self._proto.num_others == 0:
                return format_html(trans('Moving this file to <b>%(dest)s</b> will remove it for members of <b>%(src_parent)s</b>.<a href="%(help_url)s"> Open help page.</a>'), dest = self._proto.dest, src_parent = self._proto.src_parent, help_url = dropbox_url_info.help_url('fsw_shared_folder_nest'))
            return format_html(trans('Moving these items to <b>%(dest)s</b> will remove them for members of <b>%(src_parent)s</b>.<a href="%(help_url)s"> Open help page.</a>'), dest = self._proto.dest, src_parent = self._proto.src_parent, help_url = dropbox_url_info.help_url('fsw_shared_folder_nest'))
        if None._proto.num_others == 0:
            return format_html(trans('Moving this folder to <b>%(dest)s</b> will remove it for members of <b>%(src_parent)s</b>.<a href="%(help_url)s"> Open help page.</a>'), dest = self._proto.dest, src_parent = self._proto.src_parent, help_url = dropbox_url_info.help_url('fsw_shared_folder_nest'))
        return format_html(trans('Moving these items to <b>%(dest)s</b> will remove them for members of <b>%(src_parent)s</b>.<a href="%(help_url)s"> Open help page.</a>'), dest = self._proto.dest, src_parent = self._proto.src_parent, help_url = dropbox_url_info.help_url('fsw_shared_folder_nest'))

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Move anyway'))

        
        def get_button1():
            return format_text(trans('Move to member folder'))

        
        def get_button2():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), MOVE_TO_TMF),
            (get_button2(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Share'))

        return [
            (get_button0(), AuxFSWButton(share = AuxButtonShare(location_rr_paths = fsw_dialog.restorations_6a_example.share_button_rr_paths), button_action = SHARE_AND_REVERT))]



class Restorations6bUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized Restorations6bUI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('Remove "%(name)s" from everyone\'s Dropbox account and all devices?'), name = self._proto.name)
        return format_text(ungettext('Remove "%(name)s" and %(num_others)s other item from everyone\'s Dropbox account and all devices?', 'Remove "%(name)s" and %(num_others)s other items from everyone\'s Dropbox account and all devices?', self._proto.num_others), name = self._proto.name, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.is_file:
            if self._proto.num_others == 0:
                return format_html(trans("If you move this file to <b>%(dest)s</b>, it will no longer be shared with anyone, and it won't be available in Dropbox or on any devices."), dest = self._proto.dest)
            return format_html(trans("If you move these items to <b>%(dest)s</b>, they will no longer be shared with anyone, and the items won't be available in Dropbox or on any devices."), dest = self._proto.dest)
        if None._proto.num_others == 0:
            return format_html(trans("If you move this folder to <b>%(dest)s</b>, it will no longer be shared with anyone, and it won't be available in Dropbox or on any devices."), dest = self._proto.dest)
        return format_html(trans("If you move these items to <b>%(dest)s</b>, they will no longer be shared with anyone, and the items won't be available in Dropbox or on any devices."), dest = self._proto.dest)

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Move out of Dropbox'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class SharedFolderNestingUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized SharedFolderNestingUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Can\'t move "%(source_path)s" to "%(dest_path)s"'), source_path = self._proto.source_path, dest_path = self._proto.dest_path)

    
    def get_message(self):
        if self._proto.is_team:
            return format_text(trans("Unless you're working inside a team folder, shared folders can't be moved to other shared folders."))
        return format_text(trans("Shared folders can't be moved to other shared folders."))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn more'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('fsw_shared_folder_nest')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class SharedFolderNestingImplicitShareOnMoveUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized SharedFolderNestingImplicitShareOnMoveUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_rename:
            return format_text(trans('Rename and allow others to access?'))
        return format_text(trans('Move and allow others to access?'))

    
    def get_message(self):
        if self._proto.num == 0:
            return format_text(trans('Everyone with access to "%(dest_path)s" will get access to this item.'), dest_path = self._proto.dest_path)
        return format_text(ungettext('Everyone with access to "%(dest_path)s" will get access to this item.', 'Everyone with access to "%(dest_path)s" will get access to these items.', self._proto.num), dest_path = self._proto.dest_path)

    
    def get_checkbox_message(self):
        return format_text(trans('Don’t ask me this again'))

    
    def get_buttons(self):
        pass
    # WARNING: Decompyle incomplete

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class SharedFolderNestingOwnershipStealUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized SharedFolderNestingOwnershipStealUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_source_shared_folder:
            return format_text(trans("Couldn't move folder"))
        return format_text(trans('Can\'t move to "%(dest_path)s"'), dest_path = self._proto.dest_path)

    
    def get_message(self):
        if self._proto.is_source_shared_folder:
            return format_text(trans('To make this move, try contacting the owner of "%(source_path)s."'), source_path = self._proto.source_path)
        return format_text(trans('That folder has a different owner than some of the items in "%(source_path)s."'), source_path = self._proto.source_path)

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn more'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('fsw_shared_folder_nest')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class SharedFolderNestingOwnershipSurrenderUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized SharedFolderNestingOwnershipSurrenderUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_source_shared_folder:
            if self._proto.owned_shared_folder_count == 0:
                return format_text(trans('Move and lose ownership of folder?'))
            return format_text(trans('Move and lose ownership of folder?'))
        if None._proto.owned_shared_folder_count == 0:
            return format_text(trans('Move and lose ownership of %(owned_shared_folder_count)s subfolder?'), owned_shared_folder_count = self._proto.owned_shared_folder_count)
        return format_text(ungettext('Move and lose ownership of %(owned_shared_folder_count)s subfolder?', 'Move and lose ownership of %(owned_shared_folder_count)s subfolders?', self._proto.owned_shared_folder_count), owned_shared_folder_count = self._proto.owned_shared_folder_count)

    
    def get_message(self):
        if self._proto.is_source_shared_folder:
            return format_text(trans('Ownership of this folder will transfer to the owner of "%(dest_path)s."'), dest_path = self._proto.dest_path)
        return format_text(trans('Ownership of any subfolders will transfer to the owner of "%(dest_path)s."'), dest_path = self._proto.dest_path)

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Move anyway'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class SmartSyncMoveToTrashUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized SmartSyncMoveToTrashUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_any_folder:
            if self._proto.is_any_in_shared_folder:
                if self._proto.is_windows:
                    if self._proto.num_others == 0:
                        return format_text(trans('Delete "%(filename)s" for everyone?'), filename = self._proto.filename)
                    return format_text(ungettext('Delete "%(filename)s" and %(num_others)s other item for everyone?', 'Delete "%(filename)s" and %(num_others)s other items for everyone?', self._proto.num_others), filename = self._proto.filename, num_others = self._proto.num_others)
                if None._proto.num_others == 0:
                    return format_text(trans('Delete "%(filename)s" for everyone?'), filename = self._proto.filename)
                return format_text(ungettext('Delete "%(filename)s" and %(num_others)s other item for everyone?', 'Delete "%(filename)s" and %(num_others)s other items for everyone?', self._proto.num_others), filename = self._proto.filename, num_others = self._proto.num_others)
            if None._proto.is_windows:
                if self._proto.num_others == 0:
                    return format_text(trans('Delete "%(filename)s"?'), filename = self._proto.filename)
                return format_text(ungettext('Delete "%(filename)s" and %(num_others)s other item?', 'Delete "%(filename)s" and %(num_others)s other items?', self._proto.num_others), filename = self._proto.filename, num_others = self._proto.num_others)
            if None._proto.num_others == 0:
                return format_text(trans('Delete "%(filename)s"?'), filename = self._proto.filename)
            return format_text(ungettext('Delete "%(filename)s" and %(num_others)s other item?', 'Delete "%(filename)s" and %(num_others)s other items?', self._proto.num_others), filename = self._proto.filename, num_others = self._proto.num_others)
        if None._proto.is_any_in_shared_folder:
            if self._proto.is_windows:
                if self._proto.num_others == 0:
                    return format_text(trans('Delete "%(filename)s" for everyone?'), filename = self._proto.filename)
                return format_text(ungettext('Delete "%(filename)s" and %(num_others)s other file for everyone?', 'Delete "%(filename)s" and %(num_others)s other files for everyone?', self._proto.num_others), filename = self._proto.filename, num_others = self._proto.num_others)
            if None._proto.num_others == 0:
                return format_text(trans('Delete "%(filename)s" for everyone?'), filename = self._proto.filename)
            return format_text(ungettext('Delete "%(filename)s" and %(num_others)s other file for everyone?', 'Delete "%(filename)s" and %(num_others)s other files for everyone?', self._proto.num_others), filename = self._proto.filename, num_others = self._proto.num_others)
        if None._proto.is_windows:
            if self._proto.num_others == 0:
                return format_text(trans('Delete "%(filename)s"?'), filename = self._proto.filename)
            return format_text(ungettext('Delete "%(filename)s" and %(num_others)s other file?', 'Delete "%(filename)s" and %(num_others)s other files?', self._proto.num_others), filename = self._proto.filename, num_others = self._proto.num_others)
        if None._proto.num_others == 0:
            return format_text(trans('Delete "%(filename)s"?'), filename = self._proto.filename)
        return format_text(ungettext('Delete "%(filename)s" and %(num_others)s other file?', 'Delete "%(filename)s" and %(num_others)s other files?', self._proto.num_others), filename = self._proto.filename, num_others = self._proto.num_others)

    
    def get_message(self):
        if self._proto.is_any_folder:
            if self._proto.is_any_in_shared_folder:
                if self._proto.is_windows:
                    if self._proto.num_others == 0:
                        return format_html(trans("This folder will be deleted from your and everyone else's Dropbox account. <br/><br/>Because it has online-only files, it won't be moved to your Recycle Bin, but recently deleted files can be restored on dropbox.com"))
                    return format_html(trans("These items will be deleted from your and everyone else's Dropbox account. <br/><br/>Online-only items won't be moved to your Recycle Bin, but recently deleted items can be restored on dropbox.com."))
                if None._proto.num_others == 0:
                    return format_html(trans("This folder will be deleted from your and everyone else's Dropbox account. <br/><br/>Because it has online-only files, it won't be moved to your Trash, but recently deleted files can be restored on dropbox.com"))
                return format_html(trans("These items will be deleted from your and everyone else's Dropbox account. <br/><br/>Online-only items won't be moved to your Trash, but recently deleted items can be restored on dropbox.com."))
            if None._proto.is_windows:
                if self._proto.num_others == 0:
                    return format_html(trans("This folder will be deleted from your Dropbox account. <br/><br/>Because it has online-only files, it won't be moved to your Recycle Bin, but recently deleted files can be restored on dropbox.com"))
                return format_html(trans("These items will be deleted from your Dropbox account. <br/><br/>Online-only items won't be moved to your Recycle Bin, but recently deleted items can be restored on dropbox.com."))
            if None._proto.num_others == 0:
                return format_html(trans("This folder will be deleted from your Dropbox account. <br/><br/>Because it has online-only files, it won't be moved to your Trash, but recently deleted files can be restored on dropbox.com"))
            return format_html(trans("These items will be deleted from your Dropbox account. <br/><br/>Online-only items won't be moved to your Trash, but recently deleted items can be restored on dropbox.com."))
        if None._proto.is_any_in_shared_folder:
            if self._proto.is_windows:
                if self._proto.num_others == 0:
                    return format_html(trans("This file will be deleted from your and everyone else's Dropbox account. <br/><br/>Because it's online-only, it won't be moved to your Recycle Bin, but recently deleted files can be restored on dropbox.com"))
                return format_html(trans("These files will be deleted from your and everyone else's Dropbox account. <br/><br/>Online-only items won't be moved to your Recycle Bin, but recently deleted items can be restored on dropbox.com."))
            if None._proto.num_others == 0:
                return format_html(trans("This file will be deleted from your and everyone else's Dropbox account. <br/><br/>Because it's online-only, it won't be moved to your Trash, but recently deleted files can be restored on dropbox.com"))
            return format_html(trans("These files will be deleted from your and everyone else's Dropbox account. <br/><br/>Online-only items won't be moved to your Trash, but recently deleted items can be restored on dropbox.com."))
        if None._proto.is_windows:
            if self._proto.num_others == 0:
                return format_html(trans("This file will be deleted from your Dropbox account. <br/><br/>Because it's online-only, it won't be moved to your Recycle Bin, but recently deleted files can be restored on dropbox.com"))
            return format_html(trans("These files will be deleted from your Dropbox account. <br/><br/>Online-only items won't be moved to your Recycle Bin, but recently deleted items can be restored on dropbox.com."))
        if None._proto.num_others == 0:
            return format_html(trans("This file will be deleted from your Dropbox account. <br/><br/>Because it's online-only, it won't be moved to your Trash, but recently deleted files can be restored on dropbox.com"))
        return format_html(trans("These files will be deleted from your Dropbox account. <br/><br/>Online-only items won't be moved to your Trash, but recently deleted items can be restored on dropbox.com."))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        pass
    # WARNING: Decompyle incomplete

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class SmartSyncMoveToTrashInaccessibleUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized SmartSyncMoveToTrashInaccessibleUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_any_in_shared_folder:
            if self._proto.involved_placeholder_count == 0:
                return format_text(trans('An online-only file was deleted for everyone'))
            return format_text(ungettext('An online-only file was deleted for everyone', 'Some online-only files were deleted for everyone', self._proto.involved_placeholder_count))
        if None._proto.involved_placeholder_count == 0:
            return format_text(trans('An online-only file was deleted'))
        return format_text(ungettext('An online-only file was deleted', 'Some online-only files were deleted', self._proto.involved_placeholder_count))

    
    def get_message(self):
        if self._proto.is_any_in_shared_folder:
            if self._proto.involved_placeholder_count == 0:
                return format_html(trans(" This file was deleted from your and everyone else's Dropbox account. <br/><br/>Online-only files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead."))
            return format_html(ungettext(" This file was deleted from your and everyone else's Dropbox account. <br/><br/>Online-only files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.", "These files were deleted from your and everyone else's Dropbox account. <br/><br/>Online-only files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.", self._proto.involved_placeholder_count))
        if None._proto.involved_placeholder_count == 0:
            return format_html(trans('Online-only files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.'))
        return format_html(trans('Online-only files may not work if you restore them from your Trash later, so we recommend restoring them from dropbox.com instead.'))

    
    def get_checkbox_message(self):
        return format_text(trans("Don't tell me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class TeamFolderMoveUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized TeamFolderMoveUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_rename:
            return format_text(trans('Can\'t rename "%(source_path)s"'), source_path = self._proto.source_path)
        return format_text(trans('Can\'t move "%(source_path)s" to "%(dest_path)s"'), source_path = self._proto.source_path, dest_path = self._proto.dest_path)

    
    def get_message(self):
        if self._proto.is_rename:
            if self._proto.is_admin:
                return format_html(trans('To rename a team folder, go to the Content page in the Admin Console.'))
            return format_html(trans('Only Dropbox admins can rename team folders.'))
        if None._proto.is_admin:
            return format_html(trans("Team folders can't be moved."))
        return format_html(trans("Team folders can't be moved."))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        pass
    # WARNING: Decompyle incomplete



class TeamFolderMoveToTrashUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized TeamFolderMoveToTrashUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Can\'t delete "%(source_path)s"'), source_path = self._proto.source_path)

    
    def get_message(self):
        if self._proto.is_online_only:
            if self._proto.is_admin:
                return format_html(trans('Team folders can only be deleted using the Content page in the Admin Console.<br/><br/>To stop it from syncing with this computer, use selective sync.'))
            return format_html(trans('Only Dropbox admins can delete Team folders.<br/><br/>To stop it from syncing with this computer, use selective sync.'))
        if None._proto.is_admin:
            return format_html(trans('Team folders can only be deleted using the Content page in the Admin Console.<br/><br/>If you need to free up hard drive space, right-click this folder and make it online-only.'))
        return format_html(trans('Only Dropbox admins can delete Team folders.<br/><br/>If you need to free up hard drive space, right-click this folder and make it online-only.'))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        pass
    # WARNING: Decompyle incomplete



class TeamFolderMoveToTrashInaccessibleUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized TeamFolderMoveToTrashInaccessibleUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Can\'t delete "%(source_path)s"'), source_path = self._proto.source_path)

    
    def get_message(self):
        if self._proto.is_online_only:
            if self._proto.is_admin:
                return format_html(trans('Team folders can only be deleted using the Content page in the Admin Console.<br/><br/>To stop it from syncing with this computer, use selective sync.'))
            return format_html(trans('Only Dropbox admins can delete Team folders.<br/><br/>To stop it from syncing with this computer, use selective sync.'))
        if None._proto.is_admin:
            return format_html(trans('Team folders can only be deleted using the Content page in the Admin Console.<br/><br/>If you need to free up hard drive space, right-click this folder and make it online-only.'))
        return format_html(trans('Only Dropbox admins can delete Team folders.<br/><br/>If you need to free up hard drive space, right-click this folder and make it online-only.'))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        pass
    # WARNING: Decompyle incomplete



class TeamMemberFolderCopyUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized TeamMemberFolderCopyUI %r', proto)

    
    def get_caption(self):
        if self._proto.num_others == 0:
            return format_text(trans('Copied "%(source_filename)s" to "%(dest_parent_filename)s"'), source_filename = self._proto.source_filename, dest_parent_filename = self._proto.dest_parent_filename)
        return format_text(ungettext('Copied "%(source_filename)s" and %(num_others)s other item to "%(dest_parent_filename)s"', 'Copied "%(source_filename)s" and %(num_others)s other items to "%(dest_parent_filename)s"', self._proto.num_others), dest_parent_filename = self._proto.dest_parent_filename, num_others = self._proto.num_others, source_filename = self._proto.source_filename)

    
    def get_message(self):
        if self._proto.num_others == 0:
            return format_html(trans("Everyone who can access <b>%(dest_parent_filename)s</b> can now access a copy of <b>%(source_filename)s</b>. If you didn't mean to copy this item there, delete it."), dest_parent_filename = self._proto.dest_parent_filename, source_filename = self._proto.source_filename)
        return format_html(trans("Everyone who can access <b>%(dest_parent_filename)s</b> can now access a copy of all these items. If you didn't mean to copy these items there, delete them."), dest_parent_filename = self._proto.dest_parent_filename)

    
    def get_checkbox_message(self):
        return format_text(trans("Don't ask me this again"))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



class TeamMemberFolderMoveUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized TeamMemberFolderMoveUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_rename:
            return format_text(trans('Can\'t rename "%(source_path)s"'), source_path = self._proto.source_path)
        return format_text(trans('Can\'t move "%(source_path)s" to "%(dest_path)s"'), source_path = self._proto.source_path, dest_path = self._proto.dest_path)

    
    def get_message(self):
        return format_text(trans("Everyone on your team has their own member folder. This is where you can keep files that you don't want to share with everyone."))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('cdm_tmf')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class TeamMemberFolderMoveToTrashUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized TeamMemberFolderMoveToTrashUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Can\'t delete "%(source_path)s"'), source_path = self._proto.source_path)

    
    def get_message(self):
        return format_text(trans("Everyone on your team has their own member folder. This is where you can keep files that you don't want to share with everyone."))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), CLOSE_DIALOG)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('cdm_tmf')), button_action = LEARN_MORE_AND_CLOSE_DIALOG))]



class TeamMemberFolderMoveToTrashInaccessibleUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized TeamMemberFolderMoveToTrashInaccessibleUI %r', proto)

    
    def get_caption(self):
        return format_text(trans('Can\'t delete "%(source_path)s"'), source_path = self._proto.source_path)

    
    def get_message(self):
        return format_text(trans("Everyone on your team has their own member folder. This is where you can keep files that you don't want to share with everyone."))

    
    def get_checkbox_message(self):
        pass

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('OK'))

        return [
            (get_button0(), ALLOW)]

    
    def get_aux_buttons(self, fsw_dialog):
        
        def get_button0():
            return format_text(trans('Learn More'))

        return [
            (get_button0(), AuxFSWButton(learn_more = AuxButtonLearnMore(url = dropbox_url_info.help_url('cdm_tmf')), button_action = LEARN_MORE_AND_ALLOW))]



class WarningTmrMoveOutOfTeamSpaceUI(FswDialogInterface):
    
    def __init__(self, proto):
        self._proto = proto
        TRACE('initialized WarningTmrMoveOutOfTeamSpaceUI %r', proto)

    
    def get_caption(self):
        if self._proto.is_file:
            if self._proto.num == 0:
                return format_text(trans('Move file out of team folder?'))
            return format_text(ungettext('Move file out of team folder?', 'Move files out of team folder?', self._proto.num))
        if None._proto.num == 0:
            return format_text(trans('Move folder out of team folder?'))
        return format_text(ungettext('Move folder out of team folder?', 'Move folders out of team folder?', self._proto.num))

    
    def get_message(self):
        if self._proto.num_others == 0:
            return format_html(trans('Moving "%(name)s" removes access for members of "%(src_parent)s" and gives access to members of "%(dest)s". <a href="%(help_url)s">Learn more</a>'), name = self._proto.name, src_parent = self._proto.src_parent, dest = self._proto.dest, help_url = dropbox_url_info.help_url('remove_from_tsd'))
        return format_html(ungettext('Moving "%(name)s" and %(num_others)s other item removes access for members of "%(src_parent)s" and gives access to members of "%(dest)s". <a href="%(help_url)s">Learn more</a>', 'Moving "%(name)s" and %(num_others)s other items removes access for members of "%(src_parent)s" and gives access to members of "%(dest)s". <a href="%(help_url)s">Learn more</a>', self._proto.num_others), dest = self._proto.dest, help_url = dropbox_url_info.help_url('remove_from_tsd'), name = self._proto.name, num_others = self._proto.num_others, src_parent = self._proto.src_parent)

    
    def get_checkbox_message(self):
        return format_text(trans('Do not ask again'))

    
    def get_buttons(self):
        
        def get_button0():
            return format_text(trans('Move'))

        
        def get_button1():
            return format_text(trans('Cancel'))

        return [
            (get_button0(), ALLOW),
            (get_button1(), REVERT)]

    
    def get_aux_buttons(self, fsw_dialog):
        return []



def get_fsw_dialog(proto):
    which = proto.WhichOneof('dialog')
# WARNING: Decompyle incomplete


def get_all_fsw_dialogs_names():
    return [
        'allow_move_file_or_flat_folder_out_of_tsd',
        'allow_move_ns_out_of_tsd',
        'allow_move_to_forbid_non_team_sharing',
        'allow_move_to_forbid_sharing_when_owner_acl_only',
        'block_move_confidential_ns_out_of_team_space',
        'block_move_file_or_flat_folder_out_of_team_space',
        'block_move_forbid_non_team_sharing_ns_from_tsd',
        'block_move_from_team_space_to_outside_by_viewer',
        'block_move_ns_out_of_team_folder_by_actor_without_edit_access_to_containing_ns',
        'block_move_ns_with_nested_ns_from_tsd',
        'block_move_only_owner_can_update_acl_ns_from_tsd',
        'block_move_sf_to_tf_by_editor_when_non_owner_cannot_manage_membership',
        'block_move_sf_to_tf_by_viewer',
        'block_move_sf_to_tf_non_owner_diff_team',
        'block_move_shared_folder_out_of_tsd_by_viewer',
        'block_move_shared_folder_to_vault',
        'block_non_limited_team_and_owner_remove_ns_from_team_folder',
        'block_non_owner_remove_ns_from_team_folder',
        'block_tmr_move_out_of_team_space',
        'catch_all_copy',
        'cdm_onboarding_copy',
        'cdm_onboarding_create',
        'cdm_onboarding_move',
        'cloud_docs_copy_to_ignored',
        'cloud_docs_create',
        'cloud_docs_move_outside',
        'cloud_docs_move_outside2',
        'cloud_docs_move_to_ignored',
        'cloud_docs_move_to_trash',
        'cloud_docs_move_to_trash2',
        'cloud_docs_move_to_trash_inaccessible',
        'cloud_docs_move_to_trash_inaccessible2',
        'confidential_copy',
        'confidential_move',
        'device_folder_content_move_to_trash',
        'device_folder_content_move_to_trash_inaccessible',
        'device_folder_move_to_trash',
        'device_folder_move_to_trash_inaccessible',
        'device_folder_suggest_selsync',
        'device_folder_suggest_selsync_trash_inaccessible',
        'file_is_moved_from_unencrypted_to_encrypted_folder',
        'file_is_moved_out_of_encrypted_folder',
        'move_sf_to_tf_non_owner_confirmation',
        'per_node_metadata_deletable_entrypoint',
        'per_node_metadata_deletable_entrypoint_trash_inaccessible',
        'per_node_metadata_move',
        'per_node_metadata_move_to_trash',
        'per_node_metadata_move_to_trash_inaccessible',
        'per_node_metadata_rename',
        'restorations_1',
        'restorations_1_and_3_inaccessible',
        'restorations_2',
        'restorations_3',
        'restorations_4',
        'restorations_5',
        'restorations_5_inaccessible',
        'restorations_6a',
        'restorations_6a_example',
        'restorations_6b',
        'shared_folder_nesting',
        'shared_folder_nesting_implicit_share_on_move',
        'shared_folder_nesting_ownership_steal',
        'shared_folder_nesting_ownership_surrender',
        'smart_sync_move_to_trash',
        'smart_sync_move_to_trash_inaccessible',
        'team_folder_move',
        'team_folder_move_to_trash',
        'team_folder_move_to_trash_inaccessible',
        'team_member_folder_copy',
        'team_member_folder_move',
        'team_member_folder_move_to_trash',
        'team_member_folder_move_to_trash_inaccessible',
        'warning_tmr_move_out_of_team_space']


def get_fsw_dialog_variants(dialog_name):
    if dialog_name == 'allow_move_file_or_flat_folder_out_of_tsd':
        return [
            ShowFSWDialogReq(allow_move_file_or_flat_folder_out_of_tsd = AllowMoveFileOrFlatFolderOutOfTsd(dest = '<dest>', is_file = False, is_src_tsd_top_level = False, name = '<name>', num_others = 0, src_parent = '<src_parent>', team_name = '<team_name>')),
            ShowFSWDialogReq(allow_move_file_or_flat_folder_out_of_tsd = AllowMoveFileOrFlatFolderOutOfTsd(dest = '<dest>', is_file = False, is_src_tsd_top_level = False, name = '<name>', num_others = 1, src_parent = '<src_parent>', team_name = '<team_name>')),
            ShowFSWDialogReq(allow_move_file_or_flat_folder_out_of_tsd = AllowMoveFileOrFlatFolderOutOfTsd(dest = '<dest>', is_file = False, is_src_tsd_top_level = False, name = '<name>', num_others = 2, src_parent = '<src_parent>', team_name = '<team_name>')),
            ShowFSWDialogReq(allow_move_file_or_flat_folder_out_of_tsd = AllowMoveFileOrFlatFolderOutOfTsd(dest = '<dest>', is_file = False, is_src_tsd_top_level = True, name = '<name>', num_others = 0, src_parent = '<src_parent>', team_name = '<team_name>')),
            ShowFSWDialogReq(allow_move_file_or_flat_folder_out_of_tsd = AllowMoveFileOrFlatFolderOutOfTsd(dest = '<dest>', is_file = False, is_src_tsd_top_level = True, name = '<name>', num_others = 1, src_parent = '<src_parent>', team_name = '<team_name>')),
            ShowFSWDialogReq(allow_move_file_or_flat_folder_out_of_tsd = AllowMoveFileOrFlatFolderOutOfTsd(dest = '<dest>', is_file = False, is_src_tsd_top_level = True, name = '<name>', num_others = 2, src_parent = '<src_parent>', team_name = '<team_name>')),
            ShowFSWDialogReq(allow_move_file_or_flat_folder_out_of_tsd = AllowMoveFileOrFlatFolderOutOfTsd(dest = '<dest>', is_file = True, is_src_tsd_top_level = False, name = '<name>', num_others = 0, src_parent = '<src_parent>', team_name = '<team_name>')),
            ShowFSWDialogReq(allow_move_file_or_flat_folder_out_of_tsd = AllowMoveFileOrFlatFolderOutOfTsd(dest = '<dest>', is_file = True, is_src_tsd_top_level = False, name = '<name>', num_others = 1, src_parent = '<src_parent>', team_name = '<team_name>')),
            ShowFSWDialogReq(allow_move_file_or_flat_folder_out_of_tsd = AllowMoveFileOrFlatFolderOutOfTsd(dest = '<dest>', is_file = True, is_src_tsd_top_level = False, name = '<name>', num_others = 2, src_parent = '<src_parent>', team_name = '<team_name>')),
            ShowFSWDialogReq(allow_move_file_or_flat_folder_out_of_tsd = AllowMoveFileOrFlatFolderOutOfTsd(dest = '<dest>', is_file = True, is_src_tsd_top_level = True, name = '<name>', num_others = 0, src_parent = '<src_parent>', team_name = '<team_name>')),
            ShowFSWDialogReq(allow_move_file_or_flat_folder_out_of_tsd = AllowMoveFileOrFlatFolderOutOfTsd(dest = '<dest>', is_file = True, is_src_tsd_top_level = True, name = '<name>', num_others = 1, src_parent = '<src_parent>', team_name = '<team_name>')),
            ShowFSWDialogReq(allow_move_file_or_flat_folder_out_of_tsd = AllowMoveFileOrFlatFolderOutOfTsd(dest = '<dest>', is_file = True, is_src_tsd_top_level = True, name = '<name>', num_others = 2, src_parent = '<src_parent>', team_name = '<team_name>'))]
    if None == 'allow_move_ns_out_of_tsd':
        return [
            ShowFSWDialogReq(allow_move_ns_out_of_tsd = AllowMoveNsOutOfTsd(dest = '<dest>', is_src_tsd_top_level = False, name = '<name>', num_others = 0, src_parent = '<src_parent>', team_name = '<team_name>')),
            ShowFSWDialogReq(allow_move_ns_out_of_tsd = AllowMoveNsOutOfTsd(dest = '<dest>', is_src_tsd_top_level = False, name = '<name>', num_others = 1, src_parent = '<src_parent>', team_name = '<team_name>')),
            ShowFSWDialogReq(allow_move_ns_out_of_tsd = AllowMoveNsOutOfTsd(dest = '<dest>', is_src_tsd_top_level = False, name = '<name>', num_others = 2, src_parent = '<src_parent>', team_name = '<team_name>')),
            ShowFSWDialogReq(allow_move_ns_out_of_tsd = AllowMoveNsOutOfTsd(dest = '<dest>', is_src_tsd_top_level = True, name = '<name>', num_others = 0, src_parent = '<src_parent>', team_name = '<team_name>')),
            ShowFSWDialogReq(allow_move_ns_out_of_tsd = AllowMoveNsOutOfTsd(dest = '<dest>', is_src_tsd_top_level = True, name = '<name>', num_others = 1, src_parent = '<src_parent>', team_name = '<team_name>')),
            ShowFSWDialogReq(allow_move_ns_out_of_tsd = AllowMoveNsOutOfTsd(dest = '<dest>', is_src_tsd_top_level = True, name = '<name>', num_others = 2, src_parent = '<src_parent>', team_name = '<team_name>'))]
    if None == 'allow_move_to_forbid_non_team_sharing':
        return [
            ShowFSWDialogReq(allow_move_to_forbid_non_team_sharing = AllowMoveToForbidNonTeamSharing(name = '<name>', num_others = 0)),
            ShowFSWDialogReq(allow_move_to_forbid_non_team_sharing = AllowMoveToForbidNonTeamSharing(name = '<name>', num_others = 1)),
            ShowFSWDialogReq(allow_move_to_forbid_non_team_sharing = AllowMoveToForbidNonTeamSharing(name = '<name>', num_others = 2))]
    if None == 'allow_move_to_forbid_sharing_when_owner_acl_only':
        return [
            ShowFSWDialogReq(allow_move_to_forbid_sharing_when_owner_acl_only = AllowMoveToForbidSharingWhenOwnerAclOnly(name = '<name>', num_others = 0)),
            ShowFSWDialogReq(allow_move_to_forbid_sharing_when_owner_acl_only = AllowMoveToForbidSharingWhenOwnerAclOnly(name = '<name>', num_others = 1)),
            ShowFSWDialogReq(allow_move_to_forbid_sharing_when_owner_acl_only = AllowMoveToForbidSharingWhenOwnerAclOnly(name = '<name>', num_others = 2))]
    if None == 'block_move_confidential_ns_out_of_team_space':
        return [
            ShowFSWDialogReq(block_move_confidential_ns_out_of_team_space = BlockMoveConfidentialNsOutOfTeamSpace(name = '<name>', num = 0, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_confidential_ns_out_of_team_space = BlockMoveConfidentialNsOutOfTeamSpace(name = '<name>', num = 1, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_confidential_ns_out_of_team_space = BlockMoveConfidentialNsOutOfTeamSpace(name = '<name>', num = 2, team_name = '<team_name>'))]
    if None == 'block_move_file_or_flat_folder_out_of_team_space':
        return [
            ShowFSWDialogReq(block_move_file_or_flat_folder_out_of_team_space = BlockMoveFileOrFlatFolderOutOfTeamSpace(is_file = False, name = '<name>', num = 0, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_file_or_flat_folder_out_of_team_space = BlockMoveFileOrFlatFolderOutOfTeamSpace(is_file = False, name = '<name>', num = 1, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_file_or_flat_folder_out_of_team_space = BlockMoveFileOrFlatFolderOutOfTeamSpace(is_file = False, name = '<name>', num = 2, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_file_or_flat_folder_out_of_team_space = BlockMoveFileOrFlatFolderOutOfTeamSpace(is_file = True, name = '<name>', num = 0, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_file_or_flat_folder_out_of_team_space = BlockMoveFileOrFlatFolderOutOfTeamSpace(is_file = True, name = '<name>', num = 1, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_file_or_flat_folder_out_of_team_space = BlockMoveFileOrFlatFolderOutOfTeamSpace(is_file = True, name = '<name>', num = 2, team_name = '<team_name>'))]
    if None == 'block_move_forbid_non_team_sharing_ns_from_tsd':
        return [
            ShowFSWDialogReq(block_move_forbid_non_team_sharing_ns_from_tsd = BlockMoveForbidNonTeamSharingNsFromTsd(name = '<name>', num = 0, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_forbid_non_team_sharing_ns_from_tsd = BlockMoveForbidNonTeamSharingNsFromTsd(name = '<name>', num = 1, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_forbid_non_team_sharing_ns_from_tsd = BlockMoveForbidNonTeamSharingNsFromTsd(name = '<name>', num = 2, team_name = '<team_name>'))]
    if None == 'block_move_from_team_space_to_outside_by_viewer':
        return [
            ShowFSWDialogReq(block_move_from_team_space_to_outside_by_viewer = BlockMoveFromTeamSpaceToOutsideByViewer(dest = '<dest>', is_file = False, is_source_account_cdm = False, name = '<name>', num = 0, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_from_team_space_to_outside_by_viewer = BlockMoveFromTeamSpaceToOutsideByViewer(dest = '<dest>', is_file = False, is_source_account_cdm = False, name = '<name>', num = 1, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_from_team_space_to_outside_by_viewer = BlockMoveFromTeamSpaceToOutsideByViewer(dest = '<dest>', is_file = False, is_source_account_cdm = False, name = '<name>', num = 2, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_from_team_space_to_outside_by_viewer = BlockMoveFromTeamSpaceToOutsideByViewer(dest = '<dest>', is_file = False, is_source_account_cdm = True, name = '<name>', num = 0, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_from_team_space_to_outside_by_viewer = BlockMoveFromTeamSpaceToOutsideByViewer(dest = '<dest>', is_file = False, is_source_account_cdm = True, name = '<name>', num = 1, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_from_team_space_to_outside_by_viewer = BlockMoveFromTeamSpaceToOutsideByViewer(dest = '<dest>', is_file = False, is_source_account_cdm = True, name = '<name>', num = 2, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_from_team_space_to_outside_by_viewer = BlockMoveFromTeamSpaceToOutsideByViewer(dest = '<dest>', is_file = True, is_source_account_cdm = False, name = '<name>', num = 0, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_from_team_space_to_outside_by_viewer = BlockMoveFromTeamSpaceToOutsideByViewer(dest = '<dest>', is_file = True, is_source_account_cdm = False, name = '<name>', num = 1, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_from_team_space_to_outside_by_viewer = BlockMoveFromTeamSpaceToOutsideByViewer(dest = '<dest>', is_file = True, is_source_account_cdm = False, name = '<name>', num = 2, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_from_team_space_to_outside_by_viewer = BlockMoveFromTeamSpaceToOutsideByViewer(dest = '<dest>', is_file = True, is_source_account_cdm = True, name = '<name>', num = 0, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_from_team_space_to_outside_by_viewer = BlockMoveFromTeamSpaceToOutsideByViewer(dest = '<dest>', is_file = True, is_source_account_cdm = True, name = '<name>', num = 1, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_from_team_space_to_outside_by_viewer = BlockMoveFromTeamSpaceToOutsideByViewer(dest = '<dest>', is_file = True, is_source_account_cdm = True, name = '<name>', num = 2, team_name = '<team_name>'))]
    if None == 'block_move_ns_out_of_team_folder_by_actor_without_edit_access_to_containing_ns':
        return [
            ShowFSWDialogReq(block_move_ns_out_of_team_folder_by_actor_without_edit_access_to_containing_ns = BlockMoveNsOutOfTeamFolderByActorWithoutEditAccessToContainingNs(dest = '<dest>', name = '<name>', num = 0)),
            ShowFSWDialogReq(block_move_ns_out_of_team_folder_by_actor_without_edit_access_to_containing_ns = BlockMoveNsOutOfTeamFolderByActorWithoutEditAccessToContainingNs(dest = '<dest>', name = '<name>', num = 1)),
            ShowFSWDialogReq(block_move_ns_out_of_team_folder_by_actor_without_edit_access_to_containing_ns = BlockMoveNsOutOfTeamFolderByActorWithoutEditAccessToContainingNs(dest = '<dest>', name = '<name>', num = 2))]
    if None == 'block_move_ns_with_nested_ns_from_tsd':
        return [
            ShowFSWDialogReq(block_move_ns_with_nested_ns_from_tsd = BlockMoveNsWithNestedNsFromTsd(name = '<name>', num = 0, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_ns_with_nested_ns_from_tsd = BlockMoveNsWithNestedNsFromTsd(name = '<name>', num = 1, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_ns_with_nested_ns_from_tsd = BlockMoveNsWithNestedNsFromTsd(name = '<name>', num = 2, team_name = '<team_name>'))]
    if None == 'block_move_only_owner_can_update_acl_ns_from_tsd':
        return [
            ShowFSWDialogReq(block_move_only_owner_can_update_acl_ns_from_tsd = BlockMoveOnlyOwnerCanUpdateAclNsFromTsd(name = '<name>', num = 0, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_only_owner_can_update_acl_ns_from_tsd = BlockMoveOnlyOwnerCanUpdateAclNsFromTsd(name = '<name>', num = 1, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_only_owner_can_update_acl_ns_from_tsd = BlockMoveOnlyOwnerCanUpdateAclNsFromTsd(name = '<name>', num = 2, team_name = '<team_name>'))]
    if None == 'block_move_sf_to_tf_by_editor_when_non_owner_cannot_manage_membership':
        return [
            ShowFSWDialogReq(block_move_sf_to_tf_by_editor_when_non_owner_cannot_manage_membership = BlockMoveSfToTfByEditorWhenNonOwnerCannotManageMembership(is_source_account_cdm = False, num = 0, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_by_editor_when_non_owner_cannot_manage_membership = BlockMoveSfToTfByEditorWhenNonOwnerCannotManageMembership(is_source_account_cdm = False, num = 1, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_by_editor_when_non_owner_cannot_manage_membership = BlockMoveSfToTfByEditorWhenNonOwnerCannotManageMembership(is_source_account_cdm = False, num = 2, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_by_editor_when_non_owner_cannot_manage_membership = BlockMoveSfToTfByEditorWhenNonOwnerCannotManageMembership(is_source_account_cdm = True, num = 0, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_by_editor_when_non_owner_cannot_manage_membership = BlockMoveSfToTfByEditorWhenNonOwnerCannotManageMembership(is_source_account_cdm = True, num = 1, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_by_editor_when_non_owner_cannot_manage_membership = BlockMoveSfToTfByEditorWhenNonOwnerCannotManageMembership(is_source_account_cdm = True, num = 2, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>'))]
    if None == 'block_move_sf_to_tf_by_viewer':
        return [
            ShowFSWDialogReq(block_move_sf_to_tf_by_viewer = BlockMoveSfToTfByViewer(is_source_account_cdm = False, num = 0, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_by_viewer = BlockMoveSfToTfByViewer(is_source_account_cdm = False, num = 1, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_by_viewer = BlockMoveSfToTfByViewer(is_source_account_cdm = False, num = 2, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_by_viewer = BlockMoveSfToTfByViewer(is_source_account_cdm = True, num = 0, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_by_viewer = BlockMoveSfToTfByViewer(is_source_account_cdm = True, num = 1, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_by_viewer = BlockMoveSfToTfByViewer(is_source_account_cdm = True, num = 2, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>'))]
    if None == 'block_move_sf_to_tf_non_owner_diff_team':
        return [
            ShowFSWDialogReq(block_move_sf_to_tf_non_owner_diff_team = BlockMoveSfToTfNonOwnerDiffTeam(is_source_account_cdm = False, is_team = False, num = 0, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_non_owner_diff_team = BlockMoveSfToTfNonOwnerDiffTeam(is_source_account_cdm = False, is_team = False, num = 1, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_non_owner_diff_team = BlockMoveSfToTfNonOwnerDiffTeam(is_source_account_cdm = False, is_team = False, num = 2, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_non_owner_diff_team = BlockMoveSfToTfNonOwnerDiffTeam(is_source_account_cdm = False, is_team = True, num = 0, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_non_owner_diff_team = BlockMoveSfToTfNonOwnerDiffTeam(is_source_account_cdm = False, is_team = True, num = 1, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_non_owner_diff_team = BlockMoveSfToTfNonOwnerDiffTeam(is_source_account_cdm = False, is_team = True, num = 2, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_non_owner_diff_team = BlockMoveSfToTfNonOwnerDiffTeam(is_source_account_cdm = True, is_team = False, num = 0, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_non_owner_diff_team = BlockMoveSfToTfNonOwnerDiffTeam(is_source_account_cdm = True, is_team = False, num = 1, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_non_owner_diff_team = BlockMoveSfToTfNonOwnerDiffTeam(is_source_account_cdm = True, is_team = False, num = 2, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_non_owner_diff_team = BlockMoveSfToTfNonOwnerDiffTeam(is_source_account_cdm = True, is_team = True, num = 0, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_non_owner_diff_team = BlockMoveSfToTfNonOwnerDiffTeam(is_source_account_cdm = True, is_team = True, num = 1, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_sf_to_tf_non_owner_diff_team = BlockMoveSfToTfNonOwnerDiffTeam(is_source_account_cdm = True, is_team = True, num = 2, share_button_rr_paths = [], src_name = '<src_name>', team_name = '<team_name>'))]
    if None == 'block_move_shared_folder_out_of_tsd_by_viewer':
        return [
            ShowFSWDialogReq(block_move_shared_folder_out_of_tsd_by_viewer = BlockMoveSharedFolderOutOfTsdByViewer(name = '<name>', num = 0, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_shared_folder_out_of_tsd_by_viewer = BlockMoveSharedFolderOutOfTsdByViewer(name = '<name>', num = 1, team_name = '<team_name>')),
            ShowFSWDialogReq(block_move_shared_folder_out_of_tsd_by_viewer = BlockMoveSharedFolderOutOfTsdByViewer(name = '<name>', num = 2, team_name = '<team_name>'))]
    if None == 'block_move_shared_folder_to_vault':
        return [
            ShowFSWDialogReq(block_move_shared_folder_to_vault = BlockMoveSharedFolderToVault(num_others = 0, source_path = '<source_path>')),
            ShowFSWDialogReq(block_move_shared_folder_to_vault = BlockMoveSharedFolderToVault(num_others = 1, source_path = '<source_path>')),
            ShowFSWDialogReq(block_move_shared_folder_to_vault = BlockMoveSharedFolderToVault(num_others = 2, source_path = '<source_path>'))]
    if None == 'block_non_limited_team_and_owner_remove_ns_from_team_folder':
        return [
            ShowFSWDialogReq(block_non_limited_team_and_owner_remove_ns_from_team_folder = BlockNonLimitedTeamAndOwnerRemoveNsFromTeamFolder(dest = '<dest>', name = '<name>', num = 0)),
            ShowFSWDialogReq(block_non_limited_team_and_owner_remove_ns_from_team_folder = BlockNonLimitedTeamAndOwnerRemoveNsFromTeamFolder(dest = '<dest>', name = '<name>', num = 1)),
            ShowFSWDialogReq(block_non_limited_team_and_owner_remove_ns_from_team_folder = BlockNonLimitedTeamAndOwnerRemoveNsFromTeamFolder(dest = '<dest>', name = '<name>', num = 2))]
    if None == 'block_non_owner_remove_ns_from_team_folder':
        return [
            ShowFSWDialogReq(block_non_owner_remove_ns_from_team_folder = BlockNonOwnerRemoveNsFromTeamFolder(dest = '<dest>', name = '<name>', num = 0)),
            ShowFSWDialogReq(block_non_owner_remove_ns_from_team_folder = BlockNonOwnerRemoveNsFromTeamFolder(dest = '<dest>', name = '<name>', num = 1)),
            ShowFSWDialogReq(block_non_owner_remove_ns_from_team_folder = BlockNonOwnerRemoveNsFromTeamFolder(dest = '<dest>', name = '<name>', num = 2))]
    if None == 'block_tmr_move_out_of_team_space':
        return [
            ShowFSWDialogReq(block_tmr_move_out_of_team_space = BlockTmrMoveOutOfTeamSpace(is_file = False, num = 0)),
            ShowFSWDialogReq(block_tmr_move_out_of_team_space = BlockTmrMoveOutOfTeamSpace(is_file = False, num = 1)),
            ShowFSWDialogReq(block_tmr_move_out_of_team_space = BlockTmrMoveOutOfTeamSpace(is_file = False, num = 2)),
            ShowFSWDialogReq(block_tmr_move_out_of_team_space = BlockTmrMoveOutOfTeamSpace(is_file = True, num = 0)),
            ShowFSWDialogReq(block_tmr_move_out_of_team_space = BlockTmrMoveOutOfTeamSpace(is_file = True, num = 1)),
            ShowFSWDialogReq(block_tmr_move_out_of_team_space = BlockTmrMoveOutOfTeamSpace(is_file = True, num = 2))]
    if None == 'catch_all_copy':
        return [
            ShowFSWDialogReq(catch_all_copy = CatchAllCopy(dst_folder_name = '<dst_folder_name>', num_others = 0, src_name = '<src_name>'))]
    if None == 'cdm_onboarding_copy':
        return [
            ShowFSWDialogReq(cdm_onboarding_copy = CdmOnboardingCopy(dest_name = '<dest_name>', home_name = '<home_name>', num_others = 0, team_name = '<team_name>')),
            ShowFSWDialogReq(cdm_onboarding_copy = CdmOnboardingCopy(dest_name = '<dest_name>', home_name = '<home_name>', num_others = 1, team_name = '<team_name>')),
            ShowFSWDialogReq(cdm_onboarding_copy = CdmOnboardingCopy(dest_name = '<dest_name>', home_name = '<home_name>', num_others = 2, team_name = '<team_name>'))]
    if None == 'cdm_onboarding_create':
        return [
            ShowFSWDialogReq(cdm_onboarding_create = CdmOnboardingCreate(dest_name = '<dest_name>', home_name = '<home_name>', num_others = 0, team_name = '<team_name>')),
            ShowFSWDialogReq(cdm_onboarding_create = CdmOnboardingCreate(dest_name = '<dest_name>', home_name = '<home_name>', num_others = 1, team_name = '<team_name>')),
            ShowFSWDialogReq(cdm_onboarding_create = CdmOnboardingCreate(dest_name = '<dest_name>', home_name = '<home_name>', num_others = 2, team_name = '<team_name>'))]
    if None == 'cdm_onboarding_move':
        return [
            ShowFSWDialogReq(cdm_onboarding_move = CdmOnboardingMove(num_others = 0, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(cdm_onboarding_move = CdmOnboardingMove(num_others = 1, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(cdm_onboarding_move = CdmOnboardingMove(num_others = 2, src_name = '<src_name>', team_name = '<team_name>'))]
    if None == 'cloud_docs_copy_to_ignored':
        return [
            ShowFSWDialogReq(cloud_docs_copy_to_ignored = CloudDocsCopyToIgnored(name = '<name>', num_others = 0)),
            ShowFSWDialogReq(cloud_docs_copy_to_ignored = CloudDocsCopyToIgnored(name = '<name>', num_others = 1)),
            ShowFSWDialogReq(cloud_docs_copy_to_ignored = CloudDocsCopyToIgnored(name = '<name>', num_others = 2))]
    if None == 'cloud_docs_create':
        return [
            ShowFSWDialogReq(cloud_docs_create = CloudDocsCreate(name = '<name>', num_others = 0)),
            ShowFSWDialogReq(cloud_docs_create = CloudDocsCreate(name = '<name>', num_others = 1)),
            ShowFSWDialogReq(cloud_docs_create = CloudDocsCreate(name = '<name>', num_others = 2))]
    if None == 'cloud_docs_move_outside':
        return [][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside = CloudDocsMoveOutside(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 2, num_others = 2))]
    if None == 'cloud_docs_move_outside2':
        return [][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_outside2 = CloudDocsMoveOutside2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 2))]
    if None == 'cloud_docs_move_to_ignored':
        return [][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = False, name = '<name>', num_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = False, name = '<name>', num_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = False, name = '<name>', num_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = False, name = '<name>', num_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = False, name = '<name>', num_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = False, name = '<name>', num_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = False, name = '<name>', num_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = False, name = '<name>', num_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = False, name = '<name>', num_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = True, name = '<name>', num_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = True, name = '<name>', num_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = True, name = '<name>', num_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = True, name = '<name>', num_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = True, name = '<name>', num_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = True, name = '<name>', num_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = True, name = '<name>', num_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = True, name = '<name>', num_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = False, is_single_folder = True, name = '<name>', num_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = False, name = '<name>', num_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = False, name = '<name>', num_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = False, name = '<name>', num_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = False, name = '<name>', num_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = False, name = '<name>', num_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = False, name = '<name>', num_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = False, name = '<name>', num_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = False, name = '<name>', num_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = False, name = '<name>', num_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = True, name = '<name>', num_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = True, name = '<name>', num_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = True, name = '<name>', num_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = True, name = '<name>', num_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = True, name = '<name>', num_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = True, name = '<name>', num_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = True, name = '<name>', num_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = True, name = '<name>', num_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_ignored = CloudDocsMoveToIgnored(is_folder = True, is_single_folder = True, name = '<name>', num_files = 2, num_others = 2))]
    if None == 'cloud_docs_move_to_trash':
        return [][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash = CloudDocsMoveToTrash(is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_files = 2, num_others = 2))]
    if None == 'cloud_docs_move_to_trash2':
        return [][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash2 = CloudDocsMoveToTrash2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 2, num_others = 2))]
    if None == 'cloud_docs_move_to_trash_inaccessible':
        return [
            ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible = CloudDocsMoveToTrashInaccessible(num_cloud_files = 0)),
            ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible = CloudDocsMoveToTrashInaccessible(num_cloud_files = 1)),
            ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible = CloudDocsMoveToTrashInaccessible(num_cloud_files = 2))]
    if None == 'cloud_docs_move_to_trash_inaccessible2':
        return [][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = False, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = False, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = False, is_windows = True, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = False, name = '<name>', num_other_files = 2, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 0, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 0, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 0, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 1, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 1, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 1, num_others = 2))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 2, num_others = 0))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 2, num_others = 1))][ShowFSWDialogReq(cloud_docs_move_to_trash_inaccessible2 = CloudDocsMoveToTrashInaccessible2(file_name = '<file_name>', is_folder = True, is_single_folder = True, is_windows = True, name = '<name>', num_other_files = 2, num_others = 2))]
    if None == 'confidential_copy':
        return [
            ShowFSWDialogReq(confidential_copy = ConfidentialCopy(dst_folder_name = '<dst_folder_name>', num_all = 0, src_name = '<src_name>')),
            ShowFSWDialogReq(confidential_copy = ConfidentialCopy(dst_folder_name = '<dst_folder_name>', num_all = 1, src_name = '<src_name>')),
            ShowFSWDialogReq(confidential_copy = ConfidentialCopy(dst_folder_name = '<dst_folder_name>', num_all = 2, src_name = '<src_name>'))]
    if None == 'confidential_move':
        return [
            ShowFSWDialogReq(confidential_move = ConfidentialMove(dst_folder_name = '<dst_folder_name>', num = 0, num_all = 0, src_name = '<src_name>')),
            ShowFSWDialogReq(confidential_move = ConfidentialMove(dst_folder_name = '<dst_folder_name>', num = 0, num_all = 1, src_name = '<src_name>')),
            ShowFSWDialogReq(confidential_move = ConfidentialMove(dst_folder_name = '<dst_folder_name>', num = 0, num_all = 2, src_name = '<src_name>')),
            ShowFSWDialogReq(confidential_move = ConfidentialMove(dst_folder_name = '<dst_folder_name>', num = 1, num_all = 0, src_name = '<src_name>')),
            ShowFSWDialogReq(confidential_move = ConfidentialMove(dst_folder_name = '<dst_folder_name>', num = 1, num_all = 1, src_name = '<src_name>')),
            ShowFSWDialogReq(confidential_move = ConfidentialMove(dst_folder_name = '<dst_folder_name>', num = 1, num_all = 2, src_name = '<src_name>')),
            ShowFSWDialogReq(confidential_move = ConfidentialMove(dst_folder_name = '<dst_folder_name>', num = 2, num_all = 0, src_name = '<src_name>')),
            ShowFSWDialogReq(confidential_move = ConfidentialMove(dst_folder_name = '<dst_folder_name>', num = 2, num_all = 1, src_name = '<src_name>')),
            ShowFSWDialogReq(confidential_move = ConfidentialMove(dst_folder_name = '<dst_folder_name>', num = 2, num_all = 2, src_name = '<src_name>'))]
    if None == 'device_folder_content_move_to_trash':
        return [
            ShowFSWDialogReq(device_folder_content_move_to_trash = DeviceFolderContentMoveToTrash(device_folder_name = '<device_folder_name>', first_filename = '<first_filename>', num_others = 0)),
            ShowFSWDialogReq(device_folder_content_move_to_trash = DeviceFolderContentMoveToTrash(device_folder_name = '<device_folder_name>', first_filename = '<first_filename>', num_others = 1)),
            ShowFSWDialogReq(device_folder_content_move_to_trash = DeviceFolderContentMoveToTrash(device_folder_name = '<device_folder_name>', first_filename = '<first_filename>', num_others = 2))]
    if None == 'device_folder_content_move_to_trash_inaccessible':
        return [
            ShowFSWDialogReq(device_folder_content_move_to_trash_inaccessible = DeviceFolderContentMoveToTrashInaccessible(device_folder_name = '<device_folder_name>', first_filename = '<first_filename>', num_others = 0)),
            ShowFSWDialogReq(device_folder_content_move_to_trash_inaccessible = DeviceFolderContentMoveToTrashInaccessible(device_folder_name = '<device_folder_name>', first_filename = '<first_filename>', num_others = 1)),
            ShowFSWDialogReq(device_folder_content_move_to_trash_inaccessible = DeviceFolderContentMoveToTrashInaccessible(device_folder_name = '<device_folder_name>', first_filename = '<first_filename>', num_others = 2))]
    if None == 'device_folder_move_to_trash':
        return [
            ShowFSWDialogReq(device_folder_move_to_trash = DeviceFolderMoveToTrash(folder_name = '<folder_name>'))]
    if None == 'device_folder_move_to_trash_inaccessible':
        return [
            ShowFSWDialogReq(device_folder_move_to_trash_inaccessible = DeviceFolderMoveToTrashInaccessible(folder_name = '<folder_name>'))]
    if None == 'device_folder_suggest_selsync':
        return [
            ShowFSWDialogReq(device_folder_suggest_selsync = DeviceFolderSuggestSelsync(folder_name = '<folder_name>'))]
    if None == 'device_folder_suggest_selsync_trash_inaccessible':
        return [
            ShowFSWDialogReq(device_folder_suggest_selsync_trash_inaccessible = DeviceFolderSuggestSelsyncTrashInaccessible(folder_name = '<folder_name>'))]
    if None == 'file_is_moved_from_unencrypted_to_encrypted_folder':
        return [
            ShowFSWDialogReq(file_is_moved_from_unencrypted_to_encrypted_folder = FileIsMovedFromUnencryptedToEncryptedFolder())]
    if None == 'file_is_moved_out_of_encrypted_folder':
        return [
            ShowFSWDialogReq(file_is_moved_out_of_encrypted_folder = FileIsMovedOutOfEncryptedFolder())]
    if None == 'move_sf_to_tf_non_owner_confirmation':
        return [
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = False, is_source_account_cdm = False, is_source_shared_folder = False, num_others = 0, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = False, is_source_account_cdm = False, is_source_shared_folder = False, num_others = 1, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = False, is_source_account_cdm = False, is_source_shared_folder = False, num_others = 2, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = False, is_source_account_cdm = False, is_source_shared_folder = True, num_others = 0, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = False, is_source_account_cdm = False, is_source_shared_folder = True, num_others = 1, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = False, is_source_account_cdm = False, is_source_shared_folder = True, num_others = 2, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = False, is_source_account_cdm = True, is_source_shared_folder = False, num_others = 0, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = False, is_source_account_cdm = True, is_source_shared_folder = False, num_others = 1, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = False, is_source_account_cdm = True, is_source_shared_folder = False, num_others = 2, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = False, is_source_account_cdm = True, is_source_shared_folder = True, num_others = 0, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = False, is_source_account_cdm = True, is_source_shared_folder = True, num_others = 1, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = False, is_source_account_cdm = True, is_source_shared_folder = True, num_others = 2, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = True, is_source_account_cdm = False, is_source_shared_folder = False, num_others = 0, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = True, is_source_account_cdm = False, is_source_shared_folder = False, num_others = 1, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = True, is_source_account_cdm = False, is_source_shared_folder = False, num_others = 2, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = True, is_source_account_cdm = False, is_source_shared_folder = True, num_others = 0, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = True, is_source_account_cdm = False, is_source_shared_folder = True, num_others = 1, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = True, is_source_account_cdm = False, is_source_shared_folder = True, num_others = 2, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = True, is_source_account_cdm = True, is_source_shared_folder = False, num_others = 0, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = True, is_source_account_cdm = True, is_source_shared_folder = False, num_others = 1, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = True, is_source_account_cdm = True, is_source_shared_folder = False, num_others = 2, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = True, is_source_account_cdm = True, is_source_shared_folder = True, num_others = 0, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = True, is_source_account_cdm = True, is_source_shared_folder = True, num_others = 1, src_name = '<src_name>', team_name = '<team_name>')),
            ShowFSWDialogReq(move_sf_to_tf_non_owner_confirmation = MoveSfToTfNonOwnerConfirmation(dst_folder_name = '<dst_folder_name>', is_dst_tsd_top_level = True, is_source_account_cdm = True, is_source_shared_folder = True, num_others = 2, src_name = '<src_name>', team_name = '<team_name>'))]
    if None == 'per_node_metadata_deletable_entrypoint':
        return [
            ShowFSWDialogReq(per_node_metadata_deletable_entrypoint = PerNodeMetadataDeletableEntrypoint(filename = '<filename>'))]
    if None == 'per_node_metadata_deletable_entrypoint_trash_inaccessible':
        return [
            ShowFSWDialogReq(per_node_metadata_deletable_entrypoint_trash_inaccessible = PerNodeMetadataDeletableEntrypointTrashInaccessible(filename = '<filename>'))]
    if None == 'per_node_metadata_move':
        return [
            ShowFSWDialogReq(per_node_metadata_move = PerNodeMetadataMove(filename = '<filename>'))]
    if None == 'per_node_metadata_move_to_trash':
        return [
            ShowFSWDialogReq(per_node_metadata_move_to_trash = PerNodeMetadataMoveToTrash(filename = '<filename>'))]
    if None == 'per_node_metadata_move_to_trash_inaccessible':
        return [
            ShowFSWDialogReq(per_node_metadata_move_to_trash_inaccessible = PerNodeMetadataMoveToTrashInaccessible(filename = '<filename>'))]
    if None == 'per_node_metadata_rename':
        return [
            ShowFSWDialogReq(per_node_metadata_rename = PerNodeMetadataRename(filename = '<filename>'))]
    if None == 'restorations_1':
        return [
            ShowFSWDialogReq(restorations_1 = Restorations1(has_smart_sync = False, name = '<name>', num_others = 0)),
            ShowFSWDialogReq(restorations_1 = Restorations1(has_smart_sync = False, name = '<name>', num_others = 1)),
            ShowFSWDialogReq(restorations_1 = Restorations1(has_smart_sync = False, name = '<name>', num_others = 2)),
            ShowFSWDialogReq(restorations_1 = Restorations1(has_smart_sync = True, name = '<name>', num_others = 0)),
            ShowFSWDialogReq(restorations_1 = Restorations1(has_smart_sync = True, name = '<name>', num_others = 1)),
            ShowFSWDialogReq(restorations_1 = Restorations1(has_smart_sync = True, name = '<name>', num_others = 2))]
    if None == 'restorations_1_and_3_inaccessible':
        return [
            ShowFSWDialogReq(restorations_1_and_3_inaccessible = Restorations1And3Inaccessible(name = '<name>', num_others = 0)),
            ShowFSWDialogReq(restorations_1_and_3_inaccessible = Restorations1And3Inaccessible(name = '<name>', num_others = 1)),
            ShowFSWDialogReq(restorations_1_and_3_inaccessible = Restorations1And3Inaccessible(name = '<name>', num_others = 2))]
    if None == 'restorations_2':
        return [
            ShowFSWDialogReq(restorations_2 = Restorations2(dest = '<dest>', is_file = False, name = '<name>', num_others = 0)),
            ShowFSWDialogReq(restorations_2 = Restorations2(dest = '<dest>', is_file = False, name = '<name>', num_others = 1)),
            ShowFSWDialogReq(restorations_2 = Restorations2(dest = '<dest>', is_file = False, name = '<name>', num_others = 2)),
            ShowFSWDialogReq(restorations_2 = Restorations2(dest = '<dest>', is_file = True, name = '<name>', num_others = 0)),
            ShowFSWDialogReq(restorations_2 = Restorations2(dest = '<dest>', is_file = True, name = '<name>', num_others = 1)),
            ShowFSWDialogReq(restorations_2 = Restorations2(dest = '<dest>', is_file = True, name = '<name>', num_others = 2))]
    if None == 'restorations_3':
        return [
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = False, name = '<name>', num = 0, num_others = 0, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = False, name = '<name>', num = 0, num_others = 1, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = False, name = '<name>', num = 0, num_others = 2, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = False, name = '<name>', num = 1, num_others = 0, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = False, name = '<name>', num = 1, num_others = 1, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = False, name = '<name>', num = 1, num_others = 2, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = False, name = '<name>', num = 2, num_others = 0, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = False, name = '<name>', num = 2, num_others = 1, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = False, name = '<name>', num = 2, num_others = 2, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = True, name = '<name>', num = 0, num_others = 0, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = True, name = '<name>', num = 0, num_others = 1, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = True, name = '<name>', num = 0, num_others = 2, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = True, name = '<name>', num = 1, num_others = 0, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = True, name = '<name>', num = 1, num_others = 1, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = True, name = '<name>', num = 1, num_others = 2, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = True, name = '<name>', num = 2, num_others = 0, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = True, name = '<name>', num = 2, num_others = 1, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_3 = Restorations3(has_smart_sync = True, name = '<name>', num = 2, num_others = 2, share_button_rr_paths = []))]
    if None == 'restorations_4':
        return [
            ShowFSWDialogReq(restorations_4 = Restorations4(dest = '<dest>', name = '<name>', num = 0, num_others = 0, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_4 = Restorations4(dest = '<dest>', name = '<name>', num = 0, num_others = 1, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_4 = Restorations4(dest = '<dest>', name = '<name>', num = 0, num_others = 2, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_4 = Restorations4(dest = '<dest>', name = '<name>', num = 1, num_others = 0, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_4 = Restorations4(dest = '<dest>', name = '<name>', num = 1, num_others = 1, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_4 = Restorations4(dest = '<dest>', name = '<name>', num = 1, num_others = 2, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_4 = Restorations4(dest = '<dest>', name = '<name>', num = 2, num_others = 0, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_4 = Restorations4(dest = '<dest>', name = '<name>', num = 2, num_others = 1, share_button_rr_paths = [])),
            ShowFSWDialogReq(restorations_4 = Restorations4(dest = '<dest>', name = '<name>', num = 2, num_others = 2, share_button_rr_paths = []))]
    if None == 'restorations_5':
        return [
            ShowFSWDialogReq(restorations_5 = Restorations5(has_smart_sync = False, name = '<name>', num_others = 0)),
            ShowFSWDialogReq(restorations_5 = Restorations5(has_smart_sync = False, name = '<name>', num_others = 1)),
            ShowFSWDialogReq(restorations_5 = Restorations5(has_smart_sync = False, name = '<name>', num_others = 2)),
            ShowFSWDialogReq(restorations_5 = Restorations5(has_smart_sync = True, name = '<name>', num_others = 0)),
            ShowFSWDialogReq(restorations_5 = Restorations5(has_smart_sync = True, name = '<name>', num_others = 1)),
            ShowFSWDialogReq(restorations_5 = Restorations5(has_smart_sync = True, name = '<name>', num_others = 2))]
    if None == 'restorations_5_inaccessible':
        return [
            ShowFSWDialogReq(restorations_5_inaccessible = Restorations5Inaccessible(name = '<name>', num_others = 0)),
            ShowFSWDialogReq(restorations_5_inaccessible = Restorations5Inaccessible(name = '<name>', num_others = 1)),
            ShowFSWDialogReq(restorations_5_inaccessible = Restorations5Inaccessible(name = '<name>', num_others = 2))]
    if None == 'restorations_6a':
        return [
            ShowFSWDialogReq(restorations_6a = Restorations6a(dest = '<dest>', is_file = False, name = '<name>', num_others = 0, src_parent = '<src_parent>')),
            ShowFSWDialogReq(restorations_6a = Restorations6a(dest = '<dest>', is_file = False, name = '<name>', num_others = 1, src_parent = '<src_parent>')),
            ShowFSWDialogReq(restorations_6a = Restorations6a(dest = '<dest>', is_file = False, name = '<name>', num_others = 2, src_parent = '<src_parent>')),
            ShowFSWDialogReq(restorations_6a = Restorations6a(dest = '<dest>', is_file = True, name = '<name>', num_others = 0, src_parent = '<src_parent>')),
            ShowFSWDialogReq(restorations_6a = Restorations6a(dest = '<dest>', is_file = True, name = '<name>', num_others = 1, src_parent = '<src_parent>')),
            ShowFSWDialogReq(restorations_6a = Restorations6a(dest = '<dest>', is_file = True, name = '<name>', num_others = 2, src_parent = '<src_parent>'))]
    if None == 'restorations_6a_example':
        return [
            ShowFSWDialogReq(restorations_6a_example = Restorations6aExample(dest = '<dest>', is_file = False, name = '<name>', num_others = 0, share_button_rr_paths = [], src_parent = '<src_parent>')),
            ShowFSWDialogReq(restorations_6a_example = Restorations6aExample(dest = '<dest>', is_file = False, name = '<name>', num_others = 1, share_button_rr_paths = [], src_parent = '<src_parent>')),
            ShowFSWDialogReq(restorations_6a_example = Restorations6aExample(dest = '<dest>', is_file = False, name = '<name>', num_others = 2, share_button_rr_paths = [], src_parent = '<src_parent>')),
            ShowFSWDialogReq(restorations_6a_example = Restorations6aExample(dest = '<dest>', is_file = True, name = '<name>', num_others = 0, share_button_rr_paths = [], src_parent = '<src_parent>')),
            ShowFSWDialogReq(restorations_6a_example = Restorations6aExample(dest = '<dest>', is_file = True, name = '<name>', num_others = 1, share_button_rr_paths = [], src_parent = '<src_parent>')),
            ShowFSWDialogReq(restorations_6a_example = Restorations6aExample(dest = '<dest>', is_file = True, name = '<name>', num_others = 2, share_button_rr_paths = [], src_parent = '<src_parent>'))]
    if None == 'restorations_6b':
        return [
            ShowFSWDialogReq(restorations_6b = Restorations6b(dest = '<dest>', is_file = False, name = '<name>', num_others = 0)),
            ShowFSWDialogReq(restorations_6b = Restorations6b(dest = '<dest>', is_file = False, name = '<name>', num_others = 1)),
            ShowFSWDialogReq(restorations_6b = Restorations6b(dest = '<dest>', is_file = False, name = '<name>', num_others = 2)),
            ShowFSWDialogReq(restorations_6b = Restorations6b(dest = '<dest>', is_file = True, name = '<name>', num_others = 0)),
            ShowFSWDialogReq(restorations_6b = Restorations6b(dest = '<dest>', is_file = True, name = '<name>', num_others = 1)),
            ShowFSWDialogReq(restorations_6b = Restorations6b(dest = '<dest>', is_file = True, name = '<name>', num_others = 2))]
    if None == 'shared_folder_nesting':
        return [
            ShowFSWDialogReq(shared_folder_nesting = SharedFolderNesting(dest_path = '<dest_path>', is_team = False, source_path = '<source_path>')),
            ShowFSWDialogReq(shared_folder_nesting = SharedFolderNesting(dest_path = '<dest_path>', is_team = True, source_path = '<source_path>'))]
    if None == 'shared_folder_nesting_implicit_share_on_move':
        return [
            ShowFSWDialogReq(shared_folder_nesting_implicit_share_on_move = SharedFolderNestingImplicitShareOnMove(dest_path = '<dest_path>', is_rename = False, num = 0, source_path = '<source_path>')),
            ShowFSWDialogReq(shared_folder_nesting_implicit_share_on_move = SharedFolderNestingImplicitShareOnMove(dest_path = '<dest_path>', is_rename = False, num = 1, source_path = '<source_path>')),
            ShowFSWDialogReq(shared_folder_nesting_implicit_share_on_move = SharedFolderNestingImplicitShareOnMove(dest_path = '<dest_path>', is_rename = False, num = 2, source_path = '<source_path>')),
            ShowFSWDialogReq(shared_folder_nesting_implicit_share_on_move = SharedFolderNestingImplicitShareOnMove(dest_path = '<dest_path>', is_rename = True, num = 0, source_path = '<source_path>')),
            ShowFSWDialogReq(shared_folder_nesting_implicit_share_on_move = SharedFolderNestingImplicitShareOnMove(dest_path = '<dest_path>', is_rename = True, num = 1, source_path = '<source_path>')),
            ShowFSWDialogReq(shared_folder_nesting_implicit_share_on_move = SharedFolderNestingImplicitShareOnMove(dest_path = '<dest_path>', is_rename = True, num = 2, source_path = '<source_path>'))]
    if None == 'shared_folder_nesting_ownership_steal':
        return [
            ShowFSWDialogReq(shared_folder_nesting_ownership_steal = SharedFolderNestingOwnershipSteal(dest_path = '<dest_path>', is_source_shared_folder = False, source_path = '<source_path>')),
            ShowFSWDialogReq(shared_folder_nesting_ownership_steal = SharedFolderNestingOwnershipSteal(dest_path = '<dest_path>', is_source_shared_folder = True, source_path = '<source_path>'))]
    if None == 'shared_folder_nesting_ownership_surrender':
        return [
            ShowFSWDialogReq(shared_folder_nesting_ownership_surrender = SharedFolderNestingOwnershipSurrender(dest_path = '<dest_path>', is_source_shared_folder = False, owned_shared_folder_count = 0)),
            ShowFSWDialogReq(shared_folder_nesting_ownership_surrender = SharedFolderNestingOwnershipSurrender(dest_path = '<dest_path>', is_source_shared_folder = False, owned_shared_folder_count = 1)),
            ShowFSWDialogReq(shared_folder_nesting_ownership_surrender = SharedFolderNestingOwnershipSurrender(dest_path = '<dest_path>', is_source_shared_folder = False, owned_shared_folder_count = 2)),
            ShowFSWDialogReq(shared_folder_nesting_ownership_surrender = SharedFolderNestingOwnershipSurrender(dest_path = '<dest_path>', is_source_shared_folder = True, owned_shared_folder_count = 0)),
            ShowFSWDialogReq(shared_folder_nesting_ownership_surrender = SharedFolderNestingOwnershipSurrender(dest_path = '<dest_path>', is_source_shared_folder = True, owned_shared_folder_count = 1)),
            ShowFSWDialogReq(shared_folder_nesting_ownership_surrender = SharedFolderNestingOwnershipSurrender(dest_path = '<dest_path>', is_source_shared_folder = True, owned_shared_folder_count = 2))]
    if None == 'smart_sync_move_to_trash':
        return [
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = False, is_any_in_shared_folder = False, is_windows = False, num_others = 0)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = False, is_any_in_shared_folder = False, is_windows = False, num_others = 1)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = False, is_any_in_shared_folder = False, is_windows = False, num_others = 2)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = False, is_any_in_shared_folder = False, is_windows = True, num_others = 0)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = False, is_any_in_shared_folder = False, is_windows = True, num_others = 1)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = False, is_any_in_shared_folder = False, is_windows = True, num_others = 2)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = False, is_any_in_shared_folder = True, is_windows = False, num_others = 0)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = False, is_any_in_shared_folder = True, is_windows = False, num_others = 1)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = False, is_any_in_shared_folder = True, is_windows = False, num_others = 2)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = False, is_any_in_shared_folder = True, is_windows = True, num_others = 0)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = False, is_any_in_shared_folder = True, is_windows = True, num_others = 1)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = False, is_any_in_shared_folder = True, is_windows = True, num_others = 2)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = True, is_any_in_shared_folder = False, is_windows = False, num_others = 0)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = True, is_any_in_shared_folder = False, is_windows = False, num_others = 1)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = True, is_any_in_shared_folder = False, is_windows = False, num_others = 2)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = True, is_any_in_shared_folder = False, is_windows = True, num_others = 0)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = True, is_any_in_shared_folder = False, is_windows = True, num_others = 1)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = True, is_any_in_shared_folder = False, is_windows = True, num_others = 2)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = True, is_any_in_shared_folder = True, is_windows = False, num_others = 0)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = True, is_any_in_shared_folder = True, is_windows = False, num_others = 1)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = True, is_any_in_shared_folder = True, is_windows = False, num_others = 2)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = True, is_any_in_shared_folder = True, is_windows = True, num_others = 0)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = True, is_any_in_shared_folder = True, is_windows = True, num_others = 1)),
            ShowFSWDialogReq(smart_sync_move_to_trash = SmartSyncMoveToTrash(filename = '<filename>', is_any_folder = True, is_any_in_shared_folder = True, is_windows = True, num_others = 2))]
    if None == 'smart_sync_move_to_trash_inaccessible':
        return [
            ShowFSWDialogReq(smart_sync_move_to_trash_inaccessible = SmartSyncMoveToTrashInaccessible(involved_placeholder_count = 0, is_any_in_shared_folder = False)),
            ShowFSWDialogReq(smart_sync_move_to_trash_inaccessible = SmartSyncMoveToTrashInaccessible(involved_placeholder_count = 1, is_any_in_shared_folder = False)),
            ShowFSWDialogReq(smart_sync_move_to_trash_inaccessible = SmartSyncMoveToTrashInaccessible(involved_placeholder_count = 2, is_any_in_shared_folder = False)),
            ShowFSWDialogReq(smart_sync_move_to_trash_inaccessible = SmartSyncMoveToTrashInaccessible(involved_placeholder_count = 0, is_any_in_shared_folder = True)),
            ShowFSWDialogReq(smart_sync_move_to_trash_inaccessible = SmartSyncMoveToTrashInaccessible(involved_placeholder_count = 1, is_any_in_shared_folder = True)),
            ShowFSWDialogReq(smart_sync_move_to_trash_inaccessible = SmartSyncMoveToTrashInaccessible(involved_placeholder_count = 2, is_any_in_shared_folder = True))]
    if None == 'team_folder_move':
        return [
            ShowFSWDialogReq(team_folder_move = TeamFolderMove(dest_path = '<dest_path>', is_admin = False, is_rename = False, source_path = '<source_path>')),
            ShowFSWDialogReq(team_folder_move = TeamFolderMove(dest_path = '<dest_path>', is_admin = False, is_rename = True, source_path = '<source_path>')),
            ShowFSWDialogReq(team_folder_move = TeamFolderMove(dest_path = '<dest_path>', is_admin = True, is_rename = False, source_path = '<source_path>')),
            ShowFSWDialogReq(team_folder_move = TeamFolderMove(dest_path = '<dest_path>', is_admin = True, is_rename = True, source_path = '<source_path>'))]
    if None == 'team_folder_move_to_trash':
        return [
            ShowFSWDialogReq(team_folder_move_to_trash = TeamFolderMoveToTrash(dest_path = '<dest_path>', is_admin = False, is_online_only = False, source_path = '<source_path>')),
            ShowFSWDialogReq(team_folder_move_to_trash = TeamFolderMoveToTrash(dest_path = '<dest_path>', is_admin = False, is_online_only = True, source_path = '<source_path>')),
            ShowFSWDialogReq(team_folder_move_to_trash = TeamFolderMoveToTrash(dest_path = '<dest_path>', is_admin = True, is_online_only = False, source_path = '<source_path>')),
            ShowFSWDialogReq(team_folder_move_to_trash = TeamFolderMoveToTrash(dest_path = '<dest_path>', is_admin = True, is_online_only = True, source_path = '<source_path>'))]
    if None == 'team_folder_move_to_trash_inaccessible':
        return [
            ShowFSWDialogReq(team_folder_move_to_trash_inaccessible = TeamFolderMoveToTrashInaccessible(dest_path = '<dest_path>', is_admin = False, is_online_only = False, source_path = '<source_path>')),
            ShowFSWDialogReq(team_folder_move_to_trash_inaccessible = TeamFolderMoveToTrashInaccessible(dest_path = '<dest_path>', is_admin = False, is_online_only = True, source_path = '<source_path>')),
            ShowFSWDialogReq(team_folder_move_to_trash_inaccessible = TeamFolderMoveToTrashInaccessible(dest_path = '<dest_path>', is_admin = True, is_online_only = False, source_path = '<source_path>')),
            ShowFSWDialogReq(team_folder_move_to_trash_inaccessible = TeamFolderMoveToTrashInaccessible(dest_path = '<dest_path>', is_admin = True, is_online_only = True, source_path = '<source_path>'))]
    if None == 'team_member_folder_copy':
        return [
            ShowFSWDialogReq(team_member_folder_copy = TeamMemberFolderCopy(dest_parent_filename = '<dest_parent_filename>', num_others = 0, source_filename = '<source_filename>')),
            ShowFSWDialogReq(team_member_folder_copy = TeamMemberFolderCopy(dest_parent_filename = '<dest_parent_filename>', num_others = 1, source_filename = '<source_filename>')),
            ShowFSWDialogReq(team_member_folder_copy = TeamMemberFolderCopy(dest_parent_filename = '<dest_parent_filename>', num_others = 2, source_filename = '<source_filename>'))]
    if None == 'team_member_folder_move':
        return [
            ShowFSWDialogReq(team_member_folder_move = TeamMemberFolderMove(dest_path = '<dest_path>', is_rename = False, source_path = '<source_path>')),
            ShowFSWDialogReq(team_member_folder_move = TeamMemberFolderMove(dest_path = '<dest_path>', is_rename = True, source_path = '<source_path>'))]
    if None == 'team_member_folder_move_to_trash':
        return [
            ShowFSWDialogReq(team_member_folder_move_to_trash = TeamMemberFolderMoveToTrash(dest_path = '<dest_path>', is_rename = False, source_path = '<source_path>'))]
    if None == 'team_member_folder_move_to_trash_inaccessible':
        return [
            ShowFSWDialogReq(team_member_folder_move_to_trash_inaccessible = TeamMemberFolderMoveToTrashInaccessible(dest_path = '<dest_path>', is_rename = False, source_path = '<source_path>'))]
    if None == 'warning_tmr_move_out_of_team_space':
        return [
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = False, name = '<name>', num = 0, num_others = 0, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = False, name = '<name>', num = 0, num_others = 1, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = False, name = '<name>', num = 0, num_others = 2, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = False, name = '<name>', num = 1, num_others = 0, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = False, name = '<name>', num = 1, num_others = 1, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = False, name = '<name>', num = 1, num_others = 2, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = False, name = '<name>', num = 2, num_others = 0, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = False, name = '<name>', num = 2, num_others = 1, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = False, name = '<name>', num = 2, num_others = 2, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = True, name = '<name>', num = 0, num_others = 0, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = True, name = '<name>', num = 0, num_others = 1, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = True, name = '<name>', num = 0, num_others = 2, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = True, name = '<name>', num = 1, num_others = 0, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = True, name = '<name>', num = 1, num_others = 1, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = True, name = '<name>', num = 1, num_others = 2, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = True, name = '<name>', num = 2, num_others = 0, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = True, name = '<name>', num = 2, num_others = 1, src_parent = '<src_parent>')),
            ShowFSWDialogReq(warning_tmr_move_out_of_team_space = WarningTmrMoveOutOfTeamSpace(dest = '<dest>', is_file = True, name = '<name>', num = 2, num_others = 2, src_parent = '<src_parent>'))]
    raise 'dialog_name %s is unknown' % dialog_name()

