from collections import defaultdict
import math

def calc_time(time):
    h, m = map(int, time.split(":"))
    return h*60+m
    
def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    last_in_time = dict()
    total_time = defaultdict(int)
    END_OF_DAY = calc_time("23:59")
    
    for record in records:
        time_str, carNum, order = record.split()
        time = calc_time(time_str)
        
        if order == "IN":
            last_in_time[carNum] = time
        else:
            total_time[carNum] += time - last_in_time.pop(carNum)
            
    #아직 안나간 차량
    for num, time in last_in_time.items():
        total_time[num] += END_OF_DAY-time
        
    #요금 계산하기
    def calc_fee(t):
        if t <= base_time:
            return base_fee
        return base_fee + math.ceil((t-base_time)/unit_time)*unit_fee
            
    answer = [ calc_fee(total_time[carNum]) for carNum in sorted(total_time, key=int)]
    
    return answer