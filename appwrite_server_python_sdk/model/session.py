# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from appwrite_server_python_sdk import schemas  # noqa: F401


class Session(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Session
    """


    class MetaOapg:
        required = {
            "clientName",
            "secret",
            "clientVersion",
            "deviceName",
            "clientEngineVersion",
            "providerUid",
            "current",
            "clientType",
            "providerAccessToken",
            "osVersion",
            "provider",
            "countryCode",
            "mfaUpdatedAt",
            "providerRefreshToken",
            "ip",
            "$createdAt",
            "osName",
            "userId",
            "providerAccessTokenExpiry",
            "factors",
            "osCode",
            "clientEngine",
            "clientCode",
            "expire",
            "deviceModel",
            "countryName",
            "deviceBrand",
            "$id",
        }
        
        class properties:
            id = schemas.StrSchema
            created_at = schemas.StrSchema
            userId = schemas.StrSchema
            expire = schemas.StrSchema
            provider = schemas.StrSchema
            providerUid = schemas.StrSchema
            providerAccessToken = schemas.StrSchema
            providerAccessTokenExpiry = schemas.StrSchema
            providerRefreshToken = schemas.StrSchema
            ip = schemas.StrSchema
            osCode = schemas.StrSchema
            osName = schemas.StrSchema
            osVersion = schemas.StrSchema
            clientType = schemas.StrSchema
            clientCode = schemas.StrSchema
            clientName = schemas.StrSchema
            clientVersion = schemas.StrSchema
            clientEngine = schemas.StrSchema
            clientEngineVersion = schemas.StrSchema
            deviceName = schemas.StrSchema
            deviceBrand = schemas.StrSchema
            deviceModel = schemas.StrSchema
            countryCode = schemas.StrSchema
            countryName = schemas.StrSchema
            current = schemas.BoolSchema
        
            @staticmethod
            def factors() -> typing.Type['SessionFactors']:
                return SessionFactors
            secret = schemas.StrSchema
            mfaUpdatedAt = schemas.StrSchema
            __annotations__ = {
                "$id": id,
                "$createdAt": created_at,
                "userId": userId,
                "expire": expire,
                "provider": provider,
                "providerUid": providerUid,
                "providerAccessToken": providerAccessToken,
                "providerAccessTokenExpiry": providerAccessTokenExpiry,
                "providerRefreshToken": providerRefreshToken,
                "ip": ip,
                "osCode": osCode,
                "osName": osName,
                "osVersion": osVersion,
                "clientType": clientType,
                "clientCode": clientCode,
                "clientName": clientName,
                "clientVersion": clientVersion,
                "clientEngine": clientEngine,
                "clientEngineVersion": clientEngineVersion,
                "deviceName": deviceName,
                "deviceBrand": deviceBrand,
                "deviceModel": deviceModel,
                "countryCode": countryCode,
                "countryName": countryName,
                "current": current,
                "factors": factors,
                "secret": secret,
                "mfaUpdatedAt": mfaUpdatedAt,
            }
    
    clientName: MetaOapg.properties.clientName
    secret: MetaOapg.properties.secret
    clientVersion: MetaOapg.properties.clientVersion
    deviceName: MetaOapg.properties.deviceName
    clientEngineVersion: MetaOapg.properties.clientEngineVersion
    providerUid: MetaOapg.properties.providerUid
    current: MetaOapg.properties.current
    clientType: MetaOapg.properties.clientType
    providerAccessToken: MetaOapg.properties.providerAccessToken
    osVersion: MetaOapg.properties.osVersion
    provider: MetaOapg.properties.provider
    countryCode: MetaOapg.properties.countryCode
    mfaUpdatedAt: MetaOapg.properties.mfaUpdatedAt
    providerRefreshToken: MetaOapg.properties.providerRefreshToken
    ip: MetaOapg.properties.ip
    osName: MetaOapg.properties.osName
    userId: MetaOapg.properties.userId
    providerAccessTokenExpiry: MetaOapg.properties.providerAccessTokenExpiry
    factors: 'SessionFactors'
    osCode: MetaOapg.properties.osCode
    clientEngine: MetaOapg.properties.clientEngine
    clientCode: MetaOapg.properties.clientCode
    expire: MetaOapg.properties.expire
    deviceModel: MetaOapg.properties.deviceModel
    countryName: MetaOapg.properties.countryName
    deviceBrand: MetaOapg.properties.deviceBrand
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$createdAt"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expire"]) -> MetaOapg.properties.expire: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerUid"]) -> MetaOapg.properties.providerUid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerAccessToken"]) -> MetaOapg.properties.providerAccessToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerAccessTokenExpiry"]) -> MetaOapg.properties.providerAccessTokenExpiry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerRefreshToken"]) -> MetaOapg.properties.providerRefreshToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ip"]) -> MetaOapg.properties.ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["osCode"]) -> MetaOapg.properties.osCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["osName"]) -> MetaOapg.properties.osName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["osVersion"]) -> MetaOapg.properties.osVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientType"]) -> MetaOapg.properties.clientType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientCode"]) -> MetaOapg.properties.clientCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientName"]) -> MetaOapg.properties.clientName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientVersion"]) -> MetaOapg.properties.clientVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientEngine"]) -> MetaOapg.properties.clientEngine: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientEngineVersion"]) -> MetaOapg.properties.clientEngineVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deviceName"]) -> MetaOapg.properties.deviceName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deviceBrand"]) -> MetaOapg.properties.deviceBrand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deviceModel"]) -> MetaOapg.properties.deviceModel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryCode"]) -> MetaOapg.properties.countryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryName"]) -> MetaOapg.properties.countryName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current"]) -> MetaOapg.properties.current: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["factors"]) -> 'SessionFactors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mfaUpdatedAt"]) -> MetaOapg.properties.mfaUpdatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["$id", "$createdAt", "userId", "expire", "provider", "providerUid", "providerAccessToken", "providerAccessTokenExpiry", "providerRefreshToken", "ip", "osCode", "osName", "osVersion", "clientType", "clientCode", "clientName", "clientVersion", "clientEngine", "clientEngineVersion", "deviceName", "deviceBrand", "deviceModel", "countryCode", "countryName", "current", "factors", "secret", "mfaUpdatedAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$createdAt"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expire"]) -> MetaOapg.properties.expire: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerUid"]) -> MetaOapg.properties.providerUid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerAccessToken"]) -> MetaOapg.properties.providerAccessToken: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerAccessTokenExpiry"]) -> MetaOapg.properties.providerAccessTokenExpiry: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerRefreshToken"]) -> MetaOapg.properties.providerRefreshToken: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ip"]) -> MetaOapg.properties.ip: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["osCode"]) -> MetaOapg.properties.osCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["osName"]) -> MetaOapg.properties.osName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["osVersion"]) -> MetaOapg.properties.osVersion: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientType"]) -> MetaOapg.properties.clientType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientCode"]) -> MetaOapg.properties.clientCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientName"]) -> MetaOapg.properties.clientName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientVersion"]) -> MetaOapg.properties.clientVersion: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientEngine"]) -> MetaOapg.properties.clientEngine: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientEngineVersion"]) -> MetaOapg.properties.clientEngineVersion: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deviceName"]) -> MetaOapg.properties.deviceName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deviceBrand"]) -> MetaOapg.properties.deviceBrand: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deviceModel"]) -> MetaOapg.properties.deviceModel: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryCode"]) -> MetaOapg.properties.countryCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryName"]) -> MetaOapg.properties.countryName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current"]) -> MetaOapg.properties.current: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["factors"]) -> 'SessionFactors': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mfaUpdatedAt"]) -> MetaOapg.properties.mfaUpdatedAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["$id", "$createdAt", "userId", "expire", "provider", "providerUid", "providerAccessToken", "providerAccessTokenExpiry", "providerRefreshToken", "ip", "osCode", "osName", "osVersion", "clientType", "clientCode", "clientName", "clientVersion", "clientEngine", "clientEngineVersion", "deviceName", "deviceBrand", "deviceModel", "countryCode", "countryName", "current", "factors", "secret", "mfaUpdatedAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        clientName: typing.Union[MetaOapg.properties.clientName, str, ],
        secret: typing.Union[MetaOapg.properties.secret, str, ],
        clientVersion: typing.Union[MetaOapg.properties.clientVersion, str, ],
        deviceName: typing.Union[MetaOapg.properties.deviceName, str, ],
        clientEngineVersion: typing.Union[MetaOapg.properties.clientEngineVersion, str, ],
        providerUid: typing.Union[MetaOapg.properties.providerUid, str, ],
        current: typing.Union[MetaOapg.properties.current, bool, ],
        clientType: typing.Union[MetaOapg.properties.clientType, str, ],
        providerAccessToken: typing.Union[MetaOapg.properties.providerAccessToken, str, ],
        osVersion: typing.Union[MetaOapg.properties.osVersion, str, ],
        provider: typing.Union[MetaOapg.properties.provider, str, ],
        countryCode: typing.Union[MetaOapg.properties.countryCode, str, ],
        mfaUpdatedAt: typing.Union[MetaOapg.properties.mfaUpdatedAt, str, ],
        providerRefreshToken: typing.Union[MetaOapg.properties.providerRefreshToken, str, ],
        ip: typing.Union[MetaOapg.properties.ip, str, ],
        osName: typing.Union[MetaOapg.properties.osName, str, ],
        userId: typing.Union[MetaOapg.properties.userId, str, ],
        providerAccessTokenExpiry: typing.Union[MetaOapg.properties.providerAccessTokenExpiry, str, ],
        factors: 'SessionFactors',
        osCode: typing.Union[MetaOapg.properties.osCode, str, ],
        clientEngine: typing.Union[MetaOapg.properties.clientEngine, str, ],
        clientCode: typing.Union[MetaOapg.properties.clientCode, str, ],
        expire: typing.Union[MetaOapg.properties.expire, str, ],
        deviceModel: typing.Union[MetaOapg.properties.deviceModel, str, ],
        countryName: typing.Union[MetaOapg.properties.countryName, str, ],
        deviceBrand: typing.Union[MetaOapg.properties.deviceBrand, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Session':
        return super().__new__(
            cls,
            *args,
            clientName=clientName,
            secret=secret,
            clientVersion=clientVersion,
            deviceName=deviceName,
            clientEngineVersion=clientEngineVersion,
            providerUid=providerUid,
            current=current,
            clientType=clientType,
            providerAccessToken=providerAccessToken,
            osVersion=osVersion,
            provider=provider,
            countryCode=countryCode,
            mfaUpdatedAt=mfaUpdatedAt,
            providerRefreshToken=providerRefreshToken,
            ip=ip,
            osName=osName,
            userId=userId,
            providerAccessTokenExpiry=providerAccessTokenExpiry,
            factors=factors,
            osCode=osCode,
            clientEngine=clientEngine,
            clientCode=clientCode,
            expire=expire,
            deviceModel=deviceModel,
            countryName=countryName,
            deviceBrand=deviceBrand,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_server_python_sdk.model.session_factors import SessionFactors
