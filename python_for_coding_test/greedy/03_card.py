def solve1():
    N, M = map(int, input().split())

    result = 0
    for _ in range(N):
        rows = list(map(int, input().split()))
        min_val = min(rows)
        if min_val > result:
            result = min_val
    print(result)

solve1()