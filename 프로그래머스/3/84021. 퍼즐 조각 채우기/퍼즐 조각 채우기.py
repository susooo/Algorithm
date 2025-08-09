from collections import deque

#normalize
def normal(group):
    min_x = min(x for x,y in group)
    min_y = min(y for x,y in group)    
    return sorted((x-min_x, y-min_y) for x,y in group)
    
#rotation
def rotat(piece):
    return normal([(y,-x) for x,y in piece])
    
def solution(game_board, table):
    n = len(game_board)
    dxy = [(0,1),(1,0),(0,-1),(-1,0)]
    
    def in_range(x,y):
        return 0<=x<n and 0<=y<n
    
    #퍼즐 모양: 1개~6개 조각
    def bfs_find(x, y, target, board):
        q = deque([(x,y)])
        visited[x][y] = True
        group = [(x,y)]

        while q:
            xx,yy = q.popleft()

            for dx,dy in dxy:
                nx,ny = xx+dx, yy+dy

                if in_range(nx,ny) and not visited[nx][ny] and board[nx][ny]==target:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    group.append((nx,ny))

        return normal(group)

    #퍼즐 조각 찾기
    visited = [[False]*n for _ in range(n)]
    pieces = []
    for i in range(n):
        for j in range(n):
            if table[i][j]==1 and not visited[i][j]:
                pieces.append(bfs_find(i,j,1,table))
            
    #게임보드에 두기
    visited = [[False]*n for _ in range(n)]
    blanks = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j]==0 and not visited[i][j]:
                blanks.append(bfs_find(i,j,0,game_board))
    
    answer = 0
    used = [False]*len(pieces)
    for blank in blanks:
        for idx, piece in enumerate(pieces):
            if used[idx]:
                continue
            tmp = piece[:]
            match = False
            for _ in range(4):
                if tmp == blank:
                    used[idx] = True
                    answer += len(piece)
                    match = True
                    break
                tmp = rotat(tmp)
            if match:
                break
    return answer