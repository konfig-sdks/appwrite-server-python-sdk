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

from appwrite_server_python_sdk.type.messaging_create_push_notification_request_targets import MessagingCreatePushNotificationRequestTargets
from appwrite_server_python_sdk.type.messaging_create_push_notification_request_topics import MessagingCreatePushNotificationRequestTopics
from appwrite_server_python_sdk.type.messaging_create_push_notification_request_users import MessagingCreatePushNotificationRequestUsers

class RequiredMessagingCreatePushNotificationRequest(TypedDict):
    # Title for push notification.
    title: str

    # Message ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
    messageId: str

    # Body for push notification.
    body: str

class OptionalMessagingCreatePushNotificationRequest(TypedDict, total=False):
    topics: MessagingCreatePushNotificationRequestTopics

    users: MessagingCreatePushNotificationRequestUsers

    targets: MessagingCreatePushNotificationRequestTargets

    # Additional Data for push notification.
    data: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Action for push notification.
    action: str

    # Image for push notification. Must be a compound bucket ID to file ID of a jpeg, png, or bmp image in Appwrite Storage.
    image: str

    # Icon for push notification. Available only for Android and Web Platform.
    icon: str

    # Sound for push notification. Available only for Android and IOS Platform.
    sound: str

    # Color for push notification. Available only for Android Platform.
    color: str

    # Tag for push notification. Available only for Android Platform.
    tag: str

    # Badge for push notification. Available only for IOS Platform.
    badge: str

    # Is message a draft
    draft: bool

    # Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
    scheduledAt: str

class MessagingCreatePushNotificationRequest(RequiredMessagingCreatePushNotificationRequest, OptionalMessagingCreatePushNotificationRequest):
    pass
