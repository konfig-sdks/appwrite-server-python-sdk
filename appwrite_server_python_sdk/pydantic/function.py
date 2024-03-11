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

from appwrite_server_python_sdk.pydantic.function_events import FunctionEvents
from appwrite_server_python_sdk.pydantic.function_execute import FunctionExecute
from appwrite_server_python_sdk.pydantic.variable import Variable

class Function(BaseModel):
    # Version of Open Runtimes used for the function.
    version: str = Field(alias='version')

    # Function ID.
    $id_: str = Field(alias='$id')

    # Function creation date in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Function update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    execute: FunctionExecute = Field(alias='execute')

    # Function name.
    name: str = Field(alias='name')

    # Function enabled.
    enabled: bool = Field(alias='enabled')

    # Is the function deployed with the latest configuration? This is set to false if you've changed an environment variables, entrypoint, commands, or other settings that needs redeploy to be applied. When the value is false, redeploy the function to update it with the latest configuration.
    live: bool = Field(alias='live')

    # Whether executions will be logged. When set to false, executions will not be logged, but will reduce resource used by your Appwrite project.
    logging: bool = Field(alias='logging')

    # Function execution runtime.
    runtime: str = Field(alias='runtime')

    # Function's active deployment ID.
    deployment: str = Field(alias='deployment')

    # Function variables.
    vars: typing.List[Variable] = Field(alias='vars')

    events: FunctionEvents = Field(alias='events')

    # Function execution schedult in CRON format.
    schedule: str = Field(alias='schedule')

    # Function execution timeout in seconds.
    timeout: int = Field(alias='timeout')

    # The entrypoint file used to execute the deployment.
    entrypoint: str = Field(alias='entrypoint')

    # The build command used to build the deployment.
    commands: str = Field(alias='commands')

    # Function VCS (Version Control System) installation id.
    installation_id: str = Field(alias='installationId')

    # VCS (Version Control System) Repository ID
    provider_repository_id: str = Field(alias='providerRepositoryId')

    # VCS (Version Control System) branch name
    provider_branch: str = Field(alias='providerBranch')

    # Path to function in VCS (Version Control System) repository
    provider_root_directory: str = Field(alias='providerRootDirectory')

    # Is VCS (Version Control System) connection is in silent mode? When in silence mode, no comments will be posted on the repository pull or merge requests
    provider_silent_mode: bool = Field(alias='providerSilentMode')
    class Config:
        arbitrary_types_allowed = True
