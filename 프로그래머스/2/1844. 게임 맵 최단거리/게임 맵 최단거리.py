from collections import deque

def solution(maps):
    
    n,m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    dxy = [(0,1),(1,0),(0,-1),(-1,0)]
    
    def in_range(x,y):
        return 0<=x<n and 0<=y<m
    
    dq = deque()
    dq.append((0,0,1))
    visited[0][0] = True
    
    answer = float('inf')
    while dq:
        x,y,cnt = dq.popleft()
        
        if x==n-1 and y==m-1:
            answer = min(answer, cnt)
            
        for dx,dy in dxy:
            nx,ny = x+dx, y+dy
            
            if in_range(nx,ny) and maps[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx,ny,cnt+1))
            
    return answer if answer != float('inf') else -1
        
        
        
        