<details>
<summary>Welcome Google Cloud Platform</summary>

Google Cloud Platform stands out for its reliability, scalability, and a wide range of services that support various workloads. Key reasons to choose GCP for deploying python apps include:

-   **Global Infrastructure**: GCP's extensive global infrastructure ensures low-latency access to your application for users worldwide.
    
-   **Scalability**: GCP provides scalable solutions to accommodate the growth of your application, ensuring optimal performance under varying workloads.
    
-   **Integrated Services**: GCP offers a suite of integrated services for storage, databases, machine learning, and more, facilitating a seamless development and deployment experience.
    

## Choosing the Right Service

### App Engine

-   **Managed Service**: App Engine is a fully managed platform that abstracts away infrastructure management, allowing developers to focus solely on their application code.
    
-   **Automatic Scaling**: App Engine automatically adjusts resources based on traffic, ensuring optimal performance without manual intervention.
    

### Compute Engine

-   **Customizable Virtual Machines**: Compute Engine offers virtual machines with full control over configurations, making it suitable for applications with specific requirements.
    
-   **Persistent Storage**: Ideal for applications that require persistent disk storage, Compute Engine allows you to attach and detach storage volumes as needed.
    

### Cloud Run

-   **Containerized Deployments**: Cloud Run is designed for containerized applications, providing flexibility in choosing your preferred programming language and dependencies.
    
-   **Serverless**: Cloud Run is serverless, meaning you only pay for the compute resources used during the execution of your containers.
   

## Conclusion

Google Cloud Platform provides a versatile environment for deploying python applications. Choose the service that best aligns with your application's requirements, whether it's the simplicity of App Engine, the flexibility of Compute Engine, or the containerized approach with Cloud Run. Follow the steps outlined in this guide to ensure a smooth deployment process on GCP.


## References

-   [Google Cloud Documentation](https://cloud.google.com/python/docs/getting-started)
-   [Google Cloud Codelabs](https://codelabs.developers.google.com/codelabs/cloud-app-engine-python3)
- [google-cloud-django-settings](https://github.com/devfemibadmus/python-daily/tree/master/gcloud/django/settings.py)

</details>


<details>
<summary>Perform CRUD operation on Google Cloud Storage</summary>

```python
from google.cloud import storage
import json

# Set your Google Cloud Storage credentials (make sure it has the necessary permissions)
client = storage.Client.from_service_account_json('path/to/your/credentials.json')

# Set your bucket name
bucket_name = 'your-bucket-name'

# Create a bucket object
bucket = client.get_bucket(bucket_name)

def create_operation(data, file_name='db.json'):
    # Serialize the data to a JSON-formatted string
    json_data = json.dumps(data)
    
    # Write the JSON data to a file
    blob = bucket.blob(file_name)
    blob.upload_from_string(json_data)
    
    print(f"Data created successfully in '{file_name}'")

def read_operation(file_name='db.json'):
    # Get the blob
    blob = bucket.blob(file_name)
    
    try:
        # Download the content
        json_content = blob.download_as_text()
        
        # Deserialize the JSON data
        read_data = json.loads(json_content)
        
        print(f"Read Data from '{file_name}':")
        print(read_data)
    except storage.exceptions.NotFound:
        print(f"File '{file_name}' not found.")

def update_operation(data, file_name='db.json'):
    # Perform update by calling the create operation with new data
    create_operation(data, file_name)
    
    print(f"Data updated successfully in '{file_name}'")

def delete_operation(file_name='db.json'):
    # Get the blob
    blob = bucket.blob(file_name)
    
    try:
        # Delete the blob
        blob.delete()
        
        print(f"File '{file_name}' deleted successfully.")
    except storage.exceptions.NotFound:
        print(f"File '{file_name}' not found. Deletion failed.")

# Sample data
users = [
    {"id": 1, "name": "John Doe", "age": 25},
    {"id": 2, "name": "Jane Doe", "age": 30}
]

# CRUD operations
create_operation(users)
read_operation()
update_operation([
    {"id": 1, "name": "Updated John Doe", "age": 26},
    {"id": 3, "name": "New User", "age": 22}
])
read_operation()
delete_operation()
read_operation()  # This should indicate that the file is not found after deletion
```
</details>


## References

-   [Google Cloud Documentation](https://cloud.google.com/python/docs/getting-started)
-   [Google Cloud Codelabs](https://codelabs.developers.google.com/codelabs/cloud-app-engine-python3)
- [google-cloud-django](https://github.com/devfemibadmus/python-daily/tree/master/gcloud/django/settings.py)