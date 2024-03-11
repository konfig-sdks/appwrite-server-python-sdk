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

from appwrite_server_python_sdk.type.storage_update_bucket_by_id_request_allowed_file_extensions import StorageUpdateBucketByIdRequestAllowedFileExtensions
from appwrite_server_python_sdk.type.storage_update_bucket_by_id_request_permissions import StorageUpdateBucketByIdRequestPermissions

class RequiredStorageUpdateBucketByIdRequest(TypedDict):
    # Bucket name
    name: str

class OptionalStorageUpdateBucketByIdRequest(TypedDict, total=False):
    permissions: StorageUpdateBucketByIdRequestPermissions

    # Enables configuring permissions for individual file. A user needs one of file or bucket level permissions to access a file. [Learn more about permissions](https://appwrite.io/docs/permissions).
    fileSecurity: bool

    # Is bucket enabled? When set to 'disabled', users cannot access the files in this bucket but Server SDKs with and API key can still access the bucket. No files are lost when this is toggled.
    enabled: bool

    # Maximum file size allowed in bytes. Maximum allowed value is 30MB.
    maximumFileSize: int

    allowedFileExtensions: StorageUpdateBucketByIdRequestAllowedFileExtensions

    # Compression algorithm choosen for compression. Can be one of none, [gzip](https://en.wikipedia.org/wiki/Gzip), or [zstd](https://en.wikipedia.org/wiki/Zstd), For file size above 20MB compression is skipped even if it's enabled
    compression: str

    # Is encryption enabled? For file size above 20MB encryption is skipped even if it's enabled
    encryption: bool

    # Is virus scanning enabled? For file size above 20MB AntiVirus scanning is skipped even if it's enabled
    antivirus: bool

class StorageUpdateBucketByIdRequest(RequiredStorageUpdateBucketByIdRequest, OptionalStorageUpdateBucketByIdRequest):
    pass
