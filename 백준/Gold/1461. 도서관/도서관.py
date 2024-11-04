n,m = map(int, input().split())
arr = list(map(int, input().split()))

pos = []
neg = []
for x in arr:
	if x > 0:
		pos.append(x)
	else:
		neg.append(-x)

pos = sorted(pos)[::-1]
neg = sorted(neg)[::-1]

dists = []

for p in pos[::m]:
	dists.append(p)

for n in neg[::m]:
	dists.append(n)

print(2*sum(dists) - max(dists))