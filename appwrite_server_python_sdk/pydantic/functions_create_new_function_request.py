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

from appwrite_server_python_sdk.pydantic.functions_create_new_function_request_events import FunctionsCreateNewFunctionRequestEvents
from appwrite_server_python_sdk.pydantic.functions_create_new_function_request_execute import FunctionsCreateNewFunctionRequestExecute

class FunctionsCreateNewFunctionRequest(BaseModel):
    # Function ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
    function_id: str = Field(alias='functionId')

    # Function name. Max length: 128 chars.
    name: str = Field(alias='name')

    # Execution runtime.
    runtime: Literal["node-14.5", "node-16.0", "node-18.0", "node-19.0", "node-20.0", "node-21.0", "php-8.0", "php-8.1", "php-8.2", "php-8.3", "ruby-3.0", "ruby-3.1", "ruby-3.2", "ruby-3.3", "python-3.8", "python-3.9", "python-3.10", "python-3.11", "python-3.12", "deno-1.40", "dart-2.15", "dart-2.16", "dart-2.17", "dart-2.18", "dart-3.0", "dart-3.1", "dart-3.3", "dotnet-3.1", "dotnet-6.0", "dotnet-7.0", "java-8.0", "java-11.0", "java-17.0", "java-18.0", "java-21.0", "swift-5.5", "swift-5.8", "swift-5.9", "kotlin-1.6", "kotlin-1.8", "kotlin-1.9", "cpp-17", "cpp-20", "bun-1.0"] = Field(alias='runtime')

    execute: typing.Optional[FunctionsCreateNewFunctionRequestExecute] = Field(None, alias='execute')

    events: typing.Optional[FunctionsCreateNewFunctionRequestEvents] = Field(None, alias='events')

    # Schedule CRON syntax.
    schedule: typing.Optional[str] = Field(None, alias='schedule')

    # Function maximum execution time in seconds.
    timeout: typing.Optional[int] = Field(None, alias='timeout')

    # Is function enabled? When set to 'disabled', users cannot access the function but Server SDKs with and API key can still access the function. No data is lost when this is toggled.
    enabled: typing.Optional[bool] = Field(None, alias='enabled')

    # Whether executions will be logged. When set to false, executions will not be logged, but will reduce resource used by your Appwrite project.
    logging: typing.Optional[bool] = Field(None, alias='logging')

    # Entrypoint File. This path is relative to the \"providerRootDirectory\".
    entrypoint: typing.Optional[str] = Field(None, alias='entrypoint')

    # Build Commands.
    commands: typing.Optional[str] = Field(None, alias='commands')

    # Appwrite Installation ID for VCS (Version Control System) deployment.
    installation_id: typing.Optional[str] = Field(None, alias='installationId')

    # Repository ID of the repo linked to the function.
    provider_repository_id: typing.Optional[str] = Field(None, alias='providerRepositoryId')

    # Production branch for the repo linked to the function.
    provider_branch: typing.Optional[str] = Field(None, alias='providerBranch')

    # Is the VCS (Version Control System) connection in silent mode for the repo linked to the function? In silent mode, comments will not be made on commits and pull requests.
    provider_silent_mode: typing.Optional[bool] = Field(None, alias='providerSilentMode')

    # Path to function code in the linked repo.
    provider_root_directory: typing.Optional[str] = Field(None, alias='providerRootDirectory')

    # Repository name of the template.
    template_repository: typing.Optional[str] = Field(None, alias='templateRepository')

    # The name of the owner of the template.
    template_owner: typing.Optional[str] = Field(None, alias='templateOwner')

    # Path to function code in the template repo.
    template_root_directory: typing.Optional[str] = Field(None, alias='templateRootDirectory')

    # Production branch for the repo linked to the function template.
    template_branch: typing.Optional[str] = Field(None, alias='templateBranch')
    class Config:
        arbitrary_types_allowed = True
