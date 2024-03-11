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


class UsersCreatePhpassUserRequest(BaseModel):
    # User ID. Choose a custom ID or pass the string `ID.unique()`to auto generate it. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
    user_id: str = Field(alias='userId')

    # User email.
    email: str = Field(alias='email')

    # User password hashed using PHPass.
    password: str = Field(alias='password')

    # User name. Max length: 128 chars.
    name: typing.Optional[str] = Field(None, alias='name')
    class Config:
        arbitrary_types_allowed = True
