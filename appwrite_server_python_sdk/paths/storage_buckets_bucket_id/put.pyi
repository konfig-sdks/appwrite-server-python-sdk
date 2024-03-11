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

from appwrite_server_python_sdk.model.bucket import Bucket as BucketSchema
from appwrite_server_python_sdk.model.storage_update_bucket_by_id_request_permissions import StorageUpdateBucketByIdRequestPermissions as StorageUpdateBucketByIdRequestPermissionsSchema
from appwrite_server_python_sdk.model.storage_update_bucket_by_id_request import StorageUpdateBucketByIdRequest as StorageUpdateBucketByIdRequestSchema
from appwrite_server_python_sdk.model.storage_update_bucket_by_id_request_allowed_file_extensions import StorageUpdateBucketByIdRequestAllowedFileExtensions as StorageUpdateBucketByIdRequestAllowedFileExtensionsSchema

from appwrite_server_python_sdk.type.storage_update_bucket_by_id_request_permissions import StorageUpdateBucketByIdRequestPermissions
from appwrite_server_python_sdk.type.storage_update_bucket_by_id_request_allowed_file_extensions import StorageUpdateBucketByIdRequestAllowedFileExtensions
from appwrite_server_python_sdk.type.bucket import Bucket
from appwrite_server_python_sdk.type.storage_update_bucket_by_id_request import StorageUpdateBucketByIdRequest

from ...api_client import Dictionary
from appwrite_server_python_sdk.pydantic.storage_update_bucket_by_id_request import StorageUpdateBucketByIdRequest as StorageUpdateBucketByIdRequestPydantic
from appwrite_server_python_sdk.pydantic.storage_update_bucket_by_id_request_allowed_file_extensions import StorageUpdateBucketByIdRequestAllowedFileExtensions as StorageUpdateBucketByIdRequestAllowedFileExtensionsPydantic
from appwrite_server_python_sdk.pydantic.bucket import Bucket as BucketPydantic
from appwrite_server_python_sdk.pydantic.storage_update_bucket_by_id_request_permissions import StorageUpdateBucketByIdRequestPermissions as StorageUpdateBucketByIdRequestPermissionsPydantic

# Path params
BucketIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'bucketId': typing.Union[BucketIdSchema, str, ],
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
# body param
SchemaForRequestBodyApplicationJson = StorageUpdateBucketByIdRequestSchema


request_body_storage_update_bucket_by_id_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = BucketSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Bucket


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Bucket


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_bucket_by_id_mapped_args(
        self,
        name: str,
        bucket_id: str,
        permissions: typing.Optional[StorageUpdateBucketByIdRequestPermissions] = None,
        file_security: typing.Optional[bool] = None,
        enabled: typing.Optional[bool] = None,
        maximum_file_size: typing.Optional[int] = None,
        allowed_file_extensions: typing.Optional[StorageUpdateBucketByIdRequestAllowedFileExtensions] = None,
        compression: typing.Optional[str] = None,
        encryption: typing.Optional[bool] = None,
        antivirus: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if name is not None:
            _body["name"] = name
        if permissions is not None:
            _body["permissions"] = permissions
        if file_security is not None:
            _body["fileSecurity"] = file_security
        if enabled is not None:
            _body["enabled"] = enabled
        if maximum_file_size is not None:
            _body["maximumFileSize"] = maximum_file_size
        if allowed_file_extensions is not None:
            _body["allowedFileExtensions"] = allowed_file_extensions
        if compression is not None:
            _body["compression"] = compression
        if encryption is not None:
            _body["encryption"] = encryption
        if antivirus is not None:
            _body["antivirus"] = antivirus
        args.body = _body
        if bucket_id is not None:
            _path_params["bucketId"] = bucket_id
        args.path = _path_params
        return args

    async def _aupdate_bucket_by_id_oapg(
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
        Update bucket
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_bucket_id,
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
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/storage/buckets/{bucketId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_storage_update_bucket_by_id_request.serialize(body, content_type)
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


    def _update_bucket_by_id_oapg(
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
        Update bucket
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_bucket_id,
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
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/storage/buckets/{bucketId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_storage_update_bucket_by_id_request.serialize(body, content_type)
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


class UpdateBucketByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_bucket_by_id(
        self,
        name: str,
        bucket_id: str,
        permissions: typing.Optional[StorageUpdateBucketByIdRequestPermissions] = None,
        file_security: typing.Optional[bool] = None,
        enabled: typing.Optional[bool] = None,
        maximum_file_size: typing.Optional[int] = None,
        allowed_file_extensions: typing.Optional[StorageUpdateBucketByIdRequestAllowedFileExtensions] = None,
        compression: typing.Optional[str] = None,
        encryption: typing.Optional[bool] = None,
        antivirus: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_bucket_by_id_mapped_args(
            name=name,
            bucket_id=bucket_id,
            permissions=permissions,
            file_security=file_security,
            enabled=enabled,
            maximum_file_size=maximum_file_size,
            allowed_file_extensions=allowed_file_extensions,
            compression=compression,
            encryption=encryption,
            antivirus=antivirus,
        )
        return await self._aupdate_bucket_by_id_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_bucket_by_id(
        self,
        name: str,
        bucket_id: str,
        permissions: typing.Optional[StorageUpdateBucketByIdRequestPermissions] = None,
        file_security: typing.Optional[bool] = None,
        enabled: typing.Optional[bool] = None,
        maximum_file_size: typing.Optional[int] = None,
        allowed_file_extensions: typing.Optional[StorageUpdateBucketByIdRequestAllowedFileExtensions] = None,
        compression: typing.Optional[str] = None,
        encryption: typing.Optional[bool] = None,
        antivirus: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_bucket_by_id_mapped_args(
            name=name,
            bucket_id=bucket_id,
            permissions=permissions,
            file_security=file_security,
            enabled=enabled,
            maximum_file_size=maximum_file_size,
            allowed_file_extensions=allowed_file_extensions,
            compression=compression,
            encryption=encryption,
            antivirus=antivirus,
        )
        return self._update_bucket_by_id_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateBucketById(BaseApi):

    async def aupdate_bucket_by_id(
        self,
        name: str,
        bucket_id: str,
        permissions: typing.Optional[StorageUpdateBucketByIdRequestPermissions] = None,
        file_security: typing.Optional[bool] = None,
        enabled: typing.Optional[bool] = None,
        maximum_file_size: typing.Optional[int] = None,
        allowed_file_extensions: typing.Optional[StorageUpdateBucketByIdRequestAllowedFileExtensions] = None,
        compression: typing.Optional[str] = None,
        encryption: typing.Optional[bool] = None,
        antivirus: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> BucketPydantic:
        raw_response = await self.raw.aupdate_bucket_by_id(
            name=name,
            bucket_id=bucket_id,
            permissions=permissions,
            file_security=file_security,
            enabled=enabled,
            maximum_file_size=maximum_file_size,
            allowed_file_extensions=allowed_file_extensions,
            compression=compression,
            encryption=encryption,
            antivirus=antivirus,
            **kwargs,
        )
        if validate:
            return BucketPydantic(**raw_response.body)
        return api_client.construct_model_instance(BucketPydantic, raw_response.body)
    
    
    def update_bucket_by_id(
        self,
        name: str,
        bucket_id: str,
        permissions: typing.Optional[StorageUpdateBucketByIdRequestPermissions] = None,
        file_security: typing.Optional[bool] = None,
        enabled: typing.Optional[bool] = None,
        maximum_file_size: typing.Optional[int] = None,
        allowed_file_extensions: typing.Optional[StorageUpdateBucketByIdRequestAllowedFileExtensions] = None,
        compression: typing.Optional[str] = None,
        encryption: typing.Optional[bool] = None,
        antivirus: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> BucketPydantic:
        raw_response = self.raw.update_bucket_by_id(
            name=name,
            bucket_id=bucket_id,
            permissions=permissions,
            file_security=file_security,
            enabled=enabled,
            maximum_file_size=maximum_file_size,
            allowed_file_extensions=allowed_file_extensions,
            compression=compression,
            encryption=encryption,
            antivirus=antivirus,
        )
        if validate:
            return BucketPydantic(**raw_response.body)
        return api_client.construct_model_instance(BucketPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        name: str,
        bucket_id: str,
        permissions: typing.Optional[StorageUpdateBucketByIdRequestPermissions] = None,
        file_security: typing.Optional[bool] = None,
        enabled: typing.Optional[bool] = None,
        maximum_file_size: typing.Optional[int] = None,
        allowed_file_extensions: typing.Optional[StorageUpdateBucketByIdRequestAllowedFileExtensions] = None,
        compression: typing.Optional[str] = None,
        encryption: typing.Optional[bool] = None,
        antivirus: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_bucket_by_id_mapped_args(
            name=name,
            bucket_id=bucket_id,
            permissions=permissions,
            file_security=file_security,
            enabled=enabled,
            maximum_file_size=maximum_file_size,
            allowed_file_extensions=allowed_file_extensions,
            compression=compression,
            encryption=encryption,
            antivirus=antivirus,
        )
        return await self._aupdate_bucket_by_id_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        name: str,
        bucket_id: str,
        permissions: typing.Optional[StorageUpdateBucketByIdRequestPermissions] = None,
        file_security: typing.Optional[bool] = None,
        enabled: typing.Optional[bool] = None,
        maximum_file_size: typing.Optional[int] = None,
        allowed_file_extensions: typing.Optional[StorageUpdateBucketByIdRequestAllowedFileExtensions] = None,
        compression: typing.Optional[str] = None,
        encryption: typing.Optional[bool] = None,
        antivirus: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_bucket_by_id_mapped_args(
            name=name,
            bucket_id=bucket_id,
            permissions=permissions,
            file_security=file_security,
            enabled=enabled,
            maximum_file_size=maximum_file_size,
            allowed_file_extensions=allowed_file_extensions,
            compression=compression,
            encryption=encryption,
            antivirus=antivirus,
        )
        return self._update_bucket_by_id_oapg(
            body=args.body,
            path_params=args.path,
        )

