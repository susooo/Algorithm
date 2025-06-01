#누적합 알고리즘
def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            max_val = 0
            if j > 0:
                max_val = triangle[i-1][j-1]
            if j < len(triangle[i-1]):
                max_val = max(max_val, triangle[i-1][j])
            triangle[i][j] += max_val
    
    return max(triangle[-1])