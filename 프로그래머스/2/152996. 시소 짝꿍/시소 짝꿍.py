from collections import Counter
import math

def solution(weights):
    counter = Counter(weights)
    answer = 0

    for w, cnt in counter.items():
        # 같은 무게
        answer += cnt * (cnt - 1) // 2

        # 다른 무게
        if w * 2 in counter:
            answer += cnt * counter[w * 2]

        if w * 3 % 2 == 0 and w * 3 // 2 in counter:
            answer += cnt * counter[w * 3 // 2]

        if w * 4 % 3 == 0 and w * 4 // 3 in counter:
            answer += cnt * counter[w * 4 // 3]

    return answer