# [BOJ] 20056. 마법사 상어와 파이어볼
# 소요 시간 : 00분
import sys
input = sys.stdin.readline

# 1. 모든 파이어볼이 자신의 방향 d로 속력 s칸 만큼 이동하는 함수
def move_fireball():
    for idx, fireball in enumerate(fireball_info):
        r, c, m, s, d = fireball
        move_r, move_c = (r + dr[d] * s) % N, (c + dc[d] * s) % N
        fireball_info[idx] = (move_r, move_c, m, s, d)
        matrix[move_r][move_c].append(idx)

# 2. 이동이 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서 일어나는 일들을 담은 함수
def divide_fireball():
    new_fireball_info = []
    for y in range(N):
        for x in range(N):

            # 2개 이상의 파이어볼이 있는 칸일 경우
            if len(matrix[y][x]) > 1:
                divided_m, divided_s = 0, 0
                odd_dir_list = []
                for idx in matrix[y][x]:
                    r, c, m, s, d = fireball_info[idx]
                    divided_m += m
                    divided_s += s
                    odd_dir_list.append(d % 2 == 1)
                
                # 질량이 0이 될 파이어볼은 소멸
                if divided_m < 5:
                    continue
                
                # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 짝수인 경우
                if all(odd_dir_list) or not any(odd_dir_list):
                    divided_d = [0, 2, 4, 6]
                else:
                    divided_d = [1, 3, 5, 7]
                
                divided_m //= 5
                divided_s //= len(matrix[y][x])

                for d in divided_d:
                    new_fireball_info.append((r, c, divided_m, divided_s, d))
            elif len(matrix[y][x]) == 1:
                new_fireball_info.append(fireball_info[matrix[y][x][0]])

            matrix[y][x] = []
    
    return new_fireball_info


N, M, K = map(int, input().split())
matrix = [[[] * N for _ in range(N)] for _ in range(N)]
fireball_info = []

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1, 0]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball_info.append((r - 1, c - 1, m, s, d))
    # matrix[r - 1][c - 1].append(len(fireball_info) - 1)

for _ in range(K):
    move_fireball()
    fireball_info = divide_fireball()

    for y in range(N):
        for x in range(N):
            matrix[y][x] = []

    if not fireball_info:
        break

print(sum([fireball[2] for fireball in fireball_info]))