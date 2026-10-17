# Source Generated with Decompyle++
# File: account.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import account_id
from dropbox.api.v2.datatypes import async_
from dropbox.api.v2.datatypes import common
from dropbox.api.v2.datatypes import public_id

class AccessInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AccessInfo_validator = bv.Struct(AccessInfo)

class AccountNameArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AccountNameArg_validator = bv.Struct(AccountNameArg)

class AccountPhotoGetArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AccountPhotoGetArg_validator = bv.Struct(AccountPhotoGetArg)

class AccountPhotoGetError(bb.Union):
    pass
# WARNING: Decompyle incomplete

AccountPhotoGetError_validator = bv.Union(AccountPhotoGetError)

class AccountPhotoGetResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AccountPhotoGetResult_validator = bv.Struct(AccountPhotoGetResult)

class ThirdPartyLoginArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ThirdPartyLoginArg_validator = bv.Struct(ThirdPartyLoginArg)

class AppleLoginArg(ThirdPartyLoginArg):
    pass
# WARNING: Decompyle incomplete

AppleLoginArg_validator = bv.Struct(AppleLoginArg)

class ThirdPartyLoginError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ThirdPartyLoginError_validator = bv.Union(ThirdPartyLoginError)

class AppleLoginError(ThirdPartyLoginError):
    pass
# WARNING: Decompyle incomplete

AppleLoginError_validator = bv.Union(AppleLoginError)

class ThirdPartyLoginResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

ThirdPartyLoginResult_validator = bv.Union(ThirdPartyLoginResult)

class AppleLoginResult(ThirdPartyLoginResult):
    pass
# WARNING: Decompyle incomplete

AppleLoginResult_validator = bv.Union(AppleLoginResult)

class ThirdPartySignupArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ThirdPartySignupArg_validator = bv.Struct(ThirdPartySignupArg)

class AppleSignupArg(ThirdPartySignupArg):
    pass
# WARNING: Decompyle incomplete

AppleSignupArg_validator = bv.Struct(AppleSignupArg)

class AppleSignupError(bb.Union):
    pass
# WARNING: Decompyle incomplete

AppleSignupError_validator = bv.Union(AppleSignupError)

class ThirdPartySignupResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ThirdPartySignupResult_validator = bv.Struct(ThirdPartySignupResult)

class AppleSignupResult(ThirdPartySignupResult):
    pass
# WARNING: Decompyle incomplete

AppleSignupResult_validator = bv.Struct(AppleSignupResult)

class AuthCredential(bb.Union):
    pass
# WARNING: Decompyle incomplete

AuthCredential_validator = bv.Union(AuthCredential)

class ChangeEmailInitiateArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ChangeEmailInitiateArg_validator = bv.Struct(ChangeEmailInitiateArg)

class ChangeEmailInitiateError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ChangeEmailInitiateError_validator = bv.Union(ChangeEmailInitiateError)

class ChangeEmailInitiateResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ChangeEmailInitiateResponse_validator = bv.Struct(ChangeEmailInitiateResponse)

class ChangeEmailType(bb.Union):
    pass
# WARNING: Decompyle incomplete

ChangeEmailType_validator = bv.Union(ChangeEmailType)

class ChangeNameError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ChangeNameError_validator = bv.Union(ChangeNameError)

class CheckPasswordlessStateArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CheckPasswordlessStateArg_validator = bv.Struct(CheckPasswordlessStateArg)

class CheckPasswordlessStateError(bb.Union):
    pass
# WARNING: Decompyle incomplete

CheckPasswordlessStateError_validator = bv.Union(CheckPasswordlessStateError)

class CheckPaswordlessStateResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CheckPaswordlessStateResult_validator = bv.Struct(CheckPaswordlessStateResult)

class CheckUserWithEmailExistsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CheckUserWithEmailExistsArg_validator = bv.Struct(CheckUserWithEmailExistsArg)

class CheckUserWithEmailExistsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

CheckUserWithEmailExistsError_validator = bv.Union(CheckUserWithEmailExistsError)

class CheckUserWithEmailExistsResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CheckUserWithEmailExistsResult_validator = bv.Struct(CheckUserWithEmailExistsResult)

class CompanyInfoResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CompanyInfoResult_validator = bv.Struct(CompanyInfoResult)

class CompleteRegistrationArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CompleteRegistrationArg_validator = bv.Struct(CompleteRegistrationArg)

class CompleteRegistrationError(bb.Union):
    pass
# WARNING: Decompyle incomplete

CompleteRegistrationError_validator = bv.Union(CompleteRegistrationError)

class CompleteRegistrationResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CompleteRegistrationResult_validator = bv.Struct(CompleteRegistrationResult)

class CompleteRegistrationResultUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

CompleteRegistrationResultUnion_validator = bv.Union(CompleteRegistrationResultUnion)

class CreateAccountArg(AccountNameArg):
    pass
# WARNING: Decompyle incomplete

CreateAccountArg_validator = bv.Struct(CreateAccountArg)

class CreateAccountError(bb.Union):
    pass
# WARNING: Decompyle incomplete

CreateAccountError_validator = bv.Union(CreateAccountError)

class CreateAccountResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

CreateAccountResult_validator = bv.Union(CreateAccountResult)

class CreateOrLinkAccountWithIdpArg(AccountNameArg):
    pass
# WARNING: Decompyle incomplete

CreateOrLinkAccountWithIdpArg_validator = bv.Struct(CreateOrLinkAccountWithIdpArg)

class CreateOrLinkAccountWithIdpError(bb.Union):
    pass
# WARNING: Decompyle incomplete

CreateOrLinkAccountWithIdpError_validator = bv.Union(CreateOrLinkAccountWithIdpError)

class CreateOrLinkAccountWithIdpResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreateOrLinkAccountWithIdpResult_validator = bv.Struct(CreateOrLinkAccountWithIdpResult)

class DeleteAccountArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeleteAccountArg_validator = bv.Struct(DeleteAccountArg)

class DeleteAccountError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DeleteAccountError_validator = bv.Union(DeleteAccountError)

class DeleteAccountReasonUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

DeleteAccountReasonUnion_validator = bv.Union(DeleteAccountReasonUnion)

class DeleteAccountResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeleteAccountResult_validator = bv.Struct(DeleteAccountResult)

class DeleteArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeleteArg_validator = bv.Struct(DeleteArg)

class DeleteCompanyInfoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeleteCompanyInfoArg_validator = bv.Struct(DeleteCompanyInfoArg)

class DeleteCompanyInfoError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DeleteCompanyInfoError_validator = bv.Union(DeleteCompanyInfoError)

class DeleteError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DeleteError_validator = bv.Union(DeleteError)

class DeleteProfilePhotoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeleteProfilePhotoArg_validator = bv.Struct(DeleteProfilePhotoArg)

class DeleteProfilePhotoError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DeleteProfilePhotoError_validator = bv.Union(DeleteProfilePhotoError)

class DeleteProfilePhotoResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeleteProfilePhotoResult_validator = bv.Struct(DeleteProfilePhotoResult)

class DeleteResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeleteResponse_validator = bv.Struct(DeleteResponse)

class DeviceInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeviceInfo_validator = bv.Struct(DeviceInfo)

class EmailInvalidError(bb.Union):
    pass
# WARNING: Decompyle incomplete

EmailInvalidError_validator = bv.Union(EmailInvalidError)

class EmmValidationError(bb.Union):
    pass
# WARNING: Decompyle incomplete

EmmValidationError_validator = bv.Union(EmmValidationError)

class ForeignUserType(bb.Union):
    pass
# WARNING: Decompyle incomplete

ForeignUserType_validator = bv.Union(ForeignUserType)

class GetCompanyInfoError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetCompanyInfoError_validator = bv.Union(GetCompanyInfoError)

class GetOrCreateForeignUserArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetOrCreateForeignUserArgs_validator = bv.Struct(GetOrCreateForeignUserArgs)

class GetOrCreateForeignUserError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetOrCreateForeignUserError_validator = bv.Union(GetOrCreateForeignUserError)

class GetOrCreateForeignUserResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetOrCreateForeignUserResult_validator = bv.Struct(GetOrCreateForeignUserResult)

class GoogleLoginArg(ThirdPartyLoginArg):
    pass
# WARNING: Decompyle incomplete

GoogleLoginArg_validator = bv.Struct(GoogleLoginArg)

class GoogleLoginError(ThirdPartyLoginError):
    pass
# WARNING: Decompyle incomplete

GoogleLoginError_validator = bv.Union(GoogleLoginError)

class GoogleLoginResult(ThirdPartyLoginResult):
    pass
# WARNING: Decompyle incomplete

GoogleLoginResult_validator = bv.Union(GoogleLoginResult)

class GoogleSignupArg(ThirdPartySignupArg):
    pass
# WARNING: Decompyle incomplete

GoogleSignupArg_validator = bv.Struct(GoogleSignupArg)

class GoogleSignupAuthArg(bb.Union):
    pass
# WARNING: Decompyle incomplete

GoogleSignupAuthArg_validator = bv.Union(GoogleSignupAuthArg)

class GoogleSignupError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GoogleSignupError_validator = bv.Union(GoogleSignupError)

class GoogleSignupResult(ThirdPartySignupResult):
    pass
# WARNING: Decompyle incomplete

GoogleSignupResult_validator = bv.Struct(GoogleSignupResult)

class IdpAuthCode(bb.Union):
    pass
# WARNING: Decompyle incomplete

IdpAuthCode_validator = bv.Union(IdpAuthCode)

class InaccessibleSubaccount(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InaccessibleSubaccount_validator = bv.Struct(InaccessibleSubaccount)

class InitiateEmailChangeArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InitiateEmailChangeArg_validator = bv.Struct(InitiateEmailChangeArg)

class InitiateEmailChangeError(bb.Union):
    pass
# WARNING: Decompyle incomplete

InitiateEmailChangeError_validator = bv.Union(InitiateEmailChangeError)

class InitiateEmailChangeResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

InitiateEmailChangeResult_validator = bv.Union(InitiateEmailChangeResult)

class InitiateEmailChangeSource(bb.Union):
    pass
# WARNING: Decompyle incomplete

InitiateEmailChangeSource_validator = bv.Union(InitiateEmailChangeSource)

class IosAppAttestInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

IosAppAttestInfo_validator = bv.Struct(IosAppAttestInfo)

class ListInaccessibleSubaccountsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListInaccessibleSubaccountsArg_validator = bv.Struct(ListInaccessibleSubaccountsArg)

class ListInaccessibleSubaccountsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListInaccessibleSubaccountsError_validator = bv.Union(ListInaccessibleSubaccountsError)

class ListInaccessibleSubaccountsResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListInaccessibleSubaccountsResponse_validator = bv.Struct(ListInaccessibleSubaccountsResponse)

class LoginArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LoginArg_validator = bv.Struct(LoginArg)

class LoginError(bb.Union):
    pass
# WARNING: Decompyle incomplete

LoginError_validator = bv.Union(LoginError)

class LoginResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

LoginResult_validator = bv.Union(LoginResult)

class MergeArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MergeArg_validator = bv.Struct(MergeArg)

class MergeError(bb.Union):
    pass
# WARNING: Decompyle incomplete

MergeError_validator = bv.Union(MergeError)

class MergeJobStatus(async_.PollResultBase):
    pass
# WARNING: Decompyle incomplete

MergeJobStatus_validator = bv.Union(MergeJobStatus)

class MergeResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MergeResponse_validator = bv.Struct(MergeResponse)

class MobileIntegrityToken(bb.Union):
    pass
# WARNING: Decompyle incomplete

MobileIntegrityToken_validator = bv.Union(MobileIntegrityToken)

class OneTapOperation(bb.Union):
    pass
# WARNING: Decompyle incomplete

OneTapOperation_validator = bv.Union(OneTapOperation)

class OneTapPlatform(bb.Union):
    pass
# WARNING: Decompyle incomplete

OneTapPlatform_validator = bv.Union(OneTapPlatform)

class OneTapProfile(bb.Struct):
    pass
# WARNING: Decompyle incomplete

OneTapProfile_validator = bv.Struct(OneTapProfile)

class RegisterOrSignInWith1TapAccessInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RegisterOrSignInWith1TapAccessInfo_validator = bv.Struct(RegisterOrSignInWith1TapAccessInfo)

class OneTapRequiresEnableTwoFactor(RegisterOrSignInWith1TapAccessInfo):
    pass
# WARNING: Decompyle incomplete

OneTapRequiresEnableTwoFactor_validator = bv.Struct(OneTapRequiresEnableTwoFactor)

class OneTapRequiresNotUsedSig(RegisterOrSignInWith1TapAccessInfo):
    pass
# WARNING: Decompyle incomplete

OneTapRequiresNotUsedSig_validator = bv.Struct(OneTapRequiresNotUsedSig)

class OneTapRequiresPassword(RegisterOrSignInWith1TapAccessInfo):
    pass
# WARNING: Decompyle incomplete

OneTapRequiresPassword_validator = bv.Struct(OneTapRequiresPassword)

class OneTapRequiresSso(RegisterOrSignInWith1TapAccessInfo):
    pass
# WARNING: Decompyle incomplete

OneTapRequiresSso_validator = bv.Struct(OneTapRequiresSso)

class OneTapRequiresTos(RegisterOrSignInWith1TapAccessInfo):
    pass
# WARNING: Decompyle incomplete

OneTapRequiresTos_validator = bv.Struct(OneTapRequiresTos)

class OneTapRequiresTwofactor(RegisterOrSignInWith1TapAccessInfo):
    pass
# WARNING: Decompyle incomplete

OneTapRequiresTwofactor_validator = bv.Struct(OneTapRequiresTwofactor)

class OptionalUserNameArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

OptionalUserNameArg_validator = bv.Struct(OptionalUserNameArg)

class PasswordResetArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PasswordResetArg_validator = bv.Struct(PasswordResetArg)

class PasswordResetError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PasswordResetError_validator = bv.Union(PasswordResetError)

class PhotoSourceArg(bb.Union):
    pass
# WARNING: Decompyle incomplete

PhotoSourceArg_validator = bv.Union(PhotoSourceArg)

class PromoteCancelArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PromoteCancelArg_validator = bv.Struct(PromoteCancelArg)

class PromoteCancelError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PromoteCancelError_validator = bv.Union(PromoteCancelError)

class PromoteCancelResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PromoteCancelResponse_validator = bv.Struct(PromoteCancelResponse)

class PromoteInitiateArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PromoteInitiateArg_validator = bv.Struct(PromoteInitiateArg)

class PromoteInitiateError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PromoteInitiateError_validator = bv.Union(PromoteInitiateError)

class PromoteInitiateResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PromoteInitiateResponse_validator = bv.Struct(PromoteInitiateResponse)

class PromoteResendArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PromoteResendArg_validator = bv.Struct(PromoteResendArg)

class PromoteResendError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PromoteResendError_validator = bv.Union(PromoteResendError)

class PromoteResendResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PromoteResendResponse_validator = bv.Struct(PromoteResendResponse)

class ReCaptchaRequest(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ReCaptchaRequest_validator = bv.Struct(ReCaptchaRequest)

class ReCaptchaResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ReCaptchaResponse_validator = bv.Struct(ReCaptchaResponse)

class ReanchorCancelArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ReanchorCancelArg_validator = bv.Struct(ReanchorCancelArg)

class ReanchorCancelError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ReanchorCancelError_validator = bv.Union(ReanchorCancelError)

class ReanchorCancelResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ReanchorCancelResponse_validator = bv.Struct(ReanchorCancelResponse)

class ReanchorCompleteArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ReanchorCompleteArg_validator = bv.Struct(ReanchorCompleteArg)

class ReanchorCompleteError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ReanchorCompleteError_validator = bv.Union(ReanchorCompleteError)

class ReanchorCompleteResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ReanchorCompleteResponse_validator = bv.Struct(ReanchorCompleteResponse)

class ReanchorInitiateArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ReanchorInitiateArg_validator = bv.Struct(ReanchorInitiateArg)

class ReanchorInitiateError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ReanchorInitiateError_validator = bv.Union(ReanchorInitiateError)

class ReanchorInitiateResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ReanchorInitiateResponse_validator = bv.Struct(ReanchorInitiateResponse)

class ReanchorResendArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ReanchorResendArg_validator = bv.Struct(ReanchorResendArg)

class ReanchorResendError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ReanchorResendError_validator = bv.Union(ReanchorResendError)

class ReanchorResendResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ReanchorResendResponse_validator = bv.Struct(ReanchorResendResponse)

class RegisterOrSignInWith1TapArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RegisterOrSignInWith1TapArg_validator = bv.Struct(RegisterOrSignInWith1TapArg)

class RegisterOrSignInWith1TapError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RegisterOrSignInWith1TapError_validator = bv.Union(RegisterOrSignInWith1TapError)

class RegisterOrSignInWith1TapResult(bb.Union):
    pass
# WARNING: Decompyle incomplete

RegisterOrSignInWith1TapResult_validator = bv.Union(RegisterOrSignInWith1TapResult)

class RequiresEnableTwoFactor(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RequiresEnableTwoFactor_validator = bv.Struct(RequiresEnableTwoFactor)

class RequiresPassword(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RequiresPassword_validator = bv.Struct(RequiresPassword)

class RequiresSignup(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RequiresSignup_validator = bv.Struct(RequiresSignup)

class RequiresTwofactor(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RequiresTwofactor_validator = bv.Struct(RequiresTwofactor)

class Role(bb.Union):
    pass
# WARNING: Decompyle incomplete

Role_validator = bv.Union(Role)

class SetCompanyInfoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SetCompanyInfoArg_validator = bv.Struct(SetCompanyInfoArg)

class SetCompanyInfoError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SetCompanyInfoError_validator = bv.Union(SetCompanyInfoError)

class SetProfilePhotoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SetProfilePhotoArg_validator = bv.Struct(SetProfilePhotoArg)

class SetProfilePhotoError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SetProfilePhotoError_validator = bv.Union(SetProfilePhotoError)

class SetProfilePhotoResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SetProfilePhotoResult_validator = bv.Struct(SetProfilePhotoResult)

class SetTwofactorCheckpointArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SetTwofactorCheckpointArg_validator = bv.Struct(SetTwofactorCheckpointArg)

class SetTwofactorCheckpointError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SetTwofactorCheckpointError_validator = bv.Union(SetTwofactorCheckpointError)

class SmsError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SmsError_validator = bv.Struct(SmsError)

class SmsErrorReason(bb.Union):
    pass
# WARNING: Decompyle incomplete

SmsErrorReason_validator = bv.Union(SmsErrorReason)

class ThirdPartyCheckpointToken(bb.Union):
    pass
# WARNING: Decompyle incomplete

ThirdPartyCheckpointToken_validator = bv.Union(ThirdPartyCheckpointToken)

class ThumbnailError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ThumbnailError_validator = bv.Union(ThumbnailError)

class TosSignatureRequest(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TosSignatureRequest_validator = bv.Struct(TosSignatureRequest)

class TwoFactorAuthRequest(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TwoFactorAuthRequest_validator = bv.Struct(TwoFactorAuthRequest)

class TwoFactorDeliveryMode(bb.Union):
    pass
# WARNING: Decompyle incomplete

TwoFactorDeliveryMode_validator = bv.Union(TwoFactorDeliveryMode)

class TwoFactorResendArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TwoFactorResendArg_validator = bv.Struct(TwoFactorResendArg)

class TwoFactorResendError(bb.Union):
    pass
# WARNING: Decompyle incomplete

TwoFactorResendError_validator = bv.Union(TwoFactorResendError)

class TwoFactorResendResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TwoFactorResendResult_validator = bv.Struct(TwoFactorResendResult)

class TwoFactorVerifyArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TwoFactorVerifyArg_validator = bv.Struct(TwoFactorVerifyArg)

class TwoFactorVerifyError(bb.Union):
    pass
# WARNING: Decompyle incomplete

TwoFactorVerifyError_validator = bv.Union(TwoFactorVerifyError)

class VerifyEmailGoogleArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

VerifyEmailGoogleArg_validator = bv.Struct(VerifyEmailGoogleArg)

class VerifyEmailGoogleError(bb.Union):
    pass
# WARNING: Decompyle incomplete

VerifyEmailGoogleError_validator = bv.Union(VerifyEmailGoogleError)

class VerifyEmailGoogleResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

VerifyEmailGoogleResult_validator = bv.Struct(VerifyEmailGoogleResult)
AccountUserXid_validator = bv.String()
AccountUserXid_validator._redact = bv.BlotRedactor(None)
AccessInfo.user_id.validator = bv.Int64()
AccessInfo.user_id.validator._redact = bv.BlotRedactor(None)
AccessInfo.oauth2_access_token.validator = bv.String()
AccessInfo.oauth2_access_token.validator._redact = bv.BlotRedactor(None)
AccessInfo.is_passkey_login_allowed.validator = bv.Boolean()
AccessInfo.is_passkey_login_allowed.validator._redact = bv.BlotRedactor(None)
AccessInfo._all_field_names_ = set([
    'user_id',
    'oauth2_access_token',
    'is_passkey_login_allowed'])
AccessInfo._all_fields_ = [
    ('user_id', AccessInfo.user_id.validator),
    ('oauth2_access_token', AccessInfo.oauth2_access_token.validator),
    ('is_passkey_login_allowed', AccessInfo.is_passkey_login_allowed.validator)]
AccountNameArg.first_name.validator = bv.String(min_length = 1)
AccountNameArg.first_name.validator._redact = bv.BlotRedactor(None)
AccountNameArg.last_name.validator = bv.Nullable(bv.String())
AccountNameArg._all_field_names_ = set([
    'first_name',
    'last_name'])
AccountNameArg._all_fields_ = [
    ('first_name', AccountNameArg.first_name.validator),
    ('last_name', AccountNameArg.last_name.validator)]
AccountPhotoGetArg.dbx_account_id.validator = bv.String()
AccountPhotoGetArg.dbx_account_id.validator._redact = bv.BlotRedactor(None)
AccountPhotoGetArg.size.validator = bv.String()
AccountPhotoGetArg.size.validator._redact = bv.BlotRedactor(None)
AccountPhotoGetArg.circle_crop.validator = bv.Boolean()
AccountPhotoGetArg.circle_crop.validator._redact = bv.BlotRedactor(None)
AccountPhotoGetArg.expect_account_photo.validator = bv.Boolean()
AccountPhotoGetArg.expect_account_photo.validator._redact = bv.BlotRedactor(None)
AccountPhotoGetArg._all_field_names_ = set([
    'dbx_account_id',
    'size',
    'circle_crop',
    'expect_account_photo'])
AccountPhotoGetArg._all_fields_ = [
    ('dbx_account_id', AccountPhotoGetArg.dbx_account_id.validator),
    ('size', AccountPhotoGetArg.size.validator),
    ('circle_crop', AccountPhotoGetArg.circle_crop.validator),
    ('expect_account_photo', AccountPhotoGetArg.expect_account_photo.validator)]
AccountPhotoGetError._thumbnail_error_validator = ThumbnailError_validator
AccountPhotoGetError._account_photo_missing_validator = bv.Void()
AccountPhotoGetError._expected_account_photo_missing_validator = bv.Void()
AccountPhotoGetError._other_validator = bv.Void()
AccountPhotoGetError._tagmap = {
    'thumbnail_error': AccountPhotoGetError._thumbnail_error_validator,
    'account_photo_missing': AccountPhotoGetError._account_photo_missing_validator,
    'expected_account_photo_missing': AccountPhotoGetError._expected_account_photo_missing_validator,
    'other': AccountPhotoGetError._other_validator }
AccountPhotoGetError.account_photo_missing = AccountPhotoGetError('account_photo_missing')
AccountPhotoGetError.expected_account_photo_missing = AccountPhotoGetError('expected_account_photo_missing')
AccountPhotoGetError.other = AccountPhotoGetError('other')
AccountPhotoGetResult.content_type.validator = bv.String()
AccountPhotoGetResult.content_type.validator._redact = bv.BlotRedactor(None)
AccountPhotoGetResult._all_field_names_ = set([
    'content_type'])
AccountPhotoGetResult._all_fields_ = [
    ('content_type', AccountPhotoGetResult.content_type.validator)]
ThirdPartyLoginArg.auth_code.validator = bv.String()
ThirdPartyLoginArg.auth_code.validator._redact = bv.BlotRedactor(None)
ThirdPartyLoginArg.admin_only.validator = bv.Boolean()
ThirdPartyLoginArg.admin_only.validator._redact = bv.BlotRedactor(None)
ThirdPartyLoginArg.require_role.validator = bv.Nullable(bv.Int64())
ThirdPartyLoginArg.device_info.validator = bv.Nullable(DeviceInfo_validator)
ThirdPartyLoginArg.team_emm_token.validator = bv.Nullable(bv.String())
ThirdPartyLoginArg.supports_passkey.validator = bv.Nullable(bv.Boolean())
ThirdPartyLoginArg._all_field_names_ = set([
    'auth_code',
    'admin_only',
    'require_role',
    'device_info',
    'team_emm_token',
    'supports_passkey'])
ThirdPartyLoginArg._all_fields_ = [
    ('auth_code', ThirdPartyLoginArg.auth_code.validator),
    ('admin_only', ThirdPartyLoginArg.admin_only.validator),
    ('require_role', ThirdPartyLoginArg.require_role.validator),
    ('device_info', ThirdPartyLoginArg.device_info.validator),
    ('team_emm_token', ThirdPartyLoginArg.team_emm_token.validator),
    ('supports_passkey', ThirdPartyLoginArg.supports_passkey.validator)]
AppleLoginArg.state.validator = bv.Nullable(bv.String())
AppleLoginArg.pkce_response.validator = bv.Nullable(bv.String())
AppleLoginArg.client_id.validator = bv.Nullable(bv.String())
AppleLoginArg._all_field_names_ = ThirdPartyLoginArg._all_field_names_.union(set([
    'state',
    'pkce_response',
    'client_id']))
AppleLoginArg._all_fields_ = ThirdPartyLoginArg._all_fields_ + [
    ('state', AppleLoginArg.state.validator),
    ('pkce_response', AppleLoginArg.pkce_response.validator),
    ('client_id', AppleLoginArg.client_id.validator)]
ThirdPartyLoginError._emm_validation_error_validator = EmmValidationError_validator
ThirdPartyLoginError._unauthorized_validator = bv.Void()
ThirdPartyLoginError._access_denied_validator = bv.Void()
ThirdPartyLoginError._client_account_suspended_validator = bv.Void()
ThirdPartyLoginError._client_account_deleted_validator = bv.Void()
ThirdPartyLoginError._user_device_limit_exceeded_validator = bv.Void()
ThirdPartyLoginError._other_validator = bv.Void()
ThirdPartyLoginError._tagmap = {
    'emm_validation_error': ThirdPartyLoginError._emm_validation_error_validator,
    'unauthorized': ThirdPartyLoginError._unauthorized_validator,
    'access_denied': ThirdPartyLoginError._access_denied_validator,
    'client_account_suspended': ThirdPartyLoginError._client_account_suspended_validator,
    'client_account_deleted': ThirdPartyLoginError._client_account_deleted_validator,
    'user_device_limit_exceeded': ThirdPartyLoginError._user_device_limit_exceeded_validator,
    'other': ThirdPartyLoginError._other_validator }
ThirdPartyLoginError.unauthorized = ThirdPartyLoginError('unauthorized')
ThirdPartyLoginError.access_denied = ThirdPartyLoginError('access_denied')
ThirdPartyLoginError.client_account_suspended = ThirdPartyLoginError('client_account_suspended')
ThirdPartyLoginError.client_account_deleted = ThirdPartyLoginError('client_account_deleted')
ThirdPartyLoginError.user_device_limit_exceeded = ThirdPartyLoginError('user_device_limit_exceeded')
ThirdPartyLoginError.other = ThirdPartyLoginError('other')
AppleLoginError._no_email_in_response_validator = bv.Void()
AppleLoginError._tagmap = {
    'no_email_in_response': AppleLoginError._no_email_in_response_validator }
AppleLoginError._tagmap.update(ThirdPartyLoginError._tagmap)
AppleLoginError.no_email_in_response = AppleLoginError('no_email_in_response')
ThirdPartyLoginResult._success_validator = AccessInfo_validator
ThirdPartyLoginResult._requires_twofactor_validator = RequiresTwofactor_validator
ThirdPartyLoginResult._requires_signup_validator = RequiresSignup_validator
ThirdPartyLoginResult._other_validator = bv.Void()
ThirdPartyLoginResult._tagmap = {
    'success': ThirdPartyLoginResult._success_validator,
    'requires_twofactor': ThirdPartyLoginResult._requires_twofactor_validator,
    'requires_signup': ThirdPartyLoginResult._requires_signup_validator,
    'other': ThirdPartyLoginResult._other_validator }
ThirdPartyLoginResult.other = ThirdPartyLoginResult('other')
AppleLoginResult._requires_password_on_first_link_validator = RequiresPassword_validator
AppleLoginResult._tagmap = {
    'requires_password_on_first_link': AppleLoginResult._requires_password_on_first_link_validator }
AppleLoginResult._tagmap.update(ThirdPartyLoginResult._tagmap)
ThirdPartySignupArg.source.validator = bv.Nullable(bv.String())
ThirdPartySignupArg.admin_only.validator = bv.Boolean()
ThirdPartySignupArg.admin_only.validator._redact = bv.BlotRedactor(None)
ThirdPartySignupArg.device_info.validator = bv.Nullable(DeviceInfo_validator)
ThirdPartySignupArg.marketing_opt_in.validator = bv.Boolean()
ThirdPartySignupArg.marketing_opt_in.validator._redact = bv.BlotRedactor(None)
ThirdPartySignupArg._all_field_names_ = set([
    'source',
    'admin_only',
    'device_info',
    'marketing_opt_in'])
ThirdPartySignupArg._all_fields_ = [
    ('source', ThirdPartySignupArg.source.validator),
    ('admin_only', ThirdPartySignupArg.admin_only.validator),
    ('device_info', ThirdPartySignupArg.device_info.validator),
    ('marketing_opt_in', ThirdPartySignupArg.marketing_opt_in.validator)]
AppleSignupArg.encrypted_apple_data.validator = bv.String()
AppleSignupArg.encrypted_apple_data.validator._redact = bv.BlotRedactor(None)
AppleSignupArg.real_email.validator = bv.Nullable(common.EmailAddress_validator)
AppleSignupArg.account_name.validator = bv.Nullable(OptionalUserNameArg_validator)
AppleSignupArg._all_field_names_ = ThirdPartySignupArg._all_field_names_.union(set([
    'encrypted_apple_data',
    'real_email',
    'account_name']))
AppleSignupArg._all_fields_ = ThirdPartySignupArg._all_fields_ + [
    ('encrypted_apple_data', AppleSignupArg.encrypted_apple_data.validator),
    ('real_email', AppleSignupArg.real_email.validator),
    ('account_name', AppleSignupArg.account_name.validator)]
AppleSignupError._server_error_validator = bv.Void()
AppleSignupError._email_taken_validator = bv.Void()
AppleSignupError._other_validator = bv.Void()
AppleSignupError._tagmap = {
    'server_error': AppleSignupError._server_error_validator,
    'email_taken': AppleSignupError._email_taken_validator,
    'other': AppleSignupError._other_validator }
AppleSignupError.server_error = AppleSignupError('server_error')
AppleSignupError.email_taken = AppleSignupError('email_taken')
AppleSignupError.other = AppleSignupError('other')
ThirdPartySignupResult.access_info.validator = AccessInfo_validator
ThirdPartySignupResult._all_field_names_ = set([
    'access_info'])
ThirdPartySignupResult._all_fields_ = [
    ('access_info', ThirdPartySignupResult.access_info.validator)]
AppleSignupResult._all_field_names_ = ThirdPartySignupResult._all_field_names_.union(set([]))
AppleSignupResult._all_fields_ = ThirdPartySignupResult._all_fields_ + []
AuthCredential._auth_code_validator = bv.String()
AuthCredential._auth_code_validator._redact = bv.BlotRedactor(None)
AuthCredential._other_validator = bv.Void()
AuthCredential._tagmap = {
    'auth_code': AuthCredential._auth_code_validator,
    'other': AuthCredential._other_validator }
AuthCredential.other = AuthCredential('other')
ChangeEmailInitiateArg.sub_account_id.validator = bv.Nullable(AccountUserXid_validator)
ChangeEmailInitiateArg.new_email.validator = bv.Nullable(common.EmailAddress_validator)
ChangeEmailInitiateArg._all_field_names_ = set([
    'sub_account_id',
    'new_email'])
ChangeEmailInitiateArg._all_fields_ = [
    ('sub_account_id', ChangeEmailInitiateArg.sub_account_id.validator),
    ('new_email', ChangeEmailInitiateArg.new_email.validator)]
ChangeEmailInitiateError._invalid_email_validator = bv.Void()
ChangeEmailInitiateError._not_allowed_validator = bv.Void()
ChangeEmailInitiateError._other_validator = bv.Void()
ChangeEmailInitiateError._tagmap = {
    'invalid_email': ChangeEmailInitiateError._invalid_email_validator,
    'not_allowed': ChangeEmailInitiateError._not_allowed_validator,
    'other': ChangeEmailInitiateError._other_validator }
ChangeEmailInitiateError.invalid_email = ChangeEmailInitiateError('invalid_email')
ChangeEmailInitiateError.not_allowed = ChangeEmailInitiateError('not_allowed')
ChangeEmailInitiateError.other = ChangeEmailInitiateError('other')
ChangeEmailInitiateResponse.change_email_type.validator = ChangeEmailType_validator
ChangeEmailInitiateResponse.pending_email.validator = bv.String()
ChangeEmailInitiateResponse.pending_email.validator._redact = bv.BlotRedactor(None)
ChangeEmailInitiateResponse._all_field_names_ = set([
    'change_email_type',
    'pending_email'])
ChangeEmailInitiateResponse._all_fields_ = [
    ('change_email_type', ChangeEmailInitiateResponse.change_email_type.validator),
    ('pending_email', ChangeEmailInitiateResponse.pending_email.validator)]
ChangeEmailType._change_email_type_unknown_validator = bv.Void()
ChangeEmailType._change_email_type_promote_validator = bv.Void()
ChangeEmailType._change_email_type_reanchor_validator = bv.Void()
ChangeEmailType._other_validator = bv.Void()
ChangeEmailType._tagmap = {
    'change_email_type_unknown': ChangeEmailType._change_email_type_unknown_validator,
    'change_email_type_promote': ChangeEmailType._change_email_type_promote_validator,
    'change_email_type_reanchor': ChangeEmailType._change_email_type_reanchor_validator,
    'other': ChangeEmailType._other_validator }
ChangeEmailType.change_email_type_unknown = ChangeEmailType('change_email_type_unknown')
ChangeEmailType.change_email_type_promote = ChangeEmailType('change_email_type_promote')
ChangeEmailType.change_email_type_reanchor = ChangeEmailType('change_email_type_reanchor')
ChangeEmailType.other = ChangeEmailType('other')
ChangeNameError._first_name_invalid_validator = bv.Void()
ChangeNameError._last_name_invalid_validator = bv.Void()
ChangeNameError._other_validator = bv.Void()
ChangeNameError._tagmap = {
    'first_name_invalid': ChangeNameError._first_name_invalid_validator,
    'last_name_invalid': ChangeNameError._last_name_invalid_validator,
    'other': ChangeNameError._other_validator }
ChangeNameError.first_name_invalid = ChangeNameError('first_name_invalid')
ChangeNameError.last_name_invalid = ChangeNameError('last_name_invalid')
ChangeNameError.other = ChangeNameError('other')
CheckPasswordlessStateArg.email.validator = common.EmailAddress_validator
CheckPasswordlessStateArg.team_emm_token.validator = bv.Nullable(bv.String())
CheckPasswordlessStateArg._all_field_names_ = set([
    'email',
    'team_emm_token'])
CheckPasswordlessStateArg._all_fields_ = [
    ('email', CheckPasswordlessStateArg.email.validator),
    ('team_emm_token', CheckPasswordlessStateArg.team_emm_token.validator)]
CheckPasswordlessStateError._emm_validation_error_validator = EmmValidationError_validator
CheckPasswordlessStateError._other_validator = bv.Void()
CheckPasswordlessStateError._tagmap = {
    'emm_validation_error': CheckPasswordlessStateError._emm_validation_error_validator,
    'other': CheckPasswordlessStateError._other_validator }
CheckPasswordlessStateError.other = CheckPasswordlessStateError('other')
CheckPaswordlessStateResult.user_sso_state.validator = bv.String()
CheckPaswordlessStateResult.user_sso_state.validator._redact = bv.BlotRedactor(None)
CheckPaswordlessStateResult.third_party.validator = bv.String()
CheckPaswordlessStateResult.third_party.validator._redact = bv.BlotRedactor(None)
CheckPaswordlessStateResult.third_party_logins.validator = bv.Nullable(bv.List(bv.String()))
CheckPaswordlessStateResult.third_party_logins.validator._redact = bv.BlotRedactor(None)
CheckPaswordlessStateResult._all_field_names_ = set([
    'user_sso_state',
    'third_party',
    'third_party_logins'])
CheckPaswordlessStateResult._all_fields_ = [
    ('user_sso_state', CheckPaswordlessStateResult.user_sso_state.validator),
    ('third_party', CheckPaswordlessStateResult.third_party.validator),
    ('third_party_logins', CheckPaswordlessStateResult.third_party_logins.validator)]
CheckUserWithEmailExistsArg.email.validator = common.EmailAddress_validator
CheckUserWithEmailExistsArg._all_field_names_ = set([
    'email'])
CheckUserWithEmailExistsArg._all_fields_ = [
    ('email', CheckUserWithEmailExistsArg.email.validator)]
CheckUserWithEmailExistsError._other_validator = bv.Void()
CheckUserWithEmailExistsError._tagmap = {
    'other': CheckUserWithEmailExistsError._other_validator }
CheckUserWithEmailExistsError.other = CheckUserWithEmailExistsError('other')
CheckUserWithEmailExistsResult.exists.validator = bv.Boolean()
CheckUserWithEmailExistsResult.exists.validator._redact = bv.BlotRedactor(None)
CheckUserWithEmailExistsResult.has_passkey.validator = bv.Boolean()
CheckUserWithEmailExistsResult.has_passkey.validator._redact = bv.BlotRedactor(None)
CheckUserWithEmailExistsResult.exists_as_recovery_email.validator = bv.Boolean()
CheckUserWithEmailExistsResult.exists_as_recovery_email.validator._redact = bv.BlotRedactor(None)
CheckUserWithEmailExistsResult._all_field_names_ = set([
    'exists',
    'has_passkey',
    'exists_as_recovery_email'])
CheckUserWithEmailExistsResult._all_fields_ = [
    ('exists', CheckUserWithEmailExistsResult.exists.validator),
    ('has_passkey', CheckUserWithEmailExistsResult.has_passkey.validator),
    ('exists_as_recovery_email', CheckUserWithEmailExistsResult.exists_as_recovery_email.validator)]
CompanyInfoResult.company_name.validator = bv.Nullable(bv.String())
CompanyInfoResult.company_size_id.validator = bv.Nullable(bv.Int64())
CompanyInfoResult.company_role.validator = bv.Nullable(bv.String())
CompanyInfoResult._all_field_names_ = set([
    'company_name',
    'company_size_id',
    'company_role'])
CompanyInfoResult._all_fields_ = [
    ('company_name', CompanyInfoResult.company_name.validator),
    ('company_size_id', CompanyInfoResult.company_size_id.validator),
    ('company_role', CompanyInfoResult.company_role.validator)]
CompleteRegistrationArg.first_name.validator = bv.String()
CompleteRegistrationArg.first_name.validator._redact = bv.BlotRedactor(None)
CompleteRegistrationArg.last_name.validator = bv.String()
CompleteRegistrationArg.last_name.validator._redact = bv.BlotRedactor(None)
CompleteRegistrationArg.tos_agree.validator = bv.Boolean()
CompleteRegistrationArg.tos_agree.validator._redact = bv.BlotRedactor(None)
CompleteRegistrationArg.remember_me.validator = bv.Boolean()
CompleteRegistrationArg.remember_me.validator._redact = bv.BlotRedactor(None)
CompleteRegistrationArg.finish_web_auth.validator = bv.Boolean()
CompleteRegistrationArg.finish_web_auth.validator._redact = bv.BlotRedactor(None)
CompleteRegistrationArg.ownership_proof.validator = bv.Nullable(bv.String())
CompleteRegistrationArg.password.validator = bv.Nullable(bv.String())
CompleteRegistrationArg._all_field_names_ = set([
    'first_name',
    'last_name',
    'tos_agree',
    'remember_me',
    'finish_web_auth',
    'ownership_proof',
    'password'])
CompleteRegistrationArg._all_fields_ = [
    ('first_name', CompleteRegistrationArg.first_name.validator),
    ('last_name', CompleteRegistrationArg.last_name.validator),
    ('tos_agree', CompleteRegistrationArg.tos_agree.validator),
    ('remember_me', CompleteRegistrationArg.remember_me.validator),
    ('finish_web_auth', CompleteRegistrationArg.finish_web_auth.validator),
    ('ownership_proof', CompleteRegistrationArg.ownership_proof.validator),
    ('password', CompleteRegistrationArg.password.validator)]
CompleteRegistrationError._account_invalid_validator = bv.Void()
CompleteRegistrationError._ownership_proof_invalid_validator = bv.Void()
CompleteRegistrationError._first_name_invalid_validator = bv.Void()
CompleteRegistrationError._last_name_invalid_validator = bv.Void()
CompleteRegistrationError._tos_invalid_validator = bv.Void()
CompleteRegistrationError._password_invalid_validator = bv.Void()
CompleteRegistrationError._other_validator = bv.Void()
CompleteRegistrationError._tagmap = {
    'account_invalid': CompleteRegistrationError._account_invalid_validator,
    'ownership_proof_invalid': CompleteRegistrationError._ownership_proof_invalid_validator,
    'first_name_invalid': CompleteRegistrationError._first_name_invalid_validator,
    'last_name_invalid': CompleteRegistrationError._last_name_invalid_validator,
    'tos_invalid': CompleteRegistrationError._tos_invalid_validator,
    'password_invalid': CompleteRegistrationError._password_invalid_validator,
    'other': CompleteRegistrationError._other_validator }
CompleteRegistrationError.account_invalid = CompleteRegistrationError('account_invalid')
CompleteRegistrationError.ownership_proof_invalid = CompleteRegistrationError('ownership_proof_invalid')
CompleteRegistrationError.first_name_invalid = CompleteRegistrationError('first_name_invalid')
CompleteRegistrationError.last_name_invalid = CompleteRegistrationError('last_name_invalid')
CompleteRegistrationError.tos_invalid = CompleteRegistrationError('tos_invalid')
CompleteRegistrationError.password_invalid = CompleteRegistrationError('password_invalid')
CompleteRegistrationError.other = CompleteRegistrationError('other')
CompleteRegistrationResult.complete_registration_result.validator = bv.Nullable(CompleteRegistrationResultUnion_validator)
CompleteRegistrationResult._all_field_names_ = set([
    'complete_registration_result'])
CompleteRegistrationResult._all_fields_ = [
    ('complete_registration_result', CompleteRegistrationResult.complete_registration_result.validator)]
CompleteRegistrationResultUnion._success_validator = bv.Void()
CompleteRegistrationResultUnion._tfa_required_validator = bv.Void()
CompleteRegistrationResultUnion._tfa_setup_required_validator = bv.Void()
CompleteRegistrationResultUnion._other_validator = bv.Void()
CompleteRegistrationResultUnion._tagmap = {
    'success': CompleteRegistrationResultUnion._success_validator,
    'tfa_required': CompleteRegistrationResultUnion._tfa_required_validator,
    'tfa_setup_required': CompleteRegistrationResultUnion._tfa_setup_required_validator,
    'other': CompleteRegistrationResultUnion._other_validator }
CompleteRegistrationResultUnion.success = CompleteRegistrationResultUnion('success')
CompleteRegistrationResultUnion.tfa_required = CompleteRegistrationResultUnion('tfa_required')
CompleteRegistrationResultUnion.tfa_setup_required = CompleteRegistrationResultUnion('tfa_setup_required')
CompleteRegistrationResultUnion.other = CompleteRegistrationResultUnion('other')
CreateAccountArg.email.validator = common.EmailAddress_validator
CreateAccountArg.password.validator = bv.String(min_length = 1)
CreateAccountArg.password.validator._redact = bv.BlotRedactor(None)
CreateAccountArg.source.validator = bv.Nullable(bv.String())
CreateAccountArg.captcha.validator = bv.Nullable(ReCaptchaResponse_validator)
CreateAccountArg.mobile_integrity_token.validator = bv.Nullable(MobileIntegrityToken_validator)
CreateAccountArg.marketing_opt_in.validator = bv.Boolean()
CreateAccountArg.marketing_opt_in.validator._redact = bv.BlotRedactor(None)
CreateAccountArg.device_info.validator = bv.Nullable(DeviceInfo_validator)
CreateAccountArg._all_field_names_ = AccountNameArg._all_field_names_.union(set([
    'email',
    'password',
    'source',
    'captcha',
    'mobile_integrity_token',
    'marketing_opt_in',
    'device_info']))
CreateAccountArg._all_fields_ = AccountNameArg._all_fields_ + [
    ('email', CreateAccountArg.email.validator),
    ('password', CreateAccountArg.password.validator),
    ('source', CreateAccountArg.source.validator),
    ('captcha', CreateAccountArg.captcha.validator),
    ('mobile_integrity_token', CreateAccountArg.mobile_integrity_token.validator),
    ('marketing_opt_in', CreateAccountArg.marketing_opt_in.validator),
    ('device_info', CreateAccountArg.device_info.validator)]
CreateAccountError._email_invalid_validator = EmailInvalidError_validator
CreateAccountError._first_name_invalid_validator = bv.Void()
CreateAccountError._last_name_invalid_validator = bv.Void()
CreateAccountError._password_invalid_validator = bv.Void()
CreateAccountError._other_validator = bv.Void()
CreateAccountError._tagmap = {
    'email_invalid': CreateAccountError._email_invalid_validator,
    'first_name_invalid': CreateAccountError._first_name_invalid_validator,
    'last_name_invalid': CreateAccountError._last_name_invalid_validator,
    'password_invalid': CreateAccountError._password_invalid_validator,
    'other': CreateAccountError._other_validator }
CreateAccountError.first_name_invalid = CreateAccountError('first_name_invalid')
CreateAccountError.last_name_invalid = CreateAccountError('last_name_invalid')
CreateAccountError.password_invalid = CreateAccountError('password_invalid')
CreateAccountError.other = CreateAccountError('other')
CreateAccountResult._success_validator = AccessInfo_validator
CreateAccountResult._requires_captcha_validator = ReCaptchaRequest_validator
CreateAccountResult._other_validator = bv.Void()
CreateAccountResult._tagmap = {
    'success': CreateAccountResult._success_validator,
    'requires_captcha': CreateAccountResult._requires_captcha_validator,
    'other': CreateAccountResult._other_validator }
CreateAccountResult.other = CreateAccountResult('other')
CreateOrLinkAccountWithIdpArg.email.validator = common.EmailAddress_validator
CreateOrLinkAccountWithIdpArg.email_verified.validator = bv.Boolean()
CreateOrLinkAccountWithIdpArg.email_verified.validator._redact = bv.BlotRedactor(None)
CreateOrLinkAccountWithIdpArg.extra_info.validator = bv.Nullable(bv.Map(bv.String(), bv.String()))
CreateOrLinkAccountWithIdpArg._all_field_names_ = AccountNameArg._all_field_names_.union(set([
    'email',
    'email_verified',
    'extra_info']))
CreateOrLinkAccountWithIdpArg._all_fields_ = AccountNameArg._all_fields_ + [
    ('email', CreateOrLinkAccountWithIdpArg.email.validator),
    ('email_verified', CreateOrLinkAccountWithIdpArg.email_verified.validator),
    ('extra_info', CreateOrLinkAccountWithIdpArg.extra_info.validator)]
CreateOrLinkAccountWithIdpError._email_invalid_validator = bv.Void()
CreateOrLinkAccountWithIdpError._email_unverified_validator = bv.Void()
CreateOrLinkAccountWithIdpError._require_interaction_validator = bv.Void()
CreateOrLinkAccountWithIdpError._register_idp_not_allowed_validator = bv.Void()
CreateOrLinkAccountWithIdpError._auth_invalid_validator = bv.Void()
CreateOrLinkAccountWithIdpError._first_name_invalid_validator = bv.Void()
CreateOrLinkAccountWithIdpError._last_name_invalid_validator = bv.Void()
CreateOrLinkAccountWithIdpError._register_idp_not_supported_validator = bv.Void()
CreateOrLinkAccountWithIdpError._tos_not_accepted_validator = bv.Void()
CreateOrLinkAccountWithIdpError._other_validator = bv.Void()
CreateOrLinkAccountWithIdpError._tagmap = {
    'email_invalid': CreateOrLinkAccountWithIdpError._email_invalid_validator,
    'email_unverified': CreateOrLinkAccountWithIdpError._email_unverified_validator,
    'require_interaction': CreateOrLinkAccountWithIdpError._require_interaction_validator,
    'register_idp_not_allowed': CreateOrLinkAccountWithIdpError._register_idp_not_allowed_validator,
    'auth_invalid': CreateOrLinkAccountWithIdpError._auth_invalid_validator,
    'first_name_invalid': CreateOrLinkAccountWithIdpError._first_name_invalid_validator,
    'last_name_invalid': CreateOrLinkAccountWithIdpError._last_name_invalid_validator,
    'register_idp_not_supported': CreateOrLinkAccountWithIdpError._register_idp_not_supported_validator,
    'tos_not_accepted': CreateOrLinkAccountWithIdpError._tos_not_accepted_validator,
    'other': CreateOrLinkAccountWithIdpError._other_validator }
CreateOrLinkAccountWithIdpError.email_invalid = CreateOrLinkAccountWithIdpError('email_invalid')
CreateOrLinkAccountWithIdpError.email_unverified = CreateOrLinkAccountWithIdpError('email_unverified')
CreateOrLinkAccountWithIdpError.require_interaction = CreateOrLinkAccountWithIdpError('require_interaction')
CreateOrLinkAccountWithIdpError.register_idp_not_allowed = CreateOrLinkAccountWithIdpError('register_idp_not_allowed')
CreateOrLinkAccountWithIdpError.auth_invalid = CreateOrLinkAccountWithIdpError('auth_invalid')
CreateOrLinkAccountWithIdpError.first_name_invalid = CreateOrLinkAccountWithIdpError('first_name_invalid')
CreateOrLinkAccountWithIdpError.last_name_invalid = CreateOrLinkAccountWithIdpError('last_name_invalid')
CreateOrLinkAccountWithIdpError.register_idp_not_supported = CreateOrLinkAccountWithIdpError('register_idp_not_supported')
CreateOrLinkAccountWithIdpError.tos_not_accepted = CreateOrLinkAccountWithIdpError('tos_not_accepted')
CreateOrLinkAccountWithIdpError.other = CreateOrLinkAccountWithIdpError('other')
CreateOrLinkAccountWithIdpResult.external_customer_id.validator = bv.String()
CreateOrLinkAccountWithIdpResult.external_customer_id.validator._redact = bv.BlotRedactor(None)
CreateOrLinkAccountWithIdpResult.oauth2_access_token.validator = bv.Nullable(bv.String())
CreateOrLinkAccountWithIdpResult._all_field_names_ = set([
    'external_customer_id',
    'oauth2_access_token'])
CreateOrLinkAccountWithIdpResult._all_fields_ = [
    ('external_customer_id', CreateOrLinkAccountWithIdpResult.external_customer_id.validator),
    ('oauth2_access_token', CreateOrLinkAccountWithIdpResult.oauth2_access_token.validator)]
DeleteAccountArg.email.validator = common.EmailAddress_validator
DeleteAccountArg.password.validator = bv.Nullable(bv.String())
DeleteAccountArg.reason.validator = DeleteAccountReasonUnion_validator
DeleteAccountArg.additional_info.validator = bv.String()
DeleteAccountArg.additional_info.validator._redact = bv.BlotRedactor(None)
DeleteAccountArg.encrypted_password.validator = bv.Nullable(bv.Bytes())
DeleteAccountArg.idp_auth_code.validator = bv.Nullable(IdpAuthCode_validator)
DeleteAccountArg._all_field_names_ = set([
    'email',
    'password',
    'reason',
    'additional_info',
    'encrypted_password',
    'idp_auth_code'])
DeleteAccountArg._all_fields_ = [
    ('email', DeleteAccountArg.email.validator),
    ('password', DeleteAccountArg.password.validator),
    ('reason', DeleteAccountArg.reason.validator),
    ('additional_info', DeleteAccountArg.additional_info.validator),
    ('encrypted_password', DeleteAccountArg.encrypted_password.validator),
    ('idp_auth_code', DeleteAccountArg.idp_auth_code.validator)]
DeleteAccountError._auth_failed_validator = bv.Void()
DeleteAccountError._rate_limit_exceeded_validator = bv.Void()
DeleteAccountError._not_allowed_validator = bv.Void()
DeleteAccountError._invalid_reason_validator = bv.Void()
DeleteAccountError._revoke_token_failed_validator = bv.Void()
DeleteAccountError._other_validator = bv.Void()
DeleteAccountError._tagmap = {
    'auth_failed': DeleteAccountError._auth_failed_validator,
    'rate_limit_exceeded': DeleteAccountError._rate_limit_exceeded_validator,
    'not_allowed': DeleteAccountError._not_allowed_validator,
    'invalid_reason': DeleteAccountError._invalid_reason_validator,
    'revoke_token_failed': DeleteAccountError._revoke_token_failed_validator,
    'other': DeleteAccountError._other_validator }
DeleteAccountError.auth_failed = DeleteAccountError('auth_failed')
DeleteAccountError.rate_limit_exceeded = DeleteAccountError('rate_limit_exceeded')
DeleteAccountError.not_allowed = DeleteAccountError('not_allowed')
DeleteAccountError.invalid_reason = DeleteAccountError('invalid_reason')
DeleteAccountError.revoke_token_failed = DeleteAccountError('revoke_token_failed')
DeleteAccountError.other = DeleteAccountError('other')
DeleteAccountReasonUnion._unused_extra_space_validator = bv.Void()
DeleteAccountReasonUnion._unused_service_validator = bv.Void()
DeleteAccountReasonUnion._better_alternative_validator = bv.Void()
DeleteAccountReasonUnion._tech_issues_validator = bv.Void()
DeleteAccountReasonUnion._ease_of_use_validator = bv.Void()
DeleteAccountReasonUnion._expensive_validator = bv.Void()
DeleteAccountReasonUnion._missing_features_validator = bv.Void()
DeleteAccountReasonUnion._other_reason_validator = bv.Void()
DeleteAccountReasonUnion._other_validator = bv.Void()
DeleteAccountReasonUnion._tagmap = {
    'unused_extra_space': DeleteAccountReasonUnion._unused_extra_space_validator,
    'unused_service': DeleteAccountReasonUnion._unused_service_validator,
    'better_alternative': DeleteAccountReasonUnion._better_alternative_validator,
    'tech_issues': DeleteAccountReasonUnion._tech_issues_validator,
    'ease_of_use': DeleteAccountReasonUnion._ease_of_use_validator,
    'expensive': DeleteAccountReasonUnion._expensive_validator,
    'missing_features': DeleteAccountReasonUnion._missing_features_validator,
    'other_reason': DeleteAccountReasonUnion._other_reason_validator,
    'other': DeleteAccountReasonUnion._other_validator }
DeleteAccountReasonUnion.unused_extra_space = DeleteAccountReasonUnion('unused_extra_space')
DeleteAccountReasonUnion.unused_service = DeleteAccountReasonUnion('unused_service')
DeleteAccountReasonUnion.better_alternative = DeleteAccountReasonUnion('better_alternative')
DeleteAccountReasonUnion.tech_issues = DeleteAccountReasonUnion('tech_issues')
DeleteAccountReasonUnion.ease_of_use = DeleteAccountReasonUnion('ease_of_use')
DeleteAccountReasonUnion.expensive = DeleteAccountReasonUnion('expensive')
DeleteAccountReasonUnion.missing_features = DeleteAccountReasonUnion('missing_features')
DeleteAccountReasonUnion.other_reason = DeleteAccountReasonUnion('other_reason')
DeleteAccountReasonUnion.other = DeleteAccountReasonUnion('other')
DeleteAccountResult.success.validator = bv.Boolean()
DeleteAccountResult.success.validator._redact = bv.BlotRedactor(None)
DeleteAccountResult._all_field_names_ = set([
    'success'])
DeleteAccountResult._all_fields_ = [
    ('success', DeleteAccountResult.success.validator)]
DeleteArg.sub_account_id.validator = bv.Nullable(AccountUserXid_validator)
DeleteArg._all_field_names_ = set([
    'sub_account_id'])
DeleteArg._all_fields_ = [
    ('sub_account_id', DeleteArg.sub_account_id.validator)]
DeleteCompanyInfoArg.company_info_keys.validator = bv.List(bv.String())
DeleteCompanyInfoArg.company_info_keys.validator._redact = bv.BlotRedactor(None)
DeleteCompanyInfoArg._all_field_names_ = set([
    'company_info_keys'])
DeleteCompanyInfoArg._all_fields_ = [
    ('company_info_keys', DeleteCompanyInfoArg.company_info_keys.validator)]
DeleteCompanyInfoError._company_info_key_invalid_validator = bv.Void()
DeleteCompanyInfoError._company_info_entity_missing_error_validator = bv.Void()
DeleteCompanyInfoError._other_validator = bv.Void()
DeleteCompanyInfoError._tagmap = {
    'company_info_key_invalid': DeleteCompanyInfoError._company_info_key_invalid_validator,
    'company_info_entity_missing_error': DeleteCompanyInfoError._company_info_entity_missing_error_validator,
    'other': DeleteCompanyInfoError._other_validator }
DeleteCompanyInfoError.company_info_key_invalid = DeleteCompanyInfoError('company_info_key_invalid')
DeleteCompanyInfoError.company_info_entity_missing_error = DeleteCompanyInfoError('company_info_entity_missing_error')
DeleteCompanyInfoError.other = DeleteCompanyInfoError('other')
DeleteError._account_not_found_validator = bv.Void()
DeleteError._delete_not_allowed_validator = bv.Void()
DeleteError._other_validator = bv.Void()
DeleteError._tagmap = {
    'account_not_found': DeleteError._account_not_found_validator,
    'delete_not_allowed': DeleteError._delete_not_allowed_validator,
    'other': DeleteError._other_validator }
DeleteError.account_not_found = DeleteError('account_not_found')
DeleteError.delete_not_allowed = DeleteError('delete_not_allowed')
DeleteError.other = DeleteError('other')
DeleteProfilePhotoArg._all_field_names_ = set([])
DeleteProfilePhotoArg._all_fields_ = []
DeleteProfilePhotoError._other_validator = bv.Void()
DeleteProfilePhotoError._tagmap = {
    'other': DeleteProfilePhotoError._other_validator }
DeleteProfilePhotoError.other = DeleteProfilePhotoError('other')
DeleteProfilePhotoResult._all_field_names_ = set([])
DeleteProfilePhotoResult._all_fields_ = []
DeleteResponse._all_field_names_ = set([])
DeleteResponse._all_fields_ = []
DeviceInfo.device_id.validator = bv.Nullable(bv.String())
DeviceInfo.device_name.validator = bv.Nullable(bv.String())
DeviceInfo.carrier.validator = bv.Nullable(bv.String())
DeviceInfo.client_locale.validator = bv.Nullable(bv.String())
DeviceInfo.app_version.validator = bv.Nullable(bv.String())
DeviceInfo.sys_model.validator = bv.Nullable(bv.String())
DeviceInfo.sys_version.validator = bv.Nullable(bv.String())
DeviceInfo._all_field_names_ = set([
    'device_id',
    'device_name',
    'carrier',
    'client_locale',
    'app_version',
    'sys_model',
    'sys_version'])
DeviceInfo._all_fields_ = [
    ('device_id', DeviceInfo.device_id.validator),
    ('device_name', DeviceInfo.device_name.validator),
    ('carrier', DeviceInfo.carrier.validator),
    ('client_locale', DeviceInfo.client_locale.validator),
    ('app_version', DeviceInfo.app_version.validator),
    ('sys_model', DeviceInfo.sys_model.validator),
    ('sys_version', DeviceInfo.sys_version.validator)]
EmailInvalidError._already_taken_validator = bv.Void()
EmailInvalidError._invalid_validator = bv.Void()
EmailInvalidError._other_validator = bv.Void()
EmailInvalidError._tagmap = {
    'already_taken': EmailInvalidError._already_taken_validator,
    'invalid': EmailInvalidError._invalid_validator,
    'other': EmailInvalidError._other_validator }
EmailInvalidError.already_taken = EmailInvalidError('already_taken')
EmailInvalidError.invalid = EmailInvalidError('invalid')
EmailInvalidError.other = EmailInvalidError('other')
EmmValidationError._emm_validation_failure_validator = bv.Void()
EmmValidationError._emm_not_available_for_team_validator = bv.Void()
EmmValidationError._personal_user_with_emm_token_validator = bv.Void()
EmmValidationError._team_emm_token_required_validator = bv.Void()
EmmValidationError._team_emm_token_not_required_validator = bv.Void()
EmmValidationError._wrong_team_emm_token_validator = bv.Void()
EmmValidationError._other_validator = bv.Void()
EmmValidationError._tagmap = {
    'emm_validation_failure': EmmValidationError._emm_validation_failure_validator,
    'emm_not_available_for_team': EmmValidationError._emm_not_available_for_team_validator,
    'personal_user_with_emm_token': EmmValidationError._personal_user_with_emm_token_validator,
    'team_emm_token_required': EmmValidationError._team_emm_token_required_validator,
    'team_emm_token_not_required': EmmValidationError._team_emm_token_not_required_validator,
    'wrong_team_emm_token': EmmValidationError._wrong_team_emm_token_validator,
    'other': EmmValidationError._other_validator }
EmmValidationError.emm_validation_failure = EmmValidationError('emm_validation_failure')
EmmValidationError.emm_not_available_for_team = EmmValidationError('emm_not_available_for_team')
EmmValidationError.personal_user_with_emm_token = EmmValidationError('personal_user_with_emm_token')
EmmValidationError.team_emm_token_required = EmmValidationError('team_emm_token_required')
EmmValidationError.team_emm_token_not_required = EmmValidationError('team_emm_token_not_required')
EmmValidationError.wrong_team_emm_token = EmmValidationError('wrong_team_emm_token')
EmmValidationError.other = EmmValidationError('other')
ForeignUserType._hellosign_user_validator = bv.Void()
ForeignUserType._other_validator = bv.Void()
ForeignUserType._tagmap = {
    'hellosign_user': ForeignUserType._hellosign_user_validator,
    'other': ForeignUserType._other_validator }
ForeignUserType.hellosign_user = ForeignUserType('hellosign_user')
ForeignUserType.other = ForeignUserType('other')
GetCompanyInfoError._no_company_info_validator = bv.Void()
GetCompanyInfoError._other_validator = bv.Void()
GetCompanyInfoError._tagmap = {
    'no_company_info': GetCompanyInfoError._no_company_info_validator,
    'other': GetCompanyInfoError._other_validator }
GetCompanyInfoError.no_company_info = GetCompanyInfoError('no_company_info')
GetCompanyInfoError.other = GetCompanyInfoError('other')
GetOrCreateForeignUserArgs.foreign_user_type.validator = ForeignUserType_validator
GetOrCreateForeignUserArgs.merge_existing_account.validator = bv.Boolean()
GetOrCreateForeignUserArgs.merge_existing_account.validator._redact = bv.BlotRedactor(None)
GetOrCreateForeignUserArgs._all_field_names_ = set([
    'foreign_user_type',
    'merge_existing_account'])
GetOrCreateForeignUserArgs._all_fields_ = [
    ('foreign_user_type', GetOrCreateForeignUserArgs.foreign_user_type.validator),
    ('merge_existing_account', GetOrCreateForeignUserArgs.merge_existing_account.validator)]
GetOrCreateForeignUserError._has_account_conflict_validator = bv.Void()
GetOrCreateForeignUserError._internal_error_validator = bv.Void()
GetOrCreateForeignUserError._dropbox_managed_team_can_not_be_provisioned_validator = bv.Void()
GetOrCreateForeignUserError._dropbox_managed_user_can_not_be_provisioned_validator = bv.Void()
GetOrCreateForeignUserError._other_validator = bv.Void()
GetOrCreateForeignUserError._tagmap = {
    'has_account_conflict': GetOrCreateForeignUserError._has_account_conflict_validator,
    'internal_error': GetOrCreateForeignUserError._internal_error_validator,
    'dropbox_managed_team_can_not_be_provisioned': GetOrCreateForeignUserError._dropbox_managed_team_can_not_be_provisioned_validator,
    'dropbox_managed_user_can_not_be_provisioned': GetOrCreateForeignUserError._dropbox_managed_user_can_not_be_provisioned_validator,
    'other': GetOrCreateForeignUserError._other_validator }
GetOrCreateForeignUserError.has_account_conflict = GetOrCreateForeignUserError('has_account_conflict')
GetOrCreateForeignUserError.internal_error = GetOrCreateForeignUserError('internal_error')
GetOrCreateForeignUserError.dropbox_managed_team_can_not_be_provisioned = GetOrCreateForeignUserError('dropbox_managed_team_can_not_be_provisioned')
GetOrCreateForeignUserError.dropbox_managed_user_can_not_be_provisioned = GetOrCreateForeignUserError('dropbox_managed_user_can_not_be_provisioned')
GetOrCreateForeignUserError.other = GetOrCreateForeignUserError('other')
GetOrCreateForeignUserResult.foreign_user_id.validator = bv.String()
GetOrCreateForeignUserResult.foreign_user_id.validator._redact = bv.BlotRedactor(None)
GetOrCreateForeignUserResult.foreign_user_type.validator = ForeignUserType_validator
GetOrCreateForeignUserResult._all_field_names_ = set([
    'foreign_user_id',
    'foreign_user_type'])
GetOrCreateForeignUserResult._all_fields_ = [
    ('foreign_user_id', GetOrCreateForeignUserResult.foreign_user_id.validator),
    ('foreign_user_type', GetOrCreateForeignUserResult.foreign_user_type.validator)]
GoogleLoginArg._all_field_names_ = ThirdPartyLoginArg._all_field_names_.union(set([]))
GoogleLoginArg._all_fields_ = ThirdPartyLoginArg._all_fields_ + []
GoogleLoginError._tagmap = { }
GoogleLoginError._tagmap.update(ThirdPartyLoginError._tagmap)
GoogleLoginResult._requires_password_validator = RequiresPassword_validator
GoogleLoginResult._tagmap = {
    'requires_password': GoogleLoginResult._requires_password_validator }
GoogleLoginResult._tagmap.update(ThirdPartyLoginResult._tagmap)
GoogleSignupArg.auth_arg.validator = GoogleSignupAuthArg_validator
GoogleSignupArg._all_field_names_ = ThirdPartySignupArg._all_field_names_.union(set([
    'auth_arg']))
GoogleSignupArg._all_fields_ = ThirdPartySignupArg._all_fields_ + [
    ('auth_arg', GoogleSignupArg.auth_arg.validator)]
GoogleSignupAuthArg._auth_code_validator = bv.String()
GoogleSignupAuthArg._auth_code_validator._redact = bv.BlotRedactor(None)
GoogleSignupAuthArg._encrypted_google_data_validator = bv.String()
GoogleSignupAuthArg._encrypted_google_data_validator._redact = bv.BlotRedactor(None)
GoogleSignupAuthArg._other_validator = bv.Void()
GoogleSignupAuthArg._tagmap = {
    'auth_code': GoogleSignupAuthArg._auth_code_validator,
    'encrypted_google_data': GoogleSignupAuthArg._encrypted_google_data_validator,
    'other': GoogleSignupAuthArg._other_validator }
GoogleSignupAuthArg.other = GoogleSignupAuthArg('other')
GoogleSignupError._server_error_validator = bv.Void()
GoogleSignupError._email_taken_validator = bv.Void()
GoogleSignupError._other_validator = bv.Void()
GoogleSignupError._tagmap = {
    'server_error': GoogleSignupError._server_error_validator,
    'email_taken': GoogleSignupError._email_taken_validator,
    'other': GoogleSignupError._other_validator }
GoogleSignupError.server_error = GoogleSignupError('server_error')
GoogleSignupError.email_taken = GoogleSignupError('email_taken')
GoogleSignupError.other = GoogleSignupError('other')
GoogleSignupResult._all_field_names_ = ThirdPartySignupResult._all_field_names_.union(set([]))
GoogleSignupResult._all_fields_ = ThirdPartySignupResult._all_fields_ + []
IdpAuthCode._apple_auth_code_validator = bv.String()
IdpAuthCode._apple_auth_code_validator._redact = bv.BlotRedactor(None)
IdpAuthCode._google_auth_code_validator = bv.String()
IdpAuthCode._google_auth_code_validator._redact = bv.BlotRedactor(None)
IdpAuthCode._other_validator = bv.Void()
IdpAuthCode._tagmap = {
    'apple_auth_code': IdpAuthCode._apple_auth_code_validator,
    'google_auth_code': IdpAuthCode._google_auth_code_validator,
    'other': IdpAuthCode._other_validator }
IdpAuthCode.other = IdpAuthCode('other')
InaccessibleSubaccount.account_id.validator = bv.Nullable(AccountUserXid_validator)
InaccessibleSubaccount.display_name.validator = bv.String()
InaccessibleSubaccount.display_name.validator._redact = bv.BlotRedactor(None)
InaccessibleSubaccount.email.validator = bv.String()
InaccessibleSubaccount.email.validator._redact = bv.BlotRedactor(None)
InaccessibleSubaccount.dbid.validator = bv.String()
InaccessibleSubaccount.dbid.validator._redact = bv.BlotRedactor(None)
InaccessibleSubaccount.is_pending_promotion_or_transfer.validator = bv.Boolean()
InaccessibleSubaccount.is_pending_promotion_or_transfer.validator._redact = bv.BlotRedactor(None)
InaccessibleSubaccount._all_field_names_ = set([
    'account_id',
    'display_name',
    'email',
    'dbid',
    'is_pending_promotion_or_transfer'])
InaccessibleSubaccount._all_fields_ = [
    ('account_id', InaccessibleSubaccount.account_id.validator),
    ('display_name', InaccessibleSubaccount.display_name.validator),
    ('email', InaccessibleSubaccount.email.validator),
    ('dbid', InaccessibleSubaccount.dbid.validator),
    ('is_pending_promotion_or_transfer', InaccessibleSubaccount.is_pending_promotion_or_transfer.validator)]
InitiateEmailChangeArg.email.validator = common.EmailAddress_validator
InitiateEmailChangeArg.source.validator = InitiateEmailChangeSource_validator
InitiateEmailChangeArg.credential.validator = AuthCredential_validator
InitiateEmailChangeArg.device_info.validator = bv.Nullable(DeviceInfo_validator)
InitiateEmailChangeArg.client_id.validator = bv.Nullable(bv.String())
InitiateEmailChangeArg._all_field_names_ = set([
    'email',
    'source',
    'credential',
    'device_info',
    'client_id'])
InitiateEmailChangeArg._all_fields_ = [
    ('email', InitiateEmailChangeArg.email.validator),
    ('source', InitiateEmailChangeArg.source.validator),
    ('credential', InitiateEmailChangeArg.credential.validator),
    ('device_info', InitiateEmailChangeArg.device_info.validator),
    ('client_id', InitiateEmailChangeArg.client_id.validator)]
InitiateEmailChangeError._email_unavailable_validator = bv.Void()
InitiateEmailChangeError._non_matching_apple_persistent_id_validator = bv.Void()
InitiateEmailChangeError._auth_failed_validator = bv.Void()
InitiateEmailChangeError._transient_error_validator = bv.Void()
InitiateEmailChangeError._other_validator = bv.Void()
InitiateEmailChangeError._tagmap = {
    'email_unavailable': InitiateEmailChangeError._email_unavailable_validator,
    'non_matching_apple_persistent_id': InitiateEmailChangeError._non_matching_apple_persistent_id_validator,
    'auth_failed': InitiateEmailChangeError._auth_failed_validator,
    'transient_error': InitiateEmailChangeError._transient_error_validator,
    'other': InitiateEmailChangeError._other_validator }
InitiateEmailChangeError.email_unavailable = InitiateEmailChangeError('email_unavailable')
InitiateEmailChangeError.non_matching_apple_persistent_id = InitiateEmailChangeError('non_matching_apple_persistent_id')
InitiateEmailChangeError.auth_failed = InitiateEmailChangeError('auth_failed')
InitiateEmailChangeError.transient_error = InitiateEmailChangeError('transient_error')
InitiateEmailChangeError.other = InitiateEmailChangeError('other')
InitiateEmailChangeResult._needs_verification_validator = bv.Void()
InitiateEmailChangeResult._ok_validator = bv.Void()
InitiateEmailChangeResult._other_validator = bv.Void()
InitiateEmailChangeResult._tagmap = {
    'needs_verification': InitiateEmailChangeResult._needs_verification_validator,
    'ok': InitiateEmailChangeResult._ok_validator,
    'other': InitiateEmailChangeResult._other_validator }
InitiateEmailChangeResult.needs_verification = InitiateEmailChangeResult('needs_verification')
InitiateEmailChangeResult.ok = InitiateEmailChangeResult('ok')
InitiateEmailChangeResult.other = InitiateEmailChangeResult('other')
InitiateEmailChangeSource._apple_signup_validator = bv.Void()
InitiateEmailChangeSource._other_validator = bv.Void()
InitiateEmailChangeSource._tagmap = {
    'apple_signup': InitiateEmailChangeSource._apple_signup_validator,
    'other': InitiateEmailChangeSource._other_validator }
InitiateEmailChangeSource.apple_signup = InitiateEmailChangeSource('apple_signup')
InitiateEmailChangeSource.other = InitiateEmailChangeSource('other')
IosAppAttestInfo.key_id.validator = bv.String()
IosAppAttestInfo.key_id.validator._redact = bv.BlotRedactor(None)
IosAppAttestInfo.assertion.validator = bv.String()
IosAppAttestInfo.assertion.validator._redact = bv.BlotRedactor(None)
IosAppAttestInfo.client_data.validator = bv.String()
IosAppAttestInfo.client_data.validator._redact = bv.BlotRedactor(None)
IosAppAttestInfo.environment.validator = bv.String()
IosAppAttestInfo.environment.validator._redact = bv.BlotRedactor(None)
IosAppAttestInfo._all_field_names_ = set([
    'key_id',
    'assertion',
    'client_data',
    'environment'])
IosAppAttestInfo._all_fields_ = [
    ('key_id', IosAppAttestInfo.key_id.validator),
    ('assertion', IosAppAttestInfo.assertion.validator),
    ('client_data', IosAppAttestInfo.client_data.validator),
    ('environment', IosAppAttestInfo.environment.validator)]
ListInaccessibleSubaccountsArg._all_field_names_ = set([])
ListInaccessibleSubaccountsArg._all_fields_ = []
ListInaccessibleSubaccountsError._other_validator = bv.Void()
ListInaccessibleSubaccountsError._tagmap = {
    'other': ListInaccessibleSubaccountsError._other_validator }
ListInaccessibleSubaccountsError.other = ListInaccessibleSubaccountsError('other')
ListInaccessibleSubaccountsResponse.entries.validator = bv.Nullable(bv.List(InaccessibleSubaccount_validator))
ListInaccessibleSubaccountsResponse._all_field_names_ = set([
    'entries'])
ListInaccessibleSubaccountsResponse._all_fields_ = [
    ('entries', ListInaccessibleSubaccountsResponse.entries.validator)]
LoginArg.email.validator = bv.Nullable(common.EmailAddress_validator)
LoginArg.password.validator = bv.String()
LoginArg.password.validator._redact = bv.BlotRedactor(None)
LoginArg.require_role.validator = bv.Nullable(Role_validator)
LoginArg.device_info.validator = bv.Nullable(DeviceInfo_validator)
LoginArg.captcha.validator = bv.Nullable(ReCaptchaResponse_validator)
LoginArg.mobile_integrity_token.validator = bv.Nullable(MobileIntegrityToken_validator)
LoginArg.team_emm_token.validator = bv.Nullable(bv.String())
LoginArg.checkpoint_token.validator = bv.Nullable(ThirdPartyCheckpointToken_validator)
LoginArg.supports_passkey.validator = bv.Nullable(bv.Boolean())
LoginArg._all_field_names_ = set([
    'email',
    'password',
    'require_role',
    'device_info',
    'captcha',
    'mobile_integrity_token',
    'team_emm_token',
    'checkpoint_token',
    'supports_passkey'])
LoginArg._all_fields_ = [
    ('email', LoginArg.email.validator),
    ('password', LoginArg.password.validator),
    ('require_role', LoginArg.require_role.validator),
    ('device_info', LoginArg.device_info.validator),
    ('captcha', LoginArg.captcha.validator),
    ('mobile_integrity_token', LoginArg.mobile_integrity_token.validator),
    ('team_emm_token', LoginArg.team_emm_token.validator),
    ('checkpoint_token', LoginArg.checkpoint_token.validator),
    ('supports_passkey', LoginArg.supports_passkey.validator)]
LoginError._credentials_expired_validator = bv.Void()
LoginError._credentials_invalid_validator = bv.Void()
LoginError._login_rate_exceeded_validator = bv.Void()
LoginError._sms_error_validator = SmsError_validator
LoginError._two_factor_not_enabled_validator = bv.Void()
LoginError._role_mismatch_validator = bv.Void()
LoginError._auth_invalid_validator = bv.Void()
LoginError._emm_validation_error_validator = EmmValidationError_validator
LoginError._registration_completion_requried_validator = bv.Void()
LoginError._invalid_checkpoint_token_validator = bv.Void()
LoginError._user_device_limit_exceeded_validator = bv.Void()
LoginError._account_age_gated_validator = bv.Void()
LoginError._client_account_suspended_validator = bv.Void()
LoginError._sms_rate_exceeded_validator = bv.Void()
LoginError._pending_invite_not_claimed_validator = bv.Void()
LoginError._other_validator = bv.Void()
# WARNING: Decompyle incomplete
