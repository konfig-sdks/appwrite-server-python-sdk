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

from appwrite_server_python_sdk.type.target import Target
from appwrite_server_python_sdk.type.user_hash_options import UserHashOptions
from appwrite_server_python_sdk.type.user_labels import UserLabels
from appwrite_server_python_sdk.type.user_prefs import UserPrefs

RequiredUser = TypedDict("RequiredUser", {
    # User ID.
    "$id": str,

    # User creation date in ISO 8601 format.
    "$createdAt": str,

    # User update date in ISO 8601 format.
    "$updatedAt": str,

    # User name.
    "name": str,

    # User registration date in ISO 8601 format.
    "registration": str,

    # User status. Pass `true` for enabled and `false` for disabled.
    "status": bool,

    "labels": UserLabels,

    # Password update time in ISO 8601 format.
    "passwordUpdate": str,

    # User email address.
    "email": str,

    # User phone number in E.164 format.
    "phone": str,

    # Email verification status.
    "emailVerification": bool,

    # Phone verification status.
    "phoneVerification": bool,

    # Multi factor authentication status.
    "mfa": bool,

    "prefs": UserPrefs,

    # A user-owned message receiver. A single user may have multiple e.g. emails, phones, and a browser. Each target is registered with a single provider.
    "targets": typing.List[Target],

    # Most recent access date in ISO 8601 format. This attribute is only updated again after 24 hours.
    "accessedAt": str,
    })

OptionalUser = TypedDict("OptionalUser", {
    # Hashed user password.
    "password": typing.Optional[str],

    # Password hashing algorithm.
    "hash": typing.Optional[str],

    "hashOptions": UserHashOptions,
    }, total=False)

class User(RequiredUser, OptionalUser):
    pass
