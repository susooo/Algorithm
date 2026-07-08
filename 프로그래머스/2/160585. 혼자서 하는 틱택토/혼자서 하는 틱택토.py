def solution(board):

    o_cnt, x_cnt = 0,0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                x_cnt += 1
            elif board[i][j] == 'O':
                o_cnt += 1
    
    def win(ch):
        # 행
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == ch:
                return True
        # 열
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] == ch:
                return True
        # 대각선
        if board[0][0] == board[1][1] == board[2][2] == ch:
            return True
        if board[0][2] == board[1][1] == board[2][0] == ch:
            return True

        return False

    if o_cnt < x_cnt or o_cnt > x_cnt+1:
        return 0
    
    o_win = win('O')
    x_win = win('X')
    
    if o_win and x_win: #둘다 이김
        return 0
    if o_win and o_cnt != x_cnt + 1: #O가 이김
        return 0
    if x_win and o_cnt != x_cnt: #X가 이김
        return 0
    
    return 1