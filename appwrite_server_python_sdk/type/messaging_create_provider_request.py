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


class RequiredMessagingCreateProviderRequest(TypedDict):
    # Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
    providerId: str

    # Provider name.
    name: str

class OptionalMessagingCreateProviderRequest(TypedDict, total=False):
    # Mailgun API Key.
    apiKey: str

    # Mailgun Domain.
    domain: str

    # Set as EU region.
    isEuRegion: bool

    # Sender Name.
    fromName: str

    # Sender email address.
    fromEmail: str

    # Name set in the reply to field for the mail. Default value is sender name. Reply to name must have reply to email as well.
    replyToName: str

    # Email set in the reply to field for the mail. Default value is sender email. Reply to email must have reply to name as well.
    replyToEmail: str

    # Set as enabled.
    enabled: bool

class MessagingCreateProviderRequest(RequiredMessagingCreateProviderRequest, OptionalMessagingCreateProviderRequest):
    pass
