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


class MessagingUpdateMailgunProviderRequest(BaseModel):
    # Provider name.
    name: typing.Optional[str] = Field(None, alias='name')

    # Mailgun API Key.
    api_key: typing.Optional[str] = Field(None, alias='apiKey')

    # Mailgun Domain.
    domain: typing.Optional[str] = Field(None, alias='domain')

    # Set as EU region.
    is_eu_region: typing.Optional[bool] = Field(None, alias='isEuRegion')

    # Set as enabled.
    enabled: typing.Optional[bool] = Field(None, alias='enabled')

    # Sender Name.
    from_name: typing.Optional[str] = Field(None, alias='fromName')

    # Sender email address.
    from_email: typing.Optional[str] = Field(None, alias='fromEmail')

    # Name set in the reply to field for the mail. Default value is sender name.
    reply_to_name: typing.Optional[str] = Field(None, alias='replyToName')

    # Email set in the reply to field for the mail. Default value is sender email.
    reply_to_email: typing.Optional[str] = Field(None, alias='replyToEmail')
    class Config:
        arbitrary_types_allowed = True
