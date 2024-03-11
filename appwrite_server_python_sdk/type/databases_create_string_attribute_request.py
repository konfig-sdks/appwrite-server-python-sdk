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


class RequiredDatabasesCreateStringAttributeRequest(TypedDict):
    # Attribute Key.
    key: str

    # Attribute size for text attributes, in number of characters.
    size: int

    # Is attribute required?
    required: bool

class OptionalDatabasesCreateStringAttributeRequest(TypedDict, total=False):
    # Default value for attribute when not provided. Cannot be set when attribute is required.
    default: str

    # Is attribute an array?
    array: bool

    # Toggle encryption for the attribute. Encryption enhances security by not storing any plain text values in the database. However, encrypted attributes cannot be queried.
    encrypt: bool

class DatabasesCreateStringAttributeRequest(RequiredDatabasesCreateStringAttributeRequest, OptionalDatabasesCreateStringAttributeRequest):
    pass
