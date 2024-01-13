def solution(s):
    stack = []
    for ss in s:
        if not stack:
            stack.append(ss)
        else:
            if stack[-1] == ss:
                stack.pop()
            else:
                stack.append(ss)
                
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    return answer