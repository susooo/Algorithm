def solution(k, d):
    
    def dist(x):
        return int((d**2 - x**2)**0.5)//k +1
    
    answer = 0
    for i in range(0,d+1,k):
        answer += dist(i)
        
    return answer