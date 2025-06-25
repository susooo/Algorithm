from collections import defaultdict

def solution(points, routes):
    
    def get_path(p1, p2):
        r1,c1 = p1
        r2,c2 = p2
        path = []
        
        dr = 1 if r2 >= r1 else -1
        for r in range(r1,r2,dr):
            path.append([r,c1])
            
        dc = 1 if c2 >= c1 else -1
        for c in range(c1,c2, dc):
            path.append([r2,c])
        
        return path
    
    positions = defaultdict(int)
    for route in routes:
        path = []
        for i in range(len(route)-1):
            currP = points[route[i]-1]
            nextP = points[route[i+1]-1]
            path += get_path(currP,nextP)
    
        path.append(nextP)
        for t, (r,c) in enumerate(path):
            positions[(t,r,c)] += 1
    
    answer = 0
    for (t,r,c),cnt in positions.items():
        if cnt >= 2:
            answer += 1
   
    return answer