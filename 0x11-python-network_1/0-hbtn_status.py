#!/usr/bin/python3
"""
    Script that fetches https://intranet.hbtn.io/status
"""

from urllib import request


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = request.Request(url)
    with request.urlopen(req) as response:
        content = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
