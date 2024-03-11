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

from appwrite_server_python_sdk.pydantic.executionpermissions import Executionpermissions
from appwrite_server_python_sdk.pydantic.headers import Headers

class Execution(BaseModel):
    # Execution ID.
    $id_: str = Field(alias='$id')

    # Execution creation date in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Execution upate date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    $permissions_: Executionpermissions = Field(alias='$permissions')

    # Function ID.
    function_id: str = Field(alias='functionId')

    # The trigger that caused the function to execute. Possible values can be: `http`, `schedule`, or `event`.
    trigger: str = Field(alias='trigger')

    # The status of the function execution. Possible values can be: `waiting`, `processing`, `completed`, or `failed`.
    status: str = Field(alias='status')

    # HTTP request method type.
    request_method: str = Field(alias='requestMethod')

    # HTTP request path and query.
    request_path: str = Field(alias='requestPath')

    # HTTP response headers as a key-value object. This will return only whitelisted headers. All headers are returned if execution is created as synchronous.
    request_headers: typing.List[Headers] = Field(alias='requestHeaders')

    # HTTP response status code.
    response_status_code: int = Field(alias='responseStatusCode')

    # HTTP response body. This will return empty unless execution is created as synchronous.
    response_body: str = Field(alias='responseBody')

    # HTTP response headers as a key-value object. This will return only whitelisted headers. All headers are returned if execution is created as synchronous.
    response_headers: typing.List[Headers] = Field(alias='responseHeaders')

    # Function logs. Includes the last 4,000 characters. This will return an empty string unless the response is returned using an API key or as part of a webhook payload.
    logs: str = Field(alias='logs')

    # Function errors. Includes the last 4,000 characters. This will return an empty string unless the response is returned using an API key or as part of a webhook payload.
    errors: str = Field(alias='errors')

    # Function execution duration in seconds.
    duration: typing.Union[int, float] = Field(alias='duration')
    class Config:
        arbitrary_types_allowed = True
