# [BOJ] 9663. N-Queen
# 소요 시간 : 30분

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(depth):
    if depth == N:
        global cnt
        cnt += 1
        return

    for i in range(N):
        if matrix[depth][i] == 0:
            matrix[depth][i] = 2
            change_list = []
            for d in range(8):
                move_x, move_y = depth + dx[d], i + dy[d]
                while 0 <= move_x < N and 0 <= move_y < N:
                    if matrix[move_x][move_y] == 0:
                        matrix[move_x][move_y] = 1
                        change_list.append((move_x, move_y))
                    move_x += dx[d]
                    move_y += dy[d]
            dfs(depth + 1)
            for move_x, move_y in change_list:
                matrix[move_x][move_y] = 0
            matrix[depth][i] = 0


N = int(input())
matrix = [[0] * N for _ in range(N)]
cnt = 0
dfs(0)

print(cnt)