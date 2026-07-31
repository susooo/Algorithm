def solution(relation):
    
    col = len(relation[0])
    candidates = []
    
    for mask in range(1, 1<<col):
        #유일성 체크
        items = set()
        for row in relation:
            key = tuple(row[i] for i in range(col) if mask & (1<<i))
            items.add(key)
    
        if len(items) != len(relation):
            continue
            
        #최소성 체크
        is_minimal = True
        for ck in candidates:
            if (mask&ck) == ck: #부분집합
                is_minimal = False
                break
            
        if is_minimal:
            candidates.append(mask)
            
    return len(candidates)