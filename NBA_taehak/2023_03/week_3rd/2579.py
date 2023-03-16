# [BOJ] 2579. 계단 오르기
# 소요 시간 : 00분

# 입력값 : 300개 이하 계단 개수, 10000이하 점수
stair_cnt = int(input())
scores = [int(input()) for _ in range(stair_cnt)]

# dp : [한칸한칸올라서 온 경우, 두칸한칸올라서 온경우, (1, 2)칸두칸올라서 온 경우],...
# dp : [두칸 올라야함, 한칸 올라서 한칸한칸으로/ 두칸올라서 두칸으로, 한칸 올라서 두칸한칸으로/ 두칸 올라서 두칸으로]
dp = [[0, 0, 0] for _ in range(stair_cnt + 2)]

idx = 0
for idx in range(stair_cnt):
    case1, case2, case3 = dp[idx]

    dp[idx + 1][0] = max(dp[idx + 1][0], case2 + scores[idx + 1])