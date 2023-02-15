from azure.storage.blob import BlobClient


def write_to_file(container: str, filename: str, content: bytes):
    blob = BlobClient.from_connection_string(
        conn_str='DefaultEndpointsProtocol=https;AccountName=mydatalakestoragepoc;AccountKey=0tn3DNX5S9i44VlzCXL31JXmAcwat8u2futPxA+QNtPSdsYHxGkO1RxZeG+2qMNccOOEXRrbuRRb+AStEaAWRA==;EndpointSuffix=core.windows.net',
        container_name=container,
        blob_name=filename,
    )
    if blob.exists():
        blob.delete_blob()
    blob.upload_blob(data=content)
    
