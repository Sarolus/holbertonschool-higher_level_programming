#!/usr/bin/python3
"""
    Script that takes in a URL,
    sends a request to the URL and
    displays the body of the response
"""

import requests
from sys import argv


if __name__ == "__main__":
    try:
        response = requests.get(argv[1])
        response.raise_for_status()
        content = response.content
        print("{}".format(content.decode("utf-8")))
    except requests.exceptions.HTTPError as exception:
        print("Error code: {}".format(exception.response.status_code))
