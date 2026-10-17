# Source Generated with Decompyle++
# File: cert_pinning.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import objc
from Foundation import NSURLAuthenticationMethodServerTrust, NSURLCacheStorageNotAllowed, NSURLConnection, NSURLCredential, NSURLProtocol
from macffi_native import ffi
from dropbox.client.ui.cocoa.security import validate_trust
from dropbox.exception.exception_decorators import handle_exceptions, handle_exceptions_ex_2, handle_exceptions_ex_3
from dropbox.mac.internal import autoreleasepool

def register_protocol():
    NSURLProtocol.registerClass_(EFURLProtocol)


class EFURLProtocol(NSURLProtocol):
    
    def init(self):
        self = objc.super(EFURLProtocol, self).init()
        if not self:
            return None
        self.connection = None
        return self

    canInitWithRequest_ = (lambda self, request: autoreleasepool()if NSURLProtocol.propertyForKey_inRequest_('com.dropbox.client.EFProtocolHandled', request):
None(None, None)FalseNone(None, None))()
    
    def canonicalRequestForRequest_(self, request):
        return request

    requestIsCacheEquivalent_toRequest_ = (lambda self, a, b: objc.super(EFURLProtocol, self).requestIsCacheEquivalent_toRequest_(a, b))()
    startLoading = (lambda self: mutable_req = self.request().mutableCopy()NSURLProtocol.setProperty_forKey_inRequest_(True, 'com.dropbox.client.EFProtocolHandled', mutable_req)self.connection = NSURLConnection.connectionWithRequest_delegate_(mutable_req, self))()
    stopLoading = (lambda self: self.connection.cancel()self.connection = None)()
    connection_didReceiveResponse_ = (lambda self, connection, response: self.client().URLProtocol_didReceiveResponse_cacheStoragePolicy_(self, response, NSURLCacheStorageNotAllowed))()
    connection_didReceiveData_ = (lambda self, connection, data: self.client().URLProtocol_didLoadData_(self, data))()
    connectionDidFinishLoading_ = (lambda self, connection: self.client().URLProtocolDidFinishLoading_(self))()
    connection_didFailWithError_ = (lambda self, connection, error: self.client().URLProtocol_didFailWithError_(self, error))()
    
    def connection_canAuthenticateAgainstProtectionSpace_(self, connection, protectionSpace):
        return True

    connection_didReceiveAuthenticationChallenge_ = (lambda self, connection, challenge: protection_space = challenge.protectionSpace()if protection_space.authenticationMethod() != NSURLAuthenticationMethodServerTrust:
connection.cancel()Nonetrust = None.serverTrust()trust_ref = ffi.cast('SecTrustRef', trust.pointerAsInteger)if not trust_ref:
connection.cancel()Noneif not validate_trust(trust_ref):
connection.cancel()Nonecredential = NSURLCredential.credentialForTrust_(trust)challenge.sender().useCredential_forAuthenticationChallenge_(credential, challenge))()

