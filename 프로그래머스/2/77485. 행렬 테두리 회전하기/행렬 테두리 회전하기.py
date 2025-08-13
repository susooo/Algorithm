def solution(rows, columns, queries):
    answer = []
    
    board = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
    x=0
    for i in range(1,rows+1):
        for j in range(1, columns+1):
            x+=1
            board[i][j] = x
            
    for curr in queries:
        x1,y1,x2,y2 = curr
        tmp = board[x1][y1]
        min_ans = tmp
        #아래->위
        for i in range(x1+1, x2+1):
            board[i-1][y1] = board[i][y1]
            min_ans = min(min_ans, board[i][y1])
        #오->왼
        for i in range(y1+1, y2+1):
            board[x2][i-1] = board[x2][i]
            min_ans = min(min_ans, board[x2][i])
        #위->아래
        for i in range(x2-1,x1-1,-1):
            board[i+1][y2] = board[i][y2]
            min_ans = min(min_ans, board[i][y2])
        #왼->오
        for i in range(y2-1,y1-1,-1):
            board[x1][i+1] = board[x1][i]
            min_ans = min(min_ans, board[x1][i])
        
        board[x1][y1+1] = tmp
        answer.append(min_ans)
        
    return answer