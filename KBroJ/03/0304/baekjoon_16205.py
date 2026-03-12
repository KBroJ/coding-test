'''
[변수명]_https://www.acmicpc.net/problem/16205
-----------------------------------------------------------------------
변수명을 정하는 표기법은 여러 가지가 있다.

카멜 표기법 (Camel Case): 각 단어의 첫 글자를 대문자로 적는다. 단, 가장 첫 글자는 소문자를 사용한다.
예시: camelCase, variableN, thisIsCamelCase, howToSolveThisProblem
스네이크 표기법 (Snake Case): 소문자만 사용하고, 각 단어의 사이에 언더바(_)를 넣어서 적는다.
예시: snake_case, variable_n, this_is_snake_case, how_to_solve_this_problem
파스칼 표기법 (Pascal Case): 카멜 표기법과 같지만, 가장 첫 글자도 대문자를 사용한다.
예시: PascalCase, VariableN, ThisIsPascalCase, HowToSolveThisProblem
한 표기법을 사용한 변수명이 주어졌을 때, 이를 다른 표기법으로 변환하는 프로그램을 작성하시오.
-----------------------------------------------------------------------
첫째 줄에 사용한 표기법의 번호와 변수명이 주어진다.
번호가 1인 경우는 카멜 표기법, 2인 경우는 스네이크 표기법, 3인 경우는 파스칼 표기법이다.

입력으로 주어지는 변수명의 길이는 100을 넘지 않는다.

카멜 표기법, 파스칼 표기법을 사용한 변수명은 알파벳 소문자와 대문자로만 이루어져 있고,
스네이크 표기법을 사용한 변수명은 알파벳 소문자와 언더바(_)로만 이루어져 있다.
또, 스네이크 표기법을 사용한 변수명의 첫 글자와 마지막 글자는 언더바가 아니고, 언더바가 연속해서 두 개 이상 사용하는 경우는 없다.
-----------------------------------------------------------------------
예제 입력
    2 variable_n
예제 출력
    variableN
    variable_n
    VariableN

========================================================================================================================
생각하기
    1 : variableN 카멜
    2 : variable_n 스네이크
    3 : VariableN 파스칼

    공백 기준으로 입력받기

'''
import sys
input = sys.stdin.readline

def method():

    n, string = input().split()
    n = int(n)

    words = []
    current = ""

    if n == 1:
        for ch in string:
            if ch.isupper():
                words.append(current.lower())
                current = ch
            else:
                current += ch
        words.append(current.lower())
    elif n == 2:
        words = string.split('_')
    elif n == 3:
        current = string[0]
        for ch in string[1:]:
            if ch.isupper():
                words.append(current.lower())
                current = ch
            else:
                current += ch
        words.append(current.lower())

    camelCase = words[0] + "".join(w.capitalize() for w in words[1:])
    snakeCase = "_".join(words)
    pascalCase = "".join(w.capitalize() for w in words)

    print(camelCase)
    print(snakeCase)
    print(pascalCase)

method()
# ========================================================================================================================
'''
정리

[알고리즘]
    문자열 파싱 / 변환
    - 입력 표기법을 단어 리스트로 분해한 뒤, 3가지 표기법으로 재조립

[풀이 방법]
    1단계: 표기법에 따라 words(단어 리스트)로 분해
        카멜/파스칼 → 대문자를 단어 구분자로 사용, 문자를 순회하며 분리
        스네이크     → split('_') 으로 바로 분리

    2단계: words로 3가지 표기법 조립 (공통)
        camelCase  = words[0] + "".join(w.capitalize() for w in words[1:])
        snakeCase  = "_".join(words)
        pascalCase = "".join(w.capitalize() for w in words)

[이상적인 풀이]
    현재 풀이가 가장 깔끔한 형태
    카멜/파스칼 분해 로직이 동일하므로 함수로 뽑으면 더 간결해짐:
        def split_by_upper(s):
            words, current = [], s[0]
            for ch in s[1:]:
                if ch.isupper():
                    words.append(current.lower())
                    current = ch
                else:
                    current += ch
            words.append(current.lower())
            return words

[어려웠던 부분 1] 대문자 기준으로 단어 분리
    문자를 하나씩 순회하면서 대문자가 나오면 지금까지 쌓인 current를 저장하고 새 단어 시작
        if ch.isupper():
            words.append(current.lower())  # 현재까지 쌓인 단어 저장
            current = ch                   # 새 단어 시작
        else:
            current += ch
    루프 끝나고 마지막 current도 반드시 저장해야 함

[어려웠던 부분 2] 파스칼 첫 글자 문제
    PascalCase는 첫 글자도 대문자 → 루프 처음에 current=""인 상태에서 대문자 만나면
    words에 빈 문자열 "" 이 들어가는 버그 발생
    → current = string[0] 으로 초기화하고 string[1:] 부터 순회해야 함

[어려웠던 부분 3] snakeCase 조립
    words[0] + "_" + words[1] 로 하면 단어가 3개 이상일 때 나머지가 잘림
    → "_".join(words) 사용해야 함

'''