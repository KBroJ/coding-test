import sys
input = sys.stdin.readline

def method():

    T = int(input())

    for i in range(T):
        S = input().strip() # .strip() : 줄바꿈(/n) 제거
        R = S[::-1]    # 역순정렬

        max_overlap = 0
        for a in range(1, len(S) + 1):
            if S.endswith(R[:a]):
                max_overlap = a

        X = S + R[max_overlap:]
        print(X)
method()