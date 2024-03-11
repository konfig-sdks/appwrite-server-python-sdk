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


RequiredVariable = TypedDict("RequiredVariable", {
    # Variable ID.
    "$id": str,

    # Variable creation date in ISO 8601 format.
    "$createdAt": str,

    # Variable creation date in ISO 8601 format.
    "$updatedAt": str,

    # Variable key.
    "key": str,

    # Variable value.
    "value": str,

    # Service to which the variable belongs. Possible values are \"project\", \"function\"
    "resourceType": str,

    # ID of resource to which the variable belongs. If resourceType is \"project\", it is empty. If resourceType is \"function\", it is ID of the function.
    "resourceId": str,
    })

OptionalVariable = TypedDict("OptionalVariable", {
    }, total=False)

class Variable(RequiredVariable, OptionalVariable):
    pass
