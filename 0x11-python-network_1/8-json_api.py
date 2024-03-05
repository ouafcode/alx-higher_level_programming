#!/usr/bin/python3
""" script that fetches URL """

if __name__ == "__main__":
    import requests
    import sys

    var = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": var}

    res = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = res.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
