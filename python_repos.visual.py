import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

# Use the v3 of github API and return a JSON
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url=url, headers=headers)
print(f"Status code: {r.status_code}")

# Process overall results.
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Process repository information.
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # Turn repo names into active links.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # Build hover texts.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    # Plotly supports html in text variables
    # <br /> adds line break
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)


# Make a visualization.
title = "Most-Starred Python Projects on Github"
labels = {'x': "Repository", 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title,
             labels=labels, hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)
fig.show()
