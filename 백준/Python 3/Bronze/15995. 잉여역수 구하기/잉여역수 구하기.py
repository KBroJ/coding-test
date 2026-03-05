import sys
input = sys.stdin.readline

def method():

    a, m = map(int, input().split())

    a_star = 1
    while True:
        if (a * a_star) % m == 1:
            print(a_star)
            break
        a_star += 1

method()