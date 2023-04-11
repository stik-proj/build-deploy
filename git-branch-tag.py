import requests
import json
import string
import random
import time

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


# Github API access token
access_token = ''

# Github organization and repository information
org_name = 'stik-proj'
repo_name = 'deploy-giqajay'

# Create new branch
base_branch_name = 'main'

while True:
    new_branch_name = 'deploy' + '-' + generate_word()

    # Github API endpoint URL for creating a new branch
    url = f'https://api.github.com/repos/{org_name}/{repo_name}/git/refs'

    # Get base branch SHA
    response = requests.get(f'https://api.github.com/repos/{org_name}/{repo_name}/git/refs/heads/{base_branch_name}', headers={
                            'Authorization': f'token {access_token}'})
    response_json = json.loads(response.content)
    base_branch_sha = response_json['object']['sha']

    # Create new branch payload
    payload = {
        "ref": "refs/heads/" + new_branch_name,
        "sha": base_branch_sha
    }

    # Create new branch
    response = requests.post(
        url, headers={'Authorization': f'token {access_token}'}, json=payload)

    # Check if new branch was created successfully
    if response.status_code == 201:
        print(f'New branch {new_branch_name} created successfully')
    else:
        print(
            f'Error creating new branch: {response.status_code} - {response.content}')

    # Create new pull request
    pull_request_title = generate_word()
    pull_request_body = generate_word()
    base_branch = 'main'
    head_branch = new_branch_name

    # Github API endpoint URL for creating a new pull request
    url = f'https://api.github.com/repos/{org_name}/{repo_name}/pulls'

    # Create new pull request payload
    payload = {
        "title": pull_request_title,
        "body": pull_request_body,
        "head": head_branch,
        "base": base_branch
    }

    # Create new tag
    tag_name = generate_word()
    tag_message = generate_word()

    # Github API endpoint URL for creating
    url = f'https://api.github.com/repos/{org_name}/{repo_name}/git/tags'

    # Create new tag payload
    payload = {
        "tag": tag_name,
        "message": tag_message,
        "object": base_branch_sha,
        "type": "commit",
        "tagger": {
            "name": "YOUR_NAME",
            "email": "YOUR_EMAIL"
        }
    }

    # Create new tag
    response = requests.post(
        url, headers={'Authorization': f'token {access_token}'}, json=payload)

    # Check if new tag was created successfully
    if response.status_code == 201:
        print('New tag created successfully')
    else:
        print(
            f'Error creating new tag: {response.status_code} - {response.content}')

    # 10초 대기
    time.sleep(10)
