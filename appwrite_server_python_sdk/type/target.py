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


RequiredTarget = TypedDict("RequiredTarget", {
    # Target ID.
    "$id": str,

    # Target creation time in ISO 8601 format.
    "$createdAt": str,

    # Target update date in ISO 8601 format.
    "$updatedAt": str,

    # Target Name.
    "name": str,

    # User ID.
    "userId": str,

    # The target provider type. Can be one of the following: `email`, `sms` or `push`.
    "providerType": str,

    # The target identifier.
    "identifier": str,
    })

OptionalTarget = TypedDict("OptionalTarget", {
    # Provider ID.
    "providerId": typing.Optional[str],
    }, total=False)

class Target(RequiredTarget, OptionalTarget):
    pass
