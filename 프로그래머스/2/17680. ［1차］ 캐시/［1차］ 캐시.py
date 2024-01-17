from collections import deque

def solution(cacheSize, cities):
    dq = deque(maxlen=cacheSize)
    time = 0
    for city in cities:
        city = city.lower()
        if city not in dq:
            dq.append(city)
            time += 5
        else:
            dq.remove(city)
            dq.append(city)
            time += 1

    return time