from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChallengeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHALLENGE_TYPE_UNSPECIFIED: _ClassVar[ChallengeType]
    REGISTRATION: _ClassVar[ChallengeType]
    RESET_PIN: _ClassVar[ChallengeType]
    ADD_PAYMENT_METHOD: _ClassVar[ChallengeType]
CHALLENGE_TYPE_UNSPECIFIED: ChallengeType
REGISTRATION: ChallengeType
RESET_PIN: ChallengeType
ADD_PAYMENT_METHOD: ChallengeType

class User(_message.Message):
    __slots__ = ("id", "mobile", "first_name", "last_name", "create_time", "update_time", "is_verified", "is_admin", "is_super_user")
    ID_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    IS_SUPER_USER_FIELD_NUMBER: _ClassVar[int]
    id: int
    mobile: str
    first_name: str
    last_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    is_verified: bool
    is_admin: bool
    is_super_user: bool
    def __init__(self, id: _Optional[int] = ..., mobile: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_verified: bool = ..., is_admin: bool = ..., is_super_user: bool = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("user_id", "first_name", "last_name", "is_admin", "is_super_user")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    IS_SUPER_USER_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    first_name: str
    last_name: str
    is_admin: bool
    is_super_user: bool
    def __init__(self, user_id: _Optional[int] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., is_admin: bool = ..., is_super_user: bool = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("mobile", "first_name", "last_name", "pin", "verify_pin")
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    VERIFY_PIN_FIELD_NUMBER: _ClassVar[int]
    mobile: str
    first_name: str
    last_name: str
    pin: str
    verify_pin: str
    def __init__(self, mobile: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., pin: _Optional[str] = ..., verify_pin: _Optional[str] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class VerifyChallengeRequest(_message.Message):
    __slots__ = ("user_id", "challenge", "challenge_type")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    challenge: str
    challenge_type: ChallengeType
    def __init__(self, user_id: _Optional[int] = ..., challenge: _Optional[str] = ..., challenge_type: _Optional[_Union[ChallengeType, str]] = ...) -> None: ...

class VerifyChallengeResponse(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class ChallengeRequest(_message.Message):
    __slots__ = ("user_id", "challenge_type", "mobile")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    challenge_type: ChallengeType
    mobile: str
    def __init__(self, user_id: _Optional[int] = ..., challenge_type: _Optional[_Union[ChallengeType, str]] = ..., mobile: _Optional[str] = ...) -> None: ...

class ChallengeResponse(_message.Message):
    __slots__ = ("challenge",)
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    challenge: str
    def __init__(self, challenge: _Optional[str] = ...) -> None: ...

class GetUserByMobileRequest(_message.Message):
    __slots__ = ("mobile",)
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    mobile: str
    def __init__(self, mobile: _Optional[str] = ...) -> None: ...

class CreatePinRequest(_message.Message):
    __slots__ = ("user_id", "pin", "verify_pin")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    VERIFY_PIN_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    pin: str
    verify_pin: str
    def __init__(self, user_id: _Optional[int] = ..., pin: _Optional[str] = ..., verify_pin: _Optional[str] = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ("mobile", "pin")
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    mobile: str
    pin: str
    def __init__(self, mobile: _Optional[str] = ..., pin: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("access_token", "id_token", "refresh_token")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    id_token: str
    refresh_token: str
    def __init__(self, access_token: _Optional[str] = ..., id_token: _Optional[str] = ..., refresh_token: _Optional[str] = ...) -> None: ...

class ListUsersRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListUsersResponse(_message.Message):
    __slots__ = ("users", "next_page_token")
    USERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    next_page_token: str
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetNewAccessTokenRequest(_message.Message):
    __slots__ = ("refresh_token",)
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    def __init__(self, refresh_token: _Optional[str] = ...) -> None: ...

class GetNewAccessTokenResponse(_message.Message):
    __slots__ = ("access_token",)
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    def __init__(self, access_token: _Optional[str] = ...) -> None: ...
