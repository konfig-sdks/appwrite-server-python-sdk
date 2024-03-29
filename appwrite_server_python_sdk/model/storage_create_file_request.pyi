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


class StorageCreateFileRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "file",
            "fileId",
        }
        
        class properties:
            fileId = schemas.StrSchema
            file = schemas.StrSchema
        
            @staticmethod
            def permissions() -> typing.Type['StorageCreateFileRequestPermissions']:
                return StorageCreateFileRequestPermissions
            __annotations__ = {
                "fileId": fileId,
                "file": file,
                "permissions": permissions,
            }
    
    file: MetaOapg.properties.file
    fileId: MetaOapg.properties.fileId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileId"]) -> MetaOapg.properties.fileId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file"]) -> MetaOapg.properties.file: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> 'StorageCreateFileRequestPermissions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["fileId", "file", "permissions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileId"]) -> MetaOapg.properties.fileId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file"]) -> MetaOapg.properties.file: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> typing.Union['StorageCreateFileRequestPermissions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fileId", "file", "permissions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        file: typing.Union[MetaOapg.properties.file, str, ],
        fileId: typing.Union[MetaOapg.properties.fileId, str, ],
        permissions: typing.Union['StorageCreateFileRequestPermissions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StorageCreateFileRequest':
        return super().__new__(
            cls,
            *args,
            file=file,
            fileId=fileId,
            permissions=permissions,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_server_python_sdk.model.storage_create_file_request_permissions import StorageCreateFileRequestPermissions
