def solution(m, n, startX, startY, balls):
    answer = []
    
    def dist(x, y): #유클리드 거리
        return (startX - x) ** 2 + (startY - y) ** 2

    for a,b in balls:
        min_dist = float('inf')
        
        #목표 공 4면 대칭하기 - 목표 공이 시작 공과 벽 사이에 있는 경우 제외
        #왼쪽 벽
        if not (startY == b and startX > a):
            min_dist = min(min_dist, dist(-a, b))
            
        #오른쪽 벽
        if not (startY == b and startX < a):
            min_dist = min(min_dist, dist(2*m-a, b))
        
        #아래쪽 벽
        if not (startX == a and startY > b):
            min_dist = min(min_dist, dist(a, -b))

        #위쪽 벽
        if not (startX == a and startY < b):
            min_dist = min(min_dist, dist(a, 2*n-b))
            
        answer.append(min_dist)
    return answer