def solution(scores):

    target = scores[0]
    scores.sort(key=lambda x: (-x[0],x[1]))
    
    filters = []
    max_b = 0
    for a,b in scores:
        if b < max_b:
            continue
        filters.append([a,b])
        max_b = max(b, max_b)
    
    if target not in filters:
        return -1
    
    filters.sort(key=lambda x: -(x[0]+x[1]))
    
    answer = 0
    curr = sum(filters[0])
    cnt = 0
    for a,b in filters:
            
        if a+b == curr:
            cnt += 1
        else:
            curr = a+b
            answer += cnt
            cnt = 1
        
        if (a,b) == (target[0], target[1]):
            return answer + 1