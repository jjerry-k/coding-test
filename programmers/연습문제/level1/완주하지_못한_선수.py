def solution(participant, completion):
    temp = 0
    par_hash = [hash(par) for par in participant]
    com_hash = [hash(com) for com in completion]   
    return participant[par_hash.index(sum(par_hash)-sum(com_hash))]