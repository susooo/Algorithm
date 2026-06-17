import heapq

def solution(n, paths, gates, summits):
    
    graph = [[] for _ in range(n+1)]
    for i,j,w in paths:
        graph[i].append((j,w))
        graph[j].append((i,w))
        
    INF = float('inf')
    dist = [INF]*(n+1)
    
    hq = []
    for g in gates:
        heapq.heappush(hq, (0,g))
        dist[g] = 0
        
    summit_set = set(summits)
    while hq:
        intensity, node = heapq.heappop(hq)
        
        if intensity > dist[node]:
            continue
            
        if node in summits:
            continue
            
        for nx,w in graph[node]:
            new_intensity = max(intensity,w)
            
            if new_intensity < dist[nx]:
                dist[nx] = new_intensity
                heapq.heappush(hq, (new_intensity, nx))
                
    answer = min([(s, dist[s]) for s in summits], key=lambda x:(x[1],x[0]))
    
    return answer