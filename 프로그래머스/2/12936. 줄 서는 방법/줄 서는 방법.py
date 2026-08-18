def solution(n, k):
    
    answer = []
    nums = list(range(1, n+1))
    
    cnt = 1
    for i in range(1, len(nums)):
        cnt *= i
    
    while nums:
        cnt = 1
        for i in range(1, len(nums)):
            cnt *= i
        
        idx = (k-1)//cnt
        answer.append(nums.pop(idx))
        
        k = (k-1)%cnt + 1
    
    return answer