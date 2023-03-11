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

# Process the results.
print(response_dict.keys())
