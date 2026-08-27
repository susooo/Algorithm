def solution(n):
    answer = []
    
    def hanoi(n, curr, nxt, sub): #sub는 옮겨둘 보조 기둥
        if n == 1:
            answer.append([curr, nxt])
            return

        hanoi(n - 1, curr, sub, nxt)
        answer.append([curr, nxt])
        hanoi(n - 1, sub, nxt, curr)

    hanoi(n, 1, 3, 2)

    return answer