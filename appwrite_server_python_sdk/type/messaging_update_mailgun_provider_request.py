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


class RequiredMessagingUpdateMailgunProviderRequest(TypedDict):
    pass

class OptionalMessagingUpdateMailgunProviderRequest(TypedDict, total=False):
    # Provider name.
    name: str

    # Mailgun API Key.
    apiKey: str

    # Mailgun Domain.
    domain: str

    # Set as EU region.
    isEuRegion: bool

    # Set as enabled.
    enabled: bool

    # Sender Name.
    fromName: str

    # Sender email address.
    fromEmail: str

    # Name set in the reply to field for the mail. Default value is sender name.
    replyToName: str

    # Email set in the reply to field for the mail. Default value is sender email.
    replyToEmail: str

class MessagingUpdateMailgunProviderRequest(RequiredMessagingUpdateMailgunProviderRequest, OptionalMessagingUpdateMailgunProviderRequest):
    pass
