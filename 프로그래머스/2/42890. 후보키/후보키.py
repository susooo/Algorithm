from itertools import combinations

def solution(relation):
    n, m = len(relation), len(relation[0])
    
    #유일성 만족하는 키 찾기
    temp = []
    for i in range(1, m+1):
        for comb in combinations(range(m), i):
            
            group = set()
            for row in relation:
                curr = tuple(row[col] for col in comb)
                group.add(curr)
            
            if len(group)==n:
                temp.append(comb)
    
    #최소성 만족하는 키 찾기(유일성 키 후보중에서)
    answer = []
    for cand in temp:
        cand = set(cand)
        flag = True
        
        for key in answer:
            if key.issubset(cand):
                flag = False
                break
        
        if flag:
            answer.append(cand)
        
    return len(answer)