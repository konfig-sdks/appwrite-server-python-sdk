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


class RequiredLog(TypedDict):
    # Event name.
    event: str

    # User ID.
    userId: str

    # User Email.
    userEmail: str

    # User Name.
    userName: str

    # API mode when event triggered.
    mode: str

    # IP session in use when the session was created.
    ip: str

    # Log creation date in ISO 8601 format.
    time: str

    # Operating system code name. View list of [available options](https://github.com/appwrite/appwrite/blob/master/docs/lists/os.json).
    osCode: str

    # Operating system name.
    osName: str

    # Operating system version.
    osVersion: str

    # Client type.
    clientType: str

    # Client code name. View list of [available options](https://github.com/appwrite/appwrite/blob/master/docs/lists/clients.json).
    clientCode: str

    # Client name.
    clientName: str

    # Client version.
    clientVersion: str

    # Client engine name.
    clientEngine: str

    # Client engine name.
    clientEngineVersion: str

    # Device name.
    deviceName: str

    # Device brand name.
    deviceBrand: str

    # Device model name.
    deviceModel: str

    # Country two-character ISO 3166-1 alpha code.
    countryCode: str

    # Country name.
    countryName: str

class OptionalLog(TypedDict, total=False):
    pass

class Log(RequiredLog, OptionalLog):
    pass
