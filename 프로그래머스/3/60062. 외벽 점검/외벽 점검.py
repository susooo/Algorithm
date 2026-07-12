from itertools import permutations

def solution(n, weak, dist):
    
    w = len(weak)
    weak_line = weak + [n+x for x in weak]
    dist.sort(reverse=True)
    
    for cnt in range(1, len(dist)+1):
        for perm in permutations(dist, cnt):
            for start in range(w):
                idx = start
                for d in perm:
                    reach = weak_line[idx] + d 
                    
                    while idx < start+w and weak_line[idx] <= reach:
                        idx += 1
                        
                    if idx >= start+w: #취약점 모두 포함
                        return cnt
    return -1