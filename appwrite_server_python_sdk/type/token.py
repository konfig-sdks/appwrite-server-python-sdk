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


RequiredToken = TypedDict("RequiredToken", {
    # Token ID.
    "$id": str,

    # Token creation date in ISO 8601 format.
    "$createdAt": str,

    # User ID.
    "userId": str,

    # Token secret key. This will return an empty string unless the response is returned using an API key or as part of a webhook payload.
    "secret": str,

    # Token expiration date in ISO 8601 format.
    "expire": str,

    # Security phrase of a token. Empty if security phrase was not requested when creating a token. It includes randomly generated phrase which is also sent in the external resource such as email.
    "phrase": str,
    })

OptionalToken = TypedDict("OptionalToken", {
    }, total=False)

class Token(RequiredToken, OptionalToken):
    pass
