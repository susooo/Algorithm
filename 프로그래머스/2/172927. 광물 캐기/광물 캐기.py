def solution(picks, minerals):
    board = [[1,1,1],[5,1,1],[25,5,1]]
    m_idx = {'diamond':0,'iron':1,'stone':2}
    
    max_cnt = sum(picks)*5
    minerals = minerals[:max_cnt]
    groups = [minerals[i:i+5] for i in range(0,len(minerals),5)]
    
    score_info = {'diamond':25, 'iron':5, 'stone':1}
    group_info = []
    for g in groups:
        score = sum(score_info[m] for m in g)
        group_info.append((score, g))
    group_info.sort(key=lambda x:x[0], reverse=True)
    
    answer = 0
    idx = 0
    for i,p in enumerate(picks):
        for _ in range(p):
            if idx >= len(group_info):
                break
                
            _, group = group_info[idx]
            
            for mineral in group:
                answer += board[i][m_idx[mineral]]
            idx+=1
        
    return answer
        
        