def solution(play_time, adv_time, logs):
    
    def to_sec(time):
        return int(time[:2])*3600 + int(time[3:5])*60 + int(time[6:])
    
    def to_time(sec):
        h = sec // 3600
        m = (sec % 3600) // 60
        s = sec % 60
        return f"{h:02d}:{m:02d}:{s:02d}"
    
    sec_play_time = to_sec(play_time)
    sec_adv_time = to_sec(adv_time)
    time_tables = [0]*(sec_play_time+2)
    
    for log in logs:
        s, e = log.split('-')
        start, end = to_sec(s), to_sec(e)
        
        time_tables[start] += 1
        time_tables[end] -= 1 
        
    #누적합 - 현재 시청자 수
    for i in range(1,sec_play_time+1):
        time_tables[i] += time_tables[i-1]
        
    #누적합 - 누적 시간
    for i in range(1, sec_play_time+1):
        time_tables[i] += time_tables[i-1]
    
    answer = 0
    max_time = time_tables[sec_adv_time-1]
    #슬라이딩 윈도우
    for start_time in range(1, sec_play_time-sec_adv_time+1):
        end_time = start_time+sec_adv_time-1
        curr_sum = time_tables[end_time] - time_tables[start_time-1]
        if curr_sum > max_time:
            max_time = curr_sum
            answer = start_time
        
    return to_time(answer)