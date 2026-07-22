def solution(n, cores):

    if n <= len(cores):
        return n

    left = 0
    right = max(cores) * n

    while left < right:
        mid = (left + right) // 2

        cnt = 0 #시간 t일 때 처리한 작업 개수
        for c in cores:
            cnt += mid // c + 1

        if cnt < n:
            left = mid + 1
        else:
            right = mid

    time = left

    done = 0
    for c in cores:
        done += (time - 1) // c + 1 # t-1까지 완료한 작업 개수 구하기

    for i, c in enumerate(cores): #t시간 때 순서대로 처리하며 n번째 찾기
        if time % c == 0:
            done += 1
            if done == n:
                return i + 1