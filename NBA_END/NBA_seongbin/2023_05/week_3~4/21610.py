# [BOJ] 21610. 마법사 상어와 비바라기
# 소요 시간 : 00분
import sys
input = sys.stdin.readline

# 1. 구름 이동
# 2. 물복사 버그
# 3. 새로운 구름 생성

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
move = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

# 구름 이동


def move_cloud(cloud: list, d: int, s: int):
    moved_cloud = []
    for _ in range(len(cloud)):
        r, c = cloud.pop()
        nr = (r + move[d][0] * s) % N
        nc = (c + move[d][1] * s) % N
        matrix[nr][nc] += 1
        moved_cloud.append((nr, nc))
    return moved_cloud

# 물복사 버그


def water_copy_bug(cloud: list):
    for r, c in cloud:
        cnt = 0
        for i in range(1, 8, 2):
            nr = r + move[i][0]
            nc = c + move[i][1]
            if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc]:
                cnt += 1
        matrix[r][c] += cnt


# 새로운 구름 생성
def generate_cloud(prev_cloud: list):
    cloud = []
    for r in range(N):
        for c in range(N):
            if matrix[r][c] >= 2 and (r, c) not in prev_cloud:
                matrix[r][c] -= 2
                cloud.append((r, c))
    return cloud


# 바구니의 물의 합
def print_matrix_sum(matrix: list):
    total = 0
    for row in matrix:
        total += sum(row)
    print(total)


for _ in range(M):
    d, s = map(int, input().split())
    d -= 1

    moved_cloud = move_cloud(cloud, d, s)

    water_copy_bug(moved_cloud)

    cloud = generate_cloud(moved_cloud)

print_matrix_sum(matrix)
