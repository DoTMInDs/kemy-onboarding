from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from v1.invoice import common_pb2 as _common_pb2
from v1.invoice import templating_pb2 as _templating_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetPaymentRequest(_message.Message):
    __slots__ = ("transaction_id",)
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    transaction_id: str
    def __init__(self, transaction_id: _Optional[str] = ...) -> None: ...

class ListPaymentsRequest(_message.Message):
    __slots__ = ("invoice_id", "page_size", "page_token")
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    invoice_id: int
    page_size: int
    page_token: str
    def __init__(self, invoice_id: _Optional[int] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListPaymentsByNumberRequest(_message.Message):
    __slots__ = ("invoice_number", "page_size", "page_token")
    INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    invoice_number: str
    page_size: int
    page_token: str
    def __init__(self, invoice_number: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class GetPaymentResponse(_message.Message):
    __slots__ = ("payment",)
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    payment: _common_pb2.InvoicePayment
    def __init__(self, payment: _Optional[_Union[_common_pb2.InvoicePayment, _Mapping]] = ...) -> None: ...

class ListPaymentsResponse(_message.Message):
    __slots__ = ("payments", "next_page_token")
    PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    payments: _containers.RepeatedCompositeFieldContainer[_common_pb2.InvoicePayment]
    next_page_token: str
    def __init__(self, payments: _Optional[_Iterable[_Union[_common_pb2.InvoicePayment, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetInvoiceRequest(_message.Message):
    __slots__ = ("number",)
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: str
    def __init__(self, number: _Optional[str] = ...) -> None: ...

class GetInvoiceByMobileRequest(_message.Message):
    __slots__ = ("invoice_number", "mobile")
    INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    invoice_number: str
    mobile: str
    def __init__(self, invoice_number: _Optional[str] = ..., mobile: _Optional[str] = ...) -> None: ...

class GetInvoiceResponse(_message.Message):
    __slots__ = ("invoice",)
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _common_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_common_pb2.Invoice, _Mapping]] = ...) -> None: ...

class GetInvoiceForUserRequest(_message.Message):
    __slots__ = ("number",)
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: str
    def __init__(self, number: _Optional[str] = ...) -> None: ...

class GetInvoiceForUserResponse(_message.Message):
    __slots__ = ("invoice",)
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _common_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_common_pb2.Invoice, _Mapping]] = ...) -> None: ...

class FinalizeInvoiceRequest(_message.Message):
    __slots__ = ("number",)
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: str
    def __init__(self, number: _Optional[str] = ...) -> None: ...

class FinalizeInvoiceResponse(_message.Message):
    __slots__ = ("invoice",)
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _common_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_common_pb2.Invoice, _Mapping]] = ...) -> None: ...

class CreateInvoiceRequest(_message.Message):
    __slots__ = ("finalize", "customer_mobile", "merchant_id", "reference_id", "description", "due_date", "tax_amount", "currency", "line_items", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FINALIZE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MOBILE_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    TAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    LINE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    finalize: bool
    customer_mobile: str
    merchant_id: int
    reference_id: str
    description: str
    due_date: _timestamp_pb2.Timestamp
    tax_amount: _common_pb2.Money
    currency: str
    line_items: _containers.RepeatedCompositeFieldContainer[_common_pb2.InvoiceLineItem]
    custom_fields: _containers.ScalarMap[str, str]
    def __init__(self, finalize: bool = ..., customer_mobile: _Optional[str] = ..., merchant_id: _Optional[int] = ..., reference_id: _Optional[str] = ..., description: _Optional[str] = ..., due_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tax_amount: _Optional[_Union[_common_pb2.Money, _Mapping]] = ..., currency: _Optional[str] = ..., line_items: _Optional[_Iterable[_Union[_common_pb2.InvoiceLineItem, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateInvoiceResponse(_message.Message):
    __slots__ = ("invoice",)
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _common_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_common_pb2.Invoice, _Mapping]] = ...) -> None: ...

class CancelInvoiceRequest(_message.Message):
    __slots__ = ("number", "reason")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    number: str
    reason: str
    def __init__(self, number: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class CancelInvoiceResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class UpdateInvoiceRequest(_message.Message):
    __slots__ = ("invoice",)
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _common_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_common_pb2.Invoice, _Mapping]] = ...) -> None: ...

class UpdateInvoiceResponse(_message.Message):
    __slots__ = ("invoice",)
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _common_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_common_pb2.Invoice, _Mapping]] = ...) -> None: ...

class DeleteInvoiceRequest(_message.Message):
    __slots__ = ("number",)
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: str
    def __init__(self, number: _Optional[str] = ...) -> None: ...

class DeleteInvoiceResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ListCustomerInvoicesRequest(_message.Message):
    __slots__ = ("customer_id", "status")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    customer_id: int
    status: _common_pb2.InvoiceStatus
    def __init__(self, customer_id: _Optional[int] = ..., status: _Optional[_Union[_common_pb2.InvoiceStatus, str]] = ...) -> None: ...

class ListCustomerInvoicesByCustomFieldRequest(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ListCustomerInvoicesByUserRequest(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.InvoiceStatus
    def __init__(self, status: _Optional[_Union[_common_pb2.InvoiceStatus, str]] = ...) -> None: ...

class ListInvoicesResponse(_message.Message):
    __slots__ = ("invoices",)
    INVOICES_FIELD_NUMBER: _ClassVar[int]
    invoices: _containers.RepeatedCompositeFieldContainer[_common_pb2.Invoice]
    def __init__(self, invoices: _Optional[_Iterable[_Union[_common_pb2.Invoice, _Mapping]]] = ...) -> None: ...

class ListBillableEntityInvoicesRequest(_message.Message):
    __slots__ = ("billable_entity_id", "page_size", "page_token", "status")
    BILLABLE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    billable_entity_id: int
    page_size: int
    page_token: str
    status: _common_pb2.InvoiceStatus
    def __init__(self, billable_entity_id: _Optional[int] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., status: _Optional[_Union[_common_pb2.InvoiceStatus, str]] = ...) -> None: ...

class ListBillableEntityInvoicesResponse(_message.Message):
    __slots__ = ("invoices", "next_page_token")
    INVOICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    invoices: _containers.RepeatedCompositeFieldContainer[_common_pb2.Invoice]
    next_page_token: str
    def __init__(self, invoices: _Optional[_Iterable[_Union[_common_pb2.Invoice, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListMerchantRecentInvoicesRequest(_message.Message):
    __slots__ = ("merchant_id", "status", "limit")
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    merchant_id: int
    status: _common_pb2.InvoiceStatus
    limit: int
    def __init__(self, merchant_id: _Optional[int] = ..., status: _Optional[_Union[_common_pb2.InvoiceStatus, str]] = ..., limit: _Optional[int] = ...) -> None: ...

class ListMerchantInvoicesRequest(_message.Message):
    __slots__ = ("merchant_id", "filters", "page_size", "page_token")
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    merchant_id: int
    filters: _common_pb2.InvoiceFilters
    page_size: int
    page_token: str
    def __init__(self, merchant_id: _Optional[int] = ..., filters: _Optional[_Union[_common_pb2.InvoiceFilters, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListMerchantInvoicesResponse(_message.Message):
    __slots__ = ("invoices", "next_page_token")
    INVOICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    invoices: _containers.RepeatedCompositeFieldContainer[_common_pb2.Invoice]
    next_page_token: str
    def __init__(self, invoices: _Optional[_Iterable[_Union[_common_pb2.Invoice, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetPaymentMethodRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetPaymentMethodResponse(_message.Message):
    __slots__ = ("payment_method",)
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: _common_pb2.PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[_common_pb2.PaymentMethod, _Mapping]] = ...) -> None: ...

class CreatePaymentMethodRequest(_message.Message):
    __slots__ = ("payment_method",)
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: _common_pb2.PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[_common_pb2.PaymentMethod, _Mapping]] = ...) -> None: ...

class CreatePaymentMethodResponse(_message.Message):
    __slots__ = ("payment_method",)
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: _common_pb2.PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[_common_pb2.PaymentMethod, _Mapping]] = ...) -> None: ...

class UpdatePaymentMethodRequest(_message.Message):
    __slots__ = ("payment_method",)
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: _common_pb2.PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[_common_pb2.PaymentMethod, _Mapping]] = ...) -> None: ...

class UpdatePaymentMethodResponse(_message.Message):
    __slots__ = ("payment_method",)
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: _common_pb2.PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[_common_pb2.PaymentMethod, _Mapping]] = ...) -> None: ...

class DeletePaymentMethodRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeletePaymentMethodResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ListPaymentMethodsRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class ListPaymentMethodsResponse(_message.Message):
    __slots__ = ("payment_methods",)
    PAYMENT_METHODS_FIELD_NUMBER: _ClassVar[int]
    payment_methods: _containers.RepeatedCompositeFieldContainer[_common_pb2.PaymentMethod]
    def __init__(self, payment_methods: _Optional[_Iterable[_Union[_common_pb2.PaymentMethod, _Mapping]]] = ...) -> None: ...

class GetMerchantRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetMerchantResponse(_message.Message):
    __slots__ = ("merchant",)
    MERCHANT_FIELD_NUMBER: _ClassVar[int]
    merchant: _common_pb2.Merchant
    def __init__(self, merchant: _Optional[_Union[_common_pb2.Merchant, _Mapping]] = ...) -> None: ...

class CreateMerchantRequest(_message.Message):
    __slots__ = ("merchant",)
    MERCHANT_FIELD_NUMBER: _ClassVar[int]
    merchant: _common_pb2.Merchant
    def __init__(self, merchant: _Optional[_Union[_common_pb2.Merchant, _Mapping]] = ...) -> None: ...

class CreateMerchantResponse(_message.Message):
    __slots__ = ("merchant",)
    MERCHANT_FIELD_NUMBER: _ClassVar[int]
    merchant: _common_pb2.Merchant
    def __init__(self, merchant: _Optional[_Union[_common_pb2.Merchant, _Mapping]] = ...) -> None: ...

class UpdateMerchantRequest(_message.Message):
    __slots__ = ("merchant",)
    MERCHANT_FIELD_NUMBER: _ClassVar[int]
    merchant: _common_pb2.Merchant
    def __init__(self, merchant: _Optional[_Union[_common_pb2.Merchant, _Mapping]] = ...) -> None: ...

class UpdateMerchantResponse(_message.Message):
    __slots__ = ("merchant",)
    MERCHANT_FIELD_NUMBER: _ClassVar[int]
    merchant: _common_pb2.Merchant
    def __init__(self, merchant: _Optional[_Union[_common_pb2.Merchant, _Mapping]] = ...) -> None: ...

class DeleteMerchantRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeleteMerchantResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class GetMerchantUserRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetMerchantUserResponse(_message.Message):
    __slots__ = ("merchant_user",)
    MERCHANT_USER_FIELD_NUMBER: _ClassVar[int]
    merchant_user: _common_pb2.MerchantUser
    def __init__(self, merchant_user: _Optional[_Union[_common_pb2.MerchantUser, _Mapping]] = ...) -> None: ...

class ListMerchantUsersRequest(_message.Message):
    __slots__ = ("merchant_id",)
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    merchant_id: int
    def __init__(self, merchant_id: _Optional[int] = ...) -> None: ...

class ListMerchantUsersResponse(_message.Message):
    __slots__ = ("merchant_users",)
    MERCHANT_USERS_FIELD_NUMBER: _ClassVar[int]
    merchant_users: _containers.RepeatedCompositeFieldContainer[_common_pb2.MerchantUser]
    def __init__(self, merchant_users: _Optional[_Iterable[_Union[_common_pb2.MerchantUser, _Mapping]]] = ...) -> None: ...

class CreateMerchantUserRequest(_message.Message):
    __slots__ = ("merchant_user",)
    MERCHANT_USER_FIELD_NUMBER: _ClassVar[int]
    merchant_user: _common_pb2.MerchantUser
    def __init__(self, merchant_user: _Optional[_Union[_common_pb2.MerchantUser, _Mapping]] = ...) -> None: ...

class CreateMerchantUserResponse(_message.Message):
    __slots__ = ("merchant_user",)
    MERCHANT_USER_FIELD_NUMBER: _ClassVar[int]
    merchant_user: _common_pb2.MerchantUser
    def __init__(self, merchant_user: _Optional[_Union[_common_pb2.MerchantUser, _Mapping]] = ...) -> None: ...

class DeleteMerchantUserRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeleteMerchantUserResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class GetCustomerRequest(_message.Message):
    __slots__ = ("customer_id", "customer_mobile", "merchant_id")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MOBILE_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: int
    customer_mobile: str
    merchant_id: int
    def __init__(self, customer_id: _Optional[int] = ..., customer_mobile: _Optional[str] = ..., merchant_id: _Optional[int] = ...) -> None: ...

class GetCustomerResponse(_message.Message):
    __slots__ = ("customer",)
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    customer: _common_pb2.Customer
    def __init__(self, customer: _Optional[_Union[_common_pb2.Customer, _Mapping]] = ...) -> None: ...

class RegisterUserForCustomerRequest(_message.Message):
    __slots__ = ("mobile",)
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    mobile: str
    def __init__(self, mobile: _Optional[str] = ...) -> None: ...

class RegisterUserForCustomerResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class CreateCustomerRequest(_message.Message):
    __slots__ = ("merchant_id", "user_id", "national_id_no", "first_name", "last_name", "email", "mobile")
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NATIONAL_ID_NO_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    merchant_id: int
    user_id: int
    national_id_no: str
    first_name: str
    last_name: str
    email: str
    mobile: str
    def __init__(self, merchant_id: _Optional[int] = ..., user_id: _Optional[int] = ..., national_id_no: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., mobile: _Optional[str] = ...) -> None: ...

class CreateCustomerResponse(_message.Message):
    __slots__ = ("customer",)
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    customer: _common_pb2.Customer
    def __init__(self, customer: _Optional[_Union[_common_pb2.Customer, _Mapping]] = ...) -> None: ...

class UpdateCustomerRequest(_message.Message):
    __slots__ = ("merchant_id", "national_id_no", "first_name", "last_name", "email", "mobile")
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    NATIONAL_ID_NO_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    merchant_id: int
    national_id_no: str
    first_name: str
    last_name: str
    email: str
    mobile: str
    def __init__(self, merchant_id: _Optional[int] = ..., national_id_no: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., mobile: _Optional[str] = ...) -> None: ...

class UpdateCustomerResponse(_message.Message):
    __slots__ = ("customer",)
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    customer: _common_pb2.Customer
    def __init__(self, customer: _Optional[_Union[_common_pb2.Customer, _Mapping]] = ...) -> None: ...

class DeleteCustomerRequest(_message.Message):
    __slots__ = ("id", "merchant_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    merchant_id: int
    def __init__(self, id: _Optional[str] = ..., merchant_id: _Optional[int] = ...) -> None: ...

class DeleteCustomerResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class PayInvoiceRequest(_message.Message):
    __slots__ = ("payment_method_id", "invoice_number", "amount", "transaction_id")
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    payment_method_id: int
    invoice_number: str
    amount: _common_pb2.Money
    transaction_id: str
    def __init__(self, payment_method_id: _Optional[int] = ..., invoice_number: _Optional[str] = ..., amount: _Optional[_Union[_common_pb2.Money, _Mapping]] = ..., transaction_id: _Optional[str] = ...) -> None: ...

class PayInvoiceResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class InvoiceEventRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class InvoiceEventResponse(_message.Message):
    __slots__ = ("event_type", "invoice_number", "message")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    invoice_number: str
    message: str
    def __init__(self, event_type: _Optional[str] = ..., invoice_number: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class RecordCashPaymentRequest(_message.Message):
    __slots__ = ("invoice_number", "transaction_id", "amount", "paid_time")
    INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PAID_TIME_FIELD_NUMBER: _ClassVar[int]
    invoice_number: str
    transaction_id: str
    amount: _common_pb2.Money
    paid_time: _timestamp_pb2.Timestamp
    def __init__(self, invoice_number: _Optional[str] = ..., transaction_id: _Optional[str] = ..., amount: _Optional[_Union[_common_pb2.Money, _Mapping]] = ..., paid_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RecordCashPaymentResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class ListMerchantCustomersRequest(_message.Message):
    __slots__ = ("merchant_id", "page_size", "page_token")
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    merchant_id: int
    page_size: int
    page_token: str
    def __init__(self, merchant_id: _Optional[int] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListMerchantCustomersResponse(_message.Message):
    __slots__ = ("customers", "next_page_token")
    CUSTOMERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    customers: _containers.RepeatedCompositeFieldContainer[_common_pb2.Customer]
    next_page_token: str
    def __init__(self, customers: _Optional[_Iterable[_Union[_common_pb2.Customer, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListMerchantsResponse(_message.Message):
    __slots__ = ("merchants",)
    MERCHANTS_FIELD_NUMBER: _ClassVar[int]
    merchants: _containers.RepeatedCompositeFieldContainer[_common_pb2.Merchant]
    def __init__(self, merchants: _Optional[_Iterable[_Union[_common_pb2.Merchant, _Mapping]]] = ...) -> None: ...

class GetCustomerOverdueInvoicesForUserRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class GetCustomerOverdueInvoicesForUserResponse(_message.Message):
    __slots__ = ("overdue_invoice_count", "invoices")
    OVERDUE_INVOICE_COUNT_FIELD_NUMBER: _ClassVar[int]
    INVOICES_FIELD_NUMBER: _ClassVar[int]
    overdue_invoice_count: int
    invoices: _containers.RepeatedCompositeFieldContainer[_common_pb2.Invoice]
    def __init__(self, overdue_invoice_count: _Optional[int] = ..., invoices: _Optional[_Iterable[_Union[_common_pb2.Invoice, _Mapping]]] = ...) -> None: ...
