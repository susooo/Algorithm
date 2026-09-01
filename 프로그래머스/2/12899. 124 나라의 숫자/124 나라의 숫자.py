def solution(n):   
        
    answer = []
    while n > 0:
        n -= 1

        remainder = n % 3
        answer.append(['1', '2', '4'][remainder])

        n //= 3

    return ''.join(answer[::-1])