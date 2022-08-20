def solve():
    data = input()
    result = []
    int_val, int_cnt = 0, 0

    for x in data:
        if x.isalpha():
            result.append(x)
        else:
            int_cnt += 1
            int_val += int(x)
    result.sort()

    if int_cnt != 0:
        result.append(str(int_val))

    print(''.join(result))

solve()