def solution(n, k, cmd):
    #이중 연결 리스트
    
    prev = [i-1 for i in range(n)]
    next = [i+1 for i in range(n)]
    next[n-1] = -1
    
    deleted = []
    curr = k
    answer = ["O"]*n
    for c in cmd:
        if c[0] == "U":
            x = int(c[2:])
            for _ in range(x):
                curr = prev[curr]
        elif c[0] == "D":
            x = int(c[2:])
            for _ in range(x):
                curr = next[curr]
        elif c[0] == "C":
            answer[curr] = "X"
            deleted += [curr]
            #연결 끊기 
            if prev[curr] != -1:
                next[prev[curr]] = next[curr]
            if next[curr] != -1:
                prev[next[curr]] = prev[curr]
                
            #커서 이동
            curr = next[curr] if next[curr] != -1 else prev[curr]
            
        elif c[0] == "Z":
            restore = deleted.pop()
            answer[restore] = "O"
            
            #연결 복구
            if prev[restore] != -1:
                next[prev[restore]] = restore
            if next[restore] != -1:
                prev[next[restore]] = restore
            
    return "".join(answer)