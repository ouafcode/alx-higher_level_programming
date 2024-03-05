#!/usr/bin/python3
""" script that fetches URL """

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    response = requests.post(url, data)
    print(response.text)
