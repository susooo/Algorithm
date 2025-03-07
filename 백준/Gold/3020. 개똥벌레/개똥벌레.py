n,h = map(int, input().split())
top = [0]*(h+1)
bot = [0]*(h+1)

for idx in range(n):
	num = int(input())

	if idx%2 == 0:
		bot[num] += 1
	else:
		top[h-num+1] += 1

mn = n
answer = 0

cnt = n//2
for hgt in range(1,h+1):

	cnt -= bot[hgt-1]
	cnt += top[hgt]

	if cnt == mn:
		answer += 1

	if cnt < mn:
		mn = cnt
		answer = 1

print(mn, answer)