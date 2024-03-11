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


class Provider(BaseModel):
    # Provider ID.
    $id_: str = Field(alias='$id')

    # Provider creation time in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Provider update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    # The name for the provider instance.
    name: str = Field(alias='name')

    # The name of the provider service.
    provider: str = Field(alias='provider')

    # Is provider enabled?
    enabled: bool = Field(alias='enabled')

    # Type of provider.
    type: str = Field(alias='type')

    # Provider credentials.
    credentials: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='credentials')

    # Provider options.
    options: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='options')
    class Config:
        arbitrary_types_allowed = True
