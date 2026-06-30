def solution(storey):
    answer = 0
    
    curr_storey = storey
    while curr_storey > 0:
        mod = curr_storey % 10
        curr_storey //= 10
        
        if mod < 5:
            answer += mod
        elif mod == 5:
            nxt_mod = curr_storey%10
            answer += mod
            
            if nxt_mod >= 5:
                curr_storey += 1
        else:
            answer += 10 - mod
            curr_storey += 1
    return answer