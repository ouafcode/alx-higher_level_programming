#!/usr/bin/python3
""" script that fetches URL """

if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.headers["X-Request-Id"])
