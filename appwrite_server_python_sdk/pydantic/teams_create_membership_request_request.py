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

from appwrite_server_python_sdk.pydantic.teams_create_membership_request_request_roles import TeamsCreateMembershipRequestRequestRoles

class TeamsCreateMembershipRequestRequest(BaseModel):
    roles: TeamsCreateMembershipRequestRequestRoles = Field(alias='roles')

    # Email of the new team member.
    email: typing.Optional[str] = Field(None, alias='email')

    # ID of the user to be added to a team.
    user_id: typing.Optional[str] = Field(None, alias='userId')

    # Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
    phone: typing.Optional[str] = Field(None, alias='phone')

    # URL to redirect the user back to your app from the invitation email.  Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
    url: typing.Optional[str] = Field(None, alias='url')

    # Name of the new team member. Max length: 128 chars.
    name: typing.Optional[str] = Field(None, alias='name')
    class Config:
        arbitrary_types_allowed = True
