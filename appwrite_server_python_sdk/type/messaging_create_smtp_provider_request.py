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


class RequiredMessagingCreateSmtpProviderRequest(TypedDict):
    # Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
    providerId: str

    # Provider name.
    name: str

    # SMTP hosts. Either a single hostname or multiple semicolon-delimited hostnames. You can also specify a different port for each host such as `smtp1.example.com:25;smtp2.example.com`. You can also specify encryption type, for example: `tls://smtp1.example.com:587;ssl://smtp2.example.com:465\"`. Hosts will be tried in order.
    host: str

class OptionalMessagingCreateSmtpProviderRequest(TypedDict, total=False):
    # The default SMTP server port.
    port: int

    # Authentication username.
    username: str

    # Authentication password.
    password: str

    # Encryption type. Can be omitted, 'ssl', or 'tls'
    encryption: str

    # Enable SMTP AutoTLS feature.
    autoTLS: bool

    # The value to use for the X-Mailer header.
    mailer: str

    # Sender Name.
    fromName: str

    # Sender email address.
    fromEmail: str

    # Name set in the reply to field for the mail. Default value is sender name.
    replyToName: str

    # Email set in the reply to field for the mail. Default value is sender email.
    replyToEmail: str

    # Set as enabled.
    enabled: bool

class MessagingCreateSmtpProviderRequest(RequiredMessagingCreateSmtpProviderRequest, OptionalMessagingCreateSmtpProviderRequest):
    pass
