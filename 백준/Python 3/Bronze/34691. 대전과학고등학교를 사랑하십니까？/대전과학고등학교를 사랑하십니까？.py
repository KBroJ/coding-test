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
    S=input()
    if S == "end":
        break
    print(answer_scientific_name(S))