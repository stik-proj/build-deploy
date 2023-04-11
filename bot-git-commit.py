import requests
import time
import string
import random

# GitHub API 토큰
github_token = ''

# 커밋 생성을 위한 정보
commit_message = "Deploy commit"
file_content = "Deploy, a word "
file_path = "bot.py"
repo_owner = "stik-proj"
repo_name = "deploy-giqajay"
branch_name = "main"

# GitHub API URL
github_api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'

url = f'https://api.github.com/repos/{org_name}/{repo_name}/git/commits'

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'


def generate_word():
    word = ''
    length = random.randint(4, 8)  # 단어 길이는 4~8자리로 설정
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(consonants)
        else:
            word += random.choice(vowels)
    return word


while True:
    # 커밋할 파일의 현재 내용 가져오기
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {github_token}"
    }
    response = requests.get(github_api_url, headers=headers)
    if response.status_code == 200:
        current_content = response.json()["content"]
        current_sha = response.json()["sha"]
    else:
        print("Failed to get current file content. " + github_api_url)
        break

    # 새로운 커밋 내용 작성
    new_content = file_content + generate_word()
    if new_content == current_content:
        print("Content has not changed.")
        continue

    # 새로운 커밋 생성
    payload = {
        "message": commit_message,
        "content": new_content,
        "sha": current_sha,
        "branch": branch_name
    }
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {github_token}"
    }
    response = requests.put(github_api_url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Commit created successfully.")
    else:
        print("Failed to create commit.")

    # 5분 대기
    time.sleep(300)
