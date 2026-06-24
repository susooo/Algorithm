from collections import deque

def solution(land):
    
    n,m = len(land), len(land[0])
    dxy = [(0,1),(1,0),(0,-1),(-1,0)]
    
    board = [[-1]*m for _ in range(n)]
    oil_cnt = dict()
    
    def in_range(x,y):
        return 0<=x<n and 0<=y<m
    
    def bfs(i,j,cnt):
        nonlocal num
        dq = deque([(i,j)])
        
        while dq:
            x,y = dq.popleft()
            
            for dx,dy in dxy:
                nx,ny = x+dx, y+dy
                
                if in_range(nx,ny) and land[nx][ny] == 1 and board[nx][ny] == -1:
                    board[nx][ny] = num
                    cnt += 1
                    dq.append((nx,ny))
                    
        oil_cnt[num] = cnt
        
    num = 1
    for i in range(n):
        for j in range(m):
            if land[i][j]==0 or board[i][j] != -1:
                continue
            board[i][j] = num
            bfs(i,j,1)
            num += 1
            
    answer = 0   
    for j in range(m):
        oil_group = {board[i][j] for i in range(n) if board[i][j] != -1}
        answer = max(answer, sum(oil_cnt[k] for k in oil_group))
        
    return answer