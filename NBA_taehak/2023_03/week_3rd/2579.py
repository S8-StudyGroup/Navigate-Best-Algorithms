# [BOJ] 2579. 계단 오르기
# 소요 시간 : 00분

# 입력값 : 300개 이하 계단 개수, 10000이하 점수
stair_cnt = int(input())
scores = [int(input()) for _ in range(stair_cnt)]
scores = scores + [0]

# dp : [한칸 올라서 온 경우, 두칸 올라서 온 경우],...
dp = [[0, 0] for _ in range(stair_cnt + 1)]
dp[0] = [scores[0], scores[0]]
dp[1][1] = scores[1]

for idx in range(stair_cnt - 1):
    case1, case2 = dp[idx]
    dp[idx + 1][0] = case2 + scores[idx + 1]
    dp[idx + 2][1] = max(dp[idx + 2][1], case1 + scores[idx + 2], case2 + scores[idx + 2])

print(max(dp[stair_cnt - 1]))