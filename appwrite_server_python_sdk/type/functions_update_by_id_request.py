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

from appwrite_server_python_sdk.type.functions_update_by_id_request_events import FunctionsUpdateByIdRequestEvents
from appwrite_server_python_sdk.type.functions_update_by_id_request_execute import FunctionsUpdateByIdRequestExecute

class RequiredFunctionsUpdateByIdRequest(TypedDict):
    # Function name. Max length: 128 chars.
    name: str

class OptionalFunctionsUpdateByIdRequest(TypedDict, total=False):
    # Execution runtime.
    runtime: str

    execute: FunctionsUpdateByIdRequestExecute

    events: FunctionsUpdateByIdRequestEvents

    # Schedule CRON syntax.
    schedule: str

    # Maximum execution time in seconds.
    timeout: int

    # Is function enabled? When set to 'disabled', users cannot access the function but Server SDKs with and API key can still access the function. No data is lost when this is toggled.
    enabled: bool

    # Whether executions will be logged. When set to false, executions will not be logged, but will reduce resource used by your Appwrite project.
    logging: bool

    # Entrypoint File. This path is relative to the \"providerRootDirectory\".
    entrypoint: str

    # Build Commands.
    commands: str

    # Appwrite Installation ID for VCS (Version Controle System) deployment.
    installationId: str

    # Repository ID of the repo linked to the function
    providerRepositoryId: str

    # Production branch for the repo linked to the function
    providerBranch: str

    # Is the VCS (Version Control System) connection in silent mode for the repo linked to the function? In silent mode, comments will not be made on commits and pull requests.
    providerSilentMode: bool

    # Path to function code in the linked repo.
    providerRootDirectory: str

class FunctionsUpdateByIdRequest(RequiredFunctionsUpdateByIdRequest, OptionalFunctionsUpdateByIdRequest):
    pass
