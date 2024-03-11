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
from pydantic import BaseModel, Field, RootModel


class AttributeRelationship(BaseModel):
    # Attribute Key.
    key: str = Field(alias='key')

    # Attribute type.
    type: str = Field(alias='type')

    # Attribute status. Possible values: `available`, `processing`, `deleting`, `stuck`, or `failed`
    status: str = Field(alias='status')

    # Error message. Displays error generated on failure of creating or deleting an attribute.
    error: str = Field(alias='error')

    # Is attribute required?
    required: bool = Field(alias='required')

    # The ID of the related collection.
    related_collection: str = Field(alias='relatedCollection')

    # The type of the relationship.
    relation_type: str = Field(alias='relationType')

    # Is the relationship two-way?
    two_way: bool = Field(alias='twoWay')

    # The key of the two-way relationship.
    two_way_key: str = Field(alias='twoWayKey')

    # How deleting the parent document will propagate to child documents.
    on_delete: str = Field(alias='onDelete')

    # Whether this is the parent or child side of the relationship
    side: str = Field(alias='side')

    # Is attribute an array?
    array: typing.Optional[typing.Optional[bool]] = Field(None, alias='array')
    class Config:
        arbitrary_types_allowed = True
