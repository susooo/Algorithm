def solution(m, n, puddles):
    MOD = 1000000007
    grid = [[0]*(m+1) for _ in range(n+1)]
    
    for x,y in puddles:
        grid[y][x] = -1
    
    grid[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if grid[i][j] == -1:
                grid[i][j] = 0
                continue
                
            if i > 1:
                grid[i][j] += grid[i-1][j]
            if j > 1:
                grid[i][j] += grid[i][j-1]
                
    return grid[n][m] % MOD