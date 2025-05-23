from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Money(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class Provider(_message.Message):
    __slots__ = ("code", "name", "type", "api_key", "is_active", "description", "created_at", "updated_at")
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    code: str
    name: str
    type: str
    api_key: str
    is_active: bool
    description: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, code: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., api_key: _Optional[str] = ..., is_active: bool = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MerchantAccount(_message.Message):
    __slots__ = ("merchant_id", "bank_name", "bank_account_name", "bank_branch_name", "bank_branch_code", "bank_account_number", "bank_routing_number", "account_currency", "is_active", "created_at", "updated_at")
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    BANK_NAME_FIELD_NUMBER: _ClassVar[int]
    BANK_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    BANK_BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    BANK_BRANCH_CODE_FIELD_NUMBER: _ClassVar[int]
    BANK_ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BANK_ROUTING_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    merchant_id: int
    bank_name: str
    bank_account_name: str
    bank_branch_name: str
    bank_branch_code: str
    bank_account_number: str
    bank_routing_number: str
    account_currency: str
    is_active: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, merchant_id: _Optional[int] = ..., bank_name: _Optional[str] = ..., bank_account_name: _Optional[str] = ..., bank_branch_name: _Optional[str] = ..., bank_branch_code: _Optional[str] = ..., bank_account_number: _Optional[str] = ..., bank_routing_number: _Optional[str] = ..., account_currency: _Optional[str] = ..., is_active: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MerchantProviderAccount(_message.Message):
    __slots__ = ("merchant_id", "provider_id", "api_id", "api_key", "api_url", "created_at", "updated_at")
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    API_ID_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    API_URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    merchant_id: int
    provider_id: str
    api_id: str
    api_key: str
    api_url: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, merchant_id: _Optional[int] = ..., provider_id: _Optional[str] = ..., api_id: _Optional[str] = ..., api_key: _Optional[str] = ..., api_url: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MerchantInvoicePaymentDetails(_message.Message):
    __slots__ = ("invoice_number", "amount_payable", "due_date", "invoice_date", "invoice_url", "merchant_id", "currency", "provider_id", "bank_account_number", "bank_routing_number", "account_currency")
    INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_PAYABLE_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    INVOICE_DATE_FIELD_NUMBER: _ClassVar[int]
    INVOICE_URL_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    BANK_ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BANK_ROUTING_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    invoice_number: str
    amount_payable: Money
    due_date: _timestamp_pb2.Timestamp
    invoice_date: _timestamp_pb2.Timestamp
    invoice_url: str
    merchant_id: str
    currency: str
    provider_id: str
    bank_account_number: str
    bank_routing_number: str
    account_currency: str
    def __init__(self, invoice_number: _Optional[str] = ..., amount_payable: _Optional[_Union[Money, _Mapping]] = ..., due_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., invoice_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., invoice_url: _Optional[str] = ..., merchant_id: _Optional[str] = ..., currency: _Optional[str] = ..., provider_id: _Optional[str] = ..., bank_account_number: _Optional[str] = ..., bank_routing_number: _Optional[str] = ..., account_currency: _Optional[str] = ...) -> None: ...

class Transaction(_message.Message):
    __slots__ = ("id", "merchant_id", "provider_id", "invoice_number", "reference_id", "external_reference_id", "amount", "currency", "type", "status", "status_message", "payment_method", "metadata", "created_at", "updated_at", "completed_at")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    merchant_id: int
    provider_id: str
    invoice_number: str
    reference_id: str
    external_reference_id: str
    amount: Money
    currency: str
    type: str
    status: str
    status_message: str
    payment_method: str
    metadata: _containers.ScalarMap[str, str]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., merchant_id: _Optional[int] = ..., provider_id: _Optional[str] = ..., invoice_number: _Optional[str] = ..., reference_id: _Optional[str] = ..., external_reference_id: _Optional[str] = ..., amount: _Optional[_Union[Money, _Mapping]] = ..., currency: _Optional[str] = ..., type: _Optional[str] = ..., status: _Optional[str] = ..., status_message: _Optional[str] = ..., payment_method: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PaymentCallback(_message.Message):
    __slots__ = ("reference_id", "external_reference", "status", "amount_confirmed", "timestamp", "signature", "raw_data")
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    RAW_DATA_FIELD_NUMBER: _ClassVar[int]
    reference_id: str
    external_reference: str
    status: str
    amount_confirmed: float
    timestamp: _timestamp_pb2.Timestamp
    signature: str
    raw_data: bytes
    def __init__(self, reference_id: _Optional[str] = ..., external_reference: _Optional[str] = ..., status: _Optional[str] = ..., amount_confirmed: _Optional[float] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., signature: _Optional[str] = ..., raw_data: _Optional[bytes] = ...) -> None: ...

class TransactionFilter(_message.Message):
    __slots__ = ("merchant_id", "provider_id", "status", "payment_method", "to", "invoice_number", "reference_id", "limit")
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    merchant_id: int
    provider_id: str
    status: str
    payment_method: str
    to: _timestamp_pb2.Timestamp
    invoice_number: str
    reference_id: str
    limit: int
    def __init__(self, merchant_id: _Optional[int] = ..., provider_id: _Optional[str] = ..., status: _Optional[str] = ..., payment_method: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., invoice_number: _Optional[str] = ..., reference_id: _Optional[str] = ..., limit: _Optional[int] = ..., **kwargs) -> None: ...
