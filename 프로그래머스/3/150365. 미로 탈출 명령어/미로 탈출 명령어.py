def solution(n, m, x, y, r, c, k):
    
    def in_range(xx,yy):
        return 0<=xx<n and 0<=yy<m
    
    def can_move(xx,yy,path):
        remain = k-path
        dist = abs(r-xx) + abs(c-yy)
        
        if remain < dist: #남은 이동횟수보다 가야할 횟수가 더 큰 경우
            return False
        
        if (remain-dist)%2 != 0: #짝수여야 탈출지점 도착 시, 다른 위치 갔다가 다시 올 수 있음
            return False
        
        return True    
    
    answer = ''
    xx,yy,r,c = x-1,y-1,r-1,c-1
    dxy = {'d':(1,0), 'l':(0,-1), 'r':(0,1), 'u':(-1,0)}
    moved = False
    
    for dist in range(k+1):
        
        if xx==r and yy==c and dist==k:
            return answer

        for d,(dx,dy) in dxy.items():
            nx,ny = xx+dx, yy+dy
            
            if not in_range(nx,ny):
                continue
                
            if not can_move(nx,ny,dist+1):
                continue

            answer += d
            xx,yy = nx,ny
            moved = True
            break
            
        if not moved:
            return 'impossible'