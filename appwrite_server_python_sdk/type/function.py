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

from appwrite_server_python_sdk.type.function_events import FunctionEvents
from appwrite_server_python_sdk.type.function_execute import FunctionExecute
from appwrite_server_python_sdk.type.variable import Variable

RequiredFunction = TypedDict("RequiredFunction", {
    # Version of Open Runtimes used for the function.
    "version": str,

    # Function ID.
    "$id": str,

    # Function creation date in ISO 8601 format.
    "$createdAt": str,

    # Function update date in ISO 8601 format.
    "$updatedAt": str,

    "execute": FunctionExecute,

    # Function name.
    "name": str,

    # Function enabled.
    "enabled": bool,

    # Is the function deployed with the latest configuration? This is set to false if you've changed an environment variables, entrypoint, commands, or other settings that needs redeploy to be applied. When the value is false, redeploy the function to update it with the latest configuration.
    "live": bool,

    # Whether executions will be logged. When set to false, executions will not be logged, but will reduce resource used by your Appwrite project.
    "logging": bool,

    # Function execution runtime.
    "runtime": str,

    # Function's active deployment ID.
    "deployment": str,

    # Function variables.
    "vars": typing.List[Variable],

    "events": FunctionEvents,

    # Function execution schedult in CRON format.
    "schedule": str,

    # Function execution timeout in seconds.
    "timeout": int,

    # The entrypoint file used to execute the deployment.
    "entrypoint": str,

    # The build command used to build the deployment.
    "commands": str,

    # Function VCS (Version Control System) installation id.
    "installationId": str,

    # VCS (Version Control System) Repository ID
    "providerRepositoryId": str,

    # VCS (Version Control System) branch name
    "providerBranch": str,

    # Path to function in VCS (Version Control System) repository
    "providerRootDirectory": str,

    # Is VCS (Version Control System) connection is in silent mode? When in silence mode, no comments will be posted on the repository pull or merge requests
    "providerSilentMode": bool,
    })

OptionalFunction = TypedDict("OptionalFunction", {
    }, total=False)

class Function(RequiredFunction, OptionalFunction):
    pass
