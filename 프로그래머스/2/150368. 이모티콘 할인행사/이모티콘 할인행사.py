from itertools import product

def solution(users, emoticons):
    answer = [0,0]
    n = len(emoticons)
    dic = {10:0.9, 20:0.8, 30:0.7, 40:0.6}

    for comb in product(range(10,50,10), repeat=n):
        cnt = 0
        total = 0
        
        for p, limit in users:
            curr = 0
            for i in range(n):
                if p <= comb[i]:
                    curr += emoticons[i]*dic[comb[i]]
        
            if curr >= limit:
                cnt += 1
            else:
                total += curr
                
        if answer[0] < cnt:
            answer = [cnt, total]
        elif answer[0] == cnt and answer[1] < total:
            answer = [cnt, total]
            
    return answer