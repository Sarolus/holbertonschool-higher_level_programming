#!/usr/bin/python3
"""
    Script that lists 10 commits of
    the given repository and owner.
"""

import requests
from sys import argv


if __name__ == "__main__":
    repository = argv[1]
    user = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        user, repository
    )
    parameters = 'per_page'

    response = requests.get(url)
    content = response.json()

    for commit in content:
        print(
            "{}: {}".format(
                commit.get("sha"),
                commit.get("commit").get("author").get("name")
            )
        )
