from itertools import product

def solution(clockHands):
    answer = float('inf')
    n = len(clockHands)
    first = [0]*n
    dxy = [(0,0),(0,1),(1,0),(0,-1),(-1,0)]
    
    def in_range(x,y):
        return 0<=x<n and 0<=y<n
    
    def press(board, x, y, cnt):
        for dx,dy in dxy:
            nx,ny = x+dx, y+dy
            if in_range(nx,ny):
                board[nx][ny] = (board[nx][ny] + cnt)%4
    
    def simulate(first):
        board = [row[:] for row in clockHands]
        total = 0
        
        #첫번째 행
        for col in range(n):
            if first[col]:
                press(board, 0, col, first[col])
                total += first[col]
                
        #두번째 행부터
        for row in range(1,n):
            for col in range(n):
                need = (4-board[row-1][col])%4
                
                if need:
                    press(board, row, col, need)
                    total += need
        #마지막 행
        if all(board[n-1][col] == 0 for col in range(n)):
            return total
        
        return float('inf')
        
        
    for row in product(range(4), repeat=n):
        answer = min(answer, simulate(row))

    return answer