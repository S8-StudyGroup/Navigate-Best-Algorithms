# [BOJ] 1890. 점프
# 소요 시간 : 10분

# dp를 순회하면서 오른쪽과 아래쪽으로 갈 수 있는지 확인
# 갈 수 있다면 가려는 곳에 현재 위치의 dp값을 더해준다!

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):

        if i == N - 1 and j == N - 1:
            continue

        if dp[i][j] > 0:
            if i + matrix[i][j] < N:
                dp[i + matrix[i][j]][j] += dp[i][j]
            if j + matrix[i][j] < N:
                dp[i][j + matrix[i][j]] += dp[i][j]

print(dp[N - 1][N - 1])
