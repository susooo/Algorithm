def solution(s):
    answer = []
    s_list = s[2:-2].split('},{')
    s_list.sort(key = len)
    for i in s_list:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
    return answer