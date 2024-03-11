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

from appwrite_server_python_sdk.type.executionpermissions import Executionpermissions
from appwrite_server_python_sdk.type.headers import Headers

RequiredExecution = TypedDict("RequiredExecution", {
    # Execution ID.
    "$id": str,

    # Execution creation date in ISO 8601 format.
    "$createdAt": str,

    # Execution upate date in ISO 8601 format.
    "$updatedAt": str,

    "$permissions": Executionpermissions,

    # Function ID.
    "functionId": str,

    # The trigger that caused the function to execute. Possible values can be: `http`, `schedule`, or `event`.
    "trigger": str,

    # The status of the function execution. Possible values can be: `waiting`, `processing`, `completed`, or `failed`.
    "status": str,

    # HTTP request method type.
    "requestMethod": str,

    # HTTP request path and query.
    "requestPath": str,

    # HTTP response headers as a key-value object. This will return only whitelisted headers. All headers are returned if execution is created as synchronous.
    "requestHeaders": typing.List[Headers],

    # HTTP response status code.
    "responseStatusCode": int,

    # HTTP response body. This will return empty unless execution is created as synchronous.
    "responseBody": str,

    # HTTP response headers as a key-value object. This will return only whitelisted headers. All headers are returned if execution is created as synchronous.
    "responseHeaders": typing.List[Headers],

    # Function logs. Includes the last 4,000 characters. This will return an empty string unless the response is returned using an API key or as part of a webhook payload.
    "logs": str,

    # Function errors. Includes the last 4,000 characters. This will return an empty string unless the response is returned using an API key or as part of a webhook payload.
    "errors": str,

    # Function execution duration in seconds.
    "duration": typing.Union[int, float],
    })

OptionalExecution = TypedDict("OptionalExecution", {
    }, total=False)

class Execution(RequiredExecution, OptionalExecution):
    pass
