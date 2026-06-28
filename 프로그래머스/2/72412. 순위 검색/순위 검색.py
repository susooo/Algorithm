from collections import defaultdict
from itertools import combinations

def solution(info, query):
    
    db = defaultdict(list)
    for line in info:
        arr = line.split()
        conds = arr[:-1]
        score = int(arr[-1])
        
        for i in range(5):
            for comb in combinations(range(4),i):
                temp = conds[:]
                for idx in comb:
                    temp[idx] = '-'
                key = ''.join(temp)
                db[key].append(score)
                
    for key in db:
        db[key].sort()
    
    def lower_bound(arr, target):
        left, right = 0, len(arr)
        
        while left < right:
            mid = (left+right)//2
            
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    
    answer = []    
    for q in query:
        arr = q.replace(' and ', ' ').split()
        score = int(arr[-1])
        key = ''.join(arr[:-1])
        
        if key in db:
            scores = db[key]
            answer.append(len(scores) - lower_bound(scores, score))
        else:
            answer.append(0)
    return answer