#!/usr/bin/env python3
from client import GithubOrgClient


git = GithubOrgClient('google')
print(git.org)
