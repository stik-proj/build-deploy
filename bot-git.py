from github import Github

# GitHub API에 연결합니다.
g = Github("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")

# 새로운 레포지토리를 만듭니다.
user = g.get_user()
repo_name = "python-bot-proj"
repo = user.create_repo(repo_name)

# 생성한 레포지토리의 URL을 출력합니다.
print(repo.html_url)
