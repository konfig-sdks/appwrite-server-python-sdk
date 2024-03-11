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


class RequiredUsersCreateScryptUserRequest(TypedDict):
    # User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
    userId: str

    # User email.
    email: str

    # User password hashed using Scrypt.
    password: str

    # Optional salt used to hash password.
    passwordSalt: str

    # Optional CPU cost used to hash password.
    passwordCpu: int

    # Optional memory cost used to hash password.
    passwordMemory: int

    # Optional parallelization cost used to hash password.
    passwordParallel: int

    # Optional hash length used to hash password.
    passwordLength: int

class OptionalUsersCreateScryptUserRequest(TypedDict, total=False):
    # User name. Max length: 128 chars.
    name: str

class UsersCreateScryptUserRequest(RequiredUsersCreateScryptUserRequest, OptionalUsersCreateScryptUserRequest):
    pass
