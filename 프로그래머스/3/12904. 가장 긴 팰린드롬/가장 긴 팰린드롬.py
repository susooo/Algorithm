def solution(s):
    answer = 1

    def expand(left,right):

        while left>=0 and right<len(s):

            if s[left]!=s[right]:
                break

            left-=1
            right+=1

        return right-left-1
                
    for i in range(len(s)-1):    
        answer = max(answer, expand(i,i))
        if s[i] == s[i+1]:
            answer = max(answer, expand(i,i+1))

    return answer