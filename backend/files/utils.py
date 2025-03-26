# files/utils.py
import os
from uuid import uuid4
from django.conf import settings
from azure.storage.blob import BlobServiceClient

def upload_to_azure_blob(file, container_name=None):
    try:
        # Create blob service client
        blob_service_client = BlobServiceClient.from_connection_string(
            settings.AZURE_STORAGE_CONNECTION_STRING
        )
        
        container_name = container_name or settings.AZURE_STORAGE_CONTAINER_NAME
        container_client = blob_service_client.get_container_client(container_name)
        
        # Create unique filename
        file_extension = os.path.splitext(file.name)[1]
        unique_filename = f"{uuid4()}{file_extension}"
        
        # Upload file
        blob_client = container_client.get_blob_client(unique_filename)
        blob_client.upload_blob(file.read())
        
        # Generate URL
        blob_url = f"https://{settings.AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net/{container_name}/{unique_filename}"
        
        return {
            'url': blob_url,
            'filename': unique_filename,
            'original_name': file.name,
            'size': file.size
        }
    except Exception as e:
        print(f"Azure Blob Storage Upload Error: {e}")
        return None

def delete_from_azure_blob(filename, container_name=None):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            settings.AZURE_STORAGE_CONNECTION_STRING
        )
        container_name = container_name or settings.AZURE_STORAGE_CONTAINER_NAME
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=filename)
        blob_client.delete_blob()
        return True
    except Exception as e:
        print(f"Azure Blob Storage Delete Error: {e}")
        return False