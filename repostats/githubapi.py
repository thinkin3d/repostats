import json
import re
import requests


class GitHubAPI(object):

    base_url = 'https://api.github.com/repos'
    user_str = None
    repo_str = None
    repo_url = None
    repo_data = {}

    def __init__(self, *args, **kwargs):
        m = re.search('https://github\.com/(?P<user>.*)/(?P<repo>.*)', kwargs.pop('repo', ''))
        self.user_str = m.group('user')
        self.repo_str = m.group('repo')
        self.repo_url = '%s/%s/%s' % (self.base_url, self.user_str, self.repo_str)

    def repo_name(self):
        return '%s/%s' % (self.user_str, self.repo_str)

    def exists(self):
        r = requests.get(self.repo_url)
        if r.ok:
            return True
        else:
            return False

    def load_repo(self):
        r = requests.get(self.repo_url)
        self.repo_data = json.loads(r.text or r.content)

    def stargazers_count(self):
        if not self.repo_data:
            self.load_repo()
        return self.repo_data.get('stargazers_count', None)

    def watchers_count(self):
        if not self.repo_data:
            self.load_repo()
        return self.repo_data.get('subscribers_count', None)

    def forks_count(self):
        if not self.repo_data:
            self.load_repo()
        return self.repo_data.get('forks_count', None)
