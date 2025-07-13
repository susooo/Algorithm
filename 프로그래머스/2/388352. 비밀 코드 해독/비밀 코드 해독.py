from itertools import combinations

def solution(n, q, ans):
    m = len(q)
    avail = set(range(1, n+1))

    for idx in range(m):
        if ans[idx]==0:
            for num in q[idx]:
                avail.discard(num)
    
    answer = 0
    for comb in combinations(avail,5):
        flag = True
        for i in range(m):
            cnt = sum(1 for x in q[i] if x in comb)
            if cnt != ans[i]:
                flag = False
                break
                
        if flag:
            answer += 1
    
    return answer    