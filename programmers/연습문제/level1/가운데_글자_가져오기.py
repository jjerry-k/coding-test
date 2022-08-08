def solution(s):
    center_idx = len(s)//2
    return s[center_idx] if len(s)%2==1 else s[center_idx-1:center_idx+1]