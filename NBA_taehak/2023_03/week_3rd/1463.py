# [BOJ] 1463. 1로 만들기
# 소요 시간 : 00분
X = int(input())
DP = {num : 1e9 for num in range(1, X + 1)}
DP[1] = 0

num = 1
for num in range(1, X):
    cnt_now = DP[num]
    if num * 3 <= X:
        DP[num * 3] = min(cnt_now + 1, DP[num * 3])
    if num * 2 <= X:
        DP[num * 2] = min(cnt_now + 1, DP[num * 2])
    DP[num + 1] = min(cnt_now + 1, DP[num + 1])

print(DP[X])