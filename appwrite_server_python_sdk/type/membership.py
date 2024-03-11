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

from appwrite_server_python_sdk.type.membership_roles import MembershipRoles

RequiredMembership = TypedDict("RequiredMembership", {
    # Membership ID.
    "$id": str,

    # Membership creation date in ISO 8601 format.
    "$createdAt": str,

    # Membership update date in ISO 8601 format.
    "$updatedAt": str,

    # User ID.
    "userId": str,

    # User name.
    "userName": str,

    # User email address.
    "userEmail": str,

    # Team ID.
    "teamId": str,

    # Team name.
    "teamName": str,

    # Date, the user has been invited to join the team in ISO 8601 format.
    "invited": str,

    # Date, the user has accepted the invitation to join the team in ISO 8601 format.
    "joined": str,

    # User confirmation status, true if the user has joined the team or false otherwise.
    "confirm": bool,

    # Multi factor authentication status, true if the user has MFA enabled or false otherwise.
    "mfa": bool,

    "roles": MembershipRoles,
    })

OptionalMembership = TypedDict("OptionalMembership", {
    }, total=False)

class Membership(RequiredMembership, OptionalMembership):
    pass
