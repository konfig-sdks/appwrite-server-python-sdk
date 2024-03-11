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


class Token(BaseModel):
    # Token ID.
    $id_: str = Field(alias='$id')

    # Token creation date in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # User ID.
    user_id: str = Field(alias='userId')

    # Token secret key. This will return an empty string unless the response is returned using an API key or as part of a webhook payload.
    secret: str = Field(alias='secret')

    # Token expiration date in ISO 8601 format.
    expire: str = Field(alias='expire')

    # Security phrase of a token. Empty if security phrase was not requested when creating a token. It includes randomly generated phrase which is also sent in the external resource such as email.
    phrase: str = Field(alias='phrase')
    class Config:
        arbitrary_types_allowed = True
