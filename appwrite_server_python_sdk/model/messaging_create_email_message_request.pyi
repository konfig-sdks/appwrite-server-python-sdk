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


class MessagingCreateEmailMessageRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "subject",
            "messageId",
            "content",
        }
        
        class properties:
            messageId = schemas.StrSchema
            subject = schemas.StrSchema
            content = schemas.StrSchema
        
            @staticmethod
            def topics() -> typing.Type['MessagingCreateEmailMessageRequestTopics']:
                return MessagingCreateEmailMessageRequestTopics
        
            @staticmethod
            def users() -> typing.Type['MessagingCreateEmailMessageRequestUsers']:
                return MessagingCreateEmailMessageRequestUsers
        
            @staticmethod
            def targets() -> typing.Type['MessagingCreateEmailMessageRequestTargets']:
                return MessagingCreateEmailMessageRequestTargets
        
            @staticmethod
            def cc() -> typing.Type['MessagingCreateEmailMessageRequestCc']:
                return MessagingCreateEmailMessageRequestCc
        
            @staticmethod
            def bcc() -> typing.Type['MessagingCreateEmailMessageRequestBcc']:
                return MessagingCreateEmailMessageRequestBcc
        
            @staticmethod
            def attachments() -> typing.Type['MessagingCreateEmailMessageRequestAttachments']:
                return MessagingCreateEmailMessageRequestAttachments
            draft = schemas.BoolSchema
            html = schemas.BoolSchema
            scheduledAt = schemas.StrSchema
            __annotations__ = {
                "messageId": messageId,
                "subject": subject,
                "content": content,
                "topics": topics,
                "users": users,
                "targets": targets,
                "cc": cc,
                "bcc": bcc,
                "attachments": attachments,
                "draft": draft,
                "html": html,
                "scheduledAt": scheduledAt,
            }
    
    subject: MetaOapg.properties.subject
    messageId: MetaOapg.properties.messageId
    content: MetaOapg.properties.content
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["messageId"]) -> MetaOapg.properties.messageId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content"]) -> MetaOapg.properties.content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topics"]) -> 'MessagingCreateEmailMessageRequestTopics': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["users"]) -> 'MessagingCreateEmailMessageRequestUsers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targets"]) -> 'MessagingCreateEmailMessageRequestTargets': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cc"]) -> 'MessagingCreateEmailMessageRequestCc': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bcc"]) -> 'MessagingCreateEmailMessageRequestBcc': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachments"]) -> 'MessagingCreateEmailMessageRequestAttachments': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["draft"]) -> MetaOapg.properties.draft: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["html"]) -> MetaOapg.properties.html: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheduledAt"]) -> MetaOapg.properties.scheduledAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["messageId", "subject", "content", "topics", "users", "targets", "cc", "bcc", "attachments", "draft", "html", "scheduledAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["messageId"]) -> MetaOapg.properties.messageId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content"]) -> MetaOapg.properties.content: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topics"]) -> typing.Union['MessagingCreateEmailMessageRequestTopics', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["users"]) -> typing.Union['MessagingCreateEmailMessageRequestUsers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targets"]) -> typing.Union['MessagingCreateEmailMessageRequestTargets', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cc"]) -> typing.Union['MessagingCreateEmailMessageRequestCc', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bcc"]) -> typing.Union['MessagingCreateEmailMessageRequestBcc', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachments"]) -> typing.Union['MessagingCreateEmailMessageRequestAttachments', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["draft"]) -> typing.Union[MetaOapg.properties.draft, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["html"]) -> typing.Union[MetaOapg.properties.html, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheduledAt"]) -> typing.Union[MetaOapg.properties.scheduledAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["messageId", "subject", "content", "topics", "users", "targets", "cc", "bcc", "attachments", "draft", "html", "scheduledAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        subject: typing.Union[MetaOapg.properties.subject, str, ],
        messageId: typing.Union[MetaOapg.properties.messageId, str, ],
        content: typing.Union[MetaOapg.properties.content, str, ],
        topics: typing.Union['MessagingCreateEmailMessageRequestTopics', schemas.Unset] = schemas.unset,
        users: typing.Union['MessagingCreateEmailMessageRequestUsers', schemas.Unset] = schemas.unset,
        targets: typing.Union['MessagingCreateEmailMessageRequestTargets', schemas.Unset] = schemas.unset,
        cc: typing.Union['MessagingCreateEmailMessageRequestCc', schemas.Unset] = schemas.unset,
        bcc: typing.Union['MessagingCreateEmailMessageRequestBcc', schemas.Unset] = schemas.unset,
        attachments: typing.Union['MessagingCreateEmailMessageRequestAttachments', schemas.Unset] = schemas.unset,
        draft: typing.Union[MetaOapg.properties.draft, bool, schemas.Unset] = schemas.unset,
        html: typing.Union[MetaOapg.properties.html, bool, schemas.Unset] = schemas.unset,
        scheduledAt: typing.Union[MetaOapg.properties.scheduledAt, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MessagingCreateEmailMessageRequest':
        return super().__new__(
            cls,
            *args,
            subject=subject,
            messageId=messageId,
            content=content,
            topics=topics,
            users=users,
            targets=targets,
            cc=cc,
            bcc=bcc,
            attachments=attachments,
            draft=draft,
            html=html,
            scheduledAt=scheduledAt,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_server_python_sdk.model.messaging_create_email_message_request_attachments import MessagingCreateEmailMessageRequestAttachments
from appwrite_server_python_sdk.model.messaging_create_email_message_request_bcc import MessagingCreateEmailMessageRequestBcc
from appwrite_server_python_sdk.model.messaging_create_email_message_request_cc import MessagingCreateEmailMessageRequestCc
from appwrite_server_python_sdk.model.messaging_create_email_message_request_targets import MessagingCreateEmailMessageRequestTargets
from appwrite_server_python_sdk.model.messaging_create_email_message_request_topics import MessagingCreateEmailMessageRequestTopics
from appwrite_server_python_sdk.model.messaging_create_email_message_request_users import MessagingCreateEmailMessageRequestUsers
