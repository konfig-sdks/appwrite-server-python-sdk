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

from appwrite_server_python_sdk.pydantic.bucket_allowed_file_extensions import BucketAllowedFileExtensions
from appwrite_server_python_sdk.pydantic.bucketpermissions import Bucketpermissions

class Bucket(BaseModel):
    # Bucket ID.
    $id_: str = Field(alias='$id')

    # Bucket creation time in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Bucket update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    $permissions_: Bucketpermissions = Field(alias='$permissions')

    # Whether file-level security is enabled. [Learn more about permissions](https://appwrite.io/docs/permissions).
    file_security: bool = Field(alias='fileSecurity')

    # Bucket name.
    name: str = Field(alias='name')

    # Bucket enabled.
    enabled: bool = Field(alias='enabled')

    # Maximum file size supported.
    maximum_file_size: int = Field(alias='maximumFileSize')

    allowed_file_extensions: BucketAllowedFileExtensions = Field(alias='allowedFileExtensions')

    # Compression algorithm choosen for compression. Will be one of none, [gzip](https://en.wikipedia.org/wiki/Gzip), or [zstd](https://en.wikipedia.org/wiki/Zstd).
    compression: str = Field(alias='compression')

    # Bucket is encrypted.
    encryption: bool = Field(alias='encryption')

    # Virus scanning is enabled.
    antivirus: bool = Field(alias='antivirus')
    class Config:
        arbitrary_types_allowed = True
