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


class UsersCreateScryptUserRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "password",
            "passwordCpu",
            "passwordParallel",
            "passwordSalt",
            "userId",
            "email",
            "passwordLength",
            "passwordMemory",
        }
        
        class properties:
            userId = schemas.StrSchema
            email = schemas.StrSchema
            password = schemas.StrSchema
            passwordSalt = schemas.StrSchema
            passwordCpu = schemas.IntSchema
            passwordMemory = schemas.IntSchema
            passwordParallel = schemas.IntSchema
            passwordLength = schemas.IntSchema
            name = schemas.StrSchema
            __annotations__ = {
                "userId": userId,
                "email": email,
                "password": password,
                "passwordSalt": passwordSalt,
                "passwordCpu": passwordCpu,
                "passwordMemory": passwordMemory,
                "passwordParallel": passwordParallel,
                "passwordLength": passwordLength,
                "name": name,
            }
    
    password: MetaOapg.properties.password
    passwordCpu: MetaOapg.properties.passwordCpu
    passwordParallel: MetaOapg.properties.passwordParallel
    passwordSalt: MetaOapg.properties.passwordSalt
    userId: MetaOapg.properties.userId
    email: MetaOapg.properties.email
    passwordLength: MetaOapg.properties.passwordLength
    passwordMemory: MetaOapg.properties.passwordMemory
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["passwordSalt"]) -> MetaOapg.properties.passwordSalt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["passwordCpu"]) -> MetaOapg.properties.passwordCpu: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["passwordMemory"]) -> MetaOapg.properties.passwordMemory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["passwordParallel"]) -> MetaOapg.properties.passwordParallel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["passwordLength"]) -> MetaOapg.properties.passwordLength: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["userId", "email", "password", "passwordSalt", "passwordCpu", "passwordMemory", "passwordParallel", "passwordLength", "name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["passwordSalt"]) -> MetaOapg.properties.passwordSalt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["passwordCpu"]) -> MetaOapg.properties.passwordCpu: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["passwordMemory"]) -> MetaOapg.properties.passwordMemory: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["passwordParallel"]) -> MetaOapg.properties.passwordParallel: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["passwordLength"]) -> MetaOapg.properties.passwordLength: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["userId", "email", "password", "passwordSalt", "passwordCpu", "passwordMemory", "passwordParallel", "passwordLength", "name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        password: typing.Union[MetaOapg.properties.password, str, ],
        passwordCpu: typing.Union[MetaOapg.properties.passwordCpu, decimal.Decimal, int, ],
        passwordParallel: typing.Union[MetaOapg.properties.passwordParallel, decimal.Decimal, int, ],
        passwordSalt: typing.Union[MetaOapg.properties.passwordSalt, str, ],
        userId: typing.Union[MetaOapg.properties.userId, str, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        passwordLength: typing.Union[MetaOapg.properties.passwordLength, decimal.Decimal, int, ],
        passwordMemory: typing.Union[MetaOapg.properties.passwordMemory, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsersCreateScryptUserRequest':
        return super().__new__(
            cls,
            *args,
            password=password,
            passwordCpu=passwordCpu,
            passwordParallel=passwordParallel,
            passwordSalt=passwordSalt,
            userId=userId,
            email=email,
            passwordLength=passwordLength,
            passwordMemory=passwordMemory,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )
