# [BOJ] 30036. INK
# 소요 시간 : 00분

from sys import stdin

input = stdin.readline

command_dict = {
    "U": lambda x, N: [x[0] - 1, x[1]] if 0 <= x[0] - 1 < N and N_stage[x[0] - 1][x[1]] == "." else x,
    "D": lambda x, N: [x[0] + 1, x[1]] if 0 <= x[0] + 1 < N and N_stage[x[0] + 1][x[1]] == "." else x,
    "R": lambda x, N: [x[0], x[1] + 1] if 0 <= x[1] + 1 < N and N_stage[x[0]][x[1] + 1] == "." else x,
    "L": lambda x, N: [x[0], x[1] - 1] if 0 <= x[1] - 1 < N and N_stage[x[0]][x[1] - 1] == "." else x,
    }

I, N, K = map(int,input().strip().split())

I_list = list(input())

N_stage = []
square_loc = []
for i in range(N):
    N_stage.append(list(input().strip()))
    for t in range(N):
        if N_stage[-1][t] == "@":
            square_loc = [i,t]

K_command = list(input().strip())


J_count = 0
ink_amount = 0
for command in K_command:
    if command == "J":
        color = I_list[J_count]
        for i in range(N):
            for j in range(N):
                if N_stage[i][j] not in [".", "@"] and abs(square_loc[0] - i) + abs(square_loc[1] - j) <= ink_amount:
                    N_stage[i][j] = color
        J_count = (J_count + 1) % I
        ink_amount = 0
    elif command == "j":
        ink_amount += 1
    else:
        N_stage[square_loc[0]][square_loc[1]] = "."
        square_loc = command_dict[command](square_loc, N)
        N_stage[square_loc[0]][square_loc[1]] = "@"

for line in N_stage:
    print("".join(line))