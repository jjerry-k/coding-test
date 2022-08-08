def solution(arr):
    answer = [arr[0]]
    for elem in arr[1:]:
        if elem == answer[-1]:continue
        answer.append(elem)
    return answer