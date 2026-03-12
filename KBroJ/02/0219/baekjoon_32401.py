'''
[ANA는 회문이야]_https://www.acmicpc.net/problem/32401

민용이는 ANA의 광신도라서 방학에도 하루 종일 동아리방에서 공부한다. 민용이가 ANA를 좋아하는 이유는 ANA라는 문자열이 회문이기 때문이다.
회문이란 앞에서부터 읽으나 뒤에서부터 읽으나 똑같은 문자열을 의미한다.
민용이는 ANA라는 문자열을 너무 좋아한 나머지 유사 ANA 문자열이라는 것을 다음과 같이 정의했다.

    유사 ANA 문자열은 영어 대문자로 이루어진 길이가 3이상인 문자열이다.
    유사 ANA 문자열은 영어 대문자 A로 시작해서 A로 끝나며, 문자열의 다른 위치에서 A가 등장하지 않는다.
    유사 ANA 문자열은 영어 대문자 N을 한 개만 포함한다.

예를 들어 ARENA, AGENDA는 유사 ANA 문자열이다.
하지만 ANACONDA는 그렇지 않다. A를 세 개 포함하고 있고, N도 두 개 포함하고 있기 때문이다.

민용이는 어떤 문자열S가 유사 ANA 문자열이 아닐 수도 있는 것에 슬퍼했다.
그래서 민용이는S의 부분 문자열 중에서 유사 ANA 문자열을 찾으려고 한다.
문자열S가 주어질 때, S의 부분 문자열 중에 유사 ANA 문자열이 몇 개인지 구해보자.

========================================================================================================================

입력받은 문자열에서 A와A 사이에 N이 한묶음으로 되어있는 개수 찾기
    문자열 앞부터 시작하여 첫 A찾기
    첫A 기준으로 다음 A까지 진행 + N의 개수 기억
  => 2차 생각
    A 쌍의 위치를 기억 > 그 사이범위에 N의 개수 1개 판별 > ANA 문자열 개수 +1
'''
def find_ana_string(string):

    ana_number = 0

    for i in range(len(string)):

        end_a_index = -1
        n_number = 0

        # 첫 A 인덱스 찾기(start_a_index)
        if string[i] == 'A':
            start_a_index = i

            # 쌍이 되는 A 인덱스 찾기(end_a_index)
            for j in range(i + 1, len(string)):
                if string[j] == 'A':
                    end_a_index = j
                    break

            if end_a_index != -1:
                # A쌍 안에서 N의 개수 구하기
                for k in range(start_a_index, end_a_index + 1):

                    if string[k] == 'N':
                        n_number = n_number + 1

                # N의 개수가 1이면 ANA 문자열이므로 개수 +1
                if n_number == 1:
                    ana_number += 1

    return ana_number


result = find_ana_string
print("정답 = 2 현재 풀이 값 =", result("ANACONDA"))
print("정답 = 1 현재 풀이 값 =", result("ARENA"))
print("정답 = 1 현재 풀이 값 =", result("AGENDA"))
print("정답 = 5 현재 풀이 값 =", result("ANEDUCATEDMINDCANANALYZEANDADAPTTOCHANGE"))