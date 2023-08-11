#!/usr/bin/python3
if __name__ == "__main__":
     import hidden_4
     av = dir(hidden_4)
     for i in range(len(av)):
         if (av[i][:2] != "__"):
             print(av[i])
