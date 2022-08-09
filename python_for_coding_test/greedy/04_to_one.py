def solve():
    N, K = map(int, input().split())

    result = 0

    while 1:
        rem = N % K
        N = N//K if rem == 0 else N-1

        result += 1

        if N==1:
            break
    print(result)

solve()