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


class GravitySchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def CENTER(cls):
        return cls("center")
    
    @schemas.classproperty
    def TOPLEFT(cls):
        return cls("top-left")
    
    @schemas.classproperty
    def TOP(cls):
        return cls("top")
    
    @schemas.classproperty
    def TOPRIGHT(cls):
        return cls("top-right")
    
    @schemas.classproperty
    def LEFT(cls):
        return cls("left")
    
    @schemas.classproperty
    def RIGHT(cls):
        return cls("right")
    
    @schemas.classproperty
    def BOTTOMLEFT(cls):
        return cls("bottom-left")
    
    @schemas.classproperty
    def BOTTOM(cls):
        return cls("bottom")
    
    @schemas.classproperty
    def BOTTOMRIGHT(cls):
        return cls("bottom-right")
QualitySchema = schemas.Int32Schema
BorderWidthSchema = schemas.Int32Schema
BorderColorSchema = schemas.StrSchema
BorderRadiusSchema = schemas.Int32Schema
OpacitySchema = schemas.Float32Schema
RotationSchema = schemas.Int32Schema
BackgroundSchema = schemas.StrSchema


class OutputSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def JPG(cls):
        return cls("jpg")
    
    @schemas.classproperty
    def JPEG(cls):
        return cls("jpeg")
    
    @schemas.classproperty
    def GIF(cls):
        return cls("gif")
    
    @schemas.classproperty
    def PNG(cls):
        return cls("png")
    
    @schemas.classproperty
    def WEBP(cls):
        return cls("webp")
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
        'gravity': typing.Union[GravitySchema, str, ],
        'quality': typing.Union[QualitySchema, decimal.Decimal, int, ],
        'borderWidth': typing.Union[BorderWidthSchema, decimal.Decimal, int, ],
        'borderColor': typing.Union[BorderColorSchema, str, ],
        'borderRadius': typing.Union[BorderRadiusSchema, decimal.Decimal, int, ],
        'opacity': typing.Union[OpacitySchema, decimal.Decimal, int, float, ],
        'rotation': typing.Union[RotationSchema, decimal.Decimal, int, ],
        'background': typing.Union[BackgroundSchema, str, ],
        'output': typing.Union[OutputSchema, str, ],
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
request_query_gravity = api_client.QueryParameter(
    name="gravity",
    style=api_client.ParameterStyle.FORM,
    schema=GravitySchema,
    explode=True,
)
request_query_quality = api_client.QueryParameter(
    name="quality",
    style=api_client.ParameterStyle.FORM,
    schema=QualitySchema,
    explode=True,
)
request_query_border_width = api_client.QueryParameter(
    name="borderWidth",
    style=api_client.ParameterStyle.FORM,
    schema=BorderWidthSchema,
    explode=True,
)
request_query_border_color = api_client.QueryParameter(
    name="borderColor",
    style=api_client.ParameterStyle.FORM,
    schema=BorderColorSchema,
    explode=True,
)
request_query_border_radius = api_client.QueryParameter(
    name="borderRadius",
    style=api_client.ParameterStyle.FORM,
    schema=BorderRadiusSchema,
    explode=True,
)
request_query_opacity = api_client.QueryParameter(
    name="opacity",
    style=api_client.ParameterStyle.FORM,
    schema=OpacitySchema,
    explode=True,
)
request_query_rotation = api_client.QueryParameter(
    name="rotation",
    style=api_client.ParameterStyle.FORM,
    schema=RotationSchema,
    explode=True,
)
request_query_background = api_client.QueryParameter(
    name="background",
    style=api_client.ParameterStyle.FORM,
    schema=BackgroundSchema,
    explode=True,
)
request_query_output = api_client.QueryParameter(
    name="output",
    style=api_client.ParameterStyle.FORM,
    schema=OutputSchema,
    explode=True,
)
# Path params
BucketIdSchema = schemas.StrSchema
FileIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'bucketId': typing.Union[BucketIdSchema, str, ],
        'fileId': typing.Union[FileIdSchema, str, ],
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


request_path_bucket_id = api_client.PathParameter(
    name="bucketId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=BucketIdSchema,
    required=True,
)
request_path_file_id = api_client.PathParameter(
    name="fileId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FileIdSchema,
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

    def _get_file_preview_image_mapped_args(
        self,
        bucket_id: str,
        file_id: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        gravity: typing.Optional[str] = None,
        quality: typing.Optional[int] = None,
        border_width: typing.Optional[int] = None,
        border_color: typing.Optional[str] = None,
        border_radius: typing.Optional[int] = None,
        opacity: typing.Optional[typing.Union[int, float]] = None,
        rotation: typing.Optional[int] = None,
        background: typing.Optional[str] = None,
        output: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if width is not None:
            _query_params["width"] = width
        if height is not None:
            _query_params["height"] = height
        if gravity is not None:
            _query_params["gravity"] = gravity
        if quality is not None:
            _query_params["quality"] = quality
        if border_width is not None:
            _query_params["borderWidth"] = border_width
        if border_color is not None:
            _query_params["borderColor"] = border_color
        if border_radius is not None:
            _query_params["borderRadius"] = border_radius
        if opacity is not None:
            _query_params["opacity"] = opacity
        if rotation is not None:
            _query_params["rotation"] = rotation
        if background is not None:
            _query_params["background"] = background
        if output is not None:
            _query_params["output"] = output
        if bucket_id is not None:
            _path_params["bucketId"] = bucket_id
        if file_id is not None:
            _path_params["fileId"] = file_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_file_preview_image_oapg(
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
        Get file preview
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_bucket_id,
            request_path_file_id,
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
            request_query_gravity,
            request_query_quality,
            request_query_border_width,
            request_query_border_color,
            request_query_border_radius,
            request_query_opacity,
            request_query_rotation,
            request_query_background,
            request_query_output,
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
            path_template='/storage/buckets/{bucketId}/files/{fileId}/preview',
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


    def _get_file_preview_image_oapg(
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
        Get file preview
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_bucket_id,
            request_path_file_id,
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
            request_query_gravity,
            request_query_quality,
            request_query_border_width,
            request_query_border_color,
            request_query_border_radius,
            request_query_opacity,
            request_query_rotation,
            request_query_background,
            request_query_output,
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
            path_template='/storage/buckets/{bucketId}/files/{fileId}/preview',
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


class GetFilePreviewImageRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_file_preview_image(
        self,
        bucket_id: str,
        file_id: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        gravity: typing.Optional[str] = None,
        quality: typing.Optional[int] = None,
        border_width: typing.Optional[int] = None,
        border_color: typing.Optional[str] = None,
        border_radius: typing.Optional[int] = None,
        opacity: typing.Optional[typing.Union[int, float]] = None,
        rotation: typing.Optional[int] = None,
        background: typing.Optional[str] = None,
        output: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_file_preview_image_mapped_args(
            bucket_id=bucket_id,
            file_id=file_id,
            width=width,
            height=height,
            gravity=gravity,
            quality=quality,
            border_width=border_width,
            border_color=border_color,
            border_radius=border_radius,
            opacity=opacity,
            rotation=rotation,
            background=background,
            output=output,
        )
        return await self._aget_file_preview_image_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_file_preview_image(
        self,
        bucket_id: str,
        file_id: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        gravity: typing.Optional[str] = None,
        quality: typing.Optional[int] = None,
        border_width: typing.Optional[int] = None,
        border_color: typing.Optional[str] = None,
        border_radius: typing.Optional[int] = None,
        opacity: typing.Optional[typing.Union[int, float]] = None,
        rotation: typing.Optional[int] = None,
        background: typing.Optional[str] = None,
        output: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_file_preview_image_mapped_args(
            bucket_id=bucket_id,
            file_id=file_id,
            width=width,
            height=height,
            gravity=gravity,
            quality=quality,
            border_width=border_width,
            border_color=border_color,
            border_radius=border_radius,
            opacity=opacity,
            rotation=rotation,
            background=background,
            output=output,
        )
        return self._get_file_preview_image_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetFilePreviewImage(BaseApi):

    async def aget_file_preview_image(
        self,
        bucket_id: str,
        file_id: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        gravity: typing.Optional[str] = None,
        quality: typing.Optional[int] = None,
        border_width: typing.Optional[int] = None,
        border_color: typing.Optional[str] = None,
        border_radius: typing.Optional[int] = None,
        opacity: typing.Optional[typing.Union[int, float]] = None,
        rotation: typing.Optional[int] = None,
        background: typing.Optional[str] = None,
        output: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aget_file_preview_image(
            bucket_id=bucket_id,
            file_id=file_id,
            width=width,
            height=height,
            gravity=gravity,
            quality=quality,
            border_width=border_width,
            border_color=border_color,
            border_radius=border_radius,
            opacity=opacity,
            rotation=rotation,
            background=background,
            output=output,
            **kwargs,
        )
    
    
    def get_file_preview_image(
        self,
        bucket_id: str,
        file_id: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        gravity: typing.Optional[str] = None,
        quality: typing.Optional[int] = None,
        border_width: typing.Optional[int] = None,
        border_color: typing.Optional[str] = None,
        border_radius: typing.Optional[int] = None,
        opacity: typing.Optional[typing.Union[int, float]] = None,
        rotation: typing.Optional[int] = None,
        background: typing.Optional[str] = None,
        output: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.get_file_preview_image(
            bucket_id=bucket_id,
            file_id=file_id,
            width=width,
            height=height,
            gravity=gravity,
            quality=quality,
            border_width=border_width,
            border_color=border_color,
            border_radius=border_radius,
            opacity=opacity,
            rotation=rotation,
            background=background,
            output=output,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        bucket_id: str,
        file_id: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        gravity: typing.Optional[str] = None,
        quality: typing.Optional[int] = None,
        border_width: typing.Optional[int] = None,
        border_color: typing.Optional[str] = None,
        border_radius: typing.Optional[int] = None,
        opacity: typing.Optional[typing.Union[int, float]] = None,
        rotation: typing.Optional[int] = None,
        background: typing.Optional[str] = None,
        output: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_file_preview_image_mapped_args(
            bucket_id=bucket_id,
            file_id=file_id,
            width=width,
            height=height,
            gravity=gravity,
            quality=quality,
            border_width=border_width,
            border_color=border_color,
            border_radius=border_radius,
            opacity=opacity,
            rotation=rotation,
            background=background,
            output=output,
        )
        return await self._aget_file_preview_image_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        bucket_id: str,
        file_id: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        gravity: typing.Optional[str] = None,
        quality: typing.Optional[int] = None,
        border_width: typing.Optional[int] = None,
        border_color: typing.Optional[str] = None,
        border_radius: typing.Optional[int] = None,
        opacity: typing.Optional[typing.Union[int, float]] = None,
        rotation: typing.Optional[int] = None,
        background: typing.Optional[str] = None,
        output: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_file_preview_image_mapped_args(
            bucket_id=bucket_id,
            file_id=file_id,
            width=width,
            height=height,
            gravity=gravity,
            quality=quality,
            border_width=border_width,
            border_color=border_color,
            border_radius=border_radius,
            opacity=opacity,
            rotation=rotation,
            background=background,
            output=output,
        )
        return self._get_file_preview_image_oapg(
            query_params=args.query,
            path_params=args.path,
        )

