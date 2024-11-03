def check(level):
	global answer, curr_sum, nums,n,s

	if level == n:
		if curr_sum == s:
			answer += 1
		return

	curr_sum += nums[level]
	check(level+1)
	curr_sum -= nums[level]

	check(level+1)

n,s = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
curr_sum = 0

check(0)
if s == 0:
    answer -= 1

print(answer)