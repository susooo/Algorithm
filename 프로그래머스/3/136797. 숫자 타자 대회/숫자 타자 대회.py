from collections import defaultdict
import heapq

def solution(numbers):
    
    pos = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        0:(3,1)
          }
    
    phone = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [-1,0,-1]
    ]
    
    # 이동 (dx, dy, 비용)
    moves = [
        (0,0,1),
        (0,1,2),
        (1,0,2),
        (0,-1,2),
        (-1,0,2),
        (1,1,3),
        (1,-1,3),
        (-1,1,3),
        (-1,-1,3)
    ]
    
    def in_range(x,y):
        return 0<=x<4 and 0<=y<3
    
    def dijkstra(start):
        sx, sy = pos[start]
        
        pq = [(0,sx,sy)]
        visited = [[False]*3 for _ in range(4)]
        
        while pq:
            cost,x,y = heapq.heappop(pq)
            
            if visited[x][y]:
                continue
                
            visited[x][y] = True
            
            num = phone[x][y]
            if num != -1:
                dist[start][num] = cost
                
            
            for dx,dy,w in moves:
                nx,ny = x+dx, y+dy
                
                if in_range(nx,ny) and not visited[nx][ny]:
                    heapq.heappush(pq,(cost+w, nx,ny))
            
            
    dist = [[0]*10 for _ in range(10)]    
    for i in range(10):
        dijkstra(i)
        dist[i][i] = 1
    
    dp = defaultdict(lambda: float('inf'))
    dp[(4, 6)] = 0
    
    for num in numbers:
        target = int(num)
        next_dp = defaultdict(lambda: float('inf'))
        
        for (left, right), cost in dp.items():
            if left == target:
                next_dp[(left, right)] = min(next_dp[(left, right)], cost + dist[left][target])
                continue
            if right == target:
                next_dp[(left, right)] = min(next_dp[(left, right)], cost + dist[right][target])
                continue
            
            # 왼손으로 누르기
            next_dp[(target, right)] = min(next_dp[(target, right)], cost + dist[left][target])
            # 오른손으로 누르기
            next_dp[(left, target)] = min(next_dp[(left, target)], cost + dist[right][target])
        
        dp = next_dp
    
    return min(dp.values())