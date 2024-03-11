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


RequiredMessagingUpdateTwilioProviderRequest = TypedDict("RequiredMessagingUpdateTwilioProviderRequest", {
    })

OptionalMessagingUpdateTwilioProviderRequest = TypedDict("OptionalMessagingUpdateTwilioProviderRequest", {
    # Provider name.
    "name": str,

    # Set as enabled.
    "enabled": bool,

    # Twilio account secret ID.
    "accountSid": str,

    # Twilio authentication token.
    "authToken": str,

    # Sender number.
    "from": str,
    }, total=False)

class MessagingUpdateTwilioProviderRequest(RequiredMessagingUpdateTwilioProviderRequest, OptionalMessagingUpdateTwilioProviderRequest):
    pass
