from collections import deque

def solution(m, n, h, w, drops):

    board = [[float('inf')] * n for _ in range(m)]
    for i, (x, y) in enumerate(drops, 1):
        board[x][y] = i
    
    def sliding_min(arr,k):
        dq = deque() #윈도우 밖인지 확인하기 위해 인덱스 저장
        result = []
        
        for i in range(len(arr)):
            #윈도우 밖이면 제거
            while dq and dq[0] <= i-k:
                dq.popleft()
            
            #나보다 이전에 큰 값 제거
            while dq and arr[dq[-1]] >= arr[i]:
                dq.pop()
            
            dq.append(i)
        
            if i >= k-1:
                result.append(arr[dq[0]])
                
        return result
       
    #슬라이딩 윈도우로 가로 크기 줄이기
    horizontal = []
    for row in range(m):
        horizontal.append(sliding_min(board[row][:], w))
    
    #슬라이딩 윈도우로 세로 크기 줄이기
    vertical = []
    for col in zip(*horizontal):
        vertical.append(sliding_min(col[:],h))
    windows = list(zip(*vertical))
    
    #가장 늦게 비 맞는 배치의 왼쪽 위 자표 구하기
    answer = []
    max_num = 0
    for row in range(len(windows)):
        for col in range(len(windows[0])):
            if windows[row][col] > max_num:
                max_num = windows[row][col]
                answer = [row, col]
        
    return answer