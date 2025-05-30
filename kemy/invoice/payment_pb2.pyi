from kemy.invoice import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentRequest(_message.Message):
    __slots__ = ("invoice_number", "merchant_id", "transaction_id", "provider", "account_no", "amount", "customer_name")
    INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NO_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    invoice_number: str
    merchant_id: int
    transaction_id: str
    provider: _common_pb2.Provider
    account_no: str
    amount: _common_pb2.Money
    customer_name: str
    def __init__(self, invoice_number: _Optional[str] = ..., merchant_id: _Optional[int] = ..., transaction_id: _Optional[str] = ..., provider: _Optional[_Union[_common_pb2.Provider, str]] = ..., account_no: _Optional[str] = ..., amount: _Optional[_Union[_common_pb2.Money, _Mapping]] = ..., customer_name: _Optional[str] = ...) -> None: ...

class PaymentResponse(_message.Message):
    __slots__ = ("invoice_number", "transaction_id", "status", "external_ref", "amount")
    INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REF_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    invoice_number: str
    transaction_id: str
    status: _common_pb2.PaymentStatus
    external_ref: str
    amount: _common_pb2.Money
    def __init__(self, invoice_number: _Optional[str] = ..., transaction_id: _Optional[str] = ..., status: _Optional[_Union[_common_pb2.PaymentStatus, str]] = ..., external_ref: _Optional[str] = ..., amount: _Optional[_Union[_common_pb2.Money, _Mapping]] = ...) -> None: ...
