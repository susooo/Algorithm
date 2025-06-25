from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    visited = [[False]*m for _ in range(n)]
    dxy = [(0,1),(1,0),(0,-1),(-1,0)]
    
    #땅 위치 판별
    def in_range(x,y):
        return 0<=x<n and 0<=y<m
    
    #석유 덩어리 추출
    oil_grid = [[-1]*m for _ in range(n)]
    oil_sizes = dict()
    oil_num = 0
    for i in range(n):
        for j in range(m):
            if not land[i][j] or visited[i][j]:
                continue
            
            q = deque()
            q.append((i,j))
            visited[i][j] = True
            oil_grid[i][j] = oil_num
            size = 1
            
            while q:
                x,y = q.popleft()
                for dx,dy in dxy:
                    nx,ny = x+dx, y+dy
                    if in_range(nx,ny) and land[nx][ny] and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx,ny))
                        size += 1
                        oil_grid[nx][ny] = oil_num
            
            oil_sizes[oil_num] = size
            oil_num += 1
            
    #열마다 포함된 덩어리
    answer = 0
    for col in range(m):
        check = set()
        curr = 0
        for row in range(n):
            num = oil_grid[row][col]
            if num != -1 and num not in check:
                check.add(num)
                curr += oil_sizes[num]
                
        answer = max(answer, curr)
    
    return answer