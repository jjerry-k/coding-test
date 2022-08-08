def solution(s):
    s = s.split(" ")
    for i, word in enumerate(s):
        tmp = ""
        for j, elem in enumerate(word.lower()):
            elem = elem.upper() if j%2==0 else elem
            tmp += elem
        s[i] = tmp
    return " ".join(s)