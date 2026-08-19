def solution(beginning, target):
    n, m = len(beginning), len(beginning[0])
    
    def check(first_row_flip):
        board = [row[:] for row in beginning]
        cnt = 0

        # 첫 번째 행을 뒤집을지 결정
        if first_row_flip:
            cnt += 1
            for j in range(m):
                board[0][j] ^= 1

        # 첫 번째 행을 기준으로 열 뒤집기 결정
        for j in range(m):
            if board[0][j] != target[0][j]:
                cnt += 1

                for i in range(n):
                    board[i][j] ^= 1

        # 첫 번째 열을 기준으로 행 뒤집기 결정
        for i in range(n):
            if board[i][0] != target[i][0]:
                cnt += 1

                for j in range(m):
                    board[i][j] ^= 1

        # 완성됐는지 확인
        if board == target:
            return cnt

        return float('inf')

    answer = min(
        check(False),
        check(True)
    )

    return -1 if answer == float('inf') else answer