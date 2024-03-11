# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_server_python_sdk.paths.messaging_providers_apns.post import CreateApnsProvider
from appwrite_server_python_sdk.paths.messaging_messages_email.post import CreateEmailMessage
from appwrite_server_python_sdk.paths.messaging_providers_fcm.post import CreateFcmProvider
from appwrite_server_python_sdk.paths.messaging_providers_msg91.post import CreateMsg91Provider
from appwrite_server_python_sdk.paths.messaging_providers_mailgun.post import CreateProvider
from appwrite_server_python_sdk.paths.messaging_messages_push.post import CreatePushNotification
from appwrite_server_python_sdk.paths.messaging_providers_sendgrid.post import CreateSendgridProvider
from appwrite_server_python_sdk.paths.messaging_messages_sms.post import CreateSmsMessage
from appwrite_server_python_sdk.paths.messaging_providers_smtp.post import CreateSmtpProvider
from appwrite_server_python_sdk.paths.messaging_topics_topic_id_subscribers.post import CreateSubscriber
from appwrite_server_python_sdk.paths.messaging_providers_telesign.post import CreateTelesignProvider
from appwrite_server_python_sdk.paths.messaging_providers_textmagic.post import CreateTextmagicProvider
from appwrite_server_python_sdk.paths.messaging_topics.post import CreateTopic
from appwrite_server_python_sdk.paths.messaging_providers_twilio.post import CreateTwilioProvider
from appwrite_server_python_sdk.paths.messaging_providers_vonage.post import CreateVonageProvider
from appwrite_server_python_sdk.paths.messaging_messages_message_id.delete import DeleteMessageById
from appwrite_server_python_sdk.paths.messaging_providers_provider_id.delete import DeleteProviderById
from appwrite_server_python_sdk.paths.messaging_topics_topic_id_subscribers_subscriber_id.delete import DeleteSubscriberById
from appwrite_server_python_sdk.paths.messaging_topics_topic_id.delete import DeleteTopicById
from appwrite_server_python_sdk.paths.messaging_messages_message_id.get import GetMessageById
from appwrite_server_python_sdk.paths.messaging_messages_message_id_logs.get import GetMessageLogs
from appwrite_server_python_sdk.paths.messaging_providers_provider_id.get import GetProviderById
from appwrite_server_python_sdk.paths.messaging_topics_topic_id_subscribers_subscriber_id.get import GetSubscriberById
from appwrite_server_python_sdk.paths.messaging_topics_topic_id.get import GetTopicById
from appwrite_server_python_sdk.paths.messaging_messages_message_id_targets.get import ListMessageTargets
from appwrite_server_python_sdk.paths.messaging_messages.get import ListMessages
from appwrite_server_python_sdk.paths.messaging_providers_provider_id_logs.get import ListProviderLogs
from appwrite_server_python_sdk.paths.messaging_providers.get import ListProviders
from appwrite_server_python_sdk.paths.messaging_subscribers_subscriber_id_logs.get import ListSubscriberLogs
from appwrite_server_python_sdk.paths.messaging_topics_topic_id_subscribers.get import ListSubscribers
from appwrite_server_python_sdk.paths.messaging_topics_topic_id_logs.get import ListTopicLogs
from appwrite_server_python_sdk.paths.messaging_topics.get import ListTopics
from appwrite_server_python_sdk.paths.messaging_providers_apns_provider_id.patch import UpdateApnsProvider
from appwrite_server_python_sdk.paths.messaging_messages_email_message_id.patch import UpdateEmailById
from appwrite_server_python_sdk.paths.messaging_providers_fcm_provider_id.patch import UpdateFcmProviderById
from appwrite_server_python_sdk.paths.messaging_providers_mailgun_provider_id.patch import UpdateMailgunProvider
from appwrite_server_python_sdk.paths.messaging_providers_msg91_provider_id.patch import UpdateMsg91Provider
from appwrite_server_python_sdk.paths.messaging_providers_sendgrid_provider_id.patch import UpdateProvider
from appwrite_server_python_sdk.paths.messaging_providers_smtp_provider_id.patch import UpdateProviderById
from appwrite_server_python_sdk.paths.messaging_messages_push_message_id.patch import UpdatePushNotification
from appwrite_server_python_sdk.paths.messaging_messages_sms_message_id.patch import UpdateSmsMessage
from appwrite_server_python_sdk.paths.messaging_providers_telesign_provider_id.patch import UpdateTelesignProvider
from appwrite_server_python_sdk.paths.messaging_providers_textmagic_provider_id.patch import UpdateTextmagicProvider
from appwrite_server_python_sdk.paths.messaging_topics_topic_id.patch import UpdateTopicById
from appwrite_server_python_sdk.paths.messaging_providers_twilio_provider_id.patch import UpdateTwilioProvider
from appwrite_server_python_sdk.paths.messaging_providers_vonage_provider_id.patch import UpdateVonageProvider
from appwrite_server_python_sdk.apis.tags.messaging_api_raw import MessagingApiRaw


class MessagingApi(
    CreateApnsProvider,
    CreateEmailMessage,
    CreateFcmProvider,
    CreateMsg91Provider,
    CreateProvider,
    CreatePushNotification,
    CreateSendgridProvider,
    CreateSmsMessage,
    CreateSmtpProvider,
    CreateSubscriber,
    CreateTelesignProvider,
    CreateTextmagicProvider,
    CreateTopic,
    CreateTwilioProvider,
    CreateVonageProvider,
    DeleteMessageById,
    DeleteProviderById,
    DeleteSubscriberById,
    DeleteTopicById,
    GetMessageById,
    GetMessageLogs,
    GetProviderById,
    GetSubscriberById,
    GetTopicById,
    ListMessageTargets,
    ListMessages,
    ListProviderLogs,
    ListProviders,
    ListSubscriberLogs,
    ListSubscribers,
    ListTopicLogs,
    ListTopics,
    UpdateApnsProvider,
    UpdateEmailById,
    UpdateFcmProviderById,
    UpdateMailgunProvider,
    UpdateMsg91Provider,
    UpdateProvider,
    UpdateProviderById,
    UpdatePushNotification,
    UpdateSmsMessage,
    UpdateTelesignProvider,
    UpdateTextmagicProvider,
    UpdateTopicById,
    UpdateTwilioProvider,
    UpdateVonageProvider,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: MessagingApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = MessagingApiRaw(api_client)
