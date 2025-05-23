# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: v1/payment/common.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'v1/payment/common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17v1/payment/common.proto\x12\npayment.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\x16\n\x05Money\x12\r\n\x05value\x18\x01 \x01(\t\"\xe2\x01\n\x08Provider\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0f\n\x07\x61pi_key\x18\x04 \x01(\t\x12\x11\n\tis_active\x18\x05 \x01(\x08\x12\x18\n\x0b\x64\x65scription\x18\x06 \x01(\tH\x00\x88\x01\x01\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0e\n\x0c_description\"\xeb\x03\n\x0fMerchantAccount\x12\x13\n\x0bmerchant_id\x18\x01 \x01(\x05\x12\x16\n\tbank_name\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1e\n\x11\x62\x61nk_account_name\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x1d\n\x10\x62\x61nk_branch_name\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x1d\n\x10\x62\x61nk_branch_code\x18\x05 \x01(\tH\x03\x88\x01\x01\x12 \n\x13\x62\x61nk_account_number\x18\x06 \x01(\tH\x04\x88\x01\x01\x12 \n\x13\x62\x61nk_routing_number\x18\x07 \x01(\tH\x05\x88\x01\x01\x12\x18\n\x10\x61\x63\x63ount_currency\x18\x08 \x01(\t\x12\x11\n\tis_active\x18\t \x01(\x08\x12.\n\ncreated_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0c\n\n_bank_nameB\x14\n\x12_bank_account_nameB\x13\n\x11_bank_branch_nameB\x13\n\x11_bank_branch_codeB\x16\n\x14_bank_account_numberB\x16\n\x14_bank_routing_number\"\xd5\x01\n\x17MerchantProviderAccount\x12\x13\n\x0bmerchant_id\x18\x01 \x01(\x05\x12\x13\n\x0bprovider_id\x18\x02 \x01(\t\x12\x0e\n\x06\x61pi_id\x18\x03 \x01(\t\x12\x0f\n\x07\x61pi_key\x18\x04 \x01(\t\x12\x0f\n\x07\x61pi_url\x18\x05 \x01(\t\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xc9\x03\n\x1dMerchantInvoicePaymentDetails\x12\x16\n\x0einvoice_number\x18\x01 \x01(\t\x12)\n\x0e\x61mount_payable\x18\x02 \x01(\x0b\x32\x11.payment.v1.Money\x12\x31\n\x08\x64ue_date\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x12\x35\n\x0cinvoice_date\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01\x88\x01\x01\x12\x13\n\x0binvoice_url\x18\x05 \x01(\t\x12\x13\n\x0bmerchant_id\x18\x06 \x01(\t\x12\x10\n\x08\x63urrency\x18\x07 \x01(\t\x12\x13\n\x0bprovider_id\x18\x08 \x01(\t\x12 \n\x13\x62\x61nk_account_number\x18\t \x01(\tH\x02\x88\x01\x01\x12 \n\x13\x62\x61nk_routing_number\x18\n \x01(\tH\x03\x88\x01\x01\x12\x18\n\x10\x61\x63\x63ount_currency\x18\x0b \x01(\tB\x0b\n\t_due_dateB\x0f\n\r_invoice_dateB\x16\n\x14_bank_account_numberB\x16\n\x14_bank_routing_number\"\xf1\x04\n\x0bTransaction\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0bmerchant_id\x18\x02 \x01(\x05\x12\x18\n\x0bprovider_id\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x16\n\x0einvoice_number\x18\x04 \x01(\t\x12\x14\n\x0creference_id\x18\x05 \x01(\t\x12\"\n\x15\x65xternal_reference_id\x18\x06 \x01(\tH\x01\x88\x01\x01\x12!\n\x06\x61mount\x18\x07 \x01(\x0b\x32\x11.payment.v1.Money\x12\x10\n\x08\x63urrency\x18\x08 \x01(\t\x12\x0c\n\x04type\x18\t \x01(\t\x12\x0e\n\x06status\x18\n \x01(\t\x12\x1b\n\x0estatus_message\x18\x0b \x01(\tH\x02\x88\x01\x01\x12\x16\n\x0epayment_method\x18\x0c \x01(\t\x12\x37\n\x08metadata\x18\r \x03(\x0b\x32%.payment.v1.Transaction.MetadataEntry\x12.\n\ncreated_at\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x0c\x63ompleted_at\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x03\x88\x01\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0e\n\x0c_provider_idB\x18\n\x16_external_reference_idB\x11\n\x0f_status_messageB\x0f\n\r_completed_at\"\xc1\x01\n\x0fPaymentCallback\x12\x14\n\x0creference_id\x18\x01 \x01(\t\x12\x1a\n\x12\x65xternal_reference\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x18\n\x10\x61mount_confirmed\x18\x04 \x01(\x01\x12-\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tsignature\x18\x06 \x01(\t\x12\x10\n\x08raw_data\x18\x07 \x01(\x0c\"\x89\x02\n\x11TransactionFilter\x12\x13\n\x0bmerchant_id\x18\x01 \x01(\x05\x12\x18\n\x0bprovider_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x16\n\x0epayment_method\x18\x04 \x01(\t\x12(\n\x04\x66rom\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x02to\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0einvoice_number\x18\x07 \x01(\t\x12\x14\n\x0creference_id\x18\x08 \x01(\t\x12\r\n\x05limit\x18\t \x01(\x05\x42\x0e\n\x0c_provider_idB\x0cZ\ngo/paymentb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v1.payment.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\ngo/payment'
  _globals['_TRANSACTION_METADATAENTRY']._loaded_options = None
  _globals['_TRANSACTION_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_MONEY']._serialized_start=72
  _globals['_MONEY']._serialized_end=94
  _globals['_PROVIDER']._serialized_start=97
  _globals['_PROVIDER']._serialized_end=323
  _globals['_MERCHANTACCOUNT']._serialized_start=326
  _globals['_MERCHANTACCOUNT']._serialized_end=817
  _globals['_MERCHANTPROVIDERACCOUNT']._serialized_start=820
  _globals['_MERCHANTPROVIDERACCOUNT']._serialized_end=1033
  _globals['_MERCHANTINVOICEPAYMENTDETAILS']._serialized_start=1036
  _globals['_MERCHANTINVOICEPAYMENTDETAILS']._serialized_end=1493
  _globals['_TRANSACTION']._serialized_start=1496
  _globals['_TRANSACTION']._serialized_end=2121
  _globals['_TRANSACTION_METADATAENTRY']._serialized_start=1996
  _globals['_TRANSACTION_METADATAENTRY']._serialized_end=2043
  _globals['_PAYMENTCALLBACK']._serialized_start=2124
  _globals['_PAYMENTCALLBACK']._serialized_end=2317
  _globals['_TRANSACTIONFILTER']._serialized_start=2320
  _globals['_TRANSACTIONFILTER']._serialized_end=2585
# @@protoc_insertion_point(module_scope)
