#!/usr/bin/python3
"""
    Script that takes in a letter and sends
    a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter
"""

import requests
from sys import argv


if __name__ == "__main__":

    try:
        argument = argv[1]
    except:
        argument = ""

    url = "http://0.0.0.0:5000/search_user"
    value = {'q': argument}
    response = requests.post(url=url, data=value)

    try:
        content = response.json()
        if 'id' in content:
            print("[{}] {}".format(content['id'], content['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
