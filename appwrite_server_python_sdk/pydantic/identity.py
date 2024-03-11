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


class Identity(BaseModel):
    # Identity ID.
    $id_: str = Field(alias='$id')

    # Identity creation date in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Identity update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    # User ID.
    user_id: str = Field(alias='userId')

    # Identity Provider.
    provider: str = Field(alias='provider')

    # ID of the User in the Identity Provider.
    provider_uid: str = Field(alias='providerUid')

    # Email of the User in the Identity Provider.
    provider_email: str = Field(alias='providerEmail')

    # Identity Provider Access Token.
    provider_access_token: str = Field(alias='providerAccessToken')

    # The date of when the access token expires in ISO 8601 format.
    provider_access_token_expiry: str = Field(alias='providerAccessTokenExpiry')

    # Identity Provider Refresh Token.
    provider_refresh_token: str = Field(alias='providerRefreshToken')
    class Config:
        arbitrary_types_allowed = True
