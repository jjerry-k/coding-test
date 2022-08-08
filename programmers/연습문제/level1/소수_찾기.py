def solution(n):
    if n < 2: return 0
    primes = set(range(2, n+1))
    for i in range(2, n+1):
        if i in primes:
            primes -= set(range(2*i, n+1, i))
    return len(primes)