#!/usr/bin/python3
""" script that fetches URL """

if __name__ == "__main__":
    import requests
    import sys

    response = requests.get(sys.argv[1])
    print(response.headers['X-Request-Id'])
