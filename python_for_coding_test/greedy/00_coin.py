def solve():
    C = 0
    COIN_LIST = [500, 100, 50, 10]
    N = int(input())
    for coin in COIN_LIST:
        tmp_c, N = divmod(N, coin)
        C += tmp_c
    print(C)

solve()