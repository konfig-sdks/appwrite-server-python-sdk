# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_server_python_sdk.paths.users_argon2.post import CreateArgon2UserRaw
from appwrite_server_python_sdk.paths.users_bcrypt.post import CreateBcryptUserRaw
from appwrite_server_python_sdk.paths.users_md5.post import CreateMd5UserRaw
from appwrite_server_python_sdk.paths.users_user_id_mfa_recovery_codes.patch import CreateMfaRecoveryCodesRaw
from appwrite_server_python_sdk.paths.users.post import CreateNewUserRaw
from appwrite_server_python_sdk.paths.users_phpass.post import CreatePhpassUserRaw
from appwrite_server_python_sdk.paths.users_scrypt_modified.post import CreateScryptModifiedUserRaw
from appwrite_server_python_sdk.paths.users_scrypt.post import CreateScryptUserRaw
from appwrite_server_python_sdk.paths.users_user_id_sessions.post import CreateSessionRaw
from appwrite_server_python_sdk.paths.users_sha.post import CreateShaUserRaw
from appwrite_server_python_sdk.paths.users_user_id_targets.post import CreateTargetMessagingRaw
from appwrite_server_python_sdk.paths.users_user_id_tokens.post import CreateTokenSessionRaw
from appwrite_server_python_sdk.paths.users_user_id_mfa_authenticators_type.delete import DeleteAuthenticatorRaw
from appwrite_server_python_sdk.paths.users_identities_identity_id.delete import DeleteIdentityByIdRaw
from appwrite_server_python_sdk.paths.users_user_id_sessions_session_id.delete import DeleteSessionByIdRaw
from appwrite_server_python_sdk.paths.users_user_id_targets_target_id.delete import DeleteTargetMessagingRaw
from appwrite_server_python_sdk.paths.users_user_id.delete import DeleteUserByIdRaw
from appwrite_server_python_sdk.paths.users_user_id_sessions.delete import DeleteUserSessionsRaw
from appwrite_server_python_sdk.paths.users_user_id.get import GetByIdRaw
from appwrite_server_python_sdk.paths.users_user_id_mfa_recovery_codes.get import GetMfaRecoveryCodesRaw
from appwrite_server_python_sdk.paths.users_user_id_prefs.get import GetUserPrefsRaw
from appwrite_server_python_sdk.paths.users_user_id_targets_target_id.get import GetUserTargetByIdRaw
from appwrite_server_python_sdk.paths.users.get import ListAllRaw
from appwrite_server_python_sdk.paths.users_user_id_mfa_factors.get import ListFactorsRaw
from appwrite_server_python_sdk.paths.users_identities.get import ListIdentitiesRaw
from appwrite_server_python_sdk.paths.users_user_id_memberships.get import ListMembershipsRaw
from appwrite_server_python_sdk.paths.users_user_id_sessions.get import ListSessionsRaw
from appwrite_server_python_sdk.paths.users_user_id_targets.get import ListTargetsRaw
from appwrite_server_python_sdk.paths.users_user_id_logs.get import ListUserLogsRaw
from appwrite_server_python_sdk.paths.users_user_id_mfa_recovery_codes.put import RegenerateMfaRecoveryCodesRaw
from appwrite_server_python_sdk.paths.users_user_id_email.patch import UpdateEmailByIdRaw
from appwrite_server_python_sdk.paths.users_user_id_verification.patch import UpdateEmailVerificationRaw
from appwrite_server_python_sdk.paths.users_user_id_labels.put import UpdateLabelsByIdRaw
from appwrite_server_python_sdk.paths.users_user_id_mfa.patch import UpdateMfaStatusRaw
from appwrite_server_python_sdk.paths.users_user_id_password.patch import UpdatePasswordByIdRaw
from appwrite_server_python_sdk.paths.users_user_id_phone.patch import UpdatePhoneByIdRaw
from appwrite_server_python_sdk.paths.users_user_id_verification_phone.patch import UpdatePhoneVerificationRaw
from appwrite_server_python_sdk.paths.users_user_id_prefs.patch import UpdatePreferencesByIdRaw
from appwrite_server_python_sdk.paths.users_user_id_status.patch import UpdateStatusRaw
from appwrite_server_python_sdk.paths.users_user_id_targets_target_id.patch import UpdateTargetMessagingRaw
from appwrite_server_python_sdk.paths.users_user_id_name.patch import UpdateUserByNameRaw


class UsersApiRaw(
    CreateArgon2UserRaw,
    CreateBcryptUserRaw,
    CreateMd5UserRaw,
    CreateMfaRecoveryCodesRaw,
    CreateNewUserRaw,
    CreatePhpassUserRaw,
    CreateScryptModifiedUserRaw,
    CreateScryptUserRaw,
    CreateSessionRaw,
    CreateShaUserRaw,
    CreateTargetMessagingRaw,
    CreateTokenSessionRaw,
    DeleteAuthenticatorRaw,
    DeleteIdentityByIdRaw,
    DeleteSessionByIdRaw,
    DeleteTargetMessagingRaw,
    DeleteUserByIdRaw,
    DeleteUserSessionsRaw,
    GetByIdRaw,
    GetMfaRecoveryCodesRaw,
    GetUserPrefsRaw,
    GetUserTargetByIdRaw,
    ListAllRaw,
    ListFactorsRaw,
    ListIdentitiesRaw,
    ListMembershipsRaw,
    ListSessionsRaw,
    ListTargetsRaw,
    ListUserLogsRaw,
    RegenerateMfaRecoveryCodesRaw,
    UpdateEmailByIdRaw,
    UpdateEmailVerificationRaw,
    UpdateLabelsByIdRaw,
    UpdateMfaStatusRaw,
    UpdatePasswordByIdRaw,
    UpdatePhoneByIdRaw,
    UpdatePhoneVerificationRaw,
    UpdatePreferencesByIdRaw,
    UpdateStatusRaw,
    UpdateTargetMessagingRaw,
    UpdateUserByNameRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
