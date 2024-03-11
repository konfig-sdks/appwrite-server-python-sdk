# coding: utf-8

# flake8: noqa

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

__version__ = "1.5.0"

# import ApiClient
from appwrite_server_python_sdk.api_client import ApiClient

# import Configuration
from appwrite_server_python_sdk.configuration import Configuration

# import exceptions
from appwrite_server_python_sdk.exceptions import OpenApiException
from appwrite_server_python_sdk.exceptions import ApiAttributeError
from appwrite_server_python_sdk.exceptions import ApiTypeError
from appwrite_server_python_sdk.exceptions import ApiValueError
from appwrite_server_python_sdk.exceptions import ApiKeyError
from appwrite_server_python_sdk.exceptions import ApiException

from appwrite_server_python_sdk.client import AppwriteServer
