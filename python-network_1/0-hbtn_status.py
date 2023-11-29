#!/usr/bin/python3
"""
Fetches https://alu-intranet.hbtn.io/status
"""

import urllib.request

url = "https://alu-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read()
    utf8_content = content.decode('utf-8')
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
