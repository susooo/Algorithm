def solution(s):
    answer = ''
    now = ' '
    for i in range(len(s)):
        ss = s[i]
        if now.isspace():
            if s[i].isalpha():
                ss = s[i].upper()    
        else:
            if s[i].isalpha():
                ss = s[i].lower()
        now = s[i]
        answer+=ss
    return answer
                