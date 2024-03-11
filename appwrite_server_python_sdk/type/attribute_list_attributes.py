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

from appwrite_server_python_sdk.type.attribute_boolean import AttributeBoolean
from appwrite_server_python_sdk.type.attribute_datetime import AttributeDatetime
from appwrite_server_python_sdk.type.attribute_email import AttributeEmail
from appwrite_server_python_sdk.type.attribute_enum import AttributeEnum
from appwrite_server_python_sdk.type.attribute_float import AttributeFloat
from appwrite_server_python_sdk.type.attribute_integer import AttributeInteger
from appwrite_server_python_sdk.type.attribute_ip import AttributeIp
from appwrite_server_python_sdk.type.attribute_relationship import AttributeRelationship
from appwrite_server_python_sdk.type.attribute_string import AttributeString
from appwrite_server_python_sdk.type.attribute_url import AttributeUrl

AttributeListAttributes = typing.List[typing.Union[typing.List[AttributeBoolean], typing.List[AttributeInteger], typing.List[AttributeFloat], typing.List[AttributeEmail], typing.List[AttributeEnum], typing.List[AttributeUrl], typing.List[AttributeIp], typing.List[AttributeDatetime], typing.List[AttributeRelationship], typing.List[AttributeString]]]
