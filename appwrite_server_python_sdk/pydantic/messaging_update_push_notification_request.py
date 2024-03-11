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

from appwrite_server_python_sdk.pydantic.messaging_update_push_notification_request_targets import MessagingUpdatePushNotificationRequestTargets
from appwrite_server_python_sdk.pydantic.messaging_update_push_notification_request_topics import MessagingUpdatePushNotificationRequestTopics
from appwrite_server_python_sdk.pydantic.messaging_update_push_notification_request_users import MessagingUpdatePushNotificationRequestUsers

class MessagingUpdatePushNotificationRequest(BaseModel):
    # Title for push notification.
    title: typing.Optional[str] = Field(None, alias='title')

    topics: typing.Optional[MessagingUpdatePushNotificationRequestTopics] = Field(None, alias='topics')

    users: typing.Optional[MessagingUpdatePushNotificationRequestUsers] = Field(None, alias='users')

    targets: typing.Optional[MessagingUpdatePushNotificationRequestTargets] = Field(None, alias='targets')

    # Body for push notification.
    body: typing.Optional[str] = Field(None, alias='body')

    # Additional Data for push notification.
    data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='data')

    # Action for push notification.
    action: typing.Optional[str] = Field(None, alias='action')

    # Image for push notification. Must be a compound bucket ID to file ID of a jpeg, png, or bmp image in Appwrite Storage.
    image: typing.Optional[str] = Field(None, alias='image')

    # Icon for push notification. Available only for Android and Web platforms.
    icon: typing.Optional[str] = Field(None, alias='icon')

    # Sound for push notification. Available only for Android and iOS platforms.
    sound: typing.Optional[str] = Field(None, alias='sound')

    # Color for push notification. Available only for Android platforms.
    color: typing.Optional[str] = Field(None, alias='color')

    # Tag for push notification. Available only for Android platforms.
    tag: typing.Optional[str] = Field(None, alias='tag')

    # Badge for push notification. Available only for iOS platforms.
    badge: typing.Optional[int] = Field(None, alias='badge')

    # Is message a draft
    draft: typing.Optional[bool] = Field(None, alias='draft')

    # Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
    scheduled_at: typing.Optional[str] = Field(None, alias='scheduledAt')
    class Config:
        arbitrary_types_allowed = True
