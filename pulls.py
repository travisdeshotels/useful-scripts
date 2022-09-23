import json
import os
import requests
import yaml

from dotenv import load_dotenv


def get_data(org, repo):
    return_data = requests.get(url=f'https://api.github.com/repos/{org["name"]}/{repo}/pulls',
                               headers={'Authorization': f'access_token {os.environ["git_token"]}'})
    return json.loads(return_data.text)


def get_pulls():
    load_dotenv()
    titles = []
    with open('config/repos.yml', 'r') as stream:
        orgs_with_repos = yaml.safe_load(stream)

    for org in orgs_with_repos['orgs']:
        for repo in org['repos']:
            pulls = get_data(org, repo)
            for pull in pulls:
                if not pull['draft']:
                    titles.append(pull['title'])
                    print(pull['title'])
                    print(pull['html_url'])
    return titles


if __name__ == '__main__':
    get_pulls()
