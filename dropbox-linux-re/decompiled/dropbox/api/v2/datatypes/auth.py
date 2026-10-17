# Source Generated with Decompyle++
# File: auth.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import account
from dropbox.api.v2.datatypes import account_id

class AccessError(bb.Union):
    pass
# WARNING: Decompyle incomplete

AccessError_validator = bv.Union(AccessError)

class AuthError(bb.Union):
    pass
# WARNING: Decompyle incomplete

AuthError_validator = bv.Union(AuthError)

class DAuthArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DAuthArg_validator = bv.Struct(DAuthArg)

class DAuthError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DAuthError_validator = bv.Union(DAuthError)

class DAuthResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DAuthResult_validator = bv.Struct(DAuthResult)

class DauthAuthorizeInfoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DauthAuthorizeInfoArg_validator = bv.Struct(DauthAuthorizeInfoArg)

class DauthAuthorizeInfoError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DauthAuthorizeInfoError_validator = bv.Union(DauthAuthorizeInfoError)

class DauthAuthorizeInfoResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DauthAuthorizeInfoResponse_validator = bv.Struct(DauthAuthorizeInfoResponse)

class DauthAuthorizeInfoScope(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DauthAuthorizeInfoScope_validator = bv.Struct(DauthAuthorizeInfoScope)

class DesktopAuthArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DesktopAuthArg_validator = bv.Struct(DesktopAuthArg)

class DesktopAuthError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DesktopAuthError_validator = bv.Union(DesktopAuthError)

class DesktopAuthResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DesktopAuthResult_validator = bv.Struct(DesktopAuthResult)

class DesktopAuthStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

DesktopAuthStatus_validator = bv.Union(DesktopAuthStatus)

class DesktopHostKeyExchangeArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DesktopHostKeyExchangeArg_validator = bv.Struct(DesktopHostKeyExchangeArg)

class DesktopHostKeyExchangeError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DesktopHostKeyExchangeError_validator = bv.Union(DesktopHostKeyExchangeError)

class DesktopHostKeyExchangeResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DesktopHostKeyExchangeResult_validator = bv.Struct(DesktopHostKeyExchangeResult)

class DesktopPreauthExchangeArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DesktopPreauthExchangeArg_validator = bv.Struct(DesktopPreauthExchangeArg)

class DesktopPreauthExchangeError(bb.Union):
    pass
# WARNING: Decompyle incomplete

DesktopPreauthExchangeError_validator = bv.Union(DesktopPreauthExchangeError)

class DesktopPreauthExchangeResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DesktopPreauthExchangeResult_validator = bv.Struct(DesktopPreauthExchangeResult)

class InvalidAccountTypeError(bb.Union):
    pass
# WARNING: Decompyle incomplete

InvalidAccountTypeError_validator = bv.Union(InvalidAccountTypeError)

class NoPermissionError(bb.Union):
    pass
# WARNING: Decompyle incomplete

NoPermissionError_validator = bv.Union(NoPermissionError)

class PaperAccessError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PaperAccessError_validator = bv.Union(PaperAccessError)

class RateLimitError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RateLimitError_validator = bv.Struct(RateLimitError)

class RateLimitReason(bb.Union):
    pass
# WARNING: Decompyle incomplete

RateLimitReason_validator = bv.Union(RateLimitReason)

class SubAccountTokenMintArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SubAccountTokenMintArg_validator = bv.Struct(SubAccountTokenMintArg)

class SubAccountTokenMintError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SubAccountTokenMintError_validator = bv.Union(SubAccountTokenMintError)

class SubAccountTokenMintResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SubAccountTokenMintResult_validator = bv.Struct(SubAccountTokenMintResult)

class SubAccountTokenResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SubAccountTokenResult_validator = bv.Struct(SubAccountTokenResult)

class TokenExchangeArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TokenExchangeArg_validator = bv.Struct(TokenExchangeArg)

class TokenExchangeError(bb.Union):
    pass
# WARNING: Decompyle incomplete

TokenExchangeError_validator = bv.Union(TokenExchangeError)

class TokenExchangeResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TokenExchangeResult_validator = bv.Struct(TokenExchangeResult)

class TokenFromOAuth1Arg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TokenFromOAuth1Arg_validator = bv.Struct(TokenFromOAuth1Arg)

class TokenFromOAuth1Error(bb.Union):
    pass
# WARNING: Decompyle incomplete

TokenFromOAuth1Error_validator = bv.Union(TokenFromOAuth1Error)

class TokenFromOAuth1Result(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TokenFromOAuth1Result_validator = bv.Struct(TokenFromOAuth1Result)

class TokenScopeError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TokenScopeError_validator = bv.Struct(TokenScopeError)

class UnauthorizedAccountIdUsageError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UnauthorizedAccountIdUsageError_validator = bv.Struct(UnauthorizedAccountIdUsageError)

class WebAuthError(bb.Union):
    pass
# WARNING: Decompyle incomplete

WebAuthError_validator = bv.Union(WebAuthError)
AccessError._invalid_account_type_validator = InvalidAccountTypeError_validator
AccessError._paper_access_denied_validator = PaperAccessError_validator
AccessError._team_access_denied_validator = bv.Void()
AccessError._no_permission_validator = NoPermissionError_validator
AccessError._pp_access_denied_validator = bv.Void()
AccessError._other_validator = bv.Void()
AccessError._tagmap = {
    'invalid_account_type': AccessError._invalid_account_type_validator,
    'paper_access_denied': AccessError._paper_access_denied_validator,
    'team_access_denied': AccessError._team_access_denied_validator,
    'no_permission': AccessError._no_permission_validator,
    'pp_access_denied': AccessError._pp_access_denied_validator,
    'other': AccessError._other_validator }
AccessError.team_access_denied = AccessError('team_access_denied')
AccessError.pp_access_denied = AccessError('pp_access_denied')
AccessError.other = AccessError('other')
AuthError._invalid_access_token_validator = bv.Void()
AuthError._invalid_select_user_validator = bv.Void()
AuthError._invalid_select_admin_validator = bv.Void()
AuthError._user_suspended_validator = bv.Void()
AuthError._expired_access_token_validator = bv.Void()
AuthError._missing_scope_validator = TokenScopeError_validator
AuthError._route_access_denied_validator = bv.Void()
AuthError._no_team_api_access_validator = bv.Void()
AuthError._invalid_team_auth_header_validator = bv.Void()
AuthError._federation_access_denied_validator = bv.Void()
AuthError._other_validator = bv.Void()
AuthError._tagmap = {
    'invalid_access_token': AuthError._invalid_access_token_validator,
    'invalid_select_user': AuthError._invalid_select_user_validator,
    'invalid_select_admin': AuthError._invalid_select_admin_validator,
    'user_suspended': AuthError._user_suspended_validator,
    'expired_access_token': AuthError._expired_access_token_validator,
    'missing_scope': AuthError._missing_scope_validator,
    'route_access_denied': AuthError._route_access_denied_validator,
    'no_team_api_access': AuthError._no_team_api_access_validator,
    'invalid_team_auth_header': AuthError._invalid_team_auth_header_validator,
    'federation_access_denied': AuthError._federation_access_denied_validator,
    'other': AuthError._other_validator }
AuthError.invalid_access_token = AuthError('invalid_access_token')
AuthError.invalid_select_user = AuthError('invalid_select_user')
AuthError.invalid_select_admin = AuthError('invalid_select_admin')
AuthError.user_suspended = AuthError('user_suspended')
AuthError.expired_access_token = AuthError('expired_access_token')
AuthError.route_access_denied = AuthError('route_access_denied')
AuthError.no_team_api_access = AuthError('no_team_api_access')
AuthError.invalid_team_auth_header = AuthError('invalid_team_auth_header')
AuthError.federation_access_denied = AuthError('federation_access_denied')
AuthError.other = AuthError('other')
DAuthArg.consumer_key.validator = bv.String()
DAuthArg.consumer_key.validator._redact = bv.BlotRedactor(None)
DAuthArg.state.validator = bv.Nullable(bv.String())
DAuthArg.redirect_uri.validator = bv.Nullable(bv.String())
DAuthArg.extra_query_params.validator = bv.Nullable(bv.String())
DAuthArg._all_field_names_ = set([
    'consumer_key',
    'state',
    'redirect_uri',
    'extra_query_params'])
DAuthArg._all_fields_ = [
    ('consumer_key', DAuthArg.consumer_key.validator),
    ('state', DAuthArg.state.validator),
    ('redirect_uri', DAuthArg.redirect_uri.validator),
    ('extra_query_params', DAuthArg.extra_query_params.validator)]
DAuthError._dauth_max_users_authorized_validator = bv.Void()
DAuthError._dauth_add_user_failed_validator = bv.Void()
DAuthError._other_validator = bv.Void()
DAuthError._tagmap = {
    'dauth_max_users_authorized': DAuthError._dauth_max_users_authorized_validator,
    'dauth_add_user_failed': DAuthError._dauth_add_user_failed_validator,
    'other': DAuthError._other_validator }
DAuthError.dauth_max_users_authorized = DAuthError('dauth_max_users_authorized')
DAuthError.dauth_add_user_failed = DAuthError('dauth_add_user_failed')
DAuthError.other = DAuthError('other')
DAuthResult.uid.validator = bv.UInt64()
DAuthResult.uid.validator._redact = bv.BlotRedactor(None)
DAuthResult.state.validator = bv.Nullable(bv.String())
DAuthResult.oauth_token.validator = bv.String(min_length = 1)
DAuthResult.oauth_token.validator._redact = bv.BlotRedactor(None)
DAuthResult.oauth_token_secret.validator = bv.String(min_length = 1)
DAuthResult.oauth_token_secret.validator._redact = bv.BlotRedactor(None)
DAuthResult.extra_query_results.validator = bv.Nullable(bv.String())
DAuthResult._all_field_names_ = set([
    'uid',
    'state',
    'oauth_token',
    'oauth_token_secret',
    'extra_query_results'])
DAuthResult._all_fields_ = [
    ('uid', DAuthResult.uid.validator),
    ('state', DAuthResult.state.validator),
    ('oauth_token', DAuthResult.oauth_token.validator),
    ('oauth_token_secret', DAuthResult.oauth_token_secret.validator),
    ('extra_query_results', DAuthResult.extra_query_results.validator)]
DauthAuthorizeInfoArg.client_id.validator = bv.String()
DauthAuthorizeInfoArg.client_id.validator._redact = bv.BlotRedactor(None)
DauthAuthorizeInfoArg.scope.validator = bv.Nullable(bv.String())
DauthAuthorizeInfoArg.include_granted_scopes.validator = bv.Boolean()
DauthAuthorizeInfoArg.include_granted_scopes.validator._redact = bv.BlotRedactor(None)
DauthAuthorizeInfoArg._all_field_names_ = set([
    'client_id',
    'scope',
    'include_granted_scopes'])
DauthAuthorizeInfoArg._all_fields_ = [
    ('client_id', DauthAuthorizeInfoArg.client_id.validator),
    ('scope', DauthAuthorizeInfoArg.scope.validator),
    ('include_granted_scopes', DauthAuthorizeInfoArg.include_granted_scopes.validator)]
DauthAuthorizeInfoError._invalid_consumer_key_validator = bv.Void()
DauthAuthorizeInfoError._invalid_request_validator = bv.Void()
DauthAuthorizeInfoError._other_validator = bv.Void()
DauthAuthorizeInfoError._tagmap = {
    'invalid_consumer_key': DauthAuthorizeInfoError._invalid_consumer_key_validator,
    'invalid_request': DauthAuthorizeInfoError._invalid_request_validator,
    'other': DauthAuthorizeInfoError._other_validator }
DauthAuthorizeInfoError.invalid_consumer_key = DauthAuthorizeInfoError('invalid_consumer_key')
DauthAuthorizeInfoError.invalid_request = DauthAuthorizeInfoError('invalid_request')
DauthAuthorizeInfoError.other = DauthAuthorizeInfoError('other')
DauthAuthorizeInfoResponse.name.validator = bv.String()
DauthAuthorizeInfoResponse.name.validator._redact = bv.BlotRedactor(None)
DauthAuthorizeInfoResponse.app_icon_url.validator = bv.String()
DauthAuthorizeInfoResponse.app_icon_url.validator._redact = bv.BlotRedactor(None)
DauthAuthorizeInfoResponse.permissions.validator = bv.Nullable(bv.List(DauthAuthorizeInfoScope_validator))
DauthAuthorizeInfoResponse.include_granted_scopes.validator = bv.Boolean()
DauthAuthorizeInfoResponse.include_granted_scopes.validator._redact = bv.BlotRedactor(None)
DauthAuthorizeInfoResponse._all_field_names_ = set([
    'name',
    'app_icon_url',
    'permissions',
    'include_granted_scopes'])
DauthAuthorizeInfoResponse._all_fields_ = [
    ('name', DauthAuthorizeInfoResponse.name.validator),
    ('app_icon_url', DauthAuthorizeInfoResponse.app_icon_url.validator),
    ('permissions', DauthAuthorizeInfoResponse.permissions.validator),
    ('include_granted_scopes', DauthAuthorizeInfoResponse.include_granted_scopes.validator)]
DauthAuthorizeInfoScope.message.validator = bv.String()
DauthAuthorizeInfoScope.message.validator._redact = bv.BlotRedactor(None)
DauthAuthorizeInfoScope._all_field_names_ = set([
    'message'])
DauthAuthorizeInfoScope._all_fields_ = [
    ('message', DauthAuthorizeInfoScope.message.validator)]
DesktopAuthArg.consumer_key.validator = bv.String()
DesktopAuthArg.consumer_key.validator._redact = bv.BlotRedactor(None)
DesktopAuthArg.device_info.validator = account.DeviceInfo_validator
DesktopAuthArg._all_field_names_ = set([
    'consumer_key',
    'device_info'])
DesktopAuthArg._all_fields_ = [
    ('consumer_key', DesktopAuthArg.consumer_key.validator),
    ('device_info', DesktopAuthArg.device_info.validator)]
DesktopAuthError._invalid_host_key_validator = bv.Void()
DesktopAuthError._host_unlinked_validator = bv.Void()
DesktopAuthError._app_not_allowed_validator = bv.Void()
DesktopAuthError._invalid_app_validator = bv.Void()
DesktopAuthError._invalid_user_validator = bv.Void()
DesktopAuthError._other_validator = bv.Void()
DesktopAuthError._tagmap = {
    'invalid_host_key': DesktopAuthError._invalid_host_key_validator,
    'host_unlinked': DesktopAuthError._host_unlinked_validator,
    'app_not_allowed': DesktopAuthError._app_not_allowed_validator,
    'invalid_app': DesktopAuthError._invalid_app_validator,
    'invalid_user': DesktopAuthError._invalid_user_validator,
    'other': DesktopAuthError._other_validator }
DesktopAuthError.invalid_host_key = DesktopAuthError('invalid_host_key')
DesktopAuthError.host_unlinked = DesktopAuthError('host_unlinked')
DesktopAuthError.app_not_allowed = DesktopAuthError('app_not_allowed')
DesktopAuthError.invalid_app = DesktopAuthError('invalid_app')
DesktopAuthError.invalid_user = DesktopAuthError('invalid_user')
DesktopAuthError.other = DesktopAuthError('other')
DesktopAuthResult.status.validator = DesktopAuthStatus_validator
DesktopAuthResult._all_field_names_ = set([
    'status'])
DesktopAuthResult._all_fields_ = [
    ('status', DesktopAuthResult.status.validator)]
DesktopAuthStatus._success_validator = bv.String()
DesktopAuthStatus._success_validator._redact = bv.BlotRedactor(None)
DesktopAuthStatus._other_validator = bv.Void()
DesktopAuthStatus._tagmap = {
    'success': DesktopAuthStatus._success_validator,
    'other': DesktopAuthStatus._other_validator }
DesktopAuthStatus.other = DesktopAuthStatus('other')
DesktopHostKeyExchangeArg.consumer_key.validator = bv.String()
DesktopHostKeyExchangeArg.consumer_key.validator._redact = bv.BlotRedactor(None)
DesktopHostKeyExchangeArg.device_info.validator = account.DeviceInfo_validator
DesktopHostKeyExchangeArg._all_field_names_ = set([
    'consumer_key',
    'device_info'])
DesktopHostKeyExchangeArg._all_fields_ = [
    ('consumer_key', DesktopHostKeyExchangeArg.consumer_key.validator),
    ('device_info', DesktopHostKeyExchangeArg.device_info.validator)]
DesktopHostKeyExchangeError._invalid_host_key_validator = bv.Void()
DesktopHostKeyExchangeError._host_unlinked_validator = bv.Void()
DesktopHostKeyExchangeError._app_not_allowed_validator = bv.Void()
DesktopHostKeyExchangeError._invalid_app_validator = bv.Void()
DesktopHostKeyExchangeError._invalid_user_validator = bv.Void()
DesktopHostKeyExchangeError._other_validator = bv.Void()
DesktopHostKeyExchangeError._tagmap = {
    'invalid_host_key': DesktopHostKeyExchangeError._invalid_host_key_validator,
    'host_unlinked': DesktopHostKeyExchangeError._host_unlinked_validator,
    'app_not_allowed': DesktopHostKeyExchangeError._app_not_allowed_validator,
    'invalid_app': DesktopHostKeyExchangeError._invalid_app_validator,
    'invalid_user': DesktopHostKeyExchangeError._invalid_user_validator,
    'other': DesktopHostKeyExchangeError._other_validator }
DesktopHostKeyExchangeError.invalid_host_key = DesktopHostKeyExchangeError('invalid_host_key')
DesktopHostKeyExchangeError.host_unlinked = DesktopHostKeyExchangeError('host_unlinked')
DesktopHostKeyExchangeError.app_not_allowed = DesktopHostKeyExchangeError('app_not_allowed')
DesktopHostKeyExchangeError.invalid_app = DesktopHostKeyExchangeError('invalid_app')
DesktopHostKeyExchangeError.invalid_user = DesktopHostKeyExchangeError('invalid_user')
DesktopHostKeyExchangeError.other = DesktopHostKeyExchangeError('other')
DesktopHostKeyExchangeResult.access_token.validator = bv.String()
DesktopHostKeyExchangeResult.access_token.validator._redact = bv.BlotRedactor(None)
DesktopHostKeyExchangeResult.expires_in.validator = bv.Int64()
DesktopHostKeyExchangeResult.expires_in.validator._redact = bv.BlotRedactor(None)
DesktopHostKeyExchangeResult.refresh_token.validator = bv.String()
DesktopHostKeyExchangeResult.refresh_token.validator._redact = bv.BlotRedactor(None)
DesktopHostKeyExchangeResult._all_field_names_ = set([
    'access_token',
    'expires_in',
    'refresh_token'])
DesktopHostKeyExchangeResult._all_fields_ = [
    ('access_token', DesktopHostKeyExchangeResult.access_token.validator),
    ('expires_in', DesktopHostKeyExchangeResult.expires_in.validator),
    ('refresh_token', DesktopHostKeyExchangeResult.refresh_token.validator)]
DesktopPreauthExchangeArg.device_info.validator = account.DeviceInfo_validator
DesktopPreauthExchangeArg.installer_tag.validator = bv.String()
DesktopPreauthExchangeArg.installer_tag.validator._redact = bv.BlotRedactor(None)
DesktopPreauthExchangeArg.preauth_nonce.validator = bv.String()
DesktopPreauthExchangeArg.preauth_nonce.validator._redact = bv.BlotRedactor(None)
DesktopPreauthExchangeArg._all_field_names_ = set([
    'device_info',
    'installer_tag',
    'preauth_nonce'])
DesktopPreauthExchangeArg._all_fields_ = [
    ('device_info', DesktopPreauthExchangeArg.device_info.validator),
    ('installer_tag', DesktopPreauthExchangeArg.installer_tag.validator),
    ('preauth_nonce', DesktopPreauthExchangeArg.preauth_nonce.validator)]
DesktopPreauthExchangeError._invalid_tag_or_preauth_nonce_validator = bv.Void()
DesktopPreauthExchangeError._app_not_allowed_validator = bv.Void()
DesktopPreauthExchangeError._invalid_app_validator = bv.Void()
DesktopPreauthExchangeError._invalid_user_validator = bv.Void()
DesktopPreauthExchangeError._other_validator = bv.Void()
DesktopPreauthExchangeError._tagmap = {
    'invalid_tag_or_preauth_nonce': DesktopPreauthExchangeError._invalid_tag_or_preauth_nonce_validator,
    'app_not_allowed': DesktopPreauthExchangeError._app_not_allowed_validator,
    'invalid_app': DesktopPreauthExchangeError._invalid_app_validator,
    'invalid_user': DesktopPreauthExchangeError._invalid_user_validator,
    'other': DesktopPreauthExchangeError._other_validator }
DesktopPreauthExchangeError.invalid_tag_or_preauth_nonce = DesktopPreauthExchangeError('invalid_tag_or_preauth_nonce')
DesktopPreauthExchangeError.app_not_allowed = DesktopPreauthExchangeError('app_not_allowed')
DesktopPreauthExchangeError.invalid_app = DesktopPreauthExchangeError('invalid_app')
DesktopPreauthExchangeError.invalid_user = DesktopPreauthExchangeError('invalid_user')
DesktopPreauthExchangeError.other = DesktopPreauthExchangeError('other')
DesktopPreauthExchangeResult.access_token.validator = bv.String()
DesktopPreauthExchangeResult.access_token.validator._redact = bv.BlotRedactor(None)
DesktopPreauthExchangeResult.expires_in.validator = bv.Int64()
DesktopPreauthExchangeResult.expires_in.validator._redact = bv.BlotRedactor(None)
DesktopPreauthExchangeResult.refresh_token.validator = bv.String()
DesktopPreauthExchangeResult.refresh_token.validator._redact = bv.BlotRedactor(None)
DesktopPreauthExchangeResult._all_field_names_ = set([
    'access_token',
    'expires_in',
    'refresh_token'])
DesktopPreauthExchangeResult._all_fields_ = [
    ('access_token', DesktopPreauthExchangeResult.access_token.validator),
    ('expires_in', DesktopPreauthExchangeResult.expires_in.validator),
    ('refresh_token', DesktopPreauthExchangeResult.refresh_token.validator)]
InvalidAccountTypeError._endpoint_validator = bv.Void()
InvalidAccountTypeError._feature_validator = bv.Void()
InvalidAccountTypeError._other_validator = bv.Void()
InvalidAccountTypeError._tagmap = {
    'endpoint': InvalidAccountTypeError._endpoint_validator,
    'feature': InvalidAccountTypeError._feature_validator,
    'other': InvalidAccountTypeError._other_validator }
InvalidAccountTypeError.endpoint = InvalidAccountTypeError('endpoint')
InvalidAccountTypeError.feature = InvalidAccountTypeError('feature')
InvalidAccountTypeError.other = InvalidAccountTypeError('other')
NoPermissionError._unauthorized_account_id_usage_validator = UnauthorizedAccountIdUsageError_validator
NoPermissionError._other_validator = bv.Void()
NoPermissionError._tagmap = {
    'unauthorized_account_id_usage': NoPermissionError._unauthorized_account_id_usage_validator,
    'other': NoPermissionError._other_validator }
NoPermissionError.other = NoPermissionError('other')
PaperAccessError._paper_disabled_validator = bv.Void()
PaperAccessError._not_paper_user_validator = bv.Void()
PaperAccessError._other_validator = bv.Void()
PaperAccessError._tagmap = {
    'paper_disabled': PaperAccessError._paper_disabled_validator,
    'not_paper_user': PaperAccessError._not_paper_user_validator,
    'other': PaperAccessError._other_validator }
PaperAccessError.paper_disabled = PaperAccessError('paper_disabled')
PaperAccessError.not_paper_user = PaperAccessError('not_paper_user')
PaperAccessError.other = PaperAccessError('other')
RateLimitError.reason.validator = RateLimitReason_validator
RateLimitError.retry_after.validator = bv.UInt64()
RateLimitError.retry_after.validator._redact = bv.BlotRedactor(None)
RateLimitError._all_field_names_ = set([
    'reason',
    'retry_after'])
RateLimitError._all_fields_ = [
    ('reason', RateLimitError.reason.validator),
    ('retry_after', RateLimitError.retry_after.validator)]
RateLimitReason._too_many_requests_validator = bv.Void()
RateLimitReason._too_many_write_operations_validator = bv.Void()
RateLimitReason._other_validator = bv.Void()
RateLimitReason._tagmap = {
    'too_many_requests': RateLimitReason._too_many_requests_validator,
    'too_many_write_operations': RateLimitReason._too_many_write_operations_validator,
    'other': RateLimitReason._other_validator }
RateLimitReason.too_many_requests = RateLimitReason('too_many_requests')
RateLimitReason.too_many_write_operations = RateLimitReason('too_many_write_operations')
RateLimitReason.other = RateLimitReason('other')
SubAccountTokenMintArg.sub_account_user_ids.validator = bv.Nullable(bv.List(bv.String()))
SubAccountTokenMintArg.sub_account_user_ids.validator._redact = bv.BlotRedactor(None)
SubAccountTokenMintArg.device_info.validator = bv.Nullable(account.DeviceInfo_validator)
SubAccountTokenMintArg._all_field_names_ = set([
    'sub_account_user_ids',
    'device_info'])
SubAccountTokenMintArg._all_fields_ = [
    ('sub_account_user_ids', SubAccountTokenMintArg.sub_account_user_ids.validator),
    ('device_info', SubAccountTokenMintArg.device_info.validator)]
SubAccountTokenMintError._not_allowed_validator = bv.Void()
SubAccountTokenMintError._unsupported_auth_validator = bv.Void()
SubAccountTokenMintError._other_validator = bv.Void()
SubAccountTokenMintError._tagmap = {
    'not_allowed': SubAccountTokenMintError._not_allowed_validator,
    'unsupported_auth': SubAccountTokenMintError._unsupported_auth_validator,
    'other': SubAccountTokenMintError._other_validator }
SubAccountTokenMintError.not_allowed = SubAccountTokenMintError('not_allowed')
SubAccountTokenMintError.unsupported_auth = SubAccountTokenMintError('unsupported_auth')
SubAccountTokenMintError.other = SubAccountTokenMintError('other')
SubAccountTokenMintResult.tokens.validator = bv.Nullable(bv.List(SubAccountTokenResult_validator))
SubAccountTokenMintResult._all_field_names_ = set([
    'tokens'])
SubAccountTokenMintResult._all_fields_ = [
    ('tokens', SubAccountTokenMintResult.tokens.validator)]
SubAccountTokenResult.user_id.validator = bv.String()
SubAccountTokenResult.user_id.validator._redact = bv.BlotRedactor(None)
SubAccountTokenResult.oauth2_token.validator = bv.String()
SubAccountTokenResult.oauth2_token.validator._redact = bv.BlotRedactor(None)
SubAccountTokenResult.refresh_token.validator = bv.String()
SubAccountTokenResult.refresh_token.validator._redact = bv.BlotRedactor(None)
SubAccountTokenResult.expires_in.validator = bv.Int32()
SubAccountTokenResult.expires_in.validator._redact = bv.BlotRedactor(None)
SubAccountTokenResult._all_field_names_ = set([
    'user_id',
    'oauth2_token',
    'refresh_token',
    'expires_in'])
SubAccountTokenResult._all_fields_ = [
    ('user_id', SubAccountTokenResult.user_id.validator),
    ('oauth2_token', SubAccountTokenResult.oauth2_token.validator),
    ('refresh_token', SubAccountTokenResult.refresh_token.validator),
    ('expires_in', SubAccountTokenResult.expires_in.validator)]
TokenExchangeArg.consumer_key.validator = bv.String()
TokenExchangeArg.consumer_key.validator._redact = bv.BlotRedactor(None)
TokenExchangeArg.device_info.validator = account.DeviceInfo_validator
TokenExchangeArg.team_emm_token.validator = bv.Nullable(bv.String())
TokenExchangeArg._all_field_names_ = set([
    'consumer_key',
    'device_info',
    'team_emm_token'])
TokenExchangeArg._all_fields_ = [
    ('consumer_key', TokenExchangeArg.consumer_key.validator),
    ('device_info', TokenExchangeArg.device_info.validator),
    ('team_emm_token', TokenExchangeArg.team_emm_token.validator)]
TokenExchangeError._exchange_not_allowed_validator = bv.Void()
TokenExchangeError._unsupported_auth_validator = bv.Void()
TokenExchangeError._master_token_already_exists_validator = bv.Void()
TokenExchangeError._not_enabled_validator = bv.Void()
TokenExchangeError._other_validator = bv.Void()
TokenExchangeError._tagmap = {
    'exchange_not_allowed': TokenExchangeError._exchange_not_allowed_validator,
    'unsupported_auth': TokenExchangeError._unsupported_auth_validator,
    'master_token_already_exists': TokenExchangeError._master_token_already_exists_validator,
    'not_enabled': TokenExchangeError._not_enabled_validator,
    'other': TokenExchangeError._other_validator }
TokenExchangeError.exchange_not_allowed = TokenExchangeError('exchange_not_allowed')
TokenExchangeError.unsupported_auth = TokenExchangeError('unsupported_auth')
TokenExchangeError.master_token_already_exists = TokenExchangeError('master_token_already_exists')
TokenExchangeError.not_enabled = TokenExchangeError('not_enabled')
TokenExchangeError.other = TokenExchangeError('other')
TokenExchangeResult.oauth2_token.validator = bv.String(min_length = 1)
TokenExchangeResult.oauth2_token.validator._redact = bv.BlotRedactor(None)
TokenExchangeResult._all_field_names_ = set([
    'oauth2_token'])
TokenExchangeResult._all_fields_ = [
    ('oauth2_token', TokenExchangeResult.oauth2_token.validator)]
TokenFromOAuth1Arg.oauth1_token.validator = bv.String(min_length = 1)
TokenFromOAuth1Arg.oauth1_token.validator._redact = bv.BlotRedactor(None)
TokenFromOAuth1Arg.oauth1_token_secret.validator = bv.String(min_length = 1)
TokenFromOAuth1Arg.oauth1_token_secret.validator._redact = bv.BlotRedactor(None)
TokenFromOAuth1Arg._all_field_names_ = set([
    'oauth1_token',
    'oauth1_token_secret'])
TokenFromOAuth1Arg._all_fields_ = [
    ('oauth1_token', TokenFromOAuth1Arg.oauth1_token.validator),
    ('oauth1_token_secret', TokenFromOAuth1Arg.oauth1_token_secret.validator)]
TokenFromOAuth1Error._invalid_oauth1_token_info_validator = bv.Void()
TokenFromOAuth1Error._app_id_mismatch_validator = bv.Void()
TokenFromOAuth1Error._other_validator = bv.Void()
TokenFromOAuth1Error._tagmap = {
    'invalid_oauth1_token_info': TokenFromOAuth1Error._invalid_oauth1_token_info_validator,
    'app_id_mismatch': TokenFromOAuth1Error._app_id_mismatch_validator,
    'other': TokenFromOAuth1Error._other_validator }
TokenFromOAuth1Error.invalid_oauth1_token_info = TokenFromOAuth1Error('invalid_oauth1_token_info')
TokenFromOAuth1Error.app_id_mismatch = TokenFromOAuth1Error('app_id_mismatch')
TokenFromOAuth1Error.other = TokenFromOAuth1Error('other')
TokenFromOAuth1Result.oauth2_token.validator = bv.String(min_length = 1)
TokenFromOAuth1Result.oauth2_token.validator._redact = bv.BlotRedactor(None)
TokenFromOAuth1Result._all_field_names_ = set([
    'oauth2_token'])
TokenFromOAuth1Result._all_fields_ = [
    ('oauth2_token', TokenFromOAuth1Result.oauth2_token.validator)]
TokenScopeError.required_scope.validator = bv.String()
TokenScopeError.required_scope.validator._redact = bv.BlotRedactor(None)
TokenScopeError._all_field_names_ = set([
    'required_scope'])
TokenScopeError._all_fields_ = [
    ('required_scope', TokenScopeError.required_scope.validator)]
UnauthorizedAccountIdUsageError.unauthorized_account_ids.validator = bv.List(bv.String())
UnauthorizedAccountIdUsageError.unauthorized_account_ids.validator._redact = bv.BlotRedactor(None)
UnauthorizedAccountIdUsageError._all_field_names_ = set([
    'unauthorized_account_ids'])
UnauthorizedAccountIdUsageError._all_fields_ = [
    ('unauthorized_account_ids', UnauthorizedAccountIdUsageError.unauthorized_account_ids.validator)]
WebAuthError._invalid_csrf_token_validator = bv.Void()
WebAuthError._user_not_logged_in_validator = bv.Void()
WebAuthError._no_team_api_access_validator = bv.Void()
WebAuthError._invalid_team_auth_header_validator = bv.Void()
WebAuthError._federation_access_denied_validator = bv.Void()
WebAuthError._reseller_session_expired_validator = bv.Void()
WebAuthError._other_validator = bv.Void()
WebAuthError._tagmap = {
    'invalid_csrf_token': WebAuthError._invalid_csrf_token_validator,
    'user_not_logged_in': WebAuthError._user_not_logged_in_validator,
    'no_team_api_access': WebAuthError._no_team_api_access_validator,
    'invalid_team_auth_header': WebAuthError._invalid_team_auth_header_validator,
    'federation_access_denied': WebAuthError._federation_access_denied_validator,
    'reseller_session_expired': WebAuthError._reseller_session_expired_validator,
    'other': WebAuthError._other_validator }
WebAuthError.invalid_csrf_token = WebAuthError('invalid_csrf_token')
WebAuthError.user_not_logged_in = WebAuthError('user_not_logged_in')
WebAuthError.no_team_api_access = WebAuthError('no_team_api_access')
WebAuthError.invalid_team_auth_header = WebAuthError('invalid_team_auth_header')
WebAuthError.federation_access_denied = WebAuthError('federation_access_denied')
WebAuthError.reseller_session_expired = WebAuthError('reseller_session_expired')
WebAuthError.other = WebAuthError('other')
DauthAuthorizeInfoArg.include_granted_scopes.default = False
DauthAuthorizeInfoResponse.name.default = ''
DauthAuthorizeInfoResponse.app_icon_url.default = ''
DauthAuthorizeInfoResponse.include_granted_scopes.default = False
DauthAuthorizeInfoScope.message.default = ''
RateLimitError.retry_after.default = 1
SubAccountTokenResult.refresh_token.default = ''
SubAccountTokenResult.expires_in.default = 0
# WARNING: Decompyle incomplete
