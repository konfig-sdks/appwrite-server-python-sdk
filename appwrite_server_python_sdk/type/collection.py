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

from appwrite_server_python_sdk.type.collection_attributes import CollectionAttributes
from appwrite_server_python_sdk.type.collectionpermissions import Collectionpermissions
from appwrite_server_python_sdk.type.index import Index

RequiredCollection = TypedDict("RequiredCollection", {
    # Collection ID.
    "$id": str,

    # Collection creation date in ISO 8601 format.
    "$createdAt": str,

    # Collection update date in ISO 8601 format.
    "$updatedAt": str,

    "$permissions": Collectionpermissions,

    # Database ID.
    "databaseId": str,

    # Collection name.
    "name": str,

    # Collection enabled. Can be 'enabled' or 'disabled'. When disabled, the collection is inaccessible to users, but remains accessible to Server SDKs using API keys.
    "enabled": bool,

    # Whether document-level permissions are enabled. [Learn more about permissions](https://appwrite.io/docs/permissions).
    "documentSecurity": bool,

    "attributes": CollectionAttributes,

    # Collection indexes.
    "indexes": typing.List[Index],
    })

OptionalCollection = TypedDict("OptionalCollection", {
    }, total=False)

class Collection(RequiredCollection, OptionalCollection):
    pass
