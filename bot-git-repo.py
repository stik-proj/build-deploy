import requests
import string
import random

# 깃헙 API 토큰 설정
github_token = ''

# 레포지토리 생성 API URL
github_api_url = 'https://api.github.com/orgs/stik-proj/repos'

# 생성할 레포지토리 정보
repo_name_prefix = 'deploy'
repo_description = 'Project '

# 랜덤 문자열 생성 함수


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


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


for i in range(10):
    repo_name = repo_name_prefix + "-" + generate_word()
    payload = {
        "name": repo_name,
        "description": repo_description + repo_name
    }
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {github_token}"
    }
    response = requests.post(github_api_url, headers=headers, json=payload)
    if response.status_code == 201:
        print(f"{repo_name} created successfully.")
    else:
        print(f"Failed to create {repo_name}.")
