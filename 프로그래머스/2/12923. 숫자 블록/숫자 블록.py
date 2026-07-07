def solution(begin, end):
    answer = []
    
    for num in range(begin, end+1):
        
        if num == 1:
            answer.append(0)
            continue
            
        block = 1
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                if num//i <= 10000000:
                    block = num//i
                    break
                
                block = i
                
        answer.append(block)
        
    return answer