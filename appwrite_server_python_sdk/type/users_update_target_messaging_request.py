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


class RequiredUsersUpdateTargetMessagingRequest(TypedDict):
    pass

class OptionalUsersUpdateTargetMessagingRequest(TypedDict, total=False):
    # The target identifier (token, email, phone etc.)
    identifier: str

    # Provider ID. Message will be sent to this target from the specified provider ID. If no provider ID is set the first setup provider will be used.
    providerId: str

    # Target name. Max length: 128 chars. For example: My Awesome App Galaxy S23.
    name: str

class UsersUpdateTargetMessagingRequest(RequiredUsersUpdateTargetMessagingRequest, OptionalUsersUpdateTargetMessagingRequest):
    pass
