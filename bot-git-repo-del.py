import requests

# 깃헙 API 토큰 설정
github_token = ''

# Base URL for Github API
base_url = 'https://api.github.com'

# Organization name
org_name = 'stik-proj'

repo_prefix = 'k8s-'

# Function to get the list of repositories matching the search query


def get_org_repo_names():
    # API endpoint for getting the list of repositories in the organization
    repo_endpoint = f'/orgs/{org_name}/repos?type=public'
    # URL for the repository endpoint
    url = base_url + repo_endpoint
    # Headers for the API request
    headers = {'Authorization': 'token ' + github_token}

    repo_names = []
    # Loop over all the pages of repository results
    while url:
        # API request to get the list of repositories in the organization
        response = requests.get(url, headers=headers)
        # Parse the response JSON to get the list of repository names
        for repo in response.json():
            repo_names.append(repo['name'])
        # Check if there is another page of results
        if 'next' in response.links:
            url = response.links['next']['url']
        else:
            url = None
    # API request to get the list of repositories in the organization
    # response = requests.get(url, headers=headers)
    # Parse the response JSON to get the list of repository names
    # repo_names = [repo['name'] for repo in response.json()]
    return repo_names

# Function to delete a repository


def delete_repo(repo_name):
    # API endpoint for deleting a repository
    delete_endpoint = '/repos/{org}/{repo}'
    # URL for the delete endpoint
    url = base_url + delete_endpoint.format(org=org_name, repo=repo_name)
    # Headers for the API request
    headers = {'Authorization': 'token ' + github_token}
    # API request to delete the repository
    response = requests.delete(url, headers=headers)
    # Print the status code of the response
    print(response.status_code)


# Get the list of repositories matching the search query
repo_names = get_org_repo_names()
print(f'repo_names: {repo_names}')

# Loop through the repository names and delete each repository
for repo_name in repo_names:
    if repo_name.startswith(repo_prefix):
        print(f'delete_repo: {repo_name}')
        delete_repo(repo_name)
