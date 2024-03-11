# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from appwrite_server_python_sdk import schemas  # noqa: F401


class Variable(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Variable
    """


    class MetaOapg:
        required = {
            "resourceId",
            "$createdAt",
            "value",
            "key",
            "$id",
            "$updatedAt",
            "resourceType",
        }
        
        class properties:
            id = schemas.StrSchema
            created_at = schemas.StrSchema
            updated_at = schemas.StrSchema
            key = schemas.StrSchema
            value = schemas.StrSchema
            resourceType = schemas.StrSchema
            resourceId = schemas.StrSchema
            __annotations__ = {
                "$id": id,
                "$createdAt": created_at,
                "$updatedAt": updated_at,
                "key": key,
                "value": value,
                "resourceType": resourceType,
                "resourceId": resourceId,
            }
    
    resourceId: MetaOapg.properties.resourceId
    value: MetaOapg.properties.value
    key: MetaOapg.properties.key
    resourceType: MetaOapg.properties.resourceType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$createdAt"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$updatedAt"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceType"]) -> MetaOapg.properties.resourceType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceId"]) -> MetaOapg.properties.resourceId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["$id", "$createdAt", "$updatedAt", "key", "value", "resourceType", "resourceId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$createdAt"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$updatedAt"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceType"]) -> MetaOapg.properties.resourceType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceId"]) -> MetaOapg.properties.resourceId: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["$id", "$createdAt", "$updatedAt", "key", "value", "resourceType", "resourceId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        resourceId: typing.Union[MetaOapg.properties.resourceId, str, ],
        value: typing.Union[MetaOapg.properties.value, str, ],
        key: typing.Union[MetaOapg.properties.key, str, ],
        resourceType: typing.Union[MetaOapg.properties.resourceType, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Variable':
        return super().__new__(
            cls,
            *args,
            resourceId=resourceId,
            value=value,
            key=key,
            resourceType=resourceType,
            _configuration=_configuration,
            **kwargs,
        )