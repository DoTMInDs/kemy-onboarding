from google.protobuf import empty_pb2 as _empty_pb2
from v1.payment import common_pb2 as _common_pb2
from v1.invoice import common_pb2 as _common_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterProviderRequest(_message.Message):
    __slots__ = ("provider",)
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    provider: _common_pb2.PaymentProvider
    def __init__(self, provider: _Optional[_Union[_common_pb2.PaymentProvider, _Mapping]] = ...) -> None: ...

class GetProviderRequest(_message.Message):
    __slots__ = ("provider_id",)
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    def __init__(self, provider_id: _Optional[str] = ...) -> None: ...

class ListProvidersRequest(_message.Message):
    __slots__ = ("active_only",)
    ACTIVE_ONLY_FIELD_NUMBER: _ClassVar[int]
    active_only: bool
    def __init__(self, active_only: bool = ...) -> None: ...

class ListProvidersResponse(_message.Message):
    __slots__ = ("providers",)
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    providers: _containers.RepeatedCompositeFieldContainer[_common_pb2.PaymentProvider]
    def __init__(self, providers: _Optional[_Iterable[_Union[_common_pb2.PaymentProvider, _Mapping]]] = ...) -> None: ...

class UpdateProviderRequest(_message.Message):
    __slots__ = ("provider",)
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    provider: _common_pb2.PaymentProvider
    def __init__(self, provider: _Optional[_Union[_common_pb2.PaymentProvider, _Mapping]] = ...) -> None: ...

class UpdateProviderStatusRequest(_message.Message):
    __slots__ = ("provider_id", "active")
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    active: bool
    def __init__(self, provider_id: _Optional[str] = ..., active: bool = ...) -> None: ...

class SetMerchantActiveStatusRequest(_message.Message):
    __slots__ = ("merchant_id", "active")
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    merchant_id: int
    active: bool
    def __init__(self, merchant_id: _Optional[int] = ..., active: bool = ...) -> None: ...

class RemoveProviderAccountRequest(_message.Message):
    __slots__ = ("merchant_id", "provider_id")
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    merchant_id: int
    provider_id: str
    def __init__(self, merchant_id: _Optional[int] = ..., provider_id: _Optional[str] = ...) -> None: ...

class GetMerchantProviderAccountsRequest(_message.Message):
    __slots__ = ("merchant_id",)
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    merchant_id: int
    def __init__(self, merchant_id: _Optional[int] = ...) -> None: ...

class GetMerchantProviderAccountsResponse(_message.Message):
    __slots__ = ("accounts",)
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[_common_pb2.MerchantProviderAccount]
    def __init__(self, accounts: _Optional[_Iterable[_Union[_common_pb2.MerchantProviderAccount, _Mapping]]] = ...) -> None: ...

class GetMerchantAccountsRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class GetMerchantAccountsResponse(_message.Message):
    __slots__ = ("accounts", "next_page_token")
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[_common_pb2.MerchantAccount]
    next_page_token: str
    def __init__(self, accounts: _Optional[_Iterable[_Union[_common_pb2.MerchantAccount, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ProcessMobileMoneyPaymentRequest(_message.Message):
    __slots__ = ("provider", "amount", "phone_number", "merchant_id")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    provider: str
    amount: _common_pb2_1.Money
    phone_number: str
    merchant_id: int
    def __init__(self, provider: _Optional[str] = ..., amount: _Optional[_Union[_common_pb2_1.Money, _Mapping]] = ..., phone_number: _Optional[str] = ..., merchant_id: _Optional[int] = ...) -> None: ...

class GetInvoiceForPaymentRequest(_message.Message):
    __slots__ = ("invoice_number",)
    INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    invoice_number: str
    def __init__(self, invoice_number: _Optional[str] = ...) -> None: ...

class GetTransactionRequest(_message.Message):
    __slots__ = ("transaction_id",)
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    transaction_id: str
    def __init__(self, transaction_id: _Optional[str] = ...) -> None: ...

class GetTransactionByReferenceRequest(_message.Message):
    __slots__ = ("reference",)
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    reference: str
    def __init__(self, reference: _Optional[str] = ...) -> None: ...

class GetTransactionsByInvoiceRequest(_message.Message):
    __slots__ = ("invoice_id",)
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    def __init__(self, invoice_id: _Optional[str] = ...) -> None: ...

class GetTransactionsByInvoiceResponse(_message.Message):
    __slots__ = ("transactions",)
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[_common_pb2.Transaction]
    def __init__(self, transactions: _Optional[_Iterable[_Union[_common_pb2.Transaction, _Mapping]]] = ...) -> None: ...

class FindTransactionsResponse(_message.Message):
    __slots__ = ("transactions",)
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[_common_pb2.Transaction]
    def __init__(self, transactions: _Optional[_Iterable[_Union[_common_pb2.Transaction, _Mapping]]] = ...) -> None: ...
