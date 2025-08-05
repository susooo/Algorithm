from collections import defaultdict
import heapq

def dijkstra(n, start, graph):
    INF = float('inf')
    dist = [INF]*(n+1)
    dist[start] = 0
    hq = [(0, start)]
    
    while hq:
        cost, node = heapq.heappop(hq)
        if dist[node] < cost:
            continue
        for next_node, next_cost in graph[node]:
            total = cost + next_cost
            if dist[next_node] > total:
                dist[next_node] = total
                heapq.heappush(hq,(total, next_node))  
    return dist
    
def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for u,v, cost in fares:
        graph[u].append((v,cost))
        graph[v].append((u,cost))
        
    dist_s = dijkstra(n,s,graph)
    dist_a = dijkstra(n,a,graph)
    dist_b = dijkstra(n,b,graph)
    
    answer = float('inf')
    for t in range(1, n+1):
        total = dist_s[t] + dist_a[t] + dist_b[t]
        answer = min(answer, total)
        
    return answer