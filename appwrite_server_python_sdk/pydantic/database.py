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


class Database(BaseModel):
    # Database ID.
    $id_: str = Field(alias='$id')

    # Database name.
    name: str = Field(alias='name')

    # Database creation date in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Database update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    # If database is enabled. Can be 'enabled' or 'disabled'. When disabled, the database is inaccessible to users, but remains accessible to Server SDKs using API keys.
    enabled: bool = Field(alias='enabled')
    class Config:
        arbitrary_types_allowed = True
