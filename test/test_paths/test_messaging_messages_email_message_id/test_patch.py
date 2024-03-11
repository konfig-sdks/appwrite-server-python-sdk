# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

import unittest
from unittest.mock import patch

import urllib3

import appwrite_server_python_sdk
from appwrite_server_python_sdk.paths.messaging_messages_email_message_id import patch
from appwrite_server_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestMessagingMessagesEmailMessageId(ApiTestMixin, unittest.TestCase):
    """
    MessagingMessagesEmailMessageId unit test stubs
        Update email
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()