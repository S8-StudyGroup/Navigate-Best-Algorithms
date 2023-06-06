# [BOJ] 17143. 낚시왕
# 소요 시간 : 00분


def get_shark():
    shark_size = 0
    for i in range(R):
        if matrix[r][c]:
            total_shark_size += sharks[matrix[r][c][0]][4]
            del sharks[matrix[r][c][0]]
            matrix[r][c] = []
            break
    
    return shark_size


R, C, M = map(int, input().split())
matrix = [[[] for _ in range(C)] for _ in range(R)]
sharks = {}
total_shark_size = 0

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    matrix[r][c].append(i)
    sharks[i] = [s, d, z]

for king_idx in range(C):
    get_shark()
    
