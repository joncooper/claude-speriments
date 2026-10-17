# Source Generated with Decompyle++
# File: store.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

class ApiProductFamily(bb.Union):
    pass
# WARNING: Decompyle incomplete

ApiProductFamily_validator = bv.Union(ApiProductFamily)

class Duration(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Duration_validator = bv.Struct(Duration)

class GetMobileDiscountRequestArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetMobileDiscountRequestArg_validator = bv.Struct(GetMobileDiscountRequestArg)

class GetMobileDiscountResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetMobileDiscountResponse_validator = bv.Struct(GetMobileDiscountResponse)

class GooglePlaySubscriptionDetails(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GooglePlaySubscriptionDetails_validator = bv.Struct(GooglePlaySubscriptionDetails)

class IosSubscriptionDetails(bb.Struct):
    pass
# WARNING: Decompyle incomplete

IosSubscriptionDetails_validator = bv.Struct(IosSubscriptionDetails)

class MobileClientInformation(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MobileClientInformation_validator = bv.Struct(MobileClientInformation)

class MobilePlan(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MobilePlan_validator = bv.Struct(MobilePlan)

class MobilePlanV2(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MobilePlanV2_validator = bv.Struct(MobilePlanV2)

class MobilePlansError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MobilePlansError_validator = bv.Struct(MobilePlansError)

class MobilePlansExceptionTypes(bb.Union):
    pass
# WARNING: Decompyle incomplete

MobilePlansExceptionTypes_validator = bv.Union(MobilePlansExceptionTypes)

class MobilePlansRequestArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MobilePlansRequestArg_validator = bv.Struct(MobilePlansRequestArg)

class MobilePlansResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MobilePlansResponse_validator = bv.Struct(MobilePlansResponse)

class MobilePlansV2Error(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MobilePlansV2Error_validator = bv.Struct(MobilePlansV2Error)

class MobilePlansV2RequestArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MobilePlansV2RequestArg_validator = bv.Struct(MobilePlansV2RequestArg)

class MobilePlansV2Response(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MobilePlansV2Response_validator = bv.Struct(MobilePlansV2Response)

class MobileProduct(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MobileProduct_validator = bv.Struct(MobileProduct)

class MobileProductLine(bb.Union):
    pass
# WARNING: Decompyle incomplete

MobileProductLine_validator = bv.Union(MobileProductLine)

class MobileProductV2(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MobileProductV2_validator = bv.Struct(MobileProductV2)

class MobileStore(bb.Union):
    pass
# WARNING: Decompyle incomplete

MobileStore_validator = bv.Union(MobileStore)

class ProductSelectionCriteria(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ProductSelectionCriteria_validator = bv.Struct(ProductSelectionCriteria)

class QuotaInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

QuotaInfo_validator = bv.Struct(QuotaInfo)

class ScheduledTransition(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ScheduledTransition_validator = bv.Struct(ScheduledTransition)

class SubscriptionType(bb.Union):
    pass
# WARNING: Decompyle incomplete

SubscriptionType_validator = bv.Union(SubscriptionType)

class TransitionType(bb.Union):
    pass
# WARNING: Decompyle incomplete

TransitionType_validator = bv.Union(TransitionType)

class TrialInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TrialInfo_validator = bv.Struct(TrialInfo)

class UpgradeMobilePlanRequestArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpgradeMobilePlanRequestArg_validator = bv.Struct(UpgradeMobilePlanRequestArg)

class UpgradeMobilePlanResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpgradeMobilePlanResponse_validator = bv.Struct(UpgradeMobilePlanResponse)

class DetailsUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

DetailsUnion_validator = bv.Union(DetailsUnion)

class DurationUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

DurationUnion_validator = bv.Union(DurationUnion)

class Err2Union(bb.Union):
    pass
# WARNING: Decompyle incomplete

Err2Union_validator = bv.Union(Err2Union)

class ErrUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

ErrUnion_validator = bv.Union(ErrUnion)
ApiProductFamily._unknown_product_family_validator = bv.Void()
ApiProductFamily._plus_validator = bv.Void()
ApiProductFamily._professional_validator = bv.Void()
ApiProductFamily._family_validator = bv.Void()
ApiProductFamily._individual_basic_validator = bv.Void()
ApiProductFamily._transfer_validator = bv.Void()
ApiProductFamily._passwords_validator = bv.Void()
ApiProductFamily._backup_validator = bv.Void()
ApiProductFamily._hellosign_pro_bundle_validator = bv.Void()
ApiProductFamily._plus_deprecated_validator = bv.Void()
ApiProductFamily._hellosign_essentials_validator = bv.Void()
ApiProductFamily._solo_validator = bv.Void()
ApiProductFamily._basic_extra_validator = bv.Void()
ApiProductFamily._dash_validator = bv.Void()
ApiProductFamily._standard_validator = bv.Void()
ApiProductFamily._advanced_validator = bv.Void()
ApiProductFamily._server_validator = bv.Void()
ApiProductFamily._enterprise_validator = bv.Void()
ApiProductFamily._education_validator = bv.Void()
ApiProductFamily._team_basic_validator = bv.Void()
ApiProductFamily._dbx_one_business_validator = bv.Void()
ApiProductFamily._dbx_one_business_plus_validator = bv.Void()
ApiProductFamily._team_deprecated_validator = bv.Void()
ApiProductFamily._hellosign_standard_team_validator = bv.Void()
ApiProductFamily._hellosign_premium_team_validator = bv.Void()
ApiProductFamily._ds_advanced_team_validator = bv.Void()
ApiProductFamily._evh_validator = bv.Void()
ApiProductFamily._quota_validator = bv.Void()
ApiProductFamily._capture_validator = bv.Void()
ApiProductFamily._support_validator = bv.Void()
ApiProductFamily._api_rate_validator = bv.Void()
ApiProductFamily._legal_hold_validator = bv.Void()
ApiProductFamily._premium_support_validator = bv.Void()
ApiProductFamily._media_validator = bv.Void()
ApiProductFamily._local_data_residency_validator = bv.Void()
ApiProductFamily._any_product_family_validator = bv.Void()
ApiProductFamily._other_validator = bv.Void()
# WARNING: Decompyle incomplete
