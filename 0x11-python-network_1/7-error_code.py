#!/usr/bin/python3
""" script that fetches URL """

if __name__ == "__main__":
    import requests
    import sys

    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
