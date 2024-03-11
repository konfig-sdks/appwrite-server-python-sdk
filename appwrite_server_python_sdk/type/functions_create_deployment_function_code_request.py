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


class RequiredFunctionsCreateDeploymentFunctionCodeRequest(TypedDict):
    # Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code directory, and the CLI will automatically package your code. Use a path that is within the current directory.
    code: str

    # Automatically activate the deployment when it is finished building.
    activate: bool

class OptionalFunctionsCreateDeploymentFunctionCodeRequest(TypedDict, total=False):
    # Entrypoint File.
    entrypoint: str

    # Build Commands.
    commands: str

class FunctionsCreateDeploymentFunctionCodeRequest(RequiredFunctionsCreateDeploymentFunctionCodeRequest, OptionalFunctionsCreateDeploymentFunctionCodeRequest):
    pass
