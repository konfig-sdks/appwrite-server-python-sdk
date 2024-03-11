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


RequiredAttributeInteger = TypedDict("RequiredAttributeInteger", {
    # Attribute Key.
    "key": str,

    # Attribute type.
    "type": str,

    # Attribute status. Possible values: `available`, `processing`, `deleting`, `stuck`, or `failed`
    "status": str,

    # Error message. Displays error generated on failure of creating or deleting an attribute.
    "error": str,

    # Is attribute required?
    "required": bool,
    })

OptionalAttributeInteger = TypedDict("OptionalAttributeInteger", {
    # Is attribute an array?
    "array": typing.Optional[bool],

    # Minimum value to enforce for new documents.
    "min": typing.Optional[int],

    # Maximum value to enforce for new documents.
    "max": typing.Optional[int],

    # Default value for attribute when not provided. Cannot be set when attribute is required.
    "default": typing.Optional[int],

    # Default value for attribute when not provided. Cannot be set when attribute is required.
    "example": typing.Optional[int],

    # Default value for attribute when not provided. Cannot be set when attribute is required.
    "x-konfig-original-example": typing.Optional[int],
    }, total=False)

class AttributeInteger(RequiredAttributeInteger, OptionalAttributeInteger):
    pass
