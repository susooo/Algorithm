def solution(info, edges):
    answer = 0
    
    graph = [[] for _ in range(len(info))]
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
        
    def dfs(available, sheep, wolf):
        nonlocal answer
        
        if wolf >= sheep:
            return
        
        answer = max(answer, sheep)

        for node in list(available):
            for nx in graph[node]:
                if nx not in available:
                    if info[nx]==0:
                        dfs(available|{nx}, sheep+1, wolf)
                    else:
                        dfs(available|{nx}, sheep, wolf+1)
                    
    dfs(set([(0)]), 1, 0)
    return answer