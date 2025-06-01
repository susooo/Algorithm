def solution(arr):
    n = (len(arr)+1)//2
    
    min_arr = [[float('inf')]*n for _ in range(n)]
    max_arr = [[-float('inf')]*n for _ in range(n)]
    
    for x in range(n):
        min_arr[x][x] = max_arr[x][x] = int(arr[2*x])
        
    for d in range(1, n+1): #구간길이
        for i in range(n-d): #시작점 
            j = i+d #끝점
            
            for k in range(i,j): #중간점
                op = arr[2*k+1]
                if op == '+':
                    max_arr[i][j] = max(max_arr[i][j], max_arr[i][k] + max_arr[k+1][j])
                    min_arr[i][j] = min(min_arr[i][j], min_arr[i][k] + min_arr[k+1][j])
                else:
                    max_arr[i][j] = max(max_arr[i][j], max_arr[i][k] - min_arr[k+1][j])
                    min_arr[i][j] = min(min_arr[i][j], min_arr[i][k] - max_arr[k+1][j])

    return max_arr[0][n-1]