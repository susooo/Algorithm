def solution(matrix_sizes):
    
    n = len(matrix_sizes)
    
    matrix = [matrix_sizes[0][0]]
    for i in range(n):
        matrix.append(matrix_sizes[i][1])
    
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2,n+1):
        for i in range(n-length+1):
            j = i+length-1
            
            dp[i][j] = float('inf') #dp[i][j] = i번째 행렬부터 j번째 행렬까지 곱한 최소 비용
            
            for k in range(i,j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i]*matrix[k+1]*matrix[j+1])
    
    return dp[0][n-1]