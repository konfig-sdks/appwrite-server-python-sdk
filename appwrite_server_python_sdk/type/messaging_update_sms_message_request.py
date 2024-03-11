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

from appwrite_server_python_sdk.type.messaging_update_sms_message_request_targets import MessagingUpdateSmsMessageRequestTargets
from appwrite_server_python_sdk.type.messaging_update_sms_message_request_topics import MessagingUpdateSmsMessageRequestTopics
from appwrite_server_python_sdk.type.messaging_update_sms_message_request_users import MessagingUpdateSmsMessageRequestUsers

class RequiredMessagingUpdateSmsMessageRequest(TypedDict):
    pass

class OptionalMessagingUpdateSmsMessageRequest(TypedDict, total=False):
    topics: MessagingUpdateSmsMessageRequestTopics

    users: MessagingUpdateSmsMessageRequestUsers

    targets: MessagingUpdateSmsMessageRequestTargets

    # Email Content.
    content: str

    # Is message a draft
    draft: bool

    # Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
    scheduledAt: str

class MessagingUpdateSmsMessageRequest(RequiredMessagingUpdateSmsMessageRequest, OptionalMessagingUpdateSmsMessageRequest):
    pass
