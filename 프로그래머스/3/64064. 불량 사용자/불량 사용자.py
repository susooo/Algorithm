def solution(user_id, banned_id):
    
    def match(u, b):
        if len(u) != len(b): return False
        for i in range(len(u)):
            if b[i] == '*': continue
            if u[i] != b[i]: return False
        return True
    
    candidates = []
    for b in banned_id:
        tmp = []
        for u in user_id:
            if match(u,b):
                tmp.append(u)
        candidates.append(tmp)
        
    candidates.sort(key=len)
    used = set()
    result = set()

    def dfs(idx):
        if idx == len(candidates):
            result.add(frozenset(used))
            return
        
        for u in candidates[idx]:
            if u not in used:
                used.add(u)
                dfs(idx+1)
                used.remove(u)

    dfs(0)
    return len(result)