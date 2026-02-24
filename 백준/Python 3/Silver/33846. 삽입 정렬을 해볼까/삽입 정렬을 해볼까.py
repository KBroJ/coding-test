import sys

def insertion_sort(n, t):

    # 2번째 입력값 배열 저장 : 3 1 4 1 5 9 2 6 5 3 5
    # arr = list(map(int, input().split()))
    arr = list(map(int, sys.stdin.readline().split()))

    '''
    # 선택정렬 방식(앞->뒤)
    for i in range(0, t):
        for j in range(i+1, t):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    '''

    '''
    # 삽입정렬 방식(뒤->앞) - [시간초과]
    for i in range(1, t):
        for j in range(i, 0, -1):

            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

    return arr
    '''

    # sorted() 사용
    return sorted(arr[:t])+arr[t:]

# 1번째 입력값
# n, t = map(int, input().split())
n, t = map(int, sys.stdin.readline().split())
print(*insertion_sort(n, t))