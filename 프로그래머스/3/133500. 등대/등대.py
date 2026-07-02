def solution(n, lighthouse):
    
    graph = [[] for _ in range(n+1)]
    for a,b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
    
    dp = [[0, 1] for _ in range(n + 1)]

    parent = [0] * (n + 1)
    order = []  # 방문 순서 저장

    visited = [False] * (n + 1)
    visited[1] = True
    stack = [1]

    while stack:
        node = stack.pop()
        order.append(node)
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                parent[child] = node
                stack.append(child)

    #역순으로 DP 처리 (리프 → 루트)
    for node in reversed(order):
        for child in graph[node]:
            if child == parent[node]:
                continue
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])

    return min(dp[1][0], dp[1][1])