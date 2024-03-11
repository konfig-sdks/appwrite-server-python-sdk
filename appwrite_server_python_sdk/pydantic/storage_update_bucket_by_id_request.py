# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from appwrite_server_python_sdk.pydantic.storage_update_bucket_by_id_request_allowed_file_extensions import StorageUpdateBucketByIdRequestAllowedFileExtensions
from appwrite_server_python_sdk.pydantic.storage_update_bucket_by_id_request_permissions import StorageUpdateBucketByIdRequestPermissions

class StorageUpdateBucketByIdRequest(BaseModel):
    # Bucket name
    name: str = Field(alias='name')

    permissions: typing.Optional[StorageUpdateBucketByIdRequestPermissions] = Field(None, alias='permissions')

    # Enables configuring permissions for individual file. A user needs one of file or bucket level permissions to access a file. [Learn more about permissions](https://appwrite.io/docs/permissions).
    file_security: typing.Optional[bool] = Field(None, alias='fileSecurity')

    # Is bucket enabled? When set to 'disabled', users cannot access the files in this bucket but Server SDKs with and API key can still access the bucket. No files are lost when this is toggled.
    enabled: typing.Optional[bool] = Field(None, alias='enabled')

    # Maximum file size allowed in bytes. Maximum allowed value is 30MB.
    maximum_file_size: typing.Optional[int] = Field(None, alias='maximumFileSize')

    allowed_file_extensions: typing.Optional[StorageUpdateBucketByIdRequestAllowedFileExtensions] = Field(None, alias='allowedFileExtensions')

    # Compression algorithm choosen for compression. Can be one of none, [gzip](https://en.wikipedia.org/wiki/Gzip), or [zstd](https://en.wikipedia.org/wiki/Zstd), For file size above 20MB compression is skipped even if it's enabled
    compression: typing.Optional[Literal["none", "gzip", "zstd"]] = Field(None, alias='compression')

    # Is encryption enabled? For file size above 20MB encryption is skipped even if it's enabled
    encryption: typing.Optional[bool] = Field(None, alias='encryption')

    # Is virus scanning enabled? For file size above 20MB AntiVirus scanning is skipped even if it's enabled
    antivirus: typing.Optional[bool] = Field(None, alias='antivirus')
    class Config:
        arbitrary_types_allowed = True
