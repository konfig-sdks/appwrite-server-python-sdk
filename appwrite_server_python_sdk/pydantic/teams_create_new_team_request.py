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

from appwrite_server_python_sdk.pydantic.teams_create_new_team_request_roles import TeamsCreateNewTeamRequestRoles

class TeamsCreateNewTeamRequest(BaseModel):
    # Team ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
    team_id: str = Field(alias='teamId')

    # Team name. Max length: 128 chars.
    name: str = Field(alias='name')

    roles: typing.Optional[TeamsCreateNewTeamRequestRoles] = Field(None, alias='roles')
    class Config:
        arbitrary_types_allowed = True
