import sys
input = sys.stdin.readline

def calc(x, op, y):
    if op == '+': return x + y
    elif op == '-': return x - y
    elif op == '*': return x * y
    elif op == '/':
        if x * y > 0:               # 두 수의 부호가 같으면 (양수*양수, 음수*음수) → 결과 양수
            return x // y           # // : 정수 나눗셈 (Java의 /와 동일, 소수점 버림)
        elif x * y < 0:             # 두 수의 부호가 다르면 → 결과 음수
            return -(abs(x) // abs(y))  # abs()로 절댓값 나눗셈 후 음수 부호 붙이기
        else:                       # x == 0 이면 결과는 항상 0 (0 / 어떤수 = 0)
            return 0

def four_operation():
    # 입력
    a, b, c, d, e = map(str, input().split())
    a, c, e = int(a), int(c), int(e)

    result1 = calc(calc(a, b, c), d, e)
    result2 = calc(a, b, calc(c, d, e))

    if result1 < result2:
        print(result1)
        print(result2)
    else:
        print(result2)
        print(result1)


# 입력
four_operation()