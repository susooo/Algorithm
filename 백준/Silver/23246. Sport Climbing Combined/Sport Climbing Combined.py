n = int(input())
player = [tuple(map(int, input().split())) for _ in range(n)]

score = sorted(player, key=lambda x: (x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))

for idx in range(3):
	print(score[idx][0], end=" ")