from kemy.invoice import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBillableEntityRequest(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _common_pb2.BillableEntity
    def __init__(self, entity: _Optional[_Union[_common_pb2.BillableEntity, _Mapping]] = ...) -> None: ...

class GetBillableEntityRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetBillableEntitiesForMerchantRequest(_message.Message):
    __slots__ = ("merchant_id",)
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    merchant_id: int
    def __init__(self, merchant_id: _Optional[int] = ...) -> None: ...

class GetBillableEntitiesForGroupRequest(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class UpdateBillableEntityRequest(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _common_pb2.BillableEntity
    def __init__(self, entity: _Optional[_Union[_common_pb2.BillableEntity, _Mapping]] = ...) -> None: ...

class DeleteBillableEntityRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class BillableEntityResponse(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _common_pb2.BillableEntity
    def __init__(self, entity: _Optional[_Union[_common_pb2.BillableEntity, _Mapping]] = ...) -> None: ...

class BillableEntitiesResponse(_message.Message):
    __slots__ = ("entities",)
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[_common_pb2.BillableEntity]
    def __init__(self, entities: _Optional[_Iterable[_Union[_common_pb2.BillableEntity, _Mapping]]] = ...) -> None: ...

class CreateGroupRequest(_message.Message):
    __slots__ = ("group",)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: _common_pb2.Group
    def __init__(self, group: _Optional[_Union[_common_pb2.Group, _Mapping]] = ...) -> None: ...

class GetGroupRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetGroupsForMerchantRequest(_message.Message):
    __slots__ = ("merchant_id",)
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    merchant_id: int
    def __init__(self, merchant_id: _Optional[int] = ...) -> None: ...

class UpdateGroupRequest(_message.Message):
    __slots__ = ("group",)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: _common_pb2.Group
    def __init__(self, group: _Optional[_Union[_common_pb2.Group, _Mapping]] = ...) -> None: ...

class DeleteGroupRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class AddBillableEntityToGroupRequest(_message.Message):
    __slots__ = ("group_id", "item")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    item: _common_pb2.BillableEntity
    def __init__(self, group_id: _Optional[int] = ..., item: _Optional[_Union[_common_pb2.BillableEntity, _Mapping]] = ...) -> None: ...

class RemoveBillableEntityFromGroupRequest(_message.Message):
    __slots__ = ("group_id", "item_id")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    item_id: int
    def __init__(self, group_id: _Optional[int] = ..., item_id: _Optional[int] = ...) -> None: ...

class GroupResponse(_message.Message):
    __slots__ = ("group",)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: _common_pb2.Group
    def __init__(self, group: _Optional[_Union[_common_pb2.Group, _Mapping]] = ...) -> None: ...

class GroupsResponse(_message.Message):
    __slots__ = ("groups",)
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[_common_pb2.Group]
    def __init__(self, groups: _Optional[_Iterable[_Union[_common_pb2.Group, _Mapping]]] = ...) -> None: ...

class CreateTemplateRequest(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _common_pb2.InvoiceTemplate
    def __init__(self, template: _Optional[_Union[_common_pb2.InvoiceTemplate, _Mapping]] = ...) -> None: ...

class GetTemplateRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetTemplatesForMerchantRequest(_message.Message):
    __slots__ = ("merchant_id",)
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    merchant_id: int
    def __init__(self, merchant_id: _Optional[int] = ...) -> None: ...

class UpdateTemplateRequest(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _common_pb2.InvoiceTemplate
    def __init__(self, template: _Optional[_Union[_common_pb2.InvoiceTemplate, _Mapping]] = ...) -> None: ...

class DeleteTemplateRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class CreateTemplateItemRequest(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _common_pb2.InvoiceTemplateLineItem
    def __init__(self, item: _Optional[_Union[_common_pb2.InvoiceTemplateLineItem, _Mapping]] = ...) -> None: ...

class RemoveTemplateItemRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class UpdateTemplateItemRequest(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _common_pb2.InvoiceTemplateLineItem
    def __init__(self, item: _Optional[_Union[_common_pb2.InvoiceTemplateLineItem, _Mapping]] = ...) -> None: ...

class GetTemplateItemsRequest(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: int
    def __init__(self, template_id: _Optional[int] = ...) -> None: ...

class TemplateResponse(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _common_pb2.InvoiceTemplate
    def __init__(self, template: _Optional[_Union[_common_pb2.InvoiceTemplate, _Mapping]] = ...) -> None: ...

class TemplatesResponse(_message.Message):
    __slots__ = ("templates",)
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[_common_pb2.InvoiceTemplate]
    def __init__(self, templates: _Optional[_Iterable[_Union[_common_pb2.InvoiceTemplate, _Mapping]]] = ...) -> None: ...

class TemplateItemResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _common_pb2.InvoiceTemplateLineItem
    def __init__(self, item: _Optional[_Union[_common_pb2.InvoiceTemplateLineItem, _Mapping]] = ...) -> None: ...

class TemplateItemsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_common_pb2.InvoiceTemplateLineItem]
    def __init__(self, items: _Optional[_Iterable[_Union[_common_pb2.InvoiceTemplateLineItem, _Mapping]]] = ...) -> None: ...

class GenerateInvoicesForGroupRequest(_message.Message):
    __slots__ = ("group_id", "template_id")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    template_id: int
    def __init__(self, group_id: _Optional[int] = ..., template_id: _Optional[int] = ...) -> None: ...

class GenerateInvoicesForGroupResponse(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class CancelInvoicesRequest(_message.Message):
    __slots__ = ("invoice_numbers",)
    INVOICE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    invoice_numbers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, invoice_numbers: _Optional[_Iterable[str]] = ...) -> None: ...

class ApplyTemplateToGroupRequest(_message.Message):
    __slots__ = ("template_id", "group_id", "due_date")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    template_id: int
    group_id: int
    due_date: _timestamp_pb2.Timestamp
    def __init__(self, template_id: _Optional[int] = ..., group_id: _Optional[int] = ..., due_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class FinalizeDraftInvoicesRequest(_message.Message):
    __slots__ = ("invoice_numbers",)
    INVOICE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    invoice_numbers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, invoice_numbers: _Optional[_Iterable[str]] = ...) -> None: ...

class FinalizeDraftInvoicesResponse(_message.Message):
    __slots__ = ("invoices",)
    INVOICES_FIELD_NUMBER: _ClassVar[int]
    invoices: _containers.RepeatedCompositeFieldContainer[_common_pb2.Invoice]
    def __init__(self, invoices: _Optional[_Iterable[_Union[_common_pb2.Invoice, _Mapping]]] = ...) -> None: ...

class ListAssignmentsByGroupRequest(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class ListAssignmentsByTemplateRequest(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: int
    def __init__(self, template_id: _Optional[int] = ...) -> None: ...

class ListAssignmentsResponse(_message.Message):
    __slots__ = ("assignments",)
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    assignments: _containers.RepeatedCompositeFieldContainer[_common_pb2.GroupTemplateAssignment]
    def __init__(self, assignments: _Optional[_Iterable[_Union[_common_pb2.GroupTemplateAssignment, _Mapping]]] = ...) -> None: ...
