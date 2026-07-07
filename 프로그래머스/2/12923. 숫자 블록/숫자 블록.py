def solution(begin, end):
    answer = [0] * (end - begin + 1)

    LIMIT = 10000000

    for d in range(1, LIMIT + 1):

        # begin 이상인 첫 번째 d의 배수
        start = max(d * 2, ((begin + d - 1) // d) * d)

        for x in range(start, end + 1, d):
            answer[x - begin] = d

    if begin == 1:
        answer[0] = 0

    return answer