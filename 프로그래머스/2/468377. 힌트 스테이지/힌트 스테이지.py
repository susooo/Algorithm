def solution(cost, hint):
    
    n = len(cost) #n개의 스테이지
    best = float('inf')
    
    for mask in range(1<<(n-1)): #각 비트 : 힌트 번들 구매 여부 확인 (완전탐색)
        tickets = [0]*n
        total = 0
        
        #힌트 번들 구매
        for i in range(n-1):
            if mask & (1<<i): #힌트 번들 구매 확인
                total += hint[i][0]
                for t in hint[i][1:]: #힌트 개수 세기
                    tickets[t-1] += 1
                    
        #힌트권 다 사용하여 스테이지 해결 비용 합산하기
        for i in range(n):
            j = min(tickets[i], n-1)
            total += cost[i][j]
            
        best = min(best, total)
            
    return best