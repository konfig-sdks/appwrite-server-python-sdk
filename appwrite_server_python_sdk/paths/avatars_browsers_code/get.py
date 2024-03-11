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

from . import path

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


    class MetaOapg:
        enum_value_to_name = {
            "aa": "AA",
            "an": "AN",
            "ch": "CH",
            "ci": "CI",
            "cm": "CM",
            "cr": "CR",
            "ff": "FF",
            "sf": "SF",
            "mf": "MF",
            "ps": "PS",
            "oi": "OI",
            "om": "OM",
            "op": "OP",
            "true": "TRUE",
        }
    
    @schemas.classproperty
    def AA(cls):
        return cls("aa")
    
    @schemas.classproperty
    def AN(cls):
        return cls("an")
    
    @schemas.classproperty
    def CH(cls):
        return cls("ch")
    
    @schemas.classproperty
    def CI(cls):
        return cls("ci")
    
    @schemas.classproperty
    def CM(cls):
        return cls("cm")
    
    @schemas.classproperty
    def CR(cls):
        return cls("cr")
    
    @schemas.classproperty
    def FF(cls):
        return cls("ff")
    
    @schemas.classproperty
    def SF(cls):
        return cls("sf")
    
    @schemas.classproperty
    def MF(cls):
        return cls("mf")
    
    @schemas.classproperty
    def PS(cls):
        return cls("ps")
    
    @schemas.classproperty
    def OI(cls):
        return cls("oi")
    
    @schemas.classproperty
    def OM(cls):
        return cls("om")
    
    @schemas.classproperty
    def OP(cls):
        return cls("op")
    
    @schemas.classproperty
    def TRUE(cls):
        return cls("true")
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
_auth = [
    'JWT',
    'Key',
    'Project',
    'Session',
]


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
_status_code_to_response = {
    '200': _response_for_200,
}


class BaseApi(api_client.Api):

    def _get_browser_icon_mapped_args(
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

    async def _aget_browser_icon_oapg(
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
        Get browser icon
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
            path_template='/avatars/browsers/{code}',
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


    def _get_browser_icon_oapg(
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
        Get browser icon
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
            path_template='/avatars/browsers/{code}',
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


class GetBrowserIconRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_browser_icon(
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
        args = self._get_browser_icon_mapped_args(
            code=code,
            width=width,
            height=height,
            quality=quality,
        )
        return await self._aget_browser_icon_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_browser_icon(
        self,
        code: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        quality: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_browser_icon_mapped_args(
            code=code,
            width=width,
            height=height,
            quality=quality,
        )
        return self._get_browser_icon_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetBrowserIcon(BaseApi):

    async def aget_browser_icon(
        self,
        code: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        quality: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aget_browser_icon(
            code=code,
            width=width,
            height=height,
            quality=quality,
            **kwargs,
        )
    
    
    def get_browser_icon(
        self,
        code: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        quality: typing.Optional[int] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.get_browser_icon(
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
        args = self._get_browser_icon_mapped_args(
            code=code,
            width=width,
            height=height,
            quality=quality,
        )
        return await self._aget_browser_icon_oapg(
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
        args = self._get_browser_icon_mapped_args(
            code=code,
            width=width,
            height=height,
            quality=quality,
        )
        return self._get_browser_icon_oapg(
            query_params=args.query,
            path_params=args.path,
        )

