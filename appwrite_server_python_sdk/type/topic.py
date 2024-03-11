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

from appwrite_server_python_sdk.type.topic_subscribe import TopicSubscribe

RequiredTopic = TypedDict("RequiredTopic", {
    # Topic ID.
    "$id": str,

    # Topic creation time in ISO 8601 format.
    "$createdAt": str,

    # Topic update date in ISO 8601 format.
    "$updatedAt": str,

    # The name of the topic.
    "name": str,

    # Total count of email subscribers subscribed to the topic.
    "emailTotal": int,

    # Total count of SMS subscribers subscribed to the topic.
    "smsTotal": int,

    # Total count of push subscribers subscribed to the topic.
    "pushTotal": int,

    "subscribe": TopicSubscribe,
    })

OptionalTopic = TypedDict("OptionalTopic", {
    }, total=False)

class Topic(RequiredTopic, OptionalTopic):
    pass
