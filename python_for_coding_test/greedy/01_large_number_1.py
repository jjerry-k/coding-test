def solve1(): 

    N, M, K = map(int, input().split(" "))
    
    data = list(map(int, input().split(" ")))
    data.sort()

    result = 0

    first_cnt = 0
    first_num = data[N-1]
    
    second_num = data[N-2]
    
    for _ in range(M):
        if first_cnt == K:
            first_cnt = 0
            result += second_num
        else:
            result += first_num
            first_cnt += 1
    print(result)

solve1()


def solve2(): 

    N, M, K = map(int, input().split(" "))
    
    data = list(map(int, input().split(" ")))
    data.sort()

    result = 0

    first_num = data[N-1]
    second_num = data[N-2]

    bundle, cnt = divmod(M, K+1)

    result += bundle*((first_num*K)+second_num)
    result += cnt*first_num
    print(result)

solve2()
