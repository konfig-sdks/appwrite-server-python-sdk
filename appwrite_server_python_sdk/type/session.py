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

from appwrite_server_python_sdk.type.session_factors import SessionFactors

RequiredSession = TypedDict("RequiredSession", {
    # Session ID.
    "$id": str,

    # Session creation date in ISO 8601 format.
    "$createdAt": str,

    # User ID.
    "userId": str,

    # Session expiration date in ISO 8601 format.
    "expire": str,

    # Session Provider.
    "provider": str,

    # Session Provider User ID.
    "providerUid": str,

    # Session Provider Access Token.
    "providerAccessToken": str,

    # The date of when the access token expires in ISO 8601 format.
    "providerAccessTokenExpiry": str,

    # Session Provider Refresh Token.
    "providerRefreshToken": str,

    # IP in use when the session was created.
    "ip": str,

    # Operating system code name. View list of [available options](https://github.com/appwrite/appwrite/blob/master/docs/lists/os.json).
    "osCode": str,

    # Operating system name.
    "osName": str,

    # Operating system version.
    "osVersion": str,

    # Client type.
    "clientType": str,

    # Client code name. View list of [available options](https://github.com/appwrite/appwrite/blob/master/docs/lists/clients.json).
    "clientCode": str,

    # Client name.
    "clientName": str,

    # Client version.
    "clientVersion": str,

    # Client engine name.
    "clientEngine": str,

    # Client engine name.
    "clientEngineVersion": str,

    # Device name.
    "deviceName": str,

    # Device brand name.
    "deviceBrand": str,

    # Device model name.
    "deviceModel": str,

    # Country two-character ISO 3166-1 alpha code.
    "countryCode": str,

    # Country name.
    "countryName": str,

    # Returns true if this the current user session.
    "current": bool,

    "factors": SessionFactors,

    # Secret used to authenticate the user. Only included if the request was made with an API key
    "secret": str,

    # Most recent date in ISO 8601 format when the session successfully passed MFA challenge.
    "mfaUpdatedAt": str,
    })

OptionalSession = TypedDict("OptionalSession", {
    }, total=False)

class Session(RequiredSession, OptionalSession):
    pass
