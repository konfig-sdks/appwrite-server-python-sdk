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

from appwrite_server_python_sdk.pydantic.session_factors import SessionFactors

class Session(BaseModel):
    # Session ID.
    $id_: str = Field(alias='$id')

    # Session creation date in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # User ID.
    user_id: str = Field(alias='userId')

    # Session expiration date in ISO 8601 format.
    expire: str = Field(alias='expire')

    # Session Provider.
    provider: str = Field(alias='provider')

    # Session Provider User ID.
    provider_uid: str = Field(alias='providerUid')

    # Session Provider Access Token.
    provider_access_token: str = Field(alias='providerAccessToken')

    # The date of when the access token expires in ISO 8601 format.
    provider_access_token_expiry: str = Field(alias='providerAccessTokenExpiry')

    # Session Provider Refresh Token.
    provider_refresh_token: str = Field(alias='providerRefreshToken')

    # IP in use when the session was created.
    ip: str = Field(alias='ip')

    # Operating system code name. View list of [available options](https://github.com/appwrite/appwrite/blob/master/docs/lists/os.json).
    os_code: str = Field(alias='osCode')

    # Operating system name.
    os_name: str = Field(alias='osName')

    # Operating system version.
    os_version: str = Field(alias='osVersion')

    # Client type.
    client_type: str = Field(alias='clientType')

    # Client code name. View list of [available options](https://github.com/appwrite/appwrite/blob/master/docs/lists/clients.json).
    client_code: str = Field(alias='clientCode')

    # Client name.
    client_name: str = Field(alias='clientName')

    # Client version.
    client_version: str = Field(alias='clientVersion')

    # Client engine name.
    client_engine: str = Field(alias='clientEngine')

    # Client engine name.
    client_engine_version: str = Field(alias='clientEngineVersion')

    # Device name.
    device_name: str = Field(alias='deviceName')

    # Device brand name.
    device_brand: str = Field(alias='deviceBrand')

    # Device model name.
    device_model: str = Field(alias='deviceModel')

    # Country two-character ISO 3166-1 alpha code.
    country_code: str = Field(alias='countryCode')

    # Country name.
    country_name: str = Field(alias='countryName')

    # Returns true if this the current user session.
    current: bool = Field(alias='current')

    factors: SessionFactors = Field(alias='factors')

    # Secret used to authenticate the user. Only included if the request was made with an API key
    secret: str = Field(alias='secret')

    # Most recent date in ISO 8601 format when the session successfully passed MFA challenge.
    mfa_updated_at: str = Field(alias='mfaUpdatedAt')
    class Config:
        arbitrary_types_allowed = True
