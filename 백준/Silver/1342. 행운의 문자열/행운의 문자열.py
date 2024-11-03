def func(lev):
	global s, chars, cnt, choose, ans

	#base code
	if lev == len(s):
		ans += 1
		return

	#recursive case
	for c in chars:
		if cnt[c] == 0:
			continue

		if (not choose) or (choose[-1] != c):
			cnt[c] -= 1
			choose.append(c)
			func(lev+1)
			cnt[c] += 1
			choose.pop()

s = input()
chars = set()
cnt = dict()

for c in s:
	chars.add(c)
	if c not in cnt:
		cnt[c] = 0
	cnt[c] += 1

choose = []
ans = 0

func(0)
print(ans)