import typing_extensions

from appwrite_server_python_sdk.paths import PathValues
from appwrite_server_python_sdk.apis.paths.account import Account
from appwrite_server_python_sdk.apis.paths.account_email import AccountEmail
from appwrite_server_python_sdk.apis.paths.account_identities import AccountIdentities
from appwrite_server_python_sdk.apis.paths.account_identities_identity_id import AccountIdentitiesIdentityId
from appwrite_server_python_sdk.apis.paths.account_jwt import AccountJwt
from appwrite_server_python_sdk.apis.paths.account_logs import AccountLogs
from appwrite_server_python_sdk.apis.paths.account_mfa import AccountMfa
from appwrite_server_python_sdk.apis.paths.account_mfa_authenticators_type import AccountMfaAuthenticatorsType
from appwrite_server_python_sdk.apis.paths.account_mfa_challenge import AccountMfaChallenge
from appwrite_server_python_sdk.apis.paths.account_mfa_factors import AccountMfaFactors
from appwrite_server_python_sdk.apis.paths.account_mfa_recovery_codes import AccountMfaRecoveryCodes
from appwrite_server_python_sdk.apis.paths.account_name import AccountName
from appwrite_server_python_sdk.apis.paths.account_password import AccountPassword
from appwrite_server_python_sdk.apis.paths.account_phone import AccountPhone
from appwrite_server_python_sdk.apis.paths.account_prefs import AccountPrefs
from appwrite_server_python_sdk.apis.paths.account_recovery import AccountRecovery
from appwrite_server_python_sdk.apis.paths.account_sessions import AccountSessions
from appwrite_server_python_sdk.apis.paths.account_sessions_anonymous import AccountSessionsAnonymous
from appwrite_server_python_sdk.apis.paths.account_sessions_email import AccountSessionsEmail
from appwrite_server_python_sdk.apis.paths.account_sessions_magic_url import AccountSessionsMagicUrl
from appwrite_server_python_sdk.apis.paths.account_sessions_phone import AccountSessionsPhone
from appwrite_server_python_sdk.apis.paths.account_sessions_token import AccountSessionsToken
from appwrite_server_python_sdk.apis.paths.account_sessions_session_id import AccountSessionsSessionId
from appwrite_server_python_sdk.apis.paths.account_status import AccountStatus
from appwrite_server_python_sdk.apis.paths.account_tokens_email import AccountTokensEmail
from appwrite_server_python_sdk.apis.paths.account_tokens_magic_url import AccountTokensMagicUrl
from appwrite_server_python_sdk.apis.paths.account_tokens_oauth2_provider import AccountTokensOauth2Provider
from appwrite_server_python_sdk.apis.paths.account_tokens_phone import AccountTokensPhone
from appwrite_server_python_sdk.apis.paths.account_verification import AccountVerification
from appwrite_server_python_sdk.apis.paths.account_verification_phone import AccountVerificationPhone
from appwrite_server_python_sdk.apis.paths.avatars_browsers_code import AvatarsBrowsersCode
from appwrite_server_python_sdk.apis.paths.avatars_credit_cards_code import AvatarsCreditCardsCode
from appwrite_server_python_sdk.apis.paths.avatars_favicon import AvatarsFavicon
from appwrite_server_python_sdk.apis.paths.avatars_flags_code import AvatarsFlagsCode
from appwrite_server_python_sdk.apis.paths.avatars_image import AvatarsImage
from appwrite_server_python_sdk.apis.paths.avatars_initials import AvatarsInitials
from appwrite_server_python_sdk.apis.paths.avatars_qr import AvatarsQr
from appwrite_server_python_sdk.apis.paths.databases import Databases
from appwrite_server_python_sdk.apis.paths.databases_database_id import DatabasesDatabaseId
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections import DatabasesDatabaseIdCollections
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id import DatabasesDatabaseIdCollectionsCollectionId
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes import DatabasesDatabaseIdCollectionsCollectionIdAttributes
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_boolean import DatabasesDatabaseIdCollectionsCollectionIdAttributesBoolean
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_boolean_key import DatabasesDatabaseIdCollectionsCollectionIdAttributesBooleanKey
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_datetime import DatabasesDatabaseIdCollectionsCollectionIdAttributesDatetime
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_datetime_key import DatabasesDatabaseIdCollectionsCollectionIdAttributesDatetimeKey
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_email import DatabasesDatabaseIdCollectionsCollectionIdAttributesEmail
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_email_key import DatabasesDatabaseIdCollectionsCollectionIdAttributesEmailKey
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_enum import DatabasesDatabaseIdCollectionsCollectionIdAttributesEnum
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_enum_key import DatabasesDatabaseIdCollectionsCollectionIdAttributesEnumKey
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_float import DatabasesDatabaseIdCollectionsCollectionIdAttributesFloat
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_float_key import DatabasesDatabaseIdCollectionsCollectionIdAttributesFloatKey
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_integer import DatabasesDatabaseIdCollectionsCollectionIdAttributesInteger
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_integer_key import DatabasesDatabaseIdCollectionsCollectionIdAttributesIntegerKey
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_ip import DatabasesDatabaseIdCollectionsCollectionIdAttributesIp
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_ip_key import DatabasesDatabaseIdCollectionsCollectionIdAttributesIpKey
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_relationship import DatabasesDatabaseIdCollectionsCollectionIdAttributesRelationship
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_string import DatabasesDatabaseIdCollectionsCollectionIdAttributesString
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_string_key import DatabasesDatabaseIdCollectionsCollectionIdAttributesStringKey
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_url import DatabasesDatabaseIdCollectionsCollectionIdAttributesUrl
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_url_key import DatabasesDatabaseIdCollectionsCollectionIdAttributesUrlKey
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_key import DatabasesDatabaseIdCollectionsCollectionIdAttributesKey
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_attributes_key_relationship import DatabasesDatabaseIdCollectionsCollectionIdAttributesKeyRelationship
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_documents import DatabasesDatabaseIdCollectionsCollectionIdDocuments
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_documents_document_id import DatabasesDatabaseIdCollectionsCollectionIdDocumentsDocumentId
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_indexes import DatabasesDatabaseIdCollectionsCollectionIdIndexes
from appwrite_server_python_sdk.apis.paths.databases_database_id_collections_collection_id_indexes_key import DatabasesDatabaseIdCollectionsCollectionIdIndexesKey
from appwrite_server_python_sdk.apis.paths.functions import Functions
from appwrite_server_python_sdk.apis.paths.functions_runtimes import FunctionsRuntimes
from appwrite_server_python_sdk.apis.paths.functions_function_id import FunctionsFunctionId
from appwrite_server_python_sdk.apis.paths.functions_function_id_deployments import FunctionsFunctionIdDeployments
from appwrite_server_python_sdk.apis.paths.functions_function_id_deployments_deployment_id import FunctionsFunctionIdDeploymentsDeploymentId
from appwrite_server_python_sdk.apis.paths.functions_function_id_deployments_deployment_id_builds_build_id import FunctionsFunctionIdDeploymentsDeploymentIdBuildsBuildId
from appwrite_server_python_sdk.apis.paths.functions_function_id_deployments_deployment_id_download import FunctionsFunctionIdDeploymentsDeploymentIdDownload
from appwrite_server_python_sdk.apis.paths.functions_function_id_executions import FunctionsFunctionIdExecutions
from appwrite_server_python_sdk.apis.paths.functions_function_id_executions_execution_id import FunctionsFunctionIdExecutionsExecutionId
from appwrite_server_python_sdk.apis.paths.functions_function_id_variables import FunctionsFunctionIdVariables
from appwrite_server_python_sdk.apis.paths.functions_function_id_variables_variable_id import FunctionsFunctionIdVariablesVariableId
from appwrite_server_python_sdk.apis.paths.graphql import Graphql
from appwrite_server_python_sdk.apis.paths.graphql_mutation import GraphqlMutation
from appwrite_server_python_sdk.apis.paths.health import Health
from appwrite_server_python_sdk.apis.paths.health_anti_virus import HealthAntiVirus
from appwrite_server_python_sdk.apis.paths.health_cache import HealthCache
from appwrite_server_python_sdk.apis.paths.health_certificate import HealthCertificate
from appwrite_server_python_sdk.apis.paths.health_db import HealthDb
from appwrite_server_python_sdk.apis.paths.health_pubsub import HealthPubsub
from appwrite_server_python_sdk.apis.paths.health_queue import HealthQueue
from appwrite_server_python_sdk.apis.paths.health_queue_builds import HealthQueueBuilds
from appwrite_server_python_sdk.apis.paths.health_queue_certificates import HealthQueueCertificates
from appwrite_server_python_sdk.apis.paths.health_queue_databases import HealthQueueDatabases
from appwrite_server_python_sdk.apis.paths.health_queue_deletes import HealthQueueDeletes
from appwrite_server_python_sdk.apis.paths.health_queue_failed_name import HealthQueueFailedName
from appwrite_server_python_sdk.apis.paths.health_queue_functions import HealthQueueFunctions
from appwrite_server_python_sdk.apis.paths.health_queue_logs import HealthQueueLogs
from appwrite_server_python_sdk.apis.paths.health_queue_mails import HealthQueueMails
from appwrite_server_python_sdk.apis.paths.health_queue_messaging import HealthQueueMessaging
from appwrite_server_python_sdk.apis.paths.health_queue_migrations import HealthQueueMigrations
from appwrite_server_python_sdk.apis.paths.health_queue_usage import HealthQueueUsage
from appwrite_server_python_sdk.apis.paths.health_queue_usage_dump import HealthQueueUsageDump
from appwrite_server_python_sdk.apis.paths.health_queue_webhooks import HealthQueueWebhooks
from appwrite_server_python_sdk.apis.paths.health_storage import HealthStorage
from appwrite_server_python_sdk.apis.paths.health_storage_local import HealthStorageLocal
from appwrite_server_python_sdk.apis.paths.health_time import HealthTime
from appwrite_server_python_sdk.apis.paths.locale import Locale
from appwrite_server_python_sdk.apis.paths.locale_codes import LocaleCodes
from appwrite_server_python_sdk.apis.paths.locale_continents import LocaleContinents
from appwrite_server_python_sdk.apis.paths.locale_countries import LocaleCountries
from appwrite_server_python_sdk.apis.paths.locale_countries_eu import LocaleCountriesEu
from appwrite_server_python_sdk.apis.paths.locale_countries_phones import LocaleCountriesPhones
from appwrite_server_python_sdk.apis.paths.locale_currencies import LocaleCurrencies
from appwrite_server_python_sdk.apis.paths.locale_languages import LocaleLanguages
from appwrite_server_python_sdk.apis.paths.messaging_messages import MessagingMessages
from appwrite_server_python_sdk.apis.paths.messaging_messages_email import MessagingMessagesEmail
from appwrite_server_python_sdk.apis.paths.messaging_messages_email_message_id import MessagingMessagesEmailMessageId
from appwrite_server_python_sdk.apis.paths.messaging_messages_push import MessagingMessagesPush
from appwrite_server_python_sdk.apis.paths.messaging_messages_push_message_id import MessagingMessagesPushMessageId
from appwrite_server_python_sdk.apis.paths.messaging_messages_sms import MessagingMessagesSms
from appwrite_server_python_sdk.apis.paths.messaging_messages_sms_message_id import MessagingMessagesSmsMessageId
from appwrite_server_python_sdk.apis.paths.messaging_messages_message_id import MessagingMessagesMessageId
from appwrite_server_python_sdk.apis.paths.messaging_messages_message_id_logs import MessagingMessagesMessageIdLogs
from appwrite_server_python_sdk.apis.paths.messaging_messages_message_id_targets import MessagingMessagesMessageIdTargets
from appwrite_server_python_sdk.apis.paths.messaging_providers import MessagingProviders
from appwrite_server_python_sdk.apis.paths.messaging_providers_apns import MessagingProvidersApns
from appwrite_server_python_sdk.apis.paths.messaging_providers_apns_provider_id import MessagingProvidersApnsProviderId
from appwrite_server_python_sdk.apis.paths.messaging_providers_fcm import MessagingProvidersFcm
from appwrite_server_python_sdk.apis.paths.messaging_providers_fcm_provider_id import MessagingProvidersFcmProviderId
from appwrite_server_python_sdk.apis.paths.messaging_providers_mailgun import MessagingProvidersMailgun
from appwrite_server_python_sdk.apis.paths.messaging_providers_mailgun_provider_id import MessagingProvidersMailgunProviderId
from appwrite_server_python_sdk.apis.paths.messaging_providers_msg91 import MessagingProvidersMsg91
from appwrite_server_python_sdk.apis.paths.messaging_providers_msg91_provider_id import MessagingProvidersMsg91ProviderId
from appwrite_server_python_sdk.apis.paths.messaging_providers_sendgrid import MessagingProvidersSendgrid
from appwrite_server_python_sdk.apis.paths.messaging_providers_sendgrid_provider_id import MessagingProvidersSendgridProviderId
from appwrite_server_python_sdk.apis.paths.messaging_providers_smtp import MessagingProvidersSmtp
from appwrite_server_python_sdk.apis.paths.messaging_providers_smtp_provider_id import MessagingProvidersSmtpProviderId
from appwrite_server_python_sdk.apis.paths.messaging_providers_telesign import MessagingProvidersTelesign
from appwrite_server_python_sdk.apis.paths.messaging_providers_telesign_provider_id import MessagingProvidersTelesignProviderId
from appwrite_server_python_sdk.apis.paths.messaging_providers_textmagic import MessagingProvidersTextmagic
from appwrite_server_python_sdk.apis.paths.messaging_providers_textmagic_provider_id import MessagingProvidersTextmagicProviderId
from appwrite_server_python_sdk.apis.paths.messaging_providers_twilio import MessagingProvidersTwilio
from appwrite_server_python_sdk.apis.paths.messaging_providers_twilio_provider_id import MessagingProvidersTwilioProviderId
from appwrite_server_python_sdk.apis.paths.messaging_providers_vonage import MessagingProvidersVonage
from appwrite_server_python_sdk.apis.paths.messaging_providers_vonage_provider_id import MessagingProvidersVonageProviderId
from appwrite_server_python_sdk.apis.paths.messaging_providers_provider_id import MessagingProvidersProviderId
from appwrite_server_python_sdk.apis.paths.messaging_providers_provider_id_logs import MessagingProvidersProviderIdLogs
from appwrite_server_python_sdk.apis.paths.messaging_subscribers_subscriber_id_logs import MessagingSubscribersSubscriberIdLogs
from appwrite_server_python_sdk.apis.paths.messaging_topics import MessagingTopics
from appwrite_server_python_sdk.apis.paths.messaging_topics_topic_id import MessagingTopicsTopicId
from appwrite_server_python_sdk.apis.paths.messaging_topics_topic_id_logs import MessagingTopicsTopicIdLogs
from appwrite_server_python_sdk.apis.paths.messaging_topics_topic_id_subscribers import MessagingTopicsTopicIdSubscribers
from appwrite_server_python_sdk.apis.paths.messaging_topics_topic_id_subscribers_subscriber_id import MessagingTopicsTopicIdSubscribersSubscriberId
from appwrite_server_python_sdk.apis.paths.storage_buckets import StorageBuckets
from appwrite_server_python_sdk.apis.paths.storage_buckets_bucket_id import StorageBucketsBucketId
from appwrite_server_python_sdk.apis.paths.storage_buckets_bucket_id_files import StorageBucketsBucketIdFiles
from appwrite_server_python_sdk.apis.paths.storage_buckets_bucket_id_files_file_id import StorageBucketsBucketIdFilesFileId
from appwrite_server_python_sdk.apis.paths.storage_buckets_bucket_id_files_file_id_download import StorageBucketsBucketIdFilesFileIdDownload
from appwrite_server_python_sdk.apis.paths.storage_buckets_bucket_id_files_file_id_preview import StorageBucketsBucketIdFilesFileIdPreview
from appwrite_server_python_sdk.apis.paths.storage_buckets_bucket_id_files_file_id_view import StorageBucketsBucketIdFilesFileIdView
from appwrite_server_python_sdk.apis.paths.teams import Teams
from appwrite_server_python_sdk.apis.paths.teams_team_id import TeamsTeamId
from appwrite_server_python_sdk.apis.paths.teams_team_id_memberships import TeamsTeamIdMemberships
from appwrite_server_python_sdk.apis.paths.teams_team_id_memberships_membership_id import TeamsTeamIdMembershipsMembershipId
from appwrite_server_python_sdk.apis.paths.teams_team_id_memberships_membership_id_status import TeamsTeamIdMembershipsMembershipIdStatus
from appwrite_server_python_sdk.apis.paths.teams_team_id_prefs import TeamsTeamIdPrefs
from appwrite_server_python_sdk.apis.paths.users import Users
from appwrite_server_python_sdk.apis.paths.users_argon2 import UsersArgon2
from appwrite_server_python_sdk.apis.paths.users_bcrypt import UsersBcrypt
from appwrite_server_python_sdk.apis.paths.users_identities import UsersIdentities
from appwrite_server_python_sdk.apis.paths.users_identities_identity_id import UsersIdentitiesIdentityId
from appwrite_server_python_sdk.apis.paths.users_md5 import UsersMd5
from appwrite_server_python_sdk.apis.paths.users_phpass import UsersPhpass
from appwrite_server_python_sdk.apis.paths.users_scrypt import UsersScrypt
from appwrite_server_python_sdk.apis.paths.users_scrypt_modified import UsersScryptModified
from appwrite_server_python_sdk.apis.paths.users_sha import UsersSha
from appwrite_server_python_sdk.apis.paths.users_user_id import UsersUserId
from appwrite_server_python_sdk.apis.paths.users_user_id_email import UsersUserIdEmail
from appwrite_server_python_sdk.apis.paths.users_user_id_labels import UsersUserIdLabels
from appwrite_server_python_sdk.apis.paths.users_user_id_logs import UsersUserIdLogs
from appwrite_server_python_sdk.apis.paths.users_user_id_memberships import UsersUserIdMemberships
from appwrite_server_python_sdk.apis.paths.users_user_id_mfa import UsersUserIdMfa
from appwrite_server_python_sdk.apis.paths.users_user_id_mfa_authenticators_type import UsersUserIdMfaAuthenticatorsType
from appwrite_server_python_sdk.apis.paths.users_user_id_mfa_factors import UsersUserIdMfaFactors
from appwrite_server_python_sdk.apis.paths.users_user_id_mfa_recovery_codes import UsersUserIdMfaRecoveryCodes
from appwrite_server_python_sdk.apis.paths.users_user_id_name import UsersUserIdName
from appwrite_server_python_sdk.apis.paths.users_user_id_password import UsersUserIdPassword
from appwrite_server_python_sdk.apis.paths.users_user_id_phone import UsersUserIdPhone
from appwrite_server_python_sdk.apis.paths.users_user_id_prefs import UsersUserIdPrefs
from appwrite_server_python_sdk.apis.paths.users_user_id_sessions import UsersUserIdSessions
from appwrite_server_python_sdk.apis.paths.users_user_id_sessions_session_id import UsersUserIdSessionsSessionId
from appwrite_server_python_sdk.apis.paths.users_user_id_status import UsersUserIdStatus
from appwrite_server_python_sdk.apis.paths.users_user_id_targets import UsersUserIdTargets
from appwrite_server_python_sdk.apis.paths.users_user_id_targets_target_id import UsersUserIdTargetsTargetId
from appwrite_server_python_sdk.apis.paths.users_user_id_tokens import UsersUserIdTokens
from appwrite_server_python_sdk.apis.paths.users_user_id_verification import UsersUserIdVerification
from appwrite_server_python_sdk.apis.paths.users_user_id_verification_phone import UsersUserIdVerificationPhone

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACCOUNT: Account,
        PathValues.ACCOUNT_EMAIL: AccountEmail,
        PathValues.ACCOUNT_IDENTITIES: AccountIdentities,
        PathValues.ACCOUNT_IDENTITIES_IDENTITY_ID: AccountIdentitiesIdentityId,
        PathValues.ACCOUNT_JWT: AccountJwt,
        PathValues.ACCOUNT_LOGS: AccountLogs,
        PathValues.ACCOUNT_MFA: AccountMfa,
        PathValues.ACCOUNT_MFA_AUTHENTICATORS_TYPE: AccountMfaAuthenticatorsType,
        PathValues.ACCOUNT_MFA_CHALLENGE: AccountMfaChallenge,
        PathValues.ACCOUNT_MFA_FACTORS: AccountMfaFactors,
        PathValues.ACCOUNT_MFA_RECOVERYCODES: AccountMfaRecoveryCodes,
        PathValues.ACCOUNT_NAME: AccountName,
        PathValues.ACCOUNT_PASSWORD: AccountPassword,
        PathValues.ACCOUNT_PHONE: AccountPhone,
        PathValues.ACCOUNT_PREFS: AccountPrefs,
        PathValues.ACCOUNT_RECOVERY: AccountRecovery,
        PathValues.ACCOUNT_SESSIONS: AccountSessions,
        PathValues.ACCOUNT_SESSIONS_ANONYMOUS: AccountSessionsAnonymous,
        PathValues.ACCOUNT_SESSIONS_EMAIL: AccountSessionsEmail,
        PathValues.ACCOUNT_SESSIONS_MAGICURL: AccountSessionsMagicUrl,
        PathValues.ACCOUNT_SESSIONS_PHONE: AccountSessionsPhone,
        PathValues.ACCOUNT_SESSIONS_TOKEN: AccountSessionsToken,
        PathValues.ACCOUNT_SESSIONS_SESSION_ID: AccountSessionsSessionId,
        PathValues.ACCOUNT_STATUS: AccountStatus,
        PathValues.ACCOUNT_TOKENS_EMAIL: AccountTokensEmail,
        PathValues.ACCOUNT_TOKENS_MAGICURL: AccountTokensMagicUrl,
        PathValues.ACCOUNT_TOKENS_OAUTH2_PROVIDER: AccountTokensOauth2Provider,
        PathValues.ACCOUNT_TOKENS_PHONE: AccountTokensPhone,
        PathValues.ACCOUNT_VERIFICATION: AccountVerification,
        PathValues.ACCOUNT_VERIFICATION_PHONE: AccountVerificationPhone,
        PathValues.AVATARS_BROWSERS_CODE: AvatarsBrowsersCode,
        PathValues.AVATARS_CREDITCARDS_CODE: AvatarsCreditCardsCode,
        PathValues.AVATARS_FAVICON: AvatarsFavicon,
        PathValues.AVATARS_FLAGS_CODE: AvatarsFlagsCode,
        PathValues.AVATARS_IMAGE: AvatarsImage,
        PathValues.AVATARS_INITIALS: AvatarsInitials,
        PathValues.AVATARS_QR: AvatarsQr,
        PathValues.DATABASES: Databases,
        PathValues.DATABASES_DATABASE_ID: DatabasesDatabaseId,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS: DatabasesDatabaseIdCollections,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID: DatabasesDatabaseIdCollectionsCollectionId,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES: DatabasesDatabaseIdCollectionsCollectionIdAttributes,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_BOOLEAN: DatabasesDatabaseIdCollectionsCollectionIdAttributesBoolean,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_BOOLEAN_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesBooleanKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_DATETIME: DatabasesDatabaseIdCollectionsCollectionIdAttributesDatetime,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_DATETIME_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesDatetimeKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_EMAIL: DatabasesDatabaseIdCollectionsCollectionIdAttributesEmail,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_EMAIL_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesEmailKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_ENUM: DatabasesDatabaseIdCollectionsCollectionIdAttributesEnum,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_ENUM_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesEnumKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_FLOAT: DatabasesDatabaseIdCollectionsCollectionIdAttributesFloat,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_FLOAT_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesFloatKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_INTEGER: DatabasesDatabaseIdCollectionsCollectionIdAttributesInteger,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_INTEGER_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesIntegerKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_IP: DatabasesDatabaseIdCollectionsCollectionIdAttributesIp,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_IP_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesIpKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_RELATIONSHIP: DatabasesDatabaseIdCollectionsCollectionIdAttributesRelationship,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_STRING: DatabasesDatabaseIdCollectionsCollectionIdAttributesString,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_STRING_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesStringKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_URL: DatabasesDatabaseIdCollectionsCollectionIdAttributesUrl,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_URL_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesUrlKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_KEY_RELATIONSHIP: DatabasesDatabaseIdCollectionsCollectionIdAttributesKeyRelationship,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_DOCUMENTS: DatabasesDatabaseIdCollectionsCollectionIdDocuments,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_DOCUMENTS_DOCUMENT_ID: DatabasesDatabaseIdCollectionsCollectionIdDocumentsDocumentId,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_INDEXES: DatabasesDatabaseIdCollectionsCollectionIdIndexes,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_INDEXES_KEY: DatabasesDatabaseIdCollectionsCollectionIdIndexesKey,
        PathValues.FUNCTIONS: Functions,
        PathValues.FUNCTIONS_RUNTIMES: FunctionsRuntimes,
        PathValues.FUNCTIONS_FUNCTION_ID: FunctionsFunctionId,
        PathValues.FUNCTIONS_FUNCTION_ID_DEPLOYMENTS: FunctionsFunctionIdDeployments,
        PathValues.FUNCTIONS_FUNCTION_ID_DEPLOYMENTS_DEPLOYMENT_ID: FunctionsFunctionIdDeploymentsDeploymentId,
        PathValues.FUNCTIONS_FUNCTION_ID_DEPLOYMENTS_DEPLOYMENT_ID_BUILDS_BUILD_ID: FunctionsFunctionIdDeploymentsDeploymentIdBuildsBuildId,
        PathValues.FUNCTIONS_FUNCTION_ID_DEPLOYMENTS_DEPLOYMENT_ID_DOWNLOAD: FunctionsFunctionIdDeploymentsDeploymentIdDownload,
        PathValues.FUNCTIONS_FUNCTION_ID_EXECUTIONS: FunctionsFunctionIdExecutions,
        PathValues.FUNCTIONS_FUNCTION_ID_EXECUTIONS_EXECUTION_ID: FunctionsFunctionIdExecutionsExecutionId,
        PathValues.FUNCTIONS_FUNCTION_ID_VARIABLES: FunctionsFunctionIdVariables,
        PathValues.FUNCTIONS_FUNCTION_ID_VARIABLES_VARIABLE_ID: FunctionsFunctionIdVariablesVariableId,
        PathValues.GRAPHQL: Graphql,
        PathValues.GRAPHQL_MUTATION: GraphqlMutation,
        PathValues.HEALTH: Health,
        PathValues.HEALTH_ANTIVIRUS: HealthAntiVirus,
        PathValues.HEALTH_CACHE: HealthCache,
        PathValues.HEALTH_CERTIFICATE: HealthCertificate,
        PathValues.HEALTH_DB: HealthDb,
        PathValues.HEALTH_PUBSUB: HealthPubsub,
        PathValues.HEALTH_QUEUE: HealthQueue,
        PathValues.HEALTH_QUEUE_BUILDS: HealthQueueBuilds,
        PathValues.HEALTH_QUEUE_CERTIFICATES: HealthQueueCertificates,
        PathValues.HEALTH_QUEUE_DATABASES: HealthQueueDatabases,
        PathValues.HEALTH_QUEUE_DELETES: HealthQueueDeletes,
        PathValues.HEALTH_QUEUE_FAILED_NAME: HealthQueueFailedName,
        PathValues.HEALTH_QUEUE_FUNCTIONS: HealthQueueFunctions,
        PathValues.HEALTH_QUEUE_LOGS: HealthQueueLogs,
        PathValues.HEALTH_QUEUE_MAILS: HealthQueueMails,
        PathValues.HEALTH_QUEUE_MESSAGING: HealthQueueMessaging,
        PathValues.HEALTH_QUEUE_MIGRATIONS: HealthQueueMigrations,
        PathValues.HEALTH_QUEUE_USAGE: HealthQueueUsage,
        PathValues.HEALTH_QUEUE_USAGEDUMP: HealthQueueUsageDump,
        PathValues.HEALTH_QUEUE_WEBHOOKS: HealthQueueWebhooks,
        PathValues.HEALTH_STORAGE: HealthStorage,
        PathValues.HEALTH_STORAGE_LOCAL: HealthStorageLocal,
        PathValues.HEALTH_TIME: HealthTime,
        PathValues.LOCALE: Locale,
        PathValues.LOCALE_CODES: LocaleCodes,
        PathValues.LOCALE_CONTINENTS: LocaleContinents,
        PathValues.LOCALE_COUNTRIES: LocaleCountries,
        PathValues.LOCALE_COUNTRIES_EU: LocaleCountriesEu,
        PathValues.LOCALE_COUNTRIES_PHONES: LocaleCountriesPhones,
        PathValues.LOCALE_CURRENCIES: LocaleCurrencies,
        PathValues.LOCALE_LANGUAGES: LocaleLanguages,
        PathValues.MESSAGING_MESSAGES: MessagingMessages,
        PathValues.MESSAGING_MESSAGES_EMAIL: MessagingMessagesEmail,
        PathValues.MESSAGING_MESSAGES_EMAIL_MESSAGE_ID: MessagingMessagesEmailMessageId,
        PathValues.MESSAGING_MESSAGES_PUSH: MessagingMessagesPush,
        PathValues.MESSAGING_MESSAGES_PUSH_MESSAGE_ID: MessagingMessagesPushMessageId,
        PathValues.MESSAGING_MESSAGES_SMS: MessagingMessagesSms,
        PathValues.MESSAGING_MESSAGES_SMS_MESSAGE_ID: MessagingMessagesSmsMessageId,
        PathValues.MESSAGING_MESSAGES_MESSAGE_ID: MessagingMessagesMessageId,
        PathValues.MESSAGING_MESSAGES_MESSAGE_ID_LOGS: MessagingMessagesMessageIdLogs,
        PathValues.MESSAGING_MESSAGES_MESSAGE_ID_TARGETS: MessagingMessagesMessageIdTargets,
        PathValues.MESSAGING_PROVIDERS: MessagingProviders,
        PathValues.MESSAGING_PROVIDERS_APNS: MessagingProvidersApns,
        PathValues.MESSAGING_PROVIDERS_APNS_PROVIDER_ID: MessagingProvidersApnsProviderId,
        PathValues.MESSAGING_PROVIDERS_FCM: MessagingProvidersFcm,
        PathValues.MESSAGING_PROVIDERS_FCM_PROVIDER_ID: MessagingProvidersFcmProviderId,
        PathValues.MESSAGING_PROVIDERS_MAILGUN: MessagingProvidersMailgun,
        PathValues.MESSAGING_PROVIDERS_MAILGUN_PROVIDER_ID: MessagingProvidersMailgunProviderId,
        PathValues.MESSAGING_PROVIDERS_MSG91: MessagingProvidersMsg91,
        PathValues.MESSAGING_PROVIDERS_MSG91_PROVIDER_ID: MessagingProvidersMsg91ProviderId,
        PathValues.MESSAGING_PROVIDERS_SENDGRID: MessagingProvidersSendgrid,
        PathValues.MESSAGING_PROVIDERS_SENDGRID_PROVIDER_ID: MessagingProvidersSendgridProviderId,
        PathValues.MESSAGING_PROVIDERS_SMTP: MessagingProvidersSmtp,
        PathValues.MESSAGING_PROVIDERS_SMTP_PROVIDER_ID: MessagingProvidersSmtpProviderId,
        PathValues.MESSAGING_PROVIDERS_TELESIGN: MessagingProvidersTelesign,
        PathValues.MESSAGING_PROVIDERS_TELESIGN_PROVIDER_ID: MessagingProvidersTelesignProviderId,
        PathValues.MESSAGING_PROVIDERS_TEXTMAGIC: MessagingProvidersTextmagic,
        PathValues.MESSAGING_PROVIDERS_TEXTMAGIC_PROVIDER_ID: MessagingProvidersTextmagicProviderId,
        PathValues.MESSAGING_PROVIDERS_TWILIO: MessagingProvidersTwilio,
        PathValues.MESSAGING_PROVIDERS_TWILIO_PROVIDER_ID: MessagingProvidersTwilioProviderId,
        PathValues.MESSAGING_PROVIDERS_VONAGE: MessagingProvidersVonage,
        PathValues.MESSAGING_PROVIDERS_VONAGE_PROVIDER_ID: MessagingProvidersVonageProviderId,
        PathValues.MESSAGING_PROVIDERS_PROVIDER_ID: MessagingProvidersProviderId,
        PathValues.MESSAGING_PROVIDERS_PROVIDER_ID_LOGS: MessagingProvidersProviderIdLogs,
        PathValues.MESSAGING_SUBSCRIBERS_SUBSCRIBER_ID_LOGS: MessagingSubscribersSubscriberIdLogs,
        PathValues.MESSAGING_TOPICS: MessagingTopics,
        PathValues.MESSAGING_TOPICS_TOPIC_ID: MessagingTopicsTopicId,
        PathValues.MESSAGING_TOPICS_TOPIC_ID_LOGS: MessagingTopicsTopicIdLogs,
        PathValues.MESSAGING_TOPICS_TOPIC_ID_SUBSCRIBERS: MessagingTopicsTopicIdSubscribers,
        PathValues.MESSAGING_TOPICS_TOPIC_ID_SUBSCRIBERS_SUBSCRIBER_ID: MessagingTopicsTopicIdSubscribersSubscriberId,
        PathValues.STORAGE_BUCKETS: StorageBuckets,
        PathValues.STORAGE_BUCKETS_BUCKET_ID: StorageBucketsBucketId,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES: StorageBucketsBucketIdFiles,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID: StorageBucketsBucketIdFilesFileId,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID_DOWNLOAD: StorageBucketsBucketIdFilesFileIdDownload,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID_PREVIEW: StorageBucketsBucketIdFilesFileIdPreview,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID_VIEW: StorageBucketsBucketIdFilesFileIdView,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_TEAM_ID: TeamsTeamId,
        PathValues.TEAMS_TEAM_ID_MEMBERSHIPS: TeamsTeamIdMemberships,
        PathValues.TEAMS_TEAM_ID_MEMBERSHIPS_MEMBERSHIP_ID: TeamsTeamIdMembershipsMembershipId,
        PathValues.TEAMS_TEAM_ID_MEMBERSHIPS_MEMBERSHIP_ID_STATUS: TeamsTeamIdMembershipsMembershipIdStatus,
        PathValues.TEAMS_TEAM_ID_PREFS: TeamsTeamIdPrefs,
        PathValues.USERS: Users,
        PathValues.USERS_ARGON2: UsersArgon2,
        PathValues.USERS_BCRYPT: UsersBcrypt,
        PathValues.USERS_IDENTITIES: UsersIdentities,
        PathValues.USERS_IDENTITIES_IDENTITY_ID: UsersIdentitiesIdentityId,
        PathValues.USERS_MD5: UsersMd5,
        PathValues.USERS_PHPASS: UsersPhpass,
        PathValues.USERS_SCRYPT: UsersScrypt,
        PathValues.USERS_SCRYPTMODIFIED: UsersScryptModified,
        PathValues.USERS_SHA: UsersSha,
        PathValues.USERS_USER_ID: UsersUserId,
        PathValues.USERS_USER_ID_EMAIL: UsersUserIdEmail,
        PathValues.USERS_USER_ID_LABELS: UsersUserIdLabels,
        PathValues.USERS_USER_ID_LOGS: UsersUserIdLogs,
        PathValues.USERS_USER_ID_MEMBERSHIPS: UsersUserIdMemberships,
        PathValues.USERS_USER_ID_MFA: UsersUserIdMfa,
        PathValues.USERS_USER_ID_MFA_AUTHENTICATORS_TYPE: UsersUserIdMfaAuthenticatorsType,
        PathValues.USERS_USER_ID_MFA_FACTORS: UsersUserIdMfaFactors,
        PathValues.USERS_USER_ID_MFA_RECOVERYCODES: UsersUserIdMfaRecoveryCodes,
        PathValues.USERS_USER_ID_NAME: UsersUserIdName,
        PathValues.USERS_USER_ID_PASSWORD: UsersUserIdPassword,
        PathValues.USERS_USER_ID_PHONE: UsersUserIdPhone,
        PathValues.USERS_USER_ID_PREFS: UsersUserIdPrefs,
        PathValues.USERS_USER_ID_SESSIONS: UsersUserIdSessions,
        PathValues.USERS_USER_ID_SESSIONS_SESSION_ID: UsersUserIdSessionsSessionId,
        PathValues.USERS_USER_ID_STATUS: UsersUserIdStatus,
        PathValues.USERS_USER_ID_TARGETS: UsersUserIdTargets,
        PathValues.USERS_USER_ID_TARGETS_TARGET_ID: UsersUserIdTargetsTargetId,
        PathValues.USERS_USER_ID_TOKENS: UsersUserIdTokens,
        PathValues.USERS_USER_ID_VERIFICATION: UsersUserIdVerification,
        PathValues.USERS_USER_ID_VERIFICATION_PHONE: UsersUserIdVerificationPhone,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACCOUNT: Account,
        PathValues.ACCOUNT_EMAIL: AccountEmail,
        PathValues.ACCOUNT_IDENTITIES: AccountIdentities,
        PathValues.ACCOUNT_IDENTITIES_IDENTITY_ID: AccountIdentitiesIdentityId,
        PathValues.ACCOUNT_JWT: AccountJwt,
        PathValues.ACCOUNT_LOGS: AccountLogs,
        PathValues.ACCOUNT_MFA: AccountMfa,
        PathValues.ACCOUNT_MFA_AUTHENTICATORS_TYPE: AccountMfaAuthenticatorsType,
        PathValues.ACCOUNT_MFA_CHALLENGE: AccountMfaChallenge,
        PathValues.ACCOUNT_MFA_FACTORS: AccountMfaFactors,
        PathValues.ACCOUNT_MFA_RECOVERYCODES: AccountMfaRecoveryCodes,
        PathValues.ACCOUNT_NAME: AccountName,
        PathValues.ACCOUNT_PASSWORD: AccountPassword,
        PathValues.ACCOUNT_PHONE: AccountPhone,
        PathValues.ACCOUNT_PREFS: AccountPrefs,
        PathValues.ACCOUNT_RECOVERY: AccountRecovery,
        PathValues.ACCOUNT_SESSIONS: AccountSessions,
        PathValues.ACCOUNT_SESSIONS_ANONYMOUS: AccountSessionsAnonymous,
        PathValues.ACCOUNT_SESSIONS_EMAIL: AccountSessionsEmail,
        PathValues.ACCOUNT_SESSIONS_MAGICURL: AccountSessionsMagicUrl,
        PathValues.ACCOUNT_SESSIONS_PHONE: AccountSessionsPhone,
        PathValues.ACCOUNT_SESSIONS_TOKEN: AccountSessionsToken,
        PathValues.ACCOUNT_SESSIONS_SESSION_ID: AccountSessionsSessionId,
        PathValues.ACCOUNT_STATUS: AccountStatus,
        PathValues.ACCOUNT_TOKENS_EMAIL: AccountTokensEmail,
        PathValues.ACCOUNT_TOKENS_MAGICURL: AccountTokensMagicUrl,
        PathValues.ACCOUNT_TOKENS_OAUTH2_PROVIDER: AccountTokensOauth2Provider,
        PathValues.ACCOUNT_TOKENS_PHONE: AccountTokensPhone,
        PathValues.ACCOUNT_VERIFICATION: AccountVerification,
        PathValues.ACCOUNT_VERIFICATION_PHONE: AccountVerificationPhone,
        PathValues.AVATARS_BROWSERS_CODE: AvatarsBrowsersCode,
        PathValues.AVATARS_CREDITCARDS_CODE: AvatarsCreditCardsCode,
        PathValues.AVATARS_FAVICON: AvatarsFavicon,
        PathValues.AVATARS_FLAGS_CODE: AvatarsFlagsCode,
        PathValues.AVATARS_IMAGE: AvatarsImage,
        PathValues.AVATARS_INITIALS: AvatarsInitials,
        PathValues.AVATARS_QR: AvatarsQr,
        PathValues.DATABASES: Databases,
        PathValues.DATABASES_DATABASE_ID: DatabasesDatabaseId,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS: DatabasesDatabaseIdCollections,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID: DatabasesDatabaseIdCollectionsCollectionId,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES: DatabasesDatabaseIdCollectionsCollectionIdAttributes,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_BOOLEAN: DatabasesDatabaseIdCollectionsCollectionIdAttributesBoolean,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_BOOLEAN_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesBooleanKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_DATETIME: DatabasesDatabaseIdCollectionsCollectionIdAttributesDatetime,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_DATETIME_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesDatetimeKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_EMAIL: DatabasesDatabaseIdCollectionsCollectionIdAttributesEmail,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_EMAIL_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesEmailKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_ENUM: DatabasesDatabaseIdCollectionsCollectionIdAttributesEnum,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_ENUM_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesEnumKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_FLOAT: DatabasesDatabaseIdCollectionsCollectionIdAttributesFloat,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_FLOAT_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesFloatKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_INTEGER: DatabasesDatabaseIdCollectionsCollectionIdAttributesInteger,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_INTEGER_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesIntegerKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_IP: DatabasesDatabaseIdCollectionsCollectionIdAttributesIp,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_IP_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesIpKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_RELATIONSHIP: DatabasesDatabaseIdCollectionsCollectionIdAttributesRelationship,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_STRING: DatabasesDatabaseIdCollectionsCollectionIdAttributesString,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_STRING_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesStringKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_URL: DatabasesDatabaseIdCollectionsCollectionIdAttributesUrl,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_URL_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesUrlKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_KEY: DatabasesDatabaseIdCollectionsCollectionIdAttributesKey,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_ATTRIBUTES_KEY_RELATIONSHIP: DatabasesDatabaseIdCollectionsCollectionIdAttributesKeyRelationship,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_DOCUMENTS: DatabasesDatabaseIdCollectionsCollectionIdDocuments,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_DOCUMENTS_DOCUMENT_ID: DatabasesDatabaseIdCollectionsCollectionIdDocumentsDocumentId,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_INDEXES: DatabasesDatabaseIdCollectionsCollectionIdIndexes,
        PathValues.DATABASES_DATABASE_ID_COLLECTIONS_COLLECTION_ID_INDEXES_KEY: DatabasesDatabaseIdCollectionsCollectionIdIndexesKey,
        PathValues.FUNCTIONS: Functions,
        PathValues.FUNCTIONS_RUNTIMES: FunctionsRuntimes,
        PathValues.FUNCTIONS_FUNCTION_ID: FunctionsFunctionId,
        PathValues.FUNCTIONS_FUNCTION_ID_DEPLOYMENTS: FunctionsFunctionIdDeployments,
        PathValues.FUNCTIONS_FUNCTION_ID_DEPLOYMENTS_DEPLOYMENT_ID: FunctionsFunctionIdDeploymentsDeploymentId,
        PathValues.FUNCTIONS_FUNCTION_ID_DEPLOYMENTS_DEPLOYMENT_ID_BUILDS_BUILD_ID: FunctionsFunctionIdDeploymentsDeploymentIdBuildsBuildId,
        PathValues.FUNCTIONS_FUNCTION_ID_DEPLOYMENTS_DEPLOYMENT_ID_DOWNLOAD: FunctionsFunctionIdDeploymentsDeploymentIdDownload,
        PathValues.FUNCTIONS_FUNCTION_ID_EXECUTIONS: FunctionsFunctionIdExecutions,
        PathValues.FUNCTIONS_FUNCTION_ID_EXECUTIONS_EXECUTION_ID: FunctionsFunctionIdExecutionsExecutionId,
        PathValues.FUNCTIONS_FUNCTION_ID_VARIABLES: FunctionsFunctionIdVariables,
        PathValues.FUNCTIONS_FUNCTION_ID_VARIABLES_VARIABLE_ID: FunctionsFunctionIdVariablesVariableId,
        PathValues.GRAPHQL: Graphql,
        PathValues.GRAPHQL_MUTATION: GraphqlMutation,
        PathValues.HEALTH: Health,
        PathValues.HEALTH_ANTIVIRUS: HealthAntiVirus,
        PathValues.HEALTH_CACHE: HealthCache,
        PathValues.HEALTH_CERTIFICATE: HealthCertificate,
        PathValues.HEALTH_DB: HealthDb,
        PathValues.HEALTH_PUBSUB: HealthPubsub,
        PathValues.HEALTH_QUEUE: HealthQueue,
        PathValues.HEALTH_QUEUE_BUILDS: HealthQueueBuilds,
        PathValues.HEALTH_QUEUE_CERTIFICATES: HealthQueueCertificates,
        PathValues.HEALTH_QUEUE_DATABASES: HealthQueueDatabases,
        PathValues.HEALTH_QUEUE_DELETES: HealthQueueDeletes,
        PathValues.HEALTH_QUEUE_FAILED_NAME: HealthQueueFailedName,
        PathValues.HEALTH_QUEUE_FUNCTIONS: HealthQueueFunctions,
        PathValues.HEALTH_QUEUE_LOGS: HealthQueueLogs,
        PathValues.HEALTH_QUEUE_MAILS: HealthQueueMails,
        PathValues.HEALTH_QUEUE_MESSAGING: HealthQueueMessaging,
        PathValues.HEALTH_QUEUE_MIGRATIONS: HealthQueueMigrations,
        PathValues.HEALTH_QUEUE_USAGE: HealthQueueUsage,
        PathValues.HEALTH_QUEUE_USAGEDUMP: HealthQueueUsageDump,
        PathValues.HEALTH_QUEUE_WEBHOOKS: HealthQueueWebhooks,
        PathValues.HEALTH_STORAGE: HealthStorage,
        PathValues.HEALTH_STORAGE_LOCAL: HealthStorageLocal,
        PathValues.HEALTH_TIME: HealthTime,
        PathValues.LOCALE: Locale,
        PathValues.LOCALE_CODES: LocaleCodes,
        PathValues.LOCALE_CONTINENTS: LocaleContinents,
        PathValues.LOCALE_COUNTRIES: LocaleCountries,
        PathValues.LOCALE_COUNTRIES_EU: LocaleCountriesEu,
        PathValues.LOCALE_COUNTRIES_PHONES: LocaleCountriesPhones,
        PathValues.LOCALE_CURRENCIES: LocaleCurrencies,
        PathValues.LOCALE_LANGUAGES: LocaleLanguages,
        PathValues.MESSAGING_MESSAGES: MessagingMessages,
        PathValues.MESSAGING_MESSAGES_EMAIL: MessagingMessagesEmail,
        PathValues.MESSAGING_MESSAGES_EMAIL_MESSAGE_ID: MessagingMessagesEmailMessageId,
        PathValues.MESSAGING_MESSAGES_PUSH: MessagingMessagesPush,
        PathValues.MESSAGING_MESSAGES_PUSH_MESSAGE_ID: MessagingMessagesPushMessageId,
        PathValues.MESSAGING_MESSAGES_SMS: MessagingMessagesSms,
        PathValues.MESSAGING_MESSAGES_SMS_MESSAGE_ID: MessagingMessagesSmsMessageId,
        PathValues.MESSAGING_MESSAGES_MESSAGE_ID: MessagingMessagesMessageId,
        PathValues.MESSAGING_MESSAGES_MESSAGE_ID_LOGS: MessagingMessagesMessageIdLogs,
        PathValues.MESSAGING_MESSAGES_MESSAGE_ID_TARGETS: MessagingMessagesMessageIdTargets,
        PathValues.MESSAGING_PROVIDERS: MessagingProviders,
        PathValues.MESSAGING_PROVIDERS_APNS: MessagingProvidersApns,
        PathValues.MESSAGING_PROVIDERS_APNS_PROVIDER_ID: MessagingProvidersApnsProviderId,
        PathValues.MESSAGING_PROVIDERS_FCM: MessagingProvidersFcm,
        PathValues.MESSAGING_PROVIDERS_FCM_PROVIDER_ID: MessagingProvidersFcmProviderId,
        PathValues.MESSAGING_PROVIDERS_MAILGUN: MessagingProvidersMailgun,
        PathValues.MESSAGING_PROVIDERS_MAILGUN_PROVIDER_ID: MessagingProvidersMailgunProviderId,
        PathValues.MESSAGING_PROVIDERS_MSG91: MessagingProvidersMsg91,
        PathValues.MESSAGING_PROVIDERS_MSG91_PROVIDER_ID: MessagingProvidersMsg91ProviderId,
        PathValues.MESSAGING_PROVIDERS_SENDGRID: MessagingProvidersSendgrid,
        PathValues.MESSAGING_PROVIDERS_SENDGRID_PROVIDER_ID: MessagingProvidersSendgridProviderId,
        PathValues.MESSAGING_PROVIDERS_SMTP: MessagingProvidersSmtp,
        PathValues.MESSAGING_PROVIDERS_SMTP_PROVIDER_ID: MessagingProvidersSmtpProviderId,
        PathValues.MESSAGING_PROVIDERS_TELESIGN: MessagingProvidersTelesign,
        PathValues.MESSAGING_PROVIDERS_TELESIGN_PROVIDER_ID: MessagingProvidersTelesignProviderId,
        PathValues.MESSAGING_PROVIDERS_TEXTMAGIC: MessagingProvidersTextmagic,
        PathValues.MESSAGING_PROVIDERS_TEXTMAGIC_PROVIDER_ID: MessagingProvidersTextmagicProviderId,
        PathValues.MESSAGING_PROVIDERS_TWILIO: MessagingProvidersTwilio,
        PathValues.MESSAGING_PROVIDERS_TWILIO_PROVIDER_ID: MessagingProvidersTwilioProviderId,
        PathValues.MESSAGING_PROVIDERS_VONAGE: MessagingProvidersVonage,
        PathValues.MESSAGING_PROVIDERS_VONAGE_PROVIDER_ID: MessagingProvidersVonageProviderId,
        PathValues.MESSAGING_PROVIDERS_PROVIDER_ID: MessagingProvidersProviderId,
        PathValues.MESSAGING_PROVIDERS_PROVIDER_ID_LOGS: MessagingProvidersProviderIdLogs,
        PathValues.MESSAGING_SUBSCRIBERS_SUBSCRIBER_ID_LOGS: MessagingSubscribersSubscriberIdLogs,
        PathValues.MESSAGING_TOPICS: MessagingTopics,
        PathValues.MESSAGING_TOPICS_TOPIC_ID: MessagingTopicsTopicId,
        PathValues.MESSAGING_TOPICS_TOPIC_ID_LOGS: MessagingTopicsTopicIdLogs,
        PathValues.MESSAGING_TOPICS_TOPIC_ID_SUBSCRIBERS: MessagingTopicsTopicIdSubscribers,
        PathValues.MESSAGING_TOPICS_TOPIC_ID_SUBSCRIBERS_SUBSCRIBER_ID: MessagingTopicsTopicIdSubscribersSubscriberId,
        PathValues.STORAGE_BUCKETS: StorageBuckets,
        PathValues.STORAGE_BUCKETS_BUCKET_ID: StorageBucketsBucketId,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES: StorageBucketsBucketIdFiles,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID: StorageBucketsBucketIdFilesFileId,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID_DOWNLOAD: StorageBucketsBucketIdFilesFileIdDownload,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID_PREVIEW: StorageBucketsBucketIdFilesFileIdPreview,
        PathValues.STORAGE_BUCKETS_BUCKET_ID_FILES_FILE_ID_VIEW: StorageBucketsBucketIdFilesFileIdView,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_TEAM_ID: TeamsTeamId,
        PathValues.TEAMS_TEAM_ID_MEMBERSHIPS: TeamsTeamIdMemberships,
        PathValues.TEAMS_TEAM_ID_MEMBERSHIPS_MEMBERSHIP_ID: TeamsTeamIdMembershipsMembershipId,
        PathValues.TEAMS_TEAM_ID_MEMBERSHIPS_MEMBERSHIP_ID_STATUS: TeamsTeamIdMembershipsMembershipIdStatus,
        PathValues.TEAMS_TEAM_ID_PREFS: TeamsTeamIdPrefs,
        PathValues.USERS: Users,
        PathValues.USERS_ARGON2: UsersArgon2,
        PathValues.USERS_BCRYPT: UsersBcrypt,
        PathValues.USERS_IDENTITIES: UsersIdentities,
        PathValues.USERS_IDENTITIES_IDENTITY_ID: UsersIdentitiesIdentityId,
        PathValues.USERS_MD5: UsersMd5,
        PathValues.USERS_PHPASS: UsersPhpass,
        PathValues.USERS_SCRYPT: UsersScrypt,
        PathValues.USERS_SCRYPTMODIFIED: UsersScryptModified,
        PathValues.USERS_SHA: UsersSha,
        PathValues.USERS_USER_ID: UsersUserId,
        PathValues.USERS_USER_ID_EMAIL: UsersUserIdEmail,
        PathValues.USERS_USER_ID_LABELS: UsersUserIdLabels,
        PathValues.USERS_USER_ID_LOGS: UsersUserIdLogs,
        PathValues.USERS_USER_ID_MEMBERSHIPS: UsersUserIdMemberships,
        PathValues.USERS_USER_ID_MFA: UsersUserIdMfa,
        PathValues.USERS_USER_ID_MFA_AUTHENTICATORS_TYPE: UsersUserIdMfaAuthenticatorsType,
        PathValues.USERS_USER_ID_MFA_FACTORS: UsersUserIdMfaFactors,
        PathValues.USERS_USER_ID_MFA_RECOVERYCODES: UsersUserIdMfaRecoveryCodes,
        PathValues.USERS_USER_ID_NAME: UsersUserIdName,
        PathValues.USERS_USER_ID_PASSWORD: UsersUserIdPassword,
        PathValues.USERS_USER_ID_PHONE: UsersUserIdPhone,
        PathValues.USERS_USER_ID_PREFS: UsersUserIdPrefs,
        PathValues.USERS_USER_ID_SESSIONS: UsersUserIdSessions,
        PathValues.USERS_USER_ID_SESSIONS_SESSION_ID: UsersUserIdSessionsSessionId,
        PathValues.USERS_USER_ID_STATUS: UsersUserIdStatus,
        PathValues.USERS_USER_ID_TARGETS: UsersUserIdTargets,
        PathValues.USERS_USER_ID_TARGETS_TARGET_ID: UsersUserIdTargetsTargetId,
        PathValues.USERS_USER_ID_TOKENS: UsersUserIdTokens,
        PathValues.USERS_USER_ID_VERIFICATION: UsersUserIdVerification,
        PathValues.USERS_USER_ID_VERIFICATION_PHONE: UsersUserIdVerificationPhone,
    }
)
