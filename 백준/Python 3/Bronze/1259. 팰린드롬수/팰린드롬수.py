import sys
input = sys.stdin.readline

def method():

    while True:

        s = input().strip()

        if s == "0":
            break

        if s.lstrip("0") == s.lstrip("0")[::-1]:
            print("yes")
        else:
            print("no")

method()