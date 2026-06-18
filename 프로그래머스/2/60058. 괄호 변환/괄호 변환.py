def check(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True
    
def solution(w):
    answer = ''
    open_s, close_s = 0,0
    # step1
    if len(w)==0:
        return answer
    # step2
    for i in range(len(w)):
        if w[i] == '(':
            open_s+=1
        else:
            close_s+=1
        if open_s==close_s:
            u = w[:i+1]
            v = w[i+1:]
            break
    # step3
    if check(u):
        return u+solution(v)
    # step4
    else:
        answer+='('
        answer+=solution(v)
        answer += ')'
        a = ''.join([')' if j=='(' else '(' for j in u[1:-1]])
        answer+=a
    return answer