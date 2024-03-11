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


RequiredProvider = TypedDict("RequiredProvider", {
    # Provider ID.
    "$id": str,

    # Provider creation time in ISO 8601 format.
    "$createdAt": str,

    # Provider update date in ISO 8601 format.
    "$updatedAt": str,

    # The name for the provider instance.
    "name": str,

    # The name of the provider service.
    "provider": str,

    # Is provider enabled?
    "enabled": bool,

    # Type of provider.
    "type": str,

    # Provider credentials.
    "credentials": typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
    })

OptionalProvider = TypedDict("OptionalProvider", {
    # Provider options.
    "options": typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]],
    }, total=False)

class Provider(RequiredProvider, OptionalProvider):
    pass
