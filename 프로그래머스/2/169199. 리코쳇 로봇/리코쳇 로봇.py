from collections import deque

def solution(board):
    
    n,m = len(board), len(board[0])
    dxy = [(0,1),(1,0),(0,-1),(-1,0)]
    visited = [[False]*m for _ in range(n)]
    
    #시작점 찾기
    flag = False
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i,j)
                flag = True
                break
        if flag:
            break
    
    def in_range(x,y):
        return 0<=x<n and 0<=y<m
    
    dq = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True

    while dq:
        x,y,cnt = dq.popleft()
        
        if board[x][y] == 'G':
            return cnt
        
        for dx, dy in dxy:
            nx, ny = x, y

            # 벽이나 범위를 벗어날 때까지 미끄러짐
            while True:
                tx = nx + dx
                ty = ny + dy
            
                if not in_range(tx,ty):
                    break
                    
                if board[tx][ty] == 'D':
                    break
                    
                nx,ny = tx,ty
                
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx,ny,cnt+1))

    return -1