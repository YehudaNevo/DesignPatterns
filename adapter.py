from abc import ABC, abstractmethod

# Target Interface
class CloudStorage(ABC):
    @abstractmethod
    def create_bucket(self, bucket_name):
        pass

    @abstractmethod
    def delete_bucket(self, bucket_name):
        pass

# Adaptee 1: AWS S3
class AWSS3:
    def create_s3_bucket(self, bucket_name):
        print(f"Creating AWS S3 bucket: {bucket_name}")

    def delete_s3_bucket(self, bucket_name):
        print(f"Deleting AWS S3 bucket: {bucket_name}")

# Adaptee 2: Google Cloud Storage
class GoogleCloudStorage:
    def create_gcs_bucket(self, bucket_name):
        print(f"Creating Google Cloud Storage bucket: {bucket_name}")

    def delete_gcs_bucket(self, bucket_name):
        print(f"Deleting Google Cloud Storage bucket: {bucket_name}")

# Adaptee 3: Azure Blob Storage
class AzureBlobStorage:
    def create_azure_container(self, container_name):
        print(f"Creating Azure Blob Storage container: {container_name}")

    def delete_azure_container(self, container_name):
        print(f"Deleting Azure Blob Storage container: {container_name}")

# Adapter 1: AWS S3 Adapter
class AWSS3Adapter(CloudStorage):
    def __init__(self):
        self.aws_s3 = AWSS3()

    def create_bucket(self, bucket_name):
        self.aws_s3.create_s3_bucket(bucket_name)

    def delete_bucket(self, bucket_name):
        self.aws_s3.delete_s3_bucket(bucket_name)

# Adapter 2: Google Cloud Storage Adapter
class GoogleCloudStorageAdapter(CloudStorage):
    def __init__(self):
        self.google_cloud_storage = GoogleCloudStorage()

    def create_bucket(self, bucket_name):
        self.google_cloud_storage.create_gcs_bucket(bucket_name)

    def delete_bucket(self, bucket_name):
        self.google_cloud_storage.delete_gcs_bucket(bucket_name)

# Adapter 3: Azure Blob Storage Adapter
class AzureBlobStorageAdapter(CloudStorage):
    def __init__(self):
        self.azure_blob_storage = AzureBlobStorage()

    def create_bucket(self, bucket_name):
        self.azure_blob_storage.create_azure_container(bucket_name)

    def delete_bucket(self, bucket_name):
        self.azure_blob_storage.delete_azure_container(bucket_name)

# Client Code
def main(cloud_storage: CloudStorage, bucket_name):
    cloud_storage.create_bucket(bucket_name)
    # Perform other operations like uploading, downloading, etc.
    cloud_storage.delete_bucket(bucket_name)

# Usage
aws_s3_adapter = AWSS3Adapter()
main(aws_s3_adapter, "my-aws-bucket")

google_cloud_storage_adapter = GoogleCloudStorageAdapter()
main(google_cloud_storage_adapter, "my-gcs-bucket")

azure_blob_storage_adapter = AzureBlobStorageAdapter()
main(azure_blob_storage_adapter, "my-azure-container")


