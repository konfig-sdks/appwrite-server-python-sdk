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

from appwrite_server_python_sdk.pydantic.membership_roles import MembershipRoles

class Membership(BaseModel):
    # Membership ID.
    $id_: str = Field(alias='$id')

    # Membership creation date in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Membership update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    # User ID.
    user_id: str = Field(alias='userId')

    # User name.
    user_name: str = Field(alias='userName')

    # User email address.
    user_email: str = Field(alias='userEmail')

    # Team ID.
    team_id: str = Field(alias='teamId')

    # Team name.
    team_name: str = Field(alias='teamName')

    # Date, the user has been invited to join the team in ISO 8601 format.
    invited: str = Field(alias='invited')

    # Date, the user has accepted the invitation to join the team in ISO 8601 format.
    joined: str = Field(alias='joined')

    # User confirmation status, true if the user has joined the team or false otherwise.
    confirm: bool = Field(alias='confirm')

    # Multi factor authentication status, true if the user has MFA enabled or false otherwise.
    mfa: bool = Field(alias='mfa')

    roles: MembershipRoles = Field(alias='roles')
    class Config:
        arbitrary_types_allowed = True
