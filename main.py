import requests


def github_repo(repo_name, github_token):
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
    else:
        print(f"Failed to create repository. Status code: {response.status_code}")
        print(response.json())


if __name__ == "__main__":
    repo_name = input("Enter the name of the repository you want to create: ")
    github_token = input("Enter your GitHub personal access token: ")
    create_github_repo(repo_name, github_token)
