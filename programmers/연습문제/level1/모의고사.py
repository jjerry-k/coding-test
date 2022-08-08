def solution(answers):
    answer = [0, 0, 0]
    first_student = [1, 2, 3, 4 ,5]
    second_student = [2, 1, 2, 3, 2, 4, 2, 5]
    third_student = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for idx, a in enumerate(answers):
        if a==first_student[idx%len(first_student)]:
            answer[0] += 1
        if a==second_student[idx%len(second_student)]:
            answer[1] += 1
        if a==third_student[idx%len(third_student)]:
            answer[2] += 1
            
    return [i + 1 for i, v in enumerate(answer) if v == max(answer)]