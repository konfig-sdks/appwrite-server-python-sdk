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

from appwrite_server_python_sdk.pydantic.message_delivery_errors import MessageDeliveryErrors
from appwrite_server_python_sdk.pydantic.message_targets import MessageTargets
from appwrite_server_python_sdk.pydantic.message_topics import MessageTopics
from appwrite_server_python_sdk.pydantic.message_users import MessageUsers

class Message(BaseModel):
    # Message ID.
    $id_: str = Field(alias='$id')

    # Message creation time in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Message update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    # Message provider type.
    provider_type: str = Field(alias='providerType')

    topics: MessageTopics = Field(alias='topics')

    users: MessageUsers = Field(alias='users')

    targets: MessageTargets = Field(alias='targets')

    # Number of recipients the message was delivered to.
    delivered_total: int = Field(alias='deliveredTotal')

    # Data of the message.
    data: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='data')

    # Status of delivery.
    status: str = Field(alias='status')

    # The scheduled time for message.
    scheduled_at: typing.Optional[typing.Optional[str]] = Field(None, alias='scheduledAt')

    # The time when the message was delivered.
    delivered_at: typing.Optional[typing.Optional[str]] = Field(None, alias='deliveredAt')

    delivery_errors: typing.Optional[MessageDeliveryErrors] = Field(None, alias='deliveryErrors')
    class Config:
        arbitrary_types_allowed = True
