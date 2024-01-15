def solution(N, number):
    dp = [set() for i in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        for j in range(i//2 + 1):
            for n in dp[j]:
                for m in dp[i-j]:
                    dp[i].add(n+m)
                    dp[i].add(n-m)
                    dp[i].add(m-n)
                    dp[i].add(n*m)
                    if m != 0 :
                        dp[i].add(n//m)
                    if n != 0 :
                        dp[i].add(m//n)
                    
        if number in dp[i]:
            return i
    return -1