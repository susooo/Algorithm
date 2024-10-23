def combi(answer, level, cnt):
	global list,C,Ctype
	if len(answer) == L and cnt>0 and cnt<=L-2:
		print("".join(answer))
		return

	for idx in range(level, C):
		answer.append(Ctype[idx])
		if Ctype[idx] in ['a', 'e', 'i', 'o', 'u']:
			combi(answer,idx+1, cnt+1)
		else:
			combi(answer,idx+1, cnt)
		answer.pop()

L,C = map(int,input().split())
Ctype = list(input().split())
Ctype.sort()
combi([],0,0)