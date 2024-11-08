def func(n,k):
	global w,v,dp

	#base case
	if n==0 or k==0:
		return 0
	if dp[n][k] != -1:
		return dp[n][k]

	#recursive case
	dp[n][k] = func(n-1,k)
	if k-w[n] >= 0:
		dp[n][k] = max(dp[n][k], func(n-1,k-w[n])+v[n])

	return dp[n][k]

n,k = map(int,input().split())
w,v = [0],[0]

for _ in range(n):
	a,b = map(int,input().split())
	w.append(a)
	v.append(b)

dp = [[-1 for _ in range(k+1)] for _ in range(n+1)]
print(func(n,k))