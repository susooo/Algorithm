def solution(priorities, location):
    answer = 0
    p = list(enumerate(priorities))
    print(p)
    while True:
        index, value = p.pop(0)
        if any(value < other_value for _, other_value in p):
            p.append((index, value))
        else:
            answer += 1
            if index == location:
                return answer