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


class UsersUpdateTargetMessagingRequest(BaseModel):
    # The target identifier (token, email, phone etc.)
    identifier: typing.Optional[str] = Field(None, alias='identifier')

    # Provider ID. Message will be sent to this target from the specified provider ID. If no provider ID is set the first setup provider will be used.
    provider_id: typing.Optional[str] = Field(None, alias='providerId')

    # Target name. Max length: 128 chars. For example: My Awesome App Galaxy S23.
    name: typing.Optional[str] = Field(None, alias='name')
    class Config:
        arbitrary_types_allowed = True
