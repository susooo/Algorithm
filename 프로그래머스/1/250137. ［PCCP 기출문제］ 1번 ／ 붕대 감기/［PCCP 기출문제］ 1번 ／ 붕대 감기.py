def solution(bandage, health, attacks):
    t,x,y = bandage
    
    curr = health
    for a in range(len(attacks)-1):
        at,ad = attacks[a]
        curr -= ad
        if curr <= 0: return -1
        
        nt,nd = attacks[a+1]
        curr = curr + (nt-at-1)*x + (nt-at-1)//t*y
        curr = min(health, curr)
    
    if curr - attacks[-1][1] <= 0:
        return -1
    return curr - attacks[-1][1]