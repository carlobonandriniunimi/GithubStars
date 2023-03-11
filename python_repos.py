import requests

# Make an API call and check the response
# ....com/ => directs the request to github API response
# search/repositories => tells the API to search through all repos
# the ? => passing arguments, q=... => query
# language:python => repo with python as primary language
# +sort:stars => sort repo by stars given
# +stars:>1000 => repo with more than 10000 stars
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

# Use the v3 of github API and return a JSON
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url=url, headers=headers)
# If request was successful => 200
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")
