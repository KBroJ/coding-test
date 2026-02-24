def fibonacci_number(n):

    # 배열선언
    f_array = [0]*(n+1)
    f_array[0] = 0
    f_array[1] = 1

    # 2번째 인덱스부터 배열저장 시작 시작
    for i in range(2, n+1):
        f_array[i] = f_array[i-1] + f_array[i-2]

    return f_array[n]

# result = fibonacci_number
# print("정답 = 55 현재 풀이 값 =", result(10))

N = int(input())
print(fibonacci_number(N))