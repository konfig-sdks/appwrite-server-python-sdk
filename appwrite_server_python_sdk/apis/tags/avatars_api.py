# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_server_python_sdk.paths.avatars_qr.get import GenerateQrCode
from appwrite_server_python_sdk.paths.avatars_browsers_code.get import GetBrowserIcon
from appwrite_server_python_sdk.paths.avatars_flags_code.get import GetCountryFlag
from appwrite_server_python_sdk.paths.avatars_credit_cards_code.get import GetCreditCardIcon
from appwrite_server_python_sdk.paths.avatars_favicon.get import GetFavicon
from appwrite_server_python_sdk.paths.avatars_image.get import GetRemoteImage
from appwrite_server_python_sdk.paths.avatars_initials.get import GetUserInitials
from appwrite_server_python_sdk.apis.tags.avatars_api_raw import AvatarsApiRaw


class AvatarsApi(
    GenerateQrCode,
    GetBrowserIcon,
    GetCountryFlag,
    GetCreditCardIcon,
    GetFavicon,
    GetRemoteImage,
    GetUserInitials,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AvatarsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AvatarsApiRaw(api_client)