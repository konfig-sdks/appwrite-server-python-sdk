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

from appwrite_server_python_sdk.pydantic.topic_subscribe import TopicSubscribe

class Topic(BaseModel):
    # Topic ID.
    $id_: str = Field(alias='$id')

    # Topic creation time in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Topic update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    # The name of the topic.
    name: str = Field(alias='name')

    # Total count of email subscribers subscribed to the topic.
    email_total: int = Field(alias='emailTotal')

    # Total count of SMS subscribers subscribed to the topic.
    sms_total: int = Field(alias='smsTotal')

    # Total count of push subscribers subscribed to the topic.
    push_total: int = Field(alias='pushTotal')

    subscribe: TopicSubscribe = Field(alias='subscribe')
    class Config:
        arbitrary_types_allowed = True
