from collections import deque

def solution(n, roads, sources, destination):
    
    graph = [[] for _ in range(n+1)]
    for s,e in roads:
        graph[s].append(e)
        graph[e].append(s)
        
    dist = [-1] * (n + 1)
    dist[destination] = 0
    dq = deque([destination])
    
    while dq:
        node = dq.popleft()
        for nx in graph[node]:
            if dist[nx] == -1:
                dist[nx] = dist[node] + 1
                dq.append(nx)
    
    answer = []
    for s in sources:
        answer += [dist[s]]
    return answer