from collections import deque

def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    dxy = [(-1,0), (1,0), (0,-1), (0,1)]
    
    #물류창고
    board = [["*"]*(m+2)]
    for i in range(n):
        board.append(["*"]+list(storage[i])+["*"])
    board.append(["*"]*(m+2))
    
    def in_range(x,y):
        return 0<=x<=n+1 and 0<=y<=m+1
    
    #지게차 출고
    def one(char):
        q = deque()
        visited = [[False]*(m+2) for _ in range(n+2)]
        
        for i in range(n+2):
            for j in range(m+2):
                if i==0 or i==n+1 or j==0 or j==m+1:
                    q.append((i,j))
                    visited[i][j] = True
                    
        while q:
            x,y = q.popleft()
            for dx,dy in dxy:
                nx,ny = x+dx, y+dy
                
                if in_range(nx,ny) and not visited[nx][ny]:
                    if board[nx][ny]=="*":
                        q.append((nx,ny))
                    if board[nx][ny]==char:
                        board[nx][ny] = "*"
                    visited[nx][ny] = True
                         
    #크레인 출고
    def two(char):
        for i in range(n+2):
            for j in range(m+2):
                if board[i][j] == char:
                    board[i][j] = "*"
        
    for r in requests:
        if len(r) == 1:
            one(r)
        else:
            two(r[0])
    
    answer = 0
    for i in range(n+2):
        for j in range(m+2):
            if board[i][j] != "*":
                answer += 1
    
    return answer