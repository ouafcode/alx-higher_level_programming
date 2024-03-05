#!/usr/bin/python3
""" script that fetches URL """

if __name__ == "__main__":
    import requests
    import sys

    try:
        response = requests.get(sys.argv[1])
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error code:", e)
