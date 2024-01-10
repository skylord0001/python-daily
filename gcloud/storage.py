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
