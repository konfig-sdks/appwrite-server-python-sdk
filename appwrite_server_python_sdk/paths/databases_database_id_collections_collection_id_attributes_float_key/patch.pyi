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

from appwrite_server_python_sdk.model.attribute_float import AttributeFloat as AttributeFloatSchema
from appwrite_server_python_sdk.model.databases_update_float_attribute_request import DatabasesUpdateFloatAttributeRequest as DatabasesUpdateFloatAttributeRequestSchema

from appwrite_server_python_sdk.type.attribute_float import AttributeFloat
from appwrite_server_python_sdk.type.databases_update_float_attribute_request import DatabasesUpdateFloatAttributeRequest

from ...api_client import Dictionary
from appwrite_server_python_sdk.pydantic.databases_update_float_attribute_request import DatabasesUpdateFloatAttributeRequest as DatabasesUpdateFloatAttributeRequestPydantic
from appwrite_server_python_sdk.pydantic.attribute_float import AttributeFloat as AttributeFloatPydantic

# Path params
DatabaseIdSchema = schemas.StrSchema
CollectionIdSchema = schemas.StrSchema
KeySchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'databaseId': typing.Union[DatabaseIdSchema, str, ],
        'collectionId': typing.Union[CollectionIdSchema, str, ],
        'key': typing.Union[KeySchema, str, ],
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


request_path_database_id = api_client.PathParameter(
    name="databaseId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=DatabaseIdSchema,
    required=True,
)
request_path_collection_id = api_client.PathParameter(
    name="collectionId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CollectionIdSchema,
    required=True,
)
request_path_key = api_client.PathParameter(
    name="key",
    style=api_client.ParameterStyle.SIMPLE,
    schema=KeySchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = DatabasesUpdateFloatAttributeRequestSchema


request_body_databases_update_float_attribute_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBody = AttributeFloatSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AttributeFloat


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AttributeFloat


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        '': api_client.MediaType(
            schema=SchemaFor200ResponseBody),
    },
)
_all_accept_content_types = (
    '',
)


class BaseApi(api_client.Api):

    def _update_float_attribute_mapped_args(
        self,
        required: bool,
        min: typing.Union[int, float],
        max: typing.Union[int, float],
        default: typing.Optional[typing.Union[int, float]],
        database_id: str,
        collection_id: str,
        key: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if required is not None:
            _body["required"] = required
        if min is not None:
            _body["min"] = min
        if max is not None:
            _body["max"] = max
        if default is not None:
            _body["default"] = default
        args.body = _body
        if database_id is not None:
            _path_params["databaseId"] = database_id
        if collection_id is not None:
            _path_params["collectionId"] = collection_id
        if key is not None:
            _path_params["key"] = key
        args.path = _path_params
        return args

    async def _aupdate_float_attribute_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update float attribute
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_database_id,
            request_path_collection_id,
            request_path_key,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/databases/{databaseId}/collections/{collectionId}/attributes/float/{key}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_databases_update_float_attribute_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _update_float_attribute_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update float attribute
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_database_id,
            request_path_collection_id,
            request_path_key,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/databases/{databaseId}/collections/{collectionId}/attributes/float/{key}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_databases_update_float_attribute_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class UpdateFloatAttributeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_float_attribute(
        self,
        required: bool,
        min: typing.Union[int, float],
        max: typing.Union[int, float],
        default: typing.Optional[typing.Union[int, float]],
        database_id: str,
        collection_id: str,
        key: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_float_attribute_mapped_args(
            required=required,
            min=min,
            max=max,
            default=default,
            database_id=database_id,
            collection_id=collection_id,
            key=key,
        )
        return await self._aupdate_float_attribute_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_float_attribute(
        self,
        required: bool,
        min: typing.Union[int, float],
        max: typing.Union[int, float],
        default: typing.Optional[typing.Union[int, float]],
        database_id: str,
        collection_id: str,
        key: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_float_attribute_mapped_args(
            required=required,
            min=min,
            max=max,
            default=default,
            database_id=database_id,
            collection_id=collection_id,
            key=key,
        )
        return self._update_float_attribute_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateFloatAttribute(BaseApi):

    async def aupdate_float_attribute(
        self,
        required: bool,
        min: typing.Union[int, float],
        max: typing.Union[int, float],
        default: typing.Optional[typing.Union[int, float]],
        database_id: str,
        collection_id: str,
        key: str,
        validate: bool = False,
        **kwargs,
    ) -> AttributeFloatPydantic:
        raw_response = await self.raw.aupdate_float_attribute(
            required=required,
            min=min,
            max=max,
            default=default,
            database_id=database_id,
            collection_id=collection_id,
            key=key,
            **kwargs,
        )
        if validate:
            return AttributeFloatPydantic(**raw_response.body)
        return api_client.construct_model_instance(AttributeFloatPydantic, raw_response.body)
    
    
    def update_float_attribute(
        self,
        required: bool,
        min: typing.Union[int, float],
        max: typing.Union[int, float],
        default: typing.Optional[typing.Union[int, float]],
        database_id: str,
        collection_id: str,
        key: str,
        validate: bool = False,
    ) -> AttributeFloatPydantic:
        raw_response = self.raw.update_float_attribute(
            required=required,
            min=min,
            max=max,
            default=default,
            database_id=database_id,
            collection_id=collection_id,
            key=key,
        )
        if validate:
            return AttributeFloatPydantic(**raw_response.body)
        return api_client.construct_model_instance(AttributeFloatPydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        required: bool,
        min: typing.Union[int, float],
        max: typing.Union[int, float],
        default: typing.Optional[typing.Union[int, float]],
        database_id: str,
        collection_id: str,
        key: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_float_attribute_mapped_args(
            required=required,
            min=min,
            max=max,
            default=default,
            database_id=database_id,
            collection_id=collection_id,
            key=key,
        )
        return await self._aupdate_float_attribute_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        required: bool,
        min: typing.Union[int, float],
        max: typing.Union[int, float],
        default: typing.Optional[typing.Union[int, float]],
        database_id: str,
        collection_id: str,
        key: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_float_attribute_mapped_args(
            required=required,
            min=min,
            max=max,
            default=default,
            database_id=database_id,
            collection_id=collection_id,
            key=key,
        )
        return self._update_float_attribute_oapg(
            body=args.body,
            path_params=args.path,
        )

