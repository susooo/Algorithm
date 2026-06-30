import heapq

def solution(n, k, enemy):
    answer = 0
    curr_sum = 0
    hq = []
    
    if len(enemy) <= k:
        return len(enemy)
    
    for idx in range(len(enemy)):
        d = enemy[idx]
        heapq.heappush(hq, d)
        
        if len(hq) > k:
            a = heapq.heappop(hq)
            curr_sum += a
            
        answer = idx    
        if curr_sum > n:
            break
            
    if curr_sum <= n:
        answer += 1
    return answer