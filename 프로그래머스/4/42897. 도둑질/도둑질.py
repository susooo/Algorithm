def solution(money):
    
    def func(curr):
        dp = [[0,0] for _ in range(len(money))]
    
        for i in range(1, len(money)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + curr[i-1]
        
        return max(dp[-1][0], dp[-1][1])
        
    case1 = func(money[:-1])
    case2 = func(money[1:])

    return max(case1, case2)