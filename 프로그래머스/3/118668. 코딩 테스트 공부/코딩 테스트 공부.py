def solution(alp, cop, problems):
    answer = 0
    
    max_alp = max(problem[0] for problem in problems)
    max_cop = max(problem[1] for problem in problems)
    
    if alp >= max_alp and cop >= max_cop:
        return 0
    
    #out of range 고려
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    dp = [[float('inf')]*(max_cop+1) for _ in range(max_alp+1)]
    dp[alp][cop] = 0
    
    for a in range(alp, max_alp+1):
        for c in range(cop, max_cop+1):
            
            #알고력 공부
            if a + 1 <= max_alp:
                dp[a+1][c] = min(dp[a+1][c], dp[a][c]+1)
            #코딩력 공부
            if c + 1 <= max_cop:
                dp[a][c+1] = min(dp[a][c+1], dp[a][c]+1)
                
            #문제 풀기
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    na = min(max_alp, a+alp_rwd)
                    nc = min(max_cop, c+cop_rwd)
                    
                    dp[na][nc] = min(dp[na][nc], dp[a][c]+cost)
            
    return dp[max_alp][max_cop]