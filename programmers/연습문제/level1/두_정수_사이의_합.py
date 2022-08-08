def solution(a, b):
    return sum(range(a, b+1) if b >= a else range(b, a+1))