def solution(n, times):
    
    def can_do(x):
        cnt = 0
        for t in times:
            cnt += x//t
            
        return cnt >= n
    
    answer = 0
    left, right = 0, max(times)*n
    while left <= right:
        mid = (left+right)//2
        
        if can_do(mid):
            right = mid-1
            answer = mid
        else:
            left = mid+1
    return answer