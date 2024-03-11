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


class Target(BaseModel):
    # Target ID.
    $id_: str = Field(alias='$id')

    # Target creation time in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Target update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    # Target Name.
    name: str = Field(alias='name')

    # User ID.
    user_id: str = Field(alias='userId')

    # The target provider type. Can be one of the following: `email`, `sms` or `push`.
    provider_type: str = Field(alias='providerType')

    # The target identifier.
    identifier: str = Field(alias='identifier')

    # Provider ID.
    provider_id: typing.Optional[typing.Optional[str]] = Field(None, alias='providerId')
    class Config:
        arbitrary_types_allowed = True
