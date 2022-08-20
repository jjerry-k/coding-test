def solve():
    raw = input()
    x = ord(raw[0]) - ord("a") + 1
    y = int(raw[1])

    conds = [
                    (-2, -1), (-2, 1), (2, -1), (2, 1),
                    (-1, -2), (-1, 2), (1, -2), (1, 2)
                    ]

    cnt = 0
    for cond in conds:
        tmp_x = x + cond[0]
        tmp_y = y + cond[1]
        if tmp_x >= 1 and tmp_x <= 8 and tmp_y >= 1 and tmp_y <= 8:
            cnt += 1
    
    print(cnt)

solve()