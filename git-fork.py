import requests
import json

# Github Personal Access Token
token = ""

# 기관명
org_name = "stik-proj"

# 기관의 레포지토리 목록을 가져오는 API
org_repos_url = f"https://api.github.com/orgs/{org_name}/repos"

# 기관의 레포지토리 목록 가져오기
response = requests.get(org_repos_url, headers={
                        "Authorization": f"Token {token}"})

# 가져온 데이터가 JSON 형태이므로 파싱
repos = json.loads(response.text)

# 레포지토리 포크하기
for repo in repos:
    # 레포지토리 이름
    repo_name = repo["name"]
    # 레포지토리 포크 API
    fork_url = f"https://api.github.com/repos/{org_name}/{repo_name}/forks"
    # 레포지토리 포크 요청
    response = requests.post(
        fork_url, headers={"Authorization": f"Token {token}"})
    if response.status_code == 202:
        print(f"Successfully forked {repo_name}")
    else:
        print(f"Failed to fork {repo_name}")
