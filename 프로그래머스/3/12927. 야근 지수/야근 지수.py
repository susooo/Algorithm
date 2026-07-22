def solution(n, works):
    
    if sum(works) <= n:
        return 0
    
    #평균값 찾기
    left,right = 0, max(works)
    while left < right:
        mid = (left+right)//2
        
        need = 0
        for w in works:
            if w > mid:
                need += w-mid
            
        if need > n:
            left = mid + 1
        else:
            right = mid
            
    level = left
    remain = n
    
    #평균값까지 작업량 줄이기
    works.sort(reverse=True)
    for i in range(len(works)):
        if works[i] > level:
            remain -= works[i]-level
            works[i] = level
        else:
            break
            
    #남은 시간 재분배
    for i in range(len(works)):
        if remain == 0:
            break
            
        works[i] -= 1
        remain -= 1
        
    return sum(w**2 for w in works)