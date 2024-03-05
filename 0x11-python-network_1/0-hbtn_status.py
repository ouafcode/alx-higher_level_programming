#!/usr/bin/python3
""" script that fetches URL """

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        obj = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(obj)))
        print('\t- content: {}'.format(obj))
        print('\t- utf8 content: {}'.format(obj.decode("utf-8", "replace")))
