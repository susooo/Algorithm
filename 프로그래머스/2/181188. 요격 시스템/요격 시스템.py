def solution(targets):
    #그리디
    targets.sort(key=lambda x:x[1])
    
    cnt = 0
    curr = -1
    for s,e in targets:
        if not (s < curr < e):
            curr = e - 0.5
            cnt += 1
            
    return cnt