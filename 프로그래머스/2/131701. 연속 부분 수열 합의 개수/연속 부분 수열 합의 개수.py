def solution(elements):
    len_ele = len(elements)
    new_ele = elements*2
    answer = set()
    
    for idx in range(1, len_ele+1):
        for i in range(0, len_ele):
            answer.add(sum(new_ele[i:i+idx]))
            
    return len(answer)