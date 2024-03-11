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


class RequiredMessagingUpdateProviderRequest(TypedDict):
    pass

class OptionalMessagingUpdateProviderRequest(TypedDict, total=False):
    # Provider name.
    name: str

    # Set as enabled.
    enabled: bool

    # Sendgrid API key.
    apiKey: str

    # Sender Name.
    fromName: str

    # Sender email address.
    fromEmail: str

    # Name set in the Reply To field for the mail. Default value is Sender Name.
    replyToName: str

    # Email set in the Reply To field for the mail. Default value is Sender Email.
    replyToEmail: str

class MessagingUpdateProviderRequest(RequiredMessagingUpdateProviderRequest, OptionalMessagingUpdateProviderRequest):
    pass
