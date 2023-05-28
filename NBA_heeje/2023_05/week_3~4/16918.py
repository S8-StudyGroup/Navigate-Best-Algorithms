# [BOJ] 16918. 봄버맨
# 소요 시간 : 00분

R, C, N = map(int, input().split())
matrix = [input() for _ in range(R)]


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

first_matrix = [["O"] * C for _ in range(R)]

for y in range(R):
    for x in range(C):
        if matrix[y][x] == "O":
            first_matrix[y][x] = "."
            for d in range(4):
                move_y, move_x = y + dy[d], x + dx[d]
                if 0 <= move_y < R and 0 <= move_x < C:
                    first_matrix[move_y][move_x] = "."

second_matrix = [["O"] * C for _ in range(R)]

for y in range(R):
    for x in range(C):
        if first_matrix[y][x] == "O":
            second_matrix[y][x] = "."
            for d in range(4):
                move_y, move_x = y + dy[d], x + dx[d]
                if 0 <= move_y < R and 0 <= move_x < C:
                    second_matrix[move_y][move_x] = "."

# N이 1일 때 그대로 출력
if N == 1:
    for i in range(R):
        print(matrix[i])

elif N % 2 == 0:
    for i in range(R):
        print("O" * C)

elif N % 4 == 3:
    for i in range(R):
        print("".join(first_matrix[i]))

else:
    for i in range(R):
        print("".join(second_matrix[i]))


# R, C, N = map(int, input().split())
# matrix = [input() for _ in range(R)]

# # N을 4으로 나눈 나머지가 1일 땐 현재 격자판 그대로 출력
# if N % 4 == 1:
#     for i in range(R):
#         print(matrix[i])

# # N이 4로 나눈 나머지가 3이라면
# # 폭탄이 터진 자리를 제외한 다른 부분이 "O"가 된 상태의 격자판 출력
# elif N % 4 == 3:
#     dy = [-1, 0, 1, 0]
#     dx = [0, -1, 0, 1]
#     bomb_set = set()

#     first_matrix = [["O"] * C for _ in range(R)]

#     for y in range(R):
#         for x in range(C):
#             if matrix[y][x] == "O":
#                 first_matrix[y][x] = "."
#                 for d in range(4):
#                     move_y, move_x = y + dy[d], x + dx[d]
#                     if 0 <= move_y < R and 0 <= move_x < C:
#                         first_matrix[move_y][move_x] = "."
    
#     for i in range(R):
#         print("".join(first_matrix[i]))

# # N이 4로 나누어 떨어진다면
# # 격자판을 폭탄으로 채워서 출력
# else:
#     for i in range(R):
#         print("O" * C)
    
    
    