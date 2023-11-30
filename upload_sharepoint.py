import requests
from requests.auth import HTTPBasicAuth

# SharePoint site URL
site_url = "https://your-sharepoint-site-url"

# SharePoint document library and destination folder
library_name = "Shared Documents"
destination_folder = "/Folder"

# SharePoint credentials (username and password)
username = "your-username"
password = "your-password"

# File to be uploaded
file_to_upload = "file_to_upload.txt"

# SharePoint REST API endpoint for uploading a file
upload_url = f"{site_url}/_api/web/GetFolderByServerRelativePath(decodedurl='{library_name}{destination_folder}')/Files/add(url='{file_to_upload}',overwrite=true)"

# Set up the authentication using basic authentication
auth = HTTPBasicAuth(username, password)

# Read the file content
with open(file_to_upload, 'rb') as file:
    file_content = file.read()

# Set headers for the request
headers = {
    'Content-Type': 'application/json;odata=verbose',
    'X-RequestDigest': 'Fetch'  # This header requires an additional step to obtain the X-RequestDigest value
}

# Make a POST request to upload the file
response = requests.post(upload_url, auth=auth, headers=headers, data=file_content)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("File uploaded successfully.")
else:
    print(f"Failed to upload file. Status Code: {response.status_code}")
    print(response.text)
