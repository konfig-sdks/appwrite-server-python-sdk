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


class HealthCertificate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Health Certificate
    """


    class MetaOapg:
        required = {
            "signatureTypeSN",
            "name",
            "issuerOrganisation",
            "validFrom",
            "subjectSN",
            "validTo",
        }
        
        class properties:
            name = schemas.StrSchema
            subjectSN = schemas.StrSchema
            issuerOrganisation = schemas.StrSchema
            validFrom = schemas.StrSchema
            validTo = schemas.StrSchema
            signatureTypeSN = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "subjectSN": subjectSN,
                "issuerOrganisation": issuerOrganisation,
                "validFrom": validFrom,
                "validTo": validTo,
                "signatureTypeSN": signatureTypeSN,
            }
    
    signatureTypeSN: MetaOapg.properties.signatureTypeSN
    name: MetaOapg.properties.name
    issuerOrganisation: MetaOapg.properties.issuerOrganisation
    validFrom: MetaOapg.properties.validFrom
    subjectSN: MetaOapg.properties.subjectSN
    validTo: MetaOapg.properties.validTo
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subjectSN"]) -> MetaOapg.properties.subjectSN: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issuerOrganisation"]) -> MetaOapg.properties.issuerOrganisation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validFrom"]) -> MetaOapg.properties.validFrom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validTo"]) -> MetaOapg.properties.validTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signatureTypeSN"]) -> MetaOapg.properties.signatureTypeSN: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "subjectSN", "issuerOrganisation", "validFrom", "validTo", "signatureTypeSN", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subjectSN"]) -> MetaOapg.properties.subjectSN: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issuerOrganisation"]) -> MetaOapg.properties.issuerOrganisation: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validFrom"]) -> MetaOapg.properties.validFrom: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validTo"]) -> MetaOapg.properties.validTo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signatureTypeSN"]) -> MetaOapg.properties.signatureTypeSN: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "subjectSN", "issuerOrganisation", "validFrom", "validTo", "signatureTypeSN", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        signatureTypeSN: typing.Union[MetaOapg.properties.signatureTypeSN, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        issuerOrganisation: typing.Union[MetaOapg.properties.issuerOrganisation, str, ],
        validFrom: typing.Union[MetaOapg.properties.validFrom, str, ],
        subjectSN: typing.Union[MetaOapg.properties.subjectSN, str, ],
        validTo: typing.Union[MetaOapg.properties.validTo, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'HealthCertificate':
        return super().__new__(
            cls,
            *args,
            signatureTypeSN=signatureTypeSN,
            name=name,
            issuerOrganisation=issuerOrganisation,
            validFrom=validFrom,
            subjectSN=subjectSN,
            validTo=validTo,
            _configuration=_configuration,
            **kwargs,
        )
