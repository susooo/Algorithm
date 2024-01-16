from collections import Counter

def solution(topping):
    answer = 0
    chul = Counter(topping) 
    bro = set()
    
    for t in topping:
        chul[t] -= 1
        bro.add(t) 
        if chul[t] == 0:
            chul.pop(t)    
        if len(chul) == len(bro):
            answer += 1     
    return answer