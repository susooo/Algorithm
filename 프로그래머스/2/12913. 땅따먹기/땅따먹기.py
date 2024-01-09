def solution(land):
    n = len(land)
    m = len(land[0])

    dp = [[0] * m for _ in range(n)]
    for i in range(m):
        dp[0][i] = land[0][i]

    for i in range(1, n):
        for j in range(m):
            for k in range(m):
                if j != k:
                    dp[i][j] = max(dp[i][j], land[i][j] + dp[i-1][k])

    return max(dp[-1])