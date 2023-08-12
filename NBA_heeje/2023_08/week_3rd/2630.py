# [BOJ] 2630. 색종이 만들기
# 소요 시간 : 10분

import sys
input = sys.stdin.readline

def dfs(y, x, n):
    sum = 0
    for i in range(y, y + n):
        for j in range(x, x + n):
            sum += paper[i][j]
    
    if sum == 0:
        cnt_paper[0] += 1
    elif sum == n ** 2:
        cnt_paper[1] += 1
    else:
        for i in [y, y + (n // 2)]:
            for j in [x, x + (n // 2)]:
                dfs(i, j, n // 2)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
cnt_paper = [0, 0]
dfs(0, 0, N)

print(*cnt_paper, sep="\n")