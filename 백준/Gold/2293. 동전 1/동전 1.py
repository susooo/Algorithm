n, k = map(int, input().split())
values = []
for _ in range(n):
    values.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for value in values:
    for i in range(value, k+1):
        dp[i] = dp[i] + dp[i-value]

print(dp[k])