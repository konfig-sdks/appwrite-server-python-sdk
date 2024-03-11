# coding: utf-8
"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

import typing
import inspect
from datetime import date, datetime
from appwrite_server_python_sdk.client_custom import ClientCustom
from appwrite_server_python_sdk.configuration import Configuration
from appwrite_server_python_sdk.api_client import ApiClient
from appwrite_server_python_sdk.type_util import copy_signature
from appwrite_server_python_sdk.apis.tags.account_api import AccountApi
from appwrite_server_python_sdk.apis.tags.avatars_api import AvatarsApi
from appwrite_server_python_sdk.apis.tags.databases_api import DatabasesApi
from appwrite_server_python_sdk.apis.tags.functions_api import FunctionsApi
from appwrite_server_python_sdk.apis.tags.graphql_api import GraphqlApi
from appwrite_server_python_sdk.apis.tags.health_api import HealthApi
from appwrite_server_python_sdk.apis.tags.locale_api import LocaleApi
from appwrite_server_python_sdk.apis.tags.messaging_api import MessagingApi
from appwrite_server_python_sdk.apis.tags.storage_api import StorageApi
from appwrite_server_python_sdk.apis.tags.teams_api import TeamsApi
from appwrite_server_python_sdk.apis.tags.users_api import UsersApi



class AppwriteServer(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.account: AccountApi = AccountApi(api_client)
        self.avatars: AvatarsApi = AvatarsApi(api_client)
        self.databases: DatabasesApi = DatabasesApi(api_client)
        self.functions: FunctionsApi = FunctionsApi(api_client)
        self.graphql: GraphqlApi = GraphqlApi(api_client)
        self.health: HealthApi = HealthApi(api_client)
        self.locale: LocaleApi = LocaleApi(api_client)
        self.messaging: MessagingApi = MessagingApi(api_client)
        self.storage: StorageApi = StorageApi(api_client)
        self.teams: TeamsApi = TeamsApi(api_client)
        self.users: UsersApi = UsersApi(api_client)
