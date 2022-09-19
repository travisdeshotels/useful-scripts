import json
import os
import requests
import yaml

from dotenv import load_dotenv

load_dotenv()
with open('config/repos.yml', 'r') as stream:
    orgs_with_repos = yaml.safe_load(stream)

for org in orgs_with_repos['orgs']:
    for repo in org['repos']:
        pulls = requests.get(url=f'https://api.github.com/repos/{org["name"]}/{repo}/pulls',
                             headers={'Authorization': f'access_token {os.environ["git_token"]}'})
        for pull in json.loads(pulls.text):
            if not pull['draft']:
                print(pull['title'])
                print(pull['html_url'])
