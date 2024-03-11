# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from appwrite_server_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from appwrite_server_python_sdk.api_response import AsyncGeneratorResponse
from appwrite_server_python_sdk import api_client, exceptions
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



from ...api_client import Dictionary

# Query params
WidthSchema = schemas.Int32Schema
HeightSchema = schemas.Int32Schema
QualitySchema = schemas.Int32Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'width': typing.Union[WidthSchema, decimal.Decimal, int, ],
        'height': typing.Union[HeightSchema, decimal.Decimal, int, ],
        'quality': typing.Union[QualitySchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_width = api_client.QueryParameter(
    name="width",
    style=api_client.ParameterStyle.FORM,
    schema=WidthSchema,
    explode=True,
)
request_query_height = api_client.QueryParameter(
    name="height",
    style=api_client.ParameterStyle.FORM,
    schema=HeightSchema,
    explode=True,
)
request_query_quality = api_client.QueryParameter(
    name="quality",
    style=api_client.ParameterStyle.FORM,
    schema=QualitySchema,
    explode=True,
)
# Path params


class CodeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def AF(cls):
        return cls("af")
    
    @schemas.classproperty
    def AO(cls):
        return cls("ao")
    
    @schemas.classproperty
    def AL(cls):
        return cls("al")
    
    @schemas.classproperty
    def AD(cls):
        return cls("ad")
    
    @schemas.classproperty
    def AE(cls):
        return cls("ae")
    
    @schemas.classproperty
    def AR(cls):
        return cls("ar")
    
    @schemas.classproperty
    def AM(cls):
        return cls("am")
    
    @schemas.classproperty
    def AG(cls):
        return cls("ag")
    
    @schemas.classproperty
    def AU(cls):
        return cls("au")
    
    @schemas.classproperty
    def AT(cls):
        return cls("at")
    
    @schemas.classproperty
    def AZ(cls):
        return cls("az")
    
    @schemas.classproperty
    def BI(cls):
        return cls("bi")
    
    @schemas.classproperty
    def BE(cls):
        return cls("be")
    
    @schemas.classproperty
    def BJ(cls):
        return cls("bj")
    
    @schemas.classproperty
    def BF(cls):
        return cls("bf")
    
    @schemas.classproperty
    def BD(cls):
        return cls("bd")
    
    @schemas.classproperty
    def BG(cls):
        return cls("bg")
    
    @schemas.classproperty
    def BH(cls):
        return cls("bh")
    
    @schemas.classproperty
    def BS(cls):
        return cls("bs")
    
    @schemas.classproperty
    def BA(cls):
        return cls("ba")
    
    @schemas.classproperty
    def BY(cls):
        return cls("by")
    
    @schemas.classproperty
    def BZ(cls):
        return cls("bz")
    
    @schemas.classproperty
    def BO(cls):
        return cls("bo")
    
    @schemas.classproperty
    def BR(cls):
        return cls("br")
    
    @schemas.classproperty
    def BB(cls):
        return cls("bb")
    
    @schemas.classproperty
    def BN(cls):
        return cls("bn")
    
    @schemas.classproperty
    def BT(cls):
        return cls("bt")
    
    @schemas.classproperty
    def BW(cls):
        return cls("bw")
    
    @schemas.classproperty
    def CF(cls):
        return cls("cf")
    
    @schemas.classproperty
    def CA(cls):
        return cls("ca")
    
    @schemas.classproperty
    def CH(cls):
        return cls("ch")
    
    @schemas.classproperty
    def CL(cls):
        return cls("cl")
    
    @schemas.classproperty
    def CN(cls):
        return cls("cn")
    
    @schemas.classproperty
    def CI(cls):
        return cls("ci")
    
    @schemas.classproperty
    def CM(cls):
        return cls("cm")
    
    @schemas.classproperty
    def CD(cls):
        return cls("cd")
    
    @schemas.classproperty
    def CG(cls):
        return cls("cg")
    
    @schemas.classproperty
    def CO(cls):
        return cls("co")
    
    @schemas.classproperty
    def KM(cls):
        return cls("km")
    
    @schemas.classproperty
    def CV(cls):
        return cls("cv")
    
    @schemas.classproperty
    def CR(cls):
        return cls("cr")
    
    @schemas.classproperty
    def CU(cls):
        return cls("cu")
    
    @schemas.classproperty
    def CY(cls):
        return cls("cy")
    
    @schemas.classproperty
    def CZ(cls):
        return cls("cz")
    
    @schemas.classproperty
    def DE(cls):
        return cls("de")
    
    @schemas.classproperty
    def DJ(cls):
        return cls("dj")
    
    @schemas.classproperty
    def DM(cls):
        return cls("dm")
    
    @schemas.classproperty
    def DK(cls):
        return cls("dk")
    
    @schemas.classproperty
    def DO(cls):
        return cls("do")
    
    @schemas.classproperty
    def DZ(cls):
        return cls("dz")
    
    @schemas.classproperty
    def EC(cls):
        return cls("ec")
    
    @schemas.classproperty
    def EG(cls):
        return cls("eg")
    
    @schemas.classproperty
    def ER(cls):
        return cls("er")
    
    @schemas.classproperty
    def ES(cls):
        return cls("es")
    
    @schemas.classproperty
    def EE(cls):
        return cls("ee")
    
    @schemas.classproperty
    def ET(cls):
        return cls("et")
    
    @schemas.classproperty
    def FI(cls):
        return cls("fi")
    
    @schemas.classproperty
    def FJ(cls):
        return cls("fj")
    
    @schemas.classproperty
    def FR(cls):
        return cls("fr")
    
    @schemas.classproperty
    def FM(cls):
        return cls("fm")
    
    @schemas.classproperty
    def GA(cls):
        return cls("ga")
    
    @schemas.classproperty
    def GB(cls):
        return cls("gb")
    
    @schemas.classproperty
    def GE(cls):
        return cls("ge")
    
    @schemas.classproperty
    def GH(cls):
        return cls("gh")
    
    @schemas.classproperty
    def GN(cls):
        return cls("gn")
    
    @schemas.classproperty
    def GM(cls):
        return cls("gm")
    
    @schemas.classproperty
    def GW(cls):
        return cls("gw")
    
    @schemas.classproperty
    def GQ(cls):
        return cls("gq")
    
    @schemas.classproperty
    def GR(cls):
        return cls("gr")
    
    @schemas.classproperty
    def GD(cls):
        return cls("gd")
    
    @schemas.classproperty
    def GT(cls):
        return cls("gt")
    
    @schemas.classproperty
    def GY(cls):
        return cls("gy")
    
    @schemas.classproperty
    def HN(cls):
        return cls("hn")
    
    @schemas.classproperty
    def HR(cls):
        return cls("hr")
    
    @schemas.classproperty
    def HT(cls):
        return cls("ht")
    
    @schemas.classproperty
    def HU(cls):
        return cls("hu")
    
    @schemas.classproperty
    def ID(cls):
        return cls("id")
    
    @schemas.classproperty
    def IN(cls):
        return cls("in")
    
    @schemas.classproperty
    def IE(cls):
        return cls("ie")
    
    @schemas.classproperty
    def IR(cls):
        return cls("ir")
    
    @schemas.classproperty
    def IQ(cls):
        return cls("iq")
    
    @schemas.classproperty
    def IS(cls):
        return cls("is")
    
    @schemas.classproperty
    def IL(cls):
        return cls("il")
    
    @schemas.classproperty
    def IT(cls):
        return cls("it")
    
    @schemas.classproperty
    def JM(cls):
        return cls("jm")
    
    @schemas.classproperty
    def JO(cls):
        return cls("jo")
    
    @schemas.classproperty
    def JP(cls):
        return cls("jp")
    
    @schemas.classproperty
    def KZ(cls):
        return cls("kz")
    
    @schemas.classproperty
    def KE(cls):
        return cls("ke")
    
    @schemas.classproperty
    def KG(cls):
        return cls("kg")
    
    @schemas.classproperty
    def KH(cls):
        return cls("kh")
    
    @schemas.classproperty
    def KI(cls):
        return cls("ki")
    
    @schemas.classproperty
    def KN(cls):
        return cls("kn")
    
    @schemas.classproperty
    def KR(cls):
        return cls("kr")
    
    @schemas.classproperty
    def KW(cls):
        return cls("kw")
    
    @schemas.classproperty
    def LA(cls):
        return cls("la")
    
    @schemas.classproperty
    def LB(cls):
        return cls("lb")
    
    @schemas.classproperty
    def LR(cls):
        return cls("lr")
    
    @schemas.classproperty
    def LY(cls):
        return cls("ly")
    
    @schemas.classproperty
    def LC(cls):
        return cls("lc")
    
    @schemas.classproperty
    def LI(cls):
        return cls("li")
    
    @schemas.classproperty
    def LK(cls):
        return cls("lk")
    
    @schemas.classproperty
    def LS(cls):
        return cls("ls")
    
    @schemas.classproperty
    def LT(cls):
        return cls("lt")
    
    @schemas.classproperty
    def LU(cls):
        return cls("lu")
    
    @schemas.classproperty
    def LV(cls):
        return cls("lv")
    
    @schemas.classproperty
    def MA(cls):
        return cls("ma")
    
    @schemas.classproperty
    def MC(cls):
        return cls("mc")
    
    @schemas.classproperty
    def MD(cls):
        return cls("md")
    
    @schemas.classproperty
    def MG(cls):
        return cls("mg")
    
    @schemas.classproperty
    def MV(cls):
        return cls("mv")
    
    @schemas.classproperty
    def MX(cls):
        return cls("mx")
    
    @schemas.classproperty
    def MH(cls):
        return cls("mh")
    
    @schemas.classproperty
    def MK(cls):
        return cls("mk")
    
    @schemas.classproperty
    def ML(cls):
        return cls("ml")
    
    @schemas.classproperty
    def MT(cls):
        return cls("mt")
    
    @schemas.classproperty
    def MM(cls):
        return cls("mm")
    
    @schemas.classproperty
    def ME(cls):
        return cls("me")
    
    @schemas.classproperty
    def MN(cls):
        return cls("mn")
    
    @schemas.classproperty
    def MZ(cls):
        return cls("mz")
    
    @schemas.classproperty
    def MR(cls):
        return cls("mr")
    
    @schemas.classproperty
    def MU(cls):
        return cls("mu")
    
    @schemas.classproperty
    def MW(cls):
        return cls("mw")
    
    @schemas.classproperty
    def MY(cls):
        return cls("my")
    
    @schemas.classproperty
    def NA(cls):
        return cls("na")
    
    @schemas.classproperty
    def NE(cls):
        return cls("ne")
    
    @schemas.classproperty
    def NG(cls):
        return cls("ng")
    
    @schemas.classproperty
    def NI(cls):
        return cls("ni")
    
    @schemas.classproperty
    def NL(cls):
        return cls("nl")
    
    @schemas.classproperty
    def FALSE(cls):
        return cls("false")
    
    @schemas.classproperty
    def NP(cls):
        return cls("np")
    
    @schemas.classproperty
    def NR(cls):
        return cls("nr")
    
    @schemas.classproperty
    def NZ(cls):
        return cls("nz")
    
    @schemas.classproperty
    def OM(cls):
        return cls("om")
    
    @schemas.classproperty
    def PK(cls):
        return cls("pk")
    
    @schemas.classproperty
    def PA(cls):
        return cls("pa")
    
    @schemas.classproperty
    def PE(cls):
        return cls("pe")
    
    @schemas.classproperty
    def PH(cls):
        return cls("ph")
    
    @schemas.classproperty
    def PW(cls):
        return cls("pw")
    
    @schemas.classproperty
    def PG(cls):
        return cls("pg")
    
    @schemas.classproperty
    def PL(cls):
        return cls("pl")
    
    @schemas.classproperty
    def KP(cls):
        return cls("kp")
    
    @schemas.classproperty
    def PT(cls):
        return cls("pt")
    
    @schemas.classproperty
    def PY(cls):
        return cls("py")
    
    @schemas.classproperty
    def QA(cls):
        return cls("qa")
    
    @schemas.classproperty
    def RO(cls):
        return cls("ro")
    
    @schemas.classproperty
    def RU(cls):
        return cls("ru")
    
    @schemas.classproperty
    def RW(cls):
        return cls("rw")
    
    @schemas.classproperty
    def SA(cls):
        return cls("sa")
    
    @schemas.classproperty
    def SD(cls):
        return cls("sd")
    
    @schemas.classproperty
    def SN(cls):
        return cls("sn")
    
    @schemas.classproperty
    def SG(cls):
        return cls("sg")
    
    @schemas.classproperty
    def SB(cls):
        return cls("sb")
    
    @schemas.classproperty
    def SL(cls):
        return cls("sl")
    
    @schemas.classproperty
    def SV(cls):
        return cls("sv")
    
    @schemas.classproperty
    def SM(cls):
        return cls("sm")
    
    @schemas.classproperty
    def SO(cls):
        return cls("so")
    
    @schemas.classproperty
    def RS(cls):
        return cls("rs")
    
    @schemas.classproperty
    def SS(cls):
        return cls("ss")
    
    @schemas.classproperty
    def ST(cls):
        return cls("st")
    
    @schemas.classproperty
    def SR(cls):
        return cls("sr")
    
    @schemas.classproperty
    def SK(cls):
        return cls("sk")
    
    @schemas.classproperty
    def SI(cls):
        return cls("si")
    
    @schemas.classproperty
    def SE(cls):
        return cls("se")
    
    @schemas.classproperty
    def SZ(cls):
        return cls("sz")
    
    @schemas.classproperty
    def SC(cls):
        return cls("sc")
    
    @schemas.classproperty
    def SY(cls):
        return cls("sy")
    
    @schemas.classproperty
    def TD(cls):
        return cls("td")
    
    @schemas.classproperty
    def TG(cls):
        return cls("tg")
    
    @schemas.classproperty
    def TH(cls):
        return cls("th")
    
    @schemas.classproperty
    def TJ(cls):
        return cls("tj")
    
    @schemas.classproperty
    def TM(cls):
        return cls("tm")
    
    @schemas.classproperty
    def TL(cls):
        return cls("tl")
    
    @schemas.classproperty
    def TO(cls):
        return cls("to")
    
    @schemas.classproperty
    def TT(cls):
        return cls("tt")
    
    @schemas.classproperty
    def TN(cls):
        return cls("tn")
    
    @schemas.classproperty
    def TR(cls):
        return cls("tr")
    
    @schemas.classproperty
    def TV(cls):
        return cls("tv")
    
    @schemas.classproperty
    def TZ(cls):
        return cls("tz")
    
    @schemas.classproperty
    def UG(cls):
        return cls("ug")
    
    @schemas.classproperty
    def UA(cls):
        return cls("ua")
    
    @schemas.classproperty
    def UY(cls):
        return cls("uy")
    
    @schemas.classproperty
    def US(cls):
        return cls("us")
    
    @schemas.classproperty
    def UZ(cls):
        return cls("uz")
    
    @schemas.classproperty
    def VA(cls):
        return cls("va")
    
    @schemas.classproperty
    def VC(cls):
        return cls("vc")
    
    @schemas.classproperty
    def VE(cls):
        return cls("ve")
    
    @schemas.classproperty
    def VN(cls):
        return cls("vn")
    
    @schemas.classproperty
    def VU(cls):
        return cls("vu")
    
    @schemas.classproperty
    def WS(cls):
        return cls("ws")
    
    @schemas.classproperty
    def YE(cls):
        return cls("ye")
    
    @schemas.classproperty
    def ZA(cls):
        return cls("za")
    
    @schemas.classproperty
    def ZM(cls):
        return cls("zm")
    
    @schemas.classproperty
    def ZW(cls):
        return cls("zw")
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'code': typing.Union[CodeSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_code = api_client.PathParameter(
    name="code",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CodeSchema,
    required=True,
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
)


class BaseApi(api_client.Api):

    def _get_country_flag_mapped_args(
        self,
        code: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        quality: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if width is not None:
            _query_params["width"] = width
        if height is not None:
            _query_params["height"] = height
        if quality is not None:
            _query_params["quality"] = quality
        if code is not None:
            _path_params["code"] = code
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_country_flag_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get country flag
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_code,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_width,
            request_query_height,
            request_query_quality,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/avatars/flags/{code}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_country_flag_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get country flag
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_code,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_width,
            request_query_height,
            request_query_quality,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/avatars/flags/{code}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetCountryFlagRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_country_flag(
        self,
        code: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        quality: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_country_flag_mapped_args(
            code=code,
            width=width,
            height=height,
            quality=quality,
        )
        return await self._aget_country_flag_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_country_flag(
        self,
        code: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        quality: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_country_flag_mapped_args(
            code=code,
            width=width,
            height=height,
            quality=quality,
        )
        return self._get_country_flag_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetCountryFlag(BaseApi):

    async def aget_country_flag(
        self,
        code: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        quality: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aget_country_flag(
            code=code,
            width=width,
            height=height,
            quality=quality,
            **kwargs,
        )
    
    
    def get_country_flag(
        self,
        code: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        quality: typing.Optional[int] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.get_country_flag(
            code=code,
            width=width,
            height=height,
            quality=quality,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        code: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        quality: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_country_flag_mapped_args(
            code=code,
            width=width,
            height=height,
            quality=quality,
        )
        return await self._aget_country_flag_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        code: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        quality: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_country_flag_mapped_args(
            code=code,
            width=width,
            height=height,
            quality=quality,
        )
        return self._get_country_flag_oapg(
            query_params=args.query,
            path_params=args.path,
        )

