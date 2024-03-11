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

from appwrite_server_python_sdk.pydantic.filepermissions import Filepermissions

class File(BaseModel):
    # File ID.
    $id_: str = Field(alias='$id')

    # Bucket ID.
    bucket_id: str = Field(alias='bucketId')

    # File creation date in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # File update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    $permissions_: Filepermissions = Field(alias='$permissions')

    # File name.
    name: str = Field(alias='name')

    # File MD5 signature.
    signature: str = Field(alias='signature')

    # File mime type.
    mime_type: str = Field(alias='mimeType')

    # File original size in bytes.
    size_original: int = Field(alias='sizeOriginal')

    # Total number of chunks available
    chunks_total: int = Field(alias='chunksTotal')

    # Total number of chunks uploaded
    chunks_uploaded: int = Field(alias='chunksUploaded')
    class Config:
        arbitrary_types_allowed = True
