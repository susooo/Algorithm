from itertools import permutations

n = int(input())
questions = [input().split() for _ in range(n)]
answer = 0

#모든 경우를 다 탐색 -> 브루트 포스
for curr in permutations(range(1,10),3):
	flag = True

	for num,strike,ball in questions:
		sn = bn = 0
		
		for i in range(3):
			if str(curr[i]) == num[i]:
				sn += 1
			elif str(curr[i]) in num:
				bn += 1

		if sn != int(strike) or bn != int(ball):
			flag = False
			break

	if flag:
		answer += 1

print(answer)