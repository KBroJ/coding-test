def this_is_d2(n):
    
    result = "unrated"

    if 'D2' in n.upper():
        result = "D2"

    return result

N = input()
print(this_is_d2(N))