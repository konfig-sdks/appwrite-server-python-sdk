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

from appwrite_server_python_sdk.type.messaging_create_topic_request_subscribe import MessagingCreateTopicRequestSubscribe

class RequiredMessagingCreateTopicRequest(TypedDict):
    # Topic ID. Choose a custom Topic ID or a new Topic ID.
    topicId: str

    # Topic Name.
    name: str

class OptionalMessagingCreateTopicRequest(TypedDict, total=False):
    subscribe: MessagingCreateTopicRequestSubscribe

class MessagingCreateTopicRequest(RequiredMessagingCreateTopicRequest, OptionalMessagingCreateTopicRequest):
    pass
