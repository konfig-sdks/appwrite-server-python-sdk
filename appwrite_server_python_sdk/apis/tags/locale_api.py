# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_server_python_sdk.paths.locale_languages.get import GetLanguageList
from appwrite_server_python_sdk.paths.locale.get import GetUserLocaleData
from appwrite_server_python_sdk.paths.locale_codes.get import ListCodes
from appwrite_server_python_sdk.paths.locale_continents.get import ListContinents
from appwrite_server_python_sdk.paths.locale_countries.get import ListCountries
from appwrite_server_python_sdk.paths.locale_currencies.get import ListCurrenciesData
from appwrite_server_python_sdk.paths.locale_countries_eu.get import ListEuCountries
from appwrite_server_python_sdk.paths.locale_countries_phones.get import ListPhoneCodes
from appwrite_server_python_sdk.apis.tags.locale_api_raw import LocaleApiRaw


class LocaleApi(
    GetLanguageList,
    GetUserLocaleData,
    ListCodes,
    ListContinents,
    ListCountries,
    ListCurrenciesData,
    ListEuCountries,
    ListPhoneCodes,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: LocaleApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = LocaleApiRaw(api_client)
