def solution(n):
    answer = 0
    
    def dfs(x,y,curr):
        nonlocal answer
        
        if y > x:
            return
            
        if x==n or y==n:
            answer += 1
            return
            
        dfs(x+1,y, curr+'(')
        dfs(x,y+1, curr+')')
    
    dfs(1,0,'(')
    return answer