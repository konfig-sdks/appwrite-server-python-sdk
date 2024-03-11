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

from appwrite_server_python_sdk.pydantic.messaging_create_push_notification_request_targets import MessagingCreatePushNotificationRequestTargets
from appwrite_server_python_sdk.pydantic.messaging_create_push_notification_request_topics import MessagingCreatePushNotificationRequestTopics
from appwrite_server_python_sdk.pydantic.messaging_create_push_notification_request_users import MessagingCreatePushNotificationRequestUsers

class MessagingCreatePushNotificationRequest(BaseModel):
    # Title for push notification.
    title: str = Field(alias='title')

    # Message ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
    message_id: str = Field(alias='messageId')

    # Body for push notification.
    body: str = Field(alias='body')

    topics: typing.Optional[MessagingCreatePushNotificationRequestTopics] = Field(None, alias='topics')

    users: typing.Optional[MessagingCreatePushNotificationRequestUsers] = Field(None, alias='users')

    targets: typing.Optional[MessagingCreatePushNotificationRequestTargets] = Field(None, alias='targets')

    # Additional Data for push notification.
    data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='data')

    # Action for push notification.
    action: typing.Optional[str] = Field(None, alias='action')

    # Image for push notification. Must be a compound bucket ID to file ID of a jpeg, png, or bmp image in Appwrite Storage.
    image: typing.Optional[str] = Field(None, alias='image')

    # Icon for push notification. Available only for Android and Web Platform.
    icon: typing.Optional[str] = Field(None, alias='icon')

    # Sound for push notification. Available only for Android and IOS Platform.
    sound: typing.Optional[str] = Field(None, alias='sound')

    # Color for push notification. Available only for Android Platform.
    color: typing.Optional[str] = Field(None, alias='color')

    # Tag for push notification. Available only for Android Platform.
    tag: typing.Optional[str] = Field(None, alias='tag')

    # Badge for push notification. Available only for IOS Platform.
    badge: typing.Optional[str] = Field(None, alias='badge')

    # Is message a draft
    draft: typing.Optional[bool] = Field(None, alias='draft')

    # Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
    scheduled_at: typing.Optional[str] = Field(None, alias='scheduledAt')
    class Config:
        arbitrary_types_allowed = True
