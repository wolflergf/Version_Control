import requests
import getpass
import os


def create_github_repo(repo_name, github_token):
    """Creates a new repository on GitHub using the provided credentials.

    Args:
        repo_name (str): The desired name of the repository.
        github_token (str): A GitHub personal access token with repo permissions.
    """

    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"name": repo_name}

    response = requests.post(
        "https://api.github.com/user/repos", json=data, headers=headers
    )

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully!")
    elif response.status_code == 401:
        print("Unauthorized. Please check your GitHub token.")
    elif response.status_code == 422:  # Handle potential validation errors
        error_message = response.json().get("message")
        print(f"Failed to create repository: {error_message}")
    else:
        print(f"Failed to create repository. Status code: {response.status_code}")
        print(response.text)  # More informative than response.json() for general errors


if __name__ == "__main__":
    repo_name = input("Enter the name of the repository you want to create: ")

    # Avoid storing token in plain text
    github_token = getpass.getpass("Enter your GitHub personal access token: ")

    # Consider using environment variables for the token:
    # github_token = os.getenv('GITHUB_TOKEN')

    create_github_repo(repo_name, github_token)
