n = int(input())
points = [list(map(int,input().split())) for i in range(n)]

points.sort()

for idx in range(n):
	print(points[idx][0], points[idx][1])