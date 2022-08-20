def solve1(): 

    N = int(input())
    A = input().split(" ")
    
    x, y = 1, 1

    diff = { "R": [1, 0], "L": [-1, 0], "U": [0, -1], "D": [0, 1]}

    for direction in A:
        tmp_x = x + diff[direction][0]
        tmp_y = y + diff[direction][1]
        
        if tmp_x < 1 or tmp_y < 1 or tmp_x > N or tmp_y > N: 
            continue
        x, y = tmp_x, tmp_y
    print(x, y)

solve1()