# [BOJ] 15683. 감시
# 소요 시간 : 00분
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
# 상하좌우
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
cctv_dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]],
    3: [[0, 2], [0, 3], [1, 2], [1, 3]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}
cctv_list = []

for row in range(n):
    for col in range(m):
        if matrix[row][col] != 0 and matrix[row][col] != 6:
            cctv_list.append([row, col, matrix[row][col]])

min_blind_spot = float('inf')


def dfs(idx, matrix):
    global min_blind_spot

    # 종료 조건
    if idx == len(cctv_list):
        cnt = 0
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    cnt += 1
        min_blind_spot = min(min_blind_spot, cnt)
        return

    row, col, cctv_num = cctv_list[idx]
    for d in cctv_dir[cctv_num]:
        temp = [matrix[r][:] for r in range(n)]
        for i in d:
            nr = row + dir[i][0]
            nc = col + dir[i][1]
            while 0 <= nr < n and 0 <= nc < m:
                if temp[nr][nc] == 6:
                    break
                if temp[nr][nc] == 0:
                    temp[nr][nc] = '#'
                nr += dir[i][0]
                nc += dir[i][1]
        dfs(idx + 1, temp)


dfs(0, matrix)

print(min_blind_spot)
