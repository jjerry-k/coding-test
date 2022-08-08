def solution(s):
    sign = {"+":1, "-":-1}
    return int(s) if s.isdigit() else sign[s[0]]*int(s[1:])