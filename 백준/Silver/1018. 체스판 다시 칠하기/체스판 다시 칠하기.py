#모든 경우를 확인하는 브루트 포스가 적절하다.

n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
answer = n*m

flag = "W"
for row in range(n-7):
	for col in range(m-7):
		cnt1,cnt2 = 0,0
		for i in range(row, row+8):
			for j in range(col, col+8):
				if arr[i][j] != flag:
					cnt1 += 1
				else:
					cnt2 += 1

				flag = "B" if flag == "W" else "W"

			flag = "B" if flag == "W" else "W"			
		if answer > cnt1:
			answer = cnt1
		if answer > cnt2:
			answer = cnt2

print(answer)