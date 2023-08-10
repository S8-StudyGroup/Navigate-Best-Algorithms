# [BOJ] 15683. 감시
# 소요 시간 : 90분

# 1번: 한방향
# 2번: 반대 두 방향
# 3번: 직각 두 방향
# 4번: 화살표 세 방향
# 5번: 네 방향
# 각 자리의 cctv 위치 정하고 표시하기!!

import copy
N, M = map(int, input().split())
board = []
ans = N * M
cctv = []
move = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j] in [1, 2, 3, 4, 5]:
            cctv.append([temp[j], i, j])
    board.append(temp)


def watch(grid, ds, x, y):
    for d in ds:
        ni = x + di[d]
        nj = y + dj[d]
        while 0 <= ni < N and 0 <= nj < M:
            if grid[ni][nj] == 0:
                grid[ni][nj] = 7
            elif grid[ni][nj] == 6:
                break
            ni += di[d]
            nj += dj[d]


def dfs(depth, array):
    global ans
    if depth == len(cctv):
        cnt = 0
        for a in range(N):
            for b in range(M):
                if array[a][b] == 0:
                    cnt += 1
        ans = min(cnt, ans)
        return
    temp_array = copy.deepcopy(array)
    c_num, a, b = cctv[depth]
    for direction in move[c_num]:
        watch(temp_array, direction, a, b)
        dfs(depth + 1, temp_array)
        temp_array = copy.deepcopy(array)


dfs(0, board)
print(ans)



