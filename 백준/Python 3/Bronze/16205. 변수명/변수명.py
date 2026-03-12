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