import sys
input = sys.stdin.readline

def find_cheater():

    T = int(input())

    for i in range(T):
        n = int(input())
        beforeCard = sorted(list(map(str, input().split())))
        afterCard = sorted(list(map(str, input().split())))

        if beforeCard != afterCard:
            print("CHEATER")
        else:
            print("NOT CHEATER")


find_cheater()