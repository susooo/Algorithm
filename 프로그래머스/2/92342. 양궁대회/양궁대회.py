def solution(n, info):
    answer = [-1]
    diff = 0
    
    def tracking(used_arrow, idx, ryan):
        nonlocal answer, diff
        
        if idx==11:
            apeach_score, ryan_score = 0,0
            temp_ryan = ryan[:]
            temp_ryan[10] += n-used_arrow
            
            for i in range(11):
                #둘다 0발 맞힌 경우
                if info[i] == 0 and temp_ryan[i] == 0:
                    continue
                    
                if info[i] >= temp_ryan[i]:
                    apeach_score += 10-i
                else:
                    ryan_score += 10-i
            
            if apeach_score >= ryan_score: #어피치가 이긴 경우
                return
            
            if ryan_score - apeach_score > diff:
                diff = ryan_score - apeach_score
                answer = temp_ryan[:]
            elif ryan_score - apeach_score == diff: #점수차가 같은 경우
                for j in range(10,-1,-1):
                    if temp_ryan[j] > answer[j]:
                        answer = temp_ryan[:]
                        break
                    elif temp_ryan[j] < answer[j]:
                        break
            return
        
        tracking(used_arrow, idx+1, ryan)
        
        curr_used = used_arrow + info[idx] + 1
        if curr_used <= n:
            ryan[idx] += info[idx]+1
            tracking(curr_used, idx+1, ryan)
            ryan[idx] = 0
            
    tracking(0, 0, [0]*11)
    
    return answer