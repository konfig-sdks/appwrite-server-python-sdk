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


class Deployment(BaseModel):
    # Deployment ID.
    $id_: str = Field(alias='$id')

    # Deployment creation date in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Deployment update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    # Type of deployment.
    type: str = Field(alias='type')

    # Resource ID.
    resource_id: str = Field(alias='resourceId')

    # Resource type.
    resource_type: str = Field(alias='resourceType')

    # The entrypoint file to use to execute the deployment code.
    entrypoint: str = Field(alias='entrypoint')

    # The code size in bytes.
    size: int = Field(alias='size')

    # The current build ID.
    build_id: str = Field(alias='buildId')

    # Whether the deployment should be automatically activated.
    activate: bool = Field(alias='activate')

    # The deployment status. Possible values are \"processing\", \"building\", \"waiting\", \"ready\", and \"failed\".
    status: str = Field(alias='status')

    # The build logs.
    build_logs: str = Field(alias='buildLogs')

    # The current build time in seconds.
    build_time: int = Field(alias='buildTime')

    # The name of the vcs provider repository
    provider_repository_name: str = Field(alias='providerRepositoryName')

    # The name of the vcs provider repository owner
    provider_repository_owner: str = Field(alias='providerRepositoryOwner')

    # The url of the vcs provider repository
    provider_repository_url: str = Field(alias='providerRepositoryUrl')

    # The branch of the vcs repository
    provider_branch: str = Field(alias='providerBranch')

    # The commit hash of the vcs commit
    provider_commit_hash: str = Field(alias='providerCommitHash')

    # The url of vcs commit author
    provider_commit_author_url: str = Field(alias='providerCommitAuthorUrl')

    # The name of vcs commit author
    provider_commit_author: str = Field(alias='providerCommitAuthor')

    # The commit message
    provider_commit_message: str = Field(alias='providerCommitMessage')

    # The url of the vcs commit
    provider_commit_url: str = Field(alias='providerCommitUrl')

    # The branch of the vcs repository
    provider_branch_url: str = Field(alias='providerBranchUrl')
    class Config:
        arbitrary_types_allowed = True
