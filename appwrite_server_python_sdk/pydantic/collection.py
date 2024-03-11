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

from appwrite_server_python_sdk.pydantic.collection_attributes import CollectionAttributes
from appwrite_server_python_sdk.pydantic.collectionpermissions import Collectionpermissions
from appwrite_server_python_sdk.pydantic.index import Index

class Collection(BaseModel):
    # Collection ID.
    $id_: str = Field(alias='$id')

    # Collection creation date in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Collection update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    $permissions_: Collectionpermissions = Field(alias='$permissions')

    # Database ID.
    database_id: str = Field(alias='databaseId')

    # Collection name.
    name: str = Field(alias='name')

    # Collection enabled. Can be 'enabled' or 'disabled'. When disabled, the collection is inaccessible to users, but remains accessible to Server SDKs using API keys.
    enabled: bool = Field(alias='enabled')

    # Whether document-level permissions are enabled. [Learn more about permissions](https://appwrite.io/docs/permissions).
    document_security: bool = Field(alias='documentSecurity')

    attributes: CollectionAttributes = Field(alias='attributes')

    # Collection indexes.
    indexes: typing.List[Index] = Field(alias='indexes')
    class Config:
        arbitrary_types_allowed = True
