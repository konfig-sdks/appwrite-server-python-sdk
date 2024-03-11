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


class RequiredMessagingCreateSubscriberRequest(TypedDict):
    # Subscriber ID. Choose a custom Subscriber ID or a new Subscriber ID.
    subscriberId: str

    # Target ID. The target ID to link to the specified Topic ID.
    targetId: str

class OptionalMessagingCreateSubscriberRequest(TypedDict, total=False):
    pass

class MessagingCreateSubscriberRequest(RequiredMessagingCreateSubscriberRequest, OptionalMessagingCreateSubscriberRequest):
    pass
