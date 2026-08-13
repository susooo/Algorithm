def solution(target):
    
    scores = []
    for i in range(1, 21):
        scores.append((i, 1))       # 싱글: 점수 i, 싱글카운트 1
        scores.append((i*2, 0))     # 더블: 점수 i*2, 싱글카운트 0
        scores.append((i*3, 0))     # 트리플: 점수 i*3, 싱글카운트 0
    scores.append((50, 1))          # 불: 점수 50, 싱글카운트 1
    
    INF = float('inf')
    dp = [(INF, 0)] * (target + 1)
    dp[0] = (0, 0)

    for i in range(1, target + 1):
        for score, is_single in scores:
            if i - score < 0:
                continue
                
            prev_darts, prev_single = dp[i - score]
            if prev_darts == INF:
                continue

            new_darts = prev_darts + 1
            new_single = prev_single + is_single

            # 다트 수 적으면 갱신, 같으면 싱글 많은 걸로
            if new_darts < dp[i][0] or (new_darts == dp[i][0] and new_single > dp[i][1]):
                dp[i] = (new_darts, new_single)

    return list(dp[target])
