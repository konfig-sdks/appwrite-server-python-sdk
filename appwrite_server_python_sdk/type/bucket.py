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

from appwrite_server_python_sdk.type.bucket_allowed_file_extensions import BucketAllowedFileExtensions
from appwrite_server_python_sdk.type.bucketpermissions import Bucketpermissions

RequiredBucket = TypedDict("RequiredBucket", {
    # Bucket ID.
    "$id": str,

    # Bucket creation time in ISO 8601 format.
    "$createdAt": str,

    # Bucket update date in ISO 8601 format.
    "$updatedAt": str,

    "$permissions": Bucketpermissions,

    # Whether file-level security is enabled. [Learn more about permissions](https://appwrite.io/docs/permissions).
    "fileSecurity": bool,

    # Bucket name.
    "name": str,

    # Bucket enabled.
    "enabled": bool,

    # Maximum file size supported.
    "maximumFileSize": int,

    "allowedFileExtensions": BucketAllowedFileExtensions,

    # Compression algorithm choosen for compression. Will be one of none, [gzip](https://en.wikipedia.org/wiki/Gzip), or [zstd](https://en.wikipedia.org/wiki/Zstd).
    "compression": str,

    # Bucket is encrypted.
    "encryption": bool,

    # Virus scanning is enabled.
    "antivirus": bool,
    })

OptionalBucket = TypedDict("OptionalBucket", {
    }, total=False)

class Bucket(RequiredBucket, OptionalBucket):
    pass
