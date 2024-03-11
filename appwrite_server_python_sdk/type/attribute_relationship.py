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


class RequiredAttributeRelationship(TypedDict):
    # Attribute Key.
    key: str

    # Attribute type.
    type: str

    # Attribute status. Possible values: `available`, `processing`, `deleting`, `stuck`, or `failed`
    status: str

    # Error message. Displays error generated on failure of creating or deleting an attribute.
    error: str

    # Is attribute required?
    required: bool

    # The ID of the related collection.
    relatedCollection: str

    # The type of the relationship.
    relationType: str

    # Is the relationship two-way?
    twoWay: bool

    # The key of the two-way relationship.
    twoWayKey: str

    # How deleting the parent document will propagate to child documents.
    onDelete: str

    # Whether this is the parent or child side of the relationship
    side: str

class OptionalAttributeRelationship(TypedDict, total=False):
    # Is attribute an array?
    array: typing.Optional[bool]

class AttributeRelationship(RequiredAttributeRelationship, OptionalAttributeRelationship):
    pass
