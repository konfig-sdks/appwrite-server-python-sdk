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

from appwrite_server_python_sdk.type.storage_create_file_request_permissions import StorageCreateFileRequestPermissions

class RequiredStorageCreateFileRequest(TypedDict):
    # File ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
    fileId: str

    # Binary file. Appwrite SDKs provide helpers to handle file input. [Learn about file input](https://appwrite.io/docs/storage#file-input).
    file: str

class OptionalStorageCreateFileRequest(TypedDict, total=False):
    permissions: StorageCreateFileRequestPermissions

class StorageCreateFileRequest(RequiredStorageCreateFileRequest, OptionalStorageCreateFileRequest):
    pass
