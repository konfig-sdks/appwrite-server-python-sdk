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


RequiredIdentity = TypedDict("RequiredIdentity", {
    # Identity ID.
    "$id": str,

    # Identity creation date in ISO 8601 format.
    "$createdAt": str,

    # Identity update date in ISO 8601 format.
    "$updatedAt": str,

    # User ID.
    "userId": str,

    # Identity Provider.
    "provider": str,

    # ID of the User in the Identity Provider.
    "providerUid": str,

    # Email of the User in the Identity Provider.
    "providerEmail": str,

    # Identity Provider Access Token.
    "providerAccessToken": str,

    # The date of when the access token expires in ISO 8601 format.
    "providerAccessTokenExpiry": str,

    # Identity Provider Refresh Token.
    "providerRefreshToken": str,
    })

OptionalIdentity = TypedDict("OptionalIdentity", {
    }, total=False)

class Identity(RequiredIdentity, OptionalIdentity):
    pass
