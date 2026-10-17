# Source Generated with Decompyle++
# File: storefront_platform.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import common

class Addon(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Addon_validator = bv.Struct(Addon)

class AddonAttribute(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AddonAttribute_validator = bv.Struct(AddonAttribute)

class AddonItem(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AddonItem_validator = bv.Struct(AddonItem)

class AddonPrice(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AddonPrice_validator = bv.Struct(AddonPrice)

class AddonProductInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AddonProductInfo_validator = bv.Struct(AddonProductInfo)

class AddonSubscription(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AddonSubscription_validator = bv.Struct(AddonSubscription)

class AddonTransitionPreview(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AddonTransitionPreview_validator = bv.Struct(AddonTransitionPreview)

class ApplePaySpecificPurchaseUserInput(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ApplePaySpecificPurchaseUserInput_validator = bv.Struct(ApplePaySpecificPurchaseUserInput)

class AvailableAddonsQuantities(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AvailableAddonsQuantities_validator = bv.Struct(AvailableAddonsQuantities)

class BillingAddress(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BillingAddress_validator = bv.Struct(BillingAddress)

class BillingHistoryTransaction(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BillingHistoryTransaction_validator = bv.Struct(BillingHistoryTransaction)

class BillingHistoryTransactionLineItem(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BillingHistoryTransactionLineItem_validator = bv.Struct(BillingHistoryTransactionLineItem)

class BlockTransitionReason(bb.Union):
    pass
# WARNING: Decompyle incomplete

BlockTransitionReason_validator = bv.Union(BlockTransitionReason)

class CancellationPreviewResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CancellationPreviewResponse_validator = bv.Struct(CancellationPreviewResponse)

class CancellationRequestToken(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CancellationRequestToken_validator = bv.Struct(CancellationRequestToken)

class CancelledSubscription(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CancelledSubscription_validator = bv.Struct(CancelledSubscription)

class CashAmount(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CashAmount_validator = bv.Struct(CashAmount)

class ContractDaysLeft(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContractDaysLeft_validator = bv.Struct(ContractDaysLeft)

class ContractLength(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContractLength_validator = bv.Struct(ContractLength)

class CreditCardSpecificPurchaseUserInput(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreditCardSpecificPurchaseUserInput_validator = bv.Struct(CreditCardSpecificPurchaseUserInput)

class CurrentPaymentMethod(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CurrentPaymentMethod_validator = bv.Struct(CurrentPaymentMethod)

class CurrentPlan(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CurrentPlan_validator = bv.Struct(CurrentPlan)

class DetailedPrices(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DetailedPrices_validator = bv.Struct(DetailedPrices)

class DirectDebitSpecificPurchaseUserInput(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DirectDebitSpecificPurchaseUserInput_validator = bv.Struct(DirectDebitSpecificPurchaseUserInput)

class Discount(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Discount_validator = bv.Struct(Discount)

class DlocalRbiSpecificPurchaseUserInput(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DlocalRbiSpecificPurchaseUserInput_validator = bv.Struct(DlocalRbiSpecificPurchaseUserInput)

class EligibilityType(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EligibilityType_validator = bv.Struct(EligibilityType)

class FlexibleAddonInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FlexibleAddonInfo_validator = bv.Struct(FlexibleAddonInfo)

class FlexibleAddonRebillInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FlexibleAddonRebillInfo_validator = bv.Struct(FlexibleAddonRebillInfo)

class GrandfatheredStorage(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GrandfatheredStorage_validator = bv.Struct(GrandfatheredStorage)

class IdealSpecificPurchaseUserInput(bb.Struct):
    pass
# WARNING: Decompyle incomplete

IdealSpecificPurchaseUserInput_validator = bv.Struct(IdealSpecificPurchaseUserInput)

class InactiveSubscription(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InactiveSubscription_validator = bv.Struct(InactiveSubscription)

class LicenseInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LicenseInfo_validator = bv.Struct(LicenseInfo)

class LicenseKey(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LicenseKey_validator = bv.Struct(LicenseKey)

class LineItem(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LineItem_validator = bv.Struct(LineItem)

class MultiSeatProperties(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MultiSeatProperties_validator = bv.Struct(MultiSeatProperties)

class NmlVariantValue(bb.Union):
    pass
# WARNING: Decompyle incomplete

NmlVariantValue_validator = bv.Union(NmlVariantValue)

class NonTaxableBillingAddress(bb.Struct):
    pass
# WARNING: Decompyle incomplete

NonTaxableBillingAddress_validator = bv.Struct(NonTaxableBillingAddress)

class OnOffConfigValue(bb.Union):
    pass
# WARNING: Decompyle incomplete

OnOffConfigValue_validator = bv.Union(OnOffConfigValue)

class OnOffControlConfigValue(bb.Union):
    pass
# WARNING: Decompyle incomplete

OnOffControlConfigValue_validator = bv.Union(OnOffControlConfigValue)

class OrderSummary(bb.Struct):
    pass
# WARNING: Decompyle incomplete

OrderSummary_validator = bv.Struct(OrderSummary)

class PaypalSpecificPurchaseUserInput(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PaypalSpecificPurchaseUserInput_validator = bv.Struct(PaypalSpecificPurchaseUserInput)

class PercentageRatioByVolume(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PercentageRatioByVolume_validator = bv.Struct(PercentageRatioByVolume)

class PercentageRatioByVolumeEntry(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PercentageRatioByVolumeEntry_validator = bv.Struct(PercentageRatioByVolumeEntry)

class PerformCancellationResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PerformCancellationResponse_validator = bv.Struct(PerformCancellationResponse)

class PlannedTransition(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PlannedTransition_validator = bv.Struct(PlannedTransition)

class PlannedTransitionType(bb.Union):
    pass
# WARNING: Decompyle incomplete

PlannedTransitionType_validator = bv.Union(PlannedTransitionType)

class PriceVariantValue(bb.Union):
    pass
# WARNING: Decompyle incomplete

PriceVariantValue_validator = bv.Union(PriceVariantValue)

class PricingData(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PricingData_validator = bv.Struct(PricingData)

class PricingToken(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PricingToken_validator = bv.Struct(PricingToken)

class PricingTokenType(bb.Union):
    pass
# WARNING: Decompyle incomplete

PricingTokenType_validator = bv.Union(PricingTokenType)

class ProductInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ProductInfo_validator = bv.Struct(ProductInfo)

class ProductLineInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ProductLineInfo_validator = bv.Struct(ProductLineInfo)

class PromoInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PromoInfo_validator = bv.Struct(PromoInfo)

class PromoProps(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PromoProps_validator = bv.Struct(PromoProps)

class PromoType(bb.Union):
    pass
# WARNING: Decompyle incomplete

PromoType_validator = bv.Union(PromoType)

class PurchaseProductInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PurchaseProductInfo_validator = bv.Struct(PurchaseProductInfo)

class PurchaseTeamInput(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PurchaseTeamInput_validator = bv.Struct(PurchaseTeamInput)

class PurchaseUserInput(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PurchaseUserInput_validator = bv.Struct(PurchaseUserInput)

class RevApiPlannedTransition(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RevApiPlannedTransition_validator = bv.Struct(RevApiPlannedTransition)

class RevApiPricingToken(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RevApiPricingToken_validator = bv.Struct(RevApiPricingToken)

class RevApiSubscriptionChangeInput(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RevApiSubscriptionChangeInput_validator = bv.Struct(RevApiSubscriptionChangeInput)

class Schedule(bb.Union):
    pass
# WARNING: Decompyle incomplete

Schedule_validator = bv.Union(Schedule)

class ScheduledActionType(bb.Union):
    pass
# WARNING: Decompyle incomplete

ScheduledActionType_validator = bv.Union(ScheduledActionType)

class ScheduledChangesInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ScheduledChangesInfo_validator = bv.Struct(ScheduledChangesInfo)

class ScheduledChangesMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ScheduledChangesMetadata_validator = bv.Struct(ScheduledChangesMetadata)

class StorageUsageData(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StorageUsageData_validator = bv.Struct(StorageUsageData)

class StorefrontPlatformAiCreditPurchaseAction(bb.Union):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformAiCreditPurchaseAction_validator = bv.Union(StorefrontPlatformAiCreditPurchaseAction)

class StorefrontPlatformBillLineItemType(bb.Union):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformBillLineItemType_validator = bv.Union(StorefrontPlatformBillLineItemType)

class StorefrontPlatformBillStatus(bb.Union):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformBillStatus_validator = bv.Union(StorefrontPlatformBillStatus)

class StorefrontPlatformBillTransactionType(bb.Union):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformBillTransactionType_validator = bv.Union(StorefrontPlatformBillTransactionType)

class StorefrontPlatformBillingProvider(bb.Union):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformBillingProvider_validator = bv.Union(StorefrontPlatformBillingProvider)

class StorefrontPlatformConfiguration(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformConfiguration_validator = bv.Struct(StorefrontPlatformConfiguration)

class StorefrontPlatformContractLengthUnit(bb.Union):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformContractLengthUnit_validator = bv.Union(StorefrontPlatformContractLengthUnit)

class StorefrontPlatformCreditType(bb.Union):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformCreditType_validator = bv.Union(StorefrontPlatformCreditType)

class StorefrontPlatformPaymentMethod(bb.Union):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformPaymentMethod_validator = bv.Union(StorefrontPlatformPaymentMethod)

class StorefrontPlatformProductCategory(bb.Union):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformProductCategory_validator = bv.Union(StorefrontPlatformProductCategory)

class StorefrontPlatformProductLine(bb.Union):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformProductLine_validator = bv.Union(StorefrontPlatformProductLine)

class StorefrontPlatformProductRegistryKey(bb.Union):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformProductRegistryKey_validator = bv.Union(StorefrontPlatformProductRegistryKey)

class StorefrontPlatformProductType(bb.Union):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformProductType_validator = bv.Union(StorefrontPlatformProductType)

class StorefrontPlatformTrialBannerConfig(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformTrialBannerConfig_validator = bv.Struct(StorefrontPlatformTrialBannerConfig)

class StorefrontPlatformTrialCancelExpectations(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformTrialCancelExpectations_validator = bv.Struct(StorefrontPlatformTrialCancelExpectations)

class StorefrontPlatformTrialCancelSurvey(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformTrialCancelSurvey_validator = bv.Struct(StorefrontPlatformTrialCancelSurvey)

class StorefrontPlatformTrialChangePerformResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformTrialChangePerformResponse_validator = bv.Struct(StorefrontPlatformTrialChangePerformResponse)

class StorefrontPlatformTrialChangePreviewResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformTrialChangePreviewResponse_validator = bv.Struct(StorefrontPlatformTrialChangePreviewResponse)

class StorefrontPlatformTrialConfigInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformTrialConfigInfo_validator = bv.Struct(StorefrontPlatformTrialConfigInfo)

class StorefrontPlatformTrialConfigModel(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformTrialConfigModel_validator = bv.Struct(StorefrontPlatformTrialConfigModel)

class StorefrontPlatformTrialCtaConfig(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformTrialCtaConfig_validator = bv.Struct(StorefrontPlatformTrialCtaConfig)

class StorefrontPlatformTrialCtaModuleName(bb.Union):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformTrialCtaModuleName_validator = bv.Union(StorefrontPlatformTrialCtaModuleName)

class StorefrontPlatformTrialOnClickType(bb.Union):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformTrialOnClickType_validator = bv.Union(StorefrontPlatformTrialOnClickType)

class StorefrontPlatformTrialStartAutoConvertArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformTrialStartAutoConvertArgs_validator = bv.Struct(StorefrontPlatformTrialStartAutoConvertArgs)

class StorefrontPlatformTrialStartAutoConvertBrowserArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformTrialStartAutoConvertBrowserArgs_validator = bv.Struct(StorefrontPlatformTrialStartAutoConvertBrowserArgs)

class StorefrontPlatformTrialStartPreview(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformTrialStartPreview_validator = bv.Struct(StorefrontPlatformTrialStartPreview)

class StorefrontPlatformTrialStartResultView(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformTrialStartResultView_validator = bv.Struct(StorefrontPlatformTrialStartResultView)

class StorefrontPlatformTrialsProjectType(bb.Union):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformTrialsProjectType_validator = bv.Union(StorefrontPlatformTrialsProjectType)

class StorefrontPlatformTrialsTrialPlan(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StorefrontPlatformTrialsTrialPlan_validator = bv.Struct(StorefrontPlatformTrialsTrialPlan)

class StripeSpecificPurchaseUserInput(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StripeSpecificPurchaseUserInput_validator = bv.Struct(StripeSpecificPurchaseUserInput)

class SubscriptionEligibility(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SubscriptionEligibility_validator = bv.Struct(SubscriptionEligibility)

class SubscriptionIneligibilityReason(bb.Union):
    pass
# WARNING: Decompyle incomplete

SubscriptionIneligibilityReason_validator = bv.Union(SubscriptionIneligibilityReason)

class SubscriptionInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SubscriptionInfo_validator = bv.Struct(SubscriptionInfo)

class SubscriptionMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SubscriptionMetadata_validator = bv.Struct(SubscriptionMetadata)

class SubscriptionServicePlannedTransition(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SubscriptionServicePlannedTransition_validator = bv.Struct(SubscriptionServicePlannedTransition)

class SubscriptionServicePricingToken(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SubscriptionServicePricingToken_validator = bv.Struct(SubscriptionServicePricingToken)

class TagContext(bb.Union):
    pass
# WARNING: Decompyle incomplete

TagContext_validator = bv.Union(TagContext)

class TaxInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TaxInfo_validator = bv.Struct(TaxInfo)

class TaxItem(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TaxItem_validator = bv.Struct(TaxItem)

class TeamProperties(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TeamProperties_validator = bv.Struct(TeamProperties)

class TransitionPriceQuote(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TransitionPriceQuote_validator = bv.Struct(TransitionPriceQuote)

class TransitionResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TransitionResult_validator = bv.Struct(TransitionResult)

class Trial(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Trial_validator = bv.Struct(Trial)

class TrialCancellationPreviewResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TrialCancellationPreviewResponse_validator = bv.Struct(TrialCancellationPreviewResponse)

class UpcomingTotals(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpcomingTotals_validator = bv.Struct(UpcomingTotals)

class PaymentMethodSpecificUserInputUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

PaymentMethodSpecificUserInputUnion_validator = bv.Union(PaymentMethodSpecificUserInputUnion)

class PlannedTransitionUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

PlannedTransitionUnion_validator = bv.Union(PlannedTransitionUnion)

class StateUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

StateUnion_validator = bv.Union(StateUnion)

class TokenUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

TokenUnion_validator = bv.Union(TokenUnion)
Addon.offering_id.validator = bv.String()
Addon.offering_id.validator._redact = bv.BlotRedactor(None)
Addon.name.validator = bv.String()
Addon.name.validator._redact = bv.BlotRedactor(None)
Addon.description.validator = bv.String()
Addon.description.validator._redact = bv.BlotRedactor(None)
Addon.formatted_total_amount.validator = bv.String()
Addon.formatted_total_amount.validator._redact = bv.BlotRedactor(None)
Addon.addon_family.validator = bv.String()
Addon.addon_family.validator._redact = bv.BlotRedactor(None)
Addon.is_license_based.validator = bv.Boolean()
Addon.is_license_based.validator._redact = bv.BlotRedactor(None)
Addon.addon_attribute.validator = bv.Nullable(AddonAttribute_validator)
Addon.product_type.validator = StorefrontPlatformProductType_validator
Addon.add_text.validator = bv.String()
Addon.add_text.validator._redact = bv.BlotRedactor(None)
Addon.remove_text.validator = bv.String()
Addon.remove_text.validator._redact = bv.BlotRedactor(None)
Addon.details_link.validator = bv.String()
Addon.details_link.validator._redact = bv.BlotRedactor(None)
Addon.is_stackable.validator = bv.Boolean()
Addon.is_stackable.validator._redact = bv.BlotRedactor(None)
Addon.addon_sub_family.validator = bv.String()
Addon.addon_sub_family.validator._redact = bv.BlotRedactor(None)
Addon.is_paid_addon.validator = bv.Boolean()
Addon.is_paid_addon.validator._redact = bv.BlotRedactor(None)
Addon.product_id.validator = bv.String()
Addon.product_id.validator._redact = bv.BlotRedactor(None)
Addon.is_partial_provisionable.validator = bv.Boolean()
Addon.is_partial_provisionable.validator._redact = bv.BlotRedactor(None)
Addon.has_promo.validator = bv.Boolean()
Addon.has_promo.validator._redact = bv.BlotRedactor(None)
Addon.product_category.validator = StorefrontPlatformProductCategory_validator
Addon.trial_add_text.validator = bv.String()
Addon.trial_add_text.validator._redact = bv.BlotRedactor(None)
Addon.is_trial.validator = bv.Boolean()
Addon.is_trial.validator._redact = bv.BlotRedactor(None)
Addon._all_field_names_ = set([
    'offering_id',
    'name',
    'description',
    'formatted_total_amount',
    'addon_family',
    'is_license_based',
    'addon_attribute',
    'product_type',
    'add_text',
    'remove_text',
    'details_link',
    'is_stackable',
    'addon_sub_family',
    'is_paid_addon',
    'product_id',
    'is_partial_provisionable',
    'has_promo',
    'product_category',
    'trial_add_text',
    'is_trial'])
Addon._all_fields_ = [
    ('offering_id', Addon.offering_id.validator),
    ('name', Addon.name.validator),
    ('description', Addon.description.validator),
    ('formatted_total_amount', Addon.formatted_total_amount.validator),
    ('addon_family', Addon.addon_family.validator),
    ('is_license_based', Addon.is_license_based.validator),
    ('addon_attribute', Addon.addon_attribute.validator),
    ('product_type', Addon.product_type.validator),
    ('add_text', Addon.add_text.validator),
    ('remove_text', Addon.remove_text.validator),
    ('details_link', Addon.details_link.validator),
    ('is_stackable', Addon.is_stackable.validator),
    ('addon_sub_family', Addon.addon_sub_family.validator),
    ('is_paid_addon', Addon.is_paid_addon.validator),
    ('product_id', Addon.product_id.validator),
    ('is_partial_provisionable', Addon.is_partial_provisionable.validator),
    ('has_promo', Addon.has_promo.validator),
    ('product_category', Addon.product_category.validator),
    ('trial_add_text', Addon.trial_add_text.validator),
    ('is_trial', Addon.is_trial.validator)]
AddonAttribute.attribute_name.validator = bv.String()
AddonAttribute.attribute_name.validator._redact = bv.BlotRedactor(None)
AddonAttribute.attribute_value.validator = bv.String()
AddonAttribute.attribute_value.validator._redact = bv.BlotRedactor(None)
AddonAttribute.attribute_formatted_value.validator = bv.String()
AddonAttribute.attribute_formatted_value.validator._redact = bv.BlotRedactor(None)
AddonAttribute.vacuuming_policy_max_days.validator = bv.String()
AddonAttribute.vacuuming_policy_max_days.validator._redact = bv.BlotRedactor(None)
AddonAttribute.quota_gb.validator = bv.String()
AddonAttribute.quota_gb.validator._redact = bv.BlotRedactor(None)
AddonAttribute.ai_credit_count.validator = bv.UInt32()
AddonAttribute.ai_credit_count.validator._redact = bv.BlotRedactor(None)
AddonAttribute.is_ac1m.validator = bv.Boolean()
AddonAttribute.is_ac1m.validator._redact = bv.BlotRedactor(None)
AddonAttribute._all_field_names_ = set([
    'attribute_name',
    'attribute_value',
    'attribute_formatted_value',
    'vacuuming_policy_max_days',
    'quota_gb',
    'ai_credit_count',
    'is_ac1m'])
AddonAttribute._all_fields_ = [
    ('attribute_name', AddonAttribute.attribute_name.validator),
    ('attribute_value', AddonAttribute.attribute_value.validator),
    ('attribute_formatted_value', AddonAttribute.attribute_formatted_value.validator),
    ('vacuuming_policy_max_days', AddonAttribute.vacuuming_policy_max_days.validator),
    ('quota_gb', AddonAttribute.quota_gb.validator),
    ('ai_credit_count', AddonAttribute.ai_credit_count.validator),
    ('is_ac1m', AddonAttribute.is_ac1m.validator)]
AddonItem.display_price.validator = bv.String()
AddonItem.display_price.validator._redact = bv.BlotRedactor(None)
AddonItem.display_name.validator = bv.String()
AddonItem.display_name.validator._redact = bv.BlotRedactor(None)
AddonItem.offering_id.validator = bv.String()
AddonItem.offering_id.validator._redact = bv.BlotRedactor(None)
AddonItem.quantity.validator = bv.UInt32()
AddonItem.quantity.validator._redact = bv.BlotRedactor(None)
AddonItem._all_field_names_ = set([
    'display_price',
    'display_name',
    'offering_id',
    'quantity'])
AddonItem._all_fields_ = [
    ('display_price', AddonItem.display_price.validator),
    ('display_name', AddonItem.display_name.validator),
    ('offering_id', AddonItem.offering_id.validator),
    ('quantity', AddonItem.quantity.validator)]
AddonPrice.addon_type.validator = StorefrontPlatformProductType_validator
AddonPrice.price.validator = bv.Nullable(CashAmount_validator)
AddonPrice.base_price.validator = bv.Nullable(CashAmount_validator)
AddonPrice.num_licenses.validator = bv.Int64()
AddonPrice.num_licenses.validator._redact = bv.BlotRedactor(None)
AddonPrice.per_user_price.validator = bv.Nullable(CashAmount_validator)
AddonPrice.per_user_base_price.validator = bv.Nullable(CashAmount_validator)
AddonPrice._all_field_names_ = set([
    'addon_type',
    'price',
    'base_price',
    'num_licenses',
    'per_user_price',
    'per_user_base_price'])
AddonPrice._all_fields_ = [
    ('addon_type', AddonPrice.addon_type.validator),
    ('price', AddonPrice.price.validator),
    ('base_price', AddonPrice.base_price.validator),
    ('num_licenses', AddonPrice.num_licenses.validator),
    ('per_user_price', AddonPrice.per_user_price.validator),
    ('per_user_base_price', AddonPrice.per_user_base_price.validator)]
AddonProductInfo.product_type.validator = StorefrontPlatformProductType_validator
AddonProductInfo.num_licenses.validator = bv.Int64()
AddonProductInfo.num_licenses.validator._redact = bv.BlotRedactor(None)
AddonProductInfo.offering_id.validator = bv.String()
AddonProductInfo.offering_id.validator._redact = bv.BlotRedactor(None)
AddonProductInfo._all_field_names_ = set([
    'product_type',
    'num_licenses',
    'offering_id'])
AddonProductInfo._all_fields_ = [
    ('product_type', AddonProductInfo.product_type.validator),
    ('num_licenses', AddonProductInfo.num_licenses.validator),
    ('offering_id', AddonProductInfo.offering_id.validator)]
AddonSubscription.addon.validator = bv.Nullable(Addon_validator)
AddonSubscription.quantity_scheduled_for_removal.validator = bv.UInt32()
AddonSubscription.quantity_scheduled_for_removal.validator._redact = bv.BlotRedactor(None)
AddonSubscription.total_quantity.validator = bv.UInt32()
AddonSubscription.total_quantity.validator._redact = bv.BlotRedactor(None)
AddonSubscription.min_quantity_required.validator = bv.UInt32()
AddonSubscription.min_quantity_required.validator._redact = bv.BlotRedactor(None)
AddonSubscription.max_quantity_allowed.validator = bv.UInt32()
AddonSubscription.max_quantity_allowed.validator._redact = bv.BlotRedactor(None)
AddonSubscription.is_partial_provisionable.validator = bv.Boolean()
AddonSubscription.is_partial_provisionable.validator._redact = bv.BlotRedactor(None)
AddonSubscription.quantity_scheduled_for_removal_on_next_bill.validator = bv.UInt32()
AddonSubscription.quantity_scheduled_for_removal_on_next_bill.validator._redact = bv.BlotRedactor(None)
AddonSubscription.scheduled_removal_effective_date.validator = bv.Nullable(common.DropboxTimestamp_validator)
AddonSubscription._all_field_names_ = set([
    'addon',
    'quantity_scheduled_for_removal',
    'total_quantity',
    'min_quantity_required',
    'max_quantity_allowed',
    'is_partial_provisionable',
    'quantity_scheduled_for_removal_on_next_bill',
    'scheduled_removal_effective_date'])
AddonSubscription._all_fields_ = [
    ('addon', AddonSubscription.addon.validator),
    ('quantity_scheduled_for_removal', AddonSubscription.quantity_scheduled_for_removal.validator),
    ('total_quantity', AddonSubscription.total_quantity.validator),
    ('min_quantity_required', AddonSubscription.min_quantity_required.validator),
    ('max_quantity_allowed', AddonSubscription.max_quantity_allowed.validator),
    ('is_partial_provisionable', AddonSubscription.is_partial_provisionable.validator),
    ('quantity_scheduled_for_removal_on_next_bill', AddonSubscription.quantity_scheduled_for_removal_on_next_bill.validator),
    ('scheduled_removal_effective_date', AddonSubscription.scheduled_removal_effective_date.validator)]
AddonTransitionPreview.upcoming_bill_date.validator = bv.String()
AddonTransitionPreview.upcoming_bill_date.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.upcoming_bill_total_price.validator = bv.String()
AddonTransitionPreview.upcoming_bill_total_price.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.upcoming_bill_addon_price.validator = bv.String()
AddonTransitionPreview.upcoming_bill_addon_price.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.current_bill_addon_price.validator = bv.String()
AddonTransitionPreview.current_bill_addon_price.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.total_includes_taxes.validator = bv.Boolean()
AddonTransitionPreview.total_includes_taxes.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.preview_request_token.validator = bv.String()
AddonTransitionPreview.preview_request_token.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.active_payment_method_type.validator = StorefrontPlatformPaymentMethod_validator
AddonTransitionPreview.last_digits.validator = bv.String()
AddonTransitionPreview.last_digits.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.addon_change_quantity.validator = bv.Int32()
AddonTransitionPreview.addon_change_quantity.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.offering_id_change_quantity_map.validator = bv.Nullable(bv.Map(bv.String(), bv.UInt32()))
AddonTransitionPreview.upcoming_bill_addon_prices.validator = bv.Nullable(bv.Map(bv.String(), bv.String()))
AddonTransitionPreview.current_bill_addon_prices.validator = bv.Nullable(bv.Map(bv.String(), bv.String()))
AddonTransitionPreview.upcoming_contract_length.validator = bv.String()
AddonTransitionPreview.upcoming_contract_length.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.tax_items.validator = bv.Nullable(bv.List(TaxItem_validator))
AddonTransitionPreview.card_issuer.validator = bv.String()
AddonTransitionPreview.card_issuer.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.billing_country_code.validator = bv.String()
AddonTransitionPreview.billing_country_code.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.payment_method_expiration_date.validator = bv.String()
AddonTransitionPreview.payment_method_expiration_date.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.currency.validator = bv.String()
AddonTransitionPreview.currency.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.advertised_yearly_savings_percentage.validator = bv.UInt32()
AddonTransitionPreview.advertised_yearly_savings_percentage.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.is_prorated.validator = bv.Boolean()
AddonTransitionPreview.is_prorated.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.upcoming_bill_addon_amount.validator = bv.Nullable(CashAmount_validator)
AddonTransitionPreview.current_bill_addon_amount.validator = bv.Nullable(CashAmount_validator)
AddonTransitionPreview.base_plan_ai_credits.validator = bv.UInt32()
AddonTransitionPreview.base_plan_ai_credits.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.next_addon_bill_date.validator = bv.String()
AddonTransitionPreview.next_addon_bill_date.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview.base_plan_renewal_price.validator = bv.String()
AddonTransitionPreview.base_plan_renewal_price.validator._redact = bv.BlotRedactor(None)
AddonTransitionPreview._all_field_names_ = set([
    'upcoming_bill_date',
    'upcoming_bill_total_price',
    'upcoming_bill_addon_price',
    'current_bill_addon_price',
    'total_includes_taxes',
    'preview_request_token',
    'active_payment_method_type',
    'last_digits',
    'addon_change_quantity',
    'offering_id_change_quantity_map',
    'upcoming_bill_addon_prices',
    'current_bill_addon_prices',
    'upcoming_contract_length',
    'tax_items',
    'card_issuer',
    'billing_country_code',
    'payment_method_expiration_date',
    'currency',
    'advertised_yearly_savings_percentage',
    'is_prorated',
    'upcoming_bill_addon_amount',
    'current_bill_addon_amount',
    'base_plan_ai_credits',
    'next_addon_bill_date',
    'base_plan_renewal_price'])
AddonTransitionPreview._all_fields_ = [
    ('upcoming_bill_date', AddonTransitionPreview.upcoming_bill_date.validator),
    ('upcoming_bill_total_price', AddonTransitionPreview.upcoming_bill_total_price.validator),
    ('upcoming_bill_addon_price', AddonTransitionPreview.upcoming_bill_addon_price.validator),
    ('current_bill_addon_price', AddonTransitionPreview.current_bill_addon_price.validator),
    ('total_includes_taxes', AddonTransitionPreview.total_includes_taxes.validator),
    ('preview_request_token', AddonTransitionPreview.preview_request_token.validator),
    ('active_payment_method_type', AddonTransitionPreview.active_payment_method_type.validator),
    ('last_digits', AddonTransitionPreview.last_digits.validator),
    ('addon_change_quantity', AddonTransitionPreview.addon_change_quantity.validator),
    ('offering_id_change_quantity_map', AddonTransitionPreview.offering_id_change_quantity_map.validator),
    ('upcoming_bill_addon_prices', AddonTransitionPreview.upcoming_bill_addon_prices.validator),
    ('current_bill_addon_prices', AddonTransitionPreview.current_bill_addon_prices.validator),
    ('upcoming_contract_length', AddonTransitionPreview.upcoming_contract_length.validator),
    ('tax_items', AddonTransitionPreview.tax_items.validator),
    ('card_issuer', AddonTransitionPreview.card_issuer.validator),
    ('billing_country_code', AddonTransitionPreview.billing_country_code.validator),
    ('payment_method_expiration_date', AddonTransitionPreview.payment_method_expiration_date.validator),
    ('currency', AddonTransitionPreview.currency.validator),
    ('advertised_yearly_savings_percentage', AddonTransitionPreview.advertised_yearly_savings_percentage.validator),
    ('is_prorated', AddonTransitionPreview.is_prorated.validator),
    ('upcoming_bill_addon_amount', AddonTransitionPreview.upcoming_bill_addon_amount.validator),
    ('current_bill_addon_amount', AddonTransitionPreview.current_bill_addon_amount.validator),
    ('base_plan_ai_credits', AddonTransitionPreview.base_plan_ai_credits.validator),
    ('next_addon_bill_date', AddonTransitionPreview.next_addon_bill_date.validator),
    ('base_plan_renewal_price', AddonTransitionPreview.base_plan_renewal_price.validator)]
ApplePaySpecificPurchaseUserInput.apple_pay_token.validator = bv.String()
ApplePaySpecificPurchaseUserInput.apple_pay_token.validator._redact = bv.BlotRedactor(None)
ApplePaySpecificPurchaseUserInput.apple_pay_card_last_four.validator = bv.String()
ApplePaySpecificPurchaseUserInput.apple_pay_card_last_four.validator._redact = bv.BlotRedactor(None)
ApplePaySpecificPurchaseUserInput._all_field_names_ = set([
    'apple_pay_token',
    'apple_pay_card_last_four'])
ApplePaySpecificPurchaseUserInput._all_fields_ = [
    ('apple_pay_token', ApplePaySpecificPurchaseUserInput.apple_pay_token.validator),
    ('apple_pay_card_last_four', ApplePaySpecificPurchaseUserInput.apple_pay_card_last_four.validator)]
AvailableAddonsQuantities.offering_id.validator = bv.String()
AvailableAddonsQuantities.offering_id.validator._redact = bv.BlotRedactor(None)
AvailableAddonsQuantities.min_quantity_required.validator = bv.Int32()
AvailableAddonsQuantities.min_quantity_required.validator._redact = bv.BlotRedactor(None)
AvailableAddonsQuantities.max_quantity_allowed.validator = bv.Int32()
AvailableAddonsQuantities.max_quantity_allowed.validator._redact = bv.BlotRedactor(None)
AvailableAddonsQuantities._all_field_names_ = set([
    'offering_id',
    'min_quantity_required',
    'max_quantity_allowed'])
AvailableAddonsQuantities._all_fields_ = [
    ('offering_id', AvailableAddonsQuantities.offering_id.validator),
    ('min_quantity_required', AvailableAddonsQuantities.min_quantity_required.validator),
    ('max_quantity_allowed', AvailableAddonsQuantities.max_quantity_allowed.validator)]
BillingAddress.non_taxable_info.validator = bv.Nullable(NonTaxableBillingAddress_validator)
BillingAddress.taxable_info.validator = bv.Nullable(TaxInfo_validator)
BillingAddress._all_field_names_ = set([
    'non_taxable_info',
    'taxable_info'])
BillingAddress._all_fields_ = [
    ('non_taxable_info', BillingAddress.non_taxable_info.validator),
    ('taxable_info', BillingAddress.taxable_info.validator)]
BillingHistoryTransaction.bill_id.validator = bv.String()
BillingHistoryTransaction.bill_id.validator._redact = bv.BlotRedactor(None)
BillingHistoryTransaction.line_items.validator = bv.Nullable(bv.List(BillingHistoryTransactionLineItem_validator))
BillingHistoryTransaction.date.validator = bv.String()
BillingHistoryTransaction.date.validator._redact = bv.BlotRedactor(None)
BillingHistoryTransaction.total_amount.validator = bv.Nullable(CashAmount_validator)
BillingHistoryTransaction.status.validator = StorefrontPlatformBillStatus_validator
BillingHistoryTransaction.has_promotion.validator = bv.Boolean()
BillingHistoryTransaction.has_promotion.validator._redact = bv.BlotRedactor(None)
BillingHistoryTransaction.is_billing_address_updatable.validator = bv.Boolean()
BillingHistoryTransaction.is_billing_address_updatable.validator._redact = bv.BlotRedactor(None)
BillingHistoryTransaction.transaction_type.validator = StorefrontPlatformBillTransactionType_validator
BillingHistoryTransaction.total_amount_formatted.validator = bv.String()
BillingHistoryTransaction.total_amount_formatted.validator._redact = bv.BlotRedactor(None)
BillingHistoryTransaction._all_field_names_ = set([
    'bill_id',
    'line_items',
    'date',
    'total_amount',
    'status',
    'has_promotion',
    'is_billing_address_updatable',
    'transaction_type',
    'total_amount_formatted'])
BillingHistoryTransaction._all_fields_ = [
    ('bill_id', BillingHistoryTransaction.bill_id.validator),
    ('line_items', BillingHistoryTransaction.line_items.validator),
    ('date', BillingHistoryTransaction.date.validator),
    ('total_amount', BillingHistoryTransaction.total_amount.validator),
    ('status', BillingHistoryTransaction.status.validator),
    ('has_promotion', BillingHistoryTransaction.has_promotion.validator),
    ('is_billing_address_updatable', BillingHistoryTransaction.is_billing_address_updatable.validator),
    ('transaction_type', BillingHistoryTransaction.transaction_type.validator),
    ('total_amount_formatted', BillingHistoryTransaction.total_amount_formatted.validator)]
BillingHistoryTransactionLineItem.offering_description.validator = bv.String()
BillingHistoryTransactionLineItem.offering_description.validator._redact = bv.BlotRedactor(None)
BillingHistoryTransactionLineItem.quantity.validator = bv.Int32()
BillingHistoryTransactionLineItem.quantity.validator._redact = bv.BlotRedactor(None)
BillingHistoryTransactionLineItem.start_date.validator = bv.String()
BillingHistoryTransactionLineItem.start_date.validator._redact = bv.BlotRedactor(None)
BillingHistoryTransactionLineItem.end_date.validator = bv.String()
BillingHistoryTransactionLineItem.end_date.validator._redact = bv.BlotRedactor(None)
BillingHistoryTransactionLineItem.type.validator = StorefrontPlatformBillLineItemType_validator
BillingHistoryTransactionLineItem.offering_type.validator = StorefrontPlatformProductCategory_validator
BillingHistoryTransactionLineItem._all_field_names_ = set([
    'offering_description',
    'quantity',
    'start_date',
    'end_date',
    'type',
    'offering_type'])
BillingHistoryTransactionLineItem._all_fields_ = [
    ('offering_description', BillingHistoryTransactionLineItem.offering_description.validator),
    ('quantity', BillingHistoryTransactionLineItem.quantity.validator),
    ('start_date', BillingHistoryTransactionLineItem.start_date.validator),
    ('end_date', BillingHistoryTransactionLineItem.end_date.validator),
    ('type', BillingHistoryTransactionLineItem.type.validator),
    ('offering_type', BillingHistoryTransactionLineItem.offering_type.validator)]
BlockTransitionReason._none_validator = bv.Void()
BlockTransitionReason._over_quota_validator = bv.Void()
BlockTransitionReason._exceeds_quota_cap_validator = bv.Void()
BlockTransitionReason._other_validator = bv.Void()
BlockTransitionReason._tagmap = {
    'none': BlockTransitionReason._none_validator,
    'over_quota': BlockTransitionReason._over_quota_validator,
    'exceeds_quota_cap': BlockTransitionReason._exceeds_quota_cap_validator,
    'other': BlockTransitionReason._other_validator }
BlockTransitionReason.none = BlockTransitionReason('none')
BlockTransitionReason.over_quota = BlockTransitionReason('over_quota')
BlockTransitionReason.exceeds_quota_cap = BlockTransitionReason('exceeds_quota_cap')
BlockTransitionReason.other = BlockTransitionReason('other')
CancellationPreviewResponse.contract_expiration_date.validator = bv.String()
CancellationPreviewResponse.contract_expiration_date.validator._redact = bv.BlotRedactor(None)
CancellationPreviewResponse.is_eligible_for_refund.validator = bv.Boolean()
CancellationPreviewResponse.is_eligible_for_refund.validator._redact = bv.BlotRedactor(None)
CancellationPreviewResponse.cancellation_request_token.validator = bv.String()
CancellationPreviewResponse.cancellation_request_token.validator._redact = bv.BlotRedactor(None)
CancellationPreviewResponse.subscription_id.validator = bv.String()
CancellationPreviewResponse.subscription_id.validator._redact = bv.BlotRedactor(None)
CancellationPreviewResponse.refund_request_token.validator = bv.String()
CancellationPreviewResponse.refund_request_token.validator._redact = bv.BlotRedactor(None)
CancellationPreviewResponse.is_contract_expired.validator = bv.Boolean()
CancellationPreviewResponse.is_contract_expired.validator._redact = bv.BlotRedactor(None)
CancellationPreviewResponse._all_field_names_ = set([
    'contract_expiration_date',
    'is_eligible_for_refund',
    'cancellation_request_token',
    'subscription_id',
    'refund_request_token',
    'is_contract_expired'])
CancellationPreviewResponse._all_fields_ = [
    ('contract_expiration_date', CancellationPreviewResponse.contract_expiration_date.validator),
    ('is_eligible_for_refund', CancellationPreviewResponse.is_eligible_for_refund.validator),
    ('cancellation_request_token', CancellationPreviewResponse.cancellation_request_token.validator),
    ('subscription_id', CancellationPreviewResponse.subscription_id.validator),
    ('refund_request_token', CancellationPreviewResponse.refund_request_token.validator),
    ('is_contract_expired', CancellationPreviewResponse.is_contract_expired.validator)]
CancellationRequestToken.token_type.validator = PricingTokenType_validator
CancellationRequestToken.value.validator = bv.String()
CancellationRequestToken.value.validator._redact = bv.BlotRedactor(None)
CancellationRequestToken._all_field_names_ = set([
    'token_type',
    'value'])
CancellationRequestToken._all_fields_ = [
    ('token_type', CancellationRequestToken.token_type.validator),
    ('value', CancellationRequestToken.value.validator)]
CancelledSubscription.is_eligible_to_resubscribe.validator = bv.Boolean()
CancelledSubscription.is_eligible_to_resubscribe.validator._redact = bv.BlotRedactor(None)
CancelledSubscription.product_type.validator = StorefrontPlatformProductType_validator
CancelledSubscription.product_category.validator = StorefrontPlatformProductCategory_validator
CancelledSubscription.plan_display_name.validator = bv.String()
CancelledSubscription.plan_display_name.validator._redact = bv.BlotRedactor(None)
CancelledSubscription.contract_length.validator = bv.Nullable(ContractLength_validator)
CancelledSubscription.plan_current_cost.validator = bv.String()
CancelledSubscription.plan_current_cost.validator._redact = bv.BlotRedactor(None)
CancelledSubscription.purchase_endpoint.validator = bv.String()
CancelledSubscription.purchase_endpoint.validator._redact = bv.BlotRedactor(None)
CancelledSubscription.product_details_endpoint.validator = bv.String()
CancelledSubscription.product_details_endpoint.validator._redact = bv.BlotRedactor(None)
CancelledSubscription._all_field_names_ = set([
    'is_eligible_to_resubscribe',
    'product_type',
    'product_category',
    'plan_display_name',
    'contract_length',
    'plan_current_cost',
    'purchase_endpoint',
    'product_details_endpoint'])
CancelledSubscription._all_fields_ = [
    ('is_eligible_to_resubscribe', CancelledSubscription.is_eligible_to_resubscribe.validator),
    ('product_type', CancelledSubscription.product_type.validator),
    ('product_category', CancelledSubscription.product_category.validator),
    ('plan_display_name', CancelledSubscription.plan_display_name.validator),
    ('contract_length', CancelledSubscription.contract_length.validator),
    ('plan_current_cost', CancelledSubscription.plan_current_cost.validator),
    ('purchase_endpoint', CancelledSubscription.purchase_endpoint.validator),
    ('product_details_endpoint', CancelledSubscription.product_details_endpoint.validator)]
CashAmount.amount.validator = bv.String()
CashAmount.amount.validator._redact = bv.BlotRedactor(None)
CashAmount.currency.validator = bv.String()
CashAmount.currency.validator._redact = bv.BlotRedactor(None)
CashAmount._all_field_names_ = set([
    'amount',
    'currency'])
CashAmount._all_fields_ = [
    ('amount', CashAmount.amount.validator),
    ('currency', CashAmount.currency.validator)]
ContractDaysLeft.state.validator = bv.Nullable(StateUnion_validator)
ContractDaysLeft._all_field_names_ = set([
    'state'])
ContractDaysLeft._all_fields_ = [
    ('state', ContractDaysLeft.state.validator)]
ContractLength.contract_length_quantity.validator = bv.UInt64()
ContractLength.contract_length_quantity.validator._redact = bv.BlotRedactor(None)
ContractLength.contract_length_unit.validator = StorefrontPlatformContractLengthUnit_validator
ContractLength._all_field_names_ = set([
    'contract_length_quantity',
    'contract_length_unit'])
ContractLength._all_fields_ = [
    ('contract_length_quantity', ContractLength.contract_length_quantity.validator),
    ('contract_length_unit', ContractLength.contract_length_unit.validator)]
CreditCardSpecificPurchaseUserInput.ccn.validator = bv.String()
CreditCardSpecificPurchaseUserInput.ccn.validator._redact = bv.BlotRedactor(None)
CreditCardSpecificPurchaseUserInput.ccode.validator = bv.String()
CreditCardSpecificPurchaseUserInput.ccode.validator._redact = bv.BlotRedactor(None)
CreditCardSpecificPurchaseUserInput.expmo.validator = bv.String()
CreditCardSpecificPurchaseUserInput.expmo.validator._redact = bv.BlotRedactor(None)
CreditCardSpecificPurchaseUserInput.expyr.validator = bv.String()
CreditCardSpecificPurchaseUserInput.expyr.validator._redact = bv.BlotRedactor(None)
CreditCardSpecificPurchaseUserInput.bin.validator = bv.String()
CreditCardSpecificPurchaseUserInput.bin.validator._redact = bv.BlotRedactor(None)
CreditCardSpecificPurchaseUserInput.cpf.validator = bv.String()
CreditCardSpecificPurchaseUserInput.cpf.validator._redact = bv.BlotRedactor(None)
CreditCardSpecificPurchaseUserInput.cpf_name.validator = bv.String()
CreditCardSpecificPurchaseUserInput.cpf_name.validator._redact = bv.BlotRedactor(None)
CreditCardSpecificPurchaseUserInput.adyen_encrypted_card.validator = bv.String()
CreditCardSpecificPurchaseUserInput.adyen_encrypted_card.validator._redact = bv.BlotRedactor(None)
CreditCardSpecificPurchaseUserInput.network_token_encrypted_card.validator = bv.String()
CreditCardSpecificPurchaseUserInput.network_token_encrypted_card.validator._redact = bv.BlotRedactor(None)
CreditCardSpecificPurchaseUserInput.three_ds_data.validator = bv.String()
CreditCardSpecificPurchaseUserInput.three_ds_data.validator._redact = bv.BlotRedactor(None)
CreditCardSpecificPurchaseUserInput.browser_info.validator = bv.String()
CreditCardSpecificPurchaseUserInput.browser_info.validator._redact = bv.BlotRedactor(None)
CreditCardSpecificPurchaseUserInput.device_data.validator = bv.String()
CreditCardSpecificPurchaseUserInput.device_data.validator._redact = bv.BlotRedactor(None)
CreditCardSpecificPurchaseUserInput.card_type.validator = bv.String()
CreditCardSpecificPurchaseUserInput.card_type.validator._redact = bv.BlotRedactor(None)
CreditCardSpecificPurchaseUserInput.nonce.validator = bv.String()
CreditCardSpecificPurchaseUserInput.nonce.validator._redact = bv.BlotRedactor(None)
CreditCardSpecificPurchaseUserInput.selected_brand.validator = bv.String()
CreditCardSpecificPurchaseUserInput.selected_brand.validator._redact = bv.BlotRedactor(None)
CreditCardSpecificPurchaseUserInput._all_field_names_ = set([
    'ccn',
    'ccode',
    'expmo',
    'expyr',
    'bin',
    'cpf',
    'cpf_name',
    'adyen_encrypted_card',
    'network_token_encrypted_card',
    'three_ds_data',
    'browser_info',
    'device_data',
    'card_type',
    'nonce',
    'selected_brand'])
CreditCardSpecificPurchaseUserInput._all_fields_ = [
    ('ccn', CreditCardSpecificPurchaseUserInput.ccn.validator),
    ('ccode', CreditCardSpecificPurchaseUserInput.ccode.validator),
    ('expmo', CreditCardSpecificPurchaseUserInput.expmo.validator),
    ('expyr', CreditCardSpecificPurchaseUserInput.expyr.validator),
    ('bin', CreditCardSpecificPurchaseUserInput.bin.validator),
    ('cpf', CreditCardSpecificPurchaseUserInput.cpf.validator),
    ('cpf_name', CreditCardSpecificPurchaseUserInput.cpf_name.validator),
    ('adyen_encrypted_card', CreditCardSpecificPurchaseUserInput.adyen_encrypted_card.validator),
    ('network_token_encrypted_card', CreditCardSpecificPurchaseUserInput.network_token_encrypted_card.validator),
    ('three_ds_data', CreditCardSpecificPurchaseUserInput.three_ds_data.validator),
    ('browser_info', CreditCardSpecificPurchaseUserInput.browser_info.validator),
    ('device_data', CreditCardSpecificPurchaseUserInput.device_data.validator),
    ('card_type', CreditCardSpecificPurchaseUserInput.card_type.validator),
    ('nonce', CreditCardSpecificPurchaseUserInput.nonce.validator),
    ('selected_brand', CreditCardSpecificPurchaseUserInput.selected_brand.validator)]
CurrentPaymentMethod.active_payment_method_type.validator = StorefrontPlatformPaymentMethod_validator
CurrentPaymentMethod.can_update_payment_method_via_web_storefront.validator = bv.Boolean()
CurrentPaymentMethod.can_update_payment_method_via_web_storefront.validator._redact = bv.BlotRedactor(None)
CurrentPaymentMethod.last_digits.validator = bv.String()
CurrentPaymentMethod.last_digits.validator._redact = bv.BlotRedactor(None)
CurrentPaymentMethod.vat_country_code.validator = bv.String()
CurrentPaymentMethod.vat_country_code.validator._redact = bv.BlotRedactor(None)
CurrentPaymentMethod.credit_type.validator = StorefrontPlatformCreditType_validator
CurrentPaymentMethod.expiration_date.validator = bv.String()
CurrentPaymentMethod.expiration_date.validator._redact = bv.BlotRedactor(None)
CurrentPaymentMethod.selected_brand.validator = bv.String()
CurrentPaymentMethod.selected_brand.validator._redact = bv.BlotRedactor(None)
CurrentPaymentMethod._all_field_names_ = set([
    'active_payment_method_type',
    'can_update_payment_method_via_web_storefront',
    'last_digits',
    'vat_country_code',
    'credit_type',
    'expiration_date',
    'selected_brand'])
CurrentPaymentMethod._all_fields_ = [
    ('active_payment_method_type', CurrentPaymentMethod.active_payment_method_type.validator),
    ('can_update_payment_method_via_web_storefront', CurrentPaymentMethod.can_update_payment_method_via_web_storefront.validator),
    ('last_digits', CurrentPaymentMethod.last_digits.validator),
    ('vat_country_code', CurrentPaymentMethod.vat_country_code.validator),
    ('credit_type', CurrentPaymentMethod.credit_type.validator),
    ('expiration_date', CurrentPaymentMethod.expiration_date.validator),
    ('selected_brand', CurrentPaymentMethod.selected_brand.validator)]
CurrentPlan.current_product.validator = bv.Nullable(ProductInfo_validator)
CurrentPlan.current_contract_length.validator = bv.Nullable(ContractLength_validator)
CurrentPlan.is_on_free_to_paid_trial.validator = bv.Boolean()
CurrentPlan.is_on_free_to_paid_trial.validator._redact = bv.BlotRedactor(None)
CurrentPlan.is_pending_cancellation.validator = bv.Boolean()
CurrentPlan.is_pending_cancellation.validator._redact = bv.BlotRedactor(None)
CurrentPlan.pending_product_changes.validator = bv.Nullable(ProductInfo_validator)
CurrentPlan.pending_contract_length_changes.validator = bv.Nullable(ContractLength_validator)
CurrentPlan.contract_expiration_date.validator = bv.String()
CurrentPlan.contract_expiration_date.validator._redact = bv.BlotRedactor(None)
CurrentPlan.can_self_manage_subscription.validator = bv.Boolean()
CurrentPlan.can_self_manage_subscription.validator._redact = bv.BlotRedactor(None)
CurrentPlan.team_properties.validator = bv.Nullable(TeamProperties_validator)
CurrentPlan.addon_offering_ids.validator = bv.Nullable(bv.List(bv.String()))
CurrentPlan.addon_offering_ids.validator._redact = bv.BlotRedactor(None)
CurrentPlan._all_field_names_ = set([
    'current_product',
    'current_contract_length',
    'is_on_free_to_paid_trial',
    'is_pending_cancellation',
    'pending_product_changes',
    'pending_contract_length_changes',
    'contract_expiration_date',
    'can_self_manage_subscription',
    'team_properties',
    'addon_offering_ids'])
CurrentPlan._all_fields_ = [
    ('current_product', CurrentPlan.current_product.validator),
    ('current_contract_length', CurrentPlan.current_contract_length.validator),
    ('is_on_free_to_paid_trial', CurrentPlan.is_on_free_to_paid_trial.validator),
    ('is_pending_cancellation', CurrentPlan.is_pending_cancellation.validator),
    ('pending_product_changes', CurrentPlan.pending_product_changes.validator),
    ('pending_contract_length_changes', CurrentPlan.pending_contract_length_changes.validator),
    ('contract_expiration_date', CurrentPlan.contract_expiration_date.validator),
    ('can_self_manage_subscription', CurrentPlan.can_self_manage_subscription.validator),
    ('team_properties', CurrentPlan.team_properties.validator),
    ('addon_offering_ids', CurrentPlan.addon_offering_ids.validator)]
DetailedPrices.base_price.validator = bv.Nullable(CashAmount_validator)
DetailedPrices.sub_total_price.validator = bv.Nullable(CashAmount_validator)
DetailedPrices.price.validator = bv.Nullable(CashAmount_validator)
DetailedPrices.tax_inclusive_price.validator = bv.Nullable(CashAmount_validator)
DetailedPrices.per_user_price.validator = bv.Nullable(CashAmount_validator)
DetailedPrices.tax_inclusive_per_user_price.validator = bv.Nullable(CashAmount_validator)
DetailedPrices.discount_amount.validator = bv.Nullable(CashAmount_validator)
DetailedPrices.discount_percentage.validator = bv.String()
DetailedPrices.discount_percentage.validator._redact = bv.BlotRedactor(None)
DetailedPrices.per_user_base_price.validator = bv.Nullable(CashAmount_validator)
DetailedPrices.addon_prices.validator = bv.Nullable(bv.List(AddonPrice_validator))
DetailedPrices.promo_props.validator = bv.Nullable(bv.List(PromoProps_validator))
DetailedPrices._all_field_names_ = set([
    'base_price',
    'sub_total_price',
    'price',
    'tax_inclusive_price',
    'per_user_price',
    'tax_inclusive_per_user_price',
    'discount_amount',
    'discount_percentage',
    'per_user_base_price',
    'addon_prices',
    'promo_props'])
DetailedPrices._all_fields_ = [
    ('base_price', DetailedPrices.base_price.validator),
    ('sub_total_price', DetailedPrices.sub_total_price.validator),
    ('price', DetailedPrices.price.validator),
    ('tax_inclusive_price', DetailedPrices.tax_inclusive_price.validator),
    ('per_user_price', DetailedPrices.per_user_price.validator),
    ('tax_inclusive_per_user_price', DetailedPrices.tax_inclusive_per_user_price.validator),
    ('discount_amount', DetailedPrices.discount_amount.validator),
    ('discount_percentage', DetailedPrices.discount_percentage.validator),
    ('per_user_base_price', DetailedPrices.per_user_base_price.validator),
    ('addon_prices', DetailedPrices.addon_prices.validator),
    ('promo_props', DetailedPrices.promo_props.validator)]
DirectDebitSpecificPurchaseUserInput.iban.validator = bv.String()
DirectDebitSpecificPurchaseUserInput.iban.validator._redact = bv.BlotRedactor(None)
DirectDebitSpecificPurchaseUserInput.owner_name.validator = bv.String()
DirectDebitSpecificPurchaseUserInput.owner_name.validator._redact = bv.BlotRedactor(None)
DirectDebitSpecificPurchaseUserInput.mandate_signed.validator = bv.Boolean()
DirectDebitSpecificPurchaseUserInput.mandate_signed.validator._redact = bv.BlotRedactor(None)
DirectDebitSpecificPurchaseUserInput._all_field_names_ = set([
    'iban',
    'owner_name',
    'mandate_signed'])
DirectDebitSpecificPurchaseUserInput._all_fields_ = [
    ('iban', DirectDebitSpecificPurchaseUserInput.iban.validator),
    ('owner_name', DirectDebitSpecificPurchaseUserInput.owner_name.validator),
    ('mandate_signed', DirectDebitSpecificPurchaseUserInput.mandate_signed.validator)]
Discount.discount_percentage.validator = bv.String()
Discount.discount_percentage.validator._redact = bv.BlotRedactor(None)
Discount.expiry_date.validator = bv.Nullable(common.DropboxTimestamp_validator)
Discount._all_field_names_ = set([
    'discount_percentage',
    'expiry_date'])
Discount._all_fields_ = [
    ('discount_percentage', Discount.discount_percentage.validator),
    ('expiry_date', Discount.expiry_date.validator)]
DlocalRbiSpecificPurchaseUserInput.name.validator = bv.String()
DlocalRbiSpecificPurchaseUserInput.name.validator._redact = bv.BlotRedactor(None)
DlocalRbiSpecificPurchaseUserInput.pan.validator = bv.String()
DlocalRbiSpecificPurchaseUserInput.pan.validator._redact = bv.BlotRedactor(None)
DlocalRbiSpecificPurchaseUserInput.address_number.validator = bv.String()
DlocalRbiSpecificPurchaseUserInput.address_number.validator._redact = bv.BlotRedactor(None)
DlocalRbiSpecificPurchaseUserInput.address_street.validator = bv.String()
DlocalRbiSpecificPurchaseUserInput.address_street.validator._redact = bv.BlotRedactor(None)
DlocalRbiSpecificPurchaseUserInput._all_field_names_ = set([
    'name',
    'pan',
    'address_number',
    'address_street'])
DlocalRbiSpecificPurchaseUserInput._all_fields_ = [
    ('name', DlocalRbiSpecificPurchaseUserInput.name.validator),
    ('pan', DlocalRbiSpecificPurchaseUserInput.pan.validator),
    ('address_number', DlocalRbiSpecificPurchaseUserInput.address_number.validator),
    ('address_street', DlocalRbiSpecificPurchaseUserInput.address_street.validator)]
EligibilityType.is_eligible.validator = bv.Boolean()
EligibilityType.is_eligible.validator._redact = bv.BlotRedactor(None)
EligibilityType.ineligibility_reasons.validator = bv.Nullable(bv.List(SubscriptionIneligibilityReason_validator))
EligibilityType._all_field_names_ = set([
    'is_eligible',
    'ineligibility_reasons'])
EligibilityType._all_fields_ = [
    ('is_eligible', EligibilityType.is_eligible.validator),
    ('ineligibility_reasons', EligibilityType.ineligibility_reasons.validator)]
FlexibleAddonInfo.offering_id.validator = bv.String()
FlexibleAddonInfo.offering_id.validator._redact = bv.BlotRedactor(None)
FlexibleAddonInfo.product_id.validator = bv.String()
FlexibleAddonInfo.product_id.validator._redact = bv.BlotRedactor(None)
FlexibleAddonInfo.count.validator = bv.Int32()
FlexibleAddonInfo.count.validator._redact = bv.BlotRedactor(None)
FlexibleAddonInfo._all_field_names_ = set([
    'offering_id',
    'product_id',
    'count'])
FlexibleAddonInfo._all_fields_ = [
    ('offering_id', FlexibleAddonInfo.offering_id.validator),
    ('product_id', FlexibleAddonInfo.product_id.validator),
    ('count', FlexibleAddonInfo.count.validator)]
FlexibleAddonRebillInfo.total_price.validator = bv.String()
FlexibleAddonRebillInfo.total_price.validator._redact = bv.BlotRedactor(None)
FlexibleAddonRebillInfo.next_billing_date.validator = bv.String()
FlexibleAddonRebillInfo.next_billing_date.validator._redact = bv.BlotRedactor(None)
FlexibleAddonRebillInfo._all_field_names_ = set([
    'total_price',
    'next_billing_date'])
FlexibleAddonRebillInfo._all_fields_ = [
    ('total_price', FlexibleAddonRebillInfo.total_price.validator),
    ('next_billing_date', FlexibleAddonRebillInfo.next_billing_date.validator)]
GrandfatheredStorage.formatted_quota.validator = bv.String()
GrandfatheredStorage.formatted_quota.validator._redact = bv.BlotRedactor(None)
GrandfatheredStorage.formatted_expiration_date.validator = bv.String()
GrandfatheredStorage.formatted_expiration_date.validator._redact = bv.BlotRedactor(None)
GrandfatheredStorage._all_field_names_ = set([
    'formatted_quota',
    'formatted_expiration_date'])
GrandfatheredStorage._all_fields_ = [
    ('formatted_quota', GrandfatheredStorage.formatted_quota.validator),
    ('formatted_expiration_date', GrandfatheredStorage.formatted_expiration_date.validator)]
IdealSpecificPurchaseUserInput.bank_id.validator = bv.String()
IdealSpecificPurchaseUserInput.bank_id.validator._redact = bv.BlotRedactor(None)
IdealSpecificPurchaseUserInput.bank_name.validator = bv.String()
IdealSpecificPurchaseUserInput.bank_name.validator._redact = bv.BlotRedactor(None)
IdealSpecificPurchaseUserInput._all_field_names_ = set([
    'bank_id',
    'bank_name'])
IdealSpecificPurchaseUserInput._all_fields_ = [
    ('bank_id', IdealSpecificPurchaseUserInput.bank_id.validator),
    ('bank_name', IdealSpecificPurchaseUserInput.bank_name.validator)]
InactiveSubscription.product_info.validator = bv.Nullable(ProductInfo_validator)
InactiveSubscription.product_line_info.validator = bv.Nullable(ProductLineInfo_validator)
InactiveSubscription.contract_length.validator = bv.Nullable(ContractLength_validator)
InactiveSubscription.multi_seat_properties.validator = bv.Nullable(MultiSeatProperties_validator)
InactiveSubscription._all_field_names_ = set([
    'product_info',
    'product_line_info',
    'contract_length',
    'multi_seat_properties'])
InactiveSubscription._all_fields_ = [
    ('product_info', InactiveSubscription.product_info.validator),
    ('product_line_info', InactiveSubscription.product_line_info.validator),
    ('contract_length', InactiveSubscription.contract_length.validator),
    ('multi_seat_properties', InactiveSubscription.multi_seat_properties.validator)]
LicenseInfo.offering_id.validator = bv.String()
LicenseInfo.offering_id.validator._redact = bv.BlotRedactor(None)
LicenseInfo.count.validator = bv.Int64()
LicenseInfo.count.validator._redact = bv.BlotRedactor(None)
LicenseInfo.product_id.validator = bv.String()
LicenseInfo.product_id.validator._redact = bv.BlotRedactor(None)
LicenseInfo._all_field_names_ = set([
    'offering_id',
    'count',
    'product_id'])
LicenseInfo._all_fields_ = [
    ('offering_id', LicenseInfo.offering_id.validator),
    ('count', LicenseInfo.count.validator),
    ('product_id', LicenseInfo.product_id.validator)]
LicenseKey.key.validator = bv.String()
LicenseKey.key.validator._redact = bv.BlotRedactor(None)
LicenseKey.redeemed_date.validator = bv.String()
LicenseKey.redeemed_date.validator._redact = bv.BlotRedactor(None)
LicenseKey.activated_date.validator = bv.String()
LicenseKey.activated_date.validator._redact = bv.BlotRedactor(None)
LicenseKey.duration.validator = bv.String()
LicenseKey.duration.validator._redact = bv.BlotRedactor(None)
LicenseKey._all_field_names_ = set([
    'key',
    'redeemed_date',
    'activated_date',
    'duration'])
LicenseKey._all_fields_ = [
    ('key', LicenseKey.key.validator),
    ('redeemed_date', LicenseKey.redeemed_date.validator),
    ('activated_date', LicenseKey.activated_date.validator),
    ('duration', LicenseKey.duration.validator)]
LineItem.product_category.validator = StorefrontPlatformProductCategory_validator
LineItem.base_price.validator = bv.String()
LineItem.base_price.validator._redact = bv.BlotRedactor(None)
LineItem.offering_id.validator = bv.String()
LineItem.offering_id.validator._redact = bv.BlotRedactor(None)
LineItem.unit_price.validator = bv.String()
LineItem.unit_price.validator._redact = bv.BlotRedactor(None)
LineItem.product_id.validator = bv.String()
LineItem.product_id.validator._redact = bv.BlotRedactor(None)
LineItem.billing_period_unit_price.validator = bv.String()
LineItem.billing_period_unit_price.validator._redact = bv.BlotRedactor(None)
LineItem.quantity.validator = bv.UInt32()
LineItem.quantity.validator._redact = bv.BlotRedactor(None)
LineItem._all_field_names_ = set([
    'product_category',
    'base_price',
    'offering_id',
    'unit_price',
    'product_id',
    'billing_period_unit_price',
    'quantity'])
LineItem._all_fields_ = [
    ('product_category', LineItem.product_category.validator),
    ('base_price', LineItem.base_price.validator),
    ('offering_id', LineItem.offering_id.validator),
    ('unit_price', LineItem.unit_price.validator),
    ('product_id', LineItem.product_id.validator),
    ('billing_period_unit_price', LineItem.billing_period_unit_price.validator),
    ('quantity', LineItem.quantity.validator)]
MultiSeatProperties.usable_licenses.validator = bv.Nullable(bv.List(LicenseInfo_validator))
MultiSeatProperties.per_license_price.validator = bv.String()
MultiSeatProperties.per_license_price.validator._redact = bv.BlotRedactor(None)
MultiSeatProperties.total_licenses.validator = bv.Nullable(bv.List(LicenseInfo_validator))
MultiSeatProperties.per_license_quota.validator = bv.String()
MultiSeatProperties.per_license_quota.validator._redact = bv.BlotRedactor(None)
MultiSeatProperties.flexible_addons.validator = bv.Nullable(bv.List(FlexibleAddonInfo_validator))
MultiSeatProperties._all_field_names_ = set([
    'usable_licenses',
    'per_license_price',
    'total_licenses',
    'per_license_quota',
    'flexible_addons'])
MultiSeatProperties._all_fields_ = [
    ('usable_licenses', MultiSeatProperties.usable_licenses.validator),
    ('per_license_price', MultiSeatProperties.per_license_price.validator),
    ('total_licenses', MultiSeatProperties.total_licenses.validator),
    ('per_license_quota', MultiSeatProperties.per_license_quota.validator),
    ('flexible_addons', MultiSeatProperties.flexible_addons.validator)]
NmlVariantValue._nml_off_validator = bv.Void()
NmlVariantValue._nml_control_validator = bv.Void()
NmlVariantValue._nml_v1_validator = bv.Void()
NmlVariantValue._nml_v2_validator = bv.Void()
NmlVariantValue._nml_v3_validator = bv.Void()
NmlVariantValue._nml_v4_validator = bv.Void()
NmlVariantValue._no_min_with_2024_price_validator = bv.Void()
NmlVariantValue._no_min_with_gbb_price_validator = bv.Void()
NmlVariantValue._three_min_with_2024_price_validator = bv.Void()
NmlVariantValue._three_min_with_gbb_price_validator = bv.Void()
NmlVariantValue._std_min_1_license_2025_v1_validator = bv.Void()
NmlVariantValue._std_min_1_license_2025_v2_validator = bv.Void()
NmlVariantValue._std_min_1_license_2025_v3_validator = bv.Void()
NmlVariantValue._std_min_1_license_2025_v4_validator = bv.Void()
NmlVariantValue._other_validator = bv.Void()
NmlVariantValue._tagmap = {
    'nml_off': NmlVariantValue._nml_off_validator,
    'nml_control': NmlVariantValue._nml_control_validator,
    'nml_v1': NmlVariantValue._nml_v1_validator,
    'nml_v2': NmlVariantValue._nml_v2_validator,
    'nml_v3': NmlVariantValue._nml_v3_validator,
    'nml_v4': NmlVariantValue._nml_v4_validator,
    'no_min_with_2024_price': NmlVariantValue._no_min_with_2024_price_validator,
    'no_min_with_gbb_price': NmlVariantValue._no_min_with_gbb_price_validator,
    'three_min_with_2024_price': NmlVariantValue._three_min_with_2024_price_validator,
    'three_min_with_gbb_price': NmlVariantValue._three_min_with_gbb_price_validator,
    'std_min_1_license_2025_v1': NmlVariantValue._std_min_1_license_2025_v1_validator,
    'std_min_1_license_2025_v2': NmlVariantValue._std_min_1_license_2025_v2_validator,
    'std_min_1_license_2025_v3': NmlVariantValue._std_min_1_license_2025_v3_validator,
    'std_min_1_license_2025_v4': NmlVariantValue._std_min_1_license_2025_v4_validator,
    'other': NmlVariantValue._other_validator }
NmlVariantValue.nml_off = NmlVariantValue('nml_off')
NmlVariantValue.nml_control = NmlVariantValue('nml_control')
NmlVariantValue.nml_v1 = NmlVariantValue('nml_v1')
NmlVariantValue.nml_v2 = NmlVariantValue('nml_v2')
NmlVariantValue.nml_v3 = NmlVariantValue('nml_v3')
NmlVariantValue.nml_v4 = NmlVariantValue('nml_v4')
NmlVariantValue.no_min_with_2024_price = NmlVariantValue('no_min_with_2024_price')
NmlVariantValue.no_min_with_gbb_price = NmlVariantValue('no_min_with_gbb_price')
NmlVariantValue.three_min_with_2024_price = NmlVariantValue('three_min_with_2024_price')
NmlVariantValue.three_min_with_gbb_price = NmlVariantValue('three_min_with_gbb_price')
NmlVariantValue.std_min_1_license_2025_v1 = NmlVariantValue('std_min_1_license_2025_v1')
NmlVariantValue.std_min_1_license_2025_v2 = NmlVariantValue('std_min_1_license_2025_v2')
NmlVariantValue.std_min_1_license_2025_v3 = NmlVariantValue('std_min_1_license_2025_v3')
NmlVariantValue.std_min_1_license_2025_v4 = NmlVariantValue('std_min_1_license_2025_v4')
NmlVariantValue.other = NmlVariantValue('other')
NonTaxableBillingAddress.name.validator = bv.String()
NonTaxableBillingAddress.name.validator._redact = bv.BlotRedactor(None)
NonTaxableBillingAddress.address.validator = bv.String()
NonTaxableBillingAddress.address.validator._redact = bv.BlotRedactor(None)
NonTaxableBillingAddress.city.validator = bv.String()
NonTaxableBillingAddress.city.validator._redact = bv.BlotRedactor(None)
NonTaxableBillingAddress.state.validator = bv.String()
NonTaxableBillingAddress.state.validator._redact = bv.BlotRedactor(None)
NonTaxableBillingAddress._all_field_names_ = set([
    'name',
    'address',
    'city',
    'state'])
NonTaxableBillingAddress._all_fields_ = [
    ('name', NonTaxableBillingAddress.name.validator),
    ('address', NonTaxableBillingAddress.address.validator),
    ('city', NonTaxableBillingAddress.city.validator),
    ('state', NonTaxableBillingAddress.state.validator)]
OnOffConfigValue._off_validator = bv.Void()
OnOffConfigValue._on_validator = bv.Void()
OnOffConfigValue._other_validator = bv.Void()
OnOffConfigValue._tagmap = {
    'off': OnOffConfigValue._off_validator,
    'on': OnOffConfigValue._on_validator,
    'other': OnOffConfigValue._other_validator }
OnOffConfigValue.off = OnOffConfigValue('off')
OnOffConfigValue.on = OnOffConfigValue('on')
OnOffConfigValue.other = OnOffConfigValue('other')
OnOffControlConfigValue._ooc_off_validator = bv.Void()
OnOffControlConfigValue._ooc_on_validator = bv.Void()
OnOffControlConfigValue._ooc_control_validator = bv.Void()
OnOffControlConfigValue._other_validator = bv.Void()
OnOffControlConfigValue._tagmap = {
    'ooc_off': OnOffControlConfigValue._ooc_off_validator,
    'ooc_on': OnOffControlConfigValue._ooc_on_validator,
    'ooc_control': OnOffControlConfigValue._ooc_control_validator,
    'other': OnOffControlConfigValue._other_validator }
OnOffControlConfigValue.ooc_off = OnOffControlConfigValue('ooc_off')
OnOffControlConfigValue.ooc_on = OnOffControlConfigValue('ooc_on')
OnOffControlConfigValue.ooc_control = OnOffControlConfigValue('ooc_control')
OnOffControlConfigValue.other = OnOffControlConfigValue('other')
OrderSummary.total_price.validator = bv.Nullable(CashAmount_validator)
OrderSummary.tax_country_code.validator = bv.String()
OrderSummary.tax_country_code.validator._redact = bv.BlotRedactor(None)
OrderSummary.tax_amount.validator = bv.Nullable(CashAmount_validator)
OrderSummary.currency.validator = bv.String()
OrderSummary.currency.validator._redact = bv.BlotRedactor(None)
OrderSummary.withheld_tax_amount.validator = bv.Nullable(CashAmount_validator)
OrderSummary.tax_plan_name.validator = bv.String()
OrderSummary.tax_plan_name.validator._redact = bv.BlotRedactor(None)
OrderSummary.estimated_local_currency_total_amount.validator = bv.String()
OrderSummary.estimated_local_currency_total_amount.validator._redact = bv.BlotRedactor(None)
OrderSummary.estimated_local_currency_conversion_rate.validator = bv.String()
OrderSummary.estimated_local_currency_conversion_rate.validator._redact = bv.BlotRedactor(None)
OrderSummary.tax_rate.validator = bv.String()
OrderSummary.tax_rate.validator._redact = bv.BlotRedactor(None)
OrderSummary.display_price.validator = bv.String()
OrderSummary.display_price.validator._redact = bv.BlotRedactor(None)
OrderSummary._all_field_names_ = set([
    'total_price',
    'tax_country_code',
    'tax_amount',
    'currency',
    'withheld_tax_amount',
    'tax_plan_name',
    'estimated_local_currency_total_amount',
    'estimated_local_currency_conversion_rate',
    'tax_rate',
    'display_price'])
OrderSummary._all_fields_ = [
    ('total_price', OrderSummary.total_price.validator),
    ('tax_country_code', OrderSummary.tax_country_code.validator),
    ('tax_amount', OrderSummary.tax_amount.validator),
    ('currency', OrderSummary.currency.validator),
    ('withheld_tax_amount', OrderSummary.withheld_tax_amount.validator),
    ('tax_plan_name', OrderSummary.tax_plan_name.validator),
    ('estimated_local_currency_total_amount', OrderSummary.estimated_local_currency_total_amount.validator),
    ('estimated_local_currency_conversion_rate', OrderSummary.estimated_local_currency_conversion_rate.validator),
    ('tax_rate', OrderSummary.tax_rate.validator),
    ('display_price', OrderSummary.display_price.validator)]
PaypalSpecificPurchaseUserInput.payer_id.validator = bv.String()
PaypalSpecificPurchaseUserInput.payer_id.validator._redact = bv.BlotRedactor(None)
PaypalSpecificPurchaseUserInput.token.validator = bv.String()
PaypalSpecificPurchaseUserInput.token.validator._redact = bv.BlotRedactor(None)
PaypalSpecificPurchaseUserInput.has_gateway_token.validator = bv.Boolean()
PaypalSpecificPurchaseUserInput.has_gateway_token.validator._redact = bv.BlotRedactor(None)
PaypalSpecificPurchaseUserInput.paypal_nonce.validator = bv.String()
PaypalSpecificPurchaseUserInput.paypal_nonce.validator._redact = bv.BlotRedactor(None)
PaypalSpecificPurchaseUserInput._all_field_names_ = set([
    'payer_id',
    'token',
    'has_gateway_token',
    'paypal_nonce'])
PaypalSpecificPurchaseUserInput._all_fields_ = [
    ('payer_id', PaypalSpecificPurchaseUserInput.payer_id.validator),
    ('token', PaypalSpecificPurchaseUserInput.token.validator),
    ('has_gateway_token', PaypalSpecificPurchaseUserInput.has_gateway_token.validator),
    ('paypal_nonce', PaypalSpecificPurchaseUserInput.paypal_nonce.validator)]
PercentageRatioByVolume.entries.validator = bv.Nullable(bv.List(PercentageRatioByVolumeEntry_validator))
PercentageRatioByVolume._all_field_names_ = set([
    'entries'])
PercentageRatioByVolume._all_fields_ = [
    ('entries', PercentageRatioByVolume.entries.validator)]
PercentageRatioByVolumeEntry.inclusive_start.validator = bv.Int64()
PercentageRatioByVolumeEntry.inclusive_start.validator._redact = bv.BlotRedactor(None)
PercentageRatioByVolumeEntry.exclusive_end.validator = bv.Int64()
PercentageRatioByVolumeEntry.exclusive_end.validator._redact = bv.BlotRedactor(None)
PercentageRatioByVolumeEntry.percentage_ratio.validator = bv.String()
PercentageRatioByVolumeEntry.percentage_ratio.validator._redact = bv.BlotRedactor(None)
PercentageRatioByVolumeEntry._all_field_names_ = set([
    'inclusive_start',
    'exclusive_end',
    'percentage_ratio'])
PercentageRatioByVolumeEntry._all_fields_ = [
    ('inclusive_start', PercentageRatioByVolumeEntry.inclusive_start.validator),
    ('exclusive_end', PercentageRatioByVolumeEntry.exclusive_end.validator),
    ('percentage_ratio', PercentageRatioByVolumeEntry.percentage_ratio.validator)]
PerformCancellationResponse.cancelled_product_type.validator = StorefrontPlatformProductType_validator
PerformCancellationResponse._all_field_names_ = set([
    'cancelled_product_type'])
PerformCancellationResponse._all_fields_ = [
    ('cancelled_product_type', PerformCancellationResponse.cancelled_product_type.validator)]
PlannedTransition.planned_transition_type.validator = PlannedTransitionType_validator
PlannedTransition.planned_transition.validator = bv.Nullable(PlannedTransitionUnion_validator)
PlannedTransition.schedule.validator = Schedule_validator
PlannedTransition.products.validator = bv.Nullable(bv.List(PurchaseProductInfo_validator))
PlannedTransition._all_field_names_ = set([
    'planned_transition_type',
    'planned_transition',
    'schedule',
    'products'])
PlannedTransition._all_fields_ = [
    ('planned_transition_type', PlannedTransition.planned_transition_type.validator),
    ('planned_transition', PlannedTransition.planned_transition.validator),
    ('schedule', PlannedTransition.schedule.validator),
    ('products', PlannedTransition.products.validator)]
PlannedTransitionType._subscription_service_planned_transition_validator = bv.Void()
PlannedTransitionType._rev_api_planned_transition_validator = bv.Void()
PlannedTransitionType._other_validator = bv.Void()
PlannedTransitionType._tagmap = {
    'subscription_service_planned_transition': PlannedTransitionType._subscription_service_planned_transition_validator,
    'rev_api_planned_transition': PlannedTransitionType._rev_api_planned_transition_validator,
    'other': PlannedTransitionType._other_validator }
PlannedTransitionType.subscription_service_planned_transition = PlannedTransitionType('subscription_service_planned_transition')
PlannedTransitionType.rev_api_planned_transition = PlannedTransitionType('rev_api_planned_transition')
PlannedTransitionType.other = PlannedTransitionType('other')
PriceVariantValue._off_price_validator = bv.Void()
PriceVariantValue._control_price_validator = bv.Void()
PriceVariantValue._v1_price_validator = bv.Void()
PriceVariantValue._v2_price_validator = bv.Void()
PriceVariantValue._v3_price_validator = bv.Void()
PriceVariantValue._v4_price_validator = bv.Void()
PriceVariantValue._v5_price_validator = bv.Void()
PriceVariantValue._other_validator = bv.Void()
PriceVariantValue._tagmap = {
    'off_price': PriceVariantValue._off_price_validator,
    'control_price': PriceVariantValue._control_price_validator,
    'v1_price': PriceVariantValue._v1_price_validator,
    'v2_price': PriceVariantValue._v2_price_validator,
    'v3_price': PriceVariantValue._v3_price_validator,
    'v4_price': PriceVariantValue._v4_price_validator,
    'v5_price': PriceVariantValue._v5_price_validator,
    'other': PriceVariantValue._other_validator }
PriceVariantValue.off_price = PriceVariantValue('off_price')
PriceVariantValue.control_price = PriceVariantValue('control_price')
PriceVariantValue.v1_price = PriceVariantValue('v1_price')
PriceVariantValue.v2_price = PriceVariantValue('v2_price')
PriceVariantValue.v3_price = PriceVariantValue('v3_price')
PriceVariantValue.v4_price = PriceVariantValue('v4_price')
PriceVariantValue.v5_price = PriceVariantValue('v5_price')
PriceVariantValue.other = PriceVariantValue('other')
PricingData.detailed_prices.validator = bv.Nullable(DetailedPrices_validator)
PricingData.order_summary.validator = bv.Nullable(OrderSummary_validator)
PricingData.schedule.validator = Schedule_validator
PricingData.pricing_token.validator = bv.String()
PricingData.pricing_token.validator._redact = bv.BlotRedactor(None)
PricingData.product_type.validator = StorefrontPlatformProductType_validator
PricingData._all_field_names_ = set([
    'detailed_prices',
    'order_summary',
    'schedule',
    'pricing_token',
    'product_type'])
PricingData._all_fields_ = [
    ('detailed_prices', PricingData.detailed_prices.validator),
    ('order_summary', PricingData.order_summary.validator),
    ('schedule', PricingData.schedule.validator),
    ('pricing_token', PricingData.pricing_token.validator),
    ('product_type', PricingData.product_type.validator)]
PricingToken.type.validator = PricingTokenType_validator
PricingToken.token.validator = bv.Nullable(TokenUnion_validator)
PricingToken._all_field_names_ = set([
    'type',
    'token'])
PricingToken._all_fields_ = [
    ('type', PricingToken.type.validator),
    ('token', PricingToken.token.validator)]
PricingTokenType._unknown_token_type_validator = bv.Void()
PricingTokenType._sub_service_token_validator = bv.Void()
PricingTokenType._rev_api_token_validator = bv.Void()
PricingTokenType._other_validator = bv.Void()
PricingTokenType._tagmap = {
    'unknown_token_type': PricingTokenType._unknown_token_type_validator,
    'sub_service_token': PricingTokenType._sub_service_token_validator,
    'rev_api_token': PricingTokenType._rev_api_token_validator,
    'other': PricingTokenType._other_validator }
PricingTokenType.unknown_token_type = PricingTokenType('unknown_token_type')
PricingTokenType.sub_service_token = PricingTokenType('sub_service_token')
PricingTokenType.rev_api_token = PricingTokenType('rev_api_token')
PricingTokenType.other = PricingTokenType('other')
ProductInfo.storefront_plan_id.validator = bv.String()
ProductInfo.storefront_plan_id.validator._redact = bv.BlotRedactor(None)
ProductInfo.display_name.validator = bv.String()
ProductInfo.display_name.validator._redact = bv.BlotRedactor(None)
ProductInfo.product_type.validator = StorefrontPlatformProductType_validator
ProductInfo.dropbox_brand_display_name.validator = bv.String()
ProductInfo.dropbox_brand_display_name.validator._redact = bv.BlotRedactor(None)
ProductInfo.description_short.validator = bv.String()
ProductInfo.description_short.validator._redact = bv.BlotRedactor(None)
ProductInfo.brand_name.validator = bv.String()
ProductInfo.brand_name.validator._redact = bv.BlotRedactor(None)
ProductInfo._all_field_names_ = set([
    'storefront_plan_id',
    'display_name',
    'product_type',
    'dropbox_brand_display_name',
    'description_short',
    'brand_name'])
ProductInfo._all_fields_ = [
    ('storefront_plan_id', ProductInfo.storefront_plan_id.validator),
    ('display_name', ProductInfo.display_name.validator),
    ('product_type', ProductInfo.product_type.validator),
    ('dropbox_brand_display_name', ProductInfo.dropbox_brand_display_name.validator),
    ('description_short', ProductInfo.description_short.validator),
    ('brand_name', ProductInfo.brand_name.validator)]
ProductLineInfo.storefront_product_line.validator = StorefrontPlatformProductLine_validator
ProductLineInfo.product_line_display_name.validator = bv.String()
ProductLineInfo.product_line_display_name.validator._redact = bv.BlotRedactor(None)
ProductLineInfo.product_line_path_segment.validator = bv.String()
ProductLineInfo.product_line_path_segment.validator._redact = bv.BlotRedactor(None)
ProductLineInfo.product_line_settings_link.validator = bv.String()
ProductLineInfo.product_line_settings_link.validator._redact = bv.BlotRedactor(None)
ProductLineInfo._all_field_names_ = set([
    'storefront_product_line',
    'product_line_display_name',
    'product_line_path_segment',
    'product_line_settings_link'])
ProductLineInfo._all_fields_ = [
    ('storefront_product_line', ProductLineInfo.storefront_product_line.validator),
    ('product_line_display_name', ProductLineInfo.product_line_display_name.validator),
    ('product_line_path_segment', ProductLineInfo.product_line_path_segment.validator),
    ('product_line_settings_link', ProductLineInfo.product_line_settings_link.validator)]
PromoInfo.cash_code.validator = bv.String()
PromoInfo.cash_code.validator._redact = bv.BlotRedactor(None)
PromoInfo.dcode.validator = bv.String()
PromoInfo.dcode.validator._redact = bv.BlotRedactor(None)
PromoInfo.coupon_code.validator = bv.String()
PromoInfo.coupon_code.validator._redact = bv.BlotRedactor(None)
PromoInfo._all_field_names_ = set([
    'cash_code',
    'dcode',
    'coupon_code'])
PromoInfo._all_fields_ = [
    ('cash_code', PromoInfo.cash_code.validator),
    ('dcode', PromoInfo.dcode.validator),
    ('coupon_code', PromoInfo.coupon_code.validator)]
PromoProps.type.validator = PromoType_validator
PromoProps.code.validator = bv.String()
PromoProps.code.validator._redact = bv.BlotRedactor(None)
PromoProps.disallow_monthly.validator = bv.Boolean()
PromoProps.disallow_monthly.validator._redact = bv.BlotRedactor(None)
PromoProps.discount_percentage.validator = bv.Float32()
PromoProps.discount_percentage.validator._redact = bv.BlotRedactor(None)
PromoProps.expiration_date.validator = bv.String()
PromoProps.expiration_date.validator._redact = bv.BlotRedactor(None)
PromoProps.duration.validator = bv.Nullable(ContractLength_validator)
PromoProps.supported_schedule_ids.validator = bv.Nullable(bv.List(Schedule_validator))
PromoProps.storefront_platform_product_type.validator = StorefrontPlatformProductType_validator
PromoProps.include_quota_in_promo_msg.validator = bv.Boolean()
PromoProps.include_quota_in_promo_msg.validator._redact = bv.BlotRedactor(None)
PromoProps.percentage_ratio_by_volume.validator = bv.Nullable(PercentageRatioByVolume_validator)
PromoProps.claim_by_date.validator = bv.String()
PromoProps.claim_by_date.validator._redact = bv.BlotRedactor(None)
PromoProps.should_hide_go_to_trial_link.validator = bv.Boolean()
PromoProps.should_hide_go_to_trial_link.validator._redact = bv.BlotRedactor(None)
PromoProps._all_field_names_ = set([
    'type',
    'code',
    'disallow_monthly',
    'discount_percentage',
    'expiration_date',
    'duration',
    'supported_schedule_ids',
    'storefront_platform_product_type',
    'include_quota_in_promo_msg',
    'percentage_ratio_by_volume',
    'claim_by_date',
    'should_hide_go_to_trial_link'])
PromoProps._all_fields_ = [
    ('type', PromoProps.type.validator),
    ('code', PromoProps.code.validator),
    ('disallow_monthly', PromoProps.disallow_monthly.validator),
    ('discount_percentage', PromoProps.discount_percentage.validator),
    ('expiration_date', PromoProps.expiration_date.validator),
    ('duration', PromoProps.duration.validator),
    ('supported_schedule_ids', PromoProps.supported_schedule_ids.validator),
    ('storefront_platform_product_type', PromoProps.storefront_platform_product_type.validator),
    ('include_quota_in_promo_msg', PromoProps.include_quota_in_promo_msg.validator),
    ('percentage_ratio_by_volume', PromoProps.percentage_ratio_by_volume.validator),
    ('claim_by_date', PromoProps.claim_by_date.validator),
    ('should_hide_go_to_trial_link', PromoProps.should_hide_go_to_trial_link.validator)]
PromoType._benefit_type_unknown_validator = bv.Void()
PromoType._benefit_type_percentage_validator = bv.Void()
PromoType._benefit_type_time_validator = bv.Void()
PromoType._benefit_type_trial_validator = bv.Void()
PromoType._benefit_type_volume_percentage_ratio_validator = bv.Void()
PromoType._benefit_type_transaction_percentage_ratio_validator = bv.Void()
PromoType._benefit_type_free_product_validator = bv.Void()
PromoType._benefit_type_pre_paid_product_validator = bv.Void()
PromoType._other_validator = bv.Void()
PromoType._tagmap = {
    'benefit_type_unknown': PromoType._benefit_type_unknown_validator,
    'benefit_type_percentage': PromoType._benefit_type_percentage_validator,
    'benefit_type_time': PromoType._benefit_type_time_validator,
    'benefit_type_trial': PromoType._benefit_type_trial_validator,
    'benefit_type_volume_percentage_ratio': PromoType._benefit_type_volume_percentage_ratio_validator,
    'benefit_type_transaction_percentage_ratio': PromoType._benefit_type_transaction_percentage_ratio_validator,
    'benefit_type_free_product': PromoType._benefit_type_free_product_validator,
    'benefit_type_pre_paid_product': PromoType._benefit_type_pre_paid_product_validator,
    'other': PromoType._other_validator }
PromoType.benefit_type_unknown = PromoType('benefit_type_unknown')
PromoType.benefit_type_percentage = PromoType('benefit_type_percentage')
PromoType.benefit_type_time = PromoType('benefit_type_time')
PromoType.benefit_type_trial = PromoType('benefit_type_trial')
PromoType.benefit_type_volume_percentage_ratio = PromoType('benefit_type_volume_percentage_ratio')
PromoType.benefit_type_transaction_percentage_ratio = PromoType('benefit_type_transaction_percentage_ratio')
PromoType.benefit_type_free_product = PromoType('benefit_type_free_product')
PromoType.benefit_type_pre_paid_product = PromoType('benefit_type_pre_paid_product')
PromoType.other = PromoType('other')
PurchaseProductInfo.product_type.validator = StorefrontPlatformProductType_validator
PurchaseProductInfo.num_licenses.validator = bv.Int64()
PurchaseProductInfo.num_licenses.validator._redact = bv.BlotRedactor(None)
PurchaseProductInfo.add_ons.validator = bv.Nullable(bv.List(StorefrontPlatformProductType_validator))
PurchaseProductInfo.promo_info.validator = bv.Nullable(PromoInfo_validator)
PurchaseProductInfo.trial_project_type.validator = StorefrontPlatformTrialsProjectType_validator
PurchaseProductInfo.product_category.validator = StorefrontPlatformProductCategory_validator
PurchaseProductInfo.tags.validator = bv.Nullable(bv.List(bv.String()))
PurchaseProductInfo.tags.validator._redact = bv.BlotRedactor(None)
PurchaseProductInfo.addon_products.validator = bv.Nullable(bv.List(AddonProductInfo_validator))
PurchaseProductInfo.product_sub_family.validator = bv.Int32()
PurchaseProductInfo.product_sub_family.validator._redact = bv.BlotRedactor(None)
PurchaseProductInfo._all_field_names_ = set([
    'product_type',
    'num_licenses',
    'add_ons',
    'promo_info',
    'trial_project_type',
    'product_category',
    'tags',
    'addon_products',
    'product_sub_family'])
PurchaseProductInfo._all_fields_ = [
    ('product_type', PurchaseProductInfo.product_type.validator),
    ('num_licenses', PurchaseProductInfo.num_licenses.validator),
    ('add_ons', PurchaseProductInfo.add_ons.validator),
    ('promo_info', PurchaseProductInfo.promo_info.validator),
    ('trial_project_type', PurchaseProductInfo.trial_project_type.validator),
    ('product_category', PurchaseProductInfo.product_category.validator),
    ('tags', PurchaseProductInfo.tags.validator),
    ('addon_products', PurchaseProductInfo.addon_products.validator),
    ('product_sub_family', PurchaseProductInfo.product_sub_family.validator)]
PurchaseTeamInput.company_size.validator = bv.String()
PurchaseTeamInput.company_size.validator._redact = bv.BlotRedactor(None)
PurchaseTeamInput.team_name.validator = bv.String()
PurchaseTeamInput.team_name.validator._redact = bv.BlotRedactor(None)
PurchaseTeamInput.team_phone.validator = bv.String()
PurchaseTeamInput.team_phone.validator._redact = bv.BlotRedactor(None)
PurchaseTeamInput.number_of_users.validator = bv.Int32()
PurchaseTeamInput.number_of_users.validator._redact = bv.BlotRedactor(None)
PurchaseTeamInput._all_field_names_ = set([
    'company_size',
    'team_name',
    'team_phone',
    'number_of_users'])
PurchaseTeamInput._all_fields_ = [
    ('company_size', PurchaseTeamInput.company_size.validator),
    ('team_name', PurchaseTeamInput.team_name.validator),
    ('team_phone', PurchaseTeamInput.team_phone.validator),
    ('number_of_users', PurchaseTeamInput.number_of_users.validator)]
PurchaseUserInput.zip.validator = bv.String()
PurchaseUserInput.zip.validator._redact = bv.BlotRedactor(None)
PurchaseUserInput.vat.validator = bv.String()
PurchaseUserInput.vat.validator._redact = bv.BlotRedactor(None)
PurchaseUserInput.country.validator = bv.String()
PurchaseUserInput.country.validator._redact = bv.BlotRedactor(None)
PurchaseUserInput.country_code.validator = bv.String()
PurchaseUserInput.country_code.validator._redact = bv.BlotRedactor(None)
PurchaseUserInput.currency.validator = bv.String()
PurchaseUserInput.currency.validator._redact = bv.BlotRedactor(None)
PurchaseUserInput.code.validator = bv.String()
PurchaseUserInput.code.validator._redact = bv.BlotRedactor(None)
PurchaseUserInput.dcode.validator = bv.String()
PurchaseUserInput.dcode.validator._redact = bv.BlotRedactor(None)
PurchaseUserInput.promo_ids.validator = bv.String()
PurchaseUserInput.promo_ids.validator._redact = bv.BlotRedactor(None)
PurchaseUserInput.payment_method.validator = StorefrontPlatformPaymentMethod_validator
PurchaseUserInput.total_price.validator = bv.String()
PurchaseUserInput.total_price.validator._redact = bv.BlotRedactor(None)
PurchaseUserInput.declaration_confirmation.validator = bv.Boolean()
PurchaseUserInput.declaration_confirmation.validator._redact = bv.BlotRedactor(None)
PurchaseUserInput.invoice_business_name.validator = bv.String()
PurchaseUserInput.invoice_business_name.validator._redact = bv.BlotRedactor(None)
PurchaseUserInput.invoice_street_address.validator = bv.String()
PurchaseUserInput.invoice_street_address.validator._redact = bv.BlotRedactor(None)
PurchaseUserInput.invoice_city.validator = bv.String()
PurchaseUserInput.invoice_city.validator._redact = bv.BlotRedactor(None)
PurchaseUserInput.invoice_province.validator = bv.String()
PurchaseUserInput.invoice_province.validator._redact = bv.BlotRedactor(None)
PurchaseUserInput.vat_provincial.validator = bv.String()
PurchaseUserInput.vat_provincial.validator._redact = bv.BlotRedactor(None)
PurchaseUserInput.payment_method_specific_user_input.validator = bv.Nullable(PaymentMethodSpecificUserInputUnion_validator)
PurchaseUserInput._all_field_names_ = set([
    'zip',
    'vat',
    'country',
    'country_code',
    'currency',
    'code',
    'dcode',
    'promo_ids',
    'payment_method',
    'total_price',
    'declaration_confirmation',
    'invoice_business_name',
    'invoice_street_address',
    'invoice_city',
    'invoice_province',
    'vat_provincial',
    'payment_method_specific_user_input'])
PurchaseUserInput._all_fields_ = [
    ('zip', PurchaseUserInput.zip.validator),
    ('vat', PurchaseUserInput.vat.validator),
    ('country', PurchaseUserInput.country.validator),
    ('country_code', PurchaseUserInput.country_code.validator),
    ('currency', PurchaseUserInput.currency.validator),
    ('code', PurchaseUserInput.code.validator),
    ('dcode', PurchaseUserInput.dcode.validator),
    ('promo_ids', PurchaseUserInput.promo_ids.validator),
    ('payment_method', PurchaseUserInput.payment_method.validator),
    ('total_price', PurchaseUserInput.total_price.validator),
    ('declaration_confirmation', PurchaseUserInput.declaration_confirmation.validator),
    ('invoice_business_name', PurchaseUserInput.invoice_business_name.validator),
    ('invoice_street_address', PurchaseUserInput.invoice_street_address.validator),
    ('invoice_city', PurchaseUserInput.invoice_city.validator),
    ('invoice_province', PurchaseUserInput.invoice_province.validator),
    ('vat_provincial', PurchaseUserInput.vat_provincial.validator),
    ('payment_method_specific_user_input', PurchaseUserInput.payment_method_specific_user_input.validator)]
RevApiPlannedTransition.subscription_offerings.validator = bv.String()
RevApiPlannedTransition.subscription_offerings.validator._redact = bv.BlotRedactor(None)
RevApiPlannedTransition._all_field_names_ = set([
    'subscription_offerings'])
RevApiPlannedTransition._all_fields_ = [
    ('subscription_offerings', RevApiPlannedTransition.subscription_offerings.validator)]
RevApiPricingToken.preview_request_token.validator = bv.String()
RevApiPricingToken.preview_request_token.validator._redact = bv.BlotRedactor(None)
RevApiPricingToken.subscription_offerings.validator = bv.String()
RevApiPricingToken.subscription_offerings.validator._redact = bv.BlotRedactor(None)
RevApiPricingToken.subscription_id.validator = bv.String()
RevApiPricingToken.subscription_id.validator._redact = bv.BlotRedactor(None)
RevApiPricingToken.subscription_change.validator = bv.String()
RevApiPricingToken.subscription_change.validator._redact = bv.BlotRedactor(None)
RevApiPricingToken._all_field_names_ = set([
    'preview_request_token',
    'subscription_offerings',
    'subscription_id',
    'subscription_change'])
RevApiPricingToken._all_fields_ = [
    ('preview_request_token', RevApiPricingToken.preview_request_token.validator),
    ('subscription_offerings', RevApiPricingToken.subscription_offerings.validator),
    ('subscription_id', RevApiPricingToken.subscription_id.validator),
    ('subscription_change', RevApiPricingToken.subscription_change.validator)]
RevApiSubscriptionChangeInput.when.validator = bv.Int32()
RevApiSubscriptionChangeInput.when.validator._redact = bv.BlotRedactor(None)
RevApiSubscriptionChangeInput.proration_policy.validator = bv.Int32()
RevApiSubscriptionChangeInput.proration_policy.validator._redact = bv.BlotRedactor(None)
RevApiSubscriptionChangeInput.preserve_scheduled_changes.validator = bv.Boolean()
RevApiSubscriptionChangeInput.preserve_scheduled_changes.validator._redact = bv.BlotRedactor(None)
RevApiSubscriptionChangeInput._all_field_names_ = set([
    'when',
    'proration_policy',
    'preserve_scheduled_changes'])
RevApiSubscriptionChangeInput._all_fields_ = [
    ('when', RevApiSubscriptionChangeInput.when.validator),
    ('proration_policy', RevApiSubscriptionChangeInput.proration_policy.validator),
    ('preserve_scheduled_changes', RevApiSubscriptionChangeInput.preserve_scheduled_changes.validator)]
Schedule._unknown_validator = bv.Void()
Schedule._monthly_validator = bv.Void()
Schedule._yearly_validator = bv.Void()
Schedule._other_validator = bv.Void()
Schedule._tagmap = {
    'unknown': Schedule._unknown_validator,
    'monthly': Schedule._monthly_validator,
    'yearly': Schedule._yearly_validator,
    'other': Schedule._other_validator }
Schedule.unknown = Schedule('unknown')
Schedule.monthly = Schedule('monthly')
Schedule.yearly = Schedule('yearly')
Schedule.other = Schedule('other')
ScheduledActionType._unknown_scheduled_action_validator = bv.Void()
ScheduledActionType._plan_downgrade_validator = bv.Void()
ScheduledActionType._billing_schedule_change_validator = bv.Void()
ScheduledActionType._plan_cancellation_validator = bv.Void()
ScheduledActionType._license_removal_validator = bv.Void()
ScheduledActionType._addon_removal_validator = bv.Void()
ScheduledActionType._group_plan_cancellation_validator = bv.Void()
ScheduledActionType._all_scheduled_action_validator = bv.Void()
ScheduledActionType._other_validator = bv.Void()
ScheduledActionType._tagmap = {
    'unknown_scheduled_action': ScheduledActionType._unknown_scheduled_action_validator,
    'plan_downgrade': ScheduledActionType._plan_downgrade_validator,
    'billing_schedule_change': ScheduledActionType._billing_schedule_change_validator,
    'plan_cancellation': ScheduledActionType._plan_cancellation_validator,
    'license_removal': ScheduledActionType._license_removal_validator,
    'addon_removal': ScheduledActionType._addon_removal_validator,
    'group_plan_cancellation': ScheduledActionType._group_plan_cancellation_validator,
    'all_scheduled_action': ScheduledActionType._all_scheduled_action_validator,
    'other': ScheduledActionType._other_validator }
ScheduledActionType.unknown_scheduled_action = ScheduledActionType('unknown_scheduled_action')
ScheduledActionType.plan_downgrade = ScheduledActionType('plan_downgrade')
ScheduledActionType.billing_schedule_change = ScheduledActionType('billing_schedule_change')
ScheduledActionType.plan_cancellation = ScheduledActionType('plan_cancellation')
ScheduledActionType.license_removal = ScheduledActionType('license_removal')
ScheduledActionType.addon_removal = ScheduledActionType('addon_removal')
ScheduledActionType.group_plan_cancellation = ScheduledActionType('group_plan_cancellation')
ScheduledActionType.all_scheduled_action = ScheduledActionType('all_scheduled_action')
ScheduledActionType.other = ScheduledActionType('other')
ScheduledChangesInfo.scheduled_actions.validator = bv.Nullable(bv.List(ScheduledActionType_validator))
ScheduledChangesInfo.upcoming_contract_length.validator = bv.Nullable(ContractLength_validator)
ScheduledChangesInfo.upcoming_product_info.validator = bv.Nullable(ProductInfo_validator)
ScheduledChangesInfo.upcoming_addons_info.validator = bv.Nullable(bv.List(AddonSubscription_validator))
ScheduledChangesInfo.upcoming_license_info.validator = bv.Nullable(LicenseInfo_validator)
ScheduledChangesInfo.upcoming_quota.validator = bv.Int64()
ScheduledChangesInfo.upcoming_quota.validator._redact = bv.BlotRedactor(None)
ScheduledChangesInfo._all_field_names_ = set([
    'scheduled_actions',
    'upcoming_contract_length',
    'upcoming_product_info',
    'upcoming_addons_info',
    'upcoming_license_info',
    'upcoming_quota'])
ScheduledChangesInfo._all_fields_ = [
    ('scheduled_actions', ScheduledChangesInfo.scheduled_actions.validator),
    ('upcoming_contract_length', ScheduledChangesInfo.upcoming_contract_length.validator),
    ('upcoming_product_info', ScheduledChangesInfo.upcoming_product_info.validator),
    ('upcoming_addons_info', ScheduledChangesInfo.upcoming_addons_info.validator),
    ('upcoming_license_info', ScheduledChangesInfo.upcoming_license_info.validator),
    ('upcoming_quota', ScheduledChangesInfo.upcoming_quota.validator)]
ScheduledChangesMetadata.scheduled_actions.validator = bv.Nullable(bv.List(ScheduledActionType_validator))
ScheduledChangesMetadata.upcoming_contract_length.validator = bv.Nullable(ContractLength_validator)
ScheduledChangesMetadata.upcoming_product_info.validator = bv.Nullable(ProductInfo_validator)
ScheduledChangesMetadata.upcoming_license_info.validator = bv.Nullable(LicenseInfo_validator)
ScheduledChangesMetadata.upcoming_quota.validator = bv.Int64()
ScheduledChangesMetadata.upcoming_quota.validator._redact = bv.BlotRedactor(None)
ScheduledChangesMetadata._all_field_names_ = set([
    'scheduled_actions',
    'upcoming_contract_length',
    'upcoming_product_info',
    'upcoming_license_info',
    'upcoming_quota'])
ScheduledChangesMetadata._all_fields_ = [
    ('scheduled_actions', ScheduledChangesMetadata.scheduled_actions.validator),
    ('upcoming_contract_length', ScheduledChangesMetadata.upcoming_contract_length.validator),
    ('upcoming_product_info', ScheduledChangesMetadata.upcoming_product_info.validator),
    ('upcoming_license_info', ScheduledChangesMetadata.upcoming_license_info.validator),
    ('upcoming_quota', ScheduledChangesMetadata.upcoming_quota.validator)]
StorageUsageData.total_usage.validator = bv.String()
StorageUsageData.total_usage.validator._redact = bv.BlotRedactor(None)
StorageUsageData.quota.validator = bv.String()
StorageUsageData.quota.validator._redact = bv.BlotRedactor(None)
StorageUsageData.percentage_used.validator = bv.String()
StorageUsageData.percentage_used.validator._redact = bv.BlotRedactor(None)
StorageUsageData.total_shared_usage.validator = bv.String()
StorageUsageData.total_shared_usage.validator._redact = bv.BlotRedactor(None)
StorageUsageData.total_unshared_usage.validator = bv.String()
StorageUsageData.total_unshared_usage.validator._redact = bv.BlotRedactor(None)
StorageUsageData.unused_space.validator = bv.String()
StorageUsageData.unused_space.validator._redact = bv.BlotRedactor(None)
StorageUsageData.percentage_used_number.validator = bv.Float32()
StorageUsageData.percentage_used_number.validator._redact = bv.BlotRedactor(None)
StorageUsageData.backup_usage.validator = bv.String()
StorageUsageData.backup_usage.validator._redact = bv.BlotRedactor(None)
StorageUsageData.backup_raw_usage.validator = bv.Float32()
StorageUsageData.backup_raw_usage.validator._redact = bv.BlotRedactor(None)
StorageUsageData.shared_percentage_used_number.validator = bv.Float32()
StorageUsageData.shared_percentage_used_number.validator._redact = bv.BlotRedactor(None)
StorageUsageData.unshared_percentage_used_number.validator = bv.Float32()
StorageUsageData.unshared_percentage_used_number.validator._redact = bv.BlotRedactor(None)
StorageUsageData.backup_percentage_used_number.validator = bv.Float32()
StorageUsageData.backup_percentage_used_number.validator._redact = bv.BlotRedactor(None)
StorageUsageData.replay_usage.validator = bv.String()
StorageUsageData.replay_usage.validator._redact = bv.BlotRedactor(None)
StorageUsageData.replay_percentage_used_number.validator = bv.Float32()
StorageUsageData.replay_percentage_used_number.validator._redact = bv.BlotRedactor(None)
StorageUsageData.replay_raw_usage.validator = bv.Float32()
StorageUsageData.replay_raw_usage.validator._redact = bv.BlotRedactor(None)
StorageUsageData.formatted_quota_cap.validator = bv.String()
StorageUsageData.formatted_quota_cap.validator._redact = bv.BlotRedactor(None)
StorageUsageData.raw_quota.validator = bv.Int64()
StorageUsageData.raw_quota.validator._redact = bv.BlotRedactor(None)
StorageUsageData._all_field_names_ = set([
    'total_usage',
    'quota',
    'percentage_used',
    'total_shared_usage',
    'total_unshared_usage',
    'unused_space',
    'percentage_used_number',
    'backup_usage',
    'backup_raw_usage',
    'shared_percentage_used_number',
    'unshared_percentage_used_number',
    'backup_percentage_used_number',
    'replay_usage',
    'replay_percentage_used_number',
    'replay_raw_usage',
    'formatted_quota_cap',
    'raw_quota'])
StorageUsageData._all_fields_ = [
    ('total_usage', StorageUsageData.total_usage.validator),
    ('quota', StorageUsageData.quota.validator),
    ('percentage_used', StorageUsageData.percentage_used.validator),
    ('total_shared_usage', StorageUsageData.total_shared_usage.validator),
    ('total_unshared_usage', StorageUsageData.total_unshared_usage.validator),
    ('unused_space', StorageUsageData.unused_space.validator),
    ('percentage_used_number', StorageUsageData.percentage_used_number.validator),
    ('backup_usage', StorageUsageData.backup_usage.validator),
    ('backup_raw_usage', StorageUsageData.backup_raw_usage.validator),
    ('shared_percentage_used_number', StorageUsageData.shared_percentage_used_number.validator),
    ('unshared_percentage_used_number', StorageUsageData.unshared_percentage_used_number.validator),
    ('backup_percentage_used_number', StorageUsageData.backup_percentage_used_number.validator),
    ('replay_usage', StorageUsageData.replay_usage.validator),
    ('replay_percentage_used_number', StorageUsageData.replay_percentage_used_number.validator),
    ('replay_raw_usage', StorageUsageData.replay_raw_usage.validator),
    ('formatted_quota_cap', StorageUsageData.formatted_quota_cap.validator),
    ('raw_quota', StorageUsageData.raw_quota.validator)]
StorefrontPlatformAiCreditPurchaseAction._ai_credit_purchase_action_unavailable_validator = bv.Void()
StorefrontPlatformAiCreditPurchaseAction._ai_credit_purchase_action_open_portable_checkout_validator = bv.Void()
StorefrontPlatformAiCreditPurchaseAction._ai_credit_purchase_action_open_stackable_addon_modal_validator = bv.Void()
StorefrontPlatformAiCreditPurchaseAction._other_validator = bv.Void()
StorefrontPlatformAiCreditPurchaseAction._tagmap = {
    'ai_credit_purchase_action_unavailable': StorefrontPlatformAiCreditPurchaseAction._ai_credit_purchase_action_unavailable_validator,
    'ai_credit_purchase_action_open_portable_checkout': StorefrontPlatformAiCreditPurchaseAction._ai_credit_purchase_action_open_portable_checkout_validator,
    'ai_credit_purchase_action_open_stackable_addon_modal': StorefrontPlatformAiCreditPurchaseAction._ai_credit_purchase_action_open_stackable_addon_modal_validator,
    'other': StorefrontPlatformAiCreditPurchaseAction._other_validator }
StorefrontPlatformAiCreditPurchaseAction.ai_credit_purchase_action_unavailable = StorefrontPlatformAiCreditPurchaseAction('ai_credit_purchase_action_unavailable')
StorefrontPlatformAiCreditPurchaseAction.ai_credit_purchase_action_open_portable_checkout = StorefrontPlatformAiCreditPurchaseAction('ai_credit_purchase_action_open_portable_checkout')
StorefrontPlatformAiCreditPurchaseAction.ai_credit_purchase_action_open_stackable_addon_modal = StorefrontPlatformAiCreditPurchaseAction('ai_credit_purchase_action_open_stackable_addon_modal')
StorefrontPlatformAiCreditPurchaseAction.other = StorefrontPlatformAiCreditPurchaseAction('other')
StorefrontPlatformBillLineItemType._unknown_item_type_validator = bv.Void()
StorefrontPlatformBillLineItemType._debit_validator = bv.Void()
StorefrontPlatformBillLineItemType._credit_validator = bv.Void()
StorefrontPlatformBillLineItemType._reversal_validator = bv.Void()
StorefrontPlatformBillLineItemType._other_validator = bv.Void()
StorefrontPlatformBillLineItemType._tagmap = {
    'unknown_item_type': StorefrontPlatformBillLineItemType._unknown_item_type_validator,
    'debit': StorefrontPlatformBillLineItemType._debit_validator,
    'credit': StorefrontPlatformBillLineItemType._credit_validator,
    'reversal': StorefrontPlatformBillLineItemType._reversal_validator,
    'other': StorefrontPlatformBillLineItemType._other_validator }
StorefrontPlatformBillLineItemType.unknown_item_type = StorefrontPlatformBillLineItemType('unknown_item_type')
StorefrontPlatformBillLineItemType.debit = StorefrontPlatformBillLineItemType('debit')
StorefrontPlatformBillLineItemType.credit = StorefrontPlatformBillLineItemType('credit')
StorefrontPlatformBillLineItemType.reversal = StorefrontPlatformBillLineItemType('reversal')
StorefrontPlatformBillLineItemType.other = StorefrontPlatformBillLineItemType('other')
StorefrontPlatformBillStatus._unknown_bill_status_validator = bv.Void()
StorefrontPlatformBillStatus._pending_validator = bv.Void()
StorefrontPlatformBillStatus._completed_validator = bv.Void()
StorefrontPlatformBillStatus._failed_validator = bv.Void()
StorefrontPlatformBillStatus._voided_validator = bv.Void()
StorefrontPlatformBillStatus._other_validator = bv.Void()
StorefrontPlatformBillStatus._tagmap = {
    'unknown_bill_status': StorefrontPlatformBillStatus._unknown_bill_status_validator,
    'pending': StorefrontPlatformBillStatus._pending_validator,
    'completed': StorefrontPlatformBillStatus._completed_validator,
    'failed': StorefrontPlatformBillStatus._failed_validator,
    'voided': StorefrontPlatformBillStatus._voided_validator,
    'other': StorefrontPlatformBillStatus._other_validator }
StorefrontPlatformBillStatus.unknown_bill_status = StorefrontPlatformBillStatus('unknown_bill_status')
StorefrontPlatformBillStatus.pending = StorefrontPlatformBillStatus('pending')
StorefrontPlatformBillStatus.completed = StorefrontPlatformBillStatus('completed')
StorefrontPlatformBillStatus.failed = StorefrontPlatformBillStatus('failed')
StorefrontPlatformBillStatus.voided = StorefrontPlatformBillStatus('voided')
StorefrontPlatformBillStatus.other = StorefrontPlatformBillStatus('other')
StorefrontPlatformBillTransactionType._unknown_transaction_type_validator = bv.Void()
StorefrontPlatformBillTransactionType._payment_validator = bv.Void()
StorefrontPlatformBillTransactionType._refund_validator = bv.Void()
StorefrontPlatformBillTransactionType._chargeback_validator = bv.Void()
StorefrontPlatformBillTransactionType._other_validator = bv.Void()
StorefrontPlatformBillTransactionType._tagmap = {
    'unknown_transaction_type': StorefrontPlatformBillTransactionType._unknown_transaction_type_validator,
    'payment': StorefrontPlatformBillTransactionType._payment_validator,
    'refund': StorefrontPlatformBillTransactionType._refund_validator,
    'chargeback': StorefrontPlatformBillTransactionType._chargeback_validator,
    'other': StorefrontPlatformBillTransactionType._other_validator }
StorefrontPlatformBillTransactionType.unknown_transaction_type = StorefrontPlatformBillTransactionType('unknown_transaction_type')
StorefrontPlatformBillTransactionType.payment = StorefrontPlatformBillTransactionType('payment')
StorefrontPlatformBillTransactionType.refund = StorefrontPlatformBillTransactionType('refund')
StorefrontPlatformBillTransactionType.chargeback = StorefrontPlatformBillTransactionType('chargeback')
StorefrontPlatformBillTransactionType.other = StorefrontPlatformBillTransactionType('other')
StorefrontPlatformBillingProvider._unknown_billing_provider_validator = bv.Void()
StorefrontPlatformBillingProvider._web_validator = bv.Void()
StorefrontPlatformBillingProvider._mobile_ios_validator = bv.Void()
StorefrontPlatformBillingProvider._mobile_google_validator = bv.Void()
StorefrontPlatformBillingProvider._reseller_validator = bv.Void()
StorefrontPlatformBillingProvider._outbound_validator = bv.Void()
StorefrontPlatformBillingProvider._other_validator = bv.Void()
StorefrontPlatformBillingProvider._tagmap = {
    'unknown_billing_provider': StorefrontPlatformBillingProvider._unknown_billing_provider_validator,
    'web': StorefrontPlatformBillingProvider._web_validator,
    'mobile_ios': StorefrontPlatformBillingProvider._mobile_ios_validator,
    'mobile_google': StorefrontPlatformBillingProvider._mobile_google_validator,
    'reseller': StorefrontPlatformBillingProvider._reseller_validator,
    'outbound': StorefrontPlatformBillingProvider._outbound_validator,
    'other': StorefrontPlatformBillingProvider._other_validator }
StorefrontPlatformBillingProvider.unknown_billing_provider = StorefrontPlatformBillingProvider('unknown_billing_provider')
StorefrontPlatformBillingProvider.web = StorefrontPlatformBillingProvider('web')
StorefrontPlatformBillingProvider.mobile_ios = StorefrontPlatformBillingProvider('mobile_ios')
StorefrontPlatformBillingProvider.mobile_google = StorefrontPlatformBillingProvider('mobile_google')
StorefrontPlatformBillingProvider.reseller = StorefrontPlatformBillingProvider('reseller')
StorefrontPlatformBillingProvider.outbound = StorefrontPlatformBillingProvider('outbound')
StorefrontPlatformBillingProvider.other = StorefrontPlatformBillingProvider('other')
StorefrontPlatformConfiguration.session_id.validator = bv.String()
StorefrontPlatformConfiguration.session_id.validator._redact = bv.BlotRedactor(None)
StorefrontPlatformConfiguration.request_ip.validator = bv.String()
StorefrontPlatformConfiguration.request_ip.validator._redact = bv.BlotRedactor(None)
StorefrontPlatformConfiguration.ip_country.validator = bv.String()
StorefrontPlatformConfiguration.ip_country.validator._redact = bv.BlotRedactor(None)
StorefrontPlatformConfiguration.locale.validator = bv.String()
StorefrontPlatformConfiguration.locale.validator._redact = bv.BlotRedactor(None)
StorefrontPlatformConfiguration.checkout_use_revapi.validator = OnOffConfigValue_validator
StorefrontPlatformConfiguration.nml_exp_variant.validator = NmlVariantValue_validator
StorefrontPlatformConfiguration.backup_usage_breakdown.validator = OnOffConfigValue_validator
StorefrontPlatformConfiguration.abuse_disable_self_serve.validator = OnOffConfigValue_validator
StorefrontPlatformConfiguration.partial_provisioning.validator = OnOffConfigValue_validator
StorefrontPlatformConfiguration.dash_addon.validator = OnOffConfigValue_validator
StorefrontPlatformConfiguration.replay_usage_breakdown.validator = OnOffConfigValue_validator
StorefrontPlatformConfiguration.premium_support_essentials_addon.validator = OnOffConfigValue_validator
StorefrontPlatformConfiguration.show_sign_standard_addon.validator = OnOffConfigValue_validator
StorefrontPlatformConfiguration.individual_stackable_space_enabled.validator = OnOffConfigValue_validator
StorefrontPlatformConfiguration.local_data_residency_addon.validator = OnOffConfigValue_validator
StorefrontPlatformConfiguration.use_multi_product_rev_api.validator = OnOffConfigValue_validator
StorefrontPlatformConfiguration.simplified_core_pnp_2025_std_min_1_license_enabled.validator = OnOffConfigValue_validator
StorefrontPlatformConfiguration.one_license_standard_plan_enabled.validator = OnOffConfigValue_validator
StorefrontPlatformConfiguration.ai_credit_addon_purchase_surface_enabled.validator = OnOffConfigValue_validator
StorefrontPlatformConfiguration.legacy_plus_space_pack_stackability_enabled.validator = OnOffConfigValue_validator
StorefrontPlatformConfiguration.additional_plans_legacy_space_pack_stackability_enabled.validator = OnOffConfigValue_validator
StorefrontPlatformConfiguration._all_field_names_ = set([
    'session_id',
    'request_ip',
    'ip_country',
    'locale',
    'checkout_use_revapi',
    'nml_exp_variant',
    'backup_usage_breakdown',
    'abuse_disable_self_serve',
    'partial_provisioning',
    'dash_addon',
    'replay_usage_breakdown',
    'premium_support_essentials_addon',
    'show_sign_standard_addon',
    'individual_stackable_space_enabled',
    'local_data_residency_addon',
    'use_multi_product_rev_api',
    'simplified_core_pnp_2025_std_min_1_license_enabled',
    'one_license_standard_plan_enabled',
    'ai_credit_addon_purchase_surface_enabled',
    'legacy_plus_space_pack_stackability_enabled',
    'additional_plans_legacy_space_pack_stackability_enabled'])
StorefrontPlatformConfiguration._all_fields_ = [
    ('session_id', StorefrontPlatformConfiguration.session_id.validator),
    ('request_ip', StorefrontPlatformConfiguration.request_ip.validator),
    ('ip_country', StorefrontPlatformConfiguration.ip_country.validator),
    ('locale', StorefrontPlatformConfiguration.locale.validator),
    ('checkout_use_revapi', StorefrontPlatformConfiguration.checkout_use_revapi.validator),
    ('nml_exp_variant', StorefrontPlatformConfiguration.nml_exp_variant.validator),
    ('backup_usage_breakdown', StorefrontPlatformConfiguration.backup_usage_breakdown.validator),
    ('abuse_disable_self_serve', StorefrontPlatformConfiguration.abuse_disable_self_serve.validator),
    ('partial_provisioning', StorefrontPlatformConfiguration.partial_provisioning.validator),
    ('dash_addon', StorefrontPlatformConfiguration.dash_addon.validator),
    ('replay_usage_breakdown', StorefrontPlatformConfiguration.replay_usage_breakdown.validator),
    ('premium_support_essentials_addon', StorefrontPlatformConfiguration.premium_support_essentials_addon.validator),
    ('show_sign_standard_addon', StorefrontPlatformConfiguration.show_sign_standard_addon.validator),
    ('individual_stackable_space_enabled', StorefrontPlatformConfiguration.individual_stackable_space_enabled.validator),
    ('local_data_residency_addon', StorefrontPlatformConfiguration.local_data_residency_addon.validator),
    ('use_multi_product_rev_api', StorefrontPlatformConfiguration.use_multi_product_rev_api.validator),
    ('simplified_core_pnp_2025_std_min_1_license_enabled', StorefrontPlatformConfiguration.simplified_core_pnp_2025_std_min_1_license_enabled.validator),
    ('one_license_standard_plan_enabled', StorefrontPlatformConfiguration.one_license_standard_plan_enabled.validator),
    ('ai_credit_addon_purchase_surface_enabled', StorefrontPlatformConfiguration.ai_credit_addon_purchase_surface_enabled.validator),
    ('legacy_plus_space_pack_stackability_enabled', StorefrontPlatformConfiguration.legacy_plus_space_pack_stackability_enabled.validator),
    ('additional_plans_legacy_space_pack_stackability_enabled', StorefrontPlatformConfiguration.additional_plans_legacy_space_pack_stackability_enabled.validator)]
StorefrontPlatformContractLengthUnit._unknown_contract_length_unit_validator = bv.Void()
StorefrontPlatformContractLengthUnit._day_validator = bv.Void()
StorefrontPlatformContractLengthUnit._month_validator = bv.Void()
StorefrontPlatformContractLengthUnit._year_validator = bv.Void()
StorefrontPlatformContractLengthUnit._unlimited_validator = bv.Void()
StorefrontPlatformContractLengthUnit._other_validator = bv.Void()
StorefrontPlatformContractLengthUnit._tagmap = {
    'unknown_contract_length_unit': StorefrontPlatformContractLengthUnit._unknown_contract_length_unit_validator,
    'day': StorefrontPlatformContractLengthUnit._day_validator,
    'month': StorefrontPlatformContractLengthUnit._month_validator,
    'year': StorefrontPlatformContractLengthUnit._year_validator,
    'unlimited': StorefrontPlatformContractLengthUnit._unlimited_validator,
    'other': StorefrontPlatformContractLengthUnit._other_validator }
StorefrontPlatformContractLengthUnit.unknown_contract_length_unit = StorefrontPlatformContractLengthUnit('unknown_contract_length_unit')
StorefrontPlatformContractLengthUnit.day = StorefrontPlatformContractLengthUnit('day')
StorefrontPlatformContractLengthUnit.month = StorefrontPlatformContractLengthUnit('month')
StorefrontPlatformContractLengthUnit.year = StorefrontPlatformContractLengthUnit('year')
StorefrontPlatformContractLengthUnit.unlimited = StorefrontPlatformContractLengthUnit('unlimited')
StorefrontPlatformContractLengthUnit.other = StorefrontPlatformContractLengthUnit('other')
StorefrontPlatformCreditType._unknown_credit_type_validator = bv.Void()
StorefrontPlatformCreditType._mastercard_validator = bv.Void()
StorefrontPlatformCreditType._visa_validator = bv.Void()
StorefrontPlatformCreditType._amex_validator = bv.Void()
StorefrontPlatformCreditType._discover_validator = bv.Void()
StorefrontPlatformCreditType._cartes_bancaires_validator = bv.Void()
StorefrontPlatformCreditType._paypal_credit_validator = bv.Void()
StorefrontPlatformCreditType._sepa_debit_validator = bv.Void()
StorefrontPlatformCreditType._jcb_validator = bv.Void()
StorefrontPlatformCreditType._elo_validator = bv.Void()
StorefrontPlatformCreditType._union_pay_validator = bv.Void()
StorefrontPlatformCreditType._diners_club_validator = bv.Void()
StorefrontPlatformCreditType._other_validator = bv.Void()
StorefrontPlatformCreditType._tagmap = {
    'unknown_credit_type': StorefrontPlatformCreditType._unknown_credit_type_validator,
    'mastercard': StorefrontPlatformCreditType._mastercard_validator,
    'visa': StorefrontPlatformCreditType._visa_validator,
    'amex': StorefrontPlatformCreditType._amex_validator,
    'discover': StorefrontPlatformCreditType._discover_validator,
    'cartes_bancaires': StorefrontPlatformCreditType._cartes_bancaires_validator,
    'paypal_credit': StorefrontPlatformCreditType._paypal_credit_validator,
    'sepa_debit': StorefrontPlatformCreditType._sepa_debit_validator,
    'jcb': StorefrontPlatformCreditType._jcb_validator,
    'elo': StorefrontPlatformCreditType._elo_validator,
    'union_pay': StorefrontPlatformCreditType._union_pay_validator,
    'diners_club': StorefrontPlatformCreditType._diners_club_validator,
    'other': StorefrontPlatformCreditType._other_validator }
StorefrontPlatformCreditType.unknown_credit_type = StorefrontPlatformCreditType('unknown_credit_type')
StorefrontPlatformCreditType.mastercard = StorefrontPlatformCreditType('mastercard')
StorefrontPlatformCreditType.visa = StorefrontPlatformCreditType('visa')
StorefrontPlatformCreditType.amex = StorefrontPlatformCreditType('amex')
StorefrontPlatformCreditType.discover = StorefrontPlatformCreditType('discover')
StorefrontPlatformCreditType.cartes_bancaires = StorefrontPlatformCreditType('cartes_bancaires')
StorefrontPlatformCreditType.paypal_credit = StorefrontPlatformCreditType('paypal_credit')
StorefrontPlatformCreditType.sepa_debit = StorefrontPlatformCreditType('sepa_debit')
StorefrontPlatformCreditType.jcb = StorefrontPlatformCreditType('jcb')
StorefrontPlatformCreditType.elo = StorefrontPlatformCreditType('elo')
StorefrontPlatformCreditType.union_pay = StorefrontPlatformCreditType('union_pay')
StorefrontPlatformCreditType.diners_club = StorefrontPlatformCreditType('diners_club')
StorefrontPlatformCreditType.other = StorefrontPlatformCreditType('other')
StorefrontPlatformPaymentMethod._unknown_payment_method_validator = bv.Void()
StorefrontPlatformPaymentMethod._payment_card_validator = bv.Void()
StorefrontPlatformPaymentMethod._ideal_validator = bv.Void()
StorefrontPlatformPaymentMethod._sepa_validator = bv.Void()
StorefrontPlatformPaymentMethod._paypal_validator = bv.Void()
StorefrontPlatformPaymentMethod._ios_validator = bv.Void()
StorefrontPlatformPaymentMethod._apple_pay_validator = bv.Void()
StorefrontPlatformPaymentMethod._dlocal_rbi_validator = bv.Void()
StorefrontPlatformPaymentMethod._google_play_validator = bv.Void()
StorefrontPlatformPaymentMethod._no_payment_validator = bv.Void()
StorefrontPlatformPaymentMethod._stripe_validator = bv.Void()
StorefrontPlatformPaymentMethod._other_validator = bv.Void()
StorefrontPlatformPaymentMethod._tagmap = {
    'unknown_payment_method': StorefrontPlatformPaymentMethod._unknown_payment_method_validator,
    'payment_card': StorefrontPlatformPaymentMethod._payment_card_validator,
    'ideal': StorefrontPlatformPaymentMethod._ideal_validator,
    'sepa': StorefrontPlatformPaymentMethod._sepa_validator,
    'paypal': StorefrontPlatformPaymentMethod._paypal_validator,
    'ios': StorefrontPlatformPaymentMethod._ios_validator,
    'apple_pay': StorefrontPlatformPaymentMethod._apple_pay_validator,
    'dlocal_rbi': StorefrontPlatformPaymentMethod._dlocal_rbi_validator,
    'google_play': StorefrontPlatformPaymentMethod._google_play_validator,
    'no_payment': StorefrontPlatformPaymentMethod._no_payment_validator,
    'stripe': StorefrontPlatformPaymentMethod._stripe_validator,
    'other': StorefrontPlatformPaymentMethod._other_validator }
StorefrontPlatformPaymentMethod.unknown_payment_method = StorefrontPlatformPaymentMethod('unknown_payment_method')
StorefrontPlatformPaymentMethod.payment_card = StorefrontPlatformPaymentMethod('payment_card')
StorefrontPlatformPaymentMethod.ideal = StorefrontPlatformPaymentMethod('ideal')
StorefrontPlatformPaymentMethod.sepa = StorefrontPlatformPaymentMethod('sepa')
StorefrontPlatformPaymentMethod.paypal = StorefrontPlatformPaymentMethod('paypal')
StorefrontPlatformPaymentMethod.ios = StorefrontPlatformPaymentMethod('ios')
StorefrontPlatformPaymentMethod.apple_pay = StorefrontPlatformPaymentMethod('apple_pay')
StorefrontPlatformPaymentMethod.dlocal_rbi = StorefrontPlatformPaymentMethod('dlocal_rbi')
StorefrontPlatformPaymentMethod.google_play = StorefrontPlatformPaymentMethod('google_play')
StorefrontPlatformPaymentMethod.no_payment = StorefrontPlatformPaymentMethod('no_payment')
StorefrontPlatformPaymentMethod.stripe = StorefrontPlatformPaymentMethod('stripe')
StorefrontPlatformPaymentMethod.other = StorefrontPlatformPaymentMethod('other')
StorefrontPlatformProductCategory._unknown_product_category_validator = bv.Void()
StorefrontPlatformProductCategory._plan_validator = bv.Void()
StorefrontPlatformProductCategory._addon_validator = bv.Void()
StorefrontPlatformProductCategory._license_validator = bv.Void()
StorefrontPlatformProductCategory._trial_validator = bv.Void()
StorefrontPlatformProductCategory._other_validator = bv.Void()
StorefrontPlatformProductCategory._tagmap = {
    'unknown_product_category': StorefrontPlatformProductCategory._unknown_product_category_validator,
    'plan': StorefrontPlatformProductCategory._plan_validator,
    'addon': StorefrontPlatformProductCategory._addon_validator,
    'license': StorefrontPlatformProductCategory._license_validator,
    'trial': StorefrontPlatformProductCategory._trial_validator,
    'other': StorefrontPlatformProductCategory._other_validator }
StorefrontPlatformProductCategory.unknown_product_category = StorefrontPlatformProductCategory('unknown_product_category')
StorefrontPlatformProductCategory.plan = StorefrontPlatformProductCategory('plan')
StorefrontPlatformProductCategory.addon = StorefrontPlatformProductCategory('addon')
StorefrontPlatformProductCategory.license = StorefrontPlatformProductCategory('license')
StorefrontPlatformProductCategory.trial = StorefrontPlatformProductCategory('trial')
StorefrontPlatformProductCategory.other = StorefrontPlatformProductCategory('other')
StorefrontPlatformProductLine._unknown_product_line_validator = bv.Void()
StorefrontPlatformProductLine._single_fss_validator = bv.Void()
StorefrontPlatformProductLine._multi_fss_validator = bv.Void()
StorefrontPlatformProductLine._single_hellosign_validator = bv.Void()
StorefrontPlatformProductLine._multi_replay_validator = bv.Void()
StorefrontPlatformProductLine._multi_dash_validator = bv.Void()
StorefrontPlatformProductLine._single_dash_validator = bv.Void()
StorefrontPlatformProductLine._multi_dropbox_os_validator = bv.Void()
StorefrontPlatformProductLine._multi_protect_validator = bv.Void()
StorefrontPlatformProductLine._multi_send_validator = bv.Void()
StorefrontPlatformProductLine._other_validator = bv.Void()
StorefrontPlatformProductLine._tagmap = {
    'unknown_product_line': StorefrontPlatformProductLine._unknown_product_line_validator,
    'single_fss': StorefrontPlatformProductLine._single_fss_validator,
    'multi_fss': StorefrontPlatformProductLine._multi_fss_validator,
    'single_hellosign': StorefrontPlatformProductLine._single_hellosign_validator,
    'multi_replay': StorefrontPlatformProductLine._multi_replay_validator,
    'multi_dash': StorefrontPlatformProductLine._multi_dash_validator,
    'single_dash': StorefrontPlatformProductLine._single_dash_validator,
    'multi_dropbox_os': StorefrontPlatformProductLine._multi_dropbox_os_validator,
    'multi_protect': StorefrontPlatformProductLine._multi_protect_validator,
    'multi_send': StorefrontPlatformProductLine._multi_send_validator,
    'other': StorefrontPlatformProductLine._other_validator }
StorefrontPlatformProductLine.unknown_product_line = StorefrontPlatformProductLine('unknown_product_line')
StorefrontPlatformProductLine.single_fss = StorefrontPlatformProductLine('single_fss')
StorefrontPlatformProductLine.multi_fss = StorefrontPlatformProductLine('multi_fss')
StorefrontPlatformProductLine.single_hellosign = StorefrontPlatformProductLine('single_hellosign')
StorefrontPlatformProductLine.multi_replay = StorefrontPlatformProductLine('multi_replay')
StorefrontPlatformProductLine.multi_dash = StorefrontPlatformProductLine('multi_dash')
StorefrontPlatformProductLine.single_dash = StorefrontPlatformProductLine('single_dash')
StorefrontPlatformProductLine.multi_dropbox_os = StorefrontPlatformProductLine('multi_dropbox_os')
StorefrontPlatformProductLine.multi_protect = StorefrontPlatformProductLine('multi_protect')
StorefrontPlatformProductLine.multi_send = StorefrontPlatformProductLine('multi_send')
StorefrontPlatformProductLine.other = StorefrontPlatformProductLine('other')
StorefrontPlatformProductRegistryKey._unknown_registry_validator = bv.Void()
StorefrontPlatformProductRegistryKey._replay_only_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_only_validator = bv.Void()
StorefrontPlatformProductRegistryKey._dash_only_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_standard_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_standard_nml_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_standard_nml_2_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_standard_nml_3_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_standard_nml_4_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_std_nml_ts_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_advanced_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_business_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_business_plus_validator = bv.Void()
StorefrontPlatformProductRegistryKey._dropbox_os_only_validator = bv.Void()
StorefrontPlatformProductRegistryKey._dash_ss_business_validator = bv.Void()
StorefrontPlatformProductRegistryKey._dash_ss_enterprise_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_plus_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_plus_with_replay_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_plus_only_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_plus_or_professional_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_professional_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_essentials_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_family_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_backup_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_basic_extra_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_basic_100_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_basic_200_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_basic_500_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_basic_1_t_validator = bv.Void()
StorefrontPlatformProductRegistryKey._dash_business_managed_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_plus_locked_state_validator = bv.Void()
StorefrontPlatformProductRegistryKey._dash_biz_standard_validator = bv.Void()
StorefrontPlatformProductRegistryKey._dash_for_business_validator = bv.Void()
StorefrontPlatformProductRegistryKey._dash_for_teams_validator = bv.Void()
StorefrontPlatformProductRegistryKey._dash_trial_conversion_one_click_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_teams_test_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_plus_std_nml_3_pt_portable_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_basic_500_v1_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_basic_500_v2_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_plus_with_addons_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_professional_with_addons_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_standard_with_addons_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_advanced_with_addons_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_plus_or_professional_with_addons_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_basic_extra_base_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_plus_std_nml_3_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_plus_or_std_nml_3_validator = bv.Void()
StorefrontPlatformProductRegistryKey._dash_trial_early_conversion_one_click_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_plus_with_evh_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_standard_with_evh_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_basic_extra_v1_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_basic_extra_v2_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_standard_with_dash_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_advanced_with_dash_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_plus_std_nml_3_adv_portable_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_plus_std_nml_3_adv_trial_portable_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_std_adv_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_std_nml_adv_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_std_nml_2_adv_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_std_nml_3_adv_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_std_nml_3_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_std_nml_4_adv_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_std_nml_ts_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_biz_bizplus_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_plus_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_professional_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_essentials_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_backup_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_dash_biz_standard_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_dash_for_teams_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_dash_for_teams_noclick_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_business_pt_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_business_plus_pt_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_standard_pt_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_advanced_pt_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_standard_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_dash_for_teams_90_d_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_dash_for_teams_180_d_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_std_nml_3_adv_pt_portable_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_std_nml_3_pt_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_std_nml_ts_noclick_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_plus_with_addons_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_professional_with_addons_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_std_npt_dash_npt_bulk_test_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_adv_pt_dash_std_pt_bulk_test_validator = bv.Void()
StorefrontPlatformProductRegistryKey._fss_standard_pro_upgrade_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_standard_pt_with_addons_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_advanced_pt_with_addons_validator = bv.Void()
StorefrontPlatformProductRegistryKey._try_fss_basic_500_validator = bv.Void()
StorefrontPlatformProductRegistryKey._ai_credits_addon_validator = bv.Void()
StorefrontPlatformProductRegistryKey._other_validator = bv.Void()
# WARNING: Decompyle incomplete
