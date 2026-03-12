'''
[대전과학고등학교를 사랑하십니까?]_https://www.acmicpc.net/problem/34691
-----------------------------------------------------------------------
DSHStack의 참가자라면, 학교를 사랑하는 마음은 아는 것에서부터 시작되지 않을까요?

학교의 상징을 물어보는 질문이 주어졌을 때, 해당 상징의 학명을 정답으로 출력해 보자.

질문 animal의 정답은 학교의 상징 동물인 호랑이이다.
    호랑이의 학명은 Panthera tigris 이다.
질문 tree의 정답은 학교의 상징 나무인 소나무이다.
    소나무의 학명은 Pinus densiflora 이다.
질문 flower의 정답은 학교의 상징 꽃인 개나리이다.
    개나리의 학명은 Forsythia koreana 이다.
-----------------------------------------------------------------------
첫째 줄부터 한 줄에 하나씩 문자열이 주어진다.

입력되는 문자열은 animal, tree, flower, end 중 하나이며,
end는 입력의 마지막 줄에만 항상 주어진다.
end는 질문이 아니며, 처리하지 않는다.

질문은 1회 이상 주어지며, 1,000회 이상 주어지지 않는다.
-----------------------------------------------------------------------
예제 입력
    animal
    flower
    tree
    end
예제 출력
    Panthera tigris
    Forsythia koreana
    Pinus densiflora
========================================================================================================================
'''
# 방법1
def answer_scientific_name(string):

    answer = ""

    if string == "animal":
        answer = "Panthera tigris"
    elif string == "flower":
        answer = "Forsythia koreana"
    elif string == "tree":
        answer = "Pinus densiflora"

    return answer

while True:
    S = input()
    if S == "end":
        break
    print(answer_scientific_name(S))

# ========================================================================================================================
# 방법2
# 딕셔너리: key-value 쌍으로 매핑
answers = {
  "animal": "Panthera tigris",
  "flower": "Forsythia koreana",
  "tree":   "Pinus densiflora"
}

print("방법2 시작")
while True:
    S = input()
    if S == "end":
        break
    print(answers.get(S, "등록되지 않는 질문"))