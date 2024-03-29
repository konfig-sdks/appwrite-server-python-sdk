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


class DatabasesCreateIndexRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "attributes",
            "type",
            "key",
        }
        
        class properties:
            key = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def KEY(cls):
                    return cls("key")
                
                @schemas.classproperty
                def FULLTEXT(cls):
                    return cls("fulltext")
                
                @schemas.classproperty
                def UNIQUE(cls):
                    return cls("unique")
        
            @staticmethod
            def attributes() -> typing.Type['DatabasesCreateIndexRequestAttributes']:
                return DatabasesCreateIndexRequestAttributes
        
            @staticmethod
            def orders() -> typing.Type['DatabasesCreateIndexRequestOrders']:
                return DatabasesCreateIndexRequestOrders
            __annotations__ = {
                "key": key,
                "type": type,
                "attributes": attributes,
                "orders": orders,
            }
    
    attributes: 'DatabasesCreateIndexRequestAttributes'
    type: MetaOapg.properties.type
    key: MetaOapg.properties.key
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> 'DatabasesCreateIndexRequestAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orders"]) -> 'DatabasesCreateIndexRequestOrders': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["key", "type", "attributes", "orders", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> 'DatabasesCreateIndexRequestAttributes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orders"]) -> typing.Union['DatabasesCreateIndexRequestOrders', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["key", "type", "attributes", "orders", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        attributes: 'DatabasesCreateIndexRequestAttributes',
        type: typing.Union[MetaOapg.properties.type, str, ],
        key: typing.Union[MetaOapg.properties.key, str, ],
        orders: typing.Union['DatabasesCreateIndexRequestOrders', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DatabasesCreateIndexRequest':
        return super().__new__(
            cls,
            *args,
            attributes=attributes,
            type=type,
            key=key,
            orders=orders,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_server_python_sdk.model.databases_create_index_request_attributes import DatabasesCreateIndexRequestAttributes
from appwrite_server_python_sdk.model.databases_create_index_request_orders import DatabasesCreateIndexRequestOrders
