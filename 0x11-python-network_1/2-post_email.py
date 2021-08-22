#!/usr/bin/python3
"""
    Script that takes in a URL and an email,
    sends a POST request to the passed URL with the email
    as a parameter, and displays the body of the response
"""

from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({"email": email})
    data = data.encode("ascii")

    with request.urlopen(url, data) as response:
        content = response.read()
        print("{}".format(content.decode("utf-8")))
