import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2:
        s1 = heapq.heappop(scoville)
        if s1 >= K:
            return answer
        s2 = heapq.heappop(scoville)
        new = s1 + s2*2   
        heapq.heappush(scoville, new)
        answer += 1
               
    if len(scoville) == 1:
        if heapq.heappop(scoville) < K:
            return -1
    return answer