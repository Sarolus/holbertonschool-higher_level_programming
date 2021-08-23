#!/usr/bin/python3
"""
    Script that takes your GitHub credentials
    (username and password) and uses the GitHub
    API to display your id
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = argv[1]
    password = argv[2]

    response = requests.get(url=url, auth=(user, password))
    content = response.json()
    print(content.get('id'))
