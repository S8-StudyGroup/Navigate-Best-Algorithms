# [BOJ] 21610. 마법사 상어와 비바라기
# 소요 시간 : 30분

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]

cloud_list = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

for _ in range(M):
    d, s = map(int, input().split())

    # 1. 모든 구름이 d 방향으로 s 칸 이동한다.
    cloud_list = list(map(lambda x: ((x[0] + dy[d] * s) % N, (x[1] + dx[d] * s) % N), cloud_list))

    # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    for cloud_y, cloud_x in cloud_list:
        matrix[cloud_y][cloud_x] += 1

    # 3. 구름이 모두 사라진다.
    # cloud_list = []
    
    # 4. 2에서 증가한 칸에 물복사버그 마법을 시전한다.
    for cloud_y, cloud_x in cloud_list:
        dia_y = [-1, -1, 1, 1]
        dia_x = [-1, 1, -1, 1]
        for d in range(4):
            move_y, move_x = cloud_y + dia_y[d], cloud_x + dia_x[d]
            if 0 <= move_y < N and 0 <= move_x < N and matrix[move_y][move_x] > 0:
                matrix[cloud_y][cloud_x] += 1
    
    # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    # 이 떄 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    new_cloud_list = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] >= 2 and (i, j) not in cloud_list:
                new_cloud_list.append((i, j))
                matrix[i][j] -= 2
    cloud_list = new_cloud_list

total_water = 0
for i in range(N):
    for j in range(N):
        total_water += matrix[i][j]

print(total_water)