import os
import random
import time
from datetime import datetime
from git import Repo, GitCommandError

# 깃 저장소 경로
repo_path = "/Users/gilbert/workspace/staika/build-deploy"

# 깃헙 개인 접근 토큰
access_token = "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"

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
    # 현재 시간을 파일 이름으로 지정
    filename = "2023-04-10-20-18-07.txt"

    # 파일 생성
    with open(filename, "w") as f:
        f.write(generate_word())

    try:
        # 깃 저장소 객체 생성
        repo = Repo(repo_path)

        # 변경된 파일 추가
        repo.git.add(filename)

        # 변경 내용을 커밋
        commit_message = f"Added {generate_word()}"
        repo.index.commit(commit_message)

        # 깃헙으로 변경 내용을 푸시
        origin = repo.remote(name="origin")
        #url = origin.url.replace("https://", f"https://{access_token}@")
        url = f"https://{access_token}@github.com/stik-proj/build-deploy.git"
        origin.set_url = url
        origin.push()
        print(f"{url} commit successfully.")

    except GitCommandError as e:
        print(f"An error occurred: {e}")

    # 5분 대기
    time.sleep(300)
