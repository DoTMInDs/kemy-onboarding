from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentMethodType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAYMENT_METHOD_TYPE_UNSPECIFIED: _ClassVar[PaymentMethodType]
    CREDIT_CARD: _ClassVar[PaymentMethodType]
    MOBILE_MONEY: _ClassVar[PaymentMethodType]
    CASH: _ClassVar[PaymentMethodType]
    ACH: _ClassVar[PaymentMethodType]

class Provider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_UNSPECIFIED: _ClassVar[Provider]
    MTN_MOMO: _ClassVar[Provider]
    TELECEL_CASH: _ClassVar[Provider]
    AIRTELTIGO_MONEY: _ClassVar[Provider]

class PaymentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAYMENT_STATUS_UNSPECIFIED: _ClassVar[PaymentStatus]
    PAYMENT_STARTED: _ClassVar[PaymentStatus]
    PAYMENT_PENDING: _ClassVar[PaymentStatus]
    PAYMENT_PAID: _ClassVar[PaymentStatus]
    PAYMENT_FAILED: _ClassVar[PaymentStatus]
    PAYMENT_CANCELLED: _ClassVar[PaymentStatus]

class EntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENTITY_TYPE_UNSPECIFIED: _ClassVar[EntityType]
    ENTITY_TYPE_STUDENT: _ClassVar[EntityType]
    ENTITY_TYPE_PROPERTY: _ClassVar[EntityType]
    ENTITY_TYPE_OTHER: _ClassVar[EntityType]

class InvoiceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVOICE_STATUS_UNSPECIFIED: _ClassVar[InvoiceStatus]
    DRAFT: _ClassVar[InvoiceStatus]
    OPEN: _ClassVar[InvoiceStatus]
    PAID: _ClassVar[InvoiceStatus]
    VOID: _ClassVar[InvoiceStatus]
    PARTIAL: _ClassVar[InvoiceStatus]

class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CATEGORY_UNSPECIFIED: _ClassVar[Category]
    SCHOOL: _ClassVar[Category]
    HOTEL: _ClassVar[Category]
    GENERAL: _ClassVar[Category]
PAYMENT_METHOD_TYPE_UNSPECIFIED: PaymentMethodType
CREDIT_CARD: PaymentMethodType
MOBILE_MONEY: PaymentMethodType
CASH: PaymentMethodType
ACH: PaymentMethodType
PROVIDER_UNSPECIFIED: Provider
MTN_MOMO: Provider
TELECEL_CASH: Provider
AIRTELTIGO_MONEY: Provider
PAYMENT_STATUS_UNSPECIFIED: PaymentStatus
PAYMENT_STARTED: PaymentStatus
PAYMENT_PENDING: PaymentStatus
PAYMENT_PAID: PaymentStatus
PAYMENT_FAILED: PaymentStatus
PAYMENT_CANCELLED: PaymentStatus
ENTITY_TYPE_UNSPECIFIED: EntityType
ENTITY_TYPE_STUDENT: EntityType
ENTITY_TYPE_PROPERTY: EntityType
ENTITY_TYPE_OTHER: EntityType
INVOICE_STATUS_UNSPECIFIED: InvoiceStatus
DRAFT: InvoiceStatus
OPEN: InvoiceStatus
PAID: InvoiceStatus
VOID: InvoiceStatus
PARTIAL: InvoiceStatus
CATEGORY_UNSPECIFIED: Category
SCHOOL: Category
HOTEL: Category
GENERAL: Category

class Money(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class PaymentMethod(_message.Message):
    __slots__ = ("id", "name", "payment_method_type", "provider", "account_no", "customer_id", "create_time", "update_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NO_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    payment_method_type: PaymentMethodType
    provider: Provider
    account_no: str
    customer_id: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., payment_method_type: _Optional[_Union[PaymentMethodType, str]] = ..., provider: _Optional[_Union[Provider, str]] = ..., account_no: _Optional[str] = ..., customer_id: _Optional[int] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class InvoiceLineItem(_message.Message):
    __slots__ = ("id", "qty", "unit_price", "amount", "create_time", "update_time", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    QTY_FIELD_NUMBER: _ClassVar[int]
    UNIT_PRICE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: int
    qty: int
    unit_price: Money
    amount: Money
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    def __init__(self, id: _Optional[int] = ..., qty: _Optional[int] = ..., unit_price: _Optional[_Union[Money, _Mapping]] = ..., amount: _Optional[_Union[Money, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class Invoice(_message.Message):
    __slots__ = ("number", "customer_id", "merchant_id", "reference_id", "description", "due_date", "total_amount", "amount_paid", "status", "amount_remaining", "is_paid", "tax_amount", "sub_total_amount", "currency", "create_time", "update_time", "line_items", "merchant_name", "merchant_address", "customer_name", "custom_fields", "finalize_time", "cancel_time", "billable_entity_id")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_PAID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_REMAINING_FIELD_NUMBER: _ClassVar[int]
    IS_PAID_FIELD_NUMBER: _ClassVar[int]
    TAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SUB_TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LINE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_NAME_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_TIME_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TIME_FIELD_NUMBER: _ClassVar[int]
    BILLABLE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    number: str
    customer_id: int
    merchant_id: int
    reference_id: str
    description: str
    due_date: _timestamp_pb2.Timestamp
    total_amount: Money
    amount_paid: Money
    status: InvoiceStatus
    amount_remaining: Money
    is_paid: bool
    tax_amount: Money
    sub_total_amount: Money
    currency: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    line_items: _containers.RepeatedCompositeFieldContainer[InvoiceLineItem]
    merchant_name: str
    merchant_address: str
    customer_name: str
    custom_fields: _containers.ScalarMap[str, str]
    finalize_time: _timestamp_pb2.Timestamp
    cancel_time: _timestamp_pb2.Timestamp
    billable_entity_id: int
    def __init__(self, number: _Optional[str] = ..., customer_id: _Optional[int] = ..., merchant_id: _Optional[int] = ..., reference_id: _Optional[str] = ..., description: _Optional[str] = ..., due_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., total_amount: _Optional[_Union[Money, _Mapping]] = ..., amount_paid: _Optional[_Union[Money, _Mapping]] = ..., status: _Optional[_Union[InvoiceStatus, str]] = ..., amount_remaining: _Optional[_Union[Money, _Mapping]] = ..., is_paid: bool = ..., tax_amount: _Optional[_Union[Money, _Mapping]] = ..., sub_total_amount: _Optional[_Union[Money, _Mapping]] = ..., currency: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., line_items: _Optional[_Iterable[_Union[InvoiceLineItem, _Mapping]]] = ..., merchant_name: _Optional[str] = ..., merchant_address: _Optional[str] = ..., customer_name: _Optional[str] = ..., custom_fields: _Optional[_Mapping[str, str]] = ..., finalize_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cancel_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., billable_entity_id: _Optional[int] = ...) -> None: ...

class Merchant(_message.Message):
    __slots__ = ("id", "name", "address", "contact_info", "create_time", "update_time", "category", "logo_url")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONTACT_INFO_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    address: str
    contact_info: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    category: Category
    logo_url: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., address: _Optional[str] = ..., contact_info: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., category: _Optional[_Union[Category, str]] = ..., logo_url: _Optional[str] = ...) -> None: ...

class MerchantUser(_message.Message):
    __slots__ = ("id", "user_id", "merchant_id", "create_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    user_id: int
    merchant_id: int
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., user_id: _Optional[int] = ..., merchant_id: _Optional[int] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Customer(_message.Message):
    __slots__ = ("id", "user_id", "national_id_no", "first_name", "last_name", "email", "mobile", "invoice_prefix", "next_invoice_sequence", "create_time", "update_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NATIONAL_ID_NO_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    INVOICE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    NEXT_INVOICE_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    user_id: int
    national_id_no: str
    first_name: str
    last_name: str
    email: str
    mobile: str
    invoice_prefix: str
    next_invoice_sequence: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., user_id: _Optional[int] = ..., national_id_no: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., mobile: _Optional[str] = ..., invoice_prefix: _Optional[str] = ..., next_invoice_sequence: _Optional[int] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class InvoicePayment(_message.Message):
    __slots__ = ("id", "invoice_id", "invoice_number", "payment_method_id", "transaction_id", "is_cash", "status", "amount", "start_time", "cancel_time", "fail_time", "paid_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_CASH_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TIME_FIELD_NUMBER: _ClassVar[int]
    FAIL_TIME_FIELD_NUMBER: _ClassVar[int]
    PAID_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    invoice_id: int
    invoice_number: str
    payment_method_id: int
    transaction_id: str
    is_cash: bool
    status: PaymentStatus
    amount: str
    start_time: _timestamp_pb2.Timestamp
    cancel_time: _timestamp_pb2.Timestamp
    fail_time: _timestamp_pb2.Timestamp
    paid_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., invoice_id: _Optional[int] = ..., invoice_number: _Optional[str] = ..., payment_method_id: _Optional[int] = ..., transaction_id: _Optional[str] = ..., is_cash: bool = ..., status: _Optional[_Union[PaymentStatus, str]] = ..., amount: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cancel_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., fail_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., paid_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BillableEntity(_message.Message):
    __slots__ = ("id", "merchant_id", "customer_id", "entity_type", "ref_id", "name", "attr1", "attr2", "attr3", "attr4", "attr5", "create_time", "update_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    REF_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ATTR1_FIELD_NUMBER: _ClassVar[int]
    ATTR2_FIELD_NUMBER: _ClassVar[int]
    ATTR3_FIELD_NUMBER: _ClassVar[int]
    ATTR4_FIELD_NUMBER: _ClassVar[int]
    ATTR5_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    merchant_id: int
    customer_id: int
    entity_type: EntityType
    ref_id: str
    name: str
    attr1: str
    attr2: str
    attr3: str
    attr4: str
    attr5: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., merchant_id: _Optional[int] = ..., customer_id: _Optional[int] = ..., entity_type: _Optional[_Union[EntityType, str]] = ..., ref_id: _Optional[str] = ..., name: _Optional[str] = ..., attr1: _Optional[str] = ..., attr2: _Optional[str] = ..., attr3: _Optional[str] = ..., attr4: _Optional[str] = ..., attr5: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Group(_message.Message):
    __slots__ = ("id", "merchant_id", "name", "description", "create_time", "update_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    merchant_id: int
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., merchant_id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class InvoiceTemplate(_message.Message):
    __slots__ = ("id", "merchant_id", "name", "description", "due_date", "is_active", "tax", "currency", "create_time", "update_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TAX_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    merchant_id: int
    name: str
    description: str
    due_date: _timestamp_pb2.Timestamp
    is_active: bool
    tax: Money
    currency: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., merchant_id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., due_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_active: bool = ..., tax: _Optional[_Union[Money, _Mapping]] = ..., currency: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class InvoiceTemplateLineItem(_message.Message):
    __slots__ = ("id", "template_id", "description", "quantity", "unit_price", "create_time", "update_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UNIT_PRICE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    template_id: int
    description: str
    quantity: int
    unit_price: Money
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., template_id: _Optional[int] = ..., description: _Optional[str] = ..., quantity: _Optional[int] = ..., unit_price: _Optional[_Union[Money, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GroupTemplateAssignment(_message.Message):
    __slots__ = ("id", "group_id", "template_id", "due_date", "create_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    group_id: int
    template_id: int
    due_date: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., group_id: _Optional[int] = ..., template_id: _Optional[int] = ..., due_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class InvoiceFilters(_message.Message):
    __slots__ = ("status", "paid", "create_time_after", "create_time_before", "due_date_after", "due_date_before", "min_amount", "max_amount")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PAID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_AFTER_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_BEFORE_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_AFTER_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_BEFORE_FIELD_NUMBER: _ClassVar[int]
    MIN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    status: InvoiceStatus
    paid: bool
    create_time_after: _timestamp_pb2.Timestamp
    create_time_before: _timestamp_pb2.Timestamp
    due_date_after: _timestamp_pb2.Timestamp
    due_date_before: _timestamp_pb2.Timestamp
    min_amount: Money
    max_amount: Money
    def __init__(self, status: _Optional[_Union[InvoiceStatus, str]] = ..., paid: bool = ..., create_time_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., create_time_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., due_date_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., due_date_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., min_amount: _Optional[_Union[Money, _Mapping]] = ..., max_amount: _Optional[_Union[Money, _Mapping]] = ...) -> None: ...
