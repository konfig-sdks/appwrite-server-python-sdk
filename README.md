<div align="center">

[![Visit Appwrite](./header.png)](https://appwrite.io)

# Appwrite<a id="appwrite"></a>

Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`appwriteserver.account.add_authenticator_app`](#appwriteserveraccountadd_authenticator_app)
  * [`appwriteserver.account.begin_mfa_verification`](#appwriteserveraccountbegin_mfa_verification)
  * [`appwriteserver.account.block_current_user_status`](#appwriteserveraccountblock_current_user_status)
  * [`appwriteserver.account.complete_email_verification`](#appwriteserveraccountcomplete_email_verification)
  * [`appwriteserver.account.complete_mfa_challenge`](#appwriteserveraccountcomplete_mfa_challenge)
  * [`appwriteserver.account.complete_password_recovery`](#appwriteserveraccountcomplete_password_recovery)
  * [`appwriteserver.account.confirm_phone_verification`](#appwriteserveraccountconfirm_phone_verification)
  * [`appwriteserver.account.create_anonymous_session`](#appwriteserveraccountcreate_anonymous_session)
  * [`appwriteserver.account.create_email_password_session`](#appwriteserveraccountcreate_email_password_session)
  * [`appwriteserver.account.create_email_token`](#appwriteserveraccountcreate_email_token)
  * [`appwriteserver.account.create_email_verification`](#appwriteserveraccountcreate_email_verification)
  * [`appwriteserver.account.create_jwt`](#appwriteserveraccountcreate_jwt)
  * [`appwriteserver.account.create_magic_url_token`](#appwriteserveraccountcreate_magic_url_token)
  * [`appwriteserver.account.create_new_user`](#appwriteserveraccountcreate_new_user)
  * [`appwriteserver.account.create_o_auth2_token`](#appwriteserveraccountcreate_o_auth2_token)
  * [`appwriteserver.account.create_password_recovery`](#appwriteserveraccountcreate_password_recovery)
  * [`appwriteserver.account.create_phone_token`](#appwriteserveraccountcreate_phone_token)
  * [`appwriteserver.account.create_phone_verification`](#appwriteserveraccountcreate_phone_verification)
  * [`appwriteserver.account.create_token_session`](#appwriteserveraccountcreate_token_session)
  * [`appwriteserver.account.delete_authenticator_by_id`](#appwriteserveraccountdelete_authenticator_by_id)
  * [`appwriteserver.account.delete_identity_by_id`](#appwriteserveraccountdelete_identity_by_id)
  * [`appwriteserver.account.delete_user_sessions`](#appwriteserveraccountdelete_user_sessions)
  * [`appwriteserver.account.extend_session_length`](#appwriteserveraccountextend_session_length)
  * [`appwriteserver.account.generate_recovery_codes`](#appwriteserveraccountgenerate_recovery_codes)
  * [`appwriteserver.account.get_current_user`](#appwriteserveraccountget_current_user)
  * [`appwriteserver.account.get_mfa_recovery_codes`](#appwriteserveraccountget_mfa_recovery_codes)
  * [`appwriteserver.account.get_prefs`](#appwriteserveraccountget_prefs)
  * [`appwriteserver.account.get_session_by_id`](#appwriteserveraccountget_session_by_id)
  * [`appwriteserver.account.list_identities`](#appwriteserveraccountlist_identities)
  * [`appwriteserver.account.list_logs`](#appwriteserveraccountlist_logs)
  * [`appwriteserver.account.list_mfa_factors`](#appwriteserveraccountlist_mfa_factors)
  * [`appwriteserver.account.list_sessions`](#appwriteserveraccountlist_sessions)
  * [`appwriteserver.account.logout_session_by_id`](#appwriteserveraccountlogout_session_by_id)
  * [`appwriteserver.account.regenerate_mfa_recovery_codes`](#appwriteserveraccountregenerate_mfa_recovery_codes)
  * [`appwriteserver.account.update_email_address`](#appwriteserveraccountupdate_email_address)
  * [`appwriteserver.account.update_magic_url_session`](#appwriteserveraccountupdate_magic_url_session)
  * [`appwriteserver.account.update_mfa_status`](#appwriteserveraccountupdate_mfa_status)
  * [`appwriteserver.account.update_name_operation`](#appwriteserveraccountupdate_name_operation)
  * [`appwriteserver.account.update_password_operation`](#appwriteserveraccountupdate_password_operation)
  * [`appwriteserver.account.update_phone`](#appwriteserveraccountupdate_phone)
  * [`appwriteserver.account.update_phone_session`](#appwriteserveraccountupdate_phone_session)
  * [`appwriteserver.account.update_preferences`](#appwriteserveraccountupdate_preferences)
  * [`appwriteserver.account.verify_authenticator`](#appwriteserveraccountverify_authenticator)
  * [`appwriteserver.avatars.generate_qr_code`](#appwriteserveravatarsgenerate_qr_code)
  * [`appwriteserver.avatars.get_browser_icon`](#appwriteserveravatarsget_browser_icon)
  * [`appwriteserver.avatars.get_country_flag`](#appwriteserveravatarsget_country_flag)
  * [`appwriteserver.avatars.get_credit_card_icon`](#appwriteserveravatarsget_credit_card_icon)
  * [`appwriteserver.avatars.get_favicon`](#appwriteserveravatarsget_favicon)
  * [`appwriteserver.avatars.get_remote_image`](#appwriteserveravatarsget_remote_image)
  * [`appwriteserver.avatars.get_user_initials`](#appwriteserveravatarsget_user_initials)
  * [`appwriteserver.databases.create_boolean_attribute`](#appwriteserverdatabasescreate_boolean_attribute)
  * [`appwriteserver.databases.create_collection`](#appwriteserverdatabasescreate_collection)
  * [`appwriteserver.databases.create_database`](#appwriteserverdatabasescreate_database)
  * [`appwriteserver.databases.create_datetime_attribute`](#appwriteserverdatabasescreate_datetime_attribute)
  * [`appwriteserver.databases.create_document`](#appwriteserverdatabasescreate_document)
  * [`appwriteserver.databases.create_email_attribute`](#appwriteserverdatabasescreate_email_attribute)
  * [`appwriteserver.databases.create_enum_attribute`](#appwriteserverdatabasescreate_enum_attribute)
  * [`appwriteserver.databases.create_float_attribute`](#appwriteserverdatabasescreate_float_attribute)
  * [`appwriteserver.databases.create_index`](#appwriteserverdatabasescreate_index)
  * [`appwriteserver.databases.create_integer_attribute`](#appwriteserverdatabasescreate_integer_attribute)
  * [`appwriteserver.databases.create_ip_attribute`](#appwriteserverdatabasescreate_ip_attribute)
  * [`appwriteserver.databases.create_relationship_attribute`](#appwriteserverdatabasescreate_relationship_attribute)
  * [`appwriteserver.databases.create_string_attribute`](#appwriteserverdatabasescreate_string_attribute)
  * [`appwriteserver.databases.create_url_attribute`](#appwriteserverdatabasescreate_url_attribute)
  * [`appwriteserver.databases.delete_attribute_by_id`](#appwriteserverdatabasesdelete_attribute_by_id)
  * [`appwriteserver.databases.delete_by_id`](#appwriteserverdatabasesdelete_by_id)
  * [`appwriteserver.databases.delete_collection_by_id`](#appwriteserverdatabasesdelete_collection_by_id)
  * [`appwriteserver.databases.delete_document_by_id`](#appwriteserverdatabasesdelete_document_by_id)
  * [`appwriteserver.databases.delete_index`](#appwriteserverdatabasesdelete_index)
  * [`appwriteserver.databases.get_attribute_by_id`](#appwriteserverdatabasesget_attribute_by_id)
  * [`appwriteserver.databases.get_by_id`](#appwriteserverdatabasesget_by_id)
  * [`appwriteserver.databases.get_collection_by_id`](#appwriteserverdatabasesget_collection_by_id)
  * [`appwriteserver.databases.get_document_by_id`](#appwriteserverdatabasesget_document_by_id)
  * [`appwriteserver.databases.get_index_by_id`](#appwriteserverdatabasesget_index_by_id)
  * [`appwriteserver.databases.list_all`](#appwriteserverdatabaseslist_all)
  * [`appwriteserver.databases.list_collection_attributes`](#appwriteserverdatabaseslist_collection_attributes)
  * [`appwriteserver.databases.list_collection_documents`](#appwriteserverdatabaseslist_collection_documents)
  * [`appwriteserver.databases.list_collections`](#appwriteserverdatabaseslist_collections)
  * [`appwriteserver.databases.list_indexes`](#appwriteserverdatabaseslist_indexes)
  * [`appwriteserver.databases.update_boolean_attribute`](#appwriteserverdatabasesupdate_boolean_attribute)
  * [`appwriteserver.databases.update_by_id`](#appwriteserverdatabasesupdate_by_id)
  * [`appwriteserver.databases.update_collection_by_id`](#appwriteserverdatabasesupdate_collection_by_id)
  * [`appwriteserver.databases.update_datetime_attribute`](#appwriteserverdatabasesupdate_datetime_attribute)
  * [`appwriteserver.databases.update_document_by_id`](#appwriteserverdatabasesupdate_document_by_id)
  * [`appwriteserver.databases.update_email_attribute`](#appwriteserverdatabasesupdate_email_attribute)
  * [`appwriteserver.databases.update_enum_attribute`](#appwriteserverdatabasesupdate_enum_attribute)
  * [`appwriteserver.databases.update_float_attribute`](#appwriteserverdatabasesupdate_float_attribute)
  * [`appwriteserver.databases.update_integer_attribute`](#appwriteserverdatabasesupdate_integer_attribute)
  * [`appwriteserver.databases.update_ip_attribute`](#appwriteserverdatabasesupdate_ip_attribute)
  * [`appwriteserver.databases.update_relationship_attribute`](#appwriteserverdatabasesupdate_relationship_attribute)
  * [`appwriteserver.databases.update_string_attribute`](#appwriteserverdatabasesupdate_string_attribute)
  * [`appwriteserver.databases.update_url_attribute`](#appwriteserverdatabasesupdate_url_attribute)
  * [`appwriteserver.functions.create_build`](#appwriteserverfunctionscreate_build)
  * [`appwriteserver.functions.create_deployment_function_code`](#appwriteserverfunctionscreate_deployment_function_code)
  * [`appwriteserver.functions.create_new_function`](#appwriteserverfunctionscreate_new_function)
  * [`appwriteserver.functions.create_variable`](#appwriteserverfunctionscreate_variable)
  * [`appwriteserver.functions.delete_by_id`](#appwriteserverfunctionsdelete_by_id)
  * [`appwriteserver.functions.delete_deployment`](#appwriteserverfunctionsdelete_deployment)
  * [`appwriteserver.functions.delete_variable_by_id`](#appwriteserverfunctionsdelete_variable_by_id)
  * [`appwriteserver.functions.get_by_id`](#appwriteserverfunctionsget_by_id)
  * [`appwriteserver.functions.get_deployment_by_id`](#appwriteserverfunctionsget_deployment_by_id)
  * [`appwriteserver.functions.get_deployment_contents`](#appwriteserverfunctionsget_deployment_contents)
  * [`appwriteserver.functions.get_execution_log`](#appwriteserverfunctionsget_execution_log)
  * [`appwriteserver.functions.get_variable_by_id`](#appwriteserverfunctionsget_variable_by_id)
  * [`appwriteserver.functions.list_all_functions`](#appwriteserverfunctionslist_all_functions)
  * [`appwriteserver.functions.list_deployments`](#appwriteserverfunctionslist_deployments)
  * [`appwriteserver.functions.list_executions`](#appwriteserverfunctionslist_executions)
  * [`appwriteserver.functions.list_runtimes`](#appwriteserverfunctionslist_runtimes)
  * [`appwriteserver.functions.list_variables`](#appwriteserverfunctionslist_variables)
  * [`appwriteserver.functions.trigger_execution`](#appwriteserverfunctionstrigger_execution)
  * [`appwriteserver.functions.update_by_id`](#appwriteserverfunctionsupdate_by_id)
  * [`appwriteserver.functions.update_deployment_function_code`](#appwriteserverfunctionsupdate_deployment_function_code)
  * [`appwriteserver.functions.update_variable_by_id`](#appwriteserverfunctionsupdate_variable_by_id)
  * [`appwriteserver.graphql.execute_mutation`](#appwriteservergraphqlexecute_mutation)
  * [`appwriteserver.graphql.execute_mutation_0`](#appwriteservergraphqlexecute_mutation_0)
  * [`appwriteserver.health.check_antivirus_status`](#appwriteserverhealthcheck_antivirus_status)
  * [`appwriteserver.health.check_cache_status`](#appwriteserverhealthcheck_cache_status)
  * [`appwriteserver.health.check_db_status`](#appwriteserverhealthcheck_db_status)
  * [`appwriteserver.health.check_local_storage_status`](#appwriteserverhealthcheck_local_storage_status)
  * [`appwriteserver.health.check_pubsub_server_status`](#appwriteserverhealthcheck_pubsub_server_status)
  * [`appwriteserver.health.check_server_status`](#appwriteserverhealthcheck_server_status)
  * [`appwriteserver.health.check_storage_status`](#appwriteserverhealthcheck_storage_status)
  * [`appwriteserver.health.functions_queue_count`](#appwriteserverhealthfunctions_queue_count)
  * [`appwriteserver.health.get_builds_queue`](#appwriteserverhealthget_builds_queue)
  * [`appwriteserver.health.get_databases_queue`](#appwriteserverhealthget_databases_queue)
  * [`appwriteserver.health.get_deletes_queue`](#appwriteserverhealthget_deletes_queue)
  * [`appwriteserver.health.get_failed_jobs`](#appwriteserverhealthget_failed_jobs)
  * [`appwriteserver.health.get_mail_queue_size`](#appwriteserverhealthget_mail_queue_size)
  * [`appwriteserver.health.get_migrations_queue`](#appwriteserverhealthget_migrations_queue)
  * [`appwriteserver.health.get_queue_logs`](#appwriteserverhealthget_queue_logs)
  * [`appwriteserver.health.get_queue_messaging`](#appwriteserverhealthget_queue_messaging)
  * [`appwriteserver.health.get_queue_status`](#appwriteserverhealthget_queue_status)
  * [`appwriteserver.health.get_queue_usage`](#appwriteserverhealthget_queue_usage)
  * [`appwriteserver.health.get_queue_usage_dump`](#appwriteserverhealthget_queue_usage_dump)
  * [`appwriteserver.health.get_ssl_cert`](#appwriteserverhealthget_ssl_cert)
  * [`appwriteserver.health.get_time_information`](#appwriteserverhealthget_time_information)
  * [`appwriteserver.health.get_webhooks_queue`](#appwriteserverhealthget_webhooks_queue)
  * [`appwriteserver.health.queue_certificates_get`](#appwriteserverhealthqueue_certificates_get)
  * [`appwriteserver.locale.get_language_list`](#appwriteserverlocaleget_language_list)
  * [`appwriteserver.locale.get_user_locale_data`](#appwriteserverlocaleget_user_locale_data)
  * [`appwriteserver.locale.list_codes`](#appwriteserverlocalelist_codes)
  * [`appwriteserver.locale.list_continents`](#appwriteserverlocalelist_continents)
  * [`appwriteserver.locale.list_countries`](#appwriteserverlocalelist_countries)
  * [`appwriteserver.locale.list_currencies_data`](#appwriteserverlocalelist_currencies_data)
  * [`appwriteserver.locale.list_eu_countries`](#appwriteserverlocalelist_eu_countries)
  * [`appwriteserver.locale.list_phone_codes`](#appwriteserverlocalelist_phone_codes)
  * [`appwriteserver.messaging.create_apns_provider`](#appwriteservermessagingcreate_apns_provider)
  * [`appwriteserver.messaging.create_email_message`](#appwriteservermessagingcreate_email_message)
  * [`appwriteserver.messaging.create_fcm_provider`](#appwriteservermessagingcreate_fcm_provider)
  * [`appwriteserver.messaging.create_msg91_provider`](#appwriteservermessagingcreate_msg91_provider)
  * [`appwriteserver.messaging.create_provider`](#appwriteservermessagingcreate_provider)
  * [`appwriteserver.messaging.create_push_notification`](#appwriteservermessagingcreate_push_notification)
  * [`appwriteserver.messaging.create_sendgrid_provider`](#appwriteservermessagingcreate_sendgrid_provider)
  * [`appwriteserver.messaging.create_sms_message`](#appwriteservermessagingcreate_sms_message)
  * [`appwriteserver.messaging.create_smtp_provider`](#appwriteservermessagingcreate_smtp_provider)
  * [`appwriteserver.messaging.create_subscriber`](#appwriteservermessagingcreate_subscriber)
  * [`appwriteserver.messaging.create_telesign_provider`](#appwriteservermessagingcreate_telesign_provider)
  * [`appwriteserver.messaging.create_textmagic_provider`](#appwriteservermessagingcreate_textmagic_provider)
  * [`appwriteserver.messaging.create_topic`](#appwriteservermessagingcreate_topic)
  * [`appwriteserver.messaging.create_twilio_provider`](#appwriteservermessagingcreate_twilio_provider)
  * [`appwriteserver.messaging.create_vonage_provider`](#appwriteservermessagingcreate_vonage_provider)
  * [`appwriteserver.messaging.delete_message_by_id`](#appwriteservermessagingdelete_message_by_id)
  * [`appwriteserver.messaging.delete_provider_by_id`](#appwriteservermessagingdelete_provider_by_id)
  * [`appwriteserver.messaging.delete_subscriber_by_id`](#appwriteservermessagingdelete_subscriber_by_id)
  * [`appwriteserver.messaging.delete_topic_by_id`](#appwriteservermessagingdelete_topic_by_id)
  * [`appwriteserver.messaging.get_message_by_id`](#appwriteservermessagingget_message_by_id)
  * [`appwriteserver.messaging.get_message_logs`](#appwriteservermessagingget_message_logs)
  * [`appwriteserver.messaging.get_provider_by_id`](#appwriteservermessagingget_provider_by_id)
  * [`appwriteserver.messaging.get_subscriber_by_id`](#appwriteservermessagingget_subscriber_by_id)
  * [`appwriteserver.messaging.get_topic_by_id`](#appwriteservermessagingget_topic_by_id)
  * [`appwriteserver.messaging.list_message_targets`](#appwriteservermessaginglist_message_targets)
  * [`appwriteserver.messaging.list_messages`](#appwriteservermessaginglist_messages)
  * [`appwriteserver.messaging.list_provider_logs`](#appwriteservermessaginglist_provider_logs)
  * [`appwriteserver.messaging.list_providers`](#appwriteservermessaginglist_providers)
  * [`appwriteserver.messaging.list_subscriber_logs`](#appwriteservermessaginglist_subscriber_logs)
  * [`appwriteserver.messaging.list_subscribers`](#appwriteservermessaginglist_subscribers)
  * [`appwriteserver.messaging.list_topic_logs`](#appwriteservermessaginglist_topic_logs)
  * [`appwriteserver.messaging.list_topics`](#appwriteservermessaginglist_topics)
  * [`appwriteserver.messaging.update_apns_provider`](#appwriteservermessagingupdate_apns_provider)
  * [`appwriteserver.messaging.update_email_by_id`](#appwriteservermessagingupdate_email_by_id)
  * [`appwriteserver.messaging.update_fcm_provider_by_id`](#appwriteservermessagingupdate_fcm_provider_by_id)
  * [`appwriteserver.messaging.update_mailgun_provider`](#appwriteservermessagingupdate_mailgun_provider)
  * [`appwriteserver.messaging.update_msg91_provider`](#appwriteservermessagingupdate_msg91_provider)
  * [`appwriteserver.messaging.update_provider`](#appwriteservermessagingupdate_provider)
  * [`appwriteserver.messaging.update_provider_by_id`](#appwriteservermessagingupdate_provider_by_id)
  * [`appwriteserver.messaging.update_push_notification`](#appwriteservermessagingupdate_push_notification)
  * [`appwriteserver.messaging.update_sms_message`](#appwriteservermessagingupdate_sms_message)
  * [`appwriteserver.messaging.update_telesign_provider`](#appwriteservermessagingupdate_telesign_provider)
  * [`appwriteserver.messaging.update_textmagic_provider`](#appwriteservermessagingupdate_textmagic_provider)
  * [`appwriteserver.messaging.update_topic_by_id`](#appwriteservermessagingupdate_topic_by_id)
  * [`appwriteserver.messaging.update_twilio_provider`](#appwriteservermessagingupdate_twilio_provider)
  * [`appwriteserver.messaging.update_vonage_provider`](#appwriteservermessagingupdate_vonage_provider)
  * [`appwriteserver.storage.create_file`](#appwriteserverstoragecreate_file)
  * [`appwriteserver.storage.create_new_bucket`](#appwriteserverstoragecreate_new_bucket)
  * [`appwriteserver.storage.delete_bucket_by_id`](#appwriteserverstoragedelete_bucket_by_id)
  * [`appwriteserver.storage.delete_file_by_id`](#appwriteserverstoragedelete_file_by_id)
  * [`appwriteserver.storage.get_bucket_by_id`](#appwriteserverstorageget_bucket_by_id)
  * [`appwriteserver.storage.get_file_by_id`](#appwriteserverstorageget_file_by_id)
  * [`appwriteserver.storage.get_file_download`](#appwriteserverstorageget_file_download)
  * [`appwriteserver.storage.get_file_preview_image`](#appwriteserverstorageget_file_preview_image)
  * [`appwriteserver.storage.get_file_view`](#appwriteserverstorageget_file_view)
  * [`appwriteserver.storage.list_buckets`](#appwriteserverstoragelist_buckets)
  * [`appwriteserver.storage.list_files`](#appwriteserverstoragelist_files)
  * [`appwriteserver.storage.update_bucket_by_id`](#appwriteserverstorageupdate_bucket_by_id)
  * [`appwriteserver.storage.update_file_by_id`](#appwriteserverstorageupdate_file_by_id)
  * [`appwriteserver.teams.create_membership_request`](#appwriteserverteamscreate_membership_request)
  * [`appwriteserver.teams.create_new_team`](#appwriteserverteamscreate_new_team)
  * [`appwriteserver.teams.delete_membership`](#appwriteserverteamsdelete_membership)
  * [`appwriteserver.teams.get_by_id`](#appwriteserverteamsget_by_id)
  * [`appwriteserver.teams.get_membership`](#appwriteserverteamsget_membership)
  * [`appwriteserver.teams.get_prefs_by_id`](#appwriteserverteamsget_prefs_by_id)
  * [`appwriteserver.teams.get_user_teams`](#appwriteserverteamsget_user_teams)
  * [`appwriteserver.teams.list_memberships`](#appwriteserverteamslist_memberships)
  * [`appwriteserver.teams.remove_team_by_id`](#appwriteserverteamsremove_team_by_id)
  * [`appwriteserver.teams.update_membership_roles`](#appwriteserverteamsupdate_membership_roles)
  * [`appwriteserver.teams.update_membership_status`](#appwriteserverteamsupdate_membership_status)
  * [`appwriteserver.teams.update_name_by_id`](#appwriteserverteamsupdate_name_by_id)
  * [`appwriteserver.teams.update_prefs_by_id`](#appwriteserverteamsupdate_prefs_by_id)
  * [`appwriteserver.users.create_argon2_user`](#appwriteserveruserscreate_argon2_user)
  * [`appwriteserver.users.create_bcrypt_user`](#appwriteserveruserscreate_bcrypt_user)
  * [`appwriteserver.users.create_md5_user`](#appwriteserveruserscreate_md5_user)
  * [`appwriteserver.users.create_mfa_recovery_codes`](#appwriteserveruserscreate_mfa_recovery_codes)
  * [`appwriteserver.users.create_new_user`](#appwriteserveruserscreate_new_user)
  * [`appwriteserver.users.create_phpass_user`](#appwriteserveruserscreate_phpass_user)
  * [`appwriteserver.users.create_scrypt_modified_user`](#appwriteserveruserscreate_scrypt_modified_user)
  * [`appwriteserver.users.create_scrypt_user`](#appwriteserveruserscreate_scrypt_user)
  * [`appwriteserver.users.create_session`](#appwriteserveruserscreate_session)
  * [`appwriteserver.users.create_sha_user`](#appwriteserveruserscreate_sha_user)
  * [`appwriteserver.users.create_target_messaging`](#appwriteserveruserscreate_target_messaging)
  * [`appwriteserver.users.create_token_session`](#appwriteserveruserscreate_token_session)
  * [`appwriteserver.users.delete_authenticator`](#appwriteserverusersdelete_authenticator)
  * [`appwriteserver.users.delete_identity_by_id`](#appwriteserverusersdelete_identity_by_id)
  * [`appwriteserver.users.delete_session_by_id`](#appwriteserverusersdelete_session_by_id)
  * [`appwriteserver.users.delete_target_messaging`](#appwriteserverusersdelete_target_messaging)
  * [`appwriteserver.users.delete_user_by_id`](#appwriteserverusersdelete_user_by_id)
  * [`appwriteserver.users.delete_user_sessions`](#appwriteserverusersdelete_user_sessions)
  * [`appwriteserver.users.get_by_id`](#appwriteserverusersget_by_id)
  * [`appwriteserver.users.get_mfa_recovery_codes`](#appwriteserverusersget_mfa_recovery_codes)
  * [`appwriteserver.users.get_user_prefs`](#appwriteserverusersget_user_prefs)
  * [`appwriteserver.users.get_user_target_by_id`](#appwriteserverusersget_user_target_by_id)
  * [`appwriteserver.users.list_all`](#appwriteserveruserslist_all)
  * [`appwriteserver.users.list_factors`](#appwriteserveruserslist_factors)
  * [`appwriteserver.users.list_identities`](#appwriteserveruserslist_identities)
  * [`appwriteserver.users.list_memberships`](#appwriteserveruserslist_memberships)
  * [`appwriteserver.users.list_sessions`](#appwriteserveruserslist_sessions)
  * [`appwriteserver.users.list_targets`](#appwriteserveruserslist_targets)
  * [`appwriteserver.users.list_user_logs`](#appwriteserveruserslist_user_logs)
  * [`appwriteserver.users.regenerate_mfa_recovery_codes`](#appwriteserverusersregenerate_mfa_recovery_codes)
  * [`appwriteserver.users.update_email_by_id`](#appwriteserverusersupdate_email_by_id)
  * [`appwriteserver.users.update_email_verification`](#appwriteserverusersupdate_email_verification)
  * [`appwriteserver.users.update_labels_by_id`](#appwriteserverusersupdate_labels_by_id)
  * [`appwriteserver.users.update_mfa_status`](#appwriteserverusersupdate_mfa_status)
  * [`appwriteserver.users.update_password_by_id`](#appwriteserverusersupdate_password_by_id)
  * [`appwriteserver.users.update_phone_by_id`](#appwriteserverusersupdate_phone_by_id)
  * [`appwriteserver.users.update_phone_verification`](#appwriteserverusersupdate_phone_verification)
  * [`appwriteserver.users.update_preferences_by_id`](#appwriteserverusersupdate_preferences_by_id)
  * [`appwriteserver.users.update_status`](#appwriteserverusersupdate_status)
  * [`appwriteserver.users.update_target_messaging`](#appwriteserverusersupdate_target_messaging)
  * [`appwriteserver.users.update_user_by_name`](#appwriteserverusersupdate_user_by_name)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Appwrite&serviceName=Server&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from appwrite_server_python_sdk import AppwriteServer, ApiException

appwriteserver = AppwriteServer(
    jwt="YOUR_API_KEY",
    project="YOUR_API_KEY",
    session="YOUR_API_KEY",
)

try:
    # Add Authenticator
    add_authenticator_app_response = appwriteserver.account.add_authenticator_app(
        type="totp",
    )
    print(add_authenticator_app_response)
except ApiException as e:
    print("Exception when calling AccountApi.add_authenticator_app: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from appwrite_server_python_sdk import AppwriteServer, ApiException

appwriteserver = AppwriteServer(
    jwt="YOUR_API_KEY",
    project="YOUR_API_KEY",
    session="YOUR_API_KEY",
)


async def main():
    try:
        # Add Authenticator
        add_authenticator_app_response = (
            await appwriteserver.account.aadd_authenticator_app(
                type="totp",
            )
        )
        print(add_authenticator_app_response)
    except ApiException as e:
        print("Exception when calling AccountApi.add_authenticator_app: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from appwrite_server_python_sdk import AppwriteServer, ApiException

appwriteserver = AppwriteServer(
    jwt="YOUR_API_KEY",
    project="YOUR_API_KEY",
    session="YOUR_API_KEY",
)

try:
    # Add Authenticator
    add_authenticator_app_response = appwriteserver.account.raw.add_authenticator_app(
        type="totp",
    )
    pprint(add_authenticator_app_response.body)
    pprint(add_authenticator_app_response.body["secret"])
    pprint(add_authenticator_app_response.body["uri"])
    pprint(add_authenticator_app_response.headers)
    pprint(add_authenticator_app_response.status)
    pprint(add_authenticator_app_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccountApi.add_authenticator_app: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `appwriteserver.account.add_authenticator_app`<a id="appwriteserveraccountadd_authenticator_app"></a>

Add an authenticator app to be used as an MFA factor. Verify the authenticator using the [verify authenticator](/docs/references/cloud/client-web/account#verifyAuthenticator) method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_authenticator_app_response = appwriteserver.account.add_authenticator_app(
    type="totp",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Type of authenticator. Must be `totp`

#### 🔄 Return<a id="🔄-return"></a>

[`MfaType`](./appwrite_server_python_sdk/pydantic/mfa_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/authenticators/{type}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.begin_mfa_verification`<a id="appwriteserveraccountbegin_mfa_verification"></a>

Begin the process of MFA verification after sign-in. Finish the flow with [updateMfaChallenge](/docs/references/cloud/client-web/account#updateMfaChallenge) method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
begin_mfa_verification_response = appwriteserver.account.begin_mfa_verification(
    factor="email",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### factor: `str`<a id="factor-str"></a>

Factor used for verification. Must be one of following: `email`, `phone`, `totp`, `recoveryCode`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountBeginMfaVerificationRequest`](./appwrite_server_python_sdk/type/account_begin_mfa_verification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MfaChallenge`](./appwrite_server_python_sdk/pydantic/mfa_challenge.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/challenge` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.block_current_user_status`<a id="appwriteserveraccountblock_current_user_status"></a>

Block the currently logged in user account. Behind the scene, the user record is not deleted but permanently blocked from any access. To completely delete a user, use the Users API instead.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
block_current_user_status_response = appwriteserver.account.block_current_user_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/status` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.complete_email_verification`<a id="appwriteserveraccountcomplete_email_verification"></a>

Use this endpoint to complete the user email verification process. Use both the **userId** and **secret** parameters that were attached to your app URL to verify the user email ownership. If confirmed this route will return a 200 status code.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
complete_email_verification_response = (
    appwriteserver.account.complete_email_verification(
        user_id="<USER_ID>",
        secret="<SECRET>",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### secret: `str`<a id="secret-str"></a>

Valid verification token.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCompleteEmailVerificationRequest`](./appwrite_server_python_sdk/type/account_complete_email_verification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_server_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/verification` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.complete_mfa_challenge`<a id="appwriteserveraccountcomplete_mfa_challenge"></a>

Complete the MFA challenge by providing the one-time password. Finish the process of MFA verification by providing the one-time password. To begin the flow, use [createMfaChallenge](/docs/references/cloud/client-web/account#createMfaChallenge) method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
complete_mfa_challenge_response = appwriteserver.account.complete_mfa_challenge(
    challenge_id="<CHALLENGE_ID>",
    otp="<OTP>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### challenge_id: `str`<a id="challenge_id-str"></a>

ID of the challenge.

##### otp: `str`<a id="otp-str"></a>

Valid verification token.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCompleteMfaChallengeRequest`](./appwrite_server_python_sdk/type/account_complete_mfa_challenge_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_server_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/challenge` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.complete_password_recovery`<a id="appwriteserveraccountcomplete_password_recovery"></a>

Use this endpoint to complete the user account password reset. Both the **userId** and **secret** arguments will be passed as query parameters to the redirect URL you have provided when sending your request to the [POST /account/recovery](https://appwrite.io/docs/references/cloud/client-web/account#createRecovery) endpoint.

Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
complete_password_recovery_response = appwriteserver.account.complete_password_recovery(
    user_id="<USER_ID>",
    secret="<SECRET>",
    password="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### secret: `str`<a id="secret-str"></a>

Valid reset token.

##### password: `str`<a id="password-str"></a>

New user password. Must be between 8 and 256 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCompletePasswordRecoveryRequest`](./appwrite_server_python_sdk/type/account_complete_password_recovery_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_server_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/recovery` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.confirm_phone_verification`<a id="appwriteserveraccountconfirm_phone_verification"></a>

Use this endpoint to complete the user phone verification process. Use the **userId** and **secret** that were sent to your user's phone number to verify the user email ownership. If confirmed this route will return a 200 status code.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
confirm_phone_verification_response = appwriteserver.account.confirm_phone_verification(
    user_id="<USER_ID>",
    secret="<SECRET>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### secret: `str`<a id="secret-str"></a>

Valid verification token.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountConfirmPhoneVerificationRequest`](./appwrite_server_python_sdk/type/account_confirm_phone_verification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_server_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/verification/phone` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.create_anonymous_session`<a id="appwriteserveraccountcreate_anonymous_session"></a>

Use this endpoint to allow a new user to register an anonymous account in your project. This route will also create a new session for the user. To allow the new user to convert an anonymous account to a normal account, you need to update its [email and password](https://appwrite.io/docs/references/cloud/client-web/account#updateEmail) or create an [OAuth2 session](https://appwrite.io/docs/references/cloud/client-web/account#CreateOAuth2Session).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_anonymous_session_response = appwriteserver.account.create_anonymous_session()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_server_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/anonymous` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.create_email_password_session`<a id="appwriteserveraccountcreate_email_password_session"></a>

Allow the user to login into their account by providing a valid email and password combination. This route will create a new session for the user.

A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_email_password_session_response = (
    appwriteserver.account.create_email_password_session(
        email="email@example.com",
        password="password",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password. Must be at least 8 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreateEmailPasswordSessionRequest`](./appwrite_server_python_sdk/type/account_create_email_password_session_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_server_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/email` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.create_email_token`<a id="appwriteserveraccountcreate_email_token"></a>

Sends the user an email with a secret key for creating a session. If the provided user ID has not be registered, a new user will be created. Use the returned user ID and secret and submit a request to the [POST /v1/account/sessions/token](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint to complete the login process. The secret sent to the user's email is valid for 15 minutes.

A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_email_token_response = appwriteserver.account.create_email_token(
    user_id="<USER_ID>",
    email="email@example.com",
    phrase=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### phrase: `bool`<a id="phrase-bool"></a>

Toggle for security phrase. If enabled, email will be send with a randomly generated phrase and the phrase will also be included in the response. Confirming phrases match increases the security of your authentication flow.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreateEmailTokenRequest`](./appwrite_server_python_sdk/type/account_create_email_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_server_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/tokens/email` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.create_email_verification`<a id="appwriteserveraccountcreate_email_verification"></a>

Use this endpoint to send a verification message to your user email address to confirm they are the valid owners of that address. Both the **userId** and **secret** arguments will be passed as query parameters to the URL you have provided to be attached to the verification email. The provided URL should redirect the user back to your app and allow you to complete the verification process by verifying both the **userId** and **secret** parameters. Learn more about how to [complete the verification process](https://appwrite.io/docs/references/cloud/client-web/account#updateVerification). The verification link sent to the user's email address is valid for 7 days.

Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md), the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_email_verification_response = appwriteserver.account.create_email_verification(
    url="https://example.com",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

URL to redirect the user back to your app from the verification email. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreateEmailVerificationRequest`](./appwrite_server_python_sdk/type/account_create_email_verification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_server_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/verification` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.create_jwt`<a id="appwriteserveraccountcreate_jwt"></a>

Use this endpoint to create a JSON Web Token. You can use the resulting JWT to authenticate on behalf of the current user when working with the Appwrite server-side API and SDKs. The JWT secret is valid for 15 minutes from its creation and will be invalid if the user will logout in that time frame.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_jwt_response = appwriteserver.account.create_jwt()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Jwt`](./appwrite_server_python_sdk/pydantic/jwt.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/jwt` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.create_magic_url_token`<a id="appwriteserveraccountcreate_magic_url_token"></a>

Sends the user an email with a secret key for creating a session. If the provided user ID has not been registered, a new user will be created. When the user clicks the link in the email, the user is redirected back to the URL you provided with the secret key and userId values attached to the URL query string. Use the query string parameters to submit a request to the [POST /v1/account/sessions/token](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint to complete the login process. The link sent to the user's email address is valid for 1 hour. If you are on a mobile device you can leave the URL parameter empty, so that the login completion will be handled by your Appwrite instance by default.

A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_magic_url_token_response = appwriteserver.account.create_magic_url_token(
    user_id="<USER_ID>",
    email="email@example.com",
    url="https://example.com",
    phrase=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### url: `str`<a id="url-str"></a>

URL to redirect the user back to your app from the magic URL login. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

##### phrase: `bool`<a id="phrase-bool"></a>

Toggle for security phrase. If enabled, email will be send with a randomly generated phrase and the phrase will also be included in the response. Confirming phrases match increases the security of your authentication flow.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreateMagicUrlTokenRequest`](./appwrite_server_python_sdk/type/account_create_magic_url_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_server_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/tokens/magic-url` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.create_new_user`<a id="appwriteserveraccountcreate_new_user"></a>

Use this endpoint to allow a new user to register a new account in your project. After the user registration completes successfully, you can use the [/account/verfication](https://appwrite.io/docs/references/cloud/client-web/account#createVerification) route to start verifying the user email address. To allow the new user to login to their new account, you need to create a new [account session](https://appwrite.io/docs/references/cloud/client-web/account#createEmailSession).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_user_response = appwriteserver.account.create_new_user(
    user_id="<USER_ID>",
    email="email@example.com",
    password="string_example",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

New user password. Must be between 8 and 256 chars.

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreateNewUserRequest`](./appwrite_server_python_sdk/type/account_create_new_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.create_o_auth2_token`<a id="appwriteserveraccountcreate_o_auth2_token"></a>

Allow the user to login to their account using the OAuth2 provider of their choice. Each OAuth2 provider should be enabled from the Appwrite console first. Use the success and failure arguments to provide a redirect URL's back to your app when login is completed. 

If authentication succeeds, `userId` and `secret` of a token will be appended to the success URL as query parameters. These can be used to create a new session using the [Create session](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint.

A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.account.create_o_auth2_token(
    provider="amazon",
    success="",
    failure="",
    scopes=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider: `str`<a id="provider-str"></a>

OAuth2 Provider. Currently, supported providers are: amazon, apple, auth0, authentik, autodesk, bitbucket, bitly, box, dailymotion, discord, disqus, dropbox, etsy, facebook, github, gitlab, google, linkedin, microsoft, notion, oidc, okta, paypal, paypalSandbox, podio, salesforce, slack, spotify, stripe, tradeshift, tradeshiftBox, twitch, wordpress, yahoo, yammer, yandex, zoho, zoom.

##### success: `str`<a id="success-str"></a>

URL to redirect back to your app after a successful login attempt.  Only URLs from hostnames in your project's platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

##### failure: `str`<a id="failure-str"></a>

URL to redirect back to your app after a failed login attempt.  Only URLs from hostnames in your project's platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

##### scopes: List[`str`]<a id="scopes-liststr"></a>

A list of custom OAuth2 scopes. Check each provider internal docs for a list of supported scopes. Maximum of 100 scopes are allowed, each 4096 characters long.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/tokens/oauth2/{provider}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.create_password_recovery`<a id="appwriteserveraccountcreate_password_recovery"></a>

Sends the user an email with a temporary secret key for password reset. When the user clicks the confirmation link he is redirected back to your app password reset URL with the secret key and email address values attached to the URL query string. Use the query string params to submit a request to the [PUT /account/recovery](https://appwrite.io/docs/references/cloud/client-web/account#updateRecovery) endpoint to complete the process. The verification link sent to the user's email address is valid for 1 hour.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_password_recovery_response = appwriteserver.account.create_password_recovery(
    email="email@example.com",
    url="https://example.com",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

User email.

##### url: `str`<a id="url-str"></a>

URL to redirect the user back to your app from the recovery email. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreatePasswordRecoveryRequest`](./appwrite_server_python_sdk/type/account_create_password_recovery_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_server_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/recovery` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.create_phone_token`<a id="appwriteserveraccountcreate_phone_token"></a>

Sends the user an SMS with a secret key for creating a session. If the provided user ID has not be registered, a new user will be created. Use the returned user ID and secret and submit a request to the [POST /v1/account/sessions/token](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint to complete the login process. The secret sent to the user's phone is valid for 15 minutes.

A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_phone_token_response = appwriteserver.account.create_phone_token(
    user_id="<USER_ID>",
    phone="+12065550100",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### phone: `str`<a id="phone-str"></a>

Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreatePhoneTokenRequest`](./appwrite_server_python_sdk/type/account_create_phone_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_server_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/tokens/phone` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.create_phone_verification`<a id="appwriteserveraccountcreate_phone_verification"></a>

Use this endpoint to send a verification SMS to the currently logged in user. This endpoint is meant for use after updating a user's phone number using the [accountUpdatePhone](https://appwrite.io/docs/references/cloud/client-web/account#updatePhone) endpoint. Learn more about how to [complete the verification process](https://appwrite.io/docs/references/cloud/client-web/account#updatePhoneVerification). The verification code sent to the user's phone number is valid for 15 minutes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_phone_verification_response = appwriteserver.account.create_phone_verification()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_server_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/verification/phone` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.create_token_session`<a id="appwriteserveraccountcreate_token_session"></a>

Use this endpoint to create a session from token. Provide the **userId** and **secret** parameters from the successful response of authentication flows initiated by token creation. For example, magic URL and phone login.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_token_session_response = appwriteserver.account.create_token_session(
    user_id="<USER_ID>",
    secret="<SECRET>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### secret: `str`<a id="secret-str"></a>

Secret of a token generated by login methods. For example, the `createMagicURLToken` or `createPhoneToken` methods.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreateTokenSessionRequest`](./appwrite_server_python_sdk/type/account_create_token_session_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_server_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.delete_authenticator_by_id`<a id="appwriteserveraccountdelete_authenticator_by_id"></a>

Delete an authenticator for a user by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_authenticator_by_id_response = appwriteserver.account.delete_authenticator_by_id(
    otp="<OTP>",
    type="totp",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### otp: `str`<a id="otp-str"></a>

Valid verification token.

##### type: `str`<a id="type-str"></a>

Type of authenticator.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountDeleteAuthenticatorByIdRequest`](./appwrite_server_python_sdk/type/account_delete_authenticator_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/authenticators/{type}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.delete_identity_by_id`<a id="appwriteserveraccountdelete_identity_by_id"></a>

Delete an identity by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.account.delete_identity_by_id(
    identity_id="identityId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### identity_id: `str`<a id="identity_id-str"></a>

Identity ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/identities/{identityId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.delete_user_sessions`<a id="appwriteserveraccountdelete_user_sessions"></a>

Delete all sessions from the user account and remove any sessions cookies from the end client.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.account.delete_user_sessions()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.extend_session_length`<a id="appwriteserveraccountextend_session_length"></a>

Use this endpoint to extend a session's length. Extending a session is useful when session expiry is short. If the session was created using an OAuth provider, this endpoint refreshes the access token from the provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
extend_session_length_response = appwriteserver.account.extend_session_length(
    session_id="sessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

Session ID. Use the string 'current' to update the current device session.

#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_server_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/{sessionId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.generate_recovery_codes`<a id="appwriteserveraccountgenerate_recovery_codes"></a>

Generate recovery codes as backup for MFA flow. It's recommended to generate and show then immediately after user successfully adds their authehticator. Recovery codes can be used as a MFA verification type in [createMfaChallenge](/docs/references/cloud/client-web/account#createMfaChallenge) method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_recovery_codes_response = appwriteserver.account.generate_recovery_codes()
```

#### 🔄 Return<a id="🔄-return"></a>

[`MfaRecoveryCodes`](./appwrite_server_python_sdk/pydantic/mfa_recovery_codes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/recovery-codes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.get_current_user`<a id="appwriteserveraccountget_current_user"></a>

Get the currently logged in user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_current_user_response = appwriteserver.account.get_current_user()
```

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.get_mfa_recovery_codes`<a id="appwriteserveraccountget_mfa_recovery_codes"></a>

Get recovery codes that can be used as backup for MFA flow. Before getting codes, they must be generated using [createMfaRecoveryCodes](/docs/references/cloud/client-web/account#createMfaRecoveryCodes) method. An OTP challenge is required to read recovery codes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_mfa_recovery_codes_response = appwriteserver.account.get_mfa_recovery_codes()
```

#### 🔄 Return<a id="🔄-return"></a>

[`MfaRecoveryCodes`](./appwrite_server_python_sdk/pydantic/mfa_recovery_codes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/recovery-codes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.get_prefs`<a id="appwriteserveraccountget_prefs"></a>

Get the preferences as a key-value object for the currently logged in user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_prefs_response = appwriteserver.account.get_prefs()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Preferences`](./appwrite_server_python_sdk/pydantic/preferences.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/prefs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.get_session_by_id`<a id="appwriteserveraccountget_session_by_id"></a>

Use this endpoint to get a logged in user's session using a Session ID. Inputting 'current' will return the current session being used.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_session_by_id_response = appwriteserver.account.get_session_by_id(
    session_id="sessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

Session ID. Use the string 'current' to get the current device session.

#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_server_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/{sessionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.list_identities`<a id="appwriteserveraccountlist_identities"></a>

Get the list of identities for the currently logged in user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_identities_response = appwriteserver.account.list_identities(
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, provider, providerUid, providerEmail, providerAccessTokenExpiry

#### 🔄 Return<a id="🔄-return"></a>

[`IdentityList`](./appwrite_server_python_sdk/pydantic/identity_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/identities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.list_logs`<a id="appwriteserveraccountlist_logs"></a>

Get the list of latest security activity logs for the currently logged in user. Each log returns user IP address, location and date and time of log.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_logs_response = appwriteserver.account.list_logs(
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset

#### 🔄 Return<a id="🔄-return"></a>

[`LogList`](./appwrite_server_python_sdk/pydantic/log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.list_mfa_factors`<a id="appwriteserveraccountlist_mfa_factors"></a>

List the factors available on the account to be used as a MFA challange.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_mfa_factors_response = appwriteserver.account.list_mfa_factors()
```

#### 🔄 Return<a id="🔄-return"></a>

[`MfaFactors`](./appwrite_server_python_sdk/pydantic/mfa_factors.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/factors` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.list_sessions`<a id="appwriteserveraccountlist_sessions"></a>

Get the list of active sessions across different devices for the currently logged in user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_sessions_response = appwriteserver.account.list_sessions()
```

#### 🔄 Return<a id="🔄-return"></a>

[`SessionList`](./appwrite_server_python_sdk/pydantic/session_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.logout_session_by_id`<a id="appwriteserveraccountlogout_session_by_id"></a>

Logout the user. Use 'current' as the session ID to logout on this device, use a session ID to logout on another device. If you're looking to logout the user on all devices, use [Delete Sessions](https://appwrite.io/docs/references/cloud/client-web/account#deleteSessions) instead.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.account.logout_session_by_id(
    session_id="sessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

Session ID. Use the string 'current' to delete the current device session.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/{sessionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.regenerate_mfa_recovery_codes`<a id="appwriteserveraccountregenerate_mfa_recovery_codes"></a>

Regenerate recovery codes that can be used as backup for MFA flow. Before regenerating codes, they must be first generated using [createMfaRecoveryCodes](/docs/references/cloud/client-web/account#createMfaRecoveryCodes) method. An OTP challenge is required to regenreate recovery codes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
regenerate_mfa_recovery_codes_response = (
    appwriteserver.account.regenerate_mfa_recovery_codes()
)
```

#### 🔄 Return<a id="🔄-return"></a>

[`MfaRecoveryCodes`](./appwrite_server_python_sdk/pydantic/mfa_recovery_codes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/recovery-codes` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.update_email_address`<a id="appwriteserveraccountupdate_email_address"></a>

Update currently logged in user account email address. After changing user address, the user confirmation status will get reset. A new confirmation email is not sent automatically however you can use the send confirmation email endpoint again to send the confirmation email. For security measures, user password is required to complete this request.
This endpoint can also be used to convert an anonymous account to a normal one, by passing an email address and a new password.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_email_address_response = appwriteserver.account.update_email_address(
    email="email@example.com",
    password="password",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password. Must be at least 8 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdateEmailAddressRequest`](./appwrite_server_python_sdk/type/account_update_email_address_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/email` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.update_magic_url_session`<a id="appwriteserveraccountupdate_magic_url_session"></a>

Use this endpoint to create a session from token. Provide the **userId** and **secret** parameters from the successful response of authentication flows initiated by token creation. For example, magic URL and phone login.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_magic_url_session_response = appwriteserver.account.update_magic_url_session(
    user_id="<USER_ID>",
    secret="<SECRET>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### secret: `str`<a id="secret-str"></a>

Valid verification token.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdateMagicUrlSessionRequest`](./appwrite_server_python_sdk/type/account_update_magic_url_session_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_server_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/magic-url` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.update_mfa_status`<a id="appwriteserveraccountupdate_mfa_status"></a>

Enable or disable MFA on an account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_mfa_status_response = appwriteserver.account.update_mfa_status(
    mfa=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### mfa: `bool`<a id="mfa-bool"></a>

Enable or disable MFA.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdateMfaStatusRequest`](./appwrite_server_python_sdk/type/account_update_mfa_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.update_name_operation`<a id="appwriteserveraccountupdate_name_operation"></a>

Update currently logged in user account name.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_name_operation_response = appwriteserver.account.update_name_operation(
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdateNameOperationRequest`](./appwrite_server_python_sdk/type/account_update_name_operation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/name` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.update_password_operation`<a id="appwriteserveraccountupdate_password_operation"></a>

Update currently logged in user password. For validation, user is required to pass in the new password, and the old password. For users created with OAuth, Team Invites and Magic URL, oldPassword is optional.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_password_operation_response = appwriteserver.account.update_password_operation(
    password="string_example",
    old_password="password",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### password: `str`<a id="password-str"></a>

New user password. Must be at least 8 chars.

##### old_password: `str`<a id="old_password-str"></a>

Current user password. Must be at least 8 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdatePasswordOperationRequest`](./appwrite_server_python_sdk/type/account_update_password_operation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/password` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.update_phone`<a id="appwriteserveraccountupdate_phone"></a>

Update the currently logged in user's phone number. After updating the phone number, the phone verification status will be reset. A confirmation SMS is not sent automatically, however you can use the [POST /account/verification/phone](https://appwrite.io/docs/references/cloud/client-web/account#createPhoneVerification) endpoint to send a confirmation SMS.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_phone_response = appwriteserver.account.update_phone(
    phone="+12065550100",
    password="password",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### phone: `str`<a id="phone-str"></a>

Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

##### password: `str`<a id="password-str"></a>

User password. Must be at least 8 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdatePhoneRequest`](./appwrite_server_python_sdk/type/account_update_phone_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/phone` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.update_phone_session`<a id="appwriteserveraccountupdate_phone_session"></a>

Use this endpoint to create a session from token. Provide the **userId** and **secret** parameters from the successful response of authentication flows initiated by token creation. For example, magic URL and phone login.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_phone_session_response = appwriteserver.account.update_phone_session(
    user_id="<USER_ID>",
    secret="<SECRET>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### secret: `str`<a id="secret-str"></a>

Valid verification token.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdatePhoneSessionRequest`](./appwrite_server_python_sdk/type/account_update_phone_session_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_server_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/phone` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.update_preferences`<a id="appwriteserveraccountupdate_preferences"></a>

Update currently logged in user account preferences. The object you pass is stored as is, and replaces any previous value. The maximum allowed prefs size is 64kB and throws error if exceeded.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_preferences_response = appwriteserver.account.update_preferences(
    prefs={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### prefs: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="prefs-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Prefs key-value JSON object.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdatePreferencesRequest`](./appwrite_server_python_sdk/type/account_update_preferences_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/prefs` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.account.verify_authenticator`<a id="appwriteserveraccountverify_authenticator"></a>

Verify an authenticator app after adding it using the [add authenticator](/docs/references/cloud/client-web/account#addAuthenticator) method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_authenticator_response = appwriteserver.account.verify_authenticator(
    otp="<OTP>",
    type="totp",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### otp: `str`<a id="otp-str"></a>

Valid verification token.

##### type: `str`<a id="type-str"></a>

Type of authenticator.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountVerifyAuthenticatorRequest`](./appwrite_server_python_sdk/type/account_verify_authenticator_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/authenticators/{type}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.avatars.generate_qr_code`<a id="appwriteserveravatarsgenerate_qr_code"></a>

Converts a given plain text to a QR code image. You can use the query parameters to change the size and style of the resulting image.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.avatars.generate_qr_code(
    text="text_example",
    size=400,
    margin=1,
    download=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### text: `str`<a id="text-str"></a>

Plain text to be converted to QR code image.

##### size: `int`<a id="size-int"></a>

QR code size. Pass an integer between 1 to 1000. Defaults to 400.

##### margin: `int`<a id="margin-int"></a>

Margin from edge. Pass an integer between 0 to 10. Defaults to 1.

##### download: `bool`<a id="download-bool"></a>

Return resulting image with 'Content-Disposition: attachment ' headers for the browser to start downloading it. Pass 0 for no header, or 1 for otherwise. Default value is set to 0.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars/qr` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.avatars.get_browser_icon`<a id="appwriteserveravatarsget_browser_icon"></a>

You can use this endpoint to show different browser icons to your users. The code argument receives the browser code as it appears in your user [GET /account/sessions](https://appwrite.io/docs/references/cloud/client-web/account#getSessions) endpoint. Use width, height and quality arguments to change the output settings.

When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 100x100px.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.avatars.get_browser_icon(
    code="aa",
    width=100,
    height=100,
    quality=100,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Browser Code.

##### width: `int`<a id="width-int"></a>

Image width. Pass an integer between 0 to 2000. Defaults to 100.

##### height: `int`<a id="height-int"></a>

Image height. Pass an integer between 0 to 2000. Defaults to 100.

##### quality: `int`<a id="quality-int"></a>

Image quality. Pass an integer between 0 to 100. Defaults to 100.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars/browsers/{code}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.avatars.get_country_flag`<a id="appwriteserveravatarsget_country_flag"></a>

You can use this endpoint to show different country flags icons to your users. The code argument receives the 2 letter country code. Use width, height and quality arguments to change the output settings. Country codes follow the [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) standard.

When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 100x100px.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.avatars.get_country_flag(
    code="af",
    width=100,
    height=100,
    quality=100,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Country Code. ISO Alpha-2 country code format.

##### width: `int`<a id="width-int"></a>

Image width. Pass an integer between 0 to 2000. Defaults to 100.

##### height: `int`<a id="height-int"></a>

Image height. Pass an integer between 0 to 2000. Defaults to 100.

##### quality: `int`<a id="quality-int"></a>

Image quality. Pass an integer between 0 to 100. Defaults to 100.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars/flags/{code}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.avatars.get_credit_card_icon`<a id="appwriteserveravatarsget_credit_card_icon"></a>

The credit card endpoint will return you the icon of the credit card provider you need. Use width, height and quality arguments to change the output settings.

When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 100x100px.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.avatars.get_credit_card_icon(
    code="amex",
    width=100,
    height=100,
    quality=100,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Credit Card Code. Possible values: amex, argencard, cabal, censosud, diners, discover, elo, hipercard, jcb, mastercard, naranja, targeta-shopping, union-china-pay, visa, mir, maestro.

##### width: `int`<a id="width-int"></a>

Image width. Pass an integer between 0 to 2000. Defaults to 100.

##### height: `int`<a id="height-int"></a>

Image height. Pass an integer between 0 to 2000. Defaults to 100.

##### quality: `int`<a id="quality-int"></a>

Image quality. Pass an integer between 0 to 100. Defaults to 100.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars/credit-cards/{code}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.avatars.get_favicon`<a id="appwriteserveravatarsget_favicon"></a>

Use this endpoint to fetch the favorite icon (AKA favicon) of any remote website URL.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.avatars.get_favicon(
    url="url_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

Website URL which you want to fetch the favicon from.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars/favicon` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.avatars.get_remote_image`<a id="appwriteserveravatarsget_remote_image"></a>

Use this endpoint to fetch a remote image URL and crop it to any image size you want. This endpoint is very useful if you need to crop and display remote images in your app or in case you want to make sure a 3rd party image is properly served using a TLS protocol.

When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 400x400px.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.avatars.get_remote_image(
    url="url_example",
    width=400,
    height=400,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

Image URL which you want to crop.

##### width: `int`<a id="width-int"></a>

Resize preview image width, Pass an integer between 0 to 2000. Defaults to 400.

##### height: `int`<a id="height-int"></a>

Resize preview image height, Pass an integer between 0 to 2000. Defaults to 400.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars/image` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.avatars.get_user_initials`<a id="appwriteserveravatarsget_user_initials"></a>

Use this endpoint to show your user initials avatar icon on your website or app. By default, this route will try to print your logged-in user name or email initials. You can also overwrite the user name if you pass the 'name' parameter. If no name is given and no user is logged, an empty avatar will be returned.

You can use the color and background params to change the avatar colors. By default, a random theme will be selected. The random theme will persist for the user's initials when reloading the same theme will always return for the same initials.

When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 100x100px.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.avatars.get_user_initials(
    name="",
    width=500,
    height=500,
    background="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Full Name. When empty, current user name or email will be used. Max length: 128 chars.

##### width: `int`<a id="width-int"></a>

Image width. Pass an integer between 0 to 2000. Defaults to 100.

##### height: `int`<a id="height-int"></a>

Image height. Pass an integer between 0 to 2000. Defaults to 100.

##### background: `str`<a id="background-str"></a>

Changes background color. By default a random color will be picked and stay will persistent to the given name.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars/initials` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.create_boolean_attribute`<a id="appwriteserverdatabasescreate_boolean_attribute"></a>

Create a boolean attribute.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_boolean_attribute_response = appwriteserver.databases.create_boolean_attribute(
    key="string_example",
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    default=False,
    array=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### default: `bool`<a id="default-bool"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateBooleanAttributeRequest`](./appwrite_server_python_sdk/type/databases_create_boolean_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeBoolean`](./appwrite_server_python_sdk/pydantic/attribute_boolean.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/boolean` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.create_collection`<a id="appwriteserverdatabasescreate_collection"></a>

Create a new Collection. Before using this route, you should create a new database resource using either a [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection) API or directly from your database console.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_collection_response = appwriteserver.databases.create_collection(
    collection_id="<COLLECTION_ID>",
    name="<NAME>",
    database_id="databaseId_example",
    permissions=['["read("any")"]'],
    document_security=False,
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### collection_id: `str`<a id="collection_id-str"></a>

Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Collection name. Max length: 128 chars.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### permissions: [`DatabasesCreateCollectionRequestPermissions`](./appwrite_server_python_sdk/type/databases_create_collection_request_permissions.py)<a id="permissions-databasescreatecollectionrequestpermissionsappwrite_server_python_sdktypedatabases_create_collection_request_permissionspy"></a>

##### document_security: `bool`<a id="document_security-bool"></a>

Enables configuring permissions for individual documents. A user needs one of document or collection level permissions to access a document. [Learn more about permissions](https://appwrite.io/docs/permissions).

##### enabled: `bool`<a id="enabled-bool"></a>

Is collection enabled? When set to 'disabled', users cannot access the collection but Server SDKs with and API key can still read and write to the collection. No data is lost when this is toggled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateCollectionRequest`](./appwrite_server_python_sdk/type/databases_create_collection_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Collection`](./appwrite_server_python_sdk/pydantic/collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.create_database`<a id="appwriteserverdatabasescreate_database"></a>

Create a new Database.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_database_response = appwriteserver.databases.create_database(
    database_id="<DATABASE_ID>",
    name="<NAME>",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Database name. Max length: 128 chars.

##### enabled: `bool`<a id="enabled-bool"></a>

Is the database enabled? When set to 'disabled', users cannot access the database but Server SDKs with an API key can still read and write to the database. No data is lost when this is toggled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateDatabaseRequest`](./appwrite_server_python_sdk/type/databases_create_database_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Database`](./appwrite_server_python_sdk/pydantic/database.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.create_datetime_attribute`<a id="appwriteserverdatabasescreate_datetime_attribute"></a>

Create a date time attribute according to the ISO 8601 standard.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_datetime_attribute_response = appwriteserver.databases.create_datetime_attribute(
    key="string_example",
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    default="string_example",
    array=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### default: `str`<a id="default-str"></a>

Default value for the attribute in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateDatetimeAttributeRequest`](./appwrite_server_python_sdk/type/databases_create_datetime_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeDatetime`](./appwrite_server_python_sdk/pydantic/attribute_datetime.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/datetime` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.create_document`<a id="appwriteserverdatabasescreate_document"></a>

Create a new Document. Before using this route, you should create a new collection resource using either a [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection) API or directly from your database console.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_document_response = appwriteserver.databases.create_document(
    document_id="<DOCUMENT_ID>",
    data={},
    database_id="databaseId_example",
    collection_id="collectionId_example",
    permissions=['["read("any")"]'],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### document_id: `str`<a id="document_id-str"></a>

Document ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### data: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="data-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Document data as JSON object.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection). Make sure to define attributes before creating documents.

##### permissions: [`DatabasesCreateDocumentRequestPermissions`](./appwrite_server_python_sdk/type/databases_create_document_request_permissions.py)<a id="permissions-databasescreatedocumentrequestpermissionsappwrite_server_python_sdktypedatabases_create_document_request_permissionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateDocumentRequest`](./appwrite_server_python_sdk/type/databases_create_document_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Document`](./appwrite_server_python_sdk/pydantic/document.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/documents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.create_email_attribute`<a id="appwriteserverdatabasescreate_email_attribute"></a>

Create an email attribute.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_email_attribute_response = appwriteserver.databases.create_email_attribute(
    key="string_example",
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    default="email@example.com",
    array=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### default: `str`<a id="default-str"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateEmailAttributeRequest`](./appwrite_server_python_sdk/type/databases_create_email_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeEmail`](./appwrite_server_python_sdk/pydantic/attribute_email.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/email` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.create_enum_attribute`<a id="appwriteserverdatabasescreate_enum_attribute"></a>

Create an enumeration attribute. The `elements` param acts as a white-list of accepted values for this attribute. 


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_enum_attribute_response = appwriteserver.databases.create_enum_attribute(
    key="string_example",
    elements=["string_example"],
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    default="<DEFAULT>",
    array=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### elements: [`DatabasesCreateEnumAttributeRequestElements`](./appwrite_server_python_sdk/type/databases_create_enum_attribute_request_elements.py)<a id="elements-databasescreateenumattributerequestelementsappwrite_server_python_sdktypedatabases_create_enum_attribute_request_elementspy"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### default: `str`<a id="default-str"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateEnumAttributeRequest`](./appwrite_server_python_sdk/type/databases_create_enum_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeEnum`](./appwrite_server_python_sdk/pydantic/attribute_enum.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/enum` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.create_float_attribute`<a id="appwriteserverdatabasescreate_float_attribute"></a>

Create a float attribute. Optionally, minimum and maximum values can be provided.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_float_attribute_response = appwriteserver.databases.create_float_attribute(
    key="string_example",
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    min=3.14,
    max=3.14,
    default=3.14,
    array=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### min: `Union[int, float]`<a id="min-unionint-float"></a>

Minimum value to enforce on new documents

##### max: `Union[int, float]`<a id="max-unionint-float"></a>

Maximum value to enforce on new documents

##### default: `Union[int, float]`<a id="default-unionint-float"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateFloatAttributeRequest`](./appwrite_server_python_sdk/type/databases_create_float_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeFloat`](./appwrite_server_python_sdk/pydantic/attribute_float.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/float` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.create_index`<a id="appwriteserverdatabasescreate_index"></a>

Creates an index on the attributes listed. Your index should include all the attributes you will query in a single request.
Attributes can be `key`, `fulltext`, and `unique`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_index_response = appwriteserver.databases.create_index(
    key="string_example",
    type="key",
    attributes=["string_example"],
    database_id="databaseId_example",
    collection_id="collectionId_example",
    orders=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Index Key.

##### type: `str`<a id="type-str"></a>

Index type.

##### attributes: [`DatabasesCreateIndexRequestAttributes`](./appwrite_server_python_sdk/type/databases_create_index_request_attributes.py)<a id="attributes-databasescreateindexrequestattributesappwrite_server_python_sdktypedatabases_create_index_request_attributespy"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### orders: [`DatabasesCreateIndexRequestOrders`](./appwrite_server_python_sdk/type/databases_create_index_request_orders.py)<a id="orders-databasescreateindexrequestordersappwrite_server_python_sdktypedatabases_create_index_request_orderspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateIndexRequest`](./appwrite_server_python_sdk/type/databases_create_index_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Index`](./appwrite_server_python_sdk/pydantic/index.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/indexes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.create_integer_attribute`<a id="appwriteserverdatabasescreate_integer_attribute"></a>

Create an integer attribute. Optionally, minimum and maximum values can be provided.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_integer_attribute_response = appwriteserver.databases.create_integer_attribute(
    key="string_example",
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    min=1,
    max=1,
    default=1,
    array=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### min: `int`<a id="min-int"></a>

Minimum value to enforce on new documents

##### max: `int`<a id="max-int"></a>

Maximum value to enforce on new documents

##### default: `int`<a id="default-int"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateIntegerAttributeRequest`](./appwrite_server_python_sdk/type/databases_create_integer_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeInteger`](./appwrite_server_python_sdk/pydantic/attribute_integer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/integer` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.create_ip_attribute`<a id="appwriteserverdatabasescreate_ip_attribute"></a>

Create IP address attribute.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_ip_attribute_response = appwriteserver.databases.create_ip_attribute(
    key="string_example",
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    default="string_example",
    array=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### default: `str`<a id="default-str"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateIpAttributeRequest`](./appwrite_server_python_sdk/type/databases_create_ip_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeIp`](./appwrite_server_python_sdk/pydantic/attribute_ip.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/ip` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.create_relationship_attribute`<a id="appwriteserverdatabasescreate_relationship_attribute"></a>

Create relationship attribute. [Learn more about relationship attributes](https://appwrite.io/docs/databases-relationships#relationship-attributes).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_relationship_attribute_response = (
    appwriteserver.databases.create_relationship_attribute(
        related_collection_id="<RELATED_COLLECTION_ID>",
        type="oneToOne",
        database_id="databaseId_example",
        collection_id="collectionId_example",
        two_way=False,
        key="string_example",
        two_way_key="string_example",
        on_delete="cascade",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### related_collection_id: `str`<a id="related_collection_id-str"></a>

Related Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### type: `str`<a id="type-str"></a>

Relation type

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### two_way: `bool`<a id="two_way-bool"></a>

Is Two Way?

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### two_way_key: `str`<a id="two_way_key-str"></a>

Two Way Attribute Key.

##### on_delete: `str`<a id="on_delete-str"></a>

Constraints option

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateRelationshipAttributeRequest`](./appwrite_server_python_sdk/type/databases_create_relationship_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeRelationship`](./appwrite_server_python_sdk/pydantic/attribute_relationship.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/relationship` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.create_string_attribute`<a id="appwriteserverdatabasescreate_string_attribute"></a>

Create a string attribute.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_string_attribute_response = appwriteserver.databases.create_string_attribute(
    key="string_example",
    size=1,
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    default="<DEFAULT>",
    array=False,
    encrypt=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### size: `int`<a id="size-int"></a>

Attribute size for text attributes, in number of characters.

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### default: `str`<a id="default-str"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

##### encrypt: `bool`<a id="encrypt-bool"></a>

Toggle encryption for the attribute. Encryption enhances security by not storing any plain text values in the database. However, encrypted attributes cannot be queried.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateStringAttributeRequest`](./appwrite_server_python_sdk/type/databases_create_string_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeString`](./appwrite_server_python_sdk/pydantic/attribute_string.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/string` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.create_url_attribute`<a id="appwriteserverdatabasescreate_url_attribute"></a>

Create a URL attribute.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_url_attribute_response = appwriteserver.databases.create_url_attribute(
    key="string_example",
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    default="https://example.com",
    array=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### default: `str`<a id="default-str"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateUrlAttributeRequest`](./appwrite_server_python_sdk/type/databases_create_url_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeUrl`](./appwrite_server_python_sdk/pydantic/attribute_url.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/url` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.delete_attribute_by_id`<a id="appwriteserverdatabasesdelete_attribute_by_id"></a>

Deletes an attribute.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.databases.delete_attribute_by_id(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/{key}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.delete_by_id`<a id="appwriteserverdatabasesdelete_by_id"></a>

Delete a database by its unique ID. Only API keys with with databases.write scope can delete a database.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.databases.delete_by_id(
    database_id="databaseId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.delete_collection_by_id`<a id="appwriteserverdatabasesdelete_collection_by_id"></a>

Delete a collection by its unique ID. Only users with write permissions have access to delete this resource.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.databases.delete_collection_by_id(
    database_id="databaseId_example",
    collection_id="collectionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.delete_document_by_id`<a id="appwriteserverdatabasesdelete_document_by_id"></a>

Delete a document by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.databases.delete_document_by_id(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    document_id="documentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### document_id: `str`<a id="document_id-str"></a>

Document ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/documents/{documentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.delete_index`<a id="appwriteserverdatabasesdelete_index"></a>

Delete an index.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.databases.delete_index(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Index Key.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/indexes/{key}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.get_attribute_by_id`<a id="appwriteserverdatabasesget_attribute_by_id"></a>

Get attribute by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_attribute_by_id_response = appwriteserver.databases.get_attribute_by_id(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### 🔄 Return<a id="🔄-return"></a>

[`DatabasesGetAttributeByIdResponse`](./appwrite_server_python_sdk/pydantic/databases_get_attribute_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/{key}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.get_by_id`<a id="appwriteserverdatabasesget_by_id"></a>

Get a database by its unique ID. This endpoint response returns a JSON object with the database metadata.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = appwriteserver.databases.get_by_id(
    database_id="databaseId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Database`](./appwrite_server_python_sdk/pydantic/database.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.get_collection_by_id`<a id="appwriteserverdatabasesget_collection_by_id"></a>

Get a collection by its unique ID. This endpoint response returns a JSON object with the collection metadata.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_by_id_response = appwriteserver.databases.get_collection_by_id(
    database_id="databaseId_example",
    collection_id="collectionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Collection`](./appwrite_server_python_sdk/pydantic/collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.get_document_by_id`<a id="appwriteserverdatabasesget_document_by_id"></a>

Get a document by its unique ID. This endpoint response returns a JSON object with the document data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_document_by_id_response = appwriteserver.databases.get_document_by_id(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    document_id="documentId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### document_id: `str`<a id="document_id-str"></a>

Document ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.

#### 🔄 Return<a id="🔄-return"></a>

[`Document`](./appwrite_server_python_sdk/pydantic/document.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/documents/{documentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.get_index_by_id`<a id="appwriteserverdatabasesget_index_by_id"></a>

Get index by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_index_by_id_response = appwriteserver.databases.get_index_by_id(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Index Key.

#### 🔄 Return<a id="🔄-return"></a>

[`Index`](./appwrite_server_python_sdk/pydantic/index.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/indexes/{key}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.list_all`<a id="appwriteserverdatabaseslist_all"></a>

Get a list of all databases from the current Appwrite project. You can use the search parameter to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = appwriteserver.databases.list_all(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`DatabaseList`](./appwrite_server_python_sdk/pydantic/database_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.list_collection_attributes`<a id="appwriteserverdatabaseslist_collection_attributes"></a>

List attributes in the collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_collection_attributes_response = (
    appwriteserver.databases.list_collection_attributes(
        database_id="databaseId_example",
        collection_id="collectionId_example",
        queries=[],
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: key, type, size, required, array, status, error

#### 🔄 Return<a id="🔄-return"></a>

[`AttributeList`](./appwrite_server_python_sdk/pydantic/attribute_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.list_collection_documents`<a id="appwriteserverdatabaseslist_collection_documents"></a>

Get a list of all the user's documents in a given collection. You can use the query params to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_collection_documents_response = appwriteserver.databases.list_collection_documents(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.

#### 🔄 Return<a id="🔄-return"></a>

[`DocumentList`](./appwrite_server_python_sdk/pydantic/document_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/documents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.list_collections`<a id="appwriteserverdatabaseslist_collections"></a>

Get a list of all collections that belong to the provided databaseId. You can use the search parameter to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_collections_response = appwriteserver.databases.list_collections(
    database_id="databaseId_example",
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, enabled, documentSecurity

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`CollectionList`](./appwrite_server_python_sdk/pydantic/collection_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.list_indexes`<a id="appwriteserverdatabaseslist_indexes"></a>

List indexes in the collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_indexes_response = appwriteserver.databases.list_indexes(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: key, type, status, attributes, error

#### 🔄 Return<a id="🔄-return"></a>

[`IndexList`](./appwrite_server_python_sdk/pydantic/index_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/indexes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.update_boolean_attribute`<a id="appwriteserverdatabasesupdate_boolean_attribute"></a>

Update a boolean attribute. Changing the `default` value will not update already existing documents.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_boolean_attribute_response = appwriteserver.databases.update_boolean_attribute(
    required=False,
    default=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### default: `Optional[bool]`<a id="default-optionalbool"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateBooleanAttributeRequest`](./appwrite_server_python_sdk/type/databases_update_boolean_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeBoolean`](./appwrite_server_python_sdk/pydantic/attribute_boolean.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/boolean/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.update_by_id`<a id="appwriteserverdatabasesupdate_by_id"></a>

Update a database by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = appwriteserver.databases.update_by_id(
    name="<NAME>",
    database_id="databaseId_example",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Database name. Max length: 128 chars.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### enabled: `bool`<a id="enabled-bool"></a>

Is database enabled? When set to 'disabled', users cannot access the database but Server SDKs with an API key can still read and write to the database. No data is lost when this is toggled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateByIdRequest`](./appwrite_server_python_sdk/type/databases_update_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Database`](./appwrite_server_python_sdk/pydantic/database.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.update_collection_by_id`<a id="appwriteserverdatabasesupdate_collection_by_id"></a>

Update a collection by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_collection_by_id_response = appwriteserver.databases.update_collection_by_id(
    name="<NAME>",
    database_id="databaseId_example",
    collection_id="collectionId_example",
    permissions=['["read("any")"]'],
    document_security=False,
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Collection name. Max length: 128 chars.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID.

##### permissions: [`DatabasesUpdateCollectionByIdRequestPermissions`](./appwrite_server_python_sdk/type/databases_update_collection_by_id_request_permissions.py)<a id="permissions-databasesupdatecollectionbyidrequestpermissionsappwrite_server_python_sdktypedatabases_update_collection_by_id_request_permissionspy"></a>

##### document_security: `bool`<a id="document_security-bool"></a>

Enables configuring permissions for individual documents. A user needs one of document or collection level permissions to access a document. [Learn more about permissions](https://appwrite.io/docs/permissions).

##### enabled: `bool`<a id="enabled-bool"></a>

Is collection enabled? When set to 'disabled', users cannot access the collection but Server SDKs with and API key can still read and write to the collection. No data is lost when this is toggled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateCollectionByIdRequest`](./appwrite_server_python_sdk/type/databases_update_collection_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Collection`](./appwrite_server_python_sdk/pydantic/collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.update_datetime_attribute`<a id="appwriteserverdatabasesupdate_datetime_attribute"></a>

Update a date time attribute. Changing the `default` value will not update already existing documents.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_datetime_attribute_response = appwriteserver.databases.update_datetime_attribute(
    required=False,
    default="string_example",
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### default: `Optional[str]`<a id="default-optionalstr"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateDatetimeAttributeRequest`](./appwrite_server_python_sdk/type/databases_update_datetime_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeDatetime`](./appwrite_server_python_sdk/pydantic/attribute_datetime.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/datetime/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.update_document_by_id`<a id="appwriteserverdatabasesupdate_document_by_id"></a>

Update a document by its unique ID. Using the patch method you can pass only specific fields that will get updated.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_document_by_id_response = appwriteserver.databases.update_document_by_id(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    document_id="documentId_example",
    data={},
    permissions=['["read("any")"]'],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID.

##### document_id: `str`<a id="document_id-str"></a>

Document ID.

##### data: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="data-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Document data as JSON object. Include only attribute and value pairs to be updated.

##### permissions: [`DatabasesUpdateDocumentByIdRequestPermissions`](./appwrite_server_python_sdk/type/databases_update_document_by_id_request_permissions.py)<a id="permissions-databasesupdatedocumentbyidrequestpermissionsappwrite_server_python_sdktypedatabases_update_document_by_id_request_permissionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateDocumentByIdRequest`](./appwrite_server_python_sdk/type/databases_update_document_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Document`](./appwrite_server_python_sdk/pydantic/document.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/documents/{documentId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.update_email_attribute`<a id="appwriteserverdatabasesupdate_email_attribute"></a>

Update an email attribute. Changing the `default` value will not update already existing documents.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_email_attribute_response = appwriteserver.databases.update_email_attribute(
    required=False,
    default="email@example.com",
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### default: `Optional[str]`<a id="default-optionalstr"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateEmailAttributeRequest`](./appwrite_server_python_sdk/type/databases_update_email_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeEmail`](./appwrite_server_python_sdk/pydantic/attribute_email.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/email/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.update_enum_attribute`<a id="appwriteserverdatabasesupdate_enum_attribute"></a>

Update an enum attribute. Changing the `default` value will not update already existing documents.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_enum_attribute_response = appwriteserver.databases.update_enum_attribute(
    elements=["string_example"],
    required=False,
    default="<DEFAULT>",
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### elements: [`DatabasesUpdateEnumAttributeRequestElements`](./appwrite_server_python_sdk/type/databases_update_enum_attribute_request_elements.py)<a id="elements-databasesupdateenumattributerequestelementsappwrite_server_python_sdktypedatabases_update_enum_attribute_request_elementspy"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### default: `Optional[str]`<a id="default-optionalstr"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateEnumAttributeRequest`](./appwrite_server_python_sdk/type/databases_update_enum_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeEnum`](./appwrite_server_python_sdk/pydantic/attribute_enum.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/enum/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.update_float_attribute`<a id="appwriteserverdatabasesupdate_float_attribute"></a>

Update a float attribute. Changing the `default` value will not update already existing documents.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_float_attribute_response = appwriteserver.databases.update_float_attribute(
    required=False,
    min=3.14,
    max=3.14,
    default=3.14,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### min: `Union[int, float]`<a id="min-unionint-float"></a>

Minimum value to enforce on new documents

##### max: `Union[int, float]`<a id="max-unionint-float"></a>

Maximum value to enforce on new documents

##### default: `Optional[Union[int, float]]`<a id="default-optionalunionint-float"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateFloatAttributeRequest`](./appwrite_server_python_sdk/type/databases_update_float_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeFloat`](./appwrite_server_python_sdk/pydantic/attribute_float.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/float/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.update_integer_attribute`<a id="appwriteserverdatabasesupdate_integer_attribute"></a>

Update an integer attribute. Changing the `default` value will not update already existing documents.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_integer_attribute_response = appwriteserver.databases.update_integer_attribute(
    required=False,
    min=1,
    max=1,
    default=1,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### min: `int`<a id="min-int"></a>

Minimum value to enforce on new documents

##### max: `int`<a id="max-int"></a>

Maximum value to enforce on new documents

##### default: `Optional[int]`<a id="default-optionalint"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateIntegerAttributeRequest`](./appwrite_server_python_sdk/type/databases_update_integer_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeInteger`](./appwrite_server_python_sdk/pydantic/attribute_integer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/integer/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.update_ip_attribute`<a id="appwriteserverdatabasesupdate_ip_attribute"></a>

Update an ip attribute. Changing the `default` value will not update already existing documents.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_ip_attribute_response = appwriteserver.databases.update_ip_attribute(
    required=False,
    default="string_example",
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### default: `Optional[str]`<a id="default-optionalstr"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateIpAttributeRequest`](./appwrite_server_python_sdk/type/databases_update_ip_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeIp`](./appwrite_server_python_sdk/pydantic/attribute_ip.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/ip/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.update_relationship_attribute`<a id="appwriteserverdatabasesupdate_relationship_attribute"></a>

Update relationship attribute. [Learn more about relationship attributes](https://appwrite.io/docs/databases-relationships#relationship-attributes).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_relationship_attribute_response = (
    appwriteserver.databases.update_relationship_attribute(
        database_id="databaseId_example",
        collection_id="collectionId_example",
        key="key_example",
        on_delete="cascade",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### on_delete: `str`<a id="on_delete-str"></a>

Constraints option

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateRelationshipAttributeRequest`](./appwrite_server_python_sdk/type/databases_update_relationship_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeRelationship`](./appwrite_server_python_sdk/pydantic/attribute_relationship.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/{key}/relationship` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.update_string_attribute`<a id="appwriteserverdatabasesupdate_string_attribute"></a>

Update a string attribute. Changing the `default` value will not update already existing documents.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_string_attribute_response = appwriteserver.databases.update_string_attribute(
    required=False,
    default="<DEFAULT>",
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### default: `Optional[str]`<a id="default-optionalstr"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateStringAttributeRequest`](./appwrite_server_python_sdk/type/databases_update_string_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeString`](./appwrite_server_python_sdk/pydantic/attribute_string.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/string/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.databases.update_url_attribute`<a id="appwriteserverdatabasesupdate_url_attribute"></a>

Update an url attribute. Changing the `default` value will not update already existing documents.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_url_attribute_response = appwriteserver.databases.update_url_attribute(
    required=False,
    default="https://example.com",
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### default: `Optional[str]`<a id="default-optionalstr"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateUrlAttributeRequest`](./appwrite_server_python_sdk/type/databases_update_url_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeUrl`](./appwrite_server_python_sdk/pydantic/attribute_url.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/url/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.create_build`<a id="appwriteserverfunctionscreate_build"></a>

Create a new build for an Appwrite Function deployment. This endpoint can be used to retry a failed build.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.functions.create_build(
    function_id="functionId_example",
    deployment_id="deploymentId_example",
    build_id="buildId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### deployment_id: `str`<a id="deployment_id-str"></a>

Deployment ID.

##### build_id: `str`<a id="build_id-str"></a>

Build unique ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/deployments/{deploymentId}/builds/{buildId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.create_deployment_function_code`<a id="appwriteserverfunctionscreate_deployment_function_code"></a>

Create a new function code deployment. Use this endpoint to upload a new version of your code function. To execute your newly uploaded code, you'll need to update the function's deployment to use your new deployment UID.

This endpoint accepts a tar.gz file compressed with your code. Make sure to include any dependencies your code has within the compressed file. You can learn more about code packaging in the [Appwrite Cloud Functions tutorial](https://appwrite.io/docs/functions).

Use the "command" param to set the entrypoint used to execute your code.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_deployment_function_code_response = (
    appwriteserver.functions.create_deployment_function_code(
        function_id="functionId_example",
        code="string_example",
        activate=False,
        entrypoint="<ENTRYPOINT>",
        commands="<COMMANDS>",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### code: `str`<a id="code-str"></a>

Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code directory, and the CLI will automatically package your code. Use a path that is within the current directory.

##### activate: `bool`<a id="activate-bool"></a>

Automatically activate the deployment when it is finished building.

##### entrypoint: `str`<a id="entrypoint-str"></a>

Entrypoint File.

##### commands: `str`<a id="commands-str"></a>

Build Commands.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FunctionsCreateDeploymentFunctionCodeRequest`](./appwrite_server_python_sdk/type/functions_create_deployment_function_code_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Deployment`](./appwrite_server_python_sdk/pydantic/deployment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/deployments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.create_new_function`<a id="appwriteserverfunctionscreate_new_function"></a>

Create a new function. You can pass a list of [permissions](https://appwrite.io/docs/permissions) to allow different project users or team with access to execute the function using the client API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_function_response = appwriteserver.functions.create_new_function(
    function_id="<FUNCTION_ID>",
    name="<NAME>",
    runtime="node-14.5",
    execute=['["any"]'],
    events=["string_example"],
    schedule="string_example",
    timeout=1,
    enabled=False,
    logging=False,
    entrypoint="<ENTRYPOINT>",
    commands="<COMMANDS>",
    installation_id="<INSTALLATION_ID>",
    provider_repository_id="<PROVIDER_REPOSITORY_ID>",
    provider_branch="<PROVIDER_BRANCH>",
    provider_silent_mode=False,
    provider_root_directory="<PROVIDER_ROOT_DIRECTORY>",
    template_repository="<TEMPLATE_REPOSITORY>",
    template_owner="<TEMPLATE_OWNER>",
    template_root_directory="<TEMPLATE_ROOT_DIRECTORY>",
    template_branch="<TEMPLATE_BRANCH>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Function name. Max length: 128 chars.

##### runtime: `str`<a id="runtime-str"></a>

Execution runtime.

##### execute: [`FunctionsCreateNewFunctionRequestExecute`](./appwrite_server_python_sdk/type/functions_create_new_function_request_execute.py)<a id="execute-functionscreatenewfunctionrequestexecuteappwrite_server_python_sdktypefunctions_create_new_function_request_executepy"></a>

##### events: [`FunctionsCreateNewFunctionRequestEvents`](./appwrite_server_python_sdk/type/functions_create_new_function_request_events.py)<a id="events-functionscreatenewfunctionrequesteventsappwrite_server_python_sdktypefunctions_create_new_function_request_eventspy"></a>

##### schedule: `str`<a id="schedule-str"></a>

Schedule CRON syntax.

##### timeout: `int`<a id="timeout-int"></a>

Function maximum execution time in seconds.

##### enabled: `bool`<a id="enabled-bool"></a>

Is function enabled? When set to 'disabled', users cannot access the function but Server SDKs with and API key can still access the function. No data is lost when this is toggled.

##### logging: `bool`<a id="logging-bool"></a>

Whether executions will be logged. When set to false, executions will not be logged, but will reduce resource used by your Appwrite project.

##### entrypoint: `str`<a id="entrypoint-str"></a>

Entrypoint File. This path is relative to the \\\"providerRootDirectory\\\".

##### commands: `str`<a id="commands-str"></a>

Build Commands.

##### installation_id: `str`<a id="installation_id-str"></a>

Appwrite Installation ID for VCS (Version Control System) deployment.

##### provider_repository_id: `str`<a id="provider_repository_id-str"></a>

Repository ID of the repo linked to the function.

##### provider_branch: `str`<a id="provider_branch-str"></a>

Production branch for the repo linked to the function.

##### provider_silent_mode: `bool`<a id="provider_silent_mode-bool"></a>

Is the VCS (Version Control System) connection in silent mode for the repo linked to the function? In silent mode, comments will not be made on commits and pull requests.

##### provider_root_directory: `str`<a id="provider_root_directory-str"></a>

Path to function code in the linked repo.

##### template_repository: `str`<a id="template_repository-str"></a>

Repository name of the template.

##### template_owner: `str`<a id="template_owner-str"></a>

The name of the owner of the template.

##### template_root_directory: `str`<a id="template_root_directory-str"></a>

Path to function code in the template repo.

##### template_branch: `str`<a id="template_branch-str"></a>

Production branch for the repo linked to the function template.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FunctionsCreateNewFunctionRequest`](./appwrite_server_python_sdk/type/functions_create_new_function_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Function`](./appwrite_server_python_sdk/pydantic/function.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.create_variable`<a id="appwriteserverfunctionscreate_variable"></a>

Create a new function environment variable. These variables can be accessed in the function at runtime as environment variables.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_variable_response = appwriteserver.functions.create_variable(
    key="<KEY>",
    value="<VALUE>",
    function_id="functionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Variable key. Max length: 255 chars.

##### value: `str`<a id="value-str"></a>

Variable value. Max length: 8192 chars.

##### function_id: `str`<a id="function_id-str"></a>

Function unique ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FunctionsCreateVariableRequest`](./appwrite_server_python_sdk/type/functions_create_variable_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Variable`](./appwrite_server_python_sdk/pydantic/variable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/variables` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.delete_by_id`<a id="appwriteserverfunctionsdelete_by_id"></a>

Delete a function by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.functions.delete_by_id(
    function_id="functionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.delete_deployment`<a id="appwriteserverfunctionsdelete_deployment"></a>

Delete a code deployment by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.functions.delete_deployment(
    function_id="functionId_example",
    deployment_id="deploymentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### deployment_id: `str`<a id="deployment_id-str"></a>

Deployment ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/deployments/{deploymentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.delete_variable_by_id`<a id="appwriteserverfunctionsdelete_variable_by_id"></a>

Delete a variable by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.functions.delete_variable_by_id(
    function_id="functionId_example",
    variable_id="variableId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function unique ID.

##### variable_id: `str`<a id="variable_id-str"></a>

Variable unique ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/variables/{variableId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.get_by_id`<a id="appwriteserverfunctionsget_by_id"></a>

Get a function by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = appwriteserver.functions.get_by_id(
    function_id="functionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Function`](./appwrite_server_python_sdk/pydantic/function.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.get_deployment_by_id`<a id="appwriteserverfunctionsget_deployment_by_id"></a>

Get a code deployment by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_deployment_by_id_response = appwriteserver.functions.get_deployment_by_id(
    function_id="functionId_example",
    deployment_id="deploymentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### deployment_id: `str`<a id="deployment_id-str"></a>

Deployment ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Deployment`](./appwrite_server_python_sdk/pydantic/deployment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/deployments/{deploymentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.get_deployment_contents`<a id="appwriteserverfunctionsget_deployment_contents"></a>

Get a Deployment's contents by its unique ID. This endpoint supports range requests for partial or streaming file download.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.functions.get_deployment_contents(
    function_id="functionId_example",
    deployment_id="deploymentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### deployment_id: `str`<a id="deployment_id-str"></a>

Deployment ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/deployments/{deploymentId}/download` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.get_execution_log`<a id="appwriteserverfunctionsget_execution_log"></a>

Get a function execution log by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_execution_log_response = appwriteserver.functions.get_execution_log(
    function_id="functionId_example",
    execution_id="executionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### execution_id: `str`<a id="execution_id-str"></a>

Execution ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Execution`](./appwrite_server_python_sdk/pydantic/execution.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/executions/{executionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.get_variable_by_id`<a id="appwriteserverfunctionsget_variable_by_id"></a>

Get a variable by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_variable_by_id_response = appwriteserver.functions.get_variable_by_id(
    function_id="functionId_example",
    variable_id="variableId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function unique ID.

##### variable_id: `str`<a id="variable_id-str"></a>

Variable unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Variable`](./appwrite_server_python_sdk/pydantic/variable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/variables/{variableId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.list_all_functions`<a id="appwriteserverfunctionslist_all_functions"></a>

Get a list of all the project's functions. You can use the query params to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_functions_response = appwriteserver.functions.list_all_functions(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, enabled, runtime, deployment, schedule, scheduleNext, schedulePrevious, timeout, entrypoint, commands, installationId

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`FunctionList`](./appwrite_server_python_sdk/pydantic/function_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.list_deployments`<a id="appwriteserverfunctionslist_deployments"></a>

Get a list of all the project's code deployments. You can use the query params to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_deployments_response = appwriteserver.functions.list_deployments(
    function_id="functionId_example",
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: size, buildId, activate, entrypoint, commands

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`DeploymentList`](./appwrite_server_python_sdk/pydantic/deployment_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/deployments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.list_executions`<a id="appwriteserverfunctionslist_executions"></a>

Get a list of all the current user function execution logs. You can use the query params to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_executions_response = appwriteserver.functions.list_executions(
    function_id="functionId_example",
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: trigger, status, responseStatusCode, duration

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`ExecutionList`](./appwrite_server_python_sdk/pydantic/execution_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/executions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.list_runtimes`<a id="appwriteserverfunctionslist_runtimes"></a>

Get a list of all runtimes that are currently active on your instance.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_runtimes_response = appwriteserver.functions.list_runtimes()
```

#### 🔄 Return<a id="🔄-return"></a>

[`RuntimeList`](./appwrite_server_python_sdk/pydantic/runtime_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/runtimes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.list_variables`<a id="appwriteserverfunctionslist_variables"></a>

Get a list of all variables of a specific function.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_variables_response = appwriteserver.functions.list_variables(
    function_id="functionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`VariableList`](./appwrite_server_python_sdk/pydantic/variable_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/variables` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.trigger_execution`<a id="appwriteserverfunctionstrigger_execution"></a>

Trigger a function execution. The returned object will return you the current execution status. You can ping the `Get Execution` endpoint to get updates on the current execution status. Once this endpoint is called, your function execution process will start asynchronously.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trigger_execution_response = appwriteserver.functions.trigger_execution(
    function_id="functionId_example",
    body="<BODY>",
    _async=False,
    path="<PATH>",
    method="GET",
    headers={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### body: `str`<a id="body-str"></a>

HTTP body of execution. Default value is empty string.

##### _async: `bool`<a id="_async-bool"></a>

Execute code in the background. Default value is false.

##### path: `str`<a id="path-str"></a>

HTTP path of execution. Path can include query params. Default value is /

##### method: `str`<a id="method-str"></a>

HTTP method of execution. Default value is GET.

##### headers: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="headers-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

HTTP headers of execution. Defaults to empty.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FunctionsTriggerExecutionRequest`](./appwrite_server_python_sdk/type/functions_trigger_execution_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Execution`](./appwrite_server_python_sdk/pydantic/execution.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/executions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.update_by_id`<a id="appwriteserverfunctionsupdate_by_id"></a>

Update function by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = appwriteserver.functions.update_by_id(
    name="<NAME>",
    function_id="functionId_example",
    runtime="node-14.5",
    execute=['["any"]'],
    events=["string_example"],
    schedule="string_example",
    timeout=1,
    enabled=False,
    logging=False,
    entrypoint="<ENTRYPOINT>",
    commands="<COMMANDS>",
    installation_id="<INSTALLATION_ID>",
    provider_repository_id="<PROVIDER_REPOSITORY_ID>",
    provider_branch="<PROVIDER_BRANCH>",
    provider_silent_mode=False,
    provider_root_directory="<PROVIDER_ROOT_DIRECTORY>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Function name. Max length: 128 chars.

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### runtime: `str`<a id="runtime-str"></a>

Execution runtime.

##### execute: [`FunctionsUpdateByIdRequestExecute`](./appwrite_server_python_sdk/type/functions_update_by_id_request_execute.py)<a id="execute-functionsupdatebyidrequestexecuteappwrite_server_python_sdktypefunctions_update_by_id_request_executepy"></a>

##### events: [`FunctionsUpdateByIdRequestEvents`](./appwrite_server_python_sdk/type/functions_update_by_id_request_events.py)<a id="events-functionsupdatebyidrequesteventsappwrite_server_python_sdktypefunctions_update_by_id_request_eventspy"></a>

##### schedule: `str`<a id="schedule-str"></a>

Schedule CRON syntax.

##### timeout: `int`<a id="timeout-int"></a>

Maximum execution time in seconds.

##### enabled: `bool`<a id="enabled-bool"></a>

Is function enabled? When set to 'disabled', users cannot access the function but Server SDKs with and API key can still access the function. No data is lost when this is toggled.

##### logging: `bool`<a id="logging-bool"></a>

Whether executions will be logged. When set to false, executions will not be logged, but will reduce resource used by your Appwrite project.

##### entrypoint: `str`<a id="entrypoint-str"></a>

Entrypoint File. This path is relative to the \\\"providerRootDirectory\\\".

##### commands: `str`<a id="commands-str"></a>

Build Commands.

##### installation_id: `str`<a id="installation_id-str"></a>

Appwrite Installation ID for VCS (Version Controle System) deployment.

##### provider_repository_id: `str`<a id="provider_repository_id-str"></a>

Repository ID of the repo linked to the function

##### provider_branch: `str`<a id="provider_branch-str"></a>

Production branch for the repo linked to the function

##### provider_silent_mode: `bool`<a id="provider_silent_mode-bool"></a>

Is the VCS (Version Control System) connection in silent mode for the repo linked to the function? In silent mode, comments will not be made on commits and pull requests.

##### provider_root_directory: `str`<a id="provider_root_directory-str"></a>

Path to function code in the linked repo.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FunctionsUpdateByIdRequest`](./appwrite_server_python_sdk/type/functions_update_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Function`](./appwrite_server_python_sdk/pydantic/function.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.update_deployment_function_code`<a id="appwriteserverfunctionsupdate_deployment_function_code"></a>

Update the function code deployment ID using the unique function ID. Use this endpoint to switch the code deployment that should be executed by the execution endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_deployment_function_code_response = (
    appwriteserver.functions.update_deployment_function_code(
        function_id="functionId_example",
        deployment_id="deploymentId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### deployment_id: `str`<a id="deployment_id-str"></a>

Deployment ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Function`](./appwrite_server_python_sdk/pydantic/function.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/deployments/{deploymentId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.functions.update_variable_by_id`<a id="appwriteserverfunctionsupdate_variable_by_id"></a>

Update variable by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_variable_by_id_response = appwriteserver.functions.update_variable_by_id(
    key="<KEY>",
    function_id="functionId_example",
    variable_id="variableId_example",
    value="<VALUE>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Variable key. Max length: 255 chars.

##### function_id: `str`<a id="function_id-str"></a>

Function unique ID.

##### variable_id: `str`<a id="variable_id-str"></a>

Variable unique ID.

##### value: `str`<a id="value-str"></a>

Variable value. Max length: 8192 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FunctionsUpdateVariableByIdRequest`](./appwrite_server_python_sdk/type/functions_update_variable_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Variable`](./appwrite_server_python_sdk/pydantic/variable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/variables/{variableId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.graphql.execute_mutation`<a id="appwriteservergraphqlexecute_mutation"></a>

Execute a GraphQL mutation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
execute_mutation_response = appwriteserver.graphql.execute_mutation()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Any`](./appwrite_server_python_sdk/pydantic/any.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/graphql` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.graphql.execute_mutation_0`<a id="appwriteservergraphqlexecute_mutation_0"></a>

Execute a GraphQL mutation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
execute_mutation_0_response = appwriteserver.graphql.execute_mutation_0()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Any`](./appwrite_server_python_sdk/pydantic/any.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/graphql/mutation` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.check_antivirus_status`<a id="appwriteserverhealthcheck_antivirus_status"></a>

Check the Appwrite Antivirus server is up and connection is successful.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_antivirus_status_response = appwriteserver.health.check_antivirus_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthAntivirus`](./appwrite_server_python_sdk/pydantic/health_antivirus.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/anti-virus` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.check_cache_status`<a id="appwriteserverhealthcheck_cache_status"></a>

Check the Appwrite in-memory cache servers are up and connection is successful.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_cache_status_response = appwriteserver.health.check_cache_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthStatus`](./appwrite_server_python_sdk/pydantic/health_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/cache` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.check_db_status`<a id="appwriteserverhealthcheck_db_status"></a>

Check the Appwrite database servers are up and connection is successful.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_db_status_response = appwriteserver.health.check_db_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthStatus`](./appwrite_server_python_sdk/pydantic/health_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/db` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.check_local_storage_status`<a id="appwriteserverhealthcheck_local_storage_status"></a>

Check the Appwrite local storage device is up and connection is successful.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_local_storage_status_response = appwriteserver.health.check_local_storage_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthStatus`](./appwrite_server_python_sdk/pydantic/health_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/storage/local` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.check_pubsub_server_status`<a id="appwriteserverhealthcheck_pubsub_server_status"></a>

Check the Appwrite pub-sub servers are up and connection is successful.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_pubsub_server_status_response = appwriteserver.health.check_pubsub_server_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthStatus`](./appwrite_server_python_sdk/pydantic/health_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/pubsub` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.check_server_status`<a id="appwriteserverhealthcheck_server_status"></a>

Check the Appwrite HTTP server is up and responsive.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_server_status_response = appwriteserver.health.check_server_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthStatus`](./appwrite_server_python_sdk/pydantic/health_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.check_storage_status`<a id="appwriteserverhealthcheck_storage_status"></a>

Check the Appwrite storage device is up and connection is successful.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_storage_status_response = appwriteserver.health.check_storage_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthStatus`](./appwrite_server_python_sdk/pydantic/health_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/storage` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.functions_queue_count`<a id="appwriteserverhealthfunctions_queue_count"></a>

Get the number of function executions that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
functions_queue_count_response = appwriteserver.health.functions_queue_count(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_server_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/functions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.get_builds_queue`<a id="appwriteserverhealthget_builds_queue"></a>

Get the number of builds that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_builds_queue_response = appwriteserver.health.get_builds_queue(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_server_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/builds` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.get_databases_queue`<a id="appwriteserverhealthget_databases_queue"></a>

Get the number of database changes that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_databases_queue_response = appwriteserver.health.get_databases_queue(
    name="database_db_main",
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Queue name for which to check the queue size

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_server_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/databases` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.get_deletes_queue`<a id="appwriteserverhealthget_deletes_queue"></a>

Get the number of background destructive changes that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_deletes_queue_response = appwriteserver.health.get_deletes_queue(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_server_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/deletes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.get_failed_jobs`<a id="appwriteserverhealthget_failed_jobs"></a>

Returns the amount of failed jobs in a given queue.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_failed_jobs_response = appwriteserver.health.get_failed_jobs(
    name="v1-database",
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the queue

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_server_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/failed/{name}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.get_mail_queue_size`<a id="appwriteserverhealthget_mail_queue_size"></a>

Get the number of mails that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_mail_queue_size_response = appwriteserver.health.get_mail_queue_size(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_server_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/mails` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.get_migrations_queue`<a id="appwriteserverhealthget_migrations_queue"></a>

Get the number of migrations that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_migrations_queue_response = appwriteserver.health.get_migrations_queue(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_server_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/migrations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.get_queue_logs`<a id="appwriteserverhealthget_queue_logs"></a>

Get the number of logs that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_queue_logs_response = appwriteserver.health.get_queue_logs(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_server_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.get_queue_messaging`<a id="appwriteserverhealthget_queue_messaging"></a>

Get the number of messages that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_queue_messaging_response = appwriteserver.health.get_queue_messaging(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_server_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/messaging` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.get_queue_status`<a id="appwriteserverhealthget_queue_status"></a>

Check the Appwrite queue messaging servers are up and connection is successful.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_queue_status_response = appwriteserver.health.get_queue_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthStatus`](./appwrite_server_python_sdk/pydantic/health_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.get_queue_usage`<a id="appwriteserverhealthget_queue_usage"></a>

Get the number of metrics that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_queue_usage_response = appwriteserver.health.get_queue_usage(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_server_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/usage` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.get_queue_usage_dump`<a id="appwriteserverhealthget_queue_usage_dump"></a>

Get the number of projects containing metrics that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_queue_usage_dump_response = appwriteserver.health.get_queue_usage_dump(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_server_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/usage-dump` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.get_ssl_cert`<a id="appwriteserverhealthget_ssl_cert"></a>

Get the SSL certificate for a domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_ssl_cert_response = appwriteserver.health.get_ssl_cert(
    domain="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

string

#### 🔄 Return<a id="🔄-return"></a>

[`HealthCertificate`](./appwrite_server_python_sdk/pydantic/health_certificate.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/certificate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.get_time_information`<a id="appwriteserverhealthget_time_information"></a>

Check the Appwrite server time is synced with Google remote NTP server. We use this technology to smoothly handle leap seconds with no disruptive events. The [Network Time Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol) (NTP) is used by hundreds of millions of computers and devices to synchronize their clocks over the Internet. If your computer sets its own clock, it likely uses NTP.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_time_information_response = appwriteserver.health.get_time_information()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthTime`](./appwrite_server_python_sdk/pydantic/health_time.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/time` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.get_webhooks_queue`<a id="appwriteserverhealthget_webhooks_queue"></a>

Get the number of webhooks that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_webhooks_queue_response = appwriteserver.health.get_webhooks_queue(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_server_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.health.queue_certificates_get`<a id="appwriteserverhealthqueue_certificates_get"></a>

Get the number of certificates that are waiting to be issued against [Letsencrypt](https://letsencrypt.org/) in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
queue_certificates_get_response = appwriteserver.health.queue_certificates_get(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_server_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/certificates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.locale.get_language_list`<a id="appwriteserverlocaleget_language_list"></a>

List of all languages classified by ISO 639-1 including 2-letter code, name in English, and name in the respective language.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_language_list_response = appwriteserver.locale.get_language_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`LanguageList`](./appwrite_server_python_sdk/pydantic/language_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locale/languages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.locale.get_user_locale_data`<a id="appwriteserverlocaleget_user_locale_data"></a>

Get the current user location based on IP. Returns an object with user country code, country name, continent name, continent code, ip address and suggested currency. You can use the locale header to get the data in a supported language.

([IP Geolocation by DB-IP](https://db-ip.com))

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_locale_data_response = appwriteserver.locale.get_user_locale_data()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Locale`](./appwrite_server_python_sdk/pydantic/locale.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locale` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.locale.list_codes`<a id="appwriteserverlocalelist_codes"></a>

List of all locale codes in [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_codes_response = appwriteserver.locale.list_codes()
```

#### 🔄 Return<a id="🔄-return"></a>

[`LocaleCodeList`](./appwrite_server_python_sdk/pydantic/locale_code_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locale/codes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.locale.list_continents`<a id="appwriteserverlocalelist_continents"></a>

List of all continents. You can use the locale header to get the data in a supported language.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_continents_response = appwriteserver.locale.list_continents()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ContinentList`](./appwrite_server_python_sdk/pydantic/continent_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locale/continents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.locale.list_countries`<a id="appwriteserverlocalelist_countries"></a>

List of all countries. You can use the locale header to get the data in a supported language.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_countries_response = appwriteserver.locale.list_countries()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CountryList`](./appwrite_server_python_sdk/pydantic/country_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locale/countries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.locale.list_currencies_data`<a id="appwriteserverlocalelist_currencies_data"></a>

List of all currencies, including currency symbol, name, plural, and decimal digits for all major and minor currencies. You can use the locale header to get the data in a supported language.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_currencies_data_response = appwriteserver.locale.list_currencies_data()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CurrencyList`](./appwrite_server_python_sdk/pydantic/currency_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locale/currencies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.locale.list_eu_countries`<a id="appwriteserverlocalelist_eu_countries"></a>

List of all countries that are currently members of the EU. You can use the locale header to get the data in a supported language.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_eu_countries_response = appwriteserver.locale.list_eu_countries()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CountryList`](./appwrite_server_python_sdk/pydantic/country_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locale/countries/eu` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.locale.list_phone_codes`<a id="appwriteserverlocalelist_phone_codes"></a>

List of all countries phone codes. You can use the locale header to get the data in a supported language.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_phone_codes_response = appwriteserver.locale.list_phone_codes()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PhoneList`](./appwrite_server_python_sdk/pydantic/phone_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locale/countries/phones` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.create_apns_provider`<a id="appwriteservermessagingcreate_apns_provider"></a>

Create a new Apple Push Notification service provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_apns_provider_response = appwriteserver.messaging.create_apns_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    auth_key="<AUTH_KEY>",
    auth_key_id="<AUTH_KEY_ID>",
    team_id="<TEAM_ID>",
    bundle_id="<BUNDLE_ID>",
    sandbox=False,
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### auth_key: `str`<a id="auth_key-str"></a>

APNS authentication key.

##### auth_key_id: `str`<a id="auth_key_id-str"></a>

APNS authentication key ID.

##### team_id: `str`<a id="team_id-str"></a>

APNS team ID.

##### bundle_id: `str`<a id="bundle_id-str"></a>

APNS bundle ID.

##### sandbox: `bool`<a id="sandbox-bool"></a>

Use APNS sandbox environment.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateApnsProviderRequest`](./appwrite_server_python_sdk/type/messaging_create_apns_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/apns` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.create_email_message`<a id="appwriteservermessagingcreate_email_message"></a>

Create a new email message.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_email_message_response = appwriteserver.messaging.create_email_message(
    message_id="<MESSAGE_ID>",
    subject="<SUBJECT>",
    content="<CONTENT>",
    topics=["string_example"],
    users=["string_example"],
    targets=["string_example"],
    cc=["string_example"],
    bcc=["string_example"],
    attachments=["string_example"],
    draft=False,
    html=False,
    scheduled_at="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### subject: `str`<a id="subject-str"></a>

Email Subject.

##### content: `str`<a id="content-str"></a>

Email Content.

##### topics: [`MessagingCreateEmailMessageRequestTopics`](./appwrite_server_python_sdk/type/messaging_create_email_message_request_topics.py)<a id="topics-messagingcreateemailmessagerequesttopicsappwrite_server_python_sdktypemessaging_create_email_message_request_topicspy"></a>

##### users: [`MessagingCreateEmailMessageRequestUsers`](./appwrite_server_python_sdk/type/messaging_create_email_message_request_users.py)<a id="users-messagingcreateemailmessagerequestusersappwrite_server_python_sdktypemessaging_create_email_message_request_userspy"></a>

##### targets: [`MessagingCreateEmailMessageRequestTargets`](./appwrite_server_python_sdk/type/messaging_create_email_message_request_targets.py)<a id="targets-messagingcreateemailmessagerequesttargetsappwrite_server_python_sdktypemessaging_create_email_message_request_targetspy"></a>

##### cc: [`MessagingCreateEmailMessageRequestCc`](./appwrite_server_python_sdk/type/messaging_create_email_message_request_cc.py)<a id="cc-messagingcreateemailmessagerequestccappwrite_server_python_sdktypemessaging_create_email_message_request_ccpy"></a>

##### bcc: [`MessagingCreateEmailMessageRequestBcc`](./appwrite_server_python_sdk/type/messaging_create_email_message_request_bcc.py)<a id="bcc-messagingcreateemailmessagerequestbccappwrite_server_python_sdktypemessaging_create_email_message_request_bccpy"></a>

##### attachments: [`MessagingCreateEmailMessageRequestAttachments`](./appwrite_server_python_sdk/type/messaging_create_email_message_request_attachments.py)<a id="attachments-messagingcreateemailmessagerequestattachmentsappwrite_server_python_sdktypemessaging_create_email_message_request_attachmentspy"></a>

##### draft: `bool`<a id="draft-bool"></a>

Is message a draft

##### html: `bool`<a id="html-bool"></a>

Is content of type HTML

##### scheduled_at: `str`<a id="scheduled_at-str"></a>

Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateEmailMessageRequest`](./appwrite_server_python_sdk/type/messaging_create_email_message_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./appwrite_server_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/email` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.create_fcm_provider`<a id="appwriteservermessagingcreate_fcm_provider"></a>

Create a new Firebase Cloud Messaging provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_fcm_provider_response = appwriteserver.messaging.create_fcm_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    service_account_json={},
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### service_account_json: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="service_account_json-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

FCM service account JSON.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateFcmProviderRequest`](./appwrite_server_python_sdk/type/messaging_create_fcm_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/fcm` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.create_msg91_provider`<a id="appwriteservermessagingcreate_msg91_provider"></a>

Create a new MSG91 provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_msg91_provider_response = appwriteserver.messaging.create_msg91_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    _from="+12065550100",
    sender_id="<SENDER_ID>",
    auth_key="<AUTH_KEY>",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### _from: `str`<a id="_from-str"></a>

Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

##### sender_id: `str`<a id="sender_id-str"></a>

Msg91 Sender ID.

##### auth_key: `str`<a id="auth_key-str"></a>

Msg91 Auth Key.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateMsg91ProviderRequest`](./appwrite_server_python_sdk/type/messaging_create_msg91_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/msg91` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.create_provider`<a id="appwriteservermessagingcreate_provider"></a>

Create a new Mailgun provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_provider_response = appwriteserver.messaging.create_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    api_key="<API_KEY>",
    domain="<DOMAIN>",
    is_eu_region=False,
    from_name="<FROM_NAME>",
    from_email="email@example.com",
    reply_to_name="<REPLY_TO_NAME>",
    reply_to_email="email@example.com",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### api_key: `str`<a id="api_key-str"></a>

Mailgun API Key.

##### domain: `str`<a id="domain-str"></a>

Mailgun Domain.

##### is_eu_region: `bool`<a id="is_eu_region-bool"></a>

Set as EU region.

##### from_name: `str`<a id="from_name-str"></a>

Sender Name.

##### from_email: `str`<a id="from_email-str"></a>

Sender email address.

##### reply_to_name: `str`<a id="reply_to_name-str"></a>

Name set in the reply to field for the mail. Default value is sender name. Reply to name must have reply to email as well.

##### reply_to_email: `str`<a id="reply_to_email-str"></a>

Email set in the reply to field for the mail. Default value is sender email. Reply to email must have reply to name as well.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateProviderRequest`](./appwrite_server_python_sdk/type/messaging_create_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/mailgun` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.create_push_notification`<a id="appwriteservermessagingcreate_push_notification"></a>

Create a new push notification.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_push_notification_response = appwriteserver.messaging.create_push_notification(
    title="<TITLE>",
    message_id="<MESSAGE_ID>",
    body="<BODY>",
    topics=["string_example"],
    users=["string_example"],
    targets=["string_example"],
    data={},
    action="<ACTION>",
    image="[ID1:ID2]",
    icon="<ICON>",
    sound="<SOUND>",
    color="<COLOR>",
    tag="<TAG>",
    badge="<BADGE>",
    draft=False,
    scheduled_at="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

Title for push notification.

##### message_id: `str`<a id="message_id-str"></a>

Message ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### body: `str`<a id="body-str"></a>

Body for push notification.

##### topics: [`MessagingCreatePushNotificationRequestTopics`](./appwrite_server_python_sdk/type/messaging_create_push_notification_request_topics.py)<a id="topics-messagingcreatepushnotificationrequesttopicsappwrite_server_python_sdktypemessaging_create_push_notification_request_topicspy"></a>

##### users: [`MessagingCreatePushNotificationRequestUsers`](./appwrite_server_python_sdk/type/messaging_create_push_notification_request_users.py)<a id="users-messagingcreatepushnotificationrequestusersappwrite_server_python_sdktypemessaging_create_push_notification_request_userspy"></a>

##### targets: [`MessagingCreatePushNotificationRequestTargets`](./appwrite_server_python_sdk/type/messaging_create_push_notification_request_targets.py)<a id="targets-messagingcreatepushnotificationrequesttargetsappwrite_server_python_sdktypemessaging_create_push_notification_request_targetspy"></a>

##### data: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="data-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Additional Data for push notification.

##### action: `str`<a id="action-str"></a>

Action for push notification.

##### image: `str`<a id="image-str"></a>

Image for push notification. Must be a compound bucket ID to file ID of a jpeg, png, or bmp image in Appwrite Storage.

##### icon: `str`<a id="icon-str"></a>

Icon for push notification. Available only for Android and Web Platform.

##### sound: `str`<a id="sound-str"></a>

Sound for push notification. Available only for Android and IOS Platform.

##### color: `str`<a id="color-str"></a>

Color for push notification. Available only for Android Platform.

##### tag: `str`<a id="tag-str"></a>

Tag for push notification. Available only for Android Platform.

##### badge: `str`<a id="badge-str"></a>

Badge for push notification. Available only for IOS Platform.

##### draft: `bool`<a id="draft-bool"></a>

Is message a draft

##### scheduled_at: `str`<a id="scheduled_at-str"></a>

Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreatePushNotificationRequest`](./appwrite_server_python_sdk/type/messaging_create_push_notification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./appwrite_server_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/push` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.create_sendgrid_provider`<a id="appwriteservermessagingcreate_sendgrid_provider"></a>

Create a new Sendgrid provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_sendgrid_provider_response = appwriteserver.messaging.create_sendgrid_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    api_key="<API_KEY>",
    from_name="<FROM_NAME>",
    from_email="email@example.com",
    reply_to_name="<REPLY_TO_NAME>",
    reply_to_email="email@example.com",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### api_key: `str`<a id="api_key-str"></a>

Sendgrid API key.

##### from_name: `str`<a id="from_name-str"></a>

Sender Name.

##### from_email: `str`<a id="from_email-str"></a>

Sender email address.

##### reply_to_name: `str`<a id="reply_to_name-str"></a>

Name set in the reply to field for the mail. Default value is sender name.

##### reply_to_email: `str`<a id="reply_to_email-str"></a>

Email set in the reply to field for the mail. Default value is sender email.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateSendgridProviderRequest`](./appwrite_server_python_sdk/type/messaging_create_sendgrid_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/sendgrid` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.create_sms_message`<a id="appwriteservermessagingcreate_sms_message"></a>

Create a new SMS message.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_sms_message_response = appwriteserver.messaging.create_sms_message(
    message_id="<MESSAGE_ID>",
    content="<CONTENT>",
    topics=["string_example"],
    users=["string_example"],
    targets=["string_example"],
    draft=False,
    scheduled_at="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### content: `str`<a id="content-str"></a>

SMS Content.

##### topics: [`MessagingCreateSmsMessageRequestTopics`](./appwrite_server_python_sdk/type/messaging_create_sms_message_request_topics.py)<a id="topics-messagingcreatesmsmessagerequesttopicsappwrite_server_python_sdktypemessaging_create_sms_message_request_topicspy"></a>

##### users: [`MessagingCreateSmsMessageRequestUsers`](./appwrite_server_python_sdk/type/messaging_create_sms_message_request_users.py)<a id="users-messagingcreatesmsmessagerequestusersappwrite_server_python_sdktypemessaging_create_sms_message_request_userspy"></a>

##### targets: [`MessagingCreateSmsMessageRequestTargets`](./appwrite_server_python_sdk/type/messaging_create_sms_message_request_targets.py)<a id="targets-messagingcreatesmsmessagerequesttargetsappwrite_server_python_sdktypemessaging_create_sms_message_request_targetspy"></a>

##### draft: `bool`<a id="draft-bool"></a>

Is message a draft

##### scheduled_at: `str`<a id="scheduled_at-str"></a>

Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateSmsMessageRequest`](./appwrite_server_python_sdk/type/messaging_create_sms_message_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./appwrite_server_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/sms` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.create_smtp_provider`<a id="appwriteservermessagingcreate_smtp_provider"></a>

Create a new SMTP provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_smtp_provider_response = appwriteserver.messaging.create_smtp_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    host="<HOST>",
    port=1,
    username="<USERNAME>",
    password="<PASSWORD>",
    encryption="none",
    auto_tls=False,
    mailer="<MAILER>",
    from_name="<FROM_NAME>",
    from_email="email@example.com",
    reply_to_name="<REPLY_TO_NAME>",
    reply_to_email="email@example.com",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### host: `str`<a id="host-str"></a>

SMTP hosts. Either a single hostname or multiple semicolon-delimited hostnames. You can also specify a different port for each host such as `smtp1.example.com:25;smtp2.example.com`. You can also specify encryption type, for example: `tls://smtp1.example.com:587;ssl://smtp2.example.com:465\\\"`. Hosts will be tried in order.

##### port: `int`<a id="port-int"></a>

The default SMTP server port.

##### username: `str`<a id="username-str"></a>

Authentication username.

##### password: `str`<a id="password-str"></a>

Authentication password.

##### encryption: `str`<a id="encryption-str"></a>

Encryption type. Can be omitted, 'ssl', or 'tls'

##### auto_tls: `bool`<a id="auto_tls-bool"></a>

Enable SMTP AutoTLS feature.

##### mailer: `str`<a id="mailer-str"></a>

The value to use for the X-Mailer header.

##### from_name: `str`<a id="from_name-str"></a>

Sender Name.

##### from_email: `str`<a id="from_email-str"></a>

Sender email address.

##### reply_to_name: `str`<a id="reply_to_name-str"></a>

Name set in the reply to field for the mail. Default value is sender name.

##### reply_to_email: `str`<a id="reply_to_email-str"></a>

Email set in the reply to field for the mail. Default value is sender email.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateSmtpProviderRequest`](./appwrite_server_python_sdk/type/messaging_create_smtp_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/smtp` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.create_subscriber`<a id="appwriteservermessagingcreate_subscriber"></a>

Create a new subscriber.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_subscriber_response = appwriteserver.messaging.create_subscriber(
    subscriber_id="<SUBSCRIBER_ID>",
    target_id="<TARGET_ID>",
    topic_id="topicId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscriber_id: `str`<a id="subscriber_id-str"></a>

Subscriber ID. Choose a custom Subscriber ID or a new Subscriber ID.

##### target_id: `str`<a id="target_id-str"></a>

Target ID. The target ID to link to the specified Topic ID.

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID. The topic ID to subscribe to.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateSubscriberRequest`](./appwrite_server_python_sdk/type/messaging_create_subscriber_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Subscriber`](./appwrite_server_python_sdk/pydantic/subscriber.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics/{topicId}/subscribers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.create_telesign_provider`<a id="appwriteservermessagingcreate_telesign_provider"></a>

Create a new Telesign provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_telesign_provider_response = appwriteserver.messaging.create_telesign_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    _from="+12065550100",
    customer_id="<CUSTOMER_ID>",
    api_key="<API_KEY>",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### _from: `str`<a id="_from-str"></a>

Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

##### customer_id: `str`<a id="customer_id-str"></a>

Telesign customer ID.

##### api_key: `str`<a id="api_key-str"></a>

Telesign API key.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateTelesignProviderRequest`](./appwrite_server_python_sdk/type/messaging_create_telesign_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/telesign` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.create_textmagic_provider`<a id="appwriteservermessagingcreate_textmagic_provider"></a>

Create a new Textmagic provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_textmagic_provider_response = appwriteserver.messaging.create_textmagic_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    _from="+12065550100",
    username="<USERNAME>",
    api_key="<API_KEY>",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### _from: `str`<a id="_from-str"></a>

Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

##### username: `str`<a id="username-str"></a>

Textmagic username.

##### api_key: `str`<a id="api_key-str"></a>

Textmagic apiKey.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateTextmagicProviderRequest`](./appwrite_server_python_sdk/type/messaging_create_textmagic_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/textmagic` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.create_topic`<a id="appwriteservermessagingcreate_topic"></a>

Create a new topic.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_topic_response = appwriteserver.messaging.create_topic(
    topic_id="<TOPIC_ID>",
    name="<NAME>",
    subscribe=['["any"]'],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID. Choose a custom Topic ID or a new Topic ID.

##### name: `str`<a id="name-str"></a>

Topic Name.

##### subscribe: [`MessagingCreateTopicRequestSubscribe`](./appwrite_server_python_sdk/type/messaging_create_topic_request_subscribe.py)<a id="subscribe-messagingcreatetopicrequestsubscribeappwrite_server_python_sdktypemessaging_create_topic_request_subscribepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateTopicRequest`](./appwrite_server_python_sdk/type/messaging_create_topic_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Topic`](./appwrite_server_python_sdk/pydantic/topic.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.create_twilio_provider`<a id="appwriteservermessagingcreate_twilio_provider"></a>

Create a new Twilio provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_twilio_provider_response = appwriteserver.messaging.create_twilio_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    _from="+12065550100",
    account_sid="<ACCOUNT_SID>",
    auth_token="<AUTH_TOKEN>",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### _from: `str`<a id="_from-str"></a>

Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

##### account_sid: `str`<a id="account_sid-str"></a>

Twilio account secret ID.

##### auth_token: `str`<a id="auth_token-str"></a>

Twilio authentication token.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateTwilioProviderRequest`](./appwrite_server_python_sdk/type/messaging_create_twilio_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/twilio` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.create_vonage_provider`<a id="appwriteservermessagingcreate_vonage_provider"></a>

Create a new Vonage provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_vonage_provider_response = appwriteserver.messaging.create_vonage_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    _from="+12065550100",
    api_key="<API_KEY>",
    api_secret="<API_SECRET>",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### _from: `str`<a id="_from-str"></a>

Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

##### api_key: `str`<a id="api_key-str"></a>

Vonage API key.

##### api_secret: `str`<a id="api_secret-str"></a>

Vonage API secret.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateVonageProviderRequest`](./appwrite_server_python_sdk/type/messaging_create_vonage_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/vonage` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.delete_message_by_id`<a id="appwriteservermessagingdelete_message_by_id"></a>

Delete a message. If the message is not a draft or scheduled, but has been sent, this will not recall the message.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.messaging.delete_message_by_id(
    message_id="messageId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/{messageId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.delete_provider_by_id`<a id="appwriteservermessagingdelete_provider_by_id"></a>

Delete a provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.messaging.delete_provider_by_id(
    provider_id="providerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/{providerId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.delete_subscriber_by_id`<a id="appwriteservermessagingdelete_subscriber_by_id"></a>

Delete a subscriber by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.messaging.delete_subscriber_by_id(
    topic_id="topicId_example",
    subscriber_id="subscriberId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID. The topic ID subscribed to.

##### subscriber_id: `str`<a id="subscriber_id-str"></a>

Subscriber ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics/{topicId}/subscribers/{subscriberId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.delete_topic_by_id`<a id="appwriteservermessagingdelete_topic_by_id"></a>

Delete a topic by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.messaging.delete_topic_by_id(
    topic_id="topicId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics/{topicId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.get_message_by_id`<a id="appwriteservermessagingget_message_by_id"></a>

Get a message by its unique ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_message_by_id_response = appwriteserver.messaging.get_message_by_id(
    message_id="messageId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./appwrite_server_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/{messageId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.get_message_logs`<a id="appwriteservermessagingget_message_logs"></a>

Get the message activity logs listed by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_message_logs_response = appwriteserver.messaging.get_message_logs(
    message_id="messageId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset

#### 🔄 Return<a id="🔄-return"></a>

[`LogList`](./appwrite_server_python_sdk/pydantic/log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/{messageId}/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.get_provider_by_id`<a id="appwriteservermessagingget_provider_by_id"></a>

Get a provider by its unique ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_provider_by_id_response = appwriteserver.messaging.get_provider_by_id(
    provider_id="providerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/{providerId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.get_subscriber_by_id`<a id="appwriteservermessagingget_subscriber_by_id"></a>

Get a subscriber by its unique ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_subscriber_by_id_response = appwriteserver.messaging.get_subscriber_by_id(
    topic_id="topicId_example",
    subscriber_id="subscriberId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID. The topic ID subscribed to.

##### subscriber_id: `str`<a id="subscriber_id-str"></a>

Subscriber ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Subscriber`](./appwrite_server_python_sdk/pydantic/subscriber.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics/{topicId}/subscribers/{subscriberId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.get_topic_by_id`<a id="appwriteservermessagingget_topic_by_id"></a>

Get a topic by its unique ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_topic_by_id_response = appwriteserver.messaging.get_topic_by_id(
    topic_id="topicId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Topic`](./appwrite_server_python_sdk/pydantic/topic.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics/{topicId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.list_message_targets`<a id="appwriteservermessaginglist_message_targets"></a>

Get a list of the targets associated with a message.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_message_targets_response = appwriteserver.messaging.list_message_targets(
    message_id="messageId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, providerId, identifier, providerType

#### 🔄 Return<a id="🔄-return"></a>

[`TargetList`](./appwrite_server_python_sdk/pydantic/target_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/{messageId}/targets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.list_messages`<a id="appwriteservermessaginglist_messages"></a>

Get a list of all messages from the current Appwrite project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_messages_response = appwriteserver.messaging.list_messages(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: scheduledAt, deliveredAt, deliveredTotal, status, description, providerType

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`MessageList`](./appwrite_server_python_sdk/pydantic/message_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.list_provider_logs`<a id="appwriteservermessaginglist_provider_logs"></a>

Get the provider activity logs listed by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_provider_logs_response = appwriteserver.messaging.list_provider_logs(
    provider_id="providerId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset

#### 🔄 Return<a id="🔄-return"></a>

[`LogList`](./appwrite_server_python_sdk/pydantic/log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/{providerId}/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.list_providers`<a id="appwriteservermessaginglist_providers"></a>

Get a list of all providers from the current Appwrite project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_providers_response = appwriteserver.messaging.list_providers(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, provider, type, enabled

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`ProviderList`](./appwrite_server_python_sdk/pydantic/provider_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.list_subscriber_logs`<a id="appwriteservermessaginglist_subscriber_logs"></a>

Get the subscriber activity logs listed by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_subscriber_logs_response = appwriteserver.messaging.list_subscriber_logs(
    subscriber_id="subscriberId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscriber_id: `str`<a id="subscriber_id-str"></a>

Subscriber ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset

#### 🔄 Return<a id="🔄-return"></a>

[`LogList`](./appwrite_server_python_sdk/pydantic/log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/subscribers/{subscriberId}/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.list_subscribers`<a id="appwriteservermessaginglist_subscribers"></a>

Get a list of all subscribers from the current Appwrite project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_subscribers_response = appwriteserver.messaging.list_subscribers(
    topic_id="topicId_example",
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID. The topic ID subscribed to.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, provider, type, enabled

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`SubscriberList`](./appwrite_server_python_sdk/pydantic/subscriber_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics/{topicId}/subscribers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.list_topic_logs`<a id="appwriteservermessaginglist_topic_logs"></a>

Get the topic activity logs listed by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_topic_logs_response = appwriteserver.messaging.list_topic_logs(
    topic_id="topicId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset

#### 🔄 Return<a id="🔄-return"></a>

[`LogList`](./appwrite_server_python_sdk/pydantic/log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics/{topicId}/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.list_topics`<a id="appwriteservermessaginglist_topics"></a>

Get a list of all topics from the current Appwrite project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_topics_response = appwriteserver.messaging.list_topics(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, description, emailTotal, smsTotal, pushTotal

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`TopicList`](./appwrite_server_python_sdk/pydantic/topic_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.update_apns_provider`<a id="appwriteservermessagingupdate_apns_provider"></a>

Update a Apple Push Notification service provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_apns_provider_response = appwriteserver.messaging.update_apns_provider(
    provider_id="providerId_example",
    name="<NAME>",
    enabled=False,
    auth_key="<AUTH_KEY>",
    auth_key_id="<AUTH_KEY_ID>",
    team_id="<TEAM_ID>",
    bundle_id="<BUNDLE_ID>",
    sandbox=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### auth_key: `str`<a id="auth_key-str"></a>

APNS authentication key.

##### auth_key_id: `str`<a id="auth_key_id-str"></a>

APNS authentication key ID.

##### team_id: `str`<a id="team_id-str"></a>

APNS team ID.

##### bundle_id: `str`<a id="bundle_id-str"></a>

APNS bundle ID.

##### sandbox: `bool`<a id="sandbox-bool"></a>

Use APNS sandbox environment.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateApnsProviderRequest`](./appwrite_server_python_sdk/type/messaging_update_apns_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/apns/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.update_email_by_id`<a id="appwriteservermessagingupdate_email_by_id"></a>

Update an email message by its unique ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_email_by_id_response = appwriteserver.messaging.update_email_by_id(
    message_id="messageId_example",
    topics=["string_example"],
    users=["string_example"],
    targets=["string_example"],
    subject="<SUBJECT>",
    content="<CONTENT>",
    draft=False,
    html=False,
    cc=["string_example"],
    bcc=["string_example"],
    scheduled_at="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID.

##### topics: [`MessagingUpdateEmailByIdRequestTopics`](./appwrite_server_python_sdk/type/messaging_update_email_by_id_request_topics.py)<a id="topics-messagingupdateemailbyidrequesttopicsappwrite_server_python_sdktypemessaging_update_email_by_id_request_topicspy"></a>

##### users: [`MessagingUpdateEmailByIdRequestUsers`](./appwrite_server_python_sdk/type/messaging_update_email_by_id_request_users.py)<a id="users-messagingupdateemailbyidrequestusersappwrite_server_python_sdktypemessaging_update_email_by_id_request_userspy"></a>

##### targets: [`MessagingUpdateEmailByIdRequestTargets`](./appwrite_server_python_sdk/type/messaging_update_email_by_id_request_targets.py)<a id="targets-messagingupdateemailbyidrequesttargetsappwrite_server_python_sdktypemessaging_update_email_by_id_request_targetspy"></a>

##### subject: `str`<a id="subject-str"></a>

Email Subject.

##### content: `str`<a id="content-str"></a>

Email Content.

##### draft: `bool`<a id="draft-bool"></a>

Is message a draft

##### html: `bool`<a id="html-bool"></a>

Is content of type HTML

##### cc: [`MessagingUpdateEmailByIdRequestCc`](./appwrite_server_python_sdk/type/messaging_update_email_by_id_request_cc.py)<a id="cc-messagingupdateemailbyidrequestccappwrite_server_python_sdktypemessaging_update_email_by_id_request_ccpy"></a>

##### bcc: [`MessagingUpdateEmailByIdRequestBcc`](./appwrite_server_python_sdk/type/messaging_update_email_by_id_request_bcc.py)<a id="bcc-messagingupdateemailbyidrequestbccappwrite_server_python_sdktypemessaging_update_email_by_id_request_bccpy"></a>

##### scheduled_at: `str`<a id="scheduled_at-str"></a>

Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateEmailByIdRequest`](./appwrite_server_python_sdk/type/messaging_update_email_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./appwrite_server_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/email/{messageId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.update_fcm_provider_by_id`<a id="appwriteservermessagingupdate_fcm_provider_by_id"></a>

Update a Firebase Cloud Messaging provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_fcm_provider_by_id_response = appwriteserver.messaging.update_fcm_provider_by_id(
    provider_id="providerId_example",
    name="<NAME>",
    enabled=False,
    service_account_json={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### service_account_json: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="service_account_json-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

FCM service account JSON.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateFcmProviderByIdRequest`](./appwrite_server_python_sdk/type/messaging_update_fcm_provider_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/fcm/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.update_mailgun_provider`<a id="appwriteservermessagingupdate_mailgun_provider"></a>

Update a Mailgun provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_mailgun_provider_response = appwriteserver.messaging.update_mailgun_provider(
    provider_id="providerId_example",
    name="<NAME>",
    api_key="<API_KEY>",
    domain="<DOMAIN>",
    is_eu_region=False,
    enabled=False,
    from_name="<FROM_NAME>",
    from_email="email@example.com",
    reply_to_name="<REPLY_TO_NAME>",
    reply_to_email="<REPLY_TO_EMAIL>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### api_key: `str`<a id="api_key-str"></a>

Mailgun API Key.

##### domain: `str`<a id="domain-str"></a>

Mailgun Domain.

##### is_eu_region: `bool`<a id="is_eu_region-bool"></a>

Set as EU region.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### from_name: `str`<a id="from_name-str"></a>

Sender Name.

##### from_email: `str`<a id="from_email-str"></a>

Sender email address.

##### reply_to_name: `str`<a id="reply_to_name-str"></a>

Name set in the reply to field for the mail. Default value is sender name.

##### reply_to_email: `str`<a id="reply_to_email-str"></a>

Email set in the reply to field for the mail. Default value is sender email.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateMailgunProviderRequest`](./appwrite_server_python_sdk/type/messaging_update_mailgun_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/mailgun/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.update_msg91_provider`<a id="appwriteservermessagingupdate_msg91_provider"></a>

Update a MSG91 provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_msg91_provider_response = appwriteserver.messaging.update_msg91_provider(
    provider_id="providerId_example",
    name="<NAME>",
    enabled=False,
    sender_id="<SENDER_ID>",
    auth_key="<AUTH_KEY>",
    _from="<FROM>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### sender_id: `str`<a id="sender_id-str"></a>

Msg91 Sender ID.

##### auth_key: `str`<a id="auth_key-str"></a>

Msg91 Auth Key.

##### _from: `str`<a id="_from-str"></a>

Sender number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateMsg91ProviderRequest`](./appwrite_server_python_sdk/type/messaging_update_msg91_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/msg91/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.update_provider`<a id="appwriteservermessagingupdate_provider"></a>

Update a Sendgrid provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_provider_response = appwriteserver.messaging.update_provider(
    provider_id="providerId_example",
    name="<NAME>",
    enabled=False,
    api_key="<API_KEY>",
    from_name="<FROM_NAME>",
    from_email="email@example.com",
    reply_to_name="<REPLY_TO_NAME>",
    reply_to_email="<REPLY_TO_EMAIL>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### api_key: `str`<a id="api_key-str"></a>

Sendgrid API key.

##### from_name: `str`<a id="from_name-str"></a>

Sender Name.

##### from_email: `str`<a id="from_email-str"></a>

Sender email address.

##### reply_to_name: `str`<a id="reply_to_name-str"></a>

Name set in the Reply To field for the mail. Default value is Sender Name.

##### reply_to_email: `str`<a id="reply_to_email-str"></a>

Email set in the Reply To field for the mail. Default value is Sender Email.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateProviderRequest`](./appwrite_server_python_sdk/type/messaging_update_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/sendgrid/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.update_provider_by_id`<a id="appwriteservermessagingupdate_provider_by_id"></a>

Update a SMTP provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_provider_by_id_response = appwriteserver.messaging.update_provider_by_id(
    provider_id="providerId_example",
    name="<NAME>",
    host="<HOST>",
    port=1,
    username="<USERNAME>",
    password="<PASSWORD>",
    encryption="none",
    auto_tls=False,
    mailer="<MAILER>",
    from_name="<FROM_NAME>",
    from_email="email@example.com",
    reply_to_name="<REPLY_TO_NAME>",
    reply_to_email="<REPLY_TO_EMAIL>",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### host: `str`<a id="host-str"></a>

SMTP hosts. Either a single hostname or multiple semicolon-delimited hostnames. You can also specify a different port for each host such as `smtp1.example.com:25;smtp2.example.com`. You can also specify encryption type, for example: `tls://smtp1.example.com:587;ssl://smtp2.example.com:465\\\"`. Hosts will be tried in order.

##### port: `int`<a id="port-int"></a>

SMTP port.

##### username: `str`<a id="username-str"></a>

Authentication username.

##### password: `str`<a id="password-str"></a>

Authentication password.

##### encryption: `str`<a id="encryption-str"></a>

Encryption type. Can be 'ssl' or 'tls'

##### auto_tls: `bool`<a id="auto_tls-bool"></a>

Enable SMTP AutoTLS feature.

##### mailer: `str`<a id="mailer-str"></a>

The value to use for the X-Mailer header.

##### from_name: `str`<a id="from_name-str"></a>

Sender Name.

##### from_email: `str`<a id="from_email-str"></a>

Sender email address.

##### reply_to_name: `str`<a id="reply_to_name-str"></a>

Name set in the Reply To field for the mail. Default value is Sender Name.

##### reply_to_email: `str`<a id="reply_to_email-str"></a>

Email set in the Reply To field for the mail. Default value is Sender Email.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateProviderByIdRequest`](./appwrite_server_python_sdk/type/messaging_update_provider_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/smtp/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.update_push_notification`<a id="appwriteservermessagingupdate_push_notification"></a>

Update a push notification by its unique ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_push_notification_response = appwriteserver.messaging.update_push_notification(
    message_id="messageId_example",
    title="<TITLE>",
    topics=["string_example"],
    users=["string_example"],
    targets=["string_example"],
    body="<BODY>",
    data={},
    action="<ACTION>",
    image="[ID1:ID2]",
    icon="<ICON>",
    sound="<SOUND>",
    color="<COLOR>",
    tag="<TAG>",
    badge=1,
    draft=False,
    scheduled_at="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID.

##### title: `str`<a id="title-str"></a>

Title for push notification.

##### topics: [`MessagingUpdatePushNotificationRequestTopics`](./appwrite_server_python_sdk/type/messaging_update_push_notification_request_topics.py)<a id="topics-messagingupdatepushnotificationrequesttopicsappwrite_server_python_sdktypemessaging_update_push_notification_request_topicspy"></a>

##### users: [`MessagingUpdatePushNotificationRequestUsers`](./appwrite_server_python_sdk/type/messaging_update_push_notification_request_users.py)<a id="users-messagingupdatepushnotificationrequestusersappwrite_server_python_sdktypemessaging_update_push_notification_request_userspy"></a>

##### targets: [`MessagingUpdatePushNotificationRequestTargets`](./appwrite_server_python_sdk/type/messaging_update_push_notification_request_targets.py)<a id="targets-messagingupdatepushnotificationrequesttargetsappwrite_server_python_sdktypemessaging_update_push_notification_request_targetspy"></a>

##### body: `str`<a id="body-str"></a>

Body for push notification.

##### data: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="data-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Additional Data for push notification.

##### action: `str`<a id="action-str"></a>

Action for push notification.

##### image: `str`<a id="image-str"></a>

Image for push notification. Must be a compound bucket ID to file ID of a jpeg, png, or bmp image in Appwrite Storage.

##### icon: `str`<a id="icon-str"></a>

Icon for push notification. Available only for Android and Web platforms.

##### sound: `str`<a id="sound-str"></a>

Sound for push notification. Available only for Android and iOS platforms.

##### color: `str`<a id="color-str"></a>

Color for push notification. Available only for Android platforms.

##### tag: `str`<a id="tag-str"></a>

Tag for push notification. Available only for Android platforms.

##### badge: `int`<a id="badge-int"></a>

Badge for push notification. Available only for iOS platforms.

##### draft: `bool`<a id="draft-bool"></a>

Is message a draft

##### scheduled_at: `str`<a id="scheduled_at-str"></a>

Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdatePushNotificationRequest`](./appwrite_server_python_sdk/type/messaging_update_push_notification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./appwrite_server_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/push/{messageId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.update_sms_message`<a id="appwriteservermessagingupdate_sms_message"></a>

Update an email message by its unique ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_sms_message_response = appwriteserver.messaging.update_sms_message(
    message_id="messageId_example",
    topics=["string_example"],
    users=["string_example"],
    targets=["string_example"],
    content="<CONTENT>",
    draft=False,
    scheduled_at="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID.

##### topics: [`MessagingUpdateSmsMessageRequestTopics`](./appwrite_server_python_sdk/type/messaging_update_sms_message_request_topics.py)<a id="topics-messagingupdatesmsmessagerequesttopicsappwrite_server_python_sdktypemessaging_update_sms_message_request_topicspy"></a>

##### users: [`MessagingUpdateSmsMessageRequestUsers`](./appwrite_server_python_sdk/type/messaging_update_sms_message_request_users.py)<a id="users-messagingupdatesmsmessagerequestusersappwrite_server_python_sdktypemessaging_update_sms_message_request_userspy"></a>

##### targets: [`MessagingUpdateSmsMessageRequestTargets`](./appwrite_server_python_sdk/type/messaging_update_sms_message_request_targets.py)<a id="targets-messagingupdatesmsmessagerequesttargetsappwrite_server_python_sdktypemessaging_update_sms_message_request_targetspy"></a>

##### content: `str`<a id="content-str"></a>

Email Content.

##### draft: `bool`<a id="draft-bool"></a>

Is message a draft

##### scheduled_at: `str`<a id="scheduled_at-str"></a>

Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateSmsMessageRequest`](./appwrite_server_python_sdk/type/messaging_update_sms_message_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./appwrite_server_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/sms/{messageId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.update_telesign_provider`<a id="appwriteservermessagingupdate_telesign_provider"></a>

Update a Telesign provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_telesign_provider_response = appwriteserver.messaging.update_telesign_provider(
    provider_id="providerId_example",
    name="<NAME>",
    enabled=False,
    customer_id="<CUSTOMER_ID>",
    api_key="<API_KEY>",
    _from="<FROM>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### customer_id: `str`<a id="customer_id-str"></a>

Telesign customer ID.

##### api_key: `str`<a id="api_key-str"></a>

Telesign API key.

##### _from: `str`<a id="_from-str"></a>

Sender number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateTelesignProviderRequest`](./appwrite_server_python_sdk/type/messaging_update_telesign_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/telesign/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.update_textmagic_provider`<a id="appwriteservermessagingupdate_textmagic_provider"></a>

Update a Textmagic provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_textmagic_provider_response = appwriteserver.messaging.update_textmagic_provider(
    provider_id="providerId_example",
    name="<NAME>",
    enabled=False,
    username="<USERNAME>",
    api_key="<API_KEY>",
    _from="<FROM>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### username: `str`<a id="username-str"></a>

Textmagic username.

##### api_key: `str`<a id="api_key-str"></a>

Textmagic apiKey.

##### _from: `str`<a id="_from-str"></a>

Sender number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateTextmagicProviderRequest`](./appwrite_server_python_sdk/type/messaging_update_textmagic_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/textmagic/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.update_topic_by_id`<a id="appwriteservermessagingupdate_topic_by_id"></a>

Update a topic by its unique ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_topic_by_id_response = appwriteserver.messaging.update_topic_by_id(
    topic_id="topicId_example",
    name="<NAME>",
    subscribe=['["any"]'],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID.

##### name: `str`<a id="name-str"></a>

Topic Name.

##### subscribe: [`MessagingUpdateTopicByIdRequestSubscribe`](./appwrite_server_python_sdk/type/messaging_update_topic_by_id_request_subscribe.py)<a id="subscribe-messagingupdatetopicbyidrequestsubscribeappwrite_server_python_sdktypemessaging_update_topic_by_id_request_subscribepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateTopicByIdRequest`](./appwrite_server_python_sdk/type/messaging_update_topic_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Topic`](./appwrite_server_python_sdk/pydantic/topic.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics/{topicId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.update_twilio_provider`<a id="appwriteservermessagingupdate_twilio_provider"></a>

Update a Twilio provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_twilio_provider_response = appwriteserver.messaging.update_twilio_provider(
    provider_id="providerId_example",
    name="<NAME>",
    enabled=False,
    account_sid="<ACCOUNT_SID>",
    auth_token="<AUTH_TOKEN>",
    _from="<FROM>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### account_sid: `str`<a id="account_sid-str"></a>

Twilio account secret ID.

##### auth_token: `str`<a id="auth_token-str"></a>

Twilio authentication token.

##### _from: `str`<a id="_from-str"></a>

Sender number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateTwilioProviderRequest`](./appwrite_server_python_sdk/type/messaging_update_twilio_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/twilio/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.messaging.update_vonage_provider`<a id="appwriteservermessagingupdate_vonage_provider"></a>

Update a Vonage provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_vonage_provider_response = appwriteserver.messaging.update_vonage_provider(
    provider_id="providerId_example",
    name="<NAME>",
    enabled=False,
    api_key="<API_KEY>",
    api_secret="<API_SECRET>",
    _from="<FROM>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### api_key: `str`<a id="api_key-str"></a>

Vonage API key.

##### api_secret: `str`<a id="api_secret-str"></a>

Vonage API secret.

##### _from: `str`<a id="_from-str"></a>

Sender number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateVonageProviderRequest`](./appwrite_server_python_sdk/type/messaging_update_vonage_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_server_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/vonage/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.storage.create_file`<a id="appwriteserverstoragecreate_file"></a>

Create a new file. Before using this route, you should create a new bucket resource using either a [server integration](https://appwrite.io/docs/server/storage#storageCreateBucket) API or directly from your Appwrite console.

Larger files should be uploaded using multiple requests with the [content-range](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Range) header to send a partial request with a maximum supported chunk of `5MB`. The `content-range` header values should always be in bytes.

When the first request is sent, the server will return the **File** object, and the subsequent part request must include the file's **id** in `x-appwrite-id` header to allow the server to know that the partial upload is for the existing file and not for a new one.

If you're creating a new file using one of the Appwrite SDKs, all the chunking logic will be managed by the SDK internally.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_file_response = appwriteserver.storage.create_file(
    bucket_id="bucketId_example",
    file_id="<FILE_ID>",
    file="string_example",
    permissions=['["read("any")"]'],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).

##### file_id: `str`<a id="file_id-str"></a>

File ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### file: `str`<a id="file-str"></a>

Binary file. Appwrite SDKs provide helpers to handle file input. [Learn about file input](https://appwrite.io/docs/storage#file-input).

##### permissions: [`StorageCreateFileRequestPermissions`](./appwrite_server_python_sdk/type/storage_create_file_request_permissions.py)<a id="permissions-storagecreatefilerequestpermissionsappwrite_server_python_sdktypestorage_create_file_request_permissionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StorageCreateFileRequest`](./appwrite_server_python_sdk/type/storage_create_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`File`](./appwrite_server_python_sdk/pydantic/file.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}/files` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.storage.create_new_bucket`<a id="appwriteserverstoragecreate_new_bucket"></a>

Create a new storage bucket.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_bucket_response = appwriteserver.storage.create_new_bucket(
    bucket_id="<BUCKET_ID>",
    name="<NAME>",
    permissions=['["read("any")"]'],
    file_security=False,
    enabled=False,
    maximum_file_size=1,
    allowed_file_extensions=["string_example"],
    compression="none",
    encryption=False,
    antivirus=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Bucket name

##### permissions: [`StorageCreateNewBucketRequestPermissions`](./appwrite_server_python_sdk/type/storage_create_new_bucket_request_permissions.py)<a id="permissions-storagecreatenewbucketrequestpermissionsappwrite_server_python_sdktypestorage_create_new_bucket_request_permissionspy"></a>

##### file_security: `bool`<a id="file_security-bool"></a>

Enables configuring permissions for individual file. A user needs one of file or bucket level permissions to access a file. [Learn more about permissions](https://appwrite.io/docs/permissions).

##### enabled: `bool`<a id="enabled-bool"></a>

Is bucket enabled? When set to 'disabled', users cannot access the files in this bucket but Server SDKs with and API key can still access the bucket. No files are lost when this is toggled.

##### maximum_file_size: `int`<a id="maximum_file_size-int"></a>

Maximum file size allowed in bytes. Maximum allowed value is 30MB.

##### allowed_file_extensions: [`StorageCreateNewBucketRequestAllowedFileExtensions`](./appwrite_server_python_sdk/type/storage_create_new_bucket_request_allowed_file_extensions.py)<a id="allowed_file_extensions-storagecreatenewbucketrequestallowedfileextensionsappwrite_server_python_sdktypestorage_create_new_bucket_request_allowed_file_extensionspy"></a>

##### compression: `str`<a id="compression-str"></a>

Compression algorithm choosen for compression. Can be one of none,  [gzip](https://en.wikipedia.org/wiki/Gzip), or [zstd](https://en.wikipedia.org/wiki/Zstd), For file size above 20MB compression is skipped even if it's enabled

##### encryption: `bool`<a id="encryption-bool"></a>

Is encryption enabled? For file size above 20MB encryption is skipped even if it's enabled

##### antivirus: `bool`<a id="antivirus-bool"></a>

Is virus scanning enabled? For file size above 20MB AntiVirus scanning is skipped even if it's enabled

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StorageCreateNewBucketRequest`](./appwrite_server_python_sdk/type/storage_create_new_bucket_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Bucket`](./appwrite_server_python_sdk/pydantic/bucket.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.storage.delete_bucket_by_id`<a id="appwriteserverstoragedelete_bucket_by_id"></a>

Delete a storage bucket by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.storage.delete_bucket_by_id(
    bucket_id="bucketId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Bucket unique ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.storage.delete_file_by_id`<a id="appwriteserverstoragedelete_file_by_id"></a>

Delete a file by its unique ID. Only users with write permissions have access to delete this resource.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.storage.delete_file_by_id(
    bucket_id="bucketId_example",
    file_id="fileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).

##### file_id: `str`<a id="file_id-str"></a>

File ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}/files/{fileId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.storage.get_bucket_by_id`<a id="appwriteserverstorageget_bucket_by_id"></a>

Get a storage bucket by its unique ID. This endpoint response returns a JSON object with the storage bucket metadata.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_bucket_by_id_response = appwriteserver.storage.get_bucket_by_id(
    bucket_id="bucketId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Bucket unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Bucket`](./appwrite_server_python_sdk/pydantic/bucket.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.storage.get_file_by_id`<a id="appwriteserverstorageget_file_by_id"></a>

Get a file by its unique ID. This endpoint response returns a JSON object with the file metadata.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_file_by_id_response = appwriteserver.storage.get_file_by_id(
    bucket_id="bucketId_example",
    file_id="fileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).

##### file_id: `str`<a id="file_id-str"></a>

File ID.

#### 🔄 Return<a id="🔄-return"></a>

[`File`](./appwrite_server_python_sdk/pydantic/file.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}/files/{fileId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.storage.get_file_download`<a id="appwriteserverstorageget_file_download"></a>

Get a file content by its unique ID. The endpoint response return with a 'Content-Disposition: attachment' header that tells the browser to start downloading the file to user downloads directory.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.storage.get_file_download(
    bucket_id="bucketId_example",
    file_id="fileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Storage bucket ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).

##### file_id: `str`<a id="file_id-str"></a>

File ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}/files/{fileId}/download` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.storage.get_file_preview_image`<a id="appwriteserverstorageget_file_preview_image"></a>

Get a file preview image. Currently, this method supports preview for image files (jpg, png, and gif), other supported formats, like pdf, docs, slides, and spreadsheets, will return the file icon image. You can also pass query string arguments for cutting and resizing your preview image. Preview is supported only for image files smaller than 10MB.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.storage.get_file_preview_image(
    bucket_id="bucketId_example",
    file_id="fileId_example",
    width=0,
    height=0,
    gravity="center",
    quality=100,
    border_width=0,
    border_color="",
    border_radius=0,
    opacity=1,
    rotation=0,
    background="",
    output="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).

##### file_id: `str`<a id="file_id-str"></a>

File ID

##### width: `int`<a id="width-int"></a>

Resize preview image width, Pass an integer between 0 to 4000.

##### height: `int`<a id="height-int"></a>

Resize preview image height, Pass an integer between 0 to 4000.

##### gravity: `str`<a id="gravity-str"></a>

Image crop gravity. Can be one of center,top-left,top,top-right,left,right,bottom-left,bottom,bottom-right

##### quality: `int`<a id="quality-int"></a>

Preview image quality. Pass an integer between 0 to 100. Defaults to 100.

##### border_width: `int`<a id="border_width-int"></a>

Preview image border in pixels. Pass an integer between 0 to 100. Defaults to 0.

##### border_color: `str`<a id="border_color-str"></a>

Preview image border color. Use a valid HEX color, no # is needed for prefix.

##### border_radius: `int`<a id="border_radius-int"></a>

Preview image border radius in pixels. Pass an integer between 0 to 4000.

##### opacity: `Union[int, float]`<a id="opacity-unionint-float"></a>

Preview image opacity. Only works with images having an alpha channel (like png). Pass a number between 0 to 1.

##### rotation: `int`<a id="rotation-int"></a>

Preview image rotation in degrees. Pass an integer between -360 and 360.

##### background: `str`<a id="background-str"></a>

Preview image background color. Only works with transparent images (png). Use a valid HEX color, no # is needed for prefix.

##### output: `str`<a id="output-str"></a>

Output format type (jpeg, jpg, png, gif and webp).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}/files/{fileId}/preview` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.storage.get_file_view`<a id="appwriteserverstorageget_file_view"></a>

Get a file content by its unique ID. This endpoint is similar to the download method but returns with no  'Content-Disposition: attachment' header.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.storage.get_file_view(
    bucket_id="bucketId_example",
    file_id="fileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).

##### file_id: `str`<a id="file_id-str"></a>

File ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}/files/{fileId}/view` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.storage.list_buckets`<a id="appwriteserverstoragelist_buckets"></a>

Get a list of all the storage buckets. You can use the query params to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_buckets_response = appwriteserver.storage.list_buckets(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: enabled, name, fileSecurity, maximumFileSize, encryption, antivirus

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`BucketList`](./appwrite_server_python_sdk/pydantic/bucket_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.storage.list_files`<a id="appwriteserverstoragelist_files"></a>

Get a list of all the user files. You can use the query params to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_files_response = appwriteserver.storage.list_files(
    bucket_id="bucketId_example",
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, signature, mimeType, sizeOriginal, chunksTotal, chunksUploaded

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`FileList`](./appwrite_server_python_sdk/pydantic/file_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}/files` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.storage.update_bucket_by_id`<a id="appwriteserverstorageupdate_bucket_by_id"></a>

Update a storage bucket by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_bucket_by_id_response = appwriteserver.storage.update_bucket_by_id(
    name="<NAME>",
    bucket_id="bucketId_example",
    permissions=['["read("any")"]'],
    file_security=False,
    enabled=False,
    maximum_file_size=1,
    allowed_file_extensions=["string_example"],
    compression="none",
    encryption=False,
    antivirus=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Bucket name

##### bucket_id: `str`<a id="bucket_id-str"></a>

Bucket unique ID.

##### permissions: [`StorageUpdateBucketByIdRequestPermissions`](./appwrite_server_python_sdk/type/storage_update_bucket_by_id_request_permissions.py)<a id="permissions-storageupdatebucketbyidrequestpermissionsappwrite_server_python_sdktypestorage_update_bucket_by_id_request_permissionspy"></a>

##### file_security: `bool`<a id="file_security-bool"></a>

Enables configuring permissions for individual file. A user needs one of file or bucket level permissions to access a file. [Learn more about permissions](https://appwrite.io/docs/permissions).

##### enabled: `bool`<a id="enabled-bool"></a>

Is bucket enabled? When set to 'disabled', users cannot access the files in this bucket but Server SDKs with and API key can still access the bucket. No files are lost when this is toggled.

##### maximum_file_size: `int`<a id="maximum_file_size-int"></a>

Maximum file size allowed in bytes. Maximum allowed value is 30MB.

##### allowed_file_extensions: [`StorageUpdateBucketByIdRequestAllowedFileExtensions`](./appwrite_server_python_sdk/type/storage_update_bucket_by_id_request_allowed_file_extensions.py)<a id="allowed_file_extensions-storageupdatebucketbyidrequestallowedfileextensionsappwrite_server_python_sdktypestorage_update_bucket_by_id_request_allowed_file_extensionspy"></a>

##### compression: `str`<a id="compression-str"></a>

Compression algorithm choosen for compression. Can be one of none, [gzip](https://en.wikipedia.org/wiki/Gzip), or [zstd](https://en.wikipedia.org/wiki/Zstd), For file size above 20MB compression is skipped even if it's enabled

##### encryption: `bool`<a id="encryption-bool"></a>

Is encryption enabled? For file size above 20MB encryption is skipped even if it's enabled

##### antivirus: `bool`<a id="antivirus-bool"></a>

Is virus scanning enabled? For file size above 20MB AntiVirus scanning is skipped even if it's enabled

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StorageUpdateBucketByIdRequest`](./appwrite_server_python_sdk/type/storage_update_bucket_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Bucket`](./appwrite_server_python_sdk/pydantic/bucket.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.storage.update_file_by_id`<a id="appwriteserverstorageupdate_file_by_id"></a>

Update a file by its unique ID. Only users with write permissions have access to update this resource.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_file_by_id_response = appwriteserver.storage.update_file_by_id(
    bucket_id="bucketId_example",
    file_id="fileId_example",
    name="<NAME>",
    permissions=['["read("any")"]'],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).

##### file_id: `str`<a id="file_id-str"></a>

File unique ID.

##### name: `str`<a id="name-str"></a>

Name of the file

##### permissions: [`StorageUpdateFileByIdRequestPermissions`](./appwrite_server_python_sdk/type/storage_update_file_by_id_request_permissions.py)<a id="permissions-storageupdatefilebyidrequestpermissionsappwrite_server_python_sdktypestorage_update_file_by_id_request_permissionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StorageUpdateFileByIdRequest`](./appwrite_server_python_sdk/type/storage_update_file_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`File`](./appwrite_server_python_sdk/pydantic/file.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}/files/{fileId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.teams.create_membership_request`<a id="appwriteserverteamscreate_membership_request"></a>

Invite a new member to join your team. Provide an ID for existing users, or invite unregistered users using an email or phone number. If initiated from a Client SDK, Appwrite will send an email or sms with a link to join the team to the invited user, and an account will be created for them if one doesn't exist. If initiated from a Server SDK, the new member will be added automatically to the team.

You only need to provide one of a user ID, email, or phone number. Appwrite will prioritize accepting the user ID > email > phone number if you provide more than one of these parameters.

Use the `url` parameter to redirect the user from the invitation email to your app. After the user is redirected, use the [Update Team Membership Status](https://appwrite.io/docs/references/cloud/client-web/teams#updateMembershipStatus) endpoint to allow the user to accept the invitation to the team. 

Please note that to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) Appwrite will accept the only redirect URLs under the domains you have added as a platform on the Appwrite Console.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_membership_request_response = appwriteserver.teams.create_membership_request(
    roles=["string_example"],
    team_id="teamId_example",
    email="email@example.com",
    user_id="<USER_ID>",
    phone="+12065550100",
    url="https://example.com",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### roles: [`TeamsCreateMembershipRequestRequestRoles`](./appwrite_server_python_sdk/type/teams_create_membership_request_request_roles.py)<a id="roles-teamscreatemembershiprequestrequestrolesappwrite_server_python_sdktypeteams_create_membership_request_request_rolespy"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

##### email: `str`<a id="email-str"></a>

Email of the new team member.

##### user_id: `str`<a id="user_id-str"></a>

ID of the user to be added to a team.

##### phone: `str`<a id="phone-str"></a>

Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

##### url: `str`<a id="url-str"></a>

URL to redirect the user back to your app from the invitation email.  Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

##### name: `str`<a id="name-str"></a>

Name of the new team member. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsCreateMembershipRequestRequest`](./appwrite_server_python_sdk/type/teams_create_membership_request_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Membership`](./appwrite_server_python_sdk/pydantic/membership.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/memberships` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.teams.create_new_team`<a id="appwriteserverteamscreate_new_team"></a>

Create a new team. The user who creates the team will automatically be assigned as the owner of the team. Only the users with the owner role can invite new members, add new owners and delete or update the team.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_team_response = appwriteserver.teams.create_new_team(
    team_id="<TEAM_ID>",
    name="<NAME>",
    roles=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Team name. Max length: 128 chars.

##### roles: [`TeamsCreateNewTeamRequestRoles`](./appwrite_server_python_sdk/type/teams_create_new_team_request_roles.py)<a id="roles-teamscreatenewteamrequestrolesappwrite_server_python_sdktypeteams_create_new_team_request_rolespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsCreateNewTeamRequest`](./appwrite_server_python_sdk/type/teams_create_new_team_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Team`](./appwrite_server_python_sdk/pydantic/team.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.teams.delete_membership`<a id="appwriteserverteamsdelete_membership"></a>

This endpoint allows a user to leave a team or for a team owner to delete the membership of any other team member. You can also use this endpoint to delete a user membership even if it is not accepted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.teams.delete_membership(
    team_id="teamId_example",
    membership_id="membershipId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

##### membership_id: `str`<a id="membership_id-str"></a>

Membership ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/memberships/{membershipId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.teams.get_by_id`<a id="appwriteserverteamsget_by_id"></a>

Get a team by its ID. All team members have read access for this resource.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = appwriteserver.teams.get_by_id(
    team_id="teamId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Team`](./appwrite_server_python_sdk/pydantic/team.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.teams.get_membership`<a id="appwriteserverteamsget_membership"></a>

Get a team member by the membership unique id. All team members have read access for this resource.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_membership_response = appwriteserver.teams.get_membership(
    team_id="teamId_example",
    membership_id="membershipId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

##### membership_id: `str`<a id="membership_id-str"></a>

Membership ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Membership`](./appwrite_server_python_sdk/pydantic/membership.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/memberships/{membershipId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.teams.get_prefs_by_id`<a id="appwriteserverteamsget_prefs_by_id"></a>

Get the team's shared preferences by its unique ID. If a preference doesn't need to be shared by all team members, prefer storing them in [user preferences](https://appwrite.io/docs/references/cloud/client-web/account#getPrefs).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_prefs_by_id_response = appwriteserver.teams.get_prefs_by_id(
    team_id="teamId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Preferences`](./appwrite_server_python_sdk/pydantic/preferences.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/prefs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.teams.get_user_teams`<a id="appwriteserverteamsget_user_teams"></a>

Get a list of all the teams in which the current user is a member. You can use the parameters to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_teams_response = appwriteserver.teams.get_user_teams(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, total, billingPlan

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`TeamList`](./appwrite_server_python_sdk/pydantic/team_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.teams.list_memberships`<a id="appwriteserverteamslist_memberships"></a>

Use this endpoint to list a team's members using the team's ID. All team members have read access to this endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_memberships_response = appwriteserver.teams.list_memberships(
    team_id="teamId_example",
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, teamId, invited, joined, confirm

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`MembershipList`](./appwrite_server_python_sdk/pydantic/membership_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.teams.remove_team_by_id`<a id="appwriteserverteamsremove_team_by_id"></a>

Delete a team using its ID. Only team members with the owner role can delete the team.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.teams.remove_team_by_id(
    team_id="teamId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.teams.update_membership_roles`<a id="appwriteserverteamsupdate_membership_roles"></a>

Modify the roles of a team member. Only team members with the owner role have access to this endpoint. Learn more about [roles and permissions](https://appwrite.io/docs/permissions).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_membership_roles_response = appwriteserver.teams.update_membership_roles(
    roles=["string_example"],
    team_id="teamId_example",
    membership_id="membershipId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### roles: [`TeamsUpdateMembershipRolesRequestRoles`](./appwrite_server_python_sdk/type/teams_update_membership_roles_request_roles.py)<a id="roles-teamsupdatemembershiprolesrequestrolesappwrite_server_python_sdktypeteams_update_membership_roles_request_rolespy"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

##### membership_id: `str`<a id="membership_id-str"></a>

Membership ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsUpdateMembershipRolesRequest`](./appwrite_server_python_sdk/type/teams_update_membership_roles_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Membership`](./appwrite_server_python_sdk/pydantic/membership.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/memberships/{membershipId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.teams.update_membership_status`<a id="appwriteserverteamsupdate_membership_status"></a>

Use this endpoint to allow a user to accept an invitation to join a team after being redirected back to your app from the invitation email received by the user.

If the request is successful, a session for the user is automatically created.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_membership_status_response = appwriteserver.teams.update_membership_status(
    user_id="<USER_ID>",
    secret="<SECRET>",
    team_id="teamId_example",
    membership_id="membershipId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### secret: `str`<a id="secret-str"></a>

Secret key.

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

##### membership_id: `str`<a id="membership_id-str"></a>

Membership ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsUpdateMembershipStatusRequest`](./appwrite_server_python_sdk/type/teams_update_membership_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Membership`](./appwrite_server_python_sdk/pydantic/membership.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/memberships/{membershipId}/status` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.teams.update_name_by_id`<a id="appwriteserverteamsupdate_name_by_id"></a>

Update the team's name by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_name_by_id_response = appwriteserver.teams.update_name_by_id(
    name="<NAME>",
    team_id="teamId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

New team name. Max length: 128 chars.

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsUpdateNameByIdRequest`](./appwrite_server_python_sdk/type/teams_update_name_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Team`](./appwrite_server_python_sdk/pydantic/team.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.teams.update_prefs_by_id`<a id="appwriteserverteamsupdate_prefs_by_id"></a>

Update the team's preferences by its unique ID. The object you pass is stored as is and replaces any previous value. The maximum allowed prefs size is 64kB and throws an error if exceeded.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_prefs_by_id_response = appwriteserver.teams.update_prefs_by_id(
    prefs={},
    team_id="teamId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### prefs: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="prefs-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Prefs key-value JSON object.

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsUpdatePrefsByIdRequest`](./appwrite_server_python_sdk/type/teams_update_prefs_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Preferences`](./appwrite_server_python_sdk/pydantic/preferences.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/prefs` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.create_argon2_user`<a id="appwriteserveruserscreate_argon2_user"></a>

Create a new user. Password provided must be hashed with the [Argon2](https://en.wikipedia.org/wiki/Argon2) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_argon2_user_response = appwriteserver.users.create_argon2_user(
    user_id="<USER_ID>",
    email="email@example.com",
    password="password",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password hashed using Argon2.

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateArgon2UserRequest`](./appwrite_server_python_sdk/type/users_create_argon2_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/argon2` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.create_bcrypt_user`<a id="appwriteserveruserscreate_bcrypt_user"></a>

Create a new user. Password provided must be hashed with the [Bcrypt](https://en.wikipedia.org/wiki/Bcrypt) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_bcrypt_user_response = appwriteserver.users.create_bcrypt_user(
    user_id="<USER_ID>",
    email="email@example.com",
    password="password",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password hashed using Bcrypt.

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateBcryptUserRequest`](./appwrite_server_python_sdk/type/users_create_bcrypt_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/bcrypt` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.create_md5_user`<a id="appwriteserveruserscreate_md5_user"></a>

Create a new user. Password provided must be hashed with the [MD5](https://en.wikipedia.org/wiki/MD5) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_md5_user_response = appwriteserver.users.create_md5_user(
    user_id="<USER_ID>",
    email="email@example.com",
    password="password",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password hashed using MD5.

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateMd5UserRequest`](./appwrite_server_python_sdk/type/users_create_md5_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/md5` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.create_mfa_recovery_codes`<a id="appwriteserveruserscreate_mfa_recovery_codes"></a>

Generate recovery codes used as backup for MFA flow for User ID. Recovery codes can be used as a MFA verification type in [createMfaChallenge](/docs/references/cloud/client-web/account#createMfaChallenge) method by client SDK.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_mfa_recovery_codes_response = appwriteserver.users.create_mfa_recovery_codes(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🔄 Return<a id="🔄-return"></a>

[`MfaRecoveryCodes`](./appwrite_server_python_sdk/pydantic/mfa_recovery_codes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/mfa/recovery-codes` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.create_new_user`<a id="appwriteserveruserscreate_new_user"></a>

Create a new user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_user_response = appwriteserver.users.create_new_user(
    user_id="<USER_ID>",
    email="email@example.com",
    phone="+12065550100",
    password="string_example",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### phone: `str`<a id="phone-str"></a>

Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

##### password: `str`<a id="password-str"></a>

Plain text user password. Must be at least 8 chars.

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateNewUserRequest`](./appwrite_server_python_sdk/type/users_create_new_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.create_phpass_user`<a id="appwriteserveruserscreate_phpass_user"></a>

Create a new user. Password provided must be hashed with the [PHPass](https://www.openwall.com/phpass/) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_phpass_user_response = appwriteserver.users.create_phpass_user(
    user_id="<USER_ID>",
    email="email@example.com",
    password="password",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or pass the string `ID.unique()`to auto generate it. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password hashed using PHPass.

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreatePhpassUserRequest`](./appwrite_server_python_sdk/type/users_create_phpass_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/phpass` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.create_scrypt_modified_user`<a id="appwriteserveruserscreate_scrypt_modified_user"></a>

Create a new user. Password provided must be hashed with the [Scrypt Modified](https://gist.github.com/Meldiron/eecf84a0225eccb5a378d45bb27462cc) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_scrypt_modified_user_response = appwriteserver.users.create_scrypt_modified_user(
    user_id="<USER_ID>",
    email="email@example.com",
    password="password",
    password_salt="<PASSWORD_SALT>",
    password_salt_separator="<PASSWORD_SALT_SEPARATOR>",
    password_signer_key="<PASSWORD_SIGNER_KEY>",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password hashed using Scrypt Modified.

##### password_salt: `str`<a id="password_salt-str"></a>

Salt used to hash password.

##### password_salt_separator: `str`<a id="password_salt_separator-str"></a>

Salt separator used to hash password.

##### password_signer_key: `str`<a id="password_signer_key-str"></a>

Signer key used to hash password.

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateScryptModifiedUserRequest`](./appwrite_server_python_sdk/type/users_create_scrypt_modified_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/scrypt-modified` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.create_scrypt_user`<a id="appwriteserveruserscreate_scrypt_user"></a>

Create a new user. Password provided must be hashed with the [Scrypt](https://github.com/Tarsnap/scrypt) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_scrypt_user_response = appwriteserver.users.create_scrypt_user(
    user_id="<USER_ID>",
    email="email@example.com",
    password="password",
    password_salt="<PASSWORD_SALT>",
    password_cpu=1,
    password_memory=1,
    password_parallel=1,
    password_length=1,
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password hashed using Scrypt.

##### password_salt: `str`<a id="password_salt-str"></a>

Optional salt used to hash password.

##### password_cpu: `int`<a id="password_cpu-int"></a>

Optional CPU cost used to hash password.

##### password_memory: `int`<a id="password_memory-int"></a>

Optional memory cost used to hash password.

##### password_parallel: `int`<a id="password_parallel-int"></a>

Optional parallelization cost used to hash password.

##### password_length: `int`<a id="password_length-int"></a>

Optional hash length used to hash password.

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateScryptUserRequest`](./appwrite_server_python_sdk/type/users_create_scrypt_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/scrypt` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.create_session`<a id="appwriteserveruserscreate_session"></a>

Creates a session for a user. Returns an immediately usable session object.

If you want to generate a token for a custom authentication flow, use the [POST /users/{userId}/tokens](https://appwrite.io/docs/server/users#createToken) endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_session_response = appwriteserver.users.create_session(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_server_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/sessions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.create_sha_user`<a id="appwriteserveruserscreate_sha_user"></a>

Create a new user. Password provided must be hashed with the [SHA](https://en.wikipedia.org/wiki/Secure_Hash_Algorithm) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_sha_user_response = appwriteserver.users.create_sha_user(
    user_id="<USER_ID>",
    email="email@example.com",
    password="password",
    password_version="sha1",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password hashed using SHA.

##### password_version: `str`<a id="password_version-str"></a>

Optional SHA version used to hash password. Allowed values are: 'sha1', 'sha224', 'sha256', 'sha384', 'sha512/224', 'sha512/256', 'sha512', 'sha3-224', 'sha3-256', 'sha3-384', 'sha3-512'

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateShaUserRequest`](./appwrite_server_python_sdk/type/users_create_sha_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/sha` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.create_target_messaging`<a id="appwriteserveruserscreate_target_messaging"></a>

Create a messaging target.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_target_messaging_response = appwriteserver.users.create_target_messaging(
    target_id="<TARGET_ID>",
    provider_type="email",
    identifier="<IDENTIFIER>",
    user_id="userId_example",
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### target_id: `str`<a id="target_id-str"></a>

Target ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### provider_type: `str`<a id="provider_type-str"></a>

The target provider type. Can be one of the following: `email`, `sms` or `push`.

##### identifier: `str`<a id="identifier-str"></a>

The target identifier (token, email, phone etc.)

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Message will be sent to this target from the specified provider ID. If no provider ID is set the first setup provider will be used.

##### name: `str`<a id="name-str"></a>

Target name. Max length: 128 chars. For example: My Awesome App Galaxy S23.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateTargetMessagingRequest`](./appwrite_server_python_sdk/type/users_create_target_messaging_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Target`](./appwrite_server_python_sdk/pydantic/target.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/targets` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.create_token_session`<a id="appwriteserveruserscreate_token_session"></a>

Returns a token with a secret key for creating a session. If the provided user ID has not be registered, a new user will be created. Use the returned user ID and secret and submit a request to the [PUT /account/sessions/custom](https://appwrite.io/docs/references/cloud/client-web/account#updateCustomSession) endpoint to complete the login process.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_token_session_response = appwriteserver.users.create_token_session(
    user_id="userId_example",
    length=4,
    expire=60,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### length: `int`<a id="length-int"></a>

Token length in characters. The default length is 6 characters

##### expire: `int`<a id="expire-int"></a>

Token expiration period in seconds. The default expiration is 15 minutes.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateTokenSessionRequest`](./appwrite_server_python_sdk/type/users_create_token_session_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_server_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/tokens` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.delete_authenticator`<a id="appwriteserverusersdelete_authenticator"></a>

Delete an authenticator app.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_authenticator_response = appwriteserver.users.delete_authenticator(
    user_id="userId_example",
    type="totp",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### type: `str`<a id="type-str"></a>

Type of authenticator.

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/mfa/authenticators/{type}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.delete_identity_by_id`<a id="appwriteserverusersdelete_identity_by_id"></a>

Delete an identity by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.users.delete_identity_by_id(
    identity_id="identityId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### identity_id: `str`<a id="identity_id-str"></a>

Identity ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/identities/{identityId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.delete_session_by_id`<a id="appwriteserverusersdelete_session_by_id"></a>

Delete a user sessions by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.users.delete_session_by_id(
    user_id="userId_example",
    session_id="sessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### session_id: `str`<a id="session_id-str"></a>

Session ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/sessions/{sessionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.delete_target_messaging`<a id="appwriteserverusersdelete_target_messaging"></a>

Delete a messaging target.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.users.delete_target_messaging(
    user_id="userId_example",
    target_id="targetId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### target_id: `str`<a id="target_id-str"></a>

Target ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/targets/{targetId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.delete_user_by_id`<a id="appwriteserverusersdelete_user_by_id"></a>

Delete a user by its unique ID, thereby releasing it's ID. Since ID is released and can be reused, all user-related resources like documents or storage files should be deleted before user deletion. If you want to keep ID reserved, use the [updateStatus](https://appwrite.io/docs/server/users#usersUpdateStatus) endpoint instead.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.users.delete_user_by_id(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.delete_user_sessions`<a id="appwriteserverusersdelete_user_sessions"></a>

Delete all user's sessions by using the user's unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteserver.users.delete_user_sessions(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/sessions` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.get_by_id`<a id="appwriteserverusersget_by_id"></a>

Get a user by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = appwriteserver.users.get_by_id(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.get_mfa_recovery_codes`<a id="appwriteserverusersget_mfa_recovery_codes"></a>

Get recovery codes that can be used as backup for MFA flow by User ID. Before getting codes, they must be generated using [createMfaRecoveryCodes](/docs/references/cloud/client-web/account#createMfaRecoveryCodes) method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_mfa_recovery_codes_response = appwriteserver.users.get_mfa_recovery_codes(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🔄 Return<a id="🔄-return"></a>

[`MfaRecoveryCodes`](./appwrite_server_python_sdk/pydantic/mfa_recovery_codes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/mfa/recovery-codes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.get_user_prefs`<a id="appwriteserverusersget_user_prefs"></a>

Get the user preferences by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_prefs_response = appwriteserver.users.get_user_prefs(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Preferences`](./appwrite_server_python_sdk/pydantic/preferences.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/prefs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.get_user_target_by_id`<a id="appwriteserverusersget_user_target_by_id"></a>

Get a user's push notification target by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_target_by_id_response = appwriteserver.users.get_user_target_by_id(
    user_id="userId_example",
    target_id="targetId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### target_id: `str`<a id="target_id-str"></a>

Target ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Target`](./appwrite_server_python_sdk/pydantic/target.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/targets/{targetId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.list_all`<a id="appwriteserveruserslist_all"></a>

Get a list of all the project's users. You can use the query params to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = appwriteserver.users.list_all(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, email, phone, status, passwordUpdate, registration, emailVerification, phoneVerification, labels

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`UserList`](./appwrite_server_python_sdk/pydantic/user_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.list_factors`<a id="appwriteserveruserslist_factors"></a>

List the factors available on the account to be used as a MFA challange.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_factors_response = appwriteserver.users.list_factors(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🔄 Return<a id="🔄-return"></a>

[`MfaFactors`](./appwrite_server_python_sdk/pydantic/mfa_factors.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/mfa/factors` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.list_identities`<a id="appwriteserveruserslist_identities"></a>

Get identities for all users.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_identities_response = appwriteserver.users.list_identities(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, provider, providerUid, providerEmail, providerAccessTokenExpiry

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`IdentityList`](./appwrite_server_python_sdk/pydantic/identity_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/identities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.list_memberships`<a id="appwriteserveruserslist_memberships"></a>

Get the user membership list by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_memberships_response = appwriteserver.users.list_memberships(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🔄 Return<a id="🔄-return"></a>

[`MembershipList`](./appwrite_server_python_sdk/pydantic/membership_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.list_sessions`<a id="appwriteserveruserslist_sessions"></a>

Get the user sessions list by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_sessions_response = appwriteserver.users.list_sessions(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🔄 Return<a id="🔄-return"></a>

[`SessionList`](./appwrite_server_python_sdk/pydantic/session_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/sessions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.list_targets`<a id="appwriteserveruserslist_targets"></a>

List the messaging targets that are associated with a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_targets_response = appwriteserver.users.list_targets(
    user_id="userId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, email, phone, status, passwordUpdate, registration, emailVerification, phoneVerification, labels

#### 🔄 Return<a id="🔄-return"></a>

[`TargetList`](./appwrite_server_python_sdk/pydantic/target_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/targets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.list_user_logs`<a id="appwriteserveruserslist_user_logs"></a>

Get the user activity logs list by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_user_logs_response = appwriteserver.users.list_user_logs(
    user_id="userId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset

#### 🔄 Return<a id="🔄-return"></a>

[`LogList`](./appwrite_server_python_sdk/pydantic/log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.regenerate_mfa_recovery_codes`<a id="appwriteserverusersregenerate_mfa_recovery_codes"></a>

Regenerate recovery codes that can be used as backup for MFA flow by User ID. Before regenerating codes, they must be first generated using [createMfaRecoveryCodes](/docs/references/cloud/client-web/account#createMfaRecoveryCodes) method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
regenerate_mfa_recovery_codes_response = (
    appwriteserver.users.regenerate_mfa_recovery_codes(
        user_id="userId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🔄 Return<a id="🔄-return"></a>

[`MfaRecoveryCodes`](./appwrite_server_python_sdk/pydantic/mfa_recovery_codes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/mfa/recovery-codes` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.update_email_by_id`<a id="appwriteserverusersupdate_email_by_id"></a>

Update the user email by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_email_by_id_response = appwriteserver.users.update_email_by_id(
    email="email@example.com",
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

User email.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateEmailByIdRequest`](./appwrite_server_python_sdk/type/users_update_email_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/email` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.update_email_verification`<a id="appwriteserverusersupdate_email_verification"></a>

Update the user email verification status by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_email_verification_response = appwriteserver.users.update_email_verification(
    email_verification=False,
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email_verification: `bool`<a id="email_verification-bool"></a>

User email verification status.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateEmailVerificationRequest`](./appwrite_server_python_sdk/type/users_update_email_verification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/verification` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.update_labels_by_id`<a id="appwriteserverusersupdate_labels_by_id"></a>

Update the user labels by its unique ID. 

Labels can be used to grant access to resources. While teams are a way for user's to share access to a resource, labels can be defined by the developer to grant access without an invitation. See the [Permissions docs](https://appwrite.io/docs/permissions) for more info.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_labels_by_id_response = appwriteserver.users.update_labels_by_id(
    labels=["string_example"],
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### labels: [`UsersUpdateLabelsByIdRequestLabels`](./appwrite_server_python_sdk/type/users_update_labels_by_id_request_labels.py)<a id="labels-usersupdatelabelsbyidrequestlabelsappwrite_server_python_sdktypeusers_update_labels_by_id_request_labelspy"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateLabelsByIdRequest`](./appwrite_server_python_sdk/type/users_update_labels_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/labels` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.update_mfa_status`<a id="appwriteserverusersupdate_mfa_status"></a>

Enable or disable MFA on a user account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_mfa_status_response = appwriteserver.users.update_mfa_status(
    mfa=False,
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### mfa: `bool`<a id="mfa-bool"></a>

Enable or disable MFA.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateMfaStatusRequest`](./appwrite_server_python_sdk/type/users_update_mfa_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/mfa` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.update_password_by_id`<a id="appwriteserverusersupdate_password_by_id"></a>

Update the user password by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_password_by_id_response = appwriteserver.users.update_password_by_id(
    password="string_example",
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### password: `str`<a id="password-str"></a>

New user password. Must be at least 8 chars.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdatePasswordByIdRequest`](./appwrite_server_python_sdk/type/users_update_password_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/password` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.update_phone_by_id`<a id="appwriteserverusersupdate_phone_by_id"></a>

Update the user phone by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_phone_by_id_response = appwriteserver.users.update_phone_by_id(
    number="+12065550100",
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### number: `str`<a id="number-str"></a>

User phone number.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdatePhoneByIdRequest`](./appwrite_server_python_sdk/type/users_update_phone_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/phone` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.update_phone_verification`<a id="appwriteserverusersupdate_phone_verification"></a>

Update the user phone verification status by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_phone_verification_response = appwriteserver.users.update_phone_verification(
    phone_verification=False,
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### phone_verification: `bool`<a id="phone_verification-bool"></a>

User phone verification status.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdatePhoneVerificationRequest`](./appwrite_server_python_sdk/type/users_update_phone_verification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/verification/phone` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.update_preferences_by_id`<a id="appwriteserverusersupdate_preferences_by_id"></a>

Update the user preferences by its unique ID. The object you pass is stored as is, and replaces any previous value. The maximum allowed prefs size is 64kB and throws error if exceeded.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_preferences_by_id_response = appwriteserver.users.update_preferences_by_id(
    prefs={},
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### prefs: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="prefs-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Prefs key-value JSON object.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdatePreferencesByIdRequest`](./appwrite_server_python_sdk/type/users_update_preferences_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Preferences`](./appwrite_server_python_sdk/pydantic/preferences.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/prefs` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.update_status`<a id="appwriteserverusersupdate_status"></a>

Update the user status by its unique ID. Use this endpoint as an alternative to deleting a user if you want to keep user's ID reserved.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_status_response = appwriteserver.users.update_status(
    status=False,
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `bool`<a id="status-bool"></a>

User Status. To activate the user pass `true` and to block the user pass `false`.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateStatusRequest`](./appwrite_server_python_sdk/type/users_update_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/status` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.update_target_messaging`<a id="appwriteserverusersupdate_target_messaging"></a>

Update a messaging target.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_target_messaging_response = appwriteserver.users.update_target_messaging(
    user_id="userId_example",
    target_id="targetId_example",
    identifier="<IDENTIFIER>",
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### target_id: `str`<a id="target_id-str"></a>

Target ID.

##### identifier: `str`<a id="identifier-str"></a>

The target identifier (token, email, phone etc.)

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Message will be sent to this target from the specified provider ID. If no provider ID is set the first setup provider will be used.

##### name: `str`<a id="name-str"></a>

Target name. Max length: 128 chars. For example: My Awesome App Galaxy S23.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateTargetMessagingRequest`](./appwrite_server_python_sdk/type/users_update_target_messaging_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Target`](./appwrite_server_python_sdk/pydantic/target.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/targets/{targetId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteserver.users.update_user_by_name`<a id="appwriteserverusersupdate_user_by_name"></a>

Update the user name by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_user_by_name_response = appwriteserver.users.update_user_by_name(
    name="<NAME>",
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateUserByNameRequest`](./appwrite_server_python_sdk/type/users_update_user_by_name_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_server_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/name` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
