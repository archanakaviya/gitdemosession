import requests
from requests.auth import HTTPBasicAuth

# SharePoint site URL
site_url = "https://your-sharepoint-site-url"

# SharePoint document library and file path
library_name = "Shared Documents"
file_path = "/Folder/YourFile.txt"

# SharePoint credentials (username and password)
username = "your-username"
password = "your-password"

# SharePoint REST API endpoint for downloading a file
download_url = f"{site_url}/_api/web/GetFileByServerRelativePath(decodedurl='{library_name}{file_path}')/$value"

# Set up the authentication using basic authentication
auth = HTTPBasicAuth(username, password)

# Make a GET request to download the file
response = requests.get(download_url, auth=auth)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the downloaded file
    with open("downloaded_file.txt", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print(f"Failed to download file. Status Code: {response.status_code}")
    print(response.text)
