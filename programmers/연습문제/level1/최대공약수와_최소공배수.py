def solution(n, m):
    answer = []
    large_val = m if m > n else n
    
    i = large_val
    while 1 < large_val:
        if (n%i == 0) and (m%i == 0):
            answer = [i, n*m /i]
            break
        i -= 1
    return answer