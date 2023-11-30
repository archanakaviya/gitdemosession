Copy code
import requests
from requests.auth import HTTPBasicAuth

# Azure DevOps organization and project details
organization = "your-organization"
project = "your-project"
repository = "your-repository"

# Personal Access Token (PAT) with code write permissions
pat = "your-personal-access-token"

# File details
file_path = "path/to/your/file.txt"
branch = "main"
commit_message = "Check-in file using Python script"

# Azure DevOps REST API endpoint for creating a new branch
create_branch_url = f"https://dev.azure.com/{organization}/{project}/_apis/git/repositories/{repository}/refs?filter={branch}&api-version=7.1"

# Azure DevOps REST API endpoint for pushing changes
push_changes_url = f"https://dev.azure.com/{organization}/{project}/_apis/git/repositories/{repository}/pushes?api-version=7.1"

# Set up the authentication using Personal Access Token (PAT)
auth = HTTPBasicAuth("", pat)

# Step 1: Create a new branch (optional, if the branch doesn't exist)
create_branch_payload = {
    "name": branch,
    "oldObjectId": "0000000000000000000000000000000000000000"
}

response = requests.post(create_branch_url, auth=auth, json=create_branch_payload)
response.raise_for_status()

# Step 2: Push changes to the branch
with open(file_path, "rb") as file:
    file_content = file.read()

change_payload = {
    "refUpdates": [
        {
            "name": f"refs/heads/{branch}",
            "oldObjectId": "0000000000000000000000000000000000000000"
        }
    ],
    "commits": [
        {
            "comment": commit_message,
            "changes": [
                {
                    "changeType": "add",
                    "item": {
                        "path": file_path
                    },
                    "newContent": {
                        "content": file_content,
                        "contentType": "rawtext"
                    }
                }
            ]
        }
    ]
}

response = requests.post(push_changes_url, auth=auth, json=change_payload)
response.raise_for_status()

print("File checked in successfully.")
