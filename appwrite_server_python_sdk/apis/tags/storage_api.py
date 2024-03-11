# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_server_python_sdk.paths.storage_buckets_bucket_id_files.post import CreateFile
from appwrite_server_python_sdk.paths.storage_buckets.post import CreateNewBucket
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id.delete import DeleteBucketById
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id_files_file_id.delete import DeleteFileById
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id.get import GetBucketById
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id_files_file_id.get import GetFileById
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id_files_file_id_download.get import GetFileDownload
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id_files_file_id_preview.get import GetFilePreviewImage
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id_files_file_id_view.get import GetFileView
from appwrite_server_python_sdk.paths.storage_buckets.get import ListBuckets
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id_files.get import ListFiles
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id.put import UpdateBucketById
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id_files_file_id.put import UpdateFileById
from appwrite_server_python_sdk.apis.tags.storage_api_raw import StorageApiRaw


class StorageApi(
    CreateFile,
    CreateNewBucket,
    DeleteBucketById,
    DeleteFileById,
    GetBucketById,
    GetFileById,
    GetFileDownload,
    GetFilePreviewImage,
    GetFileView,
    ListBuckets,
    ListFiles,
    UpdateBucketById,
    UpdateFileById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: StorageApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = StorageApiRaw(api_client)
