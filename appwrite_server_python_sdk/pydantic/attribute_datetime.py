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


class AttributeDatetime(BaseModel):
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

    # ISO 8601 format.
    format: str = Field(alias='format')

    # Is attribute an array?
    array: typing.Optional[typing.Optional[bool]] = Field(None, alias='array')

    # Default value for attribute when not provided. Only null is optional
    default: typing.Optional[typing.Optional[str]] = Field(None, alias='default')

    # Default value for attribute when not provided. Only null is optional
    example: typing.Optional[typing.Optional[str]] = Field(None, alias='example')

    # Default value for attribute when not provided. Only null is optional
    x-konfig-original-example_: typing.Optional[typing.Optional[str]] = Field(None, alias='x-konfig-original-example')
    class Config:
        arbitrary_types_allowed = True
