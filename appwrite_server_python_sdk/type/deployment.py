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


RequiredDeployment = TypedDict("RequiredDeployment", {
    # Deployment ID.
    "$id": str,

    # Deployment creation date in ISO 8601 format.
    "$createdAt": str,

    # Deployment update date in ISO 8601 format.
    "$updatedAt": str,

    # Type of deployment.
    "type": str,

    # Resource ID.
    "resourceId": str,

    # Resource type.
    "resourceType": str,

    # The entrypoint file to use to execute the deployment code.
    "entrypoint": str,

    # The code size in bytes.
    "size": int,

    # The current build ID.
    "buildId": str,

    # Whether the deployment should be automatically activated.
    "activate": bool,

    # The deployment status. Possible values are \"processing\", \"building\", \"waiting\", \"ready\", and \"failed\".
    "status": str,

    # The build logs.
    "buildLogs": str,

    # The current build time in seconds.
    "buildTime": int,

    # The name of the vcs provider repository
    "providerRepositoryName": str,

    # The name of the vcs provider repository owner
    "providerRepositoryOwner": str,

    # The url of the vcs provider repository
    "providerRepositoryUrl": str,

    # The branch of the vcs repository
    "providerBranch": str,

    # The commit hash of the vcs commit
    "providerCommitHash": str,

    # The url of vcs commit author
    "providerCommitAuthorUrl": str,

    # The name of vcs commit author
    "providerCommitAuthor": str,

    # The commit message
    "providerCommitMessage": str,

    # The url of the vcs commit
    "providerCommitUrl": str,

    # The branch of the vcs repository
    "providerBranchUrl": str,
    })

OptionalDeployment = TypedDict("OptionalDeployment", {
    }, total=False)

class Deployment(RequiredDeployment, OptionalDeployment):
    pass
