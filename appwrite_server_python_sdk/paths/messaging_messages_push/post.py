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

from appwrite_server_python_sdk.model.messaging_create_push_notification_request_targets import MessagingCreatePushNotificationRequestTargets as MessagingCreatePushNotificationRequestTargetsSchema
from appwrite_server_python_sdk.model.messaging_create_push_notification_request_users import MessagingCreatePushNotificationRequestUsers as MessagingCreatePushNotificationRequestUsersSchema
from appwrite_server_python_sdk.model.messaging_create_push_notification_request_topics import MessagingCreatePushNotificationRequestTopics as MessagingCreatePushNotificationRequestTopicsSchema
from appwrite_server_python_sdk.model.message import Message as MessageSchema
from appwrite_server_python_sdk.model.messaging_create_push_notification_request import MessagingCreatePushNotificationRequest as MessagingCreatePushNotificationRequestSchema

from appwrite_server_python_sdk.type.messaging_create_push_notification_request_targets import MessagingCreatePushNotificationRequestTargets
from appwrite_server_python_sdk.type.messaging_create_push_notification_request_topics import MessagingCreatePushNotificationRequestTopics
from appwrite_server_python_sdk.type.messaging_create_push_notification_request import MessagingCreatePushNotificationRequest
from appwrite_server_python_sdk.type.message import Message
from appwrite_server_python_sdk.type.messaging_create_push_notification_request_users import MessagingCreatePushNotificationRequestUsers

from ...api_client import Dictionary
from appwrite_server_python_sdk.pydantic.messaging_create_push_notification_request import MessagingCreatePushNotificationRequest as MessagingCreatePushNotificationRequestPydantic
from appwrite_server_python_sdk.pydantic.message import Message as MessagePydantic
from appwrite_server_python_sdk.pydantic.messaging_create_push_notification_request_users import MessagingCreatePushNotificationRequestUsers as MessagingCreatePushNotificationRequestUsersPydantic
from appwrite_server_python_sdk.pydantic.messaging_create_push_notification_request_targets import MessagingCreatePushNotificationRequestTargets as MessagingCreatePushNotificationRequestTargetsPydantic
from appwrite_server_python_sdk.pydantic.messaging_create_push_notification_request_topics import MessagingCreatePushNotificationRequestTopics as MessagingCreatePushNotificationRequestTopicsPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = MessagingCreatePushNotificationRequestSchema


request_body_messaging_create_push_notification_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'Key',
    'Project',
]
SchemaFor201ResponseBodyApplicationJson = MessageSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Message


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Message


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_push_notification_mapped_args(
        self,
        title: str,
        message_id: str,
        body: str,
        topics: typing.Optional[MessagingCreatePushNotificationRequestTopics] = None,
        users: typing.Optional[MessagingCreatePushNotificationRequestUsers] = None,
        targets: typing.Optional[MessagingCreatePushNotificationRequestTargets] = None,
        data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        action: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        icon: typing.Optional[str] = None,
        sound: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        badge: typing.Optional[str] = None,
        draft: typing.Optional[bool] = None,
        scheduled_at: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if title is not None:
            _body["title"] = title
        if message_id is not None:
            _body["messageId"] = message_id
        if body is not None:
            _body["body"] = body
        if topics is not None:
            _body["topics"] = topics
        if users is not None:
            _body["users"] = users
        if targets is not None:
            _body["targets"] = targets
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
        return args

    async def _acreate_push_notification_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create push notification
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/messaging/messages/push',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_messaging_create_push_notification_request.serialize(body, content_type)
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


    def _create_push_notification_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create push notification
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/messaging/messages/push',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_messaging_create_push_notification_request.serialize(body, content_type)
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


class CreatePushNotificationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_push_notification(
        self,
        title: str,
        message_id: str,
        body: str,
        topics: typing.Optional[MessagingCreatePushNotificationRequestTopics] = None,
        users: typing.Optional[MessagingCreatePushNotificationRequestUsers] = None,
        targets: typing.Optional[MessagingCreatePushNotificationRequestTargets] = None,
        data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        action: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        icon: typing.Optional[str] = None,
        sound: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        badge: typing.Optional[str] = None,
        draft: typing.Optional[bool] = None,
        scheduled_at: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_push_notification_mapped_args(
            title=title,
            message_id=message_id,
            body=body,
            topics=topics,
            users=users,
            targets=targets,
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
        return await self._acreate_push_notification_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_push_notification(
        self,
        title: str,
        message_id: str,
        body: str,
        topics: typing.Optional[MessagingCreatePushNotificationRequestTopics] = None,
        users: typing.Optional[MessagingCreatePushNotificationRequestUsers] = None,
        targets: typing.Optional[MessagingCreatePushNotificationRequestTargets] = None,
        data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        action: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        icon: typing.Optional[str] = None,
        sound: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        badge: typing.Optional[str] = None,
        draft: typing.Optional[bool] = None,
        scheduled_at: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_push_notification_mapped_args(
            title=title,
            message_id=message_id,
            body=body,
            topics=topics,
            users=users,
            targets=targets,
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
        return self._create_push_notification_oapg(
            body=args.body,
        )

class CreatePushNotification(BaseApi):

    async def acreate_push_notification(
        self,
        title: str,
        message_id: str,
        body: str,
        topics: typing.Optional[MessagingCreatePushNotificationRequestTopics] = None,
        users: typing.Optional[MessagingCreatePushNotificationRequestUsers] = None,
        targets: typing.Optional[MessagingCreatePushNotificationRequestTargets] = None,
        data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        action: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        icon: typing.Optional[str] = None,
        sound: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        badge: typing.Optional[str] = None,
        draft: typing.Optional[bool] = None,
        scheduled_at: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> MessagePydantic:
        raw_response = await self.raw.acreate_push_notification(
            title=title,
            message_id=message_id,
            body=body,
            topics=topics,
            users=users,
            targets=targets,
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
    
    
    def create_push_notification(
        self,
        title: str,
        message_id: str,
        body: str,
        topics: typing.Optional[MessagingCreatePushNotificationRequestTopics] = None,
        users: typing.Optional[MessagingCreatePushNotificationRequestUsers] = None,
        targets: typing.Optional[MessagingCreatePushNotificationRequestTargets] = None,
        data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        action: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        icon: typing.Optional[str] = None,
        sound: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        badge: typing.Optional[str] = None,
        draft: typing.Optional[bool] = None,
        scheduled_at: typing.Optional[str] = None,
        validate: bool = False,
    ) -> MessagePydantic:
        raw_response = self.raw.create_push_notification(
            title=title,
            message_id=message_id,
            body=body,
            topics=topics,
            users=users,
            targets=targets,
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


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        title: str,
        message_id: str,
        body: str,
        topics: typing.Optional[MessagingCreatePushNotificationRequestTopics] = None,
        users: typing.Optional[MessagingCreatePushNotificationRequestUsers] = None,
        targets: typing.Optional[MessagingCreatePushNotificationRequestTargets] = None,
        data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        action: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        icon: typing.Optional[str] = None,
        sound: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        badge: typing.Optional[str] = None,
        draft: typing.Optional[bool] = None,
        scheduled_at: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_push_notification_mapped_args(
            title=title,
            message_id=message_id,
            body=body,
            topics=topics,
            users=users,
            targets=targets,
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
        return await self._acreate_push_notification_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        title: str,
        message_id: str,
        body: str,
        topics: typing.Optional[MessagingCreatePushNotificationRequestTopics] = None,
        users: typing.Optional[MessagingCreatePushNotificationRequestUsers] = None,
        targets: typing.Optional[MessagingCreatePushNotificationRequestTargets] = None,
        data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        action: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        icon: typing.Optional[str] = None,
        sound: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        badge: typing.Optional[str] = None,
        draft: typing.Optional[bool] = None,
        scheduled_at: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_push_notification_mapped_args(
            title=title,
            message_id=message_id,
            body=body,
            topics=topics,
            users=users,
            targets=targets,
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
        return self._create_push_notification_oapg(
            body=args.body,
        )

