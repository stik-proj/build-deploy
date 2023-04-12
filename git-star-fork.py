import requests

# Personal Access Token 설정
token = ""

# Organizations 이름 설정
org_name = "stik-proj"

# GitHub API endpoint 설정
api_endpoint = f"https://api.github.com/orgs/{org_name}/repos?type=public"

# Headers for the API request
headers = {'Authorization': 'token ' + token}

# 모든 Repository 정보 받아오기
repo_names = []
while api_endpoint:
    # API request to get the list of repositories in the organization
    response = requests.get(api_endpoint, headers=headers)
    # Parse the response JSON to get the list of repository names
    for repo in response.json():
        repo_names.append(repo['name'])
    # Check if there is another page of results
    if 'next' in response.links:
        api_endpoint = response.links['next']['url']
    else:
        api_endpoint = None

# 모든 Repository에 Star 부여
for repo_name in repo_names:
    # 모든 Repository에 Star 부여
    response = requests.put(
        f"https://api.github.com/user/starred/{org_name}/{repo_name}", headers={"Authorization": f"Token {token}"})
    if response.status_code == 204:
        print(f"Starred {repo_name}")
    else:
        print(f"Failed to star {repo_name}")

    # 레포지토리 포크 API
    fork_url = f"https://api.github.com/repos/{org_name}/{repo_name}/forks"
    # 레포지토리 포크 요청
    response = requests.post(
        fork_url, headers={"Authorization": f"Token {token}"})
    if response.status_code == 202:
        print(f"Successfully forked {repo_name}")
    else:
        print(f"Failed to fork {repo_name}")
