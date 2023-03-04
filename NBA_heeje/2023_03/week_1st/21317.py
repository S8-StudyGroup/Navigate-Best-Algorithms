# [BOJ] 21317. 징검다리 건너기
# 소요 시간 : 시간 초과(60분)

# 각 칸까지의 이동 가능 경로에 필요한 에너지를 구하고, 최솟값을 저장!
# 매우 큰 점프는 한 번 밖에 못한다는 걸 생각해야 함

# 시도 1
# 작은 점프와 큰 점프를 고려하여 dp 실행
# 해당 dp에서 에너지를 가장 많이 소비하는 구간을 매우 큰 점프로 교체
# 단, 매우 큰 점프의 에너지가 해당 구간보다 더 많이 들 수도 있음을 고려

# 시도 2 - 제한 시간 초과하여 풀이 참고
# 에너지를 가장 많이 소비하는 구간을 매우 큰 점프로 교체하는 것만으로는 정확한 답이 나오지 않는다.
# 교체한 후 추가적인 dp 계산을 진행해야 한다.

N = int(input())


bridge = []

# bridge에 작은 점프와 큰 점프 에너지 소비량 저장
for _ in range(N - 1):
    bridge.append(list(map(int, input().split())))

# 매우 큰 점프의 에너지
K = int(input())
dp = [0] * N

# N이 
if N > 1:
    dp[1] = bridge[0][0]

for i in range(2, N):
    dp[i] = min(dp[i - 1] + bridge[i - 1][0], dp[i - 2] + bridge[i - 2][1])

# max_used_energy = max([0] + [dp[i + 3] - dp[i] for i in range(len(dp) - 3)])

min_energy = dp[-1]
for i in range(3, N):
    used_energy_in_section, dp1, dp2 = dp[i - 3] + K, 1e9, 1e9
    for j in range(i, N - 1):
        if i + 1 <= N:
            dp1 = min(dp1, used_energy_in_section + bridge[j][0])
        if i + 2 <= N:
            dp2 = min(dp2, used_energy_in_section + bridge[j][1])
        used_energy_in_section, dp1, dp2 = dp1, dp2, 1e9
    min_energy = min(min_energy, used_energy_in_section)


print(min_energy)
