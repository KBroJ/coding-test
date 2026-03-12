import sys
input = sys.stdin.readline

def method():

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = 0

    # 선 비교
    if A == B:
        result = 1
        return print(result)

    for last in range(N - 1, 0, -1):
        max_idx = 0

        for j in range(1, last + 1):  # 최댓값 인덱스 찾기
            if A[j] > A[max_idx]:
                max_idx = j

        if last != max_idx:  # 한 번만 교환
            A[last], A[max_idx] = A[max_idx], A[last]

        if A == B:
            result = 1
            break

    return print(result)

method()