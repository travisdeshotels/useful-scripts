import json
import os
import requests
import yaml

from colorslib.colors import underline
from colorslib.colors import red
from dotenv import load_dotenv


def get_data(org, repo):
    return_data = requests.get(url=f'https://api.github.com/repos/{org["name"]}/{repo}/pulls',
                               headers={'Authorization': f'access_token {os.environ["git_token"]}'})
    return json.loads(return_data.text)


def dump_data(items, header):
    if len(items) > 0:
        print(header)
        for item in items:
            print(item['title'])
            print(item['html_url'])


class PullRequests:
    bad_base = []
    drafts = []
    open_pulls = []

    def populate_pull_data(self, pulls):
        for pull in pulls:
            pull_list = self.open_pulls
            if (pull['base']['ref'] == 'main' or pull['base']['ref'] == 'master') and pull['head']['ref'] != 'develop':
                pull_list = self.bad_base
            elif pull['draft']:
                pull_list = self.drafts
            pull_list.append({'title': pull['title'],
                              'html_url': pull['html_url']})

    def get_pulls(self):
        load_dotenv()
        with open(os.environ['pulls_config_file'], 'r') as stream:
            orgs_with_repos = yaml.safe_load(stream)

        for org in orgs_with_repos['orgs']:
            for repo in org['repos']:
                pulls = get_data(org, repo)
                self.populate_pull_data(pulls)
        dump_data(self.bad_base, red('Bad base:'))
        dump_data(self.drafts, underline('Drafts:'))
        dump_data(self.open_pulls, underline('Open pulls:'))

        return self.bad_base, self.drafts, self.open_pulls


if __name__ == '__main__':
    pr = PullRequests()
    pr.get_pulls()
