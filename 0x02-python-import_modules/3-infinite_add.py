#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    argv = sys.argv
    res = 0

    for i in range(1, argv):
        res = res + argv[i]

    print(res)
