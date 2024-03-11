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


RequiredFunctionsTriggerExecutionRequest = TypedDict("RequiredFunctionsTriggerExecutionRequest", {
    })

OptionalFunctionsTriggerExecutionRequest = TypedDict("OptionalFunctionsTriggerExecutionRequest", {
    # HTTP body of execution. Default value is empty string.
    "body": str,

    # Execute code in the background. Default value is false.
    "async": bool,

    # HTTP path of execution. Path can include query params. Default value is /
    "path": str,

    # HTTP method of execution. Default value is GET.
    "method": str,

    # HTTP headers of execution. Defaults to empty.
    "headers": typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
    }, total=False)

class FunctionsTriggerExecutionRequest(RequiredFunctionsTriggerExecutionRequest, OptionalFunctionsTriggerExecutionRequest):
    pass
