def solution(numbers):
    s = list(map(str,numbers))
    answer = sorted(s,key=lambda x: x*3,reverse=True)
    return str(int(''.join(answer)))
    