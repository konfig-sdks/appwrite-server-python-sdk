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

from appwrite_server_python_sdk.type.functions_create_new_function_request_events import FunctionsCreateNewFunctionRequestEvents
from appwrite_server_python_sdk.type.functions_create_new_function_request_execute import FunctionsCreateNewFunctionRequestExecute

class RequiredFunctionsCreateNewFunctionRequest(TypedDict):
    # Function ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
    functionId: str

    # Function name. Max length: 128 chars.
    name: str

    # Execution runtime.
    runtime: str

class OptionalFunctionsCreateNewFunctionRequest(TypedDict, total=False):
    execute: FunctionsCreateNewFunctionRequestExecute

    events: FunctionsCreateNewFunctionRequestEvents

    # Schedule CRON syntax.
    schedule: str

    # Function maximum execution time in seconds.
    timeout: int

    # Is function enabled? When set to 'disabled', users cannot access the function but Server SDKs with and API key can still access the function. No data is lost when this is toggled.
    enabled: bool

    # Whether executions will be logged. When set to false, executions will not be logged, but will reduce resource used by your Appwrite project.
    logging: bool

    # Entrypoint File. This path is relative to the \"providerRootDirectory\".
    entrypoint: str

    # Build Commands.
    commands: str

    # Appwrite Installation ID for VCS (Version Control System) deployment.
    installationId: str

    # Repository ID of the repo linked to the function.
    providerRepositoryId: str

    # Production branch for the repo linked to the function.
    providerBranch: str

    # Is the VCS (Version Control System) connection in silent mode for the repo linked to the function? In silent mode, comments will not be made on commits and pull requests.
    providerSilentMode: bool

    # Path to function code in the linked repo.
    providerRootDirectory: str

    # Repository name of the template.
    templateRepository: str

    # The name of the owner of the template.
    templateOwner: str

    # Path to function code in the template repo.
    templateRootDirectory: str

    # Production branch for the repo linked to the function template.
    templateBranch: str

class FunctionsCreateNewFunctionRequest(RequiredFunctionsCreateNewFunctionRequest, OptionalFunctionsCreateNewFunctionRequest):
    pass
