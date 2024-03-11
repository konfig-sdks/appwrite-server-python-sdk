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

from appwrite_server_python_sdk.type.message_delivery_errors import MessageDeliveryErrors
from appwrite_server_python_sdk.type.message_targets import MessageTargets
from appwrite_server_python_sdk.type.message_topics import MessageTopics
from appwrite_server_python_sdk.type.message_users import MessageUsers

RequiredMessage = TypedDict("RequiredMessage", {
    # Message ID.
    "$id": str,

    # Message creation time in ISO 8601 format.
    "$createdAt": str,

    # Message update date in ISO 8601 format.
    "$updatedAt": str,

    # Message provider type.
    "providerType": str,

    "topics": MessageTopics,

    "users": MessageUsers,

    "targets": MessageTargets,

    # Number of recipients the message was delivered to.
    "deliveredTotal": int,

    # Data of the message.
    "data": typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],

    # Status of delivery.
    "status": str,
    })

OptionalMessage = TypedDict("OptionalMessage", {
    # The scheduled time for message.
    "scheduledAt": typing.Optional[str],

    # The time when the message was delivered.
    "deliveredAt": typing.Optional[str],

    "deliveryErrors": MessageDeliveryErrors,
    }, total=False)

class Message(RequiredMessage, OptionalMessage):
    pass
