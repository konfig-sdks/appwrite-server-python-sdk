# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_boolean.post import CreateBooleanAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections.post import CreateCollectionRaw
from appwrite_server_python_sdk.paths.databases.post import CreateDatabaseRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_datetime.post import CreateDatetimeAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_documents.post import CreateDocumentRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_email.post import CreateEmailAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_enum.post import CreateEnumAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_float.post import CreateFloatAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_indexes.post import CreateIndexRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_integer.post import CreateIntegerAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_ip.post import CreateIpAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_relationship.post import CreateRelationshipAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_string.post import CreateStringAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_url.post import CreateUrlAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_key.delete import DeleteAttributeByIdRaw
from appwrite_server_python_sdk.paths.databases_database_id.delete import DeleteByIdRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id.delete import DeleteCollectionByIdRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_documents_document_id.delete import DeleteDocumentByIdRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_indexes_key.delete import DeleteIndexRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_key.get import GetAttributeByIdRaw
from appwrite_server_python_sdk.paths.databases_database_id.get import GetByIdRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id.get import GetCollectionByIdRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_documents_document_id.get import GetDocumentByIdRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_indexes_key.get import GetIndexByIdRaw
from appwrite_server_python_sdk.paths.databases.get import ListAllRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes.get import ListCollectionAttributesRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_documents.get import ListCollectionDocumentsRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections.get import ListCollectionsRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_indexes.get import ListIndexesRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_boolean_key.patch import UpdateBooleanAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id.put import UpdateByIdRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id.put import UpdateCollectionByIdRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_datetime_key.patch import UpdateDatetimeAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_documents_document_id.patch import UpdateDocumentByIdRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_email_key.patch import UpdateEmailAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_enum_key.patch import UpdateEnumAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_float_key.patch import UpdateFloatAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_integer_key.patch import UpdateIntegerAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_ip_key.patch import UpdateIpAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_key_relationship.patch import UpdateRelationshipAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_string_key.patch import UpdateStringAttributeRaw
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_url_key.patch import UpdateUrlAttributeRaw


class DatabasesApiRaw(
    CreateBooleanAttributeRaw,
    CreateCollectionRaw,
    CreateDatabaseRaw,
    CreateDatetimeAttributeRaw,
    CreateDocumentRaw,
    CreateEmailAttributeRaw,
    CreateEnumAttributeRaw,
    CreateFloatAttributeRaw,
    CreateIndexRaw,
    CreateIntegerAttributeRaw,
    CreateIpAttributeRaw,
    CreateRelationshipAttributeRaw,
    CreateStringAttributeRaw,
    CreateUrlAttributeRaw,
    DeleteAttributeByIdRaw,
    DeleteByIdRaw,
    DeleteCollectionByIdRaw,
    DeleteDocumentByIdRaw,
    DeleteIndexRaw,
    GetAttributeByIdRaw,
    GetByIdRaw,
    GetCollectionByIdRaw,
    GetDocumentByIdRaw,
    GetIndexByIdRaw,
    ListAllRaw,
    ListCollectionAttributesRaw,
    ListCollectionDocumentsRaw,
    ListCollectionsRaw,
    ListIndexesRaw,
    UpdateBooleanAttributeRaw,
    UpdateByIdRaw,
    UpdateCollectionByIdRaw,
    UpdateDatetimeAttributeRaw,
    UpdateDocumentByIdRaw,
    UpdateEmailAttributeRaw,
    UpdateEnumAttributeRaw,
    UpdateFloatAttributeRaw,
    UpdateIntegerAttributeRaw,
    UpdateIpAttributeRaw,
    UpdateRelationshipAttributeRaw,
    UpdateStringAttributeRaw,
    UpdateUrlAttributeRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
