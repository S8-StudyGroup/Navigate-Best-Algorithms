# [BOJ] 17822. 원판 돌리기
# 소요 시간 : 00분
import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
disks = [list(map(int, input().split())) for _ in range(n)]
rotations = [list(map(int, input().split())) for _ in range(t)]

for x, d, k in rotations:
    for i in range(x, n+1, x):
        if d == 0:
            disks[i-1] = disks[i-1][-k:] + disks[i-1][:-k]
        else:
            disks[i-1] = disks[i-1][k:] + disks[i-1][:k]

    # 인접한 수가 같은 것을 찾아서 지우기
    adj = []
    for i in range(n):
        for j in range(m):
            if disks[i][j] == 0:
                continue
            if disks[i][j] == disks[i][(j+1) % m]:
                adj.append((i, j))
            if disks[i][j] == disks[i][(j-1) % m]:
                adj.append((i, j))
            if i > 0 and disks[i][j] == disks[i-1][j]:
                adj.append((i, j))
            if i < n-1 and disks[i][j] == disks[i+1][j]:
                adj.append((i, j))

    if adj:
        for i, j in adj:
            disks[i][j] = 0
    else:
        total_sum = 0
        total_cnt = 0
        for i in range(n):
            for j in range(m):
                if disks[i][j] == 0:
                    continue
                total_sum += disks[i][j]
                total_cnt += 1

        if total_cnt:
            avg = total_sum / total_cnt
            for i in range(n):
                for j in range(m):
                    if disks[i][j] == 0:
                        continue
                    if disks[i][j] > avg:
                        disks[i][j] -= 1
                    elif disks[i][j] < avg:
                        disks[i][j] += 1


answer = sum(map(sum, disks))

print(answer)
