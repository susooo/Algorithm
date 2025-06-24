def is_possible(level, diffs, times, limit):
    total = times[0]
    for i in range(1, len(diffs)):
        if diffs[i] <= level:
            total += times[i]
        else:
            total += (diffs[i] - level) * (times[i] + times[i - 1]) + times[i]
            
        if total > limit:
            return False
    return True

def solution(diffs, times, limit):
    low = 1
    high = max(diffs)
    answer = high
    
    while low <= high:
        mid = (low + high) // 2
        if is_possible(mid, diffs, times, limit):
            answer = mid #현재 가능한 최소 level 업데이트
            high = mid - 1
        else:
            low = mid + 1
            
    return answer