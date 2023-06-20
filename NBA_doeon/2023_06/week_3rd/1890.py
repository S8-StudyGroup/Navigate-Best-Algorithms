# [BOJ] 1890. 점프
# 소요 시간 : 00분

def paint_dp(x, y):
    move_cnt = board[x][y]  # 현재 칸의 이동 가능 횟수

    nx1, ny1 = x + move_cnt, y  # 아래로 이동한 경우
    nx2, ny2 = x, y + move_cnt  # 오른쪽으로 이동한 경우

    if 0 <= nx1 < n:
        # list 범위 안으로 통과하면 dp에 해당 값 더해주기 작업
        dp[nx1][ny1] += dp[x][y]

    if 0 <= ny2 < n:
        dp[nx2][ny2] += dp[x][y]

n = int(input())
board = []
for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)

dp = [[0] * n for _ in range(n)]    # (i, j)까지 도착 가능한 경로의 수로 채워진 이차원배열 dp

dp[0][0] = 1    # 출발점까지 갈 수 있는 경우는 무조건 1

for i in range(n):
    for j in range(n):
        if board[i][j]: # 0인 마지막 칸은 제외하고 DP 배열 채우는 함수 실행
            paint_dp(i, j)

print(dp[n-1][n-1])
