def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        if (100 - progresses[i])%speeds[i] == 0:
            value = (100 - progresses[i])//speeds[i]
        else:
            value = ((100 - progresses[i])//speeds[i])+1
        days.append(value)
        
    max = days.pop(0)
    count = 1
    while days:
        a1 = days.pop(0)
        if a1 <= max:
            count+=1
        else:
            max = a1
            answer.append(count)
            count=1
    answer.append(count)
    return answer