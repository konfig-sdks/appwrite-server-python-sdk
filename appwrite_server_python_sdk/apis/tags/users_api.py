# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_server_python_sdk.paths.users_argon2.post import CreateArgon2User
from appwrite_server_python_sdk.paths.users_bcrypt.post import CreateBcryptUser
from appwrite_server_python_sdk.paths.users_md5.post import CreateMd5User
from appwrite_server_python_sdk.paths.users_user_id_mfa_recovery_codes.patch import CreateMfaRecoveryCodes
from appwrite_server_python_sdk.paths.users.post import CreateNewUser
from appwrite_server_python_sdk.paths.users_phpass.post import CreatePhpassUser
from appwrite_server_python_sdk.paths.users_scrypt_modified.post import CreateScryptModifiedUser
from appwrite_server_python_sdk.paths.users_scrypt.post import CreateScryptUser
from appwrite_server_python_sdk.paths.users_user_id_sessions.post import CreateSession
from appwrite_server_python_sdk.paths.users_sha.post import CreateShaUser
from appwrite_server_python_sdk.paths.users_user_id_targets.post import CreateTargetMessaging
from appwrite_server_python_sdk.paths.users_user_id_tokens.post import CreateTokenSession
from appwrite_server_python_sdk.paths.users_user_id_mfa_authenticators_type.delete import DeleteAuthenticator
from appwrite_server_python_sdk.paths.users_identities_identity_id.delete import DeleteIdentityById
from appwrite_server_python_sdk.paths.users_user_id_sessions_session_id.delete import DeleteSessionById
from appwrite_server_python_sdk.paths.users_user_id_targets_target_id.delete import DeleteTargetMessaging
from appwrite_server_python_sdk.paths.users_user_id.delete import DeleteUserById
from appwrite_server_python_sdk.paths.users_user_id_sessions.delete import DeleteUserSessions
from appwrite_server_python_sdk.paths.users_user_id.get import GetById
from appwrite_server_python_sdk.paths.users_user_id_mfa_recovery_codes.get import GetMfaRecoveryCodes
from appwrite_server_python_sdk.paths.users_user_id_prefs.get import GetUserPrefs
from appwrite_server_python_sdk.paths.users_user_id_targets_target_id.get import GetUserTargetById
from appwrite_server_python_sdk.paths.users.get import ListAll
from appwrite_server_python_sdk.paths.users_user_id_mfa_factors.get import ListFactors
from appwrite_server_python_sdk.paths.users_identities.get import ListIdentities
from appwrite_server_python_sdk.paths.users_user_id_memberships.get import ListMemberships
from appwrite_server_python_sdk.paths.users_user_id_sessions.get import ListSessions
from appwrite_server_python_sdk.paths.users_user_id_targets.get import ListTargets
from appwrite_server_python_sdk.paths.users_user_id_logs.get import ListUserLogs
from appwrite_server_python_sdk.paths.users_user_id_mfa_recovery_codes.put import RegenerateMfaRecoveryCodes
from appwrite_server_python_sdk.paths.users_user_id_email.patch import UpdateEmailById
from appwrite_server_python_sdk.paths.users_user_id_verification.patch import UpdateEmailVerification
from appwrite_server_python_sdk.paths.users_user_id_labels.put import UpdateLabelsById
from appwrite_server_python_sdk.paths.users_user_id_mfa.patch import UpdateMfaStatus
from appwrite_server_python_sdk.paths.users_user_id_password.patch import UpdatePasswordById
from appwrite_server_python_sdk.paths.users_user_id_phone.patch import UpdatePhoneById
from appwrite_server_python_sdk.paths.users_user_id_verification_phone.patch import UpdatePhoneVerification
from appwrite_server_python_sdk.paths.users_user_id_prefs.patch import UpdatePreferencesById
from appwrite_server_python_sdk.paths.users_user_id_status.patch import UpdateStatus
from appwrite_server_python_sdk.paths.users_user_id_targets_target_id.patch import UpdateTargetMessaging
from appwrite_server_python_sdk.paths.users_user_id_name.patch import UpdateUserByName
from appwrite_server_python_sdk.apis.tags.users_api_raw import UsersApiRaw


class UsersApi(
    CreateArgon2User,
    CreateBcryptUser,
    CreateMd5User,
    CreateMfaRecoveryCodes,
    CreateNewUser,
    CreatePhpassUser,
    CreateScryptModifiedUser,
    CreateScryptUser,
    CreateSession,
    CreateShaUser,
    CreateTargetMessaging,
    CreateTokenSession,
    DeleteAuthenticator,
    DeleteIdentityById,
    DeleteSessionById,
    DeleteTargetMessaging,
    DeleteUserById,
    DeleteUserSessions,
    GetById,
    GetMfaRecoveryCodes,
    GetUserPrefs,
    GetUserTargetById,
    ListAll,
    ListFactors,
    ListIdentities,
    ListMemberships,
    ListSessions,
    ListTargets,
    ListUserLogs,
    RegenerateMfaRecoveryCodes,
    UpdateEmailById,
    UpdateEmailVerification,
    UpdateLabelsById,
    UpdateMfaStatus,
    UpdatePasswordById,
    UpdatePhoneById,
    UpdatePhoneVerification,
    UpdatePreferencesById,
    UpdateStatus,
    UpdateTargetMessaging,
    UpdateUserByName,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UsersApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UsersApiRaw(api_client)
