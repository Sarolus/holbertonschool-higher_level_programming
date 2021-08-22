#!/usr/bin/python3
"""
    Script that takes in a URL,
    sends a request to the URL and
    displays the body of the response
"""

from urllib import request, error
from sys import argv


if __name__ == "__main__":

    try:
        with request.urlopen(argv[1]) as response:
            content = response.read()
            print(content.decode("utf-8"))
    except error.HTTPError as error:
        print("Error code: {}".format(error.code))
