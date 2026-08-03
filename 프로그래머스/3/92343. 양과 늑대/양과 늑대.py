def solution(info, edges):
    answer = 0
    n = len(info)
    
    graph = [[] for _ in range(n)]
    for a,b in edges:
        graph[a].append(b)
        
    def dfs(mask, candidates):
        nonlocal answer
        sheep, wolf = 0,0
        
        for i in range(n):
            if mask & (1<<i):
                if info[i] == 0:
                    sheep+=1
                else:
                    wolf+=1
        
        if wolf >= sheep:
            return
        
        answer = max(answer, sheep)
        
        for node in candidates:
            new_mask = mask | (1<<node)
            
            new_candidates = candidates.copy()
            new_candidates.remove(node)
            
            for child in graph[node]:
                if not (new_mask & (1 << child)):
                    new_candidates.add(child)

            dfs(new_mask, new_candidates)

    dfs(1<<0, set(graph[0]))
    
    return answer