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

from appwrite_server_python_sdk.pydantic.algo_argon2 import AlgoArgon2
from appwrite_server_python_sdk.pydantic.algo_bcrypt import AlgoBcrypt
from appwrite_server_python_sdk.pydantic.algo_md5 import AlgoMd5
from appwrite_server_python_sdk.pydantic.algo_phpass import AlgoPhpass
from appwrite_server_python_sdk.pydantic.algo_scrypt import AlgoScrypt
from appwrite_server_python_sdk.pydantic.algo_scrypt_modified import AlgoScryptModified
from appwrite_server_python_sdk.pydantic.algo_sha import AlgoSha

UserHashOptions = typing.Optional[typing.List[typing.Union[typing.List[AlgoArgon2], typing.List[AlgoScrypt], typing.List[AlgoScryptModified], typing.List[AlgoBcrypt], typing.List[AlgoPhpass], typing.List[AlgoSha], typing.List[AlgoMd5]]]]
