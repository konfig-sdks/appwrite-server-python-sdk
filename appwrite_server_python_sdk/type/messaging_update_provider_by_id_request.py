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


class RequiredMessagingUpdateProviderByIdRequest(TypedDict):
    pass

class OptionalMessagingUpdateProviderByIdRequest(TypedDict, total=False):
    # Provider name.
    name: str

    # SMTP hosts. Either a single hostname or multiple semicolon-delimited hostnames. You can also specify a different port for each host such as `smtp1.example.com:25;smtp2.example.com`. You can also specify encryption type, for example: `tls://smtp1.example.com:587;ssl://smtp2.example.com:465\"`. Hosts will be tried in order.
    host: str

    # SMTP port.
    port: int

    # Authentication username.
    username: str

    # Authentication password.
    password: str

    # Encryption type. Can be 'ssl' or 'tls'
    encryption: str

    # Enable SMTP AutoTLS feature.
    autoTLS: bool

    # The value to use for the X-Mailer header.
    mailer: str

    # Sender Name.
    fromName: str

    # Sender email address.
    fromEmail: str

    # Name set in the Reply To field for the mail. Default value is Sender Name.
    replyToName: str

    # Email set in the Reply To field for the mail. Default value is Sender Email.
    replyToEmail: str

    # Set as enabled.
    enabled: bool

class MessagingUpdateProviderByIdRequest(RequiredMessagingUpdateProviderByIdRequest, OptionalMessagingUpdateProviderByIdRequest):
    pass
