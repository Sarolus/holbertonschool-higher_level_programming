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
        parameter = argv[1]
    except:
        parameter = ""

    url = "http://0.0.0.0:5000/search_user"
    value = {'q': parameter}
    response = requests.post(url=url, data=value)

    try:
        content = response.json()
        if "id" in json:
            print("[{}] {}".format(content.get("id"), content.get("name")))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
