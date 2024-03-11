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

from appwrite_server_python_sdk.pydantic.databases_create_collection_request_permissions import DatabasesCreateCollectionRequestPermissions

class DatabasesCreateCollectionRequest(BaseModel):
    # Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
    collection_id: str = Field(alias='collectionId')

    # Collection name. Max length: 128 chars.
    name: str = Field(alias='name')

    permissions: typing.Optional[DatabasesCreateCollectionRequestPermissions] = Field(None, alias='permissions')

    # Enables configuring permissions for individual documents. A user needs one of document or collection level permissions to access a document. [Learn more about permissions](https://appwrite.io/docs/permissions).
    document_security: typing.Optional[bool] = Field(None, alias='documentSecurity')

    # Is collection enabled? When set to 'disabled', users cannot access the collection but Server SDKs with and API key can still read and write to the collection. No data is lost when this is toggled.
    enabled: typing.Optional[bool] = Field(None, alias='enabled')
    class Config:
        arbitrary_types_allowed = True
