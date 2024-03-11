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

from appwrite_server_python_sdk.model.messaging_update_push_notification_request import MessagingUpdatePushNotificationRequest as MessagingUpdatePushNotificationRequestSchema
from appwrite_server_python_sdk.model.messaging_update_push_notification_request_users import MessagingUpdatePushNotificationRequestUsers as MessagingUpdatePushNotificationRequestUsersSchema
from appwrite_server_python_sdk.model.messaging_update_push_notification_request_targets import MessagingUpdatePushNotificationRequestTargets as MessagingUpdatePushNotificationRequestTargetsSchema
from appwrite_server_python_sdk.model.messaging_update_push_notification_request_topics import MessagingUpdatePushNotificationRequestTopics as MessagingUpdatePushNotificationRequestTopicsSchema
from appwrite_server_python_sdk.model.message import Message as MessageSchema

from appwrite_server_python_sdk.type.messaging_update_push_notification_request_users import MessagingUpdatePushNotificationRequestUsers
from appwrite_server_python_sdk.type.messaging_update_push_notification_request_topics import MessagingUpdatePushNotificationRequestTopics
from appwrite_server_python_sdk.type.message import Message
from appwrite_server_python_sdk.type.messaging_update_push_notification_request import MessagingUpdatePushNotificationRequest
from appwrite_server_python_sdk.type.messaging_update_push_notification_request_targets import MessagingUpdatePushNotificationRequestTargets

from ...api_client import Dictionary
from appwrite_server_python_sdk.pydantic.message import Message as MessagePydantic
from appwrite_server_python_sdk.pydantic.messaging_update_push_notification_request import MessagingUpdatePushNotificationRequest as MessagingUpdatePushNotificationRequestPydantic
from appwrite_server_python_sdk.pydantic.messaging_update_push_notification_request_targets import MessagingUpdatePushNotificationRequestTargets as MessagingUpdatePushNotificationRequestTargetsPydantic
from appwrite_server_python_sdk.pydantic.messaging_update_push_notification_request_topics import MessagingUpdatePushNotificationRequestTopics as MessagingUpdatePushNotificationRequestTopicsPydantic
from appwrite_server_python_sdk.pydantic.messaging_update_push_notification_request_users import MessagingUpdatePushNotificationRequestUsers as MessagingUpdatePushNotificationRequestUsersPydantic

from . import path

# Path params
MessageIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'messageId': typing.Union[MessageIdSchema, str, ],
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


request_path_message_id = api_client.PathParameter(
    name="messageId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=MessageIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = MessagingUpdatePushNotificationRequestSchema


request_body_messaging_update_push_notification_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'Key',
    'Project',
]
SchemaFor200ResponseBodyApplicationJson = MessageSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Message


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Message


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_push_notification_mapped_args(
        self,
        message_id: str,
        title: typing.Optional[str] = None,
        topics: typing.Optional[MessagingUpdatePushNotificationRequestTopics] = None,
        users: typing.Optional[MessagingUpdatePushNotificationRequestUsers] = None,
        targets: typing.Optional[MessagingUpdatePushNotificationRequestTargets] = None,
        body: typing.Optional[str] = None,
        data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        action: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        icon: typing.Optional[str] = None,
        sound: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        badge: typing.Optional[int] = None,
        draft: typing.Optional[bool] = None,
        scheduled_at: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if title is not None:
            _body["title"] = title
        if topics is not None:
            _body["topics"] = topics
        if users is not None:
            _body["users"] = users
        if targets is not None:
            _body["targets"] = targets
        if body is not None:
            _body["body"] = body
        if data is not None:
            _body["data"] = data
        if action is not None:
            _body["action"] = action
        if image is not None:
            _body["image"] = image
        if icon is not None:
            _body["icon"] = icon
        if sound is not None:
            _body["sound"] = sound
        if color is not None:
            _body["color"] = color
        if tag is not None:
            _body["tag"] = tag
        if badge is not None:
            _body["badge"] = badge
        if draft is not None:
            _body["draft"] = draft
        if scheduled_at is not None:
            _body["scheduledAt"] = scheduled_at
        args.body = _body
        if message_id is not None:
            _path_params["messageId"] = message_id
        args.path = _path_params
        return args

    async def _aupdate_push_notification_oapg(
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
        Update push notification
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_message_id,
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
            path_template='/messaging/messages/push/{messageId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_messaging_update_push_notification_request.serialize(body, content_type)
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


    def _update_push_notification_oapg(
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
        Update push notification
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_message_id,
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
            path_template='/messaging/messages/push/{messageId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_messaging_update_push_notification_request.serialize(body, content_type)
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


class UpdatePushNotificationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_push_notification(
        self,
        message_id: str,
        title: typing.Optional[str] = None,
        topics: typing.Optional[MessagingUpdatePushNotificationRequestTopics] = None,
        users: typing.Optional[MessagingUpdatePushNotificationRequestUsers] = None,
        targets: typing.Optional[MessagingUpdatePushNotificationRequestTargets] = None,
        body: typing.Optional[str] = None,
        data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        action: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        icon: typing.Optional[str] = None,
        sound: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        badge: typing.Optional[int] = None,
        draft: typing.Optional[bool] = None,
        scheduled_at: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_push_notification_mapped_args(
            message_id=message_id,
            title=title,
            topics=topics,
            users=users,
            targets=targets,
            body=body,
            data=data,
            action=action,
            image=image,
            icon=icon,
            sound=sound,
            color=color,
            tag=tag,
            badge=badge,
            draft=draft,
            scheduled_at=scheduled_at,
        )
        return await self._aupdate_push_notification_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_push_notification(
        self,
        message_id: str,
        title: typing.Optional[str] = None,
        topics: typing.Optional[MessagingUpdatePushNotificationRequestTopics] = None,
        users: typing.Optional[MessagingUpdatePushNotificationRequestUsers] = None,
        targets: typing.Optional[MessagingUpdatePushNotificationRequestTargets] = None,
        body: typing.Optional[str] = None,
        data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        action: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        icon: typing.Optional[str] = None,
        sound: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        badge: typing.Optional[int] = None,
        draft: typing.Optional[bool] = None,
        scheduled_at: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_push_notification_mapped_args(
            message_id=message_id,
            title=title,
            topics=topics,
            users=users,
            targets=targets,
            body=body,
            data=data,
            action=action,
            image=image,
            icon=icon,
            sound=sound,
            color=color,
            tag=tag,
            badge=badge,
            draft=draft,
            scheduled_at=scheduled_at,
        )
        return self._update_push_notification_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdatePushNotification(BaseApi):

    async def aupdate_push_notification(
        self,
        message_id: str,
        title: typing.Optional[str] = None,
        topics: typing.Optional[MessagingUpdatePushNotificationRequestTopics] = None,
        users: typing.Optional[MessagingUpdatePushNotificationRequestUsers] = None,
        targets: typing.Optional[MessagingUpdatePushNotificationRequestTargets] = None,
        body: typing.Optional[str] = None,
        data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        action: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        icon: typing.Optional[str] = None,
        sound: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        badge: typing.Optional[int] = None,
        draft: typing.Optional[bool] = None,
        scheduled_at: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> MessagePydantic:
        raw_response = await self.raw.aupdate_push_notification(
            message_id=message_id,
            title=title,
            topics=topics,
            users=users,
            targets=targets,
            body=body,
            data=data,
            action=action,
            image=image,
            icon=icon,
            sound=sound,
            color=color,
            tag=tag,
            badge=badge,
            draft=draft,
            scheduled_at=scheduled_at,
            **kwargs,
        )
        if validate:
            return MessagePydantic(**raw_response.body)
        return api_client.construct_model_instance(MessagePydantic, raw_response.body)
    
    
    def update_push_notification(
        self,
        message_id: str,
        title: typing.Optional[str] = None,
        topics: typing.Optional[MessagingUpdatePushNotificationRequestTopics] = None,
        users: typing.Optional[MessagingUpdatePushNotificationRequestUsers] = None,
        targets: typing.Optional[MessagingUpdatePushNotificationRequestTargets] = None,
        body: typing.Optional[str] = None,
        data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        action: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        icon: typing.Optional[str] = None,
        sound: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        badge: typing.Optional[int] = None,
        draft: typing.Optional[bool] = None,
        scheduled_at: typing.Optional[str] = None,
        validate: bool = False,
    ) -> MessagePydantic:
        raw_response = self.raw.update_push_notification(
            message_id=message_id,
            title=title,
            topics=topics,
            users=users,
            targets=targets,
            body=body,
            data=data,
            action=action,
            image=image,
            icon=icon,
            sound=sound,
            color=color,
            tag=tag,
            badge=badge,
            draft=draft,
            scheduled_at=scheduled_at,
        )
        if validate:
            return MessagePydantic(**raw_response.body)
        return api_client.construct_model_instance(MessagePydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        message_id: str,
        title: typing.Optional[str] = None,
        topics: typing.Optional[MessagingUpdatePushNotificationRequestTopics] = None,
        users: typing.Optional[MessagingUpdatePushNotificationRequestUsers] = None,
        targets: typing.Optional[MessagingUpdatePushNotificationRequestTargets] = None,
        body: typing.Optional[str] = None,
        data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        action: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        icon: typing.Optional[str] = None,
        sound: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        badge: typing.Optional[int] = None,
        draft: typing.Optional[bool] = None,
        scheduled_at: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_push_notification_mapped_args(
            message_id=message_id,
            title=title,
            topics=topics,
            users=users,
            targets=targets,
            body=body,
            data=data,
            action=action,
            image=image,
            icon=icon,
            sound=sound,
            color=color,
            tag=tag,
            badge=badge,
            draft=draft,
            scheduled_at=scheduled_at,
        )
        return await self._aupdate_push_notification_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        message_id: str,
        title: typing.Optional[str] = None,
        topics: typing.Optional[MessagingUpdatePushNotificationRequestTopics] = None,
        users: typing.Optional[MessagingUpdatePushNotificationRequestUsers] = None,
        targets: typing.Optional[MessagingUpdatePushNotificationRequestTargets] = None,
        body: typing.Optional[str] = None,
        data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        action: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        icon: typing.Optional[str] = None,
        sound: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        badge: typing.Optional[int] = None,
        draft: typing.Optional[bool] = None,
        scheduled_at: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_push_notification_mapped_args(
            message_id=message_id,
            title=title,
            topics=topics,
            users=users,
            targets=targets,
            body=body,
            data=data,
            action=action,
            image=image,
            icon=icon,
            sound=sound,
            color=color,
            tag=tag,
            badge=badge,
            draft=draft,
            scheduled_at=scheduled_at,
        )
        return self._update_push_notification_oapg(
            body=args.body,
            path_params=args.path,
        )

