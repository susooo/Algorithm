import heapq

def solution(n, works):

    if sum(works) <= n:
        return 0

    # 최대 힙
    heap = [-w for w in works]
    heapq.heapify(heap)

    while n:
        x = -heapq.heappop(heap)   # 가장 큰 작업

        x -= 1                     # 1시간 작업

        heapq.heappush(heap, -x)

        n -= 1

    return sum(x * x for x in map(lambda x: -x, heap))