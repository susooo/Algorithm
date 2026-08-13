def solution(n, s):
    answer = []
    
    if s//n == 0:
        return [-1]
    
    curr = s
    cnt = n
    while curr > 0:
        if cnt == 1:
            answer.append(curr)
            break
            
        mod = curr//cnt
        answer.append(mod)
        curr -= mod
        cnt -= 1
    
    return answer