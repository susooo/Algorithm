def solution(board, skill):
    
    r = len(board)
    c = len(board[0])
    dp = [[0]*(c+2) for _ in range(r+2)]
    
    for t,r1,c1,r2,c2,d in skill:
        if t==1: d = -d
        
        r1,r2,c1,c2 = r1+1, r2+1, c1+1, c2+1
        dp[r1][c1] += d
        dp[r2+1][c2+1] += d
        dp[r1][c2+1] -= d
        dp[r2+1][c1] -= d
        
    #누적합 만들기
    for i in range(1,r+1):
        for j in range(1, c+1):
            dp[i][j] += (dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1])
            
    #개수 세기
    answer = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] + dp[i+1][j+1] > 0:
                answer += 1
    return answer