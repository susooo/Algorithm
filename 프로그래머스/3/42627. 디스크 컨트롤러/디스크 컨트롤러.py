import heapq

def solution(jobs):
    
    jobs.sort()
    heap = []
    
    curr = 0
    total = 0
    i = 0
    cnt = 0
    
    while cnt < len(jobs):
        while i < len(jobs) and jobs[i][0] <= curr:
            request_time, duration = jobs[i]
            heapq.heappush(heap, (duration, request_time))
            i += 1
            
        if heap:
            duration, request_time = heapq.heappop(heap)
            curr += duration
            total += (curr- request_time)
            cnt += 1
        else:
            curr = jobs[i][0]
                
    return total//len(jobs)