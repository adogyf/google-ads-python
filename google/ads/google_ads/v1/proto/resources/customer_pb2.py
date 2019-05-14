# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/resources/customer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v1.proto.enums import customer_pay_per_conversion_eligibility_failure_reason_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_customer__pay__per__conversion__eligibility__failure__reason__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/resources/customer.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v1.resourcesB\rCustomerProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources'),
  serialized_pb=_b('\n6google/ads/googleads_v1/proto/resources/customer.proto\x12!google.ads.googleads.v1.resources\x1a`google/ads/googleads_v1/proto/enums/customer_pay_per_conversion_eligibility_failure_reason.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xfe\x07\n\x08\x43ustomer\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\'\n\x02id\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x10\x64\x65scriptive_name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rcurrency_code\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\ttime_zone\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x15tracking_url_template\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10\x66inal_url_suffix\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x14\x61uto_tagging_enabled\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x36\n\x12has_partners_badge\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12+\n\x07manager\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x30\n\x0ctest_account\x18\r \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12W\n\x16\x63\x61ll_reporting_setting\x18\n \x01(\x0b\x32\x37.google.ads.googleads.v1.resources.CallReportingSetting\x12\x61\n\x1b\x63onversion_tracking_setting\x18\x0e \x01(\x0b\x32<.google.ads.googleads.v1.resources.ConversionTrackingSetting\x12R\n\x13remarketing_setting\x18\x0f \x01(\x0b\x32\x35.google.ads.googleads.v1.resources.RemarketingSetting\x12\xbd\x01\n.pay_per_conversion_eligibility_failure_reasons\x18\x10 \x03(\x0e\x32\x84\x01.google.ads.googleads.v1.enums.CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason\"\xd7\x01\n\x14\x43\x61llReportingSetting\x12:\n\x16\x63\x61ll_reporting_enabled\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x45\n!call_conversion_reporting_enabled\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12<\n\x16\x63\x61ll_conversion_action\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xa3\x01\n\x19\x43onversionTrackingSetting\x12;\n\x16\x63onversion_tracking_id\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12I\n$cross_account_conversion_tracking_id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"R\n\x12RemarketingSetting\x12<\n\x16google_global_site_tag\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\xfa\x01\n%com.google.ads.googleads.v1.resourcesB\rCustomerProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_customer__pay__per__conversion__eligibility__failure__reason__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CUSTOMER = _descriptor.Descriptor(
  name='Customer',
  full_name='google.ads.googleads.v1.resources.Customer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.resources.Customer.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v1.resources.Customer.id', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='descriptive_name', full_name='google.ads.googleads.v1.resources.Customer.descriptive_name', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency_code', full_name='google.ads.googleads.v1.resources.Customer.currency_code', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_zone', full_name='google.ads.googleads.v1.resources.Customer.time_zone', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tracking_url_template', full_name='google.ads.googleads.v1.resources.Customer.tracking_url_template', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='final_url_suffix', full_name='google.ads.googleads.v1.resources.Customer.final_url_suffix', index=6,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auto_tagging_enabled', full_name='google.ads.googleads.v1.resources.Customer.auto_tagging_enabled', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_partners_badge', full_name='google.ads.googleads.v1.resources.Customer.has_partners_badge', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manager', full_name='google.ads.googleads.v1.resources.Customer.manager', index=9,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_account', full_name='google.ads.googleads.v1.resources.Customer.test_account', index=10,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='call_reporting_setting', full_name='google.ads.googleads.v1.resources.Customer.call_reporting_setting', index=11,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversion_tracking_setting', full_name='google.ads.googleads.v1.resources.Customer.conversion_tracking_setting', index=12,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remarketing_setting', full_name='google.ads.googleads.v1.resources.Customer.remarketing_setting', index=13,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pay_per_conversion_eligibility_failure_reasons', full_name='google.ads.googleads.v1.resources.Customer.pay_per_conversion_eligibility_failure_reasons', index=14,
      number=16, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=254,
  serialized_end=1276,
)


_CALLREPORTINGSETTING = _descriptor.Descriptor(
  name='CallReportingSetting',
  full_name='google.ads.googleads.v1.resources.CallReportingSetting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='call_reporting_enabled', full_name='google.ads.googleads.v1.resources.CallReportingSetting.call_reporting_enabled', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='call_conversion_reporting_enabled', full_name='google.ads.googleads.v1.resources.CallReportingSetting.call_conversion_reporting_enabled', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='call_conversion_action', full_name='google.ads.googleads.v1.resources.CallReportingSetting.call_conversion_action', index=2,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1279,
  serialized_end=1494,
)


_CONVERSIONTRACKINGSETTING = _descriptor.Descriptor(
  name='ConversionTrackingSetting',
  full_name='google.ads.googleads.v1.resources.ConversionTrackingSetting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conversion_tracking_id', full_name='google.ads.googleads.v1.resources.ConversionTrackingSetting.conversion_tracking_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cross_account_conversion_tracking_id', full_name='google.ads.googleads.v1.resources.ConversionTrackingSetting.cross_account_conversion_tracking_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1497,
  serialized_end=1660,
)


_REMARKETINGSETTING = _descriptor.Descriptor(
  name='RemarketingSetting',
  full_name='google.ads.googleads.v1.resources.RemarketingSetting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='google_global_site_tag', full_name='google.ads.googleads.v1.resources.RemarketingSetting.google_global_site_tag', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1662,
  serialized_end=1744,
)

_CUSTOMER.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CUSTOMER.fields_by_name['descriptive_name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CUSTOMER.fields_by_name['currency_code'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CUSTOMER.fields_by_name['time_zone'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CUSTOMER.fields_by_name['tracking_url_template'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CUSTOMER.fields_by_name['final_url_suffix'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CUSTOMER.fields_by_name['auto_tagging_enabled'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CUSTOMER.fields_by_name['has_partners_badge'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CUSTOMER.fields_by_name['manager'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CUSTOMER.fields_by_name['test_account'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CUSTOMER.fields_by_name['call_reporting_setting'].message_type = _CALLREPORTINGSETTING
_CUSTOMER.fields_by_name['conversion_tracking_setting'].message_type = _CONVERSIONTRACKINGSETTING
_CUSTOMER.fields_by_name['remarketing_setting'].message_type = _REMARKETINGSETTING
_CUSTOMER.fields_by_name['pay_per_conversion_eligibility_failure_reasons'].enum_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_customer__pay__per__conversion__eligibility__failure__reason__pb2._CUSTOMERPAYPERCONVERSIONELIGIBILITYFAILUREREASONENUM_CUSTOMERPAYPERCONVERSIONELIGIBILITYFAILUREREASON
_CALLREPORTINGSETTING.fields_by_name['call_reporting_enabled'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CALLREPORTINGSETTING.fields_by_name['call_conversion_reporting_enabled'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CALLREPORTINGSETTING.fields_by_name['call_conversion_action'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CONVERSIONTRACKINGSETTING.fields_by_name['conversion_tracking_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CONVERSIONTRACKINGSETTING.fields_by_name['cross_account_conversion_tracking_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_REMARKETINGSETTING.fields_by_name['google_global_site_tag'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['Customer'] = _CUSTOMER
DESCRIPTOR.message_types_by_name['CallReportingSetting'] = _CALLREPORTINGSETTING
DESCRIPTOR.message_types_by_name['ConversionTrackingSetting'] = _CONVERSIONTRACKINGSETTING
DESCRIPTOR.message_types_by_name['RemarketingSetting'] = _REMARKETINGSETTING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Customer = _reflection.GeneratedProtocolMessageType('Customer', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMER,
  __module__ = 'google.ads.googleads_v1.proto.resources.customer_pb2'
  ,
  __doc__ = """A customer.
  
  
  Attributes:
      resource_name:
          The resource name of the customer. Customer resource names
          have the form:  ``customers/{customer_id}``
      id:
          The ID of the customer.
      descriptive_name:
          Optional, non-unique descriptive name of the customer.
      currency_code:
          The currency in which the account operates. A subset of the
          currency codes from the ISO 4217 standard is supported.
      time_zone:
          The local timezone ID of the customer.
      tracking_url_template:
          The URL template for constructing a tracking URL out of
          parameters.
      final_url_suffix:
          The URL template for appending params to the final URL
      auto_tagging_enabled:
          Whether auto-tagging is enabled for the customer.
      has_partners_badge:
          Whether the Customer has a Partners program badge. If the
          Customer is not associated with the Partners program, this
          will be false. For more information, see
          https://support.google.com/partners/answer/3125774.
      manager:
          Whether the customer is a manager.
      test_account:
          Whether the customer is a test account.
      call_reporting_setting:
          Call reporting setting for a customer.
      conversion_tracking_setting:
          Conversion tracking setting for a customer.
      remarketing_setting:
          Remarketing setting for a customer.
      pay_per_conversion_eligibility_failure_reasons:
          Reasons why the customer is not eligible to use
          PaymentMode.CONVERSIONS. If the list is empty, the customer is
          eligible. This field is read-only.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.Customer)
  ))
_sym_db.RegisterMessage(Customer)

CallReportingSetting = _reflection.GeneratedProtocolMessageType('CallReportingSetting', (_message.Message,), dict(
  DESCRIPTOR = _CALLREPORTINGSETTING,
  __module__ = 'google.ads.googleads_v1.proto.resources.customer_pb2'
  ,
  __doc__ = """Call reporting setting for a customer.
  
  
  Attributes:
      call_reporting_enabled:
          Enable reporting of phone call events by redirecting them via
          Google System.
      call_conversion_reporting_enabled:
          Whether to enable call conversion reporting.
      call_conversion_action:
          Customer-level call conversion action to attribute a call
          conversion to. If not set a default conversion action is used.
          Only in effect when call\_conversion\_reporting\_enabled is
          set to true.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.CallReportingSetting)
  ))
_sym_db.RegisterMessage(CallReportingSetting)

ConversionTrackingSetting = _reflection.GeneratedProtocolMessageType('ConversionTrackingSetting', (_message.Message,), dict(
  DESCRIPTOR = _CONVERSIONTRACKINGSETTING,
  __module__ = 'google.ads.googleads_v1.proto.resources.customer_pb2'
  ,
  __doc__ = """A collection of customer-wide settings related to Google Ads Conversion
  Tracking.
  
  
  Attributes:
      conversion_tracking_id:
          The conversion tracking id used for this account. This id is
          automatically assigned after any conversion tracking feature
          is used. If the customer doesn't use conversion tracking, this
          is 0. This field is read-only.
      cross_account_conversion_tracking_id:
          The conversion tracking id of the customer's manager. This is
          set when the customer is opted into cross account conversion
          tracking, and it overrides conversion\_tracking\_id. This
          field can only be managed through the Google Ads UI. This
          field is read-only.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.ConversionTrackingSetting)
  ))
_sym_db.RegisterMessage(ConversionTrackingSetting)

RemarketingSetting = _reflection.GeneratedProtocolMessageType('RemarketingSetting', (_message.Message,), dict(
  DESCRIPTOR = _REMARKETINGSETTING,
  __module__ = 'google.ads.googleads_v1.proto.resources.customer_pb2'
  ,
  __doc__ = """Remarketing setting for a customer.
  
  
  Attributes:
      google_global_site_tag:
          The Google global site tag.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.RemarketingSetting)
  ))
_sym_db.RegisterMessage(RemarketingSetting)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
