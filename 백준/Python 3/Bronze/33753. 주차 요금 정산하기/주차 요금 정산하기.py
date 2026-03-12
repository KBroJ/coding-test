import math
import sys
input = sys.stdin.readline

def method():

    # 기본요금, 초과 요금 기준시간, 추가요금
    default_fee, extra_fee_time, extra_cost = map(int, input().split())
    #  차량의 주차 시간
    parking_time = int(input())

    #  30분 이하 기본요금
    result = default_fee

    # 30분 초과 시 초과요금 추가
    if parking_time > 30:
        over_time = parking_time - 30
        cost_time = math.ceil(over_time / extra_fee_time)

        result += extra_cost * cost_time

    return print(result)

method()