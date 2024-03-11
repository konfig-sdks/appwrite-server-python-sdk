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

from appwrite_server_python_sdk.pydantic.target import Target
from appwrite_server_python_sdk.pydantic.user_hash_options import UserHashOptions
from appwrite_server_python_sdk.pydantic.user_labels import UserLabels
from appwrite_server_python_sdk.pydantic.user_prefs import UserPrefs

class User(BaseModel):
    # User ID.
    $id_: str = Field(alias='$id')

    # User creation date in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # User update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    # User name.
    name: str = Field(alias='name')

    # User registration date in ISO 8601 format.
    registration: str = Field(alias='registration')

    # User status. Pass `true` for enabled and `false` for disabled.
    status: bool = Field(alias='status')

    labels: UserLabels = Field(alias='labels')

    # Password update time in ISO 8601 format.
    password_update: str = Field(alias='passwordUpdate')

    # User email address.
    email: str = Field(alias='email')

    # User phone number in E.164 format.
    phone: str = Field(alias='phone')

    # Email verification status.
    email_verification: bool = Field(alias='emailVerification')

    # Phone verification status.
    phone_verification: bool = Field(alias='phoneVerification')

    # Multi factor authentication status.
    mfa: bool = Field(alias='mfa')

    prefs: UserPrefs = Field(alias='prefs')

    # A user-owned message receiver. A single user may have multiple e.g. emails, phones, and a browser. Each target is registered with a single provider.
    targets: typing.List[Target] = Field(alias='targets')

    # Most recent access date in ISO 8601 format. This attribute is only updated again after 24 hours.
    accessed_at: str = Field(alias='accessedAt')

    # Hashed user password.
    password: typing.Optional[typing.Optional[str]] = Field(None, alias='password')

    # Password hashing algorithm.
    hash: typing.Optional[typing.Optional[str]] = Field(None, alias='hash')

    hash_options: typing.Optional[UserHashOptions] = Field(None, alias='hashOptions')
    class Config:
        arbitrary_types_allowed = True
