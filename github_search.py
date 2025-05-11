# github_search.py

from github import Github
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
g = Github(token)

def fetch_repositories(prompt, max_results=10):
    query = f"{prompt} in:name,description"
    result = g.search_repositories(query=query, sort="stars", order="desc")
    repos = []

    for repo in result[:max_results]:
        repos.append({
            "name": repo.full_name,
            "description": repo.description or "No description available.",
            "url": repo.html_url
        })

    return repos