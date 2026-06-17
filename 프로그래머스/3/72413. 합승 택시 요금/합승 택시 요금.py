import heapq

def solution(n, s, a, b, fares):
    
    graph = [[] for _ in range(n+1)]
    for c,d,f in fares:
        graph[c].append((d,f))
        graph[d].append((c,f))
    
    def dijkstra(start, end):
        INF = float('inf')
        dist = [INF]*(n+1)
        dist[start] = 0
        hq = []
        heapq.heappush(hq, (0,start))
        
        while hq:
            cost, node = heapq.heappop(hq)
            
            if dist[node] < cost:
                continue
                
            for next_node, next_cost in graph[node]:
                total = cost + next_cost
                if dist[next_node] > total:
                    dist[next_node] = total
                    heapq.heappush(hq, (total, next_node))
                    
        return dist[end]
    
    answer = float('inf')
    for t in range(1,n+1):
        total = dijkstra(s,t) + dijkstra(t,a) + dijkstra(t,b)
        answer = min(answer, total)
        
    return answer