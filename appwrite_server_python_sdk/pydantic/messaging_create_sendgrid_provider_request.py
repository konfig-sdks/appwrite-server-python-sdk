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


class MessagingCreateSendgridProviderRequest(BaseModel):
    # Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
    provider_id: str = Field(alias='providerId')

    # Provider name.
    name: str = Field(alias='name')

    # Sendgrid API key.
    api_key: typing.Optional[str] = Field(None, alias='apiKey')

    # Sender Name.
    from_name: typing.Optional[str] = Field(None, alias='fromName')

    # Sender email address.
    from_email: typing.Optional[str] = Field(None, alias='fromEmail')

    # Name set in the reply to field for the mail. Default value is sender name.
    reply_to_name: typing.Optional[str] = Field(None, alias='replyToName')

    # Email set in the reply to field for the mail. Default value is sender email.
    reply_to_email: typing.Optional[str] = Field(None, alias='replyToEmail')

    # Set as enabled.
    enabled: typing.Optional[bool] = Field(None, alias='enabled')
    class Config:
        arbitrary_types_allowed = True
