import heapq

def solution(book_time):
    
    def time_to_min(time):
        return int(time[:2])*60 + int(time[3:])
    
    book_time.sort()
    room = []
    for a,b in book_time:
        start, end = time_to_min(a), time_to_min(b)
        
        if not room:
            heapq.heappush(room, end+10)
        else:
            last = heapq.heappop(room)
            if start < last:
                heapq.heappush(room, last)
            heapq.heappush(room, end+10)

    return len(room)