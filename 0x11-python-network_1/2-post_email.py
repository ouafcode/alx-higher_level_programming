#!/usr/bin/python3
""" script that fetches URL """

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
