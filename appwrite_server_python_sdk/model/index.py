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


class Index(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Index
    """


    class MetaOapg:
        required = {
            "attributes",
            "error",
            "type",
            "key",
            "status",
        }
        
        class properties:
            key = schemas.StrSchema
            type = schemas.StrSchema
            status = schemas.StrSchema
            error = schemas.StrSchema
        
            @staticmethod
            def attributes() -> typing.Type['IndexAttributes']:
                return IndexAttributes
        
            @staticmethod
            def orders() -> typing.Type['IndexOrders']:
                return IndexOrders
            __annotations__ = {
                "key": key,
                "type": type,
                "status": status,
                "error": error,
                "attributes": attributes,
                "orders": orders,
            }
    
    attributes: 'IndexAttributes'
    error: MetaOapg.properties.error
    type: MetaOapg.properties.type
    key: MetaOapg.properties.key
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> 'IndexAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orders"]) -> 'IndexOrders': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["key", "type", "status", "error", "attributes", "orders", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> 'IndexAttributes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orders"]) -> typing.Union['IndexOrders', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["key", "type", "status", "error", "attributes", "orders", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        attributes: 'IndexAttributes',
        error: typing.Union[MetaOapg.properties.error, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        key: typing.Union[MetaOapg.properties.key, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        orders: typing.Union['IndexOrders', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Index':
        return super().__new__(
            cls,
            *args,
            attributes=attributes,
            error=error,
            type=type,
            key=key,
            status=status,
            orders=orders,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_server_python_sdk.model.index_attributes import IndexAttributes
from appwrite_server_python_sdk.model.index_orders import IndexOrders
