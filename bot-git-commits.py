import os
from datetime import datetime
from git import Repo, GitCommandError

# 깃 저장소 경로
repo_path = "/Users/gilbert/workspace/staika/deploy-giqajay"

# 깃헙 개인 접근 토큰
access_token = ""

while True:
    # 현재 시간을 파일 이름으로 지정
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"{now}.txt"

    # 파일 생성
    with open(filename, "w") as f:
        f.write("Hello, world!")

    try:
        # 깃 저장소 객체 생성
        repo = Repo(repo_path)

        # 변경된 파일 추가
        repo.git.add(filename)

        # 변경 내용을 커밋
        commit_message = f"Add {filename}"
        repo.index.commit(commit_message)

        # 깃헙으로 변경 내용을 푸시
        origin = repo.remote(name="origin")
        url = origin.url.replace("https://", f"https://{access_token}@")
        origin.url = url
        origin.push()

    except GitCommandError as e:
        print(f"An error occurred: {e}")

    # 5분 대기
    time.sleep(300)
