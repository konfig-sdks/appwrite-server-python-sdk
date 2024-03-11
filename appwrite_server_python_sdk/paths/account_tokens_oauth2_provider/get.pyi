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
SuccessSchema = schemas.StrSchema
FailureSchema = schemas.StrSchema


class ScopesSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ScopesSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'success': typing.Union[SuccessSchema, str, ],
        'failure': typing.Union[FailureSchema, str, ],
        'scopes': typing.Union[ScopesSchema, list, tuple, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_success = api_client.QueryParameter(
    name="success",
    style=api_client.ParameterStyle.FORM,
    schema=SuccessSchema,
    explode=True,
)
request_query_failure = api_client.QueryParameter(
    name="failure",
    style=api_client.ParameterStyle.FORM,
    schema=FailureSchema,
    explode=True,
)
request_query_scopes = api_client.QueryParameter(
    name="scopes",
    style=api_client.ParameterStyle.FORM,
    schema=ScopesSchema,
    explode=True,
)
# Path params


class ProviderSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def AMAZON(cls):
        return cls("amazon")
    
    @schemas.classproperty
    def APPLE(cls):
        return cls("apple")
    
    @schemas.classproperty
    def AUTH0(cls):
        return cls("auth0")
    
    @schemas.classproperty
    def AUTHENTIK(cls):
        return cls("authentik")
    
    @schemas.classproperty
    def AUTODESK(cls):
        return cls("autodesk")
    
    @schemas.classproperty
    def BITBUCKET(cls):
        return cls("bitbucket")
    
    @schemas.classproperty
    def BITLY(cls):
        return cls("bitly")
    
    @schemas.classproperty
    def BOX(cls):
        return cls("box")
    
    @schemas.classproperty
    def DAILYMOTION(cls):
        return cls("dailymotion")
    
    @schemas.classproperty
    def DISCORD(cls):
        return cls("discord")
    
    @schemas.classproperty
    def DISQUS(cls):
        return cls("disqus")
    
    @schemas.classproperty
    def DROPBOX(cls):
        return cls("dropbox")
    
    @schemas.classproperty
    def ETSY(cls):
        return cls("etsy")
    
    @schemas.classproperty
    def FACEBOOK(cls):
        return cls("facebook")
    
    @schemas.classproperty
    def GITHUB(cls):
        return cls("github")
    
    @schemas.classproperty
    def GITLAB(cls):
        return cls("gitlab")
    
    @schemas.classproperty
    def GOOGLE(cls):
        return cls("google")
    
    @schemas.classproperty
    def LINKEDIN(cls):
        return cls("linkedin")
    
    @schemas.classproperty
    def MICROSOFT(cls):
        return cls("microsoft")
    
    @schemas.classproperty
    def NOTION(cls):
        return cls("notion")
    
    @schemas.classproperty
    def OIDC(cls):
        return cls("oidc")
    
    @schemas.classproperty
    def OKTA(cls):
        return cls("okta")
    
    @schemas.classproperty
    def PAYPAL(cls):
        return cls("paypal")
    
    @schemas.classproperty
    def PAYPAL_SANDBOX(cls):
        return cls("paypalSandbox")
    
    @schemas.classproperty
    def PODIO(cls):
        return cls("podio")
    
    @schemas.classproperty
    def SALESFORCE(cls):
        return cls("salesforce")
    
    @schemas.classproperty
    def SLACK(cls):
        return cls("slack")
    
    @schemas.classproperty
    def SPOTIFY(cls):
        return cls("spotify")
    
    @schemas.classproperty
    def STRIPE(cls):
        return cls("stripe")
    
    @schemas.classproperty
    def TRADESHIFT(cls):
        return cls("tradeshift")
    
    @schemas.classproperty
    def TRADESHIFT_BOX(cls):
        return cls("tradeshiftBox")
    
    @schemas.classproperty
    def TWITCH(cls):
        return cls("twitch")
    
    @schemas.classproperty
    def WORDPRESS(cls):
        return cls("wordpress")
    
    @schemas.classproperty
    def YAHOO(cls):
        return cls("yahoo")
    
    @schemas.classproperty
    def YAMMER(cls):
        return cls("yammer")
    
    @schemas.classproperty
    def YANDEX(cls):
        return cls("yandex")
    
    @schemas.classproperty
    def ZOHO(cls):
        return cls("zoho")
    
    @schemas.classproperty
    def ZOOM(cls):
        return cls("zoom")
    
    @schemas.classproperty
    def MOCK(cls):
        return cls("mock")
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'provider': typing.Union[ProviderSchema, str, ],
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


request_path_provider = api_client.PathParameter(
    name="provider",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ProviderSchema,
    required=True,
)


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
)


class BaseApi(api_client.Api):

    def _create_o_auth2_token_mapped_args(
        self,
        provider: str,
        success: typing.Optional[str] = None,
        failure: typing.Optional[str] = None,
        scopes: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if success is not None:
            _query_params["success"] = success
        if failure is not None:
            _query_params["failure"] = failure
        if scopes is not None:
            _query_params["scopes"] = scopes
        if provider is not None:
            _path_params["provider"] = provider
        args.query = _query_params
        args.path = _path_params
        return args

    async def _acreate_o_auth2_token_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create OAuth2 token
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_provider,
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
            request_query_success,
            request_query_failure,
            request_query_scopes,
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
            path_template='/account/tokens/oauth2/{provider}',
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
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
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


    def _create_o_auth2_token_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create OAuth2 token
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_provider,
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
            request_query_success,
            request_query_failure,
            request_query_scopes,
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
            path_template='/account/tokens/oauth2/{provider}',
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
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateOAuth2TokenRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_o_auth2_token(
        self,
        provider: str,
        success: typing.Optional[str] = None,
        failure: typing.Optional[str] = None,
        scopes: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_o_auth2_token_mapped_args(
            provider=provider,
            success=success,
            failure=failure,
            scopes=scopes,
        )
        return await self._acreate_o_auth2_token_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def create_o_auth2_token(
        self,
        provider: str,
        success: typing.Optional[str] = None,
        failure: typing.Optional[str] = None,
        scopes: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_o_auth2_token_mapped_args(
            provider=provider,
            success=success,
            failure=failure,
            scopes=scopes,
        )
        return self._create_o_auth2_token_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class CreateOAuth2Token(BaseApi):

    async def acreate_o_auth2_token(
        self,
        provider: str,
        success: typing.Optional[str] = None,
        failure: typing.Optional[str] = None,
        scopes: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.acreate_o_auth2_token(
            provider=provider,
            success=success,
            failure=failure,
            scopes=scopes,
            **kwargs,
        )
    
    
    def create_o_auth2_token(
        self,
        provider: str,
        success: typing.Optional[str] = None,
        failure: typing.Optional[str] = None,
        scopes: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.create_o_auth2_token(
            provider=provider,
            success=success,
            failure=failure,
            scopes=scopes,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        provider: str,
        success: typing.Optional[str] = None,
        failure: typing.Optional[str] = None,
        scopes: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_o_auth2_token_mapped_args(
            provider=provider,
            success=success,
            failure=failure,
            scopes=scopes,
        )
        return await self._acreate_o_auth2_token_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        provider: str,
        success: typing.Optional[str] = None,
        failure: typing.Optional[str] = None,
        scopes: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_o_auth2_token_mapped_args(
            provider=provider,
            success=success,
            failure=failure,
            scopes=scopes,
        )
        return self._create_o_auth2_token_oapg(
            query_params=args.query,
            path_params=args.path,
        )

