# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_boolean.post import CreateBooleanAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections.post import CreateCollection
from appwrite_server_python_sdk.paths.databases.post import CreateDatabase
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_datetime.post import CreateDatetimeAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_documents.post import CreateDocument
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_email.post import CreateEmailAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_enum.post import CreateEnumAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_float.post import CreateFloatAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_indexes.post import CreateIndex
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_integer.post import CreateIntegerAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_ip.post import CreateIpAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_relationship.post import CreateRelationshipAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_string.post import CreateStringAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_url.post import CreateUrlAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_key.delete import DeleteAttributeById
from appwrite_server_python_sdk.paths.databases_database_id.delete import DeleteById
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id.delete import DeleteCollectionById
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_documents_document_id.delete import DeleteDocumentById
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_indexes_key.delete import DeleteIndex
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_key.get import GetAttributeById
from appwrite_server_python_sdk.paths.databases_database_id.get import GetById
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id.get import GetCollectionById
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_documents_document_id.get import GetDocumentById
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_indexes_key.get import GetIndexById
from appwrite_server_python_sdk.paths.databases.get import ListAll
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes.get import ListCollectionAttributes
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_documents.get import ListCollectionDocuments
from appwrite_server_python_sdk.paths.databases_database_id_collections.get import ListCollections
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_indexes.get import ListIndexes
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_boolean_key.patch import UpdateBooleanAttribute
from appwrite_server_python_sdk.paths.databases_database_id.put import UpdateById
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id.put import UpdateCollectionById
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_datetime_key.patch import UpdateDatetimeAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_documents_document_id.patch import UpdateDocumentById
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_email_key.patch import UpdateEmailAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_enum_key.patch import UpdateEnumAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_float_key.patch import UpdateFloatAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_integer_key.patch import UpdateIntegerAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_ip_key.patch import UpdateIpAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_key_relationship.patch import UpdateRelationshipAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_string_key.patch import UpdateStringAttribute
from appwrite_server_python_sdk.paths.databases_database_id_collections_collection_id_attributes_url_key.patch import UpdateUrlAttribute
from appwrite_server_python_sdk.apis.tags.databases_api_raw import DatabasesApiRaw


class DatabasesApi(
    CreateBooleanAttribute,
    CreateCollection,
    CreateDatabase,
    CreateDatetimeAttribute,
    CreateDocument,
    CreateEmailAttribute,
    CreateEnumAttribute,
    CreateFloatAttribute,
    CreateIndex,
    CreateIntegerAttribute,
    CreateIpAttribute,
    CreateRelationshipAttribute,
    CreateStringAttribute,
    CreateUrlAttribute,
    DeleteAttributeById,
    DeleteById,
    DeleteCollectionById,
    DeleteDocumentById,
    DeleteIndex,
    GetAttributeById,
    GetById,
    GetCollectionById,
    GetDocumentById,
    GetIndexById,
    ListAll,
    ListCollectionAttributes,
    ListCollectionDocuments,
    ListCollections,
    ListIndexes,
    UpdateBooleanAttribute,
    UpdateById,
    UpdateCollectionById,
    UpdateDatetimeAttribute,
    UpdateDocumentById,
    UpdateEmailAttribute,
    UpdateEnumAttribute,
    UpdateFloatAttribute,
    UpdateIntegerAttribute,
    UpdateIpAttribute,
    UpdateRelationshipAttribute,
    UpdateStringAttribute,
    UpdateUrlAttribute,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: DatabasesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = DatabasesApiRaw(api_client)
