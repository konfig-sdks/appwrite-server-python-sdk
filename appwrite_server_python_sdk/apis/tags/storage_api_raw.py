# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_server_python_sdk.paths.storage_buckets_bucket_id_files.post import CreateFileRaw
from appwrite_server_python_sdk.paths.storage_buckets.post import CreateNewBucketRaw
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id.delete import DeleteBucketByIdRaw
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id_files_file_id.delete import DeleteFileByIdRaw
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id.get import GetBucketByIdRaw
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id_files_file_id.get import GetFileByIdRaw
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id_files_file_id_download.get import GetFileDownloadRaw
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id_files_file_id_preview.get import GetFilePreviewImageRaw
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id_files_file_id_view.get import GetFileViewRaw
from appwrite_server_python_sdk.paths.storage_buckets.get import ListBucketsRaw
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id_files.get import ListFilesRaw
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id.put import UpdateBucketByIdRaw
from appwrite_server_python_sdk.paths.storage_buckets_bucket_id_files_file_id.put import UpdateFileByIdRaw


class StorageApiRaw(
    CreateFileRaw,
    CreateNewBucketRaw,
    DeleteBucketByIdRaw,
    DeleteFileByIdRaw,
    GetBucketByIdRaw,
    GetFileByIdRaw,
    GetFileDownloadRaw,
    GetFilePreviewImageRaw,
    GetFileViewRaw,
    ListBucketsRaw,
    ListFilesRaw,
    UpdateBucketByIdRaw,
    UpdateFileByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
