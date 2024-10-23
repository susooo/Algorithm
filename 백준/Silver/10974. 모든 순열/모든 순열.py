def permutation():
	global answer,check, n
	if len(answer) == n:
		print(" ".join(answer))

	for idx in range(1,n+1):
		if check[idx]:
			continue
		answer.append(str(idx))
		check[idx] = True
		permutation()
		answer.pop()
		check[idx] = False

n = int(input())
check = [False]*(n+1)
answer = []
permutation()