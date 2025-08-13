def solution(lottos, win_nums):
    
    zero_cnt = lottos.count(0)
    lottos = set(lottos)
    dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    curr_cnt = 0
    for num in win_nums:
        if num in lottos:
            curr_cnt += 1
    
    return [dic[curr_cnt+zero_cnt], dic[curr_cnt]]
