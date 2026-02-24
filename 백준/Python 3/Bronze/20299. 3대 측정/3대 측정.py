import sys
input = sys.stdin.readline

def major_measurements(N, K, L):

    teamCnt = 0
    result = []

    for i in range(N):
        # 2번째 입력값
        x1, x2, x3 = map(int, input().split())

        if x1 >= L and x2 >= L and x3 >= L:
            if (x1+x2+x3) >= K:
                # result.append(x1)
                # result.append(x2)
                # result.append(x3)
                result.extend([x1, x2, x3])
                teamCnt += 1

    print(teamCnt)
    
    # print(*result)
    print(' '.join(map(str, result))) # * 말고 이걸 사용하는걸 권장

    return result

# 1번째 입력값
N, K, L = map(int, input().split())
major_measurements(N, K, L)